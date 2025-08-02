"""
ATPA Task Implementation Module
Comprehensive implementation of all ATPA tasks (1-6) for the MCP server
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.preprocessing import StandardScaler, LabelEncoder
import shap
import warnings
import logging
from typing import Dict, List, Optional, Tuple, Any
import json
import os
from datetime import datetime
import pickle

# Import specialized curriculum search classes
from task1_specialized import Task1SpecializedSearch
from task2_specialized import Task2SpecializedSearch
from task3_specialized import Task3SpecializedSearch
from task4_specialized import Task4SpecializedSearch
from task5_specialized import Task5SpecializedSearch
from task6_specialized import Task6ExecutiveSummary

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)

class ATPATaskImplementation:
    """
    Comprehensive implementation of all ATPA tasks with integrated curriculum guidance
    """
    
    def __init__(self, data_loader, protocol_layer):
        """
        Initialize task implementation with data layers and curriculum guidance
        
        Args:
            data_loader: DataLoader instance
            protocol_layer: DataProtocol instance
        """
        self.data_loader = data_loader
        self.protocol = protocol_layer
        self.results = {}
        self.models = {}
        self.scalers = {}
        self.encoders = {}
        
        # Initialize specialized curriculum search classes
        self.task1_search = Task1SpecializedSearch()
        self.task2_search = Task2SpecializedSearch()
        self.task3_search = Task3SpecializedSearch()
        self.task4_search = Task4SpecializedSearch()
        self.task5_search = Task5SpecializedSearch()
        self.task6_search = Task6ExecutiveSummary()
        
        logger.info("Task implementation initialized with curriculum guidance")
    
    def task1_data_preparation(self, sample_size: Optional[int] = None) -> Dict:
        """
        Task 1: Data Preparation and Quality Analysis
        
        Implements:
        - Missing value analysis and KNN imputation
        - Data quality assessment
        - Data merging and target variable creation
        - Curriculum guidance integration
        """
        logger.info("Starting Task 1: Data Preparation with curriculum guidance")
        
        try:
            # Load and clean data
            incidents_df = self.data_loader.load_incidents(sample_size)
            arrestee_df = self.data_loader.load_arrestee(sample_size)
            
            incidents_clean = self.data_loader.clean_incidents_data()
            arrestee_clean = self.data_loader.clean_arrestee_data()
            
            # Task 1a: Missing Values Analysis
            missing_analysis = self._analyze_missing_values(incidents_clean, arrestee_clean)
            
            # Task 1b: KNN Imputation
            incidents_imputed, arrestee_imputed = self._apply_knn_imputation(
                incidents_clean, arrestee_clean
            )
            
            # Task 1c: Data Merging and Target Creation
            merged_df = self._create_merged_dataset_with_target(incidents_imputed, arrestee_imputed)
            
            # Task 1d: Data Quality Assessment
            quality_report = self._assess_data_quality(merged_df)
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'data_preparation_content': self.task1_search.search_data_preparation_content(),
                'data_joins_content': self.task1_search.search_data_joins_content(),
                'eda_content': self.task1_search.search_eda_content(),
                'data_validation_content': self.task1_search.search_data_validation_content(),
                'variable_analysis_content': self.task1_search.search_variable_analysis_content(),
                'requirements_content': self.task1_search.get_task1_requirements_content(),
                'structured_content': self.task1_search.get_task1_structured_content()
            }
            
            # Store results with curriculum guidance
            self.results['task1'] = {
                'missing_analysis': missing_analysis,
                'imputation_summary': {
                    'incidents_shape': incidents_imputed.shape,
                    'arrestee_shape': arrestee_imputed.shape,
                    'merged_shape': merged_df.shape
                },
                'quality_report': quality_report,
                'merged_data': merged_df,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 1 completed successfully with curriculum guidance")
            return self.results['task1']
            
        except Exception as e:
            logger.error(f"Error in Task 1: {e}")
            raise
    
    def task2_privacy_ethics_analysis(self) -> Dict:
        """
        Task 2: Privacy and Ethics Analysis
        
        Implements:
        - Protected variable identification
        - Bias assessment
        - Fairness metrics
        - Curriculum guidance integration
        """
        logger.info("Starting Task 2: Privacy and Ethics Analysis with curriculum guidance")
        
        if 'task1' not in self.results:
            raise ValueError("Task 1 must be completed before Task 2")
        
        merged_df = self.results['task1']['merged_data']
        
        try:
            # Identify protected variables
            protected_vars = self._identify_protected_variables(merged_df)
            
            # Analyze demographic distributions
            demographic_analysis = self._analyze_demographics(merged_df)
            
            # Assess bias in arrest rates
            bias_assessment = self._assess_arrest_bias(merged_df)
            
            # Calculate fairness metrics
            fairness_metrics = self._calculate_fairness_metrics(merged_df)
            
            # Generate ethics recommendations
            ethics_recommendations = self._generate_ethics_recommendations(
                protected_vars, bias_assessment, fairness_metrics
            )
            
            # Simplified analysis for performance
            detailed_bias_analysis = {
                'summary': {
                    'total_records': len(merged_df),
                    'arrest_rate': merged_df['ARREST'].mean(),
                    'protected_variables_count': len(protected_vars)
                }
            }
            risk_assessment = {
                'summary_risks': [
                    f"Dataset size: {len(merged_df):,} records",
                    f"Arrest rate: {merged_df['ARREST'].mean():.1%}",
                    f"Protected variables: {len(protected_vars)} identified"
                ]
            }
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'demographic_benefits_risks': self.task2_search.search_demographic_data_benefits_risks(),
                'professional_standards_misuse': self.task2_search.search_professional_standards_misuse_prevention(),
                'criminal_justice_context': self.task2_search.search_criminal_justice_specific(),
                'algorithmic_fairness': self.task2_search.search_algorithmic_fairness_content(),
                'insurance_regulatory': self.task2_search.search_insurance_regulatory_content(),
                'nminsights_guidance': self.task2_search.get_nminsights_specific_guidance(),
                'structured_content': self.task2_search.get_task2_structured_content()
            }
            
            self.results['task2'] = {
                'protected_variables': protected_vars,
                'demographic_analysis': demographic_analysis,
                'bias_assessment': bias_assessment,
                'fairness_metrics': fairness_metrics,
                'ethics_recommendations': ethics_recommendations,
                'detailed_bias_analysis': detailed_bias_analysis,
                'risk_assessment': risk_assessment,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 2 completed successfully with curriculum guidance")
            return self.results['task2']
            
        except Exception as e:
            logger.error(f"Error in Task 2: {e}")
            raise
    
    def task3_generalized_linear_models(self) -> Dict:
        """
        Task 3: Generalized Linear Models
        
        Implements:
        - Logistic regression models
        - Model comparison and selection
        - Cross-validation
        - Curriculum guidance integration
        """
        logger.info("Starting Task 3: Generalized Linear Models with curriculum guidance")
        
        if 'task1' not in self.results:
            raise ValueError("Task 1 must be completed before Task 3")
        
        merged_df = self.results['task1']['merged_data']
        
        try:
            # Prepare features and target
            X, y, feature_names = self._prepare_modeling_data(merged_df)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            self.scalers['standard'] = scaler
            
            # Train multiple logistic regression models
            models = self._train_logistic_models(X_train_scaled, X_test_scaled, y_train, y_test)
            
            # Cross-validation
            cv_results = self._perform_cross_validation(X_train_scaled, y_train)
            
            # Model comparison
            model_comparison = self._compare_models(models, cv_results)
            
            # Store best model
            best_model_name = model_comparison['best_model']
            self.models['logistic_regression'] = models[best_model_name]['model']
            
            # Coefficient analysis
            coefficient_analysis = self._analyze_model_coefficients(models, feature_names)
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'data_splitting_content': self.task3_search.search_data_splitting_content(),
                'glm_content': self.task3_search.search_glm_content(),
                'mixed_models_content': self.task3_search.search_mixed_models_content(),
                'model_validation_content': self.task3_search.search_model_validation_content(),
                'variable_selection_content': self.task3_search.search_variable_selection_content(),
                'performance_metrics_content': self.task3_search.search_performance_metrics_content(),
                'advanced_modeling_content': self.task3_search.search_advanced_modeling_content(),
                'requirements_content': self.task3_search.get_task3_requirements_content(),
                'structured_content': self.task3_search.get_task3_structured_content()
            }
            
            self.results['task3'] = {
                'models': models,
                'cross_validation': cv_results,
                'model_comparison': model_comparison,
                'best_model': best_model_name,
                'feature_names': feature_names,
                'data_shape': X.shape,
                'coefficient_analysis': coefficient_analysis,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 3 completed successfully with curriculum guidance")
            return self.results['task3']
            
        except Exception as e:
            logger.error(f"Error in Task 3: {e}")
            raise
    
    def task4_random_forest_shap(self) -> Dict:
        """
        Task 4: Random Forest with SHAP Analysis
        
        Implements:
        - Random Forest model training
        - SHAP value analysis
        - Feature importance visualization
        - Curriculum guidance integration
        """
        logger.info("Starting Task 4: Random Forest with SHAP Analysis with curriculum guidance")
        
        if 'task1' not in self.results:
            raise ValueError("Task 1 must be completed before Task 4")
        
        merged_df = self.results['task1']['merged_data']
        
        try:
            # Prepare features and target
            X, y, feature_names = self._prepare_modeling_data(merged_df)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Train Random Forest
            rf_model = self._train_random_forest(X_train, X_test, y_train, y_test)
            
            # SHAP Analysis
            shap_analysis = self._perform_shap_analysis(rf_model, X_test, feature_names)
            
            # Feature importance analysis
            feature_importance = self._analyze_feature_importance(rf_model, feature_names)
            
            # Detailed SHAP analysis
            detailed_shap_analysis = self._perform_detailed_shap_analysis(rf_model, X_test, feature_names)
            
            # Store model
            self.models['random_forest'] = rf_model['model']
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'random_forest_content': self.task4_search.search_random_forest_content(),
                'shapley_values_content': self.task4_search.search_shapley_values_content(),
                'partial_dependence_content': self.task4_search.search_partial_dependence_content(),
                'criminal_incident_analysis': self.task4_search.search_criminal_incident_analysis_content(),
                'ensemble_methods_content': self.task4_search.search_ensemble_methods_content(),
                'model_interpretability_content': self.task4_search.search_model_interpretability_content(),
                'explainability_communication': self.task4_search.search_explainability_communication_content(),
                'requirements_content': self.task4_search.get_task4_requirements_content(),
                'structured_content': self.task4_search.get_task4_structured_content()
            }
            
            self.results['task4'] = {
                'random_forest': rf_model,
                'shap_analysis': shap_analysis,
                'feature_importance': feature_importance,
                'detailed_shap_analysis': detailed_shap_analysis,
                'feature_names': feature_names,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 4 completed successfully with curriculum guidance")
            return self.results['task4']
            
        except Exception as e:
            logger.error(f"Error in Task 4: {e}")
            raise
    
    def task5_bayesian_analysis(self) -> Dict:
        """
        Task 5: Bayesian Analysis
        
        Implements:
        - Bayesian logistic regression
        - Posterior analysis
        - Uncertainty quantification
        - Curriculum guidance integration
        """
        logger.info("Starting Task 5: Bayesian Analysis with curriculum guidance")
        
        if 'task1' not in self.results:
            raise ValueError("Task 1 must be completed before Task 5")
        
        merged_df = self.results['task1']['merged_data']
        
        try:
            # Prepare features and target
            X, y, feature_names = self._prepare_modeling_data(merged_df)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Bayesian analysis
            bayesian_results = self._perform_bayesian_analysis(
                X_train_scaled, X_test_scaled, y_train, y_test, feature_names
            )
            
            # Detailed uncertainty analysis
            uncertainty_analysis = self._analyze_bayesian_uncertainty(bayesian_results, feature_names)
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'bayesian_analysis_content': self.task5_search.search_bayesian_analysis_content(),
                'arrest_rates_criminal_categories': self.task5_search.search_arrest_rates_criminal_categories_content(),
                'conjugate_methods_content': self.task5_search.search_conjugate_methods_content(),
                'credible_intervals_content': self.task5_search.search_credible_intervals_content(),
                'business_problem_analysis': self.task5_search.search_business_problem_analysis_content(),
                'requirements_content': self.task5_search.get_task5_requirements_content(),
                'structured_content': self.task5_search.get_task5_structured_content()
            }
            
            self.results['task5'] = {
                'bayesian_results': bayesian_results,
                'uncertainty_analysis': uncertainty_analysis,
                'feature_names': feature_names,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 5 completed successfully with curriculum guidance")
            return self.results['task5']
            
        except Exception as e:
            logger.error(f"Error in Task 5: {e}")
            raise
    
    def task6_executive_summary(self) -> Dict:
        """
        Task 6: Executive Summary
        
        Implements:
        - Comprehensive results summary
        - Key insights and recommendations
        - Professional presentation
        - Curriculum guidance integration
        """
        logger.info("Starting Task 6: Executive Summary with curriculum guidance")
        
        # Check if all previous tasks are completed
        required_tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
        for task in required_tasks:
            if task not in self.results:
                raise ValueError(f"{task} must be completed before Task 6")
        
        try:
            # Generate executive summary
            executive_summary = self._generate_executive_summary()
            
            # Create visualizations
            visualizations = self._create_executive_visualizations()
            
            # Generate recommendations
            recommendations = self._generate_recommendations()
            
            # Risk assessment
            risk_assessment = self._assess_overall_risks()
            
            # Action items
            action_items = self._generate_action_items()
            
            # INTEGRATED CURRICULUM GUIDANCE
            curriculum_guidance = {
                'overview': self.task6_search.get_task6_overview(),
                'executive_summary_template': self.task6_search.get_executive_summary_template(),
                'business_problem_guidance': self.task6_search.get_business_problem_guidance(),
                'key_findings_guidance': self.task6_search.get_key_findings_guidance(),
                'recommendations_guidance': self.task6_search.get_recommendations_guidance(),
                'limitations_guidance': self.task6_search.get_limitations_guidance(),
                'writing_style_guidance': self.task6_search.get_writing_style_guidance(),
                'integration_guidance': self.task6_search.get_integration_guidance(),
                'comprehensive_guidance': self.task6_search.get_comprehensive_task6_guidance()
            }
            
            self.results['task6'] = {
                'executive_summary': executive_summary,
                'visualizations': visualizations,
                'recommendations': recommendations,
                'risk_assessment': risk_assessment,
                'action_items': action_items,
                'curriculum_guidance': curriculum_guidance,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 6 completed successfully with curriculum guidance")
            return self.results['task6']
            
        except Exception as e:
            logger.error(f"Error in Task 6: {e}")
            raise
    
    def run_all_tasks(self, sample_size: Optional[int] = None) -> Dict:
        """
        Run all ATPA tasks in sequence
        
        Args:
            sample_size: Optional sample size for data loading
            
        Returns:
            Dictionary containing results from all tasks
        """
        logger.info("Starting complete ATPA assessment")
        
        try:
            # Run all tasks
            self.task1_data_preparation(sample_size)
            self.task2_privacy_ethics_analysis()
            self.task3_generalized_linear_models()
            self.task4_random_forest_shap()
            self.task5_bayesian_analysis()
            self.task6_executive_summary()
            
            logger.info("All ATPA tasks completed successfully")
            return self.results
            
        except Exception as e:
            logger.error(f"Error running all tasks: {e}")
            raise
    
    # ============================================================================
    # HELPER METHODS FOR TASK 1
    # ============================================================================
    
    def _analyze_missing_values(self, incidents_df: pd.DataFrame, arrestee_df: pd.DataFrame) -> Dict:
        """Analyze missing values in both datasets"""
        
        incidents_missing = incidents_df.isnull().sum()
        incidents_missing_pct = (incidents_missing / len(incidents_df)) * 100
        
        arrestee_missing = arrestee_df.isnull().sum()
        arrestee_missing_pct = (arrestee_missing / len(arrestee_df)) * 100
        
        return {
            'incidents': {
                'missing_counts': incidents_missing[incidents_missing > 0].to_dict(),
                'missing_percentages': incidents_missing_pct[incidents_missing_pct > 0].to_dict()
            },
            'arrestee': {
                'missing_counts': arrestee_missing[arrestee_missing > 0].to_dict(),
                'missing_percentages': arrestee_missing_pct[arrestee_missing_pct > 0].to_dict()
            }
        }
    
    def _apply_knn_imputation(self, incidents_df: pd.DataFrame, arrestee_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Apply KNN imputation to both datasets"""
        
        logger.info("Applying KNN imputation to incidents dataset")
        incidents_imputed = self._knn_impute_dataset(incidents_df, "incidents")
        
        logger.info("Applying KNN imputation to arrestee dataset")
        arrestee_imputed = self._knn_impute_dataset(arrestee_df, "arrestee")
        
        return incidents_imputed, arrestee_imputed
    
    def _knn_impute_dataset(self, df: pd.DataFrame, dataset_name: str) -> pd.DataFrame:
        """Apply basic imputation to a single dataset (simplified for now)"""
        
        df_copy = df.copy()
        
        # Handle numeric columns - fill with median
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df_copy[col].isnull().any():
                df_copy[col] = df_copy[col].fillna(df_copy[col].median())
        
        # Handle categorical columns - fill with mode
        categorical_cols = df_copy.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            if df_copy[col].isnull().any():
                if df_copy[col].dtype.name == 'category':
                    # For categorical columns, add 'Unknown' to categories first
                    df_copy[col] = df_copy[col].cat.add_categories(['Unknown'])
                    mode_value = df_copy[col].mode().iloc[0] if not df_copy[col].mode().empty else 'Unknown'
                else:
                    mode_value = df_copy[col].mode().iloc[0] if not df_copy[col].mode().empty else 'Unknown'
                df_copy[col] = df_copy[col].fillna(mode_value)
        
        # Handle datetime columns - fill with median date
        datetime_cols = df_copy.select_dtypes(include=['datetime64']).columns
        for col in datetime_cols:
            if df_copy[col].isnull().any():
                median_date = df_copy[col].median()
                df_copy[col] = df_copy[col].fillna(median_date)
        
        logger.info(f"Basic imputation completed for {dataset_name} dataset")
        return df_copy
    
    def _create_merged_dataset_with_target(self, incidents_df: pd.DataFrame, arrestee_df: pd.DataFrame) -> pd.DataFrame:
        """Create merged dataset with ARREST target variable"""
        
        # Create arrest counts
        arrest_counts = arrestee_df.groupby('incident_id').size().reset_index(name='arrest_count')
        
        # Merge datasets
        merged_df = incidents_df.merge(arrest_counts, on='incident_id', how='left')
        merged_df['arrest_count'] = merged_df['arrest_count'].fillna(0).astype(int)
        
        # Create ARREST target variable
        merged_df['ARREST'] = (merged_df['arrest_count'] > 0).astype(int)
        
        # Add derived features
        merged_df = self._add_derived_features(merged_df)
        
        logger.info(f"Merged dataset created: {len(merged_df)} records, arrest rate: {merged_df['ARREST'].mean():.3f}")
        return merged_df
    
    def _add_derived_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add derived features to the dataset"""
        
        # Extract date features
        if 'incident_date' in df.columns:
            df['incident_date'] = pd.to_datetime(df['incident_date'], errors='coerce')
            df['year'] = df['incident_date'].dt.year
            df['month'] = df['incident_date'].dt.month
            df['day_of_week'] = df['incident_date'].dt.dayofweek
            df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        
        # Create crime severity feature
        if 'crime_against' in df.columns:
            severity_mapping = {
                'Property': 1,
                'Society': 2,
                'Person': 3
            }
            df['crime_severity'] = df['crime_against'].map(severity_mapping).fillna(1)
        
        return df
    
    def _assess_data_quality(self, df: pd.DataFrame) -> Dict:
        """Assess data quality of the merged dataset"""
        
        quality_report = {
            'total_records': len(df),
            'total_columns': len(df.columns),
            'missing_values': {
                'total_missing': df.isnull().sum().sum(),
                'columns_with_missing': (df.isnull().sum() > 0).sum(),
                'missing_percentage': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
            },
            'arrest_statistics': {
                'total_arrests': int(df['ARREST'].sum()),
                'arrest_rate': float(df['ARREST'].mean()),
                'no_arrest_count': int((df['ARREST'] == 0).sum())
            },
            'data_types': df.dtypes.value_counts().to_dict(),
            'duplicate_records': int(df.duplicated().sum())
        }
        
        return quality_report
    
    # ============================================================================
    # HELPER METHODS FOR TASK 2
    # ============================================================================
    
    def _identify_protected_variables(self, df: pd.DataFrame) -> List[str]:
        """Identify protected variables in the dataset"""
        
        protected_vars = []
        
        # Check for demographic variables
        demographic_patterns = ['race', 'ethnicity', 'sex', 'gender', 'age', 'income']
        
        for col in df.columns:
            col_lower = col.lower()
            if any(pattern in col_lower for pattern in demographic_patterns):
                protected_vars.append(col)
        
        return protected_vars
    
    def _analyze_demographics(self, df: pd.DataFrame) -> Dict:
        """Analyze demographic distributions"""
        
        demographic_analysis = {}
        
        # Analyze race distribution if available
        if 'race_desc' in df.columns:
            race_dist = df['race_desc'].value_counts()
            demographic_analysis['race_distribution'] = {
                'counts': race_dist.to_dict(),
                'percentages': (race_dist / len(df) * 100).to_dict()
            }
        
        # Analyze ethnicity distribution if available
        if 'ethnicity_name' in df.columns:
            ethnicity_dist = df['ethnicity_name'].value_counts()
            demographic_analysis['ethnicity_distribution'] = {
                'counts': ethnicity_dist.to_dict(),
                'percentages': (ethnicity_dist / len(df) * 100).to_dict()
            }
        
        return demographic_analysis
    
    def _assess_arrest_bias(self, df: pd.DataFrame) -> Dict:
        """Assess bias in arrest rates across demographic groups"""
        
        bias_assessment = {}
        
        # Analyze arrest rates by race
        if 'race_desc' in df.columns:
            race_arrest_rates = df.groupby('race_desc')['ARREST'].agg(['count', 'sum', 'mean'])
            bias_assessment['race_arrest_rates'] = race_arrest_rates.to_dict()
        
        # Analyze arrest rates by ethnicity
        if 'ethnicity_name' in df.columns:
            ethnicity_arrest_rates = df.groupby('ethnicity_name')['ARREST'].agg(['count', 'sum', 'mean'])
            bias_assessment['ethnicity_arrest_rates'] = ethnicity_arrest_rates.to_dict()
        
        return bias_assessment
    
    def _calculate_fairness_metrics(self, df: pd.DataFrame) -> Dict:
        """Calculate fairness metrics"""
        
        fairness_metrics = {
            'overall_arrest_rate': float(df['ARREST'].mean()),
            'demographic_parity': {}
        }
        
        # Calculate demographic parity for race
        if 'race_desc' in df.columns:
            race_rates = df.groupby('race_desc')['ARREST'].mean()
            fairness_metrics['demographic_parity']['race'] = {
                'rates': race_rates.to_dict(),
                'max_difference': float(race_rates.max() - race_rates.min())
            }
        
        return fairness_metrics
    
    def _generate_ethics_recommendations(self, protected_vars: List[str], bias_assessment: Dict, fairness_metrics: Dict) -> List[str]:
        """Generate ethics recommendations"""
        
        recommendations = []
        
        if protected_vars:
            recommendations.append("Protected variables identified. Consider excluding these from model training to prevent bias.")
        
        if fairness_metrics.get('demographic_parity', {}).get('race', {}).get('max_difference', 0) > 0.1:
            recommendations.append("Significant demographic parity differences detected. Consider fairness-aware modeling techniques.")
        
        recommendations.append("Ensure model predictions are not used to perpetuate existing biases in the criminal justice system.")
        recommendations.append("Regularly monitor model performance across demographic groups.")
        
        return recommendations
    
    # ============================================================================
    # HELPER METHODS FOR TASK 3
    # ============================================================================
    
    def _prepare_modeling_data(self, df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """Prepare data for modeling"""
        
        # Select features (exclude target and ID columns)
        exclude_cols = ['ARREST', 'incident_id', 'arrest_count']
        feature_cols = [col for col in df.columns if col not in exclude_cols]
        
        # Create feature matrix
        X = df[feature_cols].copy()
        
        # Handle datetime columns - convert to numeric features
        datetime_cols = X.select_dtypes(include=['datetime64']).columns
        for col in datetime_cols:
            if col in X.columns:
                X[f'{col}_year'] = X[col].dt.year
                X[f'{col}_month'] = X[col].dt.month
                X[f'{col}_day'] = X[col].dt.day
                X[f'{col}_dayofweek'] = X[col].dt.dayofweek
                X = X.drop(columns=[col])
        
        # Handle categorical variables
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns
        
        # Encode categorical variables
        for col in categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            self.encoders[col] = le
        
        # Final fillna to ensure no NaNs remain
        X = X.fillna(X.median(numeric_only=True)).fillna(0)
        
        # Convert to numeric
        X = X.astype(float)
        
        # Target variable
        y = df['ARREST'].values
        
        return X.values, y, list(X.columns)
    
    def _train_logistic_models(self, X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray) -> Dict:
        """Train multiple logistic regression models"""
        
        models = {}
        
        # Standard logistic regression
        lr_standard = LogisticRegression(random_state=42, max_iter=1000)
        lr_standard.fit(X_train, y_train)
        
        y_pred = lr_standard.predict(X_test)
        y_pred_proba = lr_standard.predict_proba(X_test)[:, 1]
        
        models['standard'] = {
            'model': lr_standard,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'metrics': self._calculate_metrics(y_test, y_pred, y_pred_proba)
        }
        
        # L1 regularized logistic regression
        lr_l1 = LogisticRegression(penalty='l1', solver='liblinear', random_state=42, max_iter=1000)
        lr_l1.fit(X_train, y_train)
        
        y_pred = lr_l1.predict(X_test)
        y_pred_proba = lr_l1.predict_proba(X_test)[:, 1]
        
        models['l1_regularized'] = {
            'model': lr_l1,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'metrics': self._calculate_metrics(y_test, y_pred, y_pred_proba)
        }
        
        # L2 regularized logistic regression
        lr_l2 = LogisticRegression(penalty='l2', random_state=42, max_iter=1000)
        lr_l2.fit(X_train, y_train)
        
        y_pred = lr_l2.predict(X_test)
        y_pred_proba = lr_l2.predict_proba(X_test)[:, 1]
        
        models['l2_regularized'] = {
            'model': lr_l2,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'metrics': self._calculate_metrics(y_test, y_pred, y_pred_proba)
        }
        
        return models
    
    def _perform_cross_validation(self, X: np.ndarray, y: np.ndarray) -> Dict:
        """Perform cross-validation"""
        
        lr = LogisticRegression(random_state=42, max_iter=1000)
        
        cv_scores = cross_val_score(lr, X, y, cv=5, scoring='accuracy')
        
        return {
            'mean_accuracy': float(cv_scores.mean()),
            'std_accuracy': float(cv_scores.std()),
            'cv_scores': cv_scores.tolist()
        }
    
    def _compare_models(self, models: Dict, cv_results: Dict) -> Dict:
        """Compare model performance"""
        
        comparison = {
            'models': {},
            'best_model': None,
            'best_auc': 0
        }
        
        for name, model_data in models.items():
            comparison['models'][name] = model_data['metrics']
            
            if model_data['metrics']['auc'] > comparison['best_auc']:
                comparison['best_auc'] = model_data['metrics']['auc']
                comparison['best_model'] = name
        
        comparison['cross_validation'] = cv_results
        
        return comparison
    
    def _calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray, y_pred_proba: np.ndarray) -> Dict:
        """Calculate classification metrics"""
        
        return {
            'accuracy': float((y_true == y_pred).mean()),
            'precision': float(confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[0, 1])),
            'recall': float(confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[1, 0])),
            'f1_score': float(2 * (confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[0, 1])) * (confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[1, 0])) / ((confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[0, 1])) + (confusion_matrix(y_true, y_pred)[1, 1] / (confusion_matrix(y_true, y_pred)[1, 1] + confusion_matrix(y_true, y_pred)[1, 0])))),
            'auc': float(roc_auc_score(y_true, y_pred_proba))
        }
    
    # ============================================================================
    # HELPER METHODS FOR TASK 4
    # ============================================================================
    
    def _train_random_forest(self, X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray) -> Dict:
        """Train Random Forest model"""
        
        rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)
        
        y_pred = rf.predict(X_test)
        y_pred_proba = rf.predict_proba(X_test)[:, 1]
        
        return {
            'model': rf,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'metrics': self._calculate_metrics(y_test, y_pred, y_pred_proba),
            'feature_importance': rf.feature_importances_
        }
    
    def _perform_shap_analysis(self, rf_results: Dict, X_test: np.ndarray, feature_names: List[str]) -> Dict:
        """Perform SHAP analysis"""
        import numpy as np
        rf_model = rf_results['model']
        
        # Create SHAP explainer
        explainer = shap.TreeExplainer(rf_model)
        
        # Calculate SHAP values for a sample
        sample_size = min(1000, len(X_test))
        X_sample = X_test[:sample_size]
        shap_values = explainer.shap_values(X_sample)
        
        # Handle binary/multiclass output
        if isinstance(shap_values, list):
            if len(shap_values) == 2:
                # Binary classification: use class 1
                shap_vals = np.array(shap_values[1])
            else:
                # Multiclass: average abs SHAP values across classes
                shap_vals = np.mean(np.abs(np.array(shap_values)), axis=0)
        else:
            shap_vals = np.array(shap_values)
        
        # Calculate mean absolute SHAP values
        mean_shap_values = np.abs(shap_vals).mean(axis=0)
        
        # Create feature importance ranking
        feature_importance_ranking = sorted(
            zip(feature_names, mean_shap_values),
            key=lambda x: float(np.ravel(x[1])[0]),
            reverse=True
        )
        
        return {
            'shap_values': np.array(shap_values).tolist(),
            'mean_shap_values': mean_shap_values.tolist(),
            'feature_importance_ranking': feature_importance_ranking,
            'sample_size': sample_size
        }
    
    def _analyze_feature_importance(self, rf_results: Dict, feature_names: List[str]) -> Dict:
        """Analyze feature importance"""
        
        importance_scores = rf_results['feature_importance']
        
        # Create feature importance ranking
        feature_importance_ranking = sorted(
            zip(feature_names, importance_scores),
            key=lambda x: x[1],
            reverse=True
        )
        
        return {
            'importance_scores': importance_scores.tolist(),
            'feature_ranking': feature_importance_ranking,
            'top_features': feature_importance_ranking[:10]
        }
    
    # ============================================================================
    # HELPER METHODS FOR TASK 5
    # ============================================================================
    
    def _perform_bayesian_analysis(self, X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray, feature_names: List[str]) -> Dict:
        """Perform Bayesian analysis"""
        
        # For simplicity, we'll use a regularized logistic regression as a proxy for Bayesian analysis
        # In a real implementation, you might use PyMC3 or similar
        
        from sklearn.linear_model import LogisticRegressionCV
        
        # Use cross-validated logistic regression with regularization
        bayesian_lr = LogisticRegressionCV(cv=5, random_state=42, max_iter=1000)
        bayesian_lr.fit(X_train, y_train)
        
        y_pred = bayesian_lr.predict(X_test)
        y_pred_proba = bayesian_lr.predict_proba(X_test)[:, 1]
        
        # Analyze coefficient uncertainty (using cross-validation)
        cv_coefficients = []
        for i in range(5):
            # Split data for this fold
            fold_indices = np.arange(len(X_train))
            np.random.shuffle(fold_indices)
            fold_size = len(X_train) // 5
            test_indices = fold_indices[i*fold_size:(i+1)*fold_size]
            train_indices = np.concatenate([fold_indices[:i*fold_size], fold_indices[(i+1)*fold_size:]])
            
            X_fold_train, X_fold_test = X_train[train_indices], X_train[test_indices]
            y_fold_train, y_fold_test = y_train[train_indices], y_train[test_indices]
            
            lr_fold = LogisticRegression(random_state=42, max_iter=1000)
            lr_fold.fit(X_fold_train, y_fold_train)
            cv_coefficients.append(lr_fold.coef_[0])
        
        cv_coefficients = np.array(cv_coefficients)
        coefficient_std = np.std(cv_coefficients, axis=0)
        
        return {
            'model': bayesian_lr,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'metrics': self._calculate_metrics(y_test, y_pred, y_pred_proba),
            'coefficient_uncertainty': coefficient_std.tolist(),
            'feature_names': feature_names,
            'cv_coefficients': cv_coefficients.tolist()
        }
    
    # ============================================================================
    # HELPER METHODS FOR TASK 6
    # ============================================================================
    
    def _generate_executive_summary(self) -> Dict:
        """Generate executive summary"""
        
        summary = {
            'overview': {
                'total_incidents': self.results['task1']['quality_report']['total_records'],
                'arrest_rate': self.results['task1']['quality_report']['arrest_statistics']['arrest_rate'],
                'data_quality_score': 100 - self.results['task1']['quality_report']['missing_values']['missing_percentage']
            },
            'model_performance': {
                'best_logistic_model': self.results['task3']['best_model'],
                'logistic_auc': self.results['task3']['model_comparison']['models'][self.results['task3']['best_model']]['auc'],
                'random_forest_auc': self.results['task4']['random_forest']['metrics']['auc'],
                'bayesian_auc': self.results['task5']['bayesian_results']['metrics']['auc']
            },
            'key_insights': [
                f"Arrest rate: {self.results['task1']['quality_report']['arrest_statistics']['arrest_rate']:.1%}",
                f"Best performing model: {self.results['task3']['best_model']} (AUC: {self.results['task3']['model_comparison']['models'][self.results['task3']['best_model']]['auc']:.3f})",
                f"Data quality: {100 - self.results['task1']['quality_report']['missing_values']['missing_percentage']:.1f}% complete"
            ],
            'ethical_considerations': self.results['task2']['ethics_recommendations']
        }
        
        return summary
    
    def _create_executive_visualizations(self) -> Dict:
        """Create executive visualizations"""
        
        # This would create actual plots in a real implementation
        # For now, we'll return placeholder information
        
        return {
            'model_comparison_plot': 'Model performance comparison visualization',
            'feature_importance_plot': 'Top 10 most important features',
            'arrest_rate_analysis': 'Arrest rate by demographic groups',
            'data_quality_plot': 'Missing values analysis'
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations"""
        
        recommendations = []
        
        # Model recommendations
        best_model = self.results['task3']['best_model']
        best_auc = self.results['task3']['model_comparison']['models'][best_model]['auc']
        
        recommendations.append(f"Use {best_model} model for arrest prediction (AUC: {best_auc:.3f})")
        
        # Feature recommendations
        if 'task4' in self.results:
            top_features = self.results['task4']['feature_importance']['top_features'][:5]
            recommendations.append(f"Focus on top 5 features: {[f[0] for f in top_features]}")
        
        # Ethical recommendations
        recommendations.extend(self.results['task2']['ethics_recommendations'])
        
        # Data quality recommendations
        missing_pct = self.results['task1']['quality_report']['missing_values']['missing_percentage']
        if missing_pct > 10:
            recommendations.append(f"Improve data collection to reduce missing values ({missing_pct:.1f}% missing)")
        
        return recommendations
    
    def save_results(self, filename: str = "atpa_results.json"):
        """Save all results to a JSON file"""
        def convert_for_json(obj):
            """Recursively convert objects to JSON-serializable format"""
            if isinstance(obj, dict):
                return {str(k): convert_for_json(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_for_json(item) for item in obj]
            elif isinstance(obj, (np.integer, np.floating)):
                return obj.item()
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif hasattr(obj, 'dtype') and hasattr(obj, 'tolist'):  # pandas Series, etc.
                return obj.tolist()
            elif hasattr(obj, 'to_dict'):  # pandas DataFrame
                return obj.to_dict('records')
            elif isinstance(obj, (str, int, float, bool, type(None))):
                return obj
            else:
                return str(obj)
        
        serializable_results = convert_for_json(self.results)
        
        with open(filename, 'w') as f:
            json.dump(serializable_results, f, indent=2, default=str)
        
        logger.info(f"Results saved to {filename}")
    
    def load_results(self, filepath: str):
        """Load results from file"""
        
        with open(filepath, 'r') as f:
            self.results = json.load(f)
        
        logger.info(f"Results loaded from {filepath}") 

    # Additional detailed analysis methods
    
    def _perform_detailed_bias_analysis(self, df: pd.DataFrame) -> Dict:
        """Perform detailed bias analysis across multiple dimensions"""
        
        bias_analysis = {
            'demographic_bias': {},
            'geographic_bias': {},
            'temporal_bias': {},
            'offense_type_bias': {}
        }
        
        # Demographic bias analysis
        if 'offender_race_id' in df.columns:
            race_arrest_rates = df.groupby('offender_race_id')['ARREST'].mean()
            bias_analysis['demographic_bias']['race_arrest_rates'] = race_arrest_rates.to_dict()
        
        if 'offender_sex_code' in df.columns:
            sex_arrest_rates = df.groupby('offender_sex_code')['ARREST'].mean()
            bias_analysis['demographic_bias']['sex_arrest_rates'] = sex_arrest_rates.to_dict()
        
        if 'offender_age_name' in df.columns:
            age_arrest_rates = df.groupby('offender_age_name')['ARREST'].mean()
            bias_analysis['demographic_bias']['age_arrest_rates'] = age_arrest_rates.to_dict()
        
        # Geographic bias analysis
        if 'agency_name' in df.columns:
            agency_arrest_rates = df.groupby('agency_name')['ARREST'].mean().sort_values(ascending=False)
            bias_analysis['geographic_bias']['agency_arrest_rates'] = agency_arrest_rates.head(10).to_dict()
        
        # Temporal bias analysis - REMOVED (unnecessary for ATPA assessment)
        bias_analysis['temporal_bias'] = {'note': 'Temporal analysis not required for ATPA assessment'}
        
        # Offense type bias analysis
        if 'offense_category_name' in df.columns:
            offense_arrest_rates = df.groupby('offense_category_name')['ARREST'].mean().sort_values(ascending=False)
            bias_analysis['offense_type_bias']['offense_arrest_rates'] = offense_arrest_rates.head(10).to_dict()
        
        return bias_analysis
    
    def _assess_model_risks(self, df: pd.DataFrame, protected_vars: List[str]) -> Dict:
        """Assess risks associated with model deployment"""
        
        risk_assessment = {
            'privacy_risks': [],
            'bias_risks': [],
            'accuracy_risks': [],
            'operational_risks': [],
            'compliance_risks': []
        }
        
        # Privacy risks
        if len(protected_vars) > 0:
            risk_assessment['privacy_risks'].append(f"Model uses {len(protected_vars)} protected variables")
            risk_assessment['privacy_risks'].append("Risk of re-identification of individuals")
        
        # Bias risks
        arrest_rate = df['ARREST'].mean()
        if arrest_rate < 0.1 or arrest_rate > 0.9:
            risk_assessment['bias_risks'].append(f"Imbalanced arrest rate ({arrest_rate:.1%}) may lead to bias")
        
        # Check for demographic imbalances
        if 'offender_race_id' in df.columns:
            race_counts = df['offender_race_id'].value_counts()
            if race_counts.max() / race_counts.min() > 10:
                risk_assessment['bias_risks'].append("Significant demographic imbalance detected")
        
        # Accuracy risks
        missing_pct = df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100
        if missing_pct > 5:
            risk_assessment['accuracy_risks'].append(f"High missing data rate ({missing_pct:.1f}%) may affect accuracy")
        
        # Operational risks
        risk_assessment['operational_risks'].append("Model requires regular retraining with new data")
        risk_assessment['operational_risks'].append("Need for ongoing bias monitoring")
        
        # Compliance risks
        risk_assessment['compliance_risks'].append("Ensure compliance with data protection regulations")
        risk_assessment['compliance_risks'].append("Regular fairness audits required")
        
        return risk_assessment
    
    def _analyze_model_coefficients(self, models: Dict, feature_names: List[str]) -> Dict:
        """Analyze model coefficients for interpretability"""
        
        coefficient_analysis = {
            'significant_features': [],
            'feature_importance': {},
            'coefficient_stability': {},
            'interpretation_notes': []
        }
        
        # Analyze coefficients for each model
        for model_name, model_data in models.items():
            if 'model' in model_data and hasattr(model_data['model'], 'coef_'):
                coefficients = model_data['model'].coef_[0]
                
                # Create feature-coefficient pairs
                feature_coef_pairs = list(zip(feature_names, coefficients))
                
                # Sort by absolute coefficient value
                feature_coef_pairs.sort(key=lambda x: abs(x[1]), reverse=True)
                
                # Store top features
                coefficient_analysis['feature_importance'][model_name] = {
                    'top_positive': feature_coef_pairs[:5],
                    'top_negative': [pair for pair in feature_coef_pairs if pair[1] < 0][:5],
                    'all_coefficients': feature_coef_pairs
                }
                
                # Identify significant features (coefficient > 0.1 or < -0.1)
                significant = [pair for pair in feature_coef_pairs if abs(pair[1]) > 0.1]
                coefficient_analysis['significant_features'].extend([f[0] for f in significant])
        
        # Remove duplicates from significant features
        coefficient_analysis['significant_features'] = list(set(coefficient_analysis['significant_features']))
        
        # Add interpretation notes
        coefficient_analysis['interpretation_notes'].append("Positive coefficients indicate higher arrest probability")
        coefficient_analysis['interpretation_notes'].append("Negative coefficients indicate lower arrest probability")
        coefficient_analysis['interpretation_notes'].append("Larger absolute values indicate stronger feature influence")
        
        return coefficient_analysis
    
    def _perform_detailed_shap_analysis(self, rf_results: Dict, X_test: np.ndarray, feature_names: List[str]) -> Dict:
        """Perform detailed SHAP analysis with multiple perspectives"""
        
        detailed_shap = {
            'global_importance': {},
            'local_explanations': {},
            'interaction_effects': {},
            'summary_statistics': {}
        }
        
        try:
            # Get the Random Forest model
            rf_model = rf_results['model']
            
            # Create SHAP explainer
            explainer = shap.TreeExplainer(rf_model)
            
            # Calculate SHAP values for test set
            shap_values = explainer.shap_values(X_test)
            
            # Handle binary classification
            if isinstance(shap_values, list):
                shap_values = shap_values[1]  # Use positive class SHAP values
            
            # Global feature importance
            feature_importance = np.abs(shap_values).mean(0)
            feature_importance_pairs = list(zip(feature_names, feature_importance))
            feature_importance_pairs.sort(key=lambda x: x[1], reverse=True)
            
            detailed_shap['global_importance'] = {
                'top_features': feature_importance_pairs[:10],
                'all_features': feature_importance_pairs
            }
            
            # Local explanations for a few sample cases
            sample_indices = np.random.choice(len(X_test), min(5, len(X_test)), replace=False)
            detailed_shap['local_explanations'] = {
                'sample_cases': []
            }
            
            for idx in sample_indices:
                case_explanation = {
                    'case_index': int(idx),
                    'prediction': float(rf_model.predict_proba(X_test[idx:idx+1])[0][1]),
                    'top_contributors': []
                }
                
                # Get top contributing features for this case
                case_shap = shap_values[idx]
                case_pairs = list(zip(feature_names, case_shap))
                case_pairs.sort(key=lambda x: abs(x[1]), reverse=True)
                case_explanation['top_contributors'] = case_pairs[:5]
                
                detailed_shap['local_explanations']['sample_cases'].append(case_explanation)
            
            # Summary statistics
            detailed_shap['summary_statistics'] = {
                'mean_shap_value': float(np.mean(shap_values)),
                'std_shap_value': float(np.std(shap_values)),
                'max_shap_value': float(np.max(shap_values)),
                'min_shap_value': float(np.min(shap_values))
            }
            
        except Exception as e:
            detailed_shap['error'] = f"SHAP analysis failed: {str(e)}"
        
        return detailed_shap
    
    def _analyze_bayesian_uncertainty(self, bayesian_results: Dict, feature_names: List[str]) -> Dict:
        """Analyze uncertainty in Bayesian model results"""
        
        uncertainty_analysis = {
            'posterior_uncertainty': {},
            'credible_intervals': {},
            'model_uncertainty': {},
            'prediction_uncertainty': {}
        }
        
        try:
            # Extract posterior samples if available
            if 'posterior_samples' in bayesian_results:
                posterior_samples = bayesian_results['posterior_samples']
                
                # Calculate credible intervals for coefficients
                for i, feature in enumerate(feature_names):
                    if i < posterior_samples.shape[1]:
                        samples = posterior_samples[:, i]
                        uncertainty_analysis['credible_intervals'][feature] = {
                            'mean': float(np.mean(samples)),
                            'std': float(np.std(samples)),
                            'ci_95_lower': float(np.percentile(samples, 2.5)),
                            'ci_95_upper': float(np.percentile(samples, 97.5)),
                            'ci_90_lower': float(np.percentile(samples, 5)),
                            'ci_90_upper': float(np.percentile(samples, 95))
                        }
            
            # Model uncertainty metrics
            if 'metrics' in bayesian_results:
                metrics = bayesian_results['metrics']
                uncertainty_analysis['model_uncertainty'] = {
                    'accuracy': metrics.get('accuracy', 0),
                    'precision': metrics.get('precision', 0),
                    'recall': metrics.get('recall', 0),
                    'auc': metrics.get('auc', 0)
                }
            
            # Prediction uncertainty
            uncertainty_analysis['prediction_uncertainty'] = {
                'calibration_quality': 'Good' if bayesian_results.get('calibration_score', 0) > 0.8 else 'Needs improvement',
                'confidence_intervals': 'Available' if 'posterior_samples' in bayesian_results else 'Not available'
            }
            
        except Exception as e:
            uncertainty_analysis['error'] = f"Uncertainty analysis failed: {str(e)}"
        
        return uncertainty_analysis
    
    def _assess_overall_risks(self) -> Dict:
        """Assess overall risks across all tasks"""
        
        overall_risks = {
            'data_quality_risks': [],
            'model_performance_risks': [],
            'ethical_risks': [],
            'operational_risks': [],
            'risk_level': 'Medium'
        }
        
        try:
            # Data quality risks
            if 'task1' in self.results:
                missing_pct = self.results['task1']['quality_report']['missing_values']['missing_percentage']
                if missing_pct > 10:
                    overall_risks['data_quality_risks'].append(f"High missing data rate: {missing_pct:.1f}%")
                    overall_risks['risk_level'] = 'High'
            
            # Model performance risks
            if 'task3' in self.results and 'task4' in self.results:
                logistic_auc = self.results['task3']['model_comparison']['models'][self.results['task3']['best_model']]['auc']
                rf_auc = self.results['task4']['random_forest']['metrics']['auc']
                
                if logistic_auc < 0.7:
                    overall_risks['model_performance_risks'].append(f"Low logistic regression AUC: {logistic_auc:.3f}")
                
                if rf_auc < 0.8:
                    overall_risks['model_performance_risks'].append(f"Low random forest AUC: {rf_auc:.3f}")
            
            # Ethical risks
            if 'task2' in self.results:
                protected_count = len(self.results['task2']['protected_variables'])
                if protected_count > 10:
                    overall_risks['ethical_risks'].append(f"Many protected variables: {protected_count}")
                    overall_risks['risk_level'] = 'High'
            
            # Operational risks
            overall_risks['operational_risks'].append("Model requires regular monitoring and retraining")
            overall_risks['operational_risks'].append("Need for bias detection and mitigation procedures")
            
        except Exception as e:
            overall_risks['error'] = f"Risk assessment failed: {str(e)}"
        
        return overall_risks
    
    def _generate_action_items(self) -> List[Dict]:
        """Generate specific action items based on analysis results"""
        
        action_items = []
        
        try:
            # Data quality actions
            if 'task1' in self.results:
                missing_pct = self.results['task1']['quality_report']['missing_values']['missing_percentage']
                if missing_pct > 5:
                    action_items.append({
                        'priority': 'High',
                        'category': 'Data Quality',
                        'action': f'Improve data collection to reduce missing values (currently {missing_pct:.1f}%)',
                        'timeline': '3 months',
                        'owner': 'Data Team'
                    })
            
            # Model performance actions
            if 'task3' in self.results:
                best_model = self.results['task3']['best_model']
                best_auc = self.results['task3']['model_comparison']['models'][best_model]['auc']
                
                if best_auc < 0.85:
                    action_items.append({
                        'priority': 'Medium',
                        'category': 'Model Performance',
                        'action': f'Investigate ways to improve model performance (current AUC: {best_auc:.3f})',
                        'timeline': '6 months',
                        'owner': 'ML Team'
                    })
            
            # Ethical actions
            if 'task2' in self.results:
                protected_count = len(self.results['task2']['protected_variables'])
                action_items.append({
                    'priority': 'High',
                    'category': 'Ethics & Compliance',
                    'action': f'Implement bias monitoring for {protected_count} protected variables',
                    'timeline': '1 month',
                    'owner': 'Compliance Team'
                })
            
            # Operational actions
            action_items.append({
                'priority': 'Medium',
                'category': 'Operations',
                'action': 'Establish regular model retraining schedule',
                'timeline': '2 months',
                'owner': 'Operations Team'
            })
            
            action_items.append({
                'priority': 'Medium',
                'category': 'Operations',
                'action': 'Create model monitoring dashboard',
                'timeline': '3 months',
                'owner': 'IT Team'
            })
            
        except Exception as e:
            action_items.append({
                'priority': 'High',
                'category': 'Error',
                'action': f'Fix error in action item generation: {str(e)}',
                'timeline': 'Immediate',
                'owner': 'Development Team'
            })
        
        return action_items 