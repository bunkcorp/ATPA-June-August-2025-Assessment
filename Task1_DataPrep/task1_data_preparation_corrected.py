"""
ATPA Assessment - June to August 2025
Task 1: Data Preparation

This script performs comprehensive data preparation for the NMInsights crime analysis project.
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
    Load and examine the arrestee data to understand structure
    """
    print("=== LOADING AND EXAMINING DATA ===")
    
    # Load arrestee data
    arrestee_df = pd.read_csv('../arrestee.csv.csv')
    print(f"Arrestee data shape: {arrestee_df.shape}")
    print(f"Arrestee columns: {arrestee_df.columns.tolist()}")
    
    # Load data dictionary
    data_dict = pd.read_excel('../Data_Dictionary.xlsx')
    print(f"Data dictionary shape: {data_dict.shape}")
    
    # Display basic info about arrestee data
    print("\n=== ARRESTEE DATA INFO ===")
    print(arrestee_df.info())
    
    print("\n=== ARRESTEE DATA SAMPLE ===")
    print(arrestee_df.head())
    
    print("\n=== MISSING VALUES ANALYSIS ===")
    missing_data = arrestee_df.isnull().sum()
    missing_percent = (missing_data / len(arrestee_df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing_data,
        'Missing_Percent': missing_percent
    }).sort_values('Missing_Percent', ascending=False)
    
    print(missing_df[missing_df['Missing_Count'] > 0])
    
    return arrestee_df, data_dict

def analyze_data_structure(arrestee_df):
    """
    Analyze the data structure to understand what we have
    """
    print("\n=== DATA STRUCTURE ANALYSIS ===")
    
    # Check unique incidents
    unique_incidents = arrestee_df['incident_id'].nunique()
    total_records = len(arrestee_df)
    print(f"Total arrestee records: {total_records}")
    print(f"Unique incidents: {unique_incidents}")
    print(f"Average arrests per incident: {total_records / unique_incidents:.2f}")
    
    # Check if we have incidents without arrests (we don't, based on the data)
    print("\nIMPORTANT INSIGHT: This dataset contains ONLY incidents that resulted in arrests.")
    print("We do not have data on incidents that did NOT result in arrests.")
    print("This means we need to approach the analysis differently.")
    
    return unique_incidents

def create_incidents_data(arrestee_df):
    """
    Create incidents data from arrestee data by aggregating at incident level
    """
    print("\n=== CREATING INCIDENTS DATA ===")
    
    # Group by incident_id to create incidents dataset
    incidents_df = arrestee_df.groupby('incident_id').agg({
        'data_year': 'first',
        'offense_code': 'first',
        'offense_category_name': 'first',
        'crime_against': 'first',
        'ct_flag': 'first',
        'hc_flag': 'first',
        'hc_code': 'first',
        'weapon_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'arrestee_id': 'count',  # Number of arrests per incident
        'arrest_date': 'first',
        'arrest_type_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'age_num': 'mean',  # Average age of arrestees
        'sex_code': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'race_desc': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'ethnicity_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown'
    }).reset_index()
    
    # Rename columns for clarity
    incidents_df = incidents_df.rename(columns={
        'arrestee_id': 'num_arrests',
        'arrest_date': 'incident_date',
        'age_num': 'avg_arrestee_age'
    })
    
    print(f"Incidents data shape: {incidents_df.shape}")
    print("Incidents data sample:")
    print(incidents_df.head())
    
    return incidents_df

def handle_missing_values(arrestee_df, incidents_df):
    """
    Handle missing values in both datasets
    """
    print("\n=== HANDLING MISSING VALUES ===")
    
    # Analyze missing values in arrestee data
    print("Missing values in arrestee data:")
    arrestee_missing = arrestee_df.isnull().sum()
    print(arrestee_missing[arrestee_missing > 0])
    
    # Handle missing values in arrestee data
    arrestee_clean = arrestee_df.copy()
    
    # For categorical variables, use mode imputation
    categorical_cols = ['weapon_name', 'under_18_disposition_code', 'resident_code']
    for col in categorical_cols:
        if arrestee_clean[col].isnull().sum() > 0:
            mode_val = arrestee_clean[col].mode().iloc[0] if len(arrestee_clean[col].mode()) > 0 else 'Unknown'
            arrestee_clean[col] = arrestee_clean[col].fillna(mode_val)
    
    # For numeric variables, use median imputation
    numeric_cols = ['age_num', 'hc_code']
    for col in numeric_cols:
        if arrestee_clean[col].isnull().sum() > 0:
            median_val = arrestee_clean[col].median()
            arrestee_clean[col] = arrestee_clean[col].fillna(median_val)
    
    # Handle missing values in incidents data
    incidents_clean = incidents_df.copy()
    
    # For categorical variables in incidents
    incidents_categorical = ['weapon_name', 'arrest_type_name', 'sex_code', 'race_desc', 'ethnicity_name']
    for col in incidents_categorical:
        if incidents_clean[col].isnull().sum() > 0:
            mode_val = incidents_clean[col].mode().iloc[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
            incidents_clean[col] = incidents_clean[col].fillna(mode_val)
    
    print("Missing values handled successfully")
    
    return arrestee_clean, incidents_clean

def create_target_variable(arrestee_clean, incidents_clean):
    """
    Create ARREST target variable - since all incidents resulted in arrests, 
    we'll create a different target variable for analysis
    """
    print("\n=== CREATING TARGET VARIABLE ===")
    
    # Since all incidents resulted in arrests, let's create a different target
    # We could analyze factors that lead to multiple arrests vs single arrests
    incidents_with_arrest = incidents_clean.copy()
    
    # Create a binary target: Multiple arrests (1) vs Single arrest (0)
    incidents_with_arrest['MULTIPLE_ARRESTS'] = (incidents_with_arrest['num_arrests'] > 1).astype(int)
    
    # Also keep the original ARREST variable (all 1s)
    incidents_with_arrest['ARREST'] = 1
    
    print(f"Target variable distribution (MULTIPLE_ARRESTS):")
    print(incidents_with_arrest['MULTIPLE_ARRESTS'].value_counts())
    print(f"Multiple arrests rate: {incidents_with_arrest['MULTIPLE_ARRESTS'].mean():.3f}")
    
    return incidents_with_arrest

def perform_eda(incidents_with_arrest):
    """
    Perform Exploratory Data Analysis
    """
    print("\n=== EXPLORATORY DATA ANALYSIS ===")
    
    # Set up plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. MULTIPLE_ARRESTS distribution
    multiple_arrests_counts = incidents_with_arrest['MULTIPLE_ARRESTS'].value_counts()
    axes[0, 0].pie(multiple_arrests_counts.values, labels=['Single Arrest', 'Multiple Arrests'], autopct='%1.1f%%')
    axes[0, 0].set_title('Distribution of Multiple Arrests')
    
    # 2. Multiple arrests rate by crime category
    crime_multiple_rate = incidents_with_arrest.groupby('offense_category_name')['MULTIPLE_ARRESTS'].mean().sort_values(ascending=False)
    crime_multiple_rate.plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Multiple Arrests Rate by Crime Category')
    axes[0, 1].set_ylabel('Multiple Arrests Rate')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Multiple arrests rate by crime against
    crime_against_multiple_rate = incidents_with_arrest.groupby('crime_against')['MULTIPLE_ARRESTS'].mean()
    crime_against_multiple_rate.plot(kind='bar', ax=axes[1, 0])
    axes[1, 0].set_title('Multiple Arrests Rate by Crime Against')
    axes[1, 0].set_ylabel('Multiple Arrests Rate')
    
    # 4. Multiple arrests rate by weapon presence
    weapon_multiple_rate = incidents_with_arrest.groupby('weapon_name')['MULTIPLE_ARRESTS'].mean().sort_values(ascending=False)
    weapon_multiple_rate.head(10).plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Multiple Arrests Rate by Weapon (Top 10)')
    axes[1, 1].set_ylabel('Multiple Arrests Rate')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('task1_eda_plots.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print key insights
    print("\n=== KEY INSIGHTS ===")
    print(f"Overall multiple arrests rate: {incidents_with_arrest['MULTIPLE_ARRESTS'].mean():.3f}")
    print(f"Total incidents: {len(incidents_with_arrest)}")
    print(f"Incidents with multiple arrests: {incidents_with_arrest['MULTIPLE_ARRESTS'].sum()}")
    
    print("\nTop 5 crime categories by multiple arrests rate:")
    print(crime_multiple_rate.head())
    
    print("\nMultiple arrests rate by crime against:")
    print(crime_against_multiple_rate)

def prepare_final_dataset(incidents_with_arrest):
    """
    Prepare final dataset for modeling
    """
    print("\n=== PREPARING FINAL DATASET ===")
    
    # Select relevant features for modeling
    feature_cols = [
        'offense_code', 'offense_category_name', 'crime_against',
        'ct_flag', 'hc_flag', 'weapon_name', 'arrest_type_name',
        'avg_arrestee_age', 'sex_code', 'race_desc', 'ethnicity_name'
    ]
    
    # Create final dataset
    final_df = incidents_with_arrest[feature_cols + ['MULTIPLE_ARRESTS', 'ARREST']].copy()
    
    # Encode categorical variables (excluding numeric ones)
    le = LabelEncoder()
    categorical_cols = [col for col in feature_cols if final_df[col].dtype == 'object']
    numeric_cols = [col for col in feature_cols if final_df[col].dtype != 'object']
    
    for col in categorical_cols:
        final_df[col + '_encoded'] = le.fit_transform(final_df[col].astype(str))
    
    # Create encoded feature columns
    encoded_cols = [col + '_encoded' for col in categorical_cols] + numeric_cols
    final_df_encoded = final_df[encoded_cols + ['MULTIPLE_ARRESTS', 'ARREST']].copy()
    
    print(f"Final dataset shape: {final_df_encoded.shape}")
    print(f"Categorical features encoded: {[col + '_encoded' for col in categorical_cols]}")
    print(f"Numeric features: {numeric_cols}")
    print(f"Targets: MULTIPLE_ARRESTS, ARREST")
    
    # Save prepared data
    final_df_encoded.to_csv('prepared_data.csv', index=False)
    incidents_with_arrest.to_csv('incidents_with_arrest.csv', index=False)
    
    print("Data preparation completed successfully!")
    
    return final_df_encoded, final_df

def main():
    """
    Main function to execute all data preparation steps
    """
    print("ATPA Assessment - Task 1: Data Preparation")
    print("=" * 50)
    
    # Step 1: Load and examine data
    arrestee_df, data_dict = load_and_examine_data()
    
    # Step 2: Analyze data structure
    unique_incidents = analyze_data_structure(arrestee_df)
    
    # Step 3: Create incidents data
    incidents_df = create_incidents_data(arrestee_df)
    
    # Step 4: Handle missing values
    arrestee_clean, incidents_clean = handle_missing_values(arrestee_df, incidents_df)
    
    # Step 5: Create target variable
    incidents_with_arrest = create_target_variable(arrestee_clean, incidents_clean)
    
    # Step 6: Perform EDA
    perform_eda(incidents_with_arrest)
    
    # Step 7: Prepare final dataset
    final_df_encoded, final_df = prepare_final_dataset(incidents_with_arrest)
    
    print("\n" + "=" * 50)
    print("TASK 1 COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print("\nIMPORTANT NOTE: This dataset contains only incidents that resulted in arrests.")
    print("For a complete arrest prediction model, we would need data on incidents")
    print("that did NOT result in arrests. This analysis focuses on factors")
    print("associated with multiple arrests vs single arrests within arrested incidents.")

if __name__ == "__main__":
    main() 