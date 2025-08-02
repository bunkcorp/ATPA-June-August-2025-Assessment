"""
Insights Layer: Exploratory Data Analysis and Visualization functions
"""
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class DataInsights:
    def __init__(self, data_protocol):
        """
        Initialize DataInsights with a DataProtocol instance
        
        Args:
            data_protocol: Instance of DataProtocol class
        """
        self.data_protocol = data_protocol
        self.merged_df = None
    
    def get_summary_statistics(self) -> Dict:
        """Get comprehensive summary statistics"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df
        
        summary = {
            'dataset_overview': {
                'total_incidents': len(df),
                'total_arrests': int(df['ARREST'].sum()),
                'arrest_rate': float(df['ARREST'].mean()),
                'unique_agencies': int(df['agency_id'].nunique()),
                'date_range': {
                    'start': str(df['incident_date'].min()) if 'incident_date' in df.columns else None,
                    'end': str(df['incident_date'].max()) if 'incident_date' in df.columns else None
                }
            },
            'arrest_distribution': {
                'arrests': int(df['ARREST'].sum()),
                'no_arrests': int((df['ARREST'] == 0).sum()),
                'multiple_arrests': int((df['arrest_count'] > 1).sum()) if 'arrest_count' in df.columns else 0
            },
            'crime_categories': self._get_crime_category_summary(df),
            'temporal_patterns': self._get_temporal_patterns(df),
            'geographic_patterns': self._get_geographic_patterns(df),
            'data_quality': self._get_data_quality_summary(df)
        }
        
        return summary
    
    def _get_crime_category_summary(self, df: pd.DataFrame) -> Dict:
        """Get summary by crime categories"""
        if 'offense_category_name' not in df.columns:
            return {}
        
        crime_summary = df.groupby('offense_category_name').agg({
            'ARREST': ['count', 'sum', 'mean'],
            'incident_id': 'count'
        }).round(3)
        
        crime_summary.columns = ['total_incidents', 'total_arrests', 'arrest_rate']
        crime_summary = crime_summary.sort_values('arrest_rate', ascending=False)
        
        return crime_summary.to_dict('index')
    
    def _get_temporal_patterns(self, df: pd.DataFrame) -> Dict:
        """Get temporal patterns in the data"""
        patterns = {}
        
        # Hourly patterns
        if 'incident_hour' in df.columns:
            hourly = df.groupby('incident_hour')['ARREST'].agg(['count', 'sum', 'mean']).round(3)
            patterns['hourly'] = hourly.to_dict('index')
        
        # Daily patterns
        if 'incident_date' in df.columns:
            df['day_of_week'] = df['incident_date'].dt.day_name()
            daily = df.groupby('day_of_week')['ARREST'].agg(['count', 'sum', 'mean']).round(3)
            patterns['daily'] = daily.to_dict('index')
        
        # Monthly patterns
        if 'incident_date' in df.columns:
            df['month'] = df['incident_date'].dt.month
            monthly = df.groupby('month')['ARREST'].agg(['count', 'sum', 'mean']).round(3)
            patterns['monthly'] = monthly.to_dict('index')
        
        return patterns
    
    def _get_geographic_patterns(self, df: pd.DataFrame) -> Dict:
        """Get geographic patterns in the data"""
        patterns = {}
        
        # Agency patterns
        if 'agency_name' in df.columns:
            agency_summary = df.groupby('agency_name')['ARREST'].agg(['count', 'sum', 'mean']).round(3)
            agency_summary.columns = ['total_incidents', 'total_arrests', 'arrest_rate']
            patterns['by_agency'] = agency_summary.head(10).to_dict('index')  # Top 10 agencies
        
        # County patterns
        if 'county_name' in df.columns:
            county_summary = df.groupby('county_name')['ARREST'].agg(['count', 'sum', 'mean']).round(3)
            county_summary.columns = ['total_incidents', 'total_arrests', 'arrest_rate']
            patterns['by_county'] = county_summary.to_dict('index')
        
        return patterns
    
    def _get_data_quality_summary(self, df: pd.DataFrame) -> Dict:
        """Get data quality summary"""
        missing_counts = df.isnull().sum()
        missing_pct = (missing_counts / len(df)) * 100
        
        return {
            'total_missing_values': int(missing_counts.sum()),
            'columns_with_missing': int((missing_counts > 0).sum()),
            'worst_missing_columns': missing_pct[missing_pct > 0].nlargest(5).to_dict(),
            'duplicate_incidents': int(df['incident_id'].duplicated().sum()),
            'data_completeness': float((1 - missing_counts.sum() / (len(df) * len(df.columns))) * 100)
        }
    
    def create_arrest_rate_visualization(self) -> Dict:
        """Create arrest rate visualization by crime type"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df
        
        if 'offense_category_name' not in df.columns:
            return {'error': 'Offense category not available'}
        
        # Calculate arrest rates by crime type
        crime_arrest_rates = df.groupby('offense_category_name')['arrest'].agg(['count', 'sum', 'mean']).round(3)
        crime_arrest_rates.columns = ['total_incidents', 'total_arrests', 'arrest_rate']
        crime_arrest_rates = crime_arrest_rates.sort_values('arrest_rate', ascending=False)
        
        # Create bar chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=crime_arrest_rates.index,
            y=crime_arrest_rates['arrest_rate'],
            text=[f"{rate:.1%}" for rate in crime_arrest_rates['arrest_rate']],
            textposition='auto',
            name='Arrest Rate',
            marker_color='lightcoral'
        ))
        
        fig.update_layout(
            title='Arrest Rate by Crime Type',
            xaxis_title='Crime Type',
            yaxis_title='Arrest Rate',
            yaxis_tickformat='.1%',
            height=600,
            showlegend=False
        )
        
        return {
            'plot_data': json.loads(fig.to_json()),
            'summary_data': crime_arrest_rates.to_dict('index')
        }
    
    def create_temporal_analysis(self) -> Dict:
        """Create temporal analysis visualizations"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df
        
        # Create subplots for different temporal patterns
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Arrest Rate by Hour', 'Arrest Rate by Day of Week', 
                          'Arrest Rate by Month', 'Incidents by Hour'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Hourly patterns
        if 'incident_hour' in df.columns:
            hourly_data = df.groupby('incident_hour')['arrest'].agg(['count', 'sum', 'mean']).round(3)
            
            fig.add_trace(
                go.Bar(x=hourly_data.index, y=hourly_data['mean'], name='Arrest Rate'),
                row=1, col=1
            )
            
            fig.add_trace(
                go.Scatter(x=hourly_data.index, y=hourly_data['count'], name='Total Incidents', yaxis='y2'),
                row=2, col=2
            )
        
        # Daily patterns
        if 'incident_date' in df.columns:
            df['day_of_week'] = df['incident_date'].dt.day_name()
            daily_data = df.groupby('day_of_week')['arrest'].agg(['count', 'sum', 'mean']).round(3)
            
            # Reorder days
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            daily_data = daily_data.reindex([day for day in day_order if day in daily_data.index])
            
            fig.add_trace(
                go.Bar(x=daily_data.index, y=daily_data['mean'], name='Arrest Rate'),
                row=1, col=2
            )
        
        # Monthly patterns
        if 'incident_date' in df.columns:
            df['month'] = df['incident_date'].dt.month
            monthly_data = df.groupby('month')['arrest'].agg(['count', 'sum', 'mean']).round(3)
            
            fig.add_trace(
                go.Bar(x=monthly_data.index, y=monthly_data['mean'], name='Arrest Rate'),
                row=2, col=1
            )
        
        fig.update_layout(
            title='Temporal Analysis of Arrest Patterns',
            height=800,
            showlegend=False
        )
        
        return {
            'plot_data': json.loads(fig.to_json()),
            'temporal_summary': self._get_temporal_patterns(df)
        }
    
    def create_correlation_analysis(self) -> Dict:
        """Create correlation analysis for numerical variables"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df
        
        # Select numerical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in ['incident_id', 'arrestee_id']]
        
        if len(numerical_cols) < 2:
            return {'error': 'Insufficient numerical variables for correlation analysis'}
        
        # Calculate correlation matrix
        corr_matrix = df[numerical_cols].corr()
        
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0
        ))
        
        fig.update_layout(
            title='Correlation Matrix of Numerical Variables',
            height=600
        )
        
        # Get top correlations with arrest
        if 'arrest' in corr_matrix.columns:
            arrest_correlations = corr_matrix['arrest'].abs().sort_values(ascending=False)
            top_correlations = arrest_correlations.head(10).to_dict()
        else:
            top_correlations = {}
        
        return {
            'plot_data': json.loads(fig.to_json()),
            'correlation_matrix': corr_matrix.to_dict(),
            'top_arrest_correlations': top_correlations
        }
    
    def create_feature_importance_analysis(self) -> Dict:
        """Create feature importance analysis for predicting arrests"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df.copy()
        
        # Prepare features for analysis
        feature_cols = []
        
        # Numerical features
        numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in ['incident_id', 'arrestee_id', 'arrest', 'arrest_count']]
        feature_cols.extend(numerical_cols)
        
        # Categorical features (one-hot encode)
        categorical_cols = ['offense_category_name', 'crime_against', 'agency_name', 'county_name']
        for col in categorical_cols:
            if col in df.columns:
                dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
                df = pd.concat([df, dummies], axis=1)
                feature_cols.extend(dummies.columns.tolist())
        
        # Remove rows with missing values
        df_clean = df[feature_cols + ['arrest']].dropna()
        
        if len(df_clean) < 100:
            return {'error': 'Insufficient data after cleaning for feature importance analysis'}
        
        # Calculate correlation with arrest
        correlations = df_clean[feature_cols].corrwith(df_clean['arrest']).abs().sort_values(ascending=False)
        
        # Create bar chart of feature importance
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=correlations.head(15).index,
            y=correlations.head(15).values,
            marker_color='lightblue'
        ))
        
        fig.update_layout(
            title='Feature Importance for Arrest Prediction (Correlation with Arrest)',
            xaxis_title='Features',
            yaxis_title='Absolute Correlation with Arrest',
            height=600
        )
        
        return {
            'plot_data': json.loads(fig.to_json()),
            'feature_importance': correlations.head(20).to_dict(),
            'analysis_summary': {
                'total_features_analyzed': len(feature_cols),
                'records_used': len(df_clean),
                'top_features': correlations.head(10).index.tolist()
            }
        }
    
    def get_reasonability_checks(self) -> Dict:
        """Perform reasonability checks on the data"""
        if not self.data_protocol.merged_created:
            return {'error': 'Merged dataset not created yet'}
        
        df = self.data_protocol.merged_df
        
        checks = {
            'data_volume': {
                'total_incidents': len(df),
                'total_arrests': int(df['ARREST'].sum()),
                'arrest_rate': float(df['ARREST'].mean()),
                'reasonability': 'Reasonable' if 0.01 <= df['ARREST'].mean() <= 0.5 else 'Check needed'
            },
            'date_ranges': {
                'incident_date_range': {
                    'min': str(df['incident_date'].min()) if 'incident_date' in df.columns else None,
                    'max': str(df['incident_date'].max()) if 'incident_date' in df.columns else None
                },
                'reasonability': 'Reasonable' if 'incident_date' in df.columns and df['incident_date'].min() >= pd.Timestamp('2020-01-01') else 'Check needed'
            },
            'outliers': self._check_for_outliers(df),
            'missing_data': self._check_missing_data(df),
            'logical_consistency': self._check_logical_consistency(df)
        }
        
        return checks
    
    def _check_for_outliers(self, df: pd.DataFrame) -> Dict:
        """Check for outliers in numerical columns"""
        outliers = {}
        
        numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in ['incident_id', 'arrestee_id']]
        
        for col in numerical_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outlier_count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            outlier_pct = (outlier_count / len(df)) * 100
            
            if outlier_pct > 5:  # Flag if more than 5% outliers
                outliers[col] = {
                    'outlier_count': int(outlier_count),
                    'outlier_percentage': float(outlier_pct),
                    'status': 'High outliers detected'
                }
        
        return outliers
    
    def _check_missing_data(self, df: pd.DataFrame) -> Dict:
        """Check for missing data patterns"""
        missing_counts = df.isnull().sum()
        missing_pct = (missing_counts / len(df)) * 100
        
        high_missing = missing_pct[missing_pct > 20].to_dict()
        
        return {
            'columns_with_high_missing': high_missing,
            'total_missing_values': int(missing_counts.sum()),
            'overall_completeness': float((1 - missing_counts.sum() / (len(df) * len(df.columns))) * 100)
        }
    
    def _check_logical_consistency(self, df: pd.DataFrame) -> Dict:
        """Check for logical consistency issues"""
        issues = {}
        
        # Check if arrest date is before incident date
        if 'arrest_date' in df.columns and 'incident_date' in df.columns:
            invalid_dates = (df['arrest_date'] < df['incident_date']).sum()
            if invalid_dates > 0:
                issues['arrest_before_incident'] = int(invalid_dates)
        
        # Check for negative ages
        age_cols = ['victim_age_num', 'offender_age_num', 'age_num']
        for col in age_cols:
            if col in df.columns:
                negative_ages = (df[col] < 0).sum()
                if negative_ages > 0:
                    issues[f'negative_{col}'] = int(negative_ages)
        
        # Check for impossible hours
        if 'incident_hour' in df.columns:
            invalid_hours = ((df['incident_hour'] < 0) | (df['incident_hour'] > 23)).sum()
            if invalid_hours > 0:
                issues['invalid_incident_hours'] = int(invalid_hours)
        
        return issues 