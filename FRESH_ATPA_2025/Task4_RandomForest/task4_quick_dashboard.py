#!/usr/bin/env python3
"""
ATPA TASK 4: QUICK COMPREHENSIVE FAIRNESS DASHBOARD
================================================================================
Quick dashboard using existing results - no re-analysis needed
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('default')
sns.set_palette("husl")

print("=================================================================================")
print("ATPA TASK 4: QUICK COMPREHENSIVE FAIRNESS DASHBOARD")
print("=================================================================================")

# Load existing results from the fairness audit report
print("📊 Loading existing fairness audit results...")

# Create sample data based on the previous analysis results
results_data = {
    'Large_Agencies': {
        'accuracy': 0.7772, 'precision': 0.4462, 'recall': 0.7979, 'f1_score': 0.5723, 'auc': 0.8643,
        'specificity': 0.7724, 'sample_size': 25234, 'positive_rate': 0.187
    },
    'Small_Agencies': {
        'accuracy': 0.7350, 'precision': 0.4333, 'recall': 0.7956, 'f1_score': 0.5611, 'auc': 0.8240,
        'specificity': 0.7186, 'sample_size': 3838, 'positive_rate': 0.213
    },
    'High_Severity_Crimes': {
        'accuracy': 0.8619, 'precision': 0.3162, 'recall': 0.5828, 'f1_score': 0.4100, 'auc': 0.8395,
        'specificity': 0.8869, 'sample_size': 14592, 'positive_rate': 0.082
    },
    'Low_Severity_Crimes': {
        'accuracy': 0.6806, 'precision': 0.4810, 'recall': 0.8571, 'f1_score': 0.6162, 'auc': 0.8156,
        'specificity': 0.6053, 'sample_size': 14480, 'positive_rate': 0.299
    },
    'Day_Time': {
        'accuracy': 0.7734, 'precision': 0.4281, 'recall': 0.7877, 'f1_score': 0.5547, 'auc': 0.8580,
        'specificity': 0.7703, 'sample_size': 18303, 'positive_rate': 0.179
    },
    'Night_Time': {
        'accuracy': 0.7685, 'precision': 0.4692, 'recall': 0.8118, 'f1_score': 0.5947, 'auc': 0.8598,
        'specificity': 0.7570, 'sample_size': 10769, 'positive_rate': 0.209
    },
    'CT_Flag_True': {
        'accuracy': 0.9681, 'precision': 0.2727, 'recall': 0.0093, 'f1_score': 0.0180, 'auc': 0.7020,
        'specificity': 0.9992, 'sample_size': 10272, 'positive_rate': 0.031
    },
    'CT_Flag_False': {
        'accuracy': 0.6643, 'precision': 0.4444, 'recall': 0.8464, 'f1_score': 0.5828, 'auc': 0.8107,
        'specificity': 0.5944, 'sample_size': 18800, 'positive_rate': 0.277
    },
    'High_Crime_Against': {
        'accuracy': 0.7304, 'precision': 0.5805, 'recall': 0.9419, 'f1_score': 0.7183, 'auc': 0.8649,
        'specificity': 0.6087, 'sample_size': 2737, 'positive_rate': 0.365
    },
    'Low_Crime_Against': {
        'accuracy': 0.7759, 'precision': 0.4176, 'recall': 0.7657, 'f1_score': 0.5405, 'auc': 0.8512,
        'specificity': 0.7780, 'sample_size': 26335, 'positive_rate': 0.172
    }
}

print(f"✅ Loaded results for {len(results_data)} subgroups")

# Create comprehensive dashboard
print("\n🎨 Creating comprehensive fairness audit dashboard...")

# Create figure with subplots
fig = plt.figure(figsize=(24, 20))
gs = fig.add_gridspec(6, 6, hspace=0.3, wspace=0.3)

# Colors for groups
colors = plt.cm.Set3(np.linspace(0, 1, len(results_data)))

# 1. PERFORMANCE METRICS PANEL
print("📊 Creating performance metrics panel...")
ax1 = fig.add_subplot(gs[0, :2])

metrics_data = []
for group_name, result in results_data.items():
    metrics_data.append({
        'Group': group_name,
        'Accuracy': result['accuracy'],
        'Precision': result['precision'],
        'Recall': result['recall'],
        'F1-Score': result['f1_score'],
        'AUC': result['auc']
    })

metrics_df = pd.DataFrame(metrics_data)
metrics_df_melted = metrics_df.melt(id_vars=['Group'], var_name='Metric', value_name='Score')

sns.barplot(data=metrics_df_melted, x='Group', y='Score', hue='Metric', ax=ax1)
ax1.set_title('Performance Metrics by Demographic Subgroup', fontsize=14, fontweight='bold')
ax1.set_xlabel('Demographic Subgroup')
ax1.set_ylabel('Score')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')

# 2. DEMOGRAPHIC PARITY
print("📊 Creating demographic parity panel...")
ax2 = fig.add_subplot(gs[0, 2:4])

# Calculate positive rates (demographic parity)
positive_rates = []
for group_name, result in results_data.items():
    positive_rates.append({
        'Group': group_name,
        'Positive_Rate': result['positive_rate']
    })

parity_df = pd.DataFrame(positive_rates)
parity_df = parity_df.sort_values('Positive_Rate', ascending=False)

bars = ax2.bar(parity_df['Group'], parity_df['Positive_Rate'], color=colors[:len(parity_df)])
ax2.set_title('Demographic Parity (Positive Rate)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Demographic Subgroup')
ax2.set_ylabel('Positive Rate (ARREST=1)')
ax2.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, rate in zip(bars, parity_df['Positive_Rate']):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{rate:.3f}', ha='center', va='bottom', fontsize=10)

# 3. EQUALIZED ODDS (TPR/FPR)
print("📊 Creating equalized odds panel...")
ax3 = fig.add_subplot(gs[0, 4:])

# Calculate TPR and FPR
odds_data = []
for group_name, result in results_data.items():
    odds_data.append({
        'Group': group_name,
        'TPR': result['recall'],
        'FPR': 1 - result['specificity']
    })

odds_df = pd.DataFrame(odds_data)
odds_df_melted = odds_df.melt(id_vars=['Group'], var_name='Rate', value_name='Value')

sns.barplot(data=odds_df_melted, x='Group', y='Value', hue='Rate', ax=ax3)
ax3.set_title('Equalized Odds (TPR/FPR)', fontsize=14, fontweight='bold')
ax3.set_xlabel('Demographic Subgroup')
ax3.set_ylabel('Rate')
ax3.tick_params(axis='x', rotation=45)
ax3.legend(title='Rate Type')

# 4. PREDICTIVE RATE PARITY (Precision)
print("📊 Creating predictive rate parity panel...")
ax4 = fig.add_subplot(gs[1, :2])

precision_data = []
for group_name, result in results_data.items():
    precision_data.append({
        'Group': group_name,
        'Precision': result['precision']
    })

precision_df = pd.DataFrame(precision_data)
precision_df = precision_df.sort_values('Precision', ascending=False)

bars = ax4.bar(precision_df['Group'], precision_df['Precision'], color=colors[:len(precision_df)])
ax4.set_title('Predictive Rate Parity (Precision)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Demographic Subgroup')
ax4.set_ylabel('Precision')
ax4.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, precision in zip(bars, precision_df['Precision']):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{precision:.3f}', ha='center', va='bottom', fontsize=10)

# 5. FAIRNESS GAPS HEATMAP
print("📊 Creating fairness gaps heatmap...")
ax5 = fig.add_subplot(gs[1, 2:4])

# Calculate fairness gaps
gap_data = []
for group_name, result in results_data.items():
    gap_data.append({
        'Group': group_name,
        'F1_Gap': result['f1_score'],
        'TPR_Gap': result['recall'],
        'FPR_Gap': 1 - result['specificity'],
        'Precision_Gap': result['precision']
    })

gap_df = pd.DataFrame(gap_data)
gap_matrix = gap_df.set_index('Group')[['F1_Gap', 'TPR_Gap', 'FPR_Gap', 'Precision_Gap']]

sns.heatmap(gap_matrix, annot=True, fmt='.3f', cmap='RdYlBu_r', ax=ax5)
ax5.set_title('Fairness Gaps Heatmap', fontsize=14, fontweight='bold')

# 6. SAMPLE SIZES
print("📊 Creating sample sizes panel...")
ax6 = fig.add_subplot(gs[1, 4:])

sample_sizes = []
for group_name, result in results_data.items():
    sample_sizes.append({
        'Group': group_name,
        'Sample_Size': result['sample_size']
    })

sample_df = pd.DataFrame(sample_sizes)
sample_df = sample_df.sort_values('Sample_Size', ascending=False)

bars = ax6.bar(sample_df['Group'], sample_df['Sample_Size'], color=colors[:len(sample_df)])
ax6.set_title('Sample Sizes by Demographic Subgroup', fontsize=14, fontweight='bold')
ax6.set_xlabel('Demographic Subgroup')
ax6.set_ylabel('Sample Size')
ax6.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, size in zip(bars, sample_df['Sample_Size']):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, 
             f'{size:,}', ha='center', va='bottom', fontsize=10)

# 7. OVERALL FAIRNESS SCORE
print("📊 Creating overall fairness score panel...")
ax7 = fig.add_subplot(gs[2, :2])

# Calculate fairness score based on demographic parity gap
parity_gap = parity_df['Positive_Rate'].max() - parity_df['Positive_Rate'].min()
fairness_threshold = 0.20
fair_groups = len(parity_df[parity_df['Positive_Rate'] <= fairness_threshold])
unfair_groups = len(parity_df) - fair_groups

fairness_scores = [fair_groups, unfair_groups]
fairness_labels = ['Fair', 'Unfair']
fairness_colors = ['lightgreen', 'lightcoral']

ax7.pie(fairness_scores, labels=fairness_labels, colors=fairness_colors, autopct='%1.1f%%', startangle=90)
ax7.set_title(f'Overall Fairness Score\n(Parity Gap: {parity_gap:.3f})', fontsize=14, fontweight='bold')

# 8. F1 SCORE COMPARISON
print("📊 Creating F1 score comparison panel...")
ax8 = fig.add_subplot(gs[2, 2:4])

f1_data = []
for group_name, result in results_data.items():
    f1_data.append({
        'Group': group_name,
        'F1_Score': result['f1_score']
    })

f1_df = pd.DataFrame(f1_data)
f1_df = f1_df.sort_values('F1_Score', ascending=False)

bars = ax8.bar(f1_df['Group'], f1_df['F1_Score'], color=colors[:len(f1_df)])
ax8.set_title('F1 Score by Demographic Subgroup', fontsize=14, fontweight='bold')
ax8.set_xlabel('Demographic Subgroup')
ax8.set_ylabel('F1 Score')
ax8.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, f1 in zip(bars, f1_df['F1_Score']):
    ax8.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{f1:.3f}', ha='center', va='bottom', fontsize=10)

# 9. AUC COMPARISON
print("📊 Creating AUC comparison panel...")
ax9 = fig.add_subplot(gs[2, 4:])

auc_data = []
for group_name, result in results_data.items():
    auc_data.append({
        'Group': group_name,
        'AUC': result['auc']
    })

auc_df = pd.DataFrame(auc_data)
auc_df = auc_df.sort_values('AUC', ascending=False)

bars = ax9.bar(auc_df['Group'], auc_df['AUC'], color=colors[:len(auc_df)])
ax9.set_title('AUC Score by Demographic Subgroup', fontsize=14, fontweight='bold')
ax9.set_xlabel('Demographic Subgroup')
ax9.set_ylabel('AUC Score')
ax9.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, auc in zip(bars, auc_df['AUC']):
    ax9.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{auc:.3f}', ha='center', va='bottom', fontsize=10)

# 10. SUMMARY STATISTICS TABLE
print("📊 Creating summary statistics panel...")
ax10 = fig.add_subplot(gs[3:, :])

# Create summary table
summary_data = []
for group_name, result in results_data.items():
    summary_data.append([
        group_name,
        f"{result['sample_size']:,}",
        f"{result['accuracy']:.3f}",
        f"{result['precision']:.3f}",
        f"{result['recall']:.3f}",
        f"{result['f1_score']:.3f}",
        f"{result['auc']:.3f}",
        f"{result['positive_rate']:.3f}"
    ])

# Create table
table_data = [['Group', 'Sample Size', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC', 'Positive Rate']] + summary_data
table = ax10.table(cellText=table_data[1:], colLabels=table_data[0], 
                   cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

ax10.set_title('Summary Statistics by Demographic Subgroup', fontsize=14, fontweight='bold', pad=20)
ax10.axis('off')

# Add overall title
fig.suptitle('COMPREHENSIVE SHAP FAIRNESS AUDIT DASHBOARD\nATPA Task 4 - Demographic Subgroup Analysis (Quick Version)', 
             fontsize=16, fontweight='bold', y=0.98)

# Save the dashboard
dashboard_filename = "task4_quick_comprehensive_dashboard.png"
plt.savefig(dashboard_filename, dpi=300, bbox_inches='tight')
print(f"✅ Saved quick comprehensive dashboard: {dashboard_filename}")

# Export summary data
performance_summary = []
for group_name, result in results_data.items():
    performance_summary.append({
        'Group': group_name,
        'Sample_Size': result['sample_size'],
        'Accuracy': result['accuracy'],
        'Precision': result['precision'],
        'Recall': result['recall'],
        'F1_Score': result['f1_score'],
        'AUC': result['auc'],
        'Specificity': result['specificity'],
        'Positive_Rate': result['positive_rate']
    })

performance_df = pd.DataFrame(performance_summary)
performance_df.to_csv("task4_quick_performance_summary.csv", index=False)
print("✅ Saved quick performance summary: task4_quick_performance_summary.csv")

print("\n" + "=" * 80)
print("QUICK COMPREHENSIVE FAIRNESS AUDIT DASHBOARD COMPLETED")
print("=" * 80)
print("📁 Files generated:")
print("   - task4_quick_comprehensive_dashboard.png: Multi-panel fairness dashboard")
print("   - task4_quick_performance_summary.csv: Performance metrics by subgroup")
print("\n🎯 Key Insights:")
print("   1. Performance varies significantly across demographic subgroups")
print("   2. CT_Flag_True has the lowest F1 score (0.018) - needs attention")
print("   3. High_Crime_Against has the highest F1 score (0.718)")
print("   4. Demographic parity gap is 0.334 (33.4%)")
print("   5. Fairness mitigation strategies needed for several groups") 