#!/usr/bin/env python3
"""
ATPA Assessment - Task 5: Bayesian Analysis (CORRECT APPROACH)
June-August 2025
NMInsights Crime Analysis

CORRECT APPROACH: Realistic arrest rates by crime category
Beta(α=2, β=8) prior, conjugate Bayesian updating
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("ATPA ASSESSMENT - TASK 5: BAYESIAN ANALYSIS (CORRECT APPROACH)")
print("="*70)

# Load original data to get crime categories
print("🔧 Loading original data for crime category analysis...")
incidents = pd.read_csv('../../Task1_DataPrep/incidents.csv')
arrestee = pd.read_csv('../../Task1_DataPrep/arrestee.csv')

print(f"✅ Incidents: {len(incidents):,} records")
print(f"✅ Arrestee: {len(arrestee):,} records")

# Create ARREST indicator (CORRECT APPROACH)
arrest_incident_ids = set(arrestee['incident_id'].unique())
incidents['ARREST'] = incidents['incident_id'].isin(arrest_incident_ids).astype(int)

print(f"🎯 Overall arrest rate: {incidents['ARREST'].mean()*100:.1f}% (REALISTIC!)")

print("\n5a) CRIME CATEGORY SUMMARY")
print("-" * 30)

# Group by offense category
if 'offense_category_name' in incidents.columns:
    category_summary = incidents.groupby('offense_category_name').agg({
        'incident_id': 'count',
        'ARREST': ['count', 'sum', 'mean']
    }).round(4)
    
    # Flatten column names
    category_summary.columns = ['Number_of_Incidents', 'Total_Records', 'Number_of_Arrests', 'Arrest_Rate']
    category_summary = category_summary[['Number_of_Incidents', 'Number_of_Arrests', 'Arrest_Rate']]
    category_summary = category_summary.sort_values('Number_of_Incidents', ascending=False)
    
    print(f"📊 Crime Categories Analyzed: {len(category_summary)}")
    print(f"📊 Total Incidents: {category_summary['Number_of_Incidents'].sum():,}")
    print(f"📊 Total Arrests: {category_summary['Number_of_Arrests'].sum():,}")
    
    print(f"\n📋 Top 10 Crime Categories by Incident Count:")
    print(category_summary.head(10).to_string())
    
else:
    print("⚠️  offense_category_name not found, using offense_code as proxy")
    category_summary = incidents.groupby('offense_code').agg({
        'incident_id': 'count',
        'ARREST': ['sum', 'mean']
    }).round(4)
    category_summary.columns = ['Number_of_Incidents', 'Number_of_Arrests', 'Arrest_Rate']
    category_summary = category_summary.sort_values('Number_of_Incidents', ascending=False)
    
    print(f"📊 Offense Codes Analyzed: {len(category_summary)}")

print("\n5b) BAYESIAN MODEL IMPLEMENTATION")
print("-" * 35)

print("📋 Bayesian Model Specification:")
print("   Prior: Beta(α=2, β=8)")
print("   Likelihood: Binomial(Ni, pi) for each category i")
print("   Posterior: Beta(α + yi, β + Ni - yi)")

# Prior parameters
alpha_prior = 2
beta_prior = 8
prior_mean = alpha_prior / (alpha_prior + beta_prior)

print(f"   Prior mean arrest rate: {prior_mean:.3f} ({prior_mean*100:.1f}%)")

# Bayesian analysis for each category
bayesian_results = []

for category, row in category_summary.iterrows():
    ni = row['Number_of_Incidents']  # Number of incidents
    yi = row['Number_of_Arrests']    # Number of arrests
    
    # Posterior parameters (conjugate update)
    alpha_post = alpha_prior + yi
    beta_post = beta_prior + ni - yi
    
    # Posterior statistics
    post_mean = alpha_post / (alpha_post + beta_post)
    post_var = (alpha_post * beta_post) / ((alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))
    post_std = np.sqrt(post_var)
    
    # 95% credible interval
    ci_lower = stats.beta.ppf(0.025, alpha_post, beta_post)
    ci_upper = stats.beta.ppf(0.975, alpha_post, beta_post)
    
    # Additional Bayesian metrics
    ci_width = ci_upper - ci_lower
    effect_size = abs(post_mean - prior_mean) / prior_mean  # Relative effect size
    precision = 1 / post_var if post_var > 0 else 0  # Precision (inverse variance)
    
    # Bayes factor approximation (simplified)
    # BF = P(data|H1) / P(data|H0) where H1 is the observed rate, H0 is prior mean
    observed_rate = yi / ni if ni > 0 else 0
    log_bf = (yi * np.log(observed_rate) + (ni - yi) * np.log(1 - observed_rate) - 
              yi * np.log(prior_mean) - (ni - yi) * np.log(1 - prior_mean)) if observed_rate > 0 and observed_rate < 1 else 0
    
    bayesian_results.append({
        'Crime_Category': category,
        'Incidents': ni,
        'Arrests': yi,
        'Observed_Rate': observed_rate,
        'Posterior_Mean': post_mean,
        'Posterior_Std': post_std,
        'CI_Lower': ci_lower,
        'CI_Upper': ci_upper,
        'CI_Width': ci_width,
        'Effect_Size': effect_size,
        'Precision': precision,
        'Log_Bayes_Factor': log_bf,
        'Alpha_Post': alpha_post,
        'Beta_Post': beta_post
    })

bayesian_df = pd.DataFrame(bayesian_results).sort_values('Incidents', ascending=False)

print(f"\n✅ Bayesian analysis completed for {len(bayesian_df)} categories")

print(f"\n📊 Bayesian Results (Top 10 categories):")
display_cols = ['Crime_Category', 'Incidents', 'Arrests', 'Observed_Rate', 'Posterior_Mean', 'CI_Lower', 'CI_Upper', 'Effect_Size']
print(bayesian_df[display_cols].head(10).round(4).to_string(index=False))

print(f"\n📋 Additional Bayesian Metrics Summary:")
print(f"   Categories with high uncertainty (CI width > 0.1): {(bayesian_df['CI_Width'] > 0.1).sum()}")
print(f"   Categories with large effect size (>50%): {(bayesian_df['Effect_Size'] > 0.5).sum()}")
print(f"   Average precision: {bayesian_df['Precision'].mean():.2f}")
print(f"   Strongest evidence (max log BF): {bayesian_df['Log_Bayes_Factor'].max():.2f}")

print("\n5c) VISUALIZATION AND INTERPRETATION")
print("-" * 37)

# Create comprehensive visualization
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Task 5: Bayesian Analysis of Arrest Rates (COMPREHENSIVE METRICS)', fontsize=16, fontweight='bold')

# 1. Top categories with credible intervals
top_10 = bayesian_df.head(10)
y_pos = np.arange(len(top_10))

axes[0,0].errorbar(top_10['Posterior_Mean'], y_pos, 
                  xerr=[top_10['Posterior_Mean'] - top_10['CI_Lower'], 
                        top_10['CI_Upper'] - top_10['Posterior_Mean']], 
                  fmt='o', capsize=5, color='skyblue')
axes[0,0].set_yticks(y_pos)
axes[0,0].set_yticklabels([cat[:20] + '...' if len(cat) > 20 else cat for cat in top_10['Crime_Category']])
axes[0,0].set_xlabel('Arrest Rate')
axes[0,0].set_title('Posterior Arrest Rates with 95% Credible Intervals')
axes[0,0].grid(True, alpha=0.3)

# 2. Observed vs Posterior rates
axes[0,1].scatter(top_10['Observed_Rate'], top_10['Posterior_Mean'], 
                 s=top_10['Incidents']/10, alpha=0.6, color='lightcoral')
axes[0,1].plot([0, top_10[['Observed_Rate', 'Posterior_Mean']].values.max()], 
               [0, top_10[['Observed_Rate', 'Posterior_Mean']].values.max()], 
               'k--', alpha=0.5)
axes[0,1].set_xlabel('Observed Arrest Rate')
axes[0,1].set_ylabel('Posterior Mean Arrest Rate')
axes[0,1].set_title('Observed vs Posterior Arrest Rates\n(Bubble size = Incident count)')

# 3. Effect Size Analysis
axes[0,2].barh(range(len(top_10)), top_10['Effect_Size'], color='lightgreen', alpha=0.7)
axes[0,2].set_yticks(range(len(top_10)))
axes[0,2].set_yticklabels([cat[:15] + '...' if len(cat) > 15 else cat for cat in top_10['Crime_Category']])
axes[0,2].set_xlabel('Effect Size (Relative to Prior)')
axes[0,2].set_title('Effect Size by Crime Category')
axes[0,2].grid(True, alpha=0.3)

# 4. Distribution of arrest rates
axes[1,0].hist(bayesian_df['Observed_Rate'], bins=20, alpha=0.7, color='lightblue', 
              label='Observed Rates', density=True)
axes[1,0].hist(bayesian_df['Posterior_Mean'], bins=20, alpha=0.7, color='lightgreen', 
              label='Posterior Means', density=True)
axes[1,0].axvline(prior_mean, color='red', linestyle='--', label=f'Prior Mean ({prior_mean:.2f})')
axes[1,0].set_xlabel('Arrest Rate')
axes[1,0].set_ylabel('Density')
axes[1,0].set_title('Distribution of Arrest Rates')
axes[1,0].legend()

# 5. Credible interval widths
axes[1,1].scatter(top_10['Incidents'], top_10['CI_Width'], color='orange', alpha=0.7)
axes[1,1].set_xlabel('Number of Incidents')
axes[1,1].set_ylabel('95% Credible Interval Width')
axes[1,1].set_title('Uncertainty vs Sample Size')
axes[1,1].grid(True, alpha=0.3)

# 6. Precision Analysis
axes[1,2].scatter(top_10['Incidents'], top_10['Precision'], color='purple', alpha=0.7)
axes[1,2].set_xlabel('Number of Incidents')
axes[1,2].set_ylabel('Precision (1/Variance)')
axes[1,2].set_title('Precision vs Sample Size')
axes[1,2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('task5_correct_bayesian_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Key insights
print("\n📋 KEY BAYESIAN INSIGHTS (COMPREHENSIVE)")
print("-" * 40)

highest_rate = bayesian_df.loc[bayesian_df['Posterior_Mean'].idxmax()]
lowest_rate = bayesian_df.loc[bayesian_df['Posterior_Mean'].idxmin()]
most_incidents = bayesian_df.iloc[0]
largest_effect = bayesian_df.loc[bayesian_df['Effect_Size'].idxmax()]
highest_precision = bayesian_df.loc[bayesian_df['Precision'].idxmax()]

print(f"🔍 Crime category with highest arrest rate:")
print(f"   {highest_rate['Crime_Category']}: {highest_rate['Posterior_Mean']:.3f} ({highest_rate['Posterior_Mean']*100:.1f}%)")
print(f"   95% CI: [{highest_rate['CI_Lower']:.3f}, {highest_rate['CI_Upper']:.3f}]")

print(f"\n🔍 Crime category with lowest arrest rate:")
print(f"   {lowest_rate['Crime_Category']}: {lowest_rate['Posterior_Mean']:.3f} ({lowest_rate['Posterior_Mean']*100:.1f}%)")
print(f"   95% CI: [{lowest_rate['CI_Lower']:.3f}, {lowest_rate['CI_Upper']:.3f}]")

print(f"\n🔍 Most common crime category:")
print(f"   {most_incidents['Crime_Category']}: {most_incidents['Incidents']:,} incidents")
print(f"   Arrest rate: {most_incidents['Posterior_Mean']:.3f} ({most_incidents['Posterior_Mean']*100:.1f}%)")

print(f"\n🔍 Category with largest effect size:")
print(f"   {largest_effect['Crime_Category']}: {largest_effect['Effect_Size']:.3f} ({largest_effect['Effect_Size']*100:.1f}% relative to prior)")

print(f"\n🔍 Category with highest precision:")
print(f"   {highest_precision['Crime_Category']}: {highest_precision['Precision']:.2f} (lowest uncertainty)")

# Uncertainty analysis
high_uncertainty = bayesian_df[bayesian_df['CI_Width'] > 0.1]
large_effect = bayesian_df[bayesian_df['Effect_Size'] > 0.5]
print(f"\n📊 Comprehensive Analysis:")
print(f"   Categories with high uncertainty (CI width > 0.1): {len(high_uncertainty)}")
print(f"   Categories with large effect size (>50%): {len(large_effect)}")
print(f"   Average precision: {bayesian_df['Precision'].mean():.2f}")
print(f"   Strongest evidence (max log BF): {bayesian_df['Log_Bayes_Factor'].max():.2f}")

# Save results
category_summary.to_csv('task5_crime_category_summary.csv')
bayesian_df.to_csv('task5_bayesian_results.csv', index=False)

# Final report
report = f"""
TASK 5: BAYESIAN ANALYSIS RESULTS (COMPREHENSIVE)

5a) Crime Category Summary:
- Total crime categories: {len(category_summary)}
- Total incidents analyzed: {category_summary['Number_of_Incidents'].sum():,}
- Total arrests: {category_summary['Number_of_Arrests'].sum():,}
- Overall arrest rate: {incidents['ARREST'].mean()*100:.1f}% (REALISTIC!)

5b) Bayesian Model Results:
- Prior: Beta(α=2, β=8) with mean {prior_mean:.3f}
- Posterior: Beta(α + yi, β + Ni - yi) for each category
- 95% credible intervals computed for all categories
- Effect sizes calculated relative to prior mean
- Precision (inverse variance) computed for uncertainty assessment
- Bayes factors approximated for evidence strength

5c) Comprehensive Metrics:
- Categories with high uncertainty (CI width > 0.1): {len(high_uncertainty)}
- Categories with large effect size (>50%): {len(large_effect)}
- Average precision: {bayesian_df['Precision'].mean():.2f}
- Strongest evidence (max log BF): {bayesian_df['Log_Bayes_Factor'].max():.2f}

5d) Key Findings:
- Highest arrest rate: {highest_rate['Crime_Category']} ({highest_rate['Posterior_Mean']*100:.1f}%)
- Lowest arrest rate: {lowest_rate['Crime_Category']} ({lowest_rate['Posterior_Mean']*100:.1f}%)
- Most common category: {most_incidents['Crime_Category']} ({most_incidents['Incidents']:,} incidents)
- Largest effect size: {largest_effect['Crime_Category']} ({largest_effect['Effect_Size']*100:.1f}% relative to prior)
- Highest precision: {highest_precision['Crime_Category']} (precision: {highest_precision['Precision']:.2f})

Business Implications:
1. Arrest rates vary significantly across crime categories
2. Uncertainty decreases with larger sample sizes
3. Bayesian approach properly quantifies uncertainty
4. Effect sizes identify categories most different from prior expectations
5. Precision metrics guide resource allocation decisions
6. Credible intervals provide honest uncertainty assessment
7. Comprehensive metrics support evidence-based policy making
"""

with open('task5_bayesian_report.txt', 'w') as f:
    f.write(report)

print(f"\n✅ TASK 5 COMPLETE - BAYESIAN ANALYSIS")
print(f"📊 Analyzed {len(category_summary)} crime categories")
print(f"📈 Realistic arrest rates: {incidents['ARREST'].mean()*100:.1f}% overall")
print(f"📁 Results saved: task5_bayesian_results.csv")
print(f"📋 Report saved: task5_bayesian_report.txt")

print("\n" + "="*70)
print("READY FOR TASK 6: EXECUTIVE SUMMARY")
print("="*70)