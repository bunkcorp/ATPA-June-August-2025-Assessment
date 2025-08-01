"""
ATPA Assessment - June to August 2025
Task 5: Bayesian Analysis of Arrest Rates by Crime Category

This script implements Bayesian analysis to explore arrest rates for different crime categories.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import beta
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

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

def create_crime_category_summary(incidents_df):
    """
    Create summary of crime categories, incident counts, and arrest counts
    """
    print("\n=== CREATING CRIME CATEGORY SUMMARY ===")
    
    # Group by crime category and calculate summary statistics
    crime_summary = incidents_df.groupby('offense_category_name').agg({
        'incident_id': 'count',  # Number of incidents
        'MULTIPLE_ARRESTS': 'sum',  # Number of multiple arrests
        'ARREST': 'sum'  # Number of arrests (should be same as incidents since all resulted in arrests)
    }).reset_index()
    
    # Rename columns for clarity
    crime_summary.columns = ['Crime_Category', 'Number_of_Incidents', 'Number_of_Multiple_Arrests', 'Number_of_Arrests']
    
    # Calculate arrest rates
    crime_summary['Arrest_Rate'] = crime_summary['Number_of_Arrests'] / crime_summary['Number_of_Incidents']
    crime_summary['Multiple_Arrest_Rate'] = crime_summary['Number_of_Multiple_Arrests'] / crime_summary['Number_of_Incidents']
    
    # Sort by number of incidents (descending)
    crime_summary = crime_summary.sort_values('Number_of_Incidents', ascending=False)
    
    print("Crime Category Summary:")
    print(crime_summary.to_string(index=False))
    
    # Save summary to CSV
    crime_summary.to_csv('crime_category_summary.csv', index=False)
    print("\nCrime category summary saved as 'crime_category_summary.csv'")
    
    return crime_summary

def bayesian_analysis_arrest_rates(crime_summary):
    """
    Perform Bayesian analysis of arrest rates for each crime category
    """
    print("\n=== BAYESIAN ANALYSIS OF ARREST RATES ===")
    
    # Prior parameters: Beta(α=2, β=8)
    alpha_prior = 2
    beta_prior = 8
    
    print(f"Prior Distribution: Beta(α={alpha_prior}, β={beta_prior})")
    print("This represents a prior belief that arrest rates are generally low (mean = 0.2)")
    
    # Initialize results storage
    bayesian_results = []
    
    # Analyze each crime category
    for _, row in crime_summary.iterrows():
        crime_category = row['Crime_Category']
        n_incidents = row['Number_of_Incidents']
        n_arrests = row['Number_of_Arrests']
        observed_rate = row['Arrest_Rate']
        
        # Posterior parameters (conjugate update)
        alpha_posterior = alpha_prior + n_arrests
        beta_posterior = beta_prior + (n_incidents - n_arrests)
        
        # Calculate posterior mean and variance
        posterior_mean = alpha_posterior / (alpha_posterior + beta_posterior)
        posterior_variance = (alpha_posterior * beta_posterior) / ((alpha_posterior + beta_posterior)**2 * (alpha_posterior + beta_posterior + 1))
        posterior_std = np.sqrt(posterior_variance)
        
        # Calculate 95% credible interval
        credible_interval_lower = beta.ppf(0.025, alpha_posterior, beta_posterior)
        credible_interval_upper = beta.ppf(0.975, alpha_posterior, beta_posterior)
        
        # Store results
        result = {
            'Crime_Category': crime_category,
            'N_Incidents': n_incidents,
            'N_Arrests': n_arrests,
            'Observed_Rate': observed_rate,
            'Posterior_Mean': posterior_mean,
            'Posterior_Std': posterior_std,
            'Credible_Interval_Lower': credible_interval_lower,
            'Credible_Interval_Upper': credible_interval_upper,
            'Alpha_Posterior': alpha_posterior,
            'Beta_Posterior': beta_posterior
        }
        bayesian_results.append(result)
        
        print(f"\n{crime_category}:")
        print(f"  Incidents: {n_incidents}, Arrests: {n_arrests}")
        print(f"  Observed Rate: {observed_rate:.4f}")
        print(f"  Posterior Mean: {posterior_mean:.4f}")
        print(f"  95% Credible Interval: [{credible_interval_lower:.4f}, {credible_interval_upper:.4f}]")
    
    # Convert to DataFrame
    bayesian_df = pd.DataFrame(bayesian_results)
    
    # Save results
    bayesian_df.to_csv('bayesian_arrest_rates.csv', index=False)
    print(f"\nBayesian analysis results saved as 'bayesian_arrest_rates.csv'")
    
    return bayesian_df

def create_bayesian_visualizations(crime_summary, bayesian_df):
    """
    Create visualizations for Bayesian analysis results
    """
    print("\n=== CREATING BAYESIAN VISUALIZATIONS ===")
    
    # Create figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    
    # 1. Observed vs Posterior arrest rates
    ax1 = axes[0, 0]
    x_pos = np.arange(len(bayesian_df))
    width = 0.35
    
    ax1.bar(x_pos - width/2, bayesian_df['Observed_Rate'], width, label='Observed Rate', alpha=0.8)
    ax1.bar(x_pos + width/2, bayesian_df['Posterior_Mean'], width, label='Posterior Mean', alpha=0.8)
    ax1.set_xlabel('Crime Category')
    ax1.set_ylabel('Arrest Rate')
    ax1.set_title('Observed vs Posterior Arrest Rates')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(bayesian_df['Crime_Category'], rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Credible intervals
    ax2 = axes[0, 1]
    y_pos = np.arange(len(bayesian_df))
    
    ax2.errorbar(bayesian_df['Posterior_Mean'], y_pos, 
                xerr=[bayesian_df['Posterior_Mean'] - bayesian_df['Credible_Interval_Lower'],
                      bayesian_df['Credible_Interval_Upper'] - bayesian_df['Posterior_Mean']],
                fmt='o', capsize=5, capthick=2)
    ax2.set_xlabel('Arrest Rate')
    ax2.set_ylabel('Crime Category')
    ax2.set_title('95% Credible Intervals for Arrest Rates')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(bayesian_df['Crime_Category'])
    ax2.grid(True, alpha=0.3)
    
    # 3. Number of incidents by category
    ax3 = axes[1, 0]
    crime_summary_sorted = crime_summary.sort_values('Number_of_Incidents', ascending=True)
    ax3.barh(range(len(crime_summary_sorted)), crime_summary_sorted['Number_of_Incidents'])
    ax3.set_xlabel('Number of Incidents')
    ax3.set_ylabel('Crime Category')
    ax3.set_title('Number of Incidents by Crime Category')
    ax3.set_yticks(range(len(crime_summary_sorted)))
    ax3.set_yticklabels(crime_summary_sorted['Crime_Category'])
    ax3.grid(True, alpha=0.3)
    
    # 4. Posterior distributions for top 5 categories
    ax4 = axes[1, 1]
    top_5_categories = bayesian_df.head(5)
    
    x = np.linspace(0, 1, 1000)
    for _, row in top_5_categories.iterrows():
        posterior_pdf = beta.pdf(x, row['Alpha_Posterior'], row['Beta_Posterior'])
        ax4.plot(x, posterior_pdf, label=row['Crime_Category'], linewidth=2)
    
    ax4.set_xlabel('Arrest Rate')
    ax4.set_ylabel('Posterior Density')
    ax4.set_title('Posterior Distributions (Top 5 Categories)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('task5_bayesian_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Bayesian analysis visualizations saved as 'task5_bayesian_analysis.png'")

def interpret_bayesian_results(bayesian_df):
    """
    Interpret Bayesian analysis results
    """
    print("\n=== INTERPRETING BAYESIAN RESULTS ===")
    
    interpretation = """
## Bayesian Analysis Interpretation

### Prior Distribution:
- **Beta(α=2, β=8)**: Represents prior belief that arrest rates are generally low
- **Prior Mean**: 0.2 (20% arrest rate)
- **Prior Variance**: 0.018 (moderate uncertainty)

### Posterior Analysis:

1. **Conjugate Update**:
   - Posterior parameters: α_post = α_prior + arrests, β_post = β_prior + (incidents - arrests)
   - Posterior distribution: Beta(α_post, β_post)

2. **Key Findings**:
   - Categories with more incidents have more precise estimates (narrower credible intervals)
   - Observed rates are generally close to 1.0 (all incidents resulted in arrests)
   - Posterior means are pulled toward the prior for categories with few incidents

3. **Credible Intervals**:
   - 95% credible intervals provide uncertainty quantification
   - Wider intervals indicate less certainty due to fewer observations
   - Narrower intervals indicate more precise estimates

### Business Implications:

1. **Resource Allocation**:
   - Focus on categories with high arrest rates and many incidents
   - Consider uncertainty when making policy decisions

2. **Policy Development**:
   - Use credible intervals to assess confidence in arrest rate estimates
   - Consider both point estimates and uncertainty

3. **Monitoring and Evaluation**:
   - Track changes in arrest rates over time
   - Update priors based on new evidence

### Limitations:
- All incidents in the dataset resulted in arrests (selection bias)
- Prior may not reflect true underlying arrest rates
- Results may not generalize to other jurisdictions or time periods
"""
    
    print(interpretation)
    
    # Save interpretation
    with open('task5_bayesian_interpretation.txt', 'w') as f:
        f.write(interpretation)
    
    print("Bayesian interpretation saved as 'task5_bayesian_interpretation.txt'")

def generate_task5_report(crime_summary, bayesian_df):
    """
    Generate comprehensive Task 5 report
    """
    print("\n=== GENERATING TASK 5 REPORT ===")
    
    report = f"""
# TASK 5: BAYESIAN ANALYSIS OF ARREST RATES

## 5a) Crime Category Summary

### Data Overview:
- Total crime categories analyzed: {len(crime_summary)}
- Total incidents: {crime_summary['Number_of_Incidents'].sum():,}
- Total arrests: {crime_summary['Number_of_Arrests'].sum():,}

### Top 5 Crime Categories by Incident Count:
{crime_summary.head(5)[['Crime_Category', 'Number_of_Incidents', 'Number_of_Arrests', 'Arrest_Rate']].to_string(index=False)}

## 5b) Bayesian Model Specification

### Prior Distribution:
- **Distribution**: Beta(α=2, β=8)
- **Prior Mean**: 0.2 (20% arrest rate)
- **Justification**: Represents conservative prior belief that arrest rates are generally low

### Likelihood:
- **Model**: Binomial likelihood for each crime category
- **Parameters**: Ni (number of incidents), yi (number of arrests)
- **Assumption**: Independent arrest outcomes within each category

### Posterior Distribution:
- **Conjugate Update**: Beta(α + yi, β + Ni - yi)
- **Inference**: 95% credible intervals for true arrest rates

## 5c) Bayesian Analysis Results

### Key Findings:

1. **Posterior Estimates**:
   - All posterior means are close to 1.0 (reflecting that all incidents resulted in arrests)
   - Credible intervals reflect uncertainty based on sample size

2. **Uncertainty Quantification**:
   - Categories with more incidents have narrower credible intervals
   - Smaller categories show more uncertainty in arrest rate estimates

3. **Model Performance**:
   - Conjugate structure allows for analytical posterior computation
   - Prior influence diminishes with larger sample sizes

### Top 5 Categories - Detailed Results:
{bayesian_df.head(5)[['Crime_Category', 'N_Incidents', 'Posterior_Mean', 'Credible_Interval_Lower', 'Credible_Interval_Upper']].to_string(index=False)}

## 5d) Business Implications

### Policy Recommendations:
1. **Resource Allocation**: Focus on high-volume crime categories
2. **Monitoring**: Track arrest rate changes over time
3. **Evaluation**: Use credible intervals for decision-making

### Limitations:
- Selection bias: All incidents resulted in arrests
- Prior specification may need adjustment
- Results may not generalize to other contexts

### Future Work:
- Update priors with additional data
- Consider hierarchical models for category relationships
- Incorporate temporal trends in arrest rates
"""
    
    # Save the report
    with open('task5_report.txt', 'w') as f:
        f.write(report)
    
    print("Task 5 report saved as 'task5_report.txt'")
    
    return report

def main():
    """
    Main function to execute Task 5 analysis
    """
    print("ATPA Assessment - Task 5: Bayesian Analysis of Arrest Rates")
    print("=" * 60)
    
    # Load data
    incidents_df = load_prepared_data()
    if incidents_df is None:
        return
    
    # Create crime category summary
    crime_summary = create_crime_category_summary(incidents_df)
    
    # Perform Bayesian analysis
    bayesian_df = bayesian_analysis_arrest_rates(crime_summary)
    
    # Create visualizations
    create_bayesian_visualizations(crime_summary, bayesian_df)
    
    # Interpret results
    interpret_bayesian_results(bayesian_df)
    
    # Generate report
    report = generate_task5_report(crime_summary, bayesian_df)
    
    print("\n" + "=" * 60)
    print("TASK 5 COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nDeliverables created:")
    print("- crime_category_summary.csv: Summary statistics by crime category")
    print("- bayesian_arrest_rates.csv: Bayesian analysis results")
    print("- task5_bayesian_analysis.png: Bayesian analysis visualizations")
    print("- task5_bayesian_interpretation.txt: Bayesian interpretation")
    print("- task5_report.txt: Comprehensive Task 5 report")
    print("\nKey findings:")
    print("- Crime category arrest rate analysis")
    print("- Bayesian posterior estimates and credible intervals")
    print("- Uncertainty quantification for policy decisions")
    print("- Business implications and recommendations")

if __name__ == "__main__":
    main() 