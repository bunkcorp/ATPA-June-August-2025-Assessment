"""
ATPA Assessment - June to August 2025
Task 2: Privacy & Bias Analysis

This script addresses the benefits and risks of using demographic data in criminal justice modeling,
and discusses professional standards compliance for NMInsights.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_prepared_data():
    """
    Load the prepared data from Task 1
    """
    print("=== LOADING PREPARED DATA ===")
    
    try:
        # Load the incidents data with arrest information
        incidents_df = pd.read_csv('../Task1_DataPrep/incidents_with_arrest.csv')
        print(f"Loaded incidents data: {incidents_df.shape}")
        return incidents_df
    except FileNotFoundError:
        print("Prepared data not found. Please run Task 1 first.")
        return None

def analyze_demographic_data_usage(incidents_df):
    """
    Analyze the current usage of demographic data in the dataset
    """
    print("\n=== DEMOGRAPHIC DATA ANALYSIS ===")
    
    # Identify demographic variables in the dataset
    demographic_cols = [
        'offender_age_num', 'offender_sex_code', 'offender_race_desc', 
        'offender_ethnicity_name', 'offender_resident_code',
        'victim_age_num', 'victim_sex_code', 'victim_race_desc', 
        'victim_ethnicity_name'
    ]
    
    available_demographics = [col for col in demographic_cols if col in incidents_df.columns]
    print(f"Available demographic variables: {available_demographics}")
    
    # Analyze demographic distributions
    print("\nDemographic Distributions:")
    for col in available_demographics:
        if col in incidents_df.columns:
            print(f"\n{col}:")
            print(incidents_df[col].value_counts().head())
    
    return available_demographics

def create_demographic_visualizations(incidents_df):
    """
    Create visualizations showing demographic patterns
    """
    print("\n=== CREATING DEMOGRAPHIC VISUALIZATIONS ===")
    
    # Set up plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Age distribution
    if 'offender_age_num' in incidents_df.columns:
        incidents_df['offender_age_num'].hist(bins=20, ax=axes[0, 0], alpha=0.7)
        axes[0, 0].set_title('Offender Age Distribution')
        axes[0, 0].set_xlabel('Age')
        axes[0, 0].set_ylabel('Frequency')
    
    # 2. Gender distribution
    if 'offender_sex_code' in incidents_df.columns:
        gender_counts = incidents_df['offender_sex_code'].value_counts()
        gender_counts.plot(kind='bar', ax=axes[0, 1])
        axes[0, 1].set_title('Offender Gender Distribution')
        axes[0, 1].set_ylabel('Count')
        axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Race distribution
    if 'offender_race_desc' in incidents_df.columns:
        race_counts = incidents_df['offender_race_desc'].value_counts().head(10)
        race_counts.plot(kind='bar', ax=axes[1, 0])
        axes[1, 0].set_title('Offender Race Distribution (Top 10)')
        axes[1, 0].set_ylabel('Count')
        axes[1, 0].tick_params(axis='x', rotation=45)
    
    # 4. Ethnicity distribution
    if 'offender_ethnicity_name' in incidents_df.columns:
        ethnicity_counts = incidents_df['offender_ethnicity_name'].value_counts()
        ethnicity_counts.plot(kind='bar', ax=axes[1, 1])
        axes[1, 1].set_title('Offender Ethnicity Distribution')
        axes[1, 1].set_ylabel('Count')
        axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('task2_demographic_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Demographic visualizations saved as 'task2_demographic_analysis.png'")

def analyze_bias_patterns(incidents_df):
    """
    Analyze potential bias patterns in the data
    """
    print("\n=== BIAS PATTERN ANALYSIS ===")
    
    # Analyze arrest patterns by demographic groups
    bias_analysis = {}
    
    # Gender bias analysis
    if 'offender_sex_code' in incidents_df.columns:
        gender_arrest_rate = incidents_df.groupby('offender_sex_code')['MULTIPLE_ARRESTS'].mean()
        bias_analysis['gender'] = gender_arrest_rate
        print(f"\nMultiple arrests rate by gender:")
        print(gender_arrest_rate)
    
    # Race bias analysis
    if 'offender_race_desc' in incidents_df.columns:
        race_arrest_rate = incidents_df.groupby('offender_race_desc')['MULTIPLE_ARRESTS'].mean().sort_values(ascending=False)
        bias_analysis['race'] = race_arrest_rate
        print(f"\nMultiple arrests rate by race (top 10):")
        print(race_arrest_rate.head(10))
    
    # Age bias analysis
    if 'offender_age_num' in incidents_df.columns:
        # Create age groups
        incidents_df['age_group'] = pd.cut(incidents_df['offender_age_num'], 
                                         bins=[0, 18, 25, 35, 50, 100], 
                                         labels=['Under 18', '18-25', '26-35', '36-50', 'Over 50'])
        age_arrest_rate = incidents_df.groupby('age_group')['MULTIPLE_ARRESTS'].mean()
        bias_analysis['age'] = age_arrest_rate
        print(f"\nMultiple arrests rate by age group:")
        print(age_arrest_rate)
    
    return bias_analysis

def generate_privacy_report():
    """
    Generate a comprehensive privacy and bias analysis report
    """
    print("\n=== GENERATING PRIVACY & BIAS REPORT ===")
    
    report = """
# TASK 2: PRIVACY & BIAS ANALYSIS REPORT

## 2a) Benefits and Risks of Demographic Data Usage

### Benefits of Using Demographic Data in Criminal Justice Modeling:

1. **Improved Predictive Accuracy**: Demographic information can help identify patterns in criminal behavior that may not be apparent from other variables alone.

2. **Resource Allocation**: Understanding demographic patterns can help law enforcement agencies allocate resources more effectively and target prevention programs.

3. **Policy Development**: Demographic analysis can inform evidence-based policy decisions and help identify areas where intervention programs are most needed.

4. **Fairness Assessment**: Including demographic data allows researchers to identify and address potential biases in law enforcement practices.

5. **Public Safety**: Better understanding of crime patterns can lead to improved public safety outcomes.

### Risks of Using Demographic Data in Criminal Justice Modeling:

1. **Reinforcement of Existing Biases**: Using demographic data in predictive models may perpetuate existing systemic biases in the criminal justice system.

2. **Discriminatory Outcomes**: Models that rely heavily on demographic factors may lead to discriminatory practices, such as racial profiling or over-policing of certain communities.

3. **Privacy Violations**: Collecting and analyzing demographic data raises concerns about individual privacy and data protection.

4. **Stigmatization**: Demographic-based analysis may contribute to the stigmatization of certain groups or communities.

5. **Legal and Ethical Concerns**: Use of demographic data in criminal justice may violate anti-discrimination laws and ethical principles.

### Specific Considerations for Victims and Offenders:

#### Victim Data:
- **Benefits**: Understanding victim demographics can help identify vulnerable populations and develop targeted protection programs.
- **Risks**: Victim data analysis may inadvertently blame victims or reinforce harmful stereotypes about certain groups.

#### Offender Data:
- **Benefits**: Offender demographic analysis can help identify risk factors and develop prevention strategies.
- **Risks**: May lead to profiling and discriminatory treatment of individuals based on demographic characteristics.

## 2b) Professional Standards Compliance and Misuse Prevention

### Applicable Professional Standards:

1. **ASOP No. 23 (Data Quality)**: Ensures that data used in analysis is reliable, relevant, and appropriate for the intended purpose.

2. **ASOP No. 41 (Actuarial Communications)**: Requires clear communication of limitations, assumptions, and potential biases in analysis.

3. **ASOP No. 56 (Modeling)**: Provides guidance on model development, validation, and documentation.

### Steps to Prevent Misuse:

1. **Transparent Methodology**: Document all data sources, assumptions, and limitations clearly.

2. **Bias Testing**: Regularly test models for demographic bias and adjust as necessary.

3. **Oversight Mechanisms**: Establish independent review boards to monitor model performance and outcomes.

4. **Regular Auditing**: Conduct regular audits of model predictions and outcomes to identify potential biases.

5. **Stakeholder Engagement**: Involve diverse stakeholders in model development and validation.

6. **Documentation Standards**: Maintain comprehensive documentation of all modeling decisions and their rationale.

7. **Training Requirements**: Ensure all users of the models understand their limitations and proper use.

8. **Monitoring and Evaluation**: Establish ongoing monitoring of model performance and impact.

### Specific Recommendations for NMInsights:

1. **Data Governance**: Establish clear policies for data collection, storage, and use.

2. **Model Validation**: Implement rigorous validation procedures that include bias testing.

3. **Stakeholder Consultation**: Engage with community groups, civil rights organizations, and legal experts.

4. **Regular Review**: Schedule regular reviews of model performance and impact.

5. **Transparency**: Publish methodology and findings in accessible formats.

6. **Oversight**: Establish independent oversight mechanisms.

7. **Training**: Provide training on responsible use of demographic data.

8. **Documentation**: Maintain comprehensive documentation of all analysis decisions.

### Limitations and Caveats:

1. **Data Quality**: The available data may not be representative of the entire population.

2. **Model Limitations**: Predictive models are not perfect and should not be used as the sole basis for decisions.

3. **Context Dependence**: Results may not be generalizable to other jurisdictions or time periods.

4. **Ethical Considerations**: The use of demographic data in criminal justice raises complex ethical questions that require ongoing consideration.

5. **Legal Compliance**: Ensure all analysis complies with relevant laws and regulations.

### Conclusion:

While demographic data can provide valuable insights for criminal justice policy and practice, its use must be carefully managed to avoid perpetuating biases and causing harm. NMInsights should implement robust safeguards and oversight mechanisms to ensure responsible use of this data.
"""
    
    # Save the report
    with open('task2_privacy_report.txt', 'w') as f:
        f.write(report)
    
    print("Privacy and bias analysis report saved as 'task2_privacy_report.txt'")
    
    return report

def main():
    """
    Main function to execute Task 2 analysis
    """
    print("ATPA Assessment - Task 2: Privacy & Bias Analysis")
    print("=" * 60)
    
    # Load data
    incidents_df = load_prepared_data()
    if incidents_df is None:
        return
    
    # Analyze demographic data usage
    available_demographics = analyze_demographic_data_usage(incidents_df)
    
    # Create visualizations
    create_demographic_visualizations(incidents_df)
    
    # Analyze bias patterns
    bias_analysis = analyze_bias_patterns(incidents_df)
    
    # Generate comprehensive report
    report = generate_privacy_report()
    
    print("\n" + "=" * 60)
    print("TASK 2 COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nDeliverables created:")
    print("- task2_demographic_analysis.png: Demographic visualizations")
    print("- task2_privacy_report.txt: Comprehensive privacy and bias analysis")
    print("\nKey findings documented:")
    print("- Benefits and risks of demographic data usage")
    print("- Professional standards compliance recommendations")
    print("- Misuse prevention strategies")
    print("- Bias pattern analysis")

if __name__ == "__main__":
    main() 