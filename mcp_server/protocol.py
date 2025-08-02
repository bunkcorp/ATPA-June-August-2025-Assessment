"""
Protocol Layer: Merge incidents and arrestee datasets and create ARREST target variable
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class DataProtocol:
    def __init__(self, data_loader):
        """
        Initialize DataProtocol with a DataLoader instance
        
        Args:
            data_loader: Instance of DataLoader class
        """
        self.data_loader = data_loader
        self.merged_df = None
        self.merged_created = False
    
    def create_merged_dataset(self, sample_size: Optional[int] = None) -> pd.DataFrame:
        """
        Merge incidents and arrestee datasets and create ARREST target variable
        
        Args:
            sample_size: Optional sample size for large datasets
            
        Returns:
            Merged DataFrame with ARREST target variable
        """
        # Ensure data is loaded and cleaned
        if not self.data_loader.incidents_cleaned:
            self.data_loader.clean_incidents_data()
        
        if not self.data_loader.arrestee_cleaned:
            self.data_loader.clean_arrestee_data()
        
        incidents_df = self.data_loader.incidents_df.copy()
        arrestee_df = self.data_loader.arrestee_df.copy()
        
        # Sample data if requested
        if sample_size:
            if len(incidents_df) > sample_size:
                incidents_df = incidents_df.sample(n=sample_size, random_state=42)
            if len(arrestee_df) > sample_size:
                arrestee_df = arrestee_df.sample(n=sample_size, random_state=42)
        
        logger.info(f"Starting merge with {len(incidents_df)} incidents and {len(arrestee_df)} arrestee records")
        
        # Create ARREST target variable
        # An incident has an arrest if it appears in the arrestee dataset
        incidents_df['ARREST'] = incidents_df['incident_id'].isin(arrestee_df['incident_id']).astype(int)
        
        # Perform left join to preserve all incidents
        merged_df = incidents_df.merge(
            arrestee_df,
            on='incident_id',
            how='left',
            suffixes=('_incident', '_arrestee')
        )
        
        # Handle multiple arrests per incident
        # For incidents with multiple arrests, we'll keep the first one
        # and add a count of total arrests
        arrest_counts = arrestee_df.groupby('incident_id').size().reset_index(name='arrest_count')
        merged_df = merged_df.merge(arrest_counts, on='incident_id', how='left')
        merged_df['arrest_count'] = merged_df['arrest_count'].fillna(0).astype(int)
        
        # Add derived features
        merged_df = self._add_derived_features(merged_df)
        
        # Clean up duplicate columns and standardize
        merged_df = self._cleanup_merged_data(merged_df)
        
        self.merged_df = merged_df
        self.merged_created = True
        
        logger.info(f"Merged dataset created: {len(merged_df)} records, {len(merged_df.columns)} columns")
        logger.info(f"Arrest rate: {merged_df['ARREST'].mean():.3f} ({merged_df['ARREST'].sum()} arrests out of {len(merged_df)} incidents)")
        
        return merged_df
    
    def _add_derived_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add derived features to the merged dataset"""
        
        # Time-based features
        if 'incident_date' in df.columns and 'arrest_date' in df.columns:
            # Days between incident and arrest
            df['days_to_arrest'] = (df['arrest_date'] - df['incident_date']).dt.days
            df['days_to_arrest'] = df['days_to_arrest'].fillna(-1)  # -1 for no arrest
        
        # Incident hour categories
        if 'incident_hour' in df.columns:
            df['incident_hour_category'] = pd.cut(
                df['incident_hour'],
                bins=[0, 6, 12, 18, 24],
                labels=['Night (0-6)', 'Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)'],
                include_lowest=True
            )
        
        # Age categories for victims and offenders
        age_columns = ['victim_age_num', 'offender_age_num', 'age_num']
        for col in age_columns:
            if col in df.columns:
                df[f'{col}_category'] = pd.cut(
                    df[col],
                    bins=[0, 18, 25, 35, 50, 100],
                    labels=['Under 18', '18-25', '26-35', '36-50', 'Over 50'],
                    include_lowest=True
                )
        
        # Agency size categories
        if 'population' in df.columns:
            df['agency_size'] = pd.cut(
                df['population'],
                bins=[0, 10000, 50000, 100000, 500000, float('inf')],
                labels=['Small (<10K)', 'Medium (10K-50K)', 'Large (50K-100K)', 
                       'Very Large (100K-500K)', 'Major (>500K)'],
                include_lowest=True
            )
        
        # Crime severity (based on crime_against)
        if 'crime_against' in df.columns:
            severity_mapping = {
                'Person': 3,  # Most severe
                'Property': 1,  # Least severe
                'Society': 2   # Medium severity
            }
            df['crime_severity'] = df['crime_against'].map(severity_mapping).fillna(1)
        
        return df
    
    def _cleanup_merged_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean up merged data and handle duplicates"""
        
        # Identify and handle duplicate columns
        duplicate_columns = []
        for col in df.columns:
            if col.endswith('_incident') or col.endswith('_arrestee'):
                base_col = col.replace('_incident', '').replace('_arrestee', '')
                if f'{base_col}_incident' in df.columns and f'{base_col}_arrestee' in df.columns:
                    duplicate_columns.append(base_col)
        
        # For duplicate columns, keep incident version and drop arrestee version
        columns_to_drop = [f'{col}_arrestee' for col in duplicate_columns]
        df = df.drop(columns=columns_to_drop)
        
        # Rename remaining _incident suffixes
        for col in df.columns:
            if col.endswith('_incident'):
                new_col = col.replace('_incident', '')
                df = df.rename(columns={col: new_col})
        
        return df
    
    def get_merged_summary(self) -> Dict:
        """Get summary statistics for the merged dataset"""
        if not self.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.merged_df
        
        summary = {
            'total_records': len(df),
            'total_columns': len(df.columns),
            'arrest_statistics': {
                'total_arrests': int(df['ARREST'].sum()),
                'arrest_rate': float(df['ARREST'].mean()),
                'no_arrest_count': int((df['ARREST'] == 0).sum()),
                'arrest_count_distribution': df['arrest_count'].value_counts().to_dict()
            },
            'data_quality': {
                'missing_values': self._get_missing_summary(df),
                'duplicate_incidents': int(df['incident_id'].duplicated().sum())
            },
            'feature_summary': {
                'categorical_features': self._get_categorical_summary(df),
                'numerical_features': self._get_numerical_summary(df)
            }
        }
        
        return summary
    
    def _get_missing_summary(self, df: pd.DataFrame) -> Dict:
        """Get missing value summary for merged dataset"""
        missing_counts = df.isnull().sum()
        missing_pct = (missing_counts / len(df)) * 100
        
        return {
            'columns_with_missing': int((missing_counts > 0).sum()),
            'total_missing_values': int(missing_counts.sum()),
            'missing_by_column': missing_counts[missing_counts > 0].to_dict(),
            'missing_pct_by_column': missing_pct[missing_pct > 0].to_dict()
        }
    
    def _get_categorical_summary(self, df: pd.DataFrame) -> Dict:
        """Get summary of categorical features"""
        categorical_cols = df.select_dtypes(include=['category', 'object']).columns
        summary = {}
        
        for col in categorical_cols:
            if col != 'incident_id':  # Skip ID columns
                value_counts = df[col].value_counts()
                summary[col] = {
                    'unique_values': int(value_counts.nunique()),
                    'top_values': value_counts.head(5).to_dict(),
                    'missing_count': int(df[col].isnull().sum())
                }
        
        return summary
    
    def _get_numerical_summary(self, df: pd.DataFrame) -> Dict:
        """Get summary of numerical features"""
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        summary = {}
        
        for col in numerical_cols:
            if col != 'incident_id':  # Skip ID columns
                summary[col] = {
                    'mean': float(df[col].mean()),
                    'std': float(df[col].std()),
                    'min': float(df[col].min()),
                    'max': float(df[col].max()),
                    'missing_count': int(df[col].isnull().sum())
                }
        
        return summary
    
    def get_paginated_merged_data(self, page: int = 1, page_size: int = 100, 
                                 filters: Optional[Dict] = None) -> Dict:
        """Get paginated merged data with optional filtering"""
        if not self.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.merged_df.copy()
        
        # Apply filters if provided
        if filters:
            for column, value in filters.items():
                if column in df.columns:
                    if isinstance(value, dict):
                        # Handle range filters
                        if 'min' in value:
                            df = df[df[column] >= value['min']]
                        if 'max' in value:
                            df = df[df[column] <= value['max']]
                    else:
                        # Handle exact match filters
                        df = df[df[column] == value]
        
        # Calculate pagination
        total_records = len(df)
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        
        # Get page data
        page_data = df.iloc[start_idx:end_idx]
        
        return {
            'data': page_data.to_dict('records'),
            'total': total_records,
            'page': page,
            'page_size': page_size,
            'total_pages': (total_records + page_size - 1) // page_size,
            'arrest_rate': float(df['arrest'].mean())
        }
    
    def get_arrest_analysis(self) -> Dict:
        """Get detailed analysis of arrest patterns"""
        if not self.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.merged_df
        
        analysis = {
                          'overall_arrest_rate': float(df['ARREST'].mean()),
              'arrest_by_crime_type': df.groupby('offense_category_name')['ARREST'].agg(['count', 'sum', 'mean']).to_dict('index'),
                          'arrest_by_crime_against': df.groupby('crime_against')['ARREST'].agg(['count', 'sum', 'mean']).to_dict('index'),
              'arrest_by_agency_size': df.groupby('agency_size')['ARREST'].agg(['count', 'sum', 'mean']).to_dict('index') if 'agency_size' in df.columns else {},
                          'arrest_by_hour': df.groupby('incident_hour_category')['ARREST'].agg(['count', 'sum', 'mean']).to_dict('index') if 'incident_hour_category' in df.columns else {},
            'time_to_arrest': {
                        'mean_days': float(df[df['ARREST'] == 1]['days_to_arrest'].mean()) if 'days_to_arrest' in df.columns else None,
        'median_days': float(df[df['ARREST'] == 1]['days_to_arrest'].median()) if 'days_to_arrest' in df.columns else None
            } if 'days_to_arrest' in df.columns else {}
        }
        
        return analysis 