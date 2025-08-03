#!/usr/bin/env python3
"""
ATPA Assessment - Task 5: Improved Bayesian Analysis
June-August 2025
NMInsights Crime Analysis

IMPROVED VERSION: Better scaled posterior distributions for top 5 categories
Enhanced visualizations with proper scaling and readability
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('default')
sns.set_palette("husl")

print("="*70)
print("ATPA ASSESSMENT - TASK 5: IMPROVED BAYESIAN ANALYSIS")
print("="*70)

# Load original data to get crime categories
print("🔧 Loading original data for crime category analysis...")
incidents = pd.read_csv('ATPA August/ATPA_June_August_2025/Task1_DataPrep/incidents.csv')
arrestee = pd.read_csv('ATPA August/ATPA_June_August_2025/Task1_DataPrep/arrestee.csv')

print(f"✅ Incidents: {len(incidents):,} records")
print(f"✅ Arrestee: {len(arrestee):,} records")

# Create ARREST indicator
arrest_incident_ids = set(arrestee['incident_id'].unique())
incidents['ARREST'] = incidents['incident_id'].isin(arrest_incident_ids).astype(int)

print(f"🎯 Overall arrest rate: {incidents['ARREST'].mean()*100:.1f}%")

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

print("\n5c) IMPROVED VISUALIZATION WITH BETTER SCALING")
print("-" * 50)

# Get top 5 categories for focused analysis
top_5 = bayesian_df.head(5)

print(f"🎯 Creating improved visualizations for top 5 categories:")
for i, (_, row) in enumerate(top_5.iterrows(), 1):
    print(f"   {i}. {row['Crime_Category']}: {row['Posterior_Mean']:.3f} ({row['Posterior_Mean']*100:.1f}%)")

# Create improved visualization with better scaling
fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('Task 5: Improved Bayesian Analysis - Top 5 Crime Categories', fontsize=16, fontweight='bold')

# 1. IMPROVED: Posterior distributions for top 5 categories (BETTER SCALED)
print("\n📊 Creating improved posterior distributions...")
x = np.linspace(0, 1, 1000)

# Create better scaled posterior distributions
for i, (_, row) in enumerate(top_5.iterrows()):
    alpha_post = row['Alpha_Post']
    beta_post = row['Beta_Post']
    posterior_pdf = stats.beta.pdf(x, alpha_post, beta_post)
    
    # Scale the PDF for better visualization
    scaled_pdf = posterior_pdf / posterior_pdf.max() * 0.8  # Scale to 80% of max height
    
    axes[0,0].plot(x, scaled_pdf, linewidth=2.5, 
                   label=f"{row['Crime_Category'][:20]}... ({row['Posterior_Mean']:.3f})")
    
    # Add vertical line for posterior mean
    axes[0,0].axvline(row['Posterior_Mean'], color='red', linestyle='--', alpha=0.7, linewidth=1)

axes[0,0].set_xlabel('Arrest Rate', fontsize=12)
axes[0,0].set_ylabel('Scaled Posterior Density', fontsize=12)
axes[0,0].set_title('Improved Posterior Distributions (Top 5 Categories)', fontsize=14, fontweight='bold')
axes[0,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
axes[0,0].grid(True, alpha=0.3)
axes[0,0].set_xlim(0, 1)

# 2. IMPROVED: Credible intervals with better scaling
print("📊 Creating improved credible intervals...")
y_pos = np.arange(len(top_5))

# Create horizontal error bars with better scaling
axes[0,1].errorbar(top_5['Posterior_Mean'], y_pos, 
                  xerr=[top_5['Posterior_Mean'] - top_5['CI_Lower'], 
                        top_5['CI_Upper'] - top_5['Posterior_Mean']], 
                  fmt='o', capsize=8, capthick=2, markersize=8, 
                  color='skyblue', ecolor='darkblue', elinewidth=2)

axes[0,1].set_yticks(y_pos)
axes[0,1].set_yticklabels([cat[:25] + '...' if len(cat) > 25 else cat for cat in top_5['Crime_Category']], fontsize=11)
axes[0,1].set_xlabel('Arrest Rate', fontsize=12)
axes[0,1].set_title('95% Credible Intervals (Top 5 Categories)', fontsize=14, fontweight='bold')
axes[0,1].grid(True, alpha=0.3)
axes[0,1].set_xlim(0, 1)

# Add value labels on the points
for i, (_, row) in enumerate(top_5.iterrows()):
    axes[0,1].text(row['Posterior_Mean'] + 0.02, i, f'{row["Posterior_Mean"]:.3f}', 
                   fontsize=10, va='center', fontweight='bold')

# 3. IMPROVED: Effect size comparison
print("📊 Creating improved effect size comparison...")
colors = plt.cm.Set3(np.linspace(0, 1, len(top_5)))
bars = axes[1,0].barh(range(len(top_5)), top_5['Effect_Size'], color=colors, alpha=0.8, height=0.6)

axes[1,0].set_yticks(range(len(top_5)))
axes[1,0].set_yticklabels([cat[:20] + '...' if len(cat) > 20 else cat for cat in top_5['Crime_Category']], fontsize=11)
axes[1,0].set_xlabel('Effect Size (Relative to Prior)', fontsize=12)
axes[1,0].set_title('Effect Size by Crime Category', fontsize=14, fontweight='bold')
axes[1,0].grid(True, alpha=0.3)

# Add value labels on bars
for i, (bar, _, row) in enumerate(zip(bars, range(len(top_5)), top_5.iterrows())):
    width = bar.get_width()
    axes[1,0].text(width + 0.01, bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
                   ha='left', va='center', fontsize=10, fontweight='bold')

# 4. IMPROVED: Precision vs Sample Size
print("📊 Creating improved precision analysis...")
scatter = axes[1,1].scatter(top_5['Incidents'], top_5['Precision'], 
                           s=top_5['Incidents']/50, alpha=0.7, 
                           c=range(len(top_5)), cmap='viridis')

axes[1,1].set_xlabel('Number of Incidents', fontsize=12)
axes[1,1].set_ylabel('Precision (1/Variance)', fontsize=12)
axes[1,1].set_title('Precision vs Sample Size', fontsize=14, fontweight='bold')
axes[1,1].grid(True, alpha=0.3)

# Add category labels to scatter points with better positioning
for i, (_, row) in enumerate(top_5.iterrows()):
    # Calculate offset based on position to avoid overlap
    x_offset = 200 if row['Incidents'] < 10000 else -200
    y_offset = 5000 if row['Precision'] < 150000 else -5000
    
    axes[1,1].annotate(row['Crime_Category'][:20] + '...', 
                      (row['Incidents'], row['Precision']),
                      xytext=(x_offset, y_offset), 
                      textcoords='offset points', 
                      fontsize=10, alpha=0.9, fontweight='bold',
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                      arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2', alpha=0.7))

plt.tight_layout(pad=2.0)
plt.savefig('task5_improved_bayesian_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Create additional focused visualization for posterior distributions
print("\n📊 Creating additional focused posterior distribution plot...")
fig2, ax = plt.subplots(1, 1, figsize=(12, 8))

# Generate x values for smooth curves
x = np.linspace(0, 1, 1000)

# Plot posterior distributions with better scaling and colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, (_, row) in enumerate(top_5.iterrows()):
    alpha_post = row['Alpha_Post']
    beta_post = row['Beta_Post']
    posterior_pdf = stats.beta.pdf(x, alpha_post, beta_post)
    
    # Scale for better visualization
    scaled_pdf = posterior_pdf / posterior_pdf.max() * 0.9
    
    ax.plot(x, scaled_pdf, linewidth=3, color=colors[i],
            label=f"{row['Crime_Category'][:25]}... (μ={row['Posterior_Mean']:.3f})")
    
    # Add vertical line for posterior mean
    ax.axvline(row['Posterior_Mean'], color=colors[i], linestyle='--', alpha=0.7, linewidth=1.5)

# Add prior distribution for comparison
prior_pdf = stats.beta.pdf(x, alpha_prior, beta_prior)
scaled_prior = prior_pdf / prior_pdf.max() * 0.6
ax.plot(x, scaled_prior, linewidth=2, color='gray', linestyle=':', 
        label=f'Prior Beta({alpha_prior},{beta_prior}) (μ={prior_mean:.3f})')

ax.set_xlabel('Arrest Rate', fontsize=14)
ax.set_ylabel('Scaled Posterior Density', fontsize=14)
ax.set_title('Focused Posterior Distributions: Top 5 Crime Categories', fontsize=16, fontweight='bold')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 1)

plt.tight_layout()
plt.savefig('task5_focused_posterior_distributions.png', dpi=300, bbox_inches='tight')
plt.show()

# Key insights
print("\n📋 KEY IMPROVED BAYESIAN INSIGHTS")
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

# Top 5 specific insights
print(f"\n🎯 TOP 5 CATEGORIES ANALYSIS:")
for i, (_, row) in enumerate(top_5.iterrows(), 1):
    print(f"   {i}. {row['Crime_Category'][:30]}...")
    print(f"      Arrest Rate: {row['Posterior_Mean']:.3f} ({row['Posterior_Mean']*100:.1f}%)")
    print(f"      95% CI: [{row['CI_Lower']:.3f}, {row['CI_Upper']:.3f}]")
    print(f"      Effect Size: {row['Effect_Size']:.2f}")
    print(f"      Precision: {row['Precision']:.2f}")
    print()

print(f"\n✅ IMPROVED TASK 5 COMPLETE - BAYESIAN ANALYSIS")
print(f"📊 Analyzed {len(category_summary)} crime categories")
print(f"📈 Focused on top 5 categories with improved scaling")
print(f"📁 Generated improved visualizations:")
print(f"   - task5_improved_bayesian_analysis.png")
print(f"   - task5_focused_posterior_distributions.png")

print("\n" + "="*70)
print("IMPROVED VISUALIZATIONS READY!")
print("="*70) 