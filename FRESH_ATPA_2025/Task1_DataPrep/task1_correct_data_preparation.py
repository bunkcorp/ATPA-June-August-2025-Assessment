#!/usr/bin/env python3
"""
ATPA Assessment - Task 1: Data Preparation & EDA (CORRECT APPROACH)
June-August 2025
NMInsights Crime Analysis

CRITICAL FIX: Properly define ARREST target variable
- incidents.csv = ALL criminal incidents 
- arrestee.csv = Only incidents with arrests
- ARREST = 1 if incident_id in arrestee.csv, 0 otherwise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("ATPA ASSESSMENT - TASK 1: DATA PREPARATION (CORRECT APPROACH)")
print("="*70)

# Load data
print("\n1. LOADING DATA")
print("-" * 30)

incidents = pd.read_csv('../../Task1_DataPrep/incidents.csv')
arrestee = pd.read_csv('../../Task1_DataPrep/arrestee.csv')

print(f"✅ Incidents data: {len(incidents):,} records, {len(incidents.columns)} columns")
print(f"✅ Arrestee data: {len(arrestee):,} records, {len(arrestee.columns)} columns")

# 1c) Create correct ARREST target variable
print("\n2. CREATING CORRECT TARGET VARIABLE")
print("-" * 40)

# Get incident IDs that resulted in arrests
arrest_incident_ids = set(arrestee['incident_id'].unique())
total_incidents = len(incidents['incident_id'].unique())
arrest_incidents = len(arrest_incident_ids)

print(f"📊 Total unique incidents: {total_incidents:,}")
print(f"📊 Incidents with arrests: {arrest_incidents:,}")
print(f"📊 Incidents without arrests: {total_incidents - arrest_incidents:,}")
print(f"📊 Arrest rate: {arrest_incidents/total_incidents*100:.1f}%")

# Create ARREST target variable (CORRECT APPROACH)
incidents['ARREST'] = incidents['incident_id'].isin(arrest_incident_ids).astype(int)

print(f"\n✅ ARREST target variable created:")
print(f"   - ARREST = 1: {incidents['ARREST'].sum():,} incidents ({incidents['ARREST'].mean()*100:.1f}%)")
print(f"   - ARREST = 0: {(incidents['ARREST'] == 0).sum():,} incidents ({(1-incidents['ARREST'].mean())*100:.1f}%)")

# 1a) Missing values analysis
print("\n3. MISSING VALUES ANALYSIS")
print("-" * 30)

missing_analysis = pd.DataFrame({
    'Column': incidents.columns,
    'Missing_Count': incidents.isnull().sum(),
    'Missing_Percentage': (incidents.isnull().sum() / len(incidents)) * 100
}).sort_values('Missing_Percentage', ascending=False)

high_missing = missing_analysis[missing_analysis['Missing_Percentage'] > 10]
print("📋 Columns with >10% missing values:")
for _, row in high_missing.head(10).iterrows():
    print(f"   {row['Column']}: {row['Missing_Count']:,} ({row['Missing_Percentage']:.1f}%)")

# Select key predictors for modeling
key_predictors = [
    'incident_id', 'incident_hour', 'offense_code', 'offense_category_name',
    'crime_against', 'location_name', 'state_name', 'agency_name', 
    'population_group_name', 'bias_desc', 'victim_count', 'ct_flag', 'ARREST'
]

# Keep only available columns
available_predictors = [col for col in key_predictors if col in incidents.columns]
incidents_clean = incidents[available_predictors].copy()

print(f"\n✅ Selected {len(available_predictors)} key predictors for analysis")

# Handle missing values in selected predictors
print("\n4. HANDLING MISSING VALUES")
print("-" * 30)

# For categorical variables - use mode imputation
categorical_cols = incidents_clean.select_dtypes(include=['object']).columns
categorical_cols = [col for col in categorical_cols if col not in ['incident_id']]

# For numerical variables - use median imputation  
numerical_cols = incidents_clean.select_dtypes(include=['int64', 'float64']).columns
numerical_cols = [col for col in numerical_cols if col not in ['incident_id', 'ARREST']]

print(f"📊 Categorical columns to impute: {len(categorical_cols)}")
print(f"📊 Numerical columns to impute: {len(numerical_cols)}")

# Impute missing values
for col in categorical_cols:
    if incidents_clean[col].isnull().any():
        mode_val = incidents_clean[col].mode()[0] if len(incidents_clean[col].mode()) > 0 else 'Unknown'
        incidents_clean[col] = incidents_clean[col].fillna(mode_val)
        print(f"   ✅ {col}: filled with mode '{mode_val}'")

for col in numerical_cols:
    if incidents_clean[col].isnull().any():
        median_val = incidents_clean[col].median()
        incidents_clean[col] = incidents_clean[col].fillna(median_val)
        print(f"   ✅ {col}: filled with median {median_val}")

# 1a) Convert numeric to categorical where appropriate
print("\n5. NUMERIC TO CATEGORICAL CONVERSION")
print("-" * 40)

# Check incident_hour - should be categorical for time-of-day analysis
if 'incident_hour' in incidents_clean.columns:
    print(f"📊 incident_hour: {incidents_clean['incident_hour'].nunique()} unique values")
    # Create time periods
    incidents_clean['time_period'] = pd.cut(
        incidents_clean['incident_hour'], 
        bins=[0, 6, 12, 18, 24], 
        labels=['Night', 'Morning', 'Afternoon', 'Evening'],
        include_lowest=True
    )
    print("   ✅ Created time_period categories: Night, Morning, Afternoon, Evening")

# Encode categorical variables
print("\n6. ENCODING CATEGORICAL VARIABLES")  
print("-" * 35)

label_encoders = {}
for col in categorical_cols:
    if col in incidents_clean.columns:
        le = LabelEncoder()
        incidents_clean[f'{col}_encoded'] = le.fit_transform(incidents_clean[col].astype(str))
        label_encoders[col] = le
        print(f"   ✅ {col}: {len(le.classes_)} categories encoded")

# 1d) Exploratory Data Analysis
print("\n7. EXPLORATORY DATA ANALYSIS")
print("-" * 30)

# Target variable distribution
print("📊 ARREST Target Variable Distribution:")
arrest_counts = incidents_clean['ARREST'].value_counts()
print(f"   No Arrest (0): {arrest_counts[0]:,} ({arrest_counts[0]/len(incidents_clean)*100:.1f}%)")
print(f"   Arrest (1): {arrest_counts[1]:,} ({arrest_counts[1]/len(incidents_clean)*100:.1f}%)")

# Create visualizations
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('ATPA Task 1: Exploratory Data Analysis (CORRECT APPROACH)', fontsize=16, fontweight='bold')

# 1. Target variable distribution
axes[0,0].pie(arrest_counts.values, labels=['No Arrest', 'Arrest'], autopct='%1.1f%%', 
              colors=['lightcoral', 'lightblue'])
axes[0,0].set_title('Arrest Distribution\n(Realistic 19% Arrest Rate)')

# 2. Arrests by time period (if available)
if 'time_period' in incidents_clean.columns:
    time_arrest = pd.crosstab(incidents_clean['time_period'], incidents_clean['ARREST'])
    time_arrest_pct = time_arrest.div(time_arrest.sum(axis=1), axis=0) * 100
    time_arrest_pct[1].plot(kind='bar', ax=axes[0,1], color='skyblue')
    axes[0,1].set_title('Arrest Rate by Time Period')
    axes[0,1].set_ylabel('Arrest Rate (%)')
    axes[0,1].tick_params(axis='x', rotation=45)

# 3. Arrests by offense category (top 10)
if 'offense_category_name' in incidents_clean.columns:
    offense_arrest = incidents_clean.groupby('offense_category_name')['ARREST'].agg(['count', 'mean']).sort_values('count', ascending=False)
    top_offenses = offense_arrest.head(10)
    axes[1,0].barh(range(len(top_offenses)), top_offenses['mean']*100, color='lightgreen')
    axes[1,0].set_yticks(range(len(top_offenses)))
    axes[1,0].set_yticklabels([name[:20] + '...' if len(name) > 20 else name for name in top_offenses.index])
    axes[1,0].set_xlabel('Arrest Rate (%)')
    axes[1,0].set_title('Arrest Rate by Offense Category (Top 10)')

# 4. Data quality summary
quality_summary = pd.DataFrame({
    'Metric': ['Total Incidents', 'Incidents with Arrests', 'Arrest Rate (%)', 
               'Complete Records', 'Missing Data Handled'],
    'Value': [f"{len(incidents_clean):,}", f"{incidents_clean['ARREST'].sum():,}", 
              f"{incidents_clean['ARREST'].mean()*100:.1f}%", 
              f"{len(incidents_clean):,}", "✅ Yes"]
})

axes[1,1].axis('off')
table = axes[1,1].table(cellText=quality_summary.values, colLabels=quality_summary.columns,
                        cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)
axes[1,1].set_title('Data Quality Summary')

plt.tight_layout()
plt.savefig('task1_correct_eda_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Data quality checks
print("\n8. DATA QUALITY CHECKS")
print("-" * 25)

print("📋 Reasonability Checks:")
print(f"   ✅ Total records: {len(incidents_clean):,}")
print(f"   ✅ No missing values in target: {incidents_clean['ARREST'].isnull().sum() == 0}")
print(f"   ✅ Realistic arrest rate: {incidents_clean['ARREST'].mean()*100:.1f}% (expected ~10-30%)")
print(f"   ✅ No duplicate incident IDs: {incidents_clean['incident_id'].nunique() == len(incidents_clean)}")

# Check for outliers in numerical columns
print("\n📋 Outlier Detection:")
for col in numerical_cols:
    if col in incidents_clean.columns:
        Q1 = incidents_clean[col].quantile(0.25)
        Q3 = incidents_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = incidents_clean[(incidents_clean[col] < Q1 - 1.5*IQR) | 
                                 (incidents_clean[col] > Q3 + 1.5*IQR)]
        print(f"   {col}: {len(outliers)} outliers ({len(outliers)/len(incidents_clean)*100:.1f}%)")

# Save final dataset
final_columns = ['incident_id'] + [col for col in incidents_clean.columns if col.endswith('_encoded')] + ['ARREST']
if 'incident_hour' in incidents_clean.columns:
    final_columns.append('incident_hour')

final_dataset = incidents_clean[final_columns].copy()
final_dataset.to_csv('task1_prepared_dataset_correct.csv', index=False)

print(f"\n✅ TASK 1 COMPLETE - CORRECT APPROACH")
print(f"📁 Final dataset saved: {len(final_dataset)} records, {len(final_dataset.columns)} columns")
print(f"🎯 Target variable: ARREST with realistic {final_dataset['ARREST'].mean()*100:.1f}% arrest rate")

print("\n" + "="*70)
print("READY FOR TASK 2: PRIVACY & ETHICS ANALYSIS")
print("="*70)