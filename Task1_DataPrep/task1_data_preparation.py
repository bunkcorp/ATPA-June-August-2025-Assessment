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
        'arrest_type_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown'
    }).reset_index()
    
    # Rename columns for clarity
    incidents_df = incidents_df.rename(columns={
        'arrestee_id': 'num_arrests',
        'arrest_date': 'incident_date'
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
    categorical_cols = ['weapon_name', 'under_18_disposition_code']
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
    incidents_categorical = ['weapon_name', 'arrest_type_name']
    for col in incidents_categorical:
        if incidents_clean[col].isnull().sum() > 0:
            mode_val = incidents_clean[col].mode().iloc[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
            incidents_clean[col] = incidents_clean[col].fillna(mode_val)
    
    print("Missing values handled successfully")
    
    return arrestee_clean, incidents_clean

def create_target_variable(arrestee_clean, incidents_clean):
    """
    Create ARREST target variable
    """
    print("\n=== CREATING TARGET VARIABLE ===")
    
    # Create incidents with arrest information
    incidents_with_arrest = incidents_clean.copy()
    
    # ARREST = 1 if num_arrests > 0, 0 otherwise
    incidents_with_arrest['ARREST'] = (incidents_with_arrest['num_arrests'] > 0).astype(int)
    
    print(f"Target variable distribution:")
    print(incidents_with_arrest['ARREST'].value_counts())
    print(f"Arrest rate: {incidents_with_arrest['ARREST'].mean():.3f}")
    
    return incidents_with_arrest

def perform_eda(incidents_with_arrest):
    """
    Perform Exploratory Data Analysis
    """
    print("\n=== EXPLORATORY DATA ANALYSIS ===")
    
    # Set up plotting style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. ARREST distribution
    arrest_counts = incidents_with_arrest['ARREST'].value_counts()
    axes[0, 0].pie(arrest_counts.values, labels=['No Arrest', 'Arrest'], autopct='%1.1f%%')
    axes[0, 0].set_title('Distribution of ARREST Target Variable')
    
    # 2. Arrest rate by crime category
    crime_arrest_rate = incidents_with_arrest.groupby('offense_category_name')['ARREST'].mean().sort_values(ascending=False)
    crime_arrest_rate.plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Arrest Rate by Crime Category')
    axes[0, 1].set_ylabel('Arrest Rate')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Arrest rate by crime against
    crime_against_arrest_rate = incidents_with_arrest.groupby('crime_against')['ARREST'].mean()
    crime_against_arrest_rate.plot(kind='bar', ax=axes[1, 0])
    axes[1, 0].set_title('Arrest Rate by Crime Against')
    axes[1, 0].set_ylabel('Arrest Rate')
    
    # 4. Arrest rate by weapon presence
    weapon_arrest_rate = incidents_with_arrest.groupby('weapon_name')['ARREST'].mean().sort_values(ascending=False)
    weapon_arrest_rate.head(10).plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Arrest Rate by Weapon (Top 10)')
    axes[1, 1].set_ylabel('Arrest Rate')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('task1_eda_plots.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print key insights
    print("\n=== KEY INSIGHTS ===")
    print(f"Overall arrest rate: {incidents_with_arrest['ARREST'].mean():.3f}")
    print(f"Total incidents: {len(incidents_with_arrest)}")
    print(f"Incidents with arrests: {incidents_with_arrest['ARREST'].sum()}")
    
    print("\nTop 5 crime categories by arrest rate:")
    print(crime_arrest_rate.head())
    
    print("\nArrest rate by crime against:")
    print(crime_against_arrest_rate)

def prepare_final_dataset(incidents_with_arrest):
    """
    Prepare final dataset for modeling
    """
    print("\n=== PREPARING FINAL DATASET ===")
    
    # Select relevant features for modeling
    feature_cols = [
        'offense_code', 'offense_category_name', 'crime_against',
        'ct_flag', 'hc_flag', 'weapon_name', 'arrest_type_name'
    ]
    
    # Create final dataset
    final_df = incidents_with_arrest[feature_cols + ['ARREST']].copy()
    
    # Encode categorical variables
    le = LabelEncoder()
    for col in feature_cols:
        if final_df[col].dtype == 'object':
            final_df[col + '_encoded'] = le.fit_transform(final_df[col].astype(str))
    
    # Create encoded feature columns
    encoded_cols = [col + '_encoded' for col in feature_cols]
    final_df_encoded = final_df[encoded_cols + ['ARREST']].copy()
    
    print(f"Final dataset shape: {final_df_encoded.shape}")
    print(f"Features: {encoded_cols}")
    print(f"Target: ARREST")
    
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
    
    # Step 2: Create incidents data
    incidents_df = create_incidents_data(arrestee_df)
    
    # Step 3: Handle missing values
    arrestee_clean, incidents_clean = handle_missing_values(arrestee_df, incidents_df)
    
    # Step 4: Create target variable
    incidents_with_arrest = create_target_variable(arrestee_clean, incidents_clean)
    
    # Step 5: Perform EDA
    perform_eda(incidents_with_arrest)
    
    # Step 6: Prepare final dataset
    final_df_encoded, final_df = prepare_final_dataset(incidents_with_arrest)
    
    print("\n" + "=" * 50)
    print("TASK 1 COMPLETED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main() 