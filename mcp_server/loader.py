"""
Model Layer: Load and clean incidents and arrestee CSV files
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime
import re

logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self, incidents_path: str, arrestee_path: str):
        """
        Initialize DataLoader with paths to CSV files
        
        Args:
            incidents_path: Path to incidents.csv file
            arrestee_path: Path to arrestee.csv file
        """
        self.incidents_path = incidents_path
        self.arrestee_path = arrestee_path
        self.incidents_df = None
        self.arrestee_df = None
        self.incidents_cleaned = False
        self.arrestee_cleaned = False
    
    def load_incidents(self, sample_size: Optional[int] = None) -> pd.DataFrame:
        """Load incidents data with optional sampling"""
        try:
            if sample_size:
                # Read in chunks for large files
                chunks = []
                chunk_size = min(sample_size * 2, 10000)  # Read more than needed to ensure good sample
                
                for chunk in pd.read_csv(self.incidents_path, chunksize=chunk_size):
                    chunks.append(chunk)
                    if len(chunks) * chunk_size >= sample_size:
                        break
                
                self.incidents_df = pd.concat(chunks, ignore_index=True)
                if len(self.incidents_df) > sample_size:
                    self.incidents_df = self.incidents_df.sample(n=sample_size, random_state=42)
            else:
                self.incidents_df = pd.read_csv(self.incidents_path)
            
            logger.info(f"Loaded incidents data: {len(self.incidents_df)} records, {len(self.incidents_df.columns)} columns")
            return self.incidents_df
            
        except Exception as e:
            logger.error(f"Error loading incidents data: {e}")
            raise
    
    def load_arrestee(self, sample_size: Optional[int] = None) -> pd.DataFrame:
        """Load arrestee data with optional sampling"""
        try:
            if sample_size:
                # Read in chunks for large files
                chunks = []
                chunk_size = min(sample_size * 2, 10000)
                
                for chunk in pd.read_csv(self.arrestee_path, chunksize=chunk_size):
                    chunks.append(chunk)
                    if len(chunks) * chunk_size >= sample_size:
                        break
                
                self.arrestee_df = pd.concat(chunks, ignore_index=True)
                if len(self.arrestee_df) > sample_size:
                    self.arrestee_df = self.arrestee_df.sample(n=sample_size, random_state=42)
            else:
                self.arrestee_df = pd.read_csv(self.arrestee_path)
            
            logger.info(f"Loaded arrestee data: {len(self.arrestee_df)} records, {len(self.arrestee_df.columns)} columns")
            return self.arrestee_df
            
        except Exception as e:
            logger.error(f"Error loading arrestee data: {e}")
            raise
    
    def clean_incidents_data(self) -> pd.DataFrame:
        """Clean and standardize incidents data"""
        if self.incidents_df is None:
            self.load_incidents()
        
        df = self.incidents_df.copy()
        
        # Standardize column names
        df.columns = [self._standardize_column_name(col) for col in df.columns]
        
        # Parse date columns
        date_columns = ['incident_date', 'submission_date', 'cleared_except_date']
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Convert numeric columns
        numeric_columns = ['incident_id', 'agency_id', 'offense_id', 'offense_code', 
                          'location_id', 'num_premises_entered', 'method_entry_code',
                          'offender_id', 'offender_age_num', 'victim_id', 'victim_age_num',
                          'property_id', 'property_loss_id', 'stolen_count', 'recovered_count',
                          'population', 'male_officer', 'male_civilian', 'female_officer', 'female_civilian']
        
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Handle boolean flags
        flag_columns = ['cargo_theft_flag', 'report_date_flag', 'ct_flag', 'hc_flag', 'suburban_area']
        for col in flag_columns:
            if col in df.columns:
                df[col] = df[col].map({'t': True, 'f': False, 'T': True, 'F': False}).fillna(False)
        
        # Clean categorical variables
        categorical_columns = ['attempt_complete_flag', 'crime_against', 'offense_category_name',
                             'victim_type_name', 'assignment_type_name', 'agency_name', 
                             'agency_type_name', 'population_group_desc', 'county_name']
        
        for col in categorical_columns:
            if col in df.columns:
                df[col] = df[col].astype('category')
        
        self.incidents_df = df
        self.incidents_cleaned = True
        
        logger.info("Incidents data cleaned and standardized")
        return df
    
    def clean_arrestee_data(self) -> pd.DataFrame:
        """Clean and standardize arrestee data"""
        if self.arrestee_df is None:
            self.load_arrestee()
        
        df = self.arrestee_df.copy()
        
        # Standardize column names
        df.columns = [self._standardize_column_name(col) for col in df.columns]
        
        # Parse date columns
        if 'arrest_date' in df.columns:
            df['arrest_date'] = pd.to_datetime(df['arrest_date'], errors='coerce')
        
        # Convert numeric columns
        numeric_columns = ['arrestee_id', 'incident_id', 'arrestee_seq_num', 'offense_code',
                          'age_id', 'age_num', 'sex_code', 'race_desc', 'ethnicity_name']
        
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Handle boolean flags
        flag_columns = ['multiple_indicator', 'ct_flag', 'hc_flag']
        for col in flag_columns:
            if col in df.columns:
                df[col] = df[col].map({'Y': True, 'N': False, 'y': True, 'n': False, 
                                     't': True, 'f': False, 'T': True, 'F': False}).fillna(False)
        
        # Clean categorical variables
        categorical_columns = ['arrest_type_name', 'offense_category_name', 'crime_against',
                             'race_desc', 'ethnicity_name', 'resident_code', 
                             'under_18_disposition_code', 'weapon_name']
        
        for col in categorical_columns:
            if col in df.columns:
                df[col] = df[col].astype('category')
        
        self.arrestee_df = df
        self.arrestee_cleaned = True
        
        logger.info("Arrestee data cleaned and standardized")
        return df
    
    def _standardize_column_name(self, column_name: str) -> str:
        """Standardize column names to snake_case"""
        # Remove special characters and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9\s_]', '', str(column_name))
        # Replace spaces with underscores
        cleaned = re.sub(r'\s+', '_', cleaned.lower())
        # Remove multiple underscores
        cleaned = re.sub(r'_+', '_', cleaned)
        # Remove leading/trailing underscores
        cleaned = cleaned.strip('_')
        return cleaned
    
    def get_data_summary(self) -> Dict:
        """Get summary statistics for both datasets"""
        summary = {
            'incidents': {
                'loaded': self.incidents_df is not None,
                'cleaned': self.incidents_cleaned,
                'records': len(self.incidents_df) if self.incidents_df is not None else 0,
                'columns': len(self.incidents_df.columns) if self.incidents_df is not None else 0,
                'missing_values': self._get_missing_summary(self.incidents_df) if self.incidents_df is not None else {}
            },
            'arrestee': {
                'loaded': self.arrestee_df is not None,
                'cleaned': self.arrestee_cleaned,
                'records': len(self.arrestee_df) if self.arrestee_df is not None else 0,
                'columns': len(self.arrestee_df.columns) if self.arrestee_df is not None else 0,
                'missing_values': self._get_missing_summary(self.arrestee_df) if self.arrestee_df is not None else {}
            }
        }
        
        return summary
    
    def _get_missing_summary(self, df: pd.DataFrame) -> Dict:
        """Get summary of missing values in a dataframe"""
        if df is None:
            return {}
        
        missing_counts = df.isnull().sum()
        missing_pct = (missing_counts / len(df)) * 100
        
        return {
            'columns_with_missing': int((missing_counts > 0).sum()),
            'total_missing_values': int(missing_counts.sum()),
            'missing_by_column': missing_counts[missing_counts > 0].to_dict(),
            'missing_pct_by_column': missing_pct[missing_pct > 0].to_dict()
        }
    
    def get_paginated_data(self, dataset: str, page: int = 1, page_size: int = 100, 
                          filters: Optional[Dict] = None) -> Dict:
        """Get paginated data with optional filtering"""
        if dataset.lower() == 'incidents':
            df = self.incidents_df
        elif dataset.lower() == 'arrestee':
            df = self.arrestee_df
        else:
            raise ValueError(f"Unknown dataset: {dataset}")
        
        if df is None:
            return {'data': [], 'total': 0, 'page': page, 'page_size': page_size}
        
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
        
        # Convert DataFrame to JSON-safe format
        def safe_json_convert(obj):
            if pd.isna(obj) or pd.isnull(obj) or obj is None:
                return None
            if isinstance(obj, (float, int)):
                if np.isnan(obj) or np.isinf(obj):
                    return None
                return obj
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            return str(obj)
        
        # Convert records to JSON-safe format
        safe_records = []
        for record in page_data.to_dict('records'):
            safe_record = {}
            for key, value in record.items():
                safe_record[key] = safe_json_convert(value)
            safe_records.append(safe_record)
        
        return {
            'data': safe_records,
            'total': total_records,
            'page': page,
            'page_size': page_size,
            'total_pages': (total_records + page_size - 1) // page_size
        } 