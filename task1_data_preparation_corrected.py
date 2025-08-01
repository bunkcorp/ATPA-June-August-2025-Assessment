"""
ATPA Assessment - June to August 2025
Task 1: Data Preparation - CORRECTED VERSION

This script performs comprehensive data preparation following the proper data dictionary structure.
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

def analyze_data_dictionary(data_dict):
    """
    Analyze the data dictionary to understand the expected structure
    """
    print("\n=== DATA DICTIONARY ANALYSIS ===")
    
    # Arrestee data variables (first 22 rows)
    arrestee_vars = data_dict.iloc[0:22]
    print("Arrestee data variables (22 rows):")
    print(arrestee_vars[['Variable', 'Type']].to_string())
    
    # Incidents data variables (rows 23-58)
    incidents_vars = data_dict.iloc[22:58]
    print("\nIncidents data variables (36 rows):")
    print(incidents_vars[['Variable', 'Type']].to_string())
    
    return arrestee_vars, incidents_vars

def analyze_data_dictionary(data_dict):
    """
    Analyze the data dictionary to understand the expected structure
    """
    print("\n=== DATA DICTIONARY ANALYSIS ===")
    
    # Arrestee data variables (first 22 rows)
    arrestee_vars = data_dict.iloc[0:22]
    print("Arrestee data variables (22 rows):")
    print(arrestee_vars[['Variable', 'Type']].to_string())
    
    # Incidents data variables (rows 23-58)
    incidents_vars = data_dict.iloc[22:58]
    print("\nIncidents data variables (36 rows):")
    print(incidents_vars[['Variable', 'Type']].to_string())
    
    return arrestee_vars, incidents_vars

def create_incidents_data_from_arrestee(arrestee_df):
    """
    Create incidents data from arrestee data following the incidents data dictionary structure
    """
    print("\n=== CREATING INCIDENTS DATA FROM ARRESTEE DATA ===")
    
    # Group by incident_id to create incidents dataset
    # We'll map arrestee data to incidents data structure
    incidents_df = arrestee_df.groupby('incident_id').agg({
        # Incident-level information (from arrestee data)
        'data_year': 'first',
        'offense_code': 'first',
        'offense_category_name': 'first',
        'crime_against': 'first',
        'ct_flag': 'first',
        'hc_flag': 'first',
        'hc_code': 'first',
        'weapon_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'arrest_date': 'first',
        'arrest_type_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        
        # Offender information (from arrestee data)
        'age_num': 'mean',  # Average age of offenders
        'sex_code': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'race_desc': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'ethnicity_name': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        'resident_code': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        
        # Count information
        'arrestee_id': 'count',  # Number of arrests per incident
    }).reset_index()
    
    # Rename columns to match incidents data structure
    incidents_df = incidents_df.rename(columns={
        'arrestee_id': 'num_arrests',
        'arrest_date': 'incident_date',
        'age_num': 'offender_age_num',
        'sex_code': 'offender_sex_code',
        'race_desc': 'offender_race_desc',
        'ethnicity_name': 'offender_ethnicity_name',
        'resident_code': 'offender_resident_code'
    })
    
    # Add missing incidents variables (set to default values since we don't have this data)
    incidents_df['victim_id'] = incidents_df['incident_id']  # Assume one victim per incident
    incidents_df['victim_seq_num'] = 1
    incidents_df['victim_type_name'] = 'Individual'  # Default assumption
    incidents_df['victim_age_num'] = np.nan  # We don't have victim age
    incidents_df['victim_sex_code'] = 'Unknown'  # We don't have victim sex
    incidents_df['victim_race_desc'] = 'Unknown'  # We don't have victim race
    incidents_df['victim_ethnicity_name'] = 'Unknown'  # We don't have victim ethnicity
    incidents_df['relationship_name'] = 'Unknown'  # We don't have relationship data
    incidents_df['property_id'] = np.nan  # We don't have property data
    incidents_df['stolen_count'] = 0  # Default to 0
    incidents_df['recovered_count'] = 0  # Default to 0
    incidents_df['agency_name'] = 'New Mexico Law Enforcement'  # Generic agency name
    incidents_df['agency_type_name'] = 'Municipal Police'  # Generic agency type
    incidents_df['population'] = np.nan  # We don't have population data
    incidents_df['suburban_area'] = 'Unknown'  # We don't have area data
    incidents_df['population_group_desc'] = 'Unknown'  # We don't have population group
    incidents_df['male_officer'] = np.nan  # We don't have officer data
    incidents_df['male_civilian'] = np.nan  # We don't have civilian data
    incidents_df['female_officer'] = np.nan  # We don't have officer data
    incidents_df['female_civilian'] = np.nan  # We don't have civilian data
    incidents_df['county_name'] = 'Unknown'  # We don't have county data
    
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
    incidents_categorical = ['weapon_name', 'arrest_type_name', 'offender_sex_code', 
                           'offender_race_desc', 'offender_ethnicity_name', 'offender_resident_code']
    for col in incidents_categorical:
        if incidents_clean[col].isnull().sum() > 0:
            mode_val = incidents_clean[col].mode().iloc[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
            incidents_clean[col] = incidents_clean[col].fillna(mode_val)
    
    print("Missing values handled successfully")
    
    return arrestee_clean, incidents_clean

def create_target_variable(incidents_clean):
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
    plt.savefig('task1_eda_plots_corrected.png', dpi=300, bbox_inches='tight')
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
    
    # Select relevant features for modeling (focusing on available data)
    feature_cols = [
        'offense_code', 'offense_category_name', 'crime_against',
        'ct_flag', 'hc_flag', 'weapon_name', 'arrest_type_name',
        'offender_age_num', 'offender_sex_code', 'offender_race_desc', 
        'offender_ethnicity_name', 'offender_resident_code'
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
    final_df_encoded.to_csv('prepared_data_corrected.csv', index=False)
    incidents_with_arrest.to_csv('incidents_with_arrest_corrected.csv', index=False)
    
    print("Data preparation completed successfully!")
    
    return final_df_encoded, final_df

def main():
    """
    Main function to execute all data preparation steps
    """
    print("ATPA Assessment - Task 1: Data Preparation (CORRECTED)")
    print("=" * 60)
    
    # Step 1: Load and examine data
    arrestee_df, data_dict = load_and_examine_data()
    
    # Step 2: Analyze data dictionary structure
    arrestee_vars, incidents_vars = analyze_data_dictionary(data_dict)
    
    # Step 3: Create incidents data following proper structure
    incidents_df = create_incidents_data_from_arrestee(arrestee_df)
    
    # Step 4: Handle missing values
    arrestee_clean, incidents_clean = handle_missing_values(arrestee_df, incidents_df)
    
    # Step 5: Create target variable
    incidents_with_arrest = create_target_variable(incidents_clean)
    
    # Step 6: Perform EDA
    perform_eda(incidents_with_arrest)
    
    # Step 7: Prepare final dataset
    final_df_encoded, final_df = prepare_final_dataset(incidents_with_arrest)
    
    print("\n" + "=" * 60)
    print("TASK 1 COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nIMPORTANT NOTES:")
    print("1. This dataset contains only incidents that resulted in arrests.")
    print("2. Incidents data was created from arrestee data following the data dictionary structure.")
    print("3. Some incidents variables are set to default values since we don't have victim data.")
    print("4. Analysis focuses on factors associated with multiple arrests vs single arrests.")
    print("5. For complete arrest prediction, we would need data on incidents without arrests.")

if __name__ == "__main__":
    main() 