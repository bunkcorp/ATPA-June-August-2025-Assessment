"""
ATPA Assessment - June to August 2025
Task 1: Data Preparation - Complete Implementation

This script performs comprehensive data preparation for the NMInsights crime analysis project.
Addresses all Task 1 requirements including data cleaning, merging, target variable creation, and EDA.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

def load_and_examine_data():
    """
    Load and examine both incidents and arrestee data to understand structure
    """
    print("=== LOADING AND EXAMINING DATA ===")
    
    # Load incidents data
    incidents_df = pd.read_csv('incidents.csv')
    print(f"Incidents data shape: {incidents_df.shape}")
    print(f"Incidents columns: {incidents_df.columns.tolist()}")
    
    # Load arrestee data
    arrestee_df = pd.read_csv('arrestee.csv')
    print(f"Arrestee data shape: {arrestee_df.shape}")
    print(f"Arrestee columns: {arrestee_df.columns.tolist()}")
    
    # Load data dictionary
    try:
        data_dict = pd.read_excel('Data_Dictionary.xlsx')
        print(f"Data dictionary shape: {data_dict.shape}")
    except:
        print("Data dictionary not found, proceeding without it")
        data_dict = None
    
    # Display basic info about both datasets
    print("\n=== INCIDENTS DATA INFO ===")
    print(incidents_df.info())
    
    print("\n=== ARRESTEE DATA INFO ===")
    print(arrestee_df.info())
    
    print("\n=== INCIDENTS DATA SAMPLE ===")
    print(incidents_df.head())
    
    print("\n=== ARRESTEE DATA SAMPLE ===")
    print(arrestee_df.head())
    
    return incidents_df, arrestee_df, data_dict

def analyze_missing_values(incidents_df, arrestee_df):
    """
    Analyze missing values in both datasets
    """
    print("\n=== MISSING VALUES ANALYSIS ===")
    
    # Incidents missing values
    print("Missing values in incidents data:")
    missing_incidents = incidents_df.isnull().sum()
    missing_incidents_percent = (missing_incidents / len(incidents_df)) * 100
    missing_incidents_df = pd.DataFrame({
        'Missing_Count': missing_incidents,
        'Missing_Percent': missing_incidents_percent
    }).sort_values('Missing_Percent', ascending=False)
    
    print(missing_incidents_df[missing_incidents_df['Missing_Count'] > 0])
    
    # Arrestee missing values
    print("\nMissing values in arrestee data:")
    missing_arrestee = arrestee_df.isnull().sum()
    missing_arrestee_percent = (missing_arrestee / len(arrestee_df)) * 100
    missing_arrestee_df = pd.DataFrame({
        'Missing_Count': missing_arrestee,
        'Missing_Percent': missing_arrestee_percent
    }).sort_values('Missing_Percent', ascending=False)
    
    print(missing_arrestee_df[missing_arrestee_df['Missing_Count'] > 0])
    
    return missing_incidents_df, missing_arrestee_df

def handle_missing_values(incidents_df, arrestee_df):
    """
    Handle missing values in both datasets with appropriate strategies
    """
    print("\n=== HANDLING MISSING VALUES ===")
    
    # Create copies to avoid modifying original data
    incidents_clean = incidents_df.copy()
    arrestee_clean = arrestee_df.copy()
    
    # Handle missing values in incidents data
    print("Handling missing values in incidents data...")
    
    # Categorical variables - mode imputation
    categorical_cols_incidents = ['offense_category_name', 'crime_against', 'victim_type_name', 
                                 'weapon_name', 'agency_name', 'agency_type_name', 'county_name']
    
    for col in categorical_cols_incidents:
        if col in incidents_clean.columns and incidents_clean[col].isnull().sum() > 0:
            mode_val = incidents_clean[col].mode().iloc[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
            incidents_clean[col].fillna(mode_val, inplace=True)
            print(f"  Filled missing values in {col} with mode: {mode_val}")
    
    # Numeric variables - median imputation
    numeric_cols_incidents = ['incident_hour', 'victim_age_num', 'offender_age_num', 
                             'stolen_count', 'recovered_count', 'population']
    
    for col in numeric_cols_incidents:
        if col in incidents_clean.columns and incidents_clean[col].isnull().sum() > 0:
            median_val = incidents_clean[col].median()
            incidents_clean[col].fillna(median_val, inplace=True)
            print(f"  Filled missing values in {col} with median: {median_val}")
    
    # Handle missing values in arrestee data
    print("Handling missing values in arrestee data...")
    
    # Categorical variables - mode imputation
    categorical_cols_arrestee = ['arrest_type_name', 'offense_category_name', 'crime_against',
                                'race_desc', 'ethnicity_name', 'resident_code', 'weapon_name']
    
    for col in categorical_cols_arrestee:
        if col in arrestee_clean.columns and arrestee_clean[col].isnull().sum() > 0:
            mode_val = arrestee_clean[col].mode().iloc[0] if len(arrestee_clean[col].mode()) > 0 else 'Unknown'
            arrestee_clean[col].fillna(mode_val, inplace=True)
            print(f"  Filled missing values in {col} with mode: {mode_val}")
    
    # Numeric variables - median imputation
    numeric_cols_arrestee = ['age_num', 'hc_code']
    
    for col in numeric_cols_arrestee:
        if col in arrestee_clean.columns and arrestee_clean[col].isnull().sum() > 0:
            median_val = arrestee_clean[col].median()
            arrestee_clean[col].fillna(median_val, inplace=True)
            print(f"  Filled missing values in {col} with median: {median_val}")
    
    return incidents_clean, arrestee_clean

def perform_dimension_reduction(incidents_clean, arrestee_clean):
    """
    Perform dimension reduction where appropriate
    """
    print("\n=== DIMENSION REDUCTION ===")
    
    # Identify high-cardinality categorical variables
    print("Analyzing categorical variables for dimension reduction...")
    
    # For incidents data
    categorical_cols_incidents = incidents_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols_incidents:
        unique_count = incidents_clean[col].nunique()
        if unique_count > 50:  # High cardinality threshold
            print(f"  High cardinality in incidents.{col}: {unique_count} unique values")
            # Keep top 20 categories, group others as 'Other'
            top_categories = incidents_clean[col].value_counts().head(20).index
            incidents_clean[col] = incidents_clean[col].apply(
                lambda x: x if x in top_categories else 'Other'
            )
            print(f"    Reduced to {incidents_clean[col].nunique()} categories")
    
    # For arrestee data
    categorical_cols_arrestee = arrestee_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols_arrestee:
        unique_count = arrestee_clean[col].nunique()
        if unique_count > 50:  # High cardinality threshold
            print(f"  High cardinality in arrestee.{col}: {unique_count} unique values")
            # Keep top 20 categories, group others as 'Other'
            top_categories = arrestee_clean[col].value_counts().head(20).index
            arrestee_clean[col] = arrestee_clean[col].apply(
                lambda x: x if x in top_categories else 'Other'
            )
            print(f"    Reduced to {arrestee_clean[col].nunique()} categories")
    
    return incidents_clean, arrestee_clean

def convert_numeric_to_factors(incidents_clean, arrestee_clean):
    """
    Convert numeric variables that should be factors
    """
    print("\n=== CONVERTING NUMERIC TO FACTORS ===")
    
    # Convert age groups to categorical
    if 'victim_age_num' in incidents_clean.columns:
        # Convert to numeric, handling non-numeric values
        incidents_clean['victim_age_num'] = pd.to_numeric(incidents_clean['victim_age_num'], errors='coerce')
        # Only create groups for non-null values
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
    
    # Convert population groups to categorical
    if 'population' in incidents_clean.columns:
        incidents_clean['population_group'] = pd.cut(
            incidents_clean['population'], 
            bins=[0, 10000, 50000, 100000, 500000, float('inf')], 
            labels=['Under 10K', '10K-50K', '50K-100K', '100K-500K', '500K+']
        )
        print("  Created population_group from population")
    
    return incidents_clean, arrestee_clean

def merge_datasets(incidents_clean, arrestee_clean):
    """
    Merge incidents and arrestee datasets
    """
    print("\n=== MERGING DATASETS ===")
    
    # Analyze the matching between datasets
    incidents_ids = set(incidents_clean['incident_id'])
    arrestee_ids = set(arrestee_clean['incident_id'])
    
    print(f"Unique incidents in incidents data: {len(incidents_ids)}")
    print(f"Unique incidents in arrestee data: {len(arrestee_ids)}")
    print(f"Incidents in both datasets: {len(incidents_ids.intersection(arrestee_ids))}")
    print(f"Incidents only in incidents data: {len(incidents_ids - arrestee_ids)}")
    print(f"Incidents only in arrestee data: {len(arrestee_ids - incidents_ids)}")
    
    # Create arrestee summary by incident
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
    
    arrestee_summary.columns = ['incident_id', 'num_arrests', 'arrest_date', 'arrest_type', 
                               'avg_arrestee_age', 'arrestee_sex', 'arrestee_race', 
                               'arrestee_ethnicity', 'arrestee_weapon']
    
    # Merge datasets
    merged_df = incidents_clean.merge(arrestee_summary, on='incident_id', how='left')
    
    print(f"Merged dataset shape: {merged_df.shape}")
    print("Merge strategy: LEFT JOIN (keep all incidents, add arrestee info where available)")
    
    return merged_df

def create_target_variable(merged_df):
    """
    Create the ARREST target variable
    """
    print("\n=== CREATING TARGET VARIABLE ===")
    
    # Create binary ARREST variable
    merged_df['ARREST'] = merged_df['num_arrests'].notna().astype(int)
    
    # Analyze target variable distribution
    arrest_distribution = merged_df['ARREST'].value_counts()
    arrest_percentage = merged_df['ARREST'].value_counts(normalize=True) * 100
    
    print("Target variable distribution:")
    print(f"  No Arrest (0): {arrest_distribution[0]:,} ({arrest_percentage[0]:.2f}%)")
    print(f"  Arrest (1): {arrest_distribution[1]:,} ({arrest_percentage[1]:.2f}%)")
    
    return merged_df

def perform_eda(merged_df):
    """
    Perform Exploratory Data Analysis
    """
    print("\n=== EXPLORATORY DATA ANALYSIS ===")
    
    # Create visualizations
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Arrest rate by offense category
    plt.subplot(2, 2, 1)
    arrest_by_offense = merged_df.groupby('offense_category_name')['ARREST'].mean().sort_values(ascending=False)
    arrest_by_offense.plot(kind='bar')
    plt.title('Arrest Rate by Offense Category')
    plt.xlabel('Offense Category')
    plt.ylabel('Arrest Rate')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Plot 2: Arrest rate by time of day
    plt.subplot(2, 2, 2)
    arrest_by_hour = merged_df.groupby('incident_hour')['ARREST'].mean()
    arrest_by_hour.plot(kind='line', marker='o')
    plt.title('Arrest Rate by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Arrest Rate')
    plt.grid(True, alpha=0.3)
    
    # Plot 3: Arrest rate by victim type
    plt.subplot(2, 2, 3)
    arrest_by_victim = merged_df.groupby('victim_type_name')['ARREST'].mean().sort_values(ascending=False)
    arrest_by_victim.plot(kind='bar')
    plt.title('Arrest Rate by Victim Type')
    plt.xlabel('Victim Type')
    plt.ylabel('Arrest Rate')
    plt.xticks(rotation=45, ha='right')
    
    # Plot 4: Arrest rate by agency type
    plt.subplot(2, 2, 4)
    arrest_by_agency = merged_df.groupby('agency_type_name')['ARREST'].mean().sort_values(ascending=False)
    arrest_by_agency.plot(kind='bar')
    plt.title('Arrest Rate by Agency Type')
    plt.xlabel('Agency Type')
    plt.ylabel('Arrest Rate')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('task1_eda_plots.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Reasonability checks
    print("\n=== REASONABILITY CHECKS ===")
    
    # Check for outliers in numeric variables
    numeric_cols = merged_df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col != 'ARREST':
            Q1 = merged_df[col].quantile(0.25)
            Q3 = merged_df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = merged_df[(merged_df[col] < Q1 - 1.5*IQR) | (merged_df[col] > Q3 + 1.5*IQR)]
            if len(outliers) > 0:
                print(f"  Outliers in {col}: {len(outliers)} records ({len(outliers)/len(merged_df)*100:.2f}%)")
    
    # Check internal consistency
    print("\nInternal consistency checks:")
    
    # Check if incident_hour is within valid range
    invalid_hours = merged_df[(merged_df['incident_hour'] < 0) | (merged_df['incident_hour'] > 23)]
    if len(invalid_hours) > 0:
        print(f"  Invalid incident hours: {len(invalid_hours)} records")
    
    # Check if ages are reasonable
    if 'victim_age_num' in merged_df.columns:
        invalid_victim_ages = merged_df[(merged_df['victim_age_num'] < 0) | (merged_df['victim_age_num'] > 120)]
        if len(invalid_victim_ages) > 0:
            print(f"  Invalid victim ages: {len(invalid_victim_ages)} records")
    
    if 'offender_age_num' in merged_df.columns:
        invalid_offender_ages = merged_df[(merged_df['offender_age_num'] < 0) | (merged_df['offender_age_num'] > 120)]
        if len(invalid_offender_ages) > 0:
            print(f"  Invalid offender ages: {len(invalid_offender_ages)} records")

def prepare_final_dataset(merged_df):
    """
    Prepare final dataset for modeling
    """
    print("\n=== PREPARING FINAL DATASET ===")
    
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
    
    # Save final dataset
    final_df.to_csv('prepared_data.csv', index=False)
    print("Final dataset saved as 'prepared_data.csv'")
    
    return final_df

def main():
    """
    Main execution function
    """
    print("ATPA Assessment - Task 1: Data Preparation")
    print("=" * 50)
    
    # Load and examine data
    incidents_df, arrestee_df, data_dict = load_and_examine_data()
    
    # Analyze missing values
    missing_incidents_df, missing_arrestee_df = analyze_missing_values(incidents_df, arrestee_df)
    
    # Handle missing values
    incidents_clean, arrestee_clean = handle_missing_values(incidents_df, arrestee_df)
    
    # Perform dimension reduction
    incidents_clean, arrestee_clean = perform_dimension_reduction(incidents_clean, arrestee_clean)
    
    # Convert numeric to factors
    incidents_clean, arrestee_clean = convert_numeric_to_factors(incidents_clean, arrestee_clean)
    
    # Merge datasets
    merged_df = merge_datasets(incidents_clean, arrestee_clean)
    
    # Create target variable
    merged_df = create_target_variable(merged_df)
    
    # Perform EDA
    perform_eda(merged_df)
    
    # Prepare final dataset
    final_df = prepare_final_dataset(merged_df)
    
    print("\n" + "=" * 50)
    print("TASK 1 COMPLETED SUCCESSFULLY")
    print("=" * 50)
    print(f"Final dataset: {final_df.shape[0]} records, {final_df.shape[1]} features")
    print(f"Arrest rate: {final_df['ARREST'].mean():.2%}")
    print("Files created:")
    print("  - prepared_data.csv (final dataset)")
    print("  - task1_eda_plots.png (visualizations)")

if __name__ == "__main__":
    main() 