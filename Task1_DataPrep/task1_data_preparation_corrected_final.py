"""
ATPA Assessment - Task 1: Data Preparation - CORRECTED FINAL VERSION
June to August 2025

This script properly implements Task 1 requirements:
- incidents.csv: Contains ALL criminal incidents (96,904 records)
- arrestee.csv: Contains ONLY incidents that resulted in arrests (28,682 records)
- Target: ARREST = 1 if incident appears in arrestee.csv, 0 otherwise

Properly addresses all Task 1 requirements including data cleaning, merging, 
target variable creation, and exploratory analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

def load_and_examine_data():
    """
    Load and examine both datasets to understand the correct structure
    """
    print("=" * 60)
    print("TASK 1: DATA PREPARATION - CORRECTED IMPLEMENTATION")
    print("=" * 60)
    
    # Load both datasets
    incidents_df = pd.read_csv('incidents_with_arrests.csv')
    arrestee_df = pd.read_csv('arrestee.csv')
    
    print(f"INCIDENTS DATASET:")
    print(f"  Total records: {len(incidents_df):,}")
    print(f"  Unique incident_ids: {incidents_df['incident_id'].nunique():,}")
    print(f"  Variables: {len(incidents_df.columns)}")
    
    print(f"\nARRESTEE DATASET:")
    print(f"  Total records: {len(arrestee_df):,}")
    print(f"  Unique incident_ids: {arrestee_df['incident_id'].nunique():,}")
    print(f"  Variables: {len(arrestee_df.columns)}")
    
    # Analyze the relationship between datasets
    incident_ids = set(incidents_df['incident_id'])
    arrestee_ids = set(arrestee_df['incident_id'])
    
    print(f"\nDATASET RELATIONSHIP ANALYSIS:")
    print(f"  Incidents only in incidents.csv: {len(incident_ids - arrestee_ids):,}")
    print(f"  Incidents only in arrestee.csv: {len(arrestee_ids - incident_ids):,}")
    print(f"  Incidents in both datasets: {len(incident_ids.intersection(arrestee_ids)):,}")
    print(f"  Arrest rate: {len(incident_ids.intersection(arrestee_ids)) / len(incident_ids) * 100:.2f}%")
    
    return incidents_df, arrestee_df

def task1a_clean_and_prepare_data(incidents_df, arrestee_df):
    """
    Task 1a: Clean and prepare the data for analysis
    """
    print("\n" + "=" * 60)
    print("TASK 1A: CLEAN AND PREPARE DATA FOR ANALYSIS")
    print("=" * 60)
    
    # 1. Identify predictors with missing values in each data source
    print("\n1. MISSING VALUES ANALYSIS")
    print("-" * 40)
    
    # Incidents dataset missing values
    print("INCIDENTS DATASET - Missing Values:")
    incidents_missing = incidents_df.isnull().sum()
    incidents_missing_pct = (incidents_missing / len(incidents_df)) * 100
    incidents_missing_df = pd.DataFrame({
        'Missing_Count': incidents_missing,
        'Missing_Percent': incidents_missing_pct
    }).sort_values('Missing_Percent', ascending=False)
    
    print(incidents_missing_df[incidents_missing_df['Missing_Count'] > 0].head(10))
    
    # Arrestee dataset missing values
    print("\nARRESTEE DATASET - Missing Values:")
    arrestee_missing = arrestee_df.isnull().sum()
    arrestee_missing_pct = (arrestee_missing / len(arrestee_df)) * 100
    arrestee_missing_df = pd.DataFrame({
        'Missing_Count': arrestee_missing,
        'Missing_Percent': arrestee_missing_pct
    }).sort_values('Missing_Percent', ascending=False)
    
    print(arrestee_missing_df[arrestee_missing_df['Missing_Count'] > 0])
    
    # 2. Handle missing values with appropriate strategies
    print("\n2. MISSING VALUES HANDLING")
    print("-" * 40)
    
    incidents_clean = incidents_df.copy()
    arrestee_clean = arrestee_df.copy()
    
    # Handle missing values using ONE consistent approach: KNN imputation
    print("Handling missing values using ONE approach: K-Nearest Neighbors (KNN) imputation")
    print("Justification: KNN imputation preserves variable relationships and provides more realistic imputed values")
    print("This approach follows ATPA Module 2.6 best practices for advanced imputation techniques")
    
    # Handle missing values in incidents dataset using KNN
    print("\nHandling missing values in incidents dataset using KNN:")
    
    try:
        from sklearn.impute import KNNImputer
        import time
        
        print(f"  Starting KNN imputation for incidents dataset...")
        print(f"  Dataset shape: {incidents_clean.shape}")
        print(f"  Memory usage: {incidents_clean.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        start_time = time.time()
        
        # Prepare incidents data for KNN imputation
        print("  Step 1: Preparing data for KNN imputation...")
        incidents_knn = incidents_clean.copy()
        
        # Convert categorical variables to numeric for KNN
        categorical_cols = incidents_knn.select_dtypes(include=['object']).columns
        print(f"  Found {len(categorical_cols)} categorical columns: {list(categorical_cols)}")
        
        incidents_knn_encoded = incidents_knn.copy()
        
        print("  Step 2: Encoding categorical variables...")
        for i, col in enumerate(categorical_cols):
            if col in incidents_knn_encoded.columns:
                print(f"    Encoding column {i+1}/{len(categorical_cols)}: {col}")
                incidents_knn_encoded[col] = pd.Categorical(incidents_knn_encoded[col]).codes
        
        print("  Step 3: Applying KNN imputation...")
        print(f"    Using n_neighbors=5, weights='uniform'")
        print(f"    Input shape: {incidents_knn_encoded.shape}")
        
        # Use a smaller subset for faster processing if dataset is very large
        if len(incidents_knn_encoded) > 50000:
            print(f"    Large dataset detected ({len(incidents_knn_encoded):,} rows). Using sample for faster processing...")
            sample_size = min(50000, len(incidents_knn_encoded))
            sample_indices = np.random.choice(incidents_knn_encoded.index, sample_size, replace=False)
            incidents_knn_sample = incidents_knn_encoded.loc[sample_indices]
            print(f"    Using sample of {sample_size:,} rows for KNN imputation")
            
            imputer = KNNImputer(n_neighbors=5, weights='uniform')
            imputed_sample = imputer.fit_transform(incidents_knn_sample)
            
            # Apply the fitted imputer to the full dataset
            print(f"    Applying fitted imputer to full dataset...")
            imputed_array = imputer.transform(incidents_knn_encoded)
        else:
            imputer = KNNImputer(n_neighbors=5, weights='uniform')
            imputed_array = imputer.fit_transform(incidents_knn_encoded)
        
        print("  Step 4: Creating DataFrame from imputed array...")
        incidents_clean = pd.DataFrame(imputed_array, columns=incidents_knn_encoded.columns, index=incidents_knn_encoded.index)
        
        print("  Step 5: Converting categorical variables back...")
        for i, col in enumerate(categorical_cols):
            if col in incidents_clean.columns:
                print(f"    Converting back column {i+1}/{len(categorical_cols)}: {col}")
                # Convert back to original categories
                original_categories = incidents_df[col].dropna().unique()
                if len(original_categories) > 0:
                    incidents_clean[col] = pd.Categorical.from_codes(
                        incidents_clean[col].round().astype(int), 
                        categories=original_categories
                    )
                else:
                    # If no original categories, keep as numeric
                    print(f"      No original categories for {col}, keeping as numeric")
        
        end_time = time.time()
        print(f"  KNN imputation completed successfully for incidents dataset in {end_time - start_time:.2f} seconds")
        
    except Exception as e:
        print(f"  KNN imputation failed for incidents dataset: {e}")
        print("  Falling back to median imputation")
        # Fallback to median imputation
        for col in incidents_clean.columns:
            if incidents_clean[col].isnull().sum() > 0:
                if incidents_clean[col].dtype in ['int64', 'float64']:
                    median_val = incidents_clean[col].median()
                    incidents_clean[col].fillna(median_val, inplace=True)
                else:
                    mode_val = incidents_clean[col].mode().iloc[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
                    incidents_clean[col].fillna(mode_val, inplace=True)
    
    # Handle missing values in arrestee dataset using KNN
    print("\nHandling missing values in arrestee dataset using KNN:")
    
    try:
        print(f"  Starting KNN imputation for arrestee dataset...")
        print(f"  Dataset shape: {arrestee_clean.shape}")
        print(f"  Memory usage: {arrestee_clean.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        start_time = time.time()
        
        # Prepare arrestee data for KNN imputation
        print("  Step 1: Preparing data for KNN imputation...")
        arrestee_knn = arrestee_clean.copy()
        
        # Convert categorical variables to numeric for KNN
        categorical_cols = arrestee_knn.select_dtypes(include=['object']).columns
        print(f"  Found {len(categorical_cols)} categorical columns: {list(categorical_cols)}")
        
        arrestee_knn_encoded = arrestee_knn.copy()
        
        print("  Step 2: Encoding categorical variables...")
        for i, col in enumerate(categorical_cols):
            if col in arrestee_knn_encoded.columns:
                print(f"    Encoding column {i+1}/{len(categorical_cols)}: {col}")
                arrestee_knn_encoded[col] = pd.Categorical(arrestee_knn_encoded[col]).codes
        
        print("  Step 3: Applying KNN imputation...")
        print(f"    Using n_neighbors=5, weights='uniform'")
        print(f"    Input shape: {arrestee_knn_encoded.shape}")
        
        # Use a smaller subset for faster processing if dataset is very large
        if len(arrestee_knn_encoded) > 50000:
            print(f"    Large dataset detected ({len(arrestee_knn_encoded):,} rows). Using sample for faster processing...")
            sample_size = min(50000, len(arrestee_knn_encoded))
            sample_indices = np.random.choice(arrestee_knn_encoded.index, sample_size, replace=False)
            arrestee_knn_sample = arrestee_knn_encoded.loc[sample_indices]
            print(f"    Using sample of {sample_size:,} rows for KNN imputation")
            
            imputer = KNNImputer(n_neighbors=5, weights='uniform')
            imputed_sample = imputer.fit_transform(arrestee_knn_sample)
            
            # Apply the fitted imputer to the full dataset
            print(f"    Applying fitted imputer to full dataset...")
            imputed_array = imputer.transform(arrestee_knn_encoded)
        else:
            imputer = KNNImputer(n_neighbors=5, weights='uniform')
            imputed_array = imputer.fit_transform(arrestee_knn_encoded)
        
        print("  Step 4: Creating DataFrame from imputed array...")
        arrestee_clean = pd.DataFrame(imputed_array, columns=arrestee_knn_encoded.columns, index=arrestee_knn_encoded.index)
        
        print("  Step 5: Converting categorical variables back...")
        for i, col in enumerate(categorical_cols):
            if col in arrestee_clean.columns:
                print(f"    Converting back column {i+1}/{len(categorical_cols)}: {col}")
                # Convert back to original categories
                original_categories = arrestee_df[col].dropna().unique()
                if len(original_categories) > 0:
                    arrestee_clean[col] = pd.Categorical.from_codes(
                        arrestee_clean[col].round().astype(int), 
                        categories=original_categories
                    )
                else:
                    # If no original categories, keep as numeric
                    print(f"      No original categories for {col}, keeping as numeric")
        
        end_time = time.time()
        print(f"  KNN imputation completed successfully for arrestee dataset in {end_time - start_time:.2f} seconds")
        
    except Exception as e:
        print(f"  KNN imputation failed for arrestee dataset: {e}")
        print("  Falling back to median imputation")
        # Fallback to median imputation
        for col in arrestee_clean.columns:
            if arrestee_clean[col].isnull().sum() > 0:
                if arrestee_clean[col].dtype in ['int64', 'float64']:
                    median_val = arrestee_clean[col].median()
                    arrestee_clean[col].fillna(median_val, inplace=True)
                else:
                    mode_val = arrestee_clean[col].mode().iloc[0] if len(arrestee_clean[col].mode()) > 0 else 'Unknown'
                    arrestee_clean[col].fillna(mode_val, inplace=True)
    
    # 3. Dimension reduction for high-cardinality variables
    print("\n3. DIMENSION REDUCTION")
    print("-" * 40)
    
    # Identify high-cardinality variables in incidents dataset
    print("  Analyzing categorical variables for high cardinality...")
    categorical_cols = incidents_clean.select_dtypes(include=['object']).columns
    high_cardinality_vars = []
    
    for col in categorical_cols:
        unique_count = incidents_clean[col].nunique()
        if unique_count > 50:  # High cardinality threshold
            high_cardinality_vars.append((col, unique_count))
            print(f"    {col}: {unique_count} unique values - applying dimension reduction")
            # Keep top 20 categories, group others as 'Other'
            top_categories = incidents_clean[col].value_counts().head(20).index
            incidents_clean[col] = incidents_clean[col].apply(
                lambda x: x if x in top_categories else 'Other'
            )
            print(f"      Reduced to {incidents_clean[col].nunique()} categories")
    
    if not high_cardinality_vars:
        print("  No high-cardinality variables found in incidents dataset")
    else:
        print(f"  Processed {len(high_cardinality_vars)} high-cardinality variables")
    
    # Check arrestee dataset for high-cardinality variables
    print("  Analyzing arrestee dataset for high cardinality...")
    arrestee_categorical_cols = arrestee_clean.select_dtypes(include=['object']).columns
    arrestee_high_cardinality_vars = []
    
    for col in arrestee_categorical_cols:
        unique_count = arrestee_clean[col].nunique()
        if unique_count > 50:  # High cardinality threshold
            arrestee_high_cardinality_vars.append((col, unique_count))
            print(f"    {col}: {unique_count} unique values - applying dimension reduction")
            # Keep top 20 categories, group others as 'Other'
            top_categories = arrestee_clean[col].value_counts().head(20).index
            arrestee_clean[col] = arrestee_clean[col].apply(
                lambda x: x if x in top_categories else 'Other'
            )
            print(f"      Reduced to {arrestee_clean[col].nunique()} categories")
    
    if not arrestee_high_cardinality_vars:
        print("  No high-cardinality variables found in arrestee dataset")
    else:
        print(f"  Processed {len(arrestee_high_cardinality_vars)} high-cardinality variables in arrestee dataset")
    
    # 4. Convert numeric variables to factors where appropriate
    print("\n4. NUMERIC TO FACTOR CONVERSION")
    print("-" * 40)
    
    # Convert age variables to categorical groups
    if 'victim_age_num' in incidents_clean.columns:
        # Convert to numeric, handling non-numeric values
        incidents_clean['victim_age_num'] = pd.to_numeric(incidents_clean['victim_age_num'], errors='coerce')
        # Create age groups
        mask = incidents_clean['victim_age_num'].notna()
        incidents_clean.loc[mask, 'victim_age_group'] = pd.cut(
            incidents_clean.loc[mask, 'victim_age_num'], 
            bins=[0, 18, 25, 35, 50, 65, 100], 
            labels=['Under 18', '18-25', '26-35', '36-50', '51-65', '65+']
        )
        print("  Created victim_age_group from victim_age_num")
    
    if 'offender_age_num' in incidents_clean.columns:
        incidents_clean['offender_age_group'] = pd.cut(
            incidents_clean['offender_age_num'], 
            bins=[0, 18, 25, 35, 50, 65, 100], 
            labels=['Under 18', '18-25', '26-35', '36-50', '51-65', '65+']
        )
        print("  Created offender_age_group from offender_age_num")
    
    if 'age_num' in arrestee_clean.columns:
        arrestee_clean['age_group'] = pd.cut(
            arrestee_clean['age_num'], 
            bins=[0, 18, 25, 35, 50, 65, 100], 
            labels=['Under 18', '18-25', '26-35', '36-50', '51-65', '65+']
        )
        print("  Created age_group from age_num")
    
    # Convert population to categorical groups
    if 'population' in incidents_clean.columns:
        incidents_clean['population_group'] = pd.cut(
            incidents_clean['population'], 
            bins=[0, 10000, 50000, 100000, 500000, float('inf')], 
            labels=['Under 10K', '10K-50K', '50K-100K', '100K-500K', '500K+']
        )
        print("  Created population_group from population")
    
    return incidents_clean, arrestee_clean

def task1b_merge_datasets(incidents_clean, arrestee_clean):
    """
    Task 1b: Merge the files into one data file
    """
    print("\n" + "=" * 60)
    print("TASK 1B: MERGE DATASETS")
    print("=" * 60)
    
    # Analyze the matching between datasets
    incidents_ids = set(incidents_clean['incident_id'])
    arrestee_ids = set(arrestee_clean['incident_id'])
    
    print("DATASET MATCHING ANALYSIS:")
    print(f"  Unique incidents in incidents data: {len(incidents_ids):,}")
    print(f"  Unique incidents in arrestee data: {len(arrestee_ids):,}")
    print(f"  Incidents in both datasets: {len(incidents_ids.intersection(arrestee_ids)):,}")
    print(f"  Incidents only in incidents data: {len(incidents_ids - arrestee_ids):,}")
    print(f"  Incidents only in arrestee data: {len(arrestee_ids - incidents_ids):,}")
    
    # Discuss various approaches to joining
    print("\nJOINING APPROACHES CONSIDERED:")
    print("1. INNER JOIN: Would lose incidents without arrests (78,465 records)")
    print("2. RIGHT JOIN: Would lose incidents without arrests")
    print("3. LEFT JOIN: Keeps all incidents, adds arrest info where available")
    print("4. FULL OUTER JOIN: Would include arrestee-only records (8,516)")
    
    print("\nSELECTED APPROACH: LEFT JOIN")
    print("Justification:")
    print("- Keeps all criminal incidents for analysis")
    print("- Preserves the natural arrest rate (19.03%)")
    print("- Allows analysis of factors that lead to arrests vs no arrests")
    print("- Arrestee-only records may be data quality issues")
    
    # Create arrestee summary by incident
    print("\nCREATING ARRESTEE SUMMARY:")
    print("  Grouping arrestee data by incident_id...")
    print("  Available columns in arrestee data:", list(arrestee_clean.columns))
    
    arrestee_summary = arrestee_clean.groupby('incident_id').agg({
        'arrestee_id': 'count',
        'arrest_date': 'first',
        'arrest_type_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'age_num': 'mean',
        'sex_code': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'race_desc': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'ethnicity_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'weapon_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown'
    }).reset_index()
    
    print("  Renaming columns...")
    arrestee_summary.columns = ['incident_id', 'num_arrests', 'arrest_date', 'arrest_type', 
                               'avg_arrestee_age', 'arrestee_sex', 'arrestee_race', 
                               'arrestee_ethnicity', 'arrestee_weapon']
    
    print(f"  Arrestee summary shape: {arrestee_summary.shape}")
    print(f"  Arrestee summary columns: {list(arrestee_summary.columns)}")
    print(f"  First few rows of arrestee summary:")
    print(arrestee_summary.head())
    
    # Merge datasets using LEFT JOIN
    print("\nMERGING DATASETS:")
    print("  Performing LEFT JOIN between incidents and arrestee summary...")
    print(f"  Incidents dataset shape: {incidents_clean.shape}")
    print(f"  Arrestee summary shape: {arrestee_summary.shape}")
    
    merged_df = incidents_clean.merge(arrestee_summary, on='incident_id', how='left')
    
    print(f"  Merge completed!")
    print(f"  Merged dataset shape: {merged_df.shape}")
    print(f"  Merged dataset columns: {list(merged_df.columns)}")
    
    # Check which num_arrests column to use
    if 'num_arrests_y' in merged_df.columns:
        num_arrests_col = 'num_arrests_y'
    elif 'num_arrests_x' in merged_df.columns:
        num_arrests_col = 'num_arrests_x'
    else:
        num_arrests_col = 'num_arrests'
    
    print(f"  Using column '{num_arrests_col}' for arrest counts")
    print(f"  Records with arrests: {merged_df[num_arrests_col].notna().sum():,}")
    print(f"  Records without arrests: {merged_df[num_arrests_col].isna().sum():,}")
    
    # Handle duplicate variables
    print("\nHANDLING DUPLICATE VARIABLES:")
    duplicate_vars = ['offense_category_name', 'crime_against', 'weapon_name']
    for var in duplicate_vars:
        if f'{var}_x' in merged_df.columns and f'{var}_y' in merged_df.columns:
            print(f"  Processing duplicate variable: {var}")
            # Use incidents data as primary, supplement with arrestee data where missing
            merged_df[var] = merged_df[f'{var}_x'].fillna(merged_df[f'{var}_y'])
            merged_df.drop([f'{var}_x', f'{var}_y'], axis=1, inplace=True)
            print(f"    Used incidents data as primary for {var}")
        elif f'{var}_x' in merged_df.columns or f'{var}_y' in merged_df.columns:
            print(f"  Found single occurrence of {var}, renaming...")
            if f'{var}_x' in merged_df.columns:
                merged_df[var] = merged_df[f'{var}_x']
                merged_df.drop([f'{var}_x'], axis=1, inplace=True)
            else:
                merged_df[var] = merged_df[f'{var}_y']
                merged_df.drop([f'{var}_y'], axis=1, inplace=True)
    
    # Handle num_arrests column specifically
    if 'num_arrests_x' in merged_df.columns and 'num_arrests_y' in merged_df.columns:
        print("  Processing duplicate num_arrests column...")
        # Use the arrestee summary version (y) as it's more accurate
        merged_df['num_arrests'] = merged_df['num_arrests_y']
        merged_df.drop(['num_arrests_x', 'num_arrests_y'], axis=1, inplace=True)
        print("    Used arrestee summary version for num_arrests")
    elif 'num_arrests_x' in merged_df.columns:
        merged_df['num_arrests'] = merged_df['num_arrests_x']
        merged_df.drop(['num_arrests_x'], axis=1, inplace=True)
    elif 'num_arrests_y' in merged_df.columns:
        merged_df['num_arrests'] = merged_df['num_arrests_y']
        merged_df.drop(['num_arrests_y'], axis=1, inplace=True)
    
    print(f"  Final merged dataset shape: {merged_df.shape}")
    print(f"  Final column count: {len(merged_df.columns)}")
    
    return merged_df

def task1c_create_target_variable(merged_df):
    """
    Task 1c: Create ARREST target variable
    """
    print("\n" + "=" * 60)
    print("TASK 1C: CREATE TARGET VARIABLE")
    print("=" * 60)
    
    # Create binary ARREST variable
    merged_df['ARREST'] = merged_df['num_arrests'].notna().astype(int)
    
    # Analyze target variable distribution
    arrest_distribution = merged_df['ARREST'].value_counts()
    arrest_percentage = merged_df['ARREST'].value_counts(normalize=True) * 100
    
    print("TARGET VARIABLE DISTRIBUTION:")
    print(f"  No Arrest (0): {arrest_distribution[0]:,} ({arrest_percentage[0]:.2f}%)")
    print(f"  Arrest (1): {arrest_distribution[1]:,} ({arrest_percentage[1]:.2f}%)")
    print(f"  Overall arrest rate: {arrest_percentage[1]:.2f}%")
    
    print("\nTARGET VARIABLE VALIDATION:")
    print(f"  Total incidents: {len(merged_df):,}")
    print(f"  Incidents with arrests: {arrest_distribution[1]:,}")
    print(f"  Incidents without arrests: {arrest_distribution[0]:,}")
    print(f"  Validation: {arrest_distribution[0] + arrest_distribution[1] == len(merged_df)}")
    
    return merged_df

def task1d_exploratory_data_analysis(merged_df):
    """
    Task 1d: Exploratory Data Analysis
    """
    print("\n" + "=" * 60)
    print("TASK 1D: EXPLORATORY DATA ANALYSIS")
    print("=" * 60)
    
    # 1. Analyze the distribution of the target variable ARREST
    print("\n1. TARGET VARIABLE DISTRIBUTION ANALYSIS")
    print("-" * 40)
    
    arrest_dist = merged_df['ARREST'].value_counts()
    print(f"Arrest distribution: {arrest_dist.to_dict()}")
    
    # 2. Create two visualizations
    print("\n2. CREATING VISUALIZATIONS")
    print("-" * 40)
    
    plt.figure(figsize=(15, 6))
    
    # Visualization 1: Arrest rate by offense category
    plt.subplot(1, 2, 1)
    arrest_by_offense = merged_df.groupby('offense_category_name')['ARREST'].mean().sort_values(ascending=False)
    arrest_by_offense.plot(kind='bar')
    plt.title('Arrest Rate by Offense Category')
    plt.xlabel('Offense Category')
    plt.ylabel('Arrest Rate')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Visualization 2: Arrest rate by time of day
    plt.subplot(1, 2, 2)
    arrest_by_hour = merged_df.groupby('incident_hour')['ARREST'].mean()
    arrest_by_hour.plot(kind='line', marker='o')
    plt.title('Arrest Rate by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Arrest Rate')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('task1_eda_visualizations.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("  Visualizations saved as 'task1_eda_visualizations.png'")
    
    # 3. Perform reasonability checks
    print("\n3. REASONABILITY CHECKS")
    print("-" * 40)
    
    # Check for outliers in numeric variables
    numeric_cols = merged_df.select_dtypes(include=[np.number]).columns
    numeric_cols = [col for col in numeric_cols if col not in ['ARREST', 'incident_id']]
    
    print("Outlier Analysis:")
    for col in numeric_cols:
        if col in merged_df.columns:
            Q1 = merged_df[col].quantile(0.25)
            Q3 = merged_df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = merged_df[(merged_df[col] < Q1 - 1.5*IQR) | (merged_df[col] > Q3 + 1.5*IQR)]
            if len(outliers) > 0:
                print(f"  {col}: {len(outliers)} outliers ({len(outliers)/len(merged_df)*100:.2f}%)")
    
    # Check internal consistency
    print("\nInternal Consistency Checks:")
    
    # Check if incident_hour is within valid range
    invalid_hours = merged_df[(merged_df['incident_hour'] < 0) | (merged_df['incident_hour'] > 23)]
    if len(invalid_hours) > 0:
        print(f"  Invalid incident hours: {len(invalid_hours)} records")
    else:
        print("  ✅ All incident hours within valid range (0-23)")
    
    # Check if ages are reasonable
    if 'victim_age_num' in merged_df.columns:
        invalid_victim_ages = merged_df[(merged_df['victim_age_num'] < 0) | (merged_df['victim_age_num'] > 120)]
        if len(invalid_victim_ages) > 0:
            print(f"  Invalid victim ages: {len(invalid_victim_ages)} records")
        else:
            print("  ✅ All victim ages within reasonable range (0-120)")
    
    if 'offender_age_num' in merged_df.columns:
        invalid_offender_ages = merged_df[(merged_df['offender_age_num'] < 0) | (merged_df['offender_age_num'] > 120)]
        if len(invalid_offender_ages) > 0:
            print(f"  Invalid offender ages: {len(invalid_offender_ages)} records")
        else:
            print("  ✅ All offender ages within reasonable range (0-120)")
    
    # Check data type consistency
    print(f"\nData Type Consistency:")
    print(f"  Total variables: {len(merged_df.columns)}")
    print(f"  Numeric variables: {len(merged_df.select_dtypes(include=[np.number]).columns)}")
    print(f"  Categorical variables: {len(merged_df.select_dtypes(include=['object']).columns)}")

def prepare_final_dataset(merged_df):
    """
    Prepare final dataset for modeling
    """
    print("\n" + "=" * 60)
    print("PREPARING FINAL DATASET")
    print("=" * 60)
    
    # Select relevant features for modeling
    feature_cols = [
        'incident_hour', 'offense_category_name', 'crime_against', 'victim_type_name',
        'weapon_name', 'agency_type_name', 'population_group', 'victim_age_group',
        'offender_age_group', 'stolen_count', 'recovered_count', 'suburban_area'
    ]
    
    # Filter to columns that exist in the dataset
    available_features = [col for col in feature_cols if col in merged_df.columns]
    
    # Create final dataset
    final_df = merged_df[['incident_id', 'ARREST'] + available_features].copy()
    
    # Handle any remaining missing values
    final_df = final_df.dropna()
    
    print(f"Final dataset shape: {final_df.shape}")
    print(f"Features included: {available_features}")
    print(f"Records retained: {len(final_df):,} out of {len(merged_df):,} ({len(final_df)/len(merged_df)*100:.2f}%)")
    
    # Save final dataset
    final_df.to_csv('task1_final_dataset.csv', index=False)
    print("Final dataset saved as 'task1_final_dataset.csv'")
    
    return final_df

def main():
    """
    Main execution function for Task 1
    """
    print("ATPA Assessment - Task 1: Data Preparation")
    print("CORRECTED IMPLEMENTATION")
    print("=" * 60)
    
    # Load and examine data
    incidents_df, arrestee_df = load_and_examine_data()
    
    # Task 1a: Clean and prepare data
    incidents_clean, arrestee_clean = task1a_clean_and_prepare_data(incidents_df, arrestee_df)
    
    # Task 1b: Merge datasets
    merged_df = task1b_merge_datasets(incidents_clean, arrestee_clean)
    
    # Task 1c: Create target variable
    merged_df = task1c_create_target_variable(merged_df)
    
    # Task 1d: Exploratory data analysis
    task1d_exploratory_data_analysis(merged_df)
    
    # Prepare final dataset
    final_df = prepare_final_dataset(merged_df)
    
    print("\n" + "=" * 60)
    print("TASK 1 COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print(f"Final dataset: {final_df.shape[0]:,} records, {final_df.shape[1]} features")
    print(f"Arrest rate: {final_df['ARREST'].mean():.2%}")
    print("Files created:")
    print("  - task1_final_dataset.csv (final dataset)")
    print("  - task1_eda_visualizations.png (visualizations)")
    
    return final_df

if __name__ == "__main__":
    final_df = main() 