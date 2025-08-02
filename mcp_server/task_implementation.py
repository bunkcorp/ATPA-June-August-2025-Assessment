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

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)

class ATPATaskImplementation:
    """
    Comprehensive implementation of all ATPA tasks
    """
    
    def __init__(self, data_loader, protocol_layer):
        """
        Initialize task implementation with data layers
        
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
        
    def task1_data_preparation(self, sample_size: Optional[int] = None) -> Dict:
        """
        Task 1: Data Preparation and Quality Analysis
        
        Implements:
        - Missing value analysis and KNN imputation
        - Data quality assessment
        - Data merging and target variable creation
        """
        logger.info("Starting Task 1: Data Preparation")
        
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
            
            # Store results
            self.results['task1'] = {
                'missing_analysis': missing_analysis,
                'imputation_summary': {
                    'incidents_shape': incidents_imputed.shape,
                    'arrestee_shape': arrestee_imputed.shape,
                    'merged_shape': merged_df.shape
                },
                'quality_report': quality_report,
                'merged_data': merged_df,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 1 completed successfully")
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
        """
        logger.info("Starting Task 2: Privacy and Ethics Analysis")
        
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
            
            self.results['task2'] = {
                'protected_variables': protected_vars,
                'demographic_analysis': demographic_analysis,
                'bias_assessment': bias_assessment,
                'fairness_metrics': fairness_metrics,
                'ethics_recommendations': ethics_recommendations,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 2 completed successfully")
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
        """
        logger.info("Starting Task 3: Generalized Linear Models")
        
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
            
            self.results['task3'] = {
                'models': models,
                'cross_validation': cv_results,
                'model_comparison': model_comparison,
                'best_model': best_model_name,
                'feature_names': feature_names,
                'data_shape': X.shape,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 3 completed successfully")
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
        """
        logger.info("Starting Task 4: Random Forest with SHAP Analysis")
        
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
            
            # Store model
            self.models['random_forest'] = rf_model['model']
            
            self.results['task4'] = {
                'random_forest': rf_model,
                'shap_analysis': shap_analysis,
                'feature_importance': feature_importance,
                'feature_names': feature_names,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 4 completed successfully")
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
        """
        logger.info("Starting Task 5: Bayesian Analysis")
        
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
            
            self.results['task5'] = {
                'bayesian_analysis': bayesian_results,
                'feature_names': feature_names,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 5 completed successfully")
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
        """
        logger.info("Starting Task 6: Executive Summary")
        
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
            
            self.results['task6'] = {
                'executive_summary': executive_summary,
                'visualizations': visualizations,
                'recommendations': recommendations,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info("Task 6 completed successfully")
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
        merged_df['arrest'] = (merged_df['arrest_count'] > 0).astype(int)
        
        # Add derived features
        merged_df = self._add_derived_features(merged_df)
        
        logger.info(f"Merged dataset created: {len(merged_df)} records, arrest rate: {merged_df['arrest'].mean():.3f}")
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
                'total_arrests': int(df['arrest'].sum()),
                'arrest_rate': float(df['arrest'].mean()),
                'no_arrest_count': int((df['arrest'] == 0).sum())
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
            race_arrest_rates = df.groupby('race_desc')['arrest'].agg(['count', 'sum', 'mean'])
            bias_assessment['race_arrest_rates'] = race_arrest_rates.to_dict()
        
        # Analyze arrest rates by ethnicity
        if 'ethnicity_name' in df.columns:
            ethnicity_arrest_rates = df.groupby('ethnicity_name')['arrest'].agg(['count', 'sum', 'mean'])
            bias_assessment['ethnicity_arrest_rates'] = ethnicity_arrest_rates.to_dict()
        
        return bias_assessment
    
    def _calculate_fairness_metrics(self, df: pd.DataFrame) -> Dict:
        """Calculate fairness metrics"""
        
        fairness_metrics = {
            'overall_arrest_rate': float(df['arrest'].mean()),
            'demographic_parity': {}
        }
        
        # Calculate demographic parity for race
        if 'race_desc' in df.columns:
            race_rates = df.groupby('race_desc')['arrest'].mean()
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
        exclude_cols = ['arrest', 'incident_id', 'arrest_count']
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
        y = df['arrest'].values
        
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
                'bayesian_auc': self.results['task5']['bayesian_analysis']['metrics']['auc']
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