"""
Comprehensive Data Quality Analysis - 3 Phases Implementation
ATPA Assessment - June to August 2025

This script implements all 3 phases of comprehensive data quality analysis:
Phase 1: Data Quality Assessment
Phase 2: Imputation Implementation  
Phase 3: Integration and Validation

Following ATPA course materials (Module 2.6) for professional imputation techniques.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

def phase1_data_quality_assessment(data):
    """
    Phase 1: Comprehensive Data Quality Assessment
    - Missing data analysis
    - Missingness testing (MAR/MCAR)
    - Data quality metrics
    """
    print("=" * 60)
    print("PHASE 1: DATA QUALITY ASSESSMENT")
    print("=" * 60)
    
    # Load the prepared data
    df = pd.read_csv('prepared_data.csv')
    print(f"Dataset shape: {df.shape}")
    print(f"Variables: {df.columns.tolist()}")
    
    # 1.1 Missing Data Analysis
    print("\n1.1 MISSING DATA ANALYSIS")
    print("-" * 30)
    
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing_data,
        'Missing_Percent': missing_percent
    }).sort_values('Missing_Percent', ascending=False)
    
    print("Missing data summary:")
    print(missing_df[missing_df['Missing_Count'] > 0])
    
    # 1.2 Data Quality Metrics
    print("\n1.2 DATA QUALITY METRICS")
    print("-" * 30)
    
    # Completeness
    completeness = (1 - missing_percent / 100).mean()
    print(f"Overall completeness: {completeness:.2%}")
    
    # Consistency checks
    print("\nConsistency checks:")
    
    # Check for duplicate records
    duplicates = df.duplicated().sum()
    print(f"Duplicate records: {duplicates}")
    
    # Check data types
    print(f"\nData types:")
    print(df.dtypes.value_counts())
    
    # 1.3 Missingness Pattern Analysis
    print("\n1.3 MISSINGNESS PATTERN ANALYSIS")
    print("-" * 30)
    
    # Test for missing at random (MAR) using permutation test
    variables_with_missing = missing_df[missing_df['Missing_Count'] > 0].index.tolist()
    
    for var in variables_with_missing[:3]:  # Test first 3 variables with missing data
        if df[var].dtype in ['int64', 'float64']:
            print(f"\nTesting missingness pattern for {var}:")
            
            # Use incident_hour as test variable (complete variable)
            test_var = 'incident_hour'
            if test_var in df.columns:
                is_missing = df[var].isnull()
                if is_missing.sum() > 0 and (~is_missing).sum() > 0:
                    test_stat = df.loc[is_missing, test_var].mean() - df.loc[~is_missing, test_var].mean()
                    print(f"  Test statistic: {test_stat:.4f}")
                    
                    # Simple permutation test
                    n_permutations = 1000
                    perm_stats = []
                    
                    for _ in range(n_permutations):
                        perm_missing = np.random.permutation(is_missing)
                        perm_stat = df.loc[perm_missing, test_var].mean() - df.loc[~perm_missing, test_var].mean()
                        perm_stats.append(perm_stat)
                    
                    # Calculate p-value
                    p_value = (np.abs(perm_stats) >= np.abs(test_stat)).mean()
                    print(f"  P-value: {p_value:.4f}")
                    
                    if p_value < 0.05:
                        print(f"  Conclusion: {var} is NOT missing at random (MAR)")
                    else:
                        print(f"  Conclusion: {var} appears to be missing at random (MAR)")
    
    return df, missing_df, variables_with_missing

def phase2_imputation_implementation(df, variables_with_missing):
    """
    Phase 2: Implement Multiple Imputation Techniques
    - Mean/Median imputation
    - KNN imputation
    - Regression imputation
    """
    print("\n" + "=" * 60)
    print("PHASE 2: IMPUTATION IMPLEMENTATION")
    print("=" * 60)
    
    imputation_results = {}
    
    # Separate numeric and categorical variables
    numeric_vars = [var for var in variables_with_missing if df[var].dtype in ['int64', 'float64']]
    categorical_vars = [var for var in variables_with_missing if df[var].dtype == 'object']
    
    print(f"Numeric variables with missing data: {numeric_vars}")
    print(f"Categorical variables with missing data: {categorical_vars}")
    
    # 2.1 Mean/Median Imputation (ATPA Technique 1)
    print("\n2.1 MEAN/MEDIAN IMPUTATION")
    print("-" * 30)
    
    df_mean_imputed = df.copy()
    
    for var in numeric_vars:
        if df[var].isnull().sum() > 0:
            # Use median for skewed data, mean for normal data
            if abs(df[var].skew()) > 1:
                impute_value = df[var].median()
                method = 'median'
            else:
                impute_value = df[var].mean()
                method = 'mean'
            
            original_mean = df[var].mean()
            original_std = df[var].std()
            
            df_mean_imputed[var] = df[var].fillna(impute_value)
            
            imputed_mean = df_mean_imputed[var].mean()
            imputed_std = df_mean_imputed[var].std()
            
            print(f"  {var}:")
            print(f"    Method: {method} ({impute_value:.2f})")
            print(f"    Values imputed: {df[var].isnull().sum()}")
            print(f"    Original mean: {original_mean:.2f}, Imputed mean: {imputed_mean:.2f}")
            print(f"    Original std: {original_std:.2f}, Imputed std: {imputed_std:.2f}")
    
    for var in categorical_vars:
        if df[var].isnull().sum() > 0:
            mode_value = df[var].mode().iloc[0] if len(df[var].mode()) > 0 else 'Unknown'
            df_mean_imputed[var] = df[var].fillna(mode_value)
            print(f"  {var}: Mode imputation ({mode_value}) - {df[var].isnull().sum()} values")
    
    imputation_results['mean_median'] = df_mean_imputed
    
    # 2.2 KNN Imputation (ATPA Technique 2)
    print("\n2.2 K-NEAREST NEIGHBORS IMPUTATION")
    print("-" * 30)
    
    try:
        # Prepare data for KNN imputation
        df_knn = df.copy()
        
        # Convert categorical variables to numeric for KNN
        categorical_cols = df_knn.select_dtypes(include=['object']).columns
        df_knn_encoded = df_knn.copy()
        
        for col in categorical_cols:
            if col in df_knn_encoded.columns:
                df_knn_encoded[col] = pd.Categorical(df_knn_encoded[col]).codes
        
        # Apply KNN imputation
        imputer = KNNImputer(n_neighbors=5, weights='uniform')
        imputed_array = imputer.fit_transform(df_knn_encoded)
        
        df_knn_imputed = pd.DataFrame(imputed_array, columns=df_knn_encoded.columns, index=df_knn_encoded.index)
        
        # Convert back categorical variables
        for col in categorical_cols:
            if col in df_knn_imputed.columns:
                # Convert back to original categories
                original_categories = df_knn[col].unique()
                df_knn_imputed[col] = pd.Categorical.from_codes(
                    df_knn_imputed[col].round().astype(int), 
                    categories=original_categories
                )
        
        print("KNN imputation completed successfully")
        
        # Quality assessment for numeric variables
        for var in numeric_vars:
            if df[var].isnull().sum() > 0:
                original_mean = df[var].mean()
                original_std = df[var].std()
                imputed_mean = df_knn_imputed[var].mean()
                imputed_std = df_knn_imputed[var].std()
                
                print(f"  {var}:")
                print(f"    Original mean: {original_mean:.2f}, Imputed mean: {imputed_mean:.2f}")
                print(f"    Original std: {original_std:.2f}, Imputed std: {imputed_std:.2f}")
        
        imputation_results['knn'] = df_knn_imputed
        
    except Exception as e:
        print(f"KNN imputation failed: {e}")
        imputation_results['knn'] = df.copy()
    
    # 2.3 Regression Imputation (ATPA Technique 3)
    print("\n2.3 REGRESSION IMPUTATION")
    print("-" * 30)
    
    df_reg_imputed = df.copy()
    
    for var in numeric_vars:
        if df[var].isnull().sum() > 0:
            # Find complete variables for prediction
            complete_vars = [col for col in df.columns if col != var and df[col].isnull().sum() == 0 and df[col].dtype in ['int64', 'float64']]
            
            if len(complete_vars) > 0:
                # Use first complete variable as predictor
                predictor = complete_vars[0]
                
                # Prepare data for regression
                train_data = df.dropna(subset=[var])
                X_train = train_data[predictor].values.reshape(-1, 1)
                y_train = train_data[var].values
                
                # Fit regression model
                reg = LinearRegression().fit(X_train, y_train)
                
                # Predict missing values
                missing_mask = df[var].isnull()
                if missing_mask.sum() > 0:
                    X_pred = df.loc[missing_mask, predictor].values.reshape(-1, 1)
                    predictions = reg.predict(X_pred)
                    df_reg_imputed.loc[missing_mask, var] = predictions
                    
                    original_mean = df[var].mean()
                    original_std = df[var].std()
                    imputed_mean = df_reg_imputed[var].mean()
                    imputed_std = df_reg_imputed[var].std()
                    
                    print(f"  {var} (predicted by {predictor}):")
                    print(f"    Original mean: {original_mean:.2f}, Imputed mean: {imputed_mean:.2f}")
                    print(f"    Original std: {original_std:.2f}, Imputed std: {imputed_std:.2f}")
    
    imputation_results['regression'] = df_reg_imputed
    
    return imputation_results

def phase3_integration_validation(imputation_results, original_df):
    """
    Phase 3: Integration and Validation
    - Model performance comparison
    - Quality assessment
    - Final recommendations
    """
    print("\n" + "=" * 60)
    print("PHASE 3: INTEGRATION AND VALIDATION")
    print("=" * 60)
    
    # 3.1 Model Performance Comparison
    print("\n3.1 MODEL PERFORMANCE COMPARISON")
    print("-" * 30)
    
    # Prepare target variable
    target = 'ARREST'
    
    # Remove rows with missing target
    complete_data = original_df.dropna(subset=[target])
    
    if len(complete_data) > 0:
        # Prepare features (exclude target and non-numeric columns)
        feature_cols = [col for col in complete_data.columns if col != target and complete_data[col].dtype in ['int64', 'float64']]
        
        if len(feature_cols) > 0:
            X = complete_data[feature_cols]
            y = complete_data[target]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
            
            # Train baseline model (with original data)
            baseline_model = RandomForestClassifier(n_estimators=100, random_state=42)
            baseline_model.fit(X_train, y_train)
            baseline_pred = baseline_model.predict(X_test)
            baseline_accuracy = accuracy_score(y_test, baseline_pred)
            
            print(f"Baseline model accuracy (original data): {baseline_accuracy:.4f}")
            
            # Test each imputation method
            model_results = {}
            
            for method_name, imputed_df in imputation_results.items():
                try:
                    # Prepare imputed data
                    imputed_complete = imputed_df.dropna(subset=[target])
                    
                    if len(imputed_complete) > 0:
                        X_imputed = imputed_complete[feature_cols]
                        y_imputed = imputed_complete[target]
                        
                        # Split imputed data
                        X_train_imp, X_test_imp, y_train_imp, y_test_imp = train_test_split(
                            X_imputed, y_imputed, test_size=0.3, random_state=42, stratify=y_imputed
                        )
                        
                        # Train model on imputed data
                        model = RandomForestClassifier(n_estimators=100, random_state=42)
                        model.fit(X_train_imp, y_train_imp)
                        pred = model.predict(X_test_imp)
                        accuracy = accuracy_score(y_test_imp, pred)
                        
                        model_results[method_name] = accuracy
                        print(f"{method_name} imputation accuracy: {accuracy:.4f}")
                        
                except Exception as e:
                    print(f"Error with {method_name}: {e}")
                    model_results[method_name] = 0
    
    # 3.2 Quality Assessment
    print("\n3.2 QUALITY ASSESSMENT")
    print("-" * 30)
    
    quality_scores = {}
    
    for method_name, imputed_df in imputation_results.items():
        score = 0
        
        # Check completeness
        completeness = (1 - imputed_df.isnull().sum().sum() / (len(imputed_df) * len(imputed_df.columns))) * 100
        if completeness == 100:
            score += 2
        elif completeness > 95:
            score += 1
        
        # Check data type preservation
        type_preservation = (imputed_df.dtypes == original_df.dtypes).mean()
        if type_preservation == 1:
            score += 1
        
        # Check for extreme values
        numeric_cols = imputed_df.select_dtypes(include=[np.number]).columns
        extreme_values = 0
        for col in numeric_cols:
            if col in original_df.columns:
                Q1 = original_df[col].quantile(0.25)
                Q3 = original_df[col].quantile(0.75)
                IQR = Q3 - Q1
                extreme_count = ((imputed_df[col] < Q1 - 1.5*IQR) | (imputed_df[col] > Q3 + 1.5*IQR)).sum()
                extreme_values += extreme_count
        
        if extreme_values == 0:
            score += 1
        
        quality_scores[method_name] = score
        print(f"{method_name}: Quality score = {score}/4")
    
    # 3.3 Final Recommendations
    print("\n3.3 FINAL RECOMMENDATIONS")
    print("-" * 30)
    
    # Find best method based on quality scores
    best_quality_method = max(quality_scores, key=quality_scores.get)
    print(f"Best quality method: {best_quality_method} (Score: {quality_scores[best_quality_method]}/4)")
    
    # Find best method based on model performance
    if 'model_results' in locals() and model_results:
        best_model_method = max(model_results, key=model_results.get)
        print(f"Best model performance: {best_model_method} (Accuracy: {model_results[best_model_method]:.4f})")
    
    # Overall recommendation
    print(f"\nOverall recommendation: Use {best_quality_method} imputation method")
    
    return imputation_results, quality_scores, model_results if 'model_results' in locals() else {}

def create_comprehensive_report(original_df, imputation_results, quality_scores, model_results):
    """
    Create comprehensive report of all 3 phases
    """
    print("\n" + "=" * 60)
    print("COMPREHENSIVE DATA QUALITY ANALYSIS REPORT")
    print("=" * 60)
    
    # Summary statistics
    print(f"\nDataset Summary:")
    print(f"  Original records: {len(original_df)}")
    print(f"  Variables: {len(original_df.columns)}")
    print(f"  Missing values: {original_df.isnull().sum().sum()}")
    
    # Phase 1 results
    print(f"\nPhase 1 - Data Quality Assessment:")
    print(f"  Completeness: {(1 - original_df.isnull().sum().sum() / (len(original_df) * len(original_df.columns))) * 100:.2f}%")
    print(f"  Variables with missing data: {(original_df.isnull().sum() > 0).sum()}")
    
    # Phase 2 results
    print(f"\nPhase 2 - Imputation Implementation:")
    for method in imputation_results.keys():
        imputed_df = imputation_results[method]
        completeness = (1 - imputed_df.isnull().sum().sum() / (len(imputed_df) * len(imputed_df.columns))) * 100
        print(f"  {method}: {completeness:.2f}% completeness")
    
    # Phase 3 results
    print(f"\nPhase 3 - Integration and Validation:")
    print(f"  Quality scores: {quality_scores}")
    if model_results:
        print(f"  Model performance: {model_results}")
    
    # Save final imputed dataset
    best_method = max(quality_scores, key=quality_scores.get)
    final_dataset = imputation_results[best_method]
    final_dataset.to_csv('final_imputed_dataset.csv', index=False)
    print(f"\nFinal imputed dataset saved as 'final_imputed_dataset.csv' using {best_method} method")
    
    return final_dataset

def main():
    """
    Main execution function implementing all 3 phases
    """
    print("COMPREHENSIVE DATA QUALITY ANALYSIS - 3 PHASES")
    print("ATPA Assessment - June to August 2025")
    print("=" * 60)
    
    # Phase 1: Data Quality Assessment
    original_df, missing_df, variables_with_missing = phase1_data_quality_assessment(None)
    
    # Phase 2: Imputation Implementation
    imputation_results = phase2_imputation_implementation(original_df, variables_with_missing)
    
    # Phase 3: Integration and Validation
    imputation_results, quality_scores, model_results = phase3_integration_validation(imputation_results, original_df)
    
    # Create comprehensive report
    final_dataset = create_comprehensive_report(original_df, imputation_results, quality_scores, model_results)
    
    print("\n" + "=" * 60)
    print("ALL 3 PHASES COMPLETED SUCCESSFULLY")
    print("=" * 60)
    
    return final_dataset

if __name__ == "__main__":
    final_dataset = main() 