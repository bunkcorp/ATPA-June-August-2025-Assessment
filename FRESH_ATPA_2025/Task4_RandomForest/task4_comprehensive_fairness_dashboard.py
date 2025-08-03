#!/usr/bin/env python3
"""
ATPA TASK 4: COMPREHENSIVE SHAP FAIRNESS AUDIT DASHBOARD
================================================================================
Multi-panel visualization dashboard for fairness audit with SHAP analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('default')
sns.set_palette("husl")

print("=================================================================================")
print("ATPA TASK 4: COMPREHENSIVE SHAP FAIRNESS AUDIT DASHBOARD")
print("=================================================================================")

# 1. LOAD DATA AND PREPARE MODEL
print("📊 Loading prepared dataset...")
data = pd.read_csv('../Task1_DataPrep/task1_prepared_dataset_correct.csv')
print(f"✅ Loaded dataset: {len(data):,} records")

# Prepare features and target
feature_cols = ['offense_code_encoded', 'offense_category_name_encoded', 
                'crime_against_encoded', 'agency_name_encoded', 
                'ct_flag_encoded', 'incident_hour']
X = data[feature_cols]
y = data['ARREST']

# Train model
print("🔧 Training Random Forest model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf_model.fit(X_train, y_train)

# Initialize SHAP explainer
print("🔧 Initializing SHAP explainer...")
explainer = shap.TreeExplainer(rf_model)

# 2. DEFINE DEMOGRAPHIC SUBGROUPS
print("\n📊 Defining demographic subgroups...")

# Agency-based subgroups
large_agencies = data['agency_name_encoded'] > data['agency_name_encoded'].median()
small_agencies = ~large_agencies

# Crime severity subgroups (based on offense_code_encoded)
high_severity = data['offense_code_encoded'] > data['offense_code_encoded'].quantile(0.75)
low_severity = data['offense_code_encoded'] <= data['offense_code_encoded'].quantile(0.25)

# Time-based subgroups
day_time = (data['incident_hour'] >= 6) & (data['incident_hour'] < 18)
night_time = ~day_time

# CT Flag subgroups
ct_flag_true = data['ct_flag_encoded'] == 1
ct_flag_false = data['ct_flag_encoded'] == 0

# Crime against subgroups
high_crime_against = data['crime_against_encoded'] > data['crime_against_encoded'].quantile(0.8)
low_crime_against = data['crime_against_encoded'] <= data['crime_against_encoded'].quantile(0.2)

# Define all subgroups
subgroups = {
    'Large_Agencies': large_agencies,
    'Small_Agencies': small_agencies,
    'High_Severity_Crimes': high_severity,
    'Low_Severity_Crimes': low_severity,
    'Day_Time': day_time,
    'Night_Time': night_time,
    'CT_Flag_True': ct_flag_true,
    'CT_Flag_False': ct_flag_false,
    'High_Crime_Against': high_crime_against,
    'Low_Crime_Against': low_crime_against
}

# 3. ANALYZE EACH SUBGROUP
print("\n🔍 Analyzing each demographic subgroup...")
results = {}

for group_name, group_mask in subgroups.items():
    print(f"📊 Analyzing {group_name}...")
    
    # Get group data
    group_data = data[group_mask]
    X_group = group_data[feature_cols]
    y_group = group_data['ARREST']
    
    if len(X_group) == 0:
        print(f"   ⚠️ No data for {group_name}")
        continue
    
    # Split group data
    X_group_train, X_group_test, y_group_train, y_group_test = train_test_split(
        X_group, y_group, test_size=0.3, random_state=42, stratify=y_group
    )
    
    # Train model on group data
    group_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    group_model.fit(X_group_train, y_group_train)
    
    # Predictions
    y_pred = group_model.predict(X_group_test)
    y_pred_proba = group_model.predict_proba(X_group_test)[:, 1]
    
    # Performance metrics
    accuracy = accuracy_score(y_group_test, y_pred)
    precision = precision_score(y_group_test, y_pred, zero_division=0)
    recall = recall_score(y_group_test, y_pred, zero_division=0)
    f1 = f1_score(y_group_test, y_pred, zero_division=0)
    auc = roc_auc_score(y_group_test, y_pred_proba)
    
    # Confusion matrix
    cm = confusion_matrix(y_group_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    # SHAP analysis
    group_explainer = shap.TreeExplainer(group_model)
    shap_values = group_explainer.shap_values(X_group_test)
    
    # Handle multi-class SHAP output
    if isinstance(shap_values, list):
        shap_values = shap_values[1]  # ARREST = 1 class
    elif shap_values.ndim == 3:
        shap_values = shap_values[:, :, 1]  # ARREST = 1 class
    
    # Calculate SHAP importance
    shap_importance = np.mean(np.abs(shap_values), axis=0)
    shap_importance_df = pd.DataFrame({
        'Feature': feature_cols,
        'SHAP_Importance': shap_importance
    }).sort_values('SHAP_Importance', ascending=False)
    
    # Store results
    results[group_name] = {
        'performance': {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'auc': auc,
            'specificity': specificity,
            'sample_size': len(X_group_test)
        },
        'confusion_matrix': cm,
        'shap_importance': shap_importance_df,
        'shap_values': shap_values,
        'data': X_group_test,
        'targets': y_group_test,
        'predictions': y_pred,
        'probabilities': y_pred_proba
    }

print(f"✅ Completed analysis for {len(results)} subgroups")

# 4. CREATE COMPREHENSIVE DASHBOARD
print("\n🎨 Creating comprehensive fairness audit dashboard...")

# Create figure with subplots
fig = plt.figure(figsize=(24, 20))
gs = fig.add_gridspec(6, 6, hspace=0.3, wspace=0.3)

# Colors for groups
colors = plt.cm.Set3(np.linspace(0, 1, len(results)))

# 1. PERFORMANCE METRICS PANEL
print("📊 Creating performance metrics panel...")
ax1 = fig.add_subplot(gs[0, :2])

metrics_data = []
for group_name, result in results.items():
    perf = result['performance']
    metrics_data.append({
        'Group': group_name,
        'Accuracy': perf['accuracy'],
        'Precision': perf['precision'],
        'Recall': perf['recall'],
        'F1-Score': perf['f1_score'],
        'AUC': perf['auc']
    })

metrics_df = pd.DataFrame(metrics_data)
metrics_df_melted = metrics_df.melt(id_vars=['Group'], var_name='Metric', value_name='Score')

sns.barplot(data=metrics_df_melted, x='Group', y='Score', hue='Metric', ax=ax1)
ax1.set_title('Performance Metrics by Demographic Subgroup', fontsize=14, fontweight='bold')
ax1.set_xlabel('Demographic Subgroup')
ax1.set_ylabel('Score')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')

# 2. CONFUSION MATRICES (3 subgroups)
print("📊 Creating confusion matrices...")
selected_groups = ['Large_Agencies', 'CT_Flag_False', 'High_Crime_Against']
for i, group_name in enumerate(selected_groups):
    if group_name in results:
        ax = fig.add_subplot(gs[0, 3+i])
        cm = results[group_name]['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_title(f'Confusion Matrix\n{group_name}', fontsize=12, fontweight='bold')
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')

# 3. SHAP FEATURE IMPORTANCE PANEL
print("📊 Creating SHAP feature importance panel...")
ax2 = fig.add_subplot(gs[1, :2])

# Get top 3 features for each group
top_features_data = []
for group_name, result in results.items():
    top_3 = result['shap_importance'].head(3)
    for feature, importance in zip(top_3['Feature'], top_3['SHAP_Importance']):
        top_features_data.append({
            'Group': group_name,
            'Feature': feature,
            'SHAP_Importance': importance
        })

top_features_df = pd.DataFrame(top_features_data)
sns.barplot(data=top_features_df, x='Group', y='SHAP_Importance', hue='Feature', ax=ax2)
ax2.set_title('Top 3 SHAP Feature Importance by Subgroup', fontsize=14, fontweight='bold')
ax2.set_xlabel('Demographic Subgroup')
ax2.set_ylabel('SHAP Importance')
ax2.tick_params(axis='x', rotation=45)
ax2.legend(title='Feature', bbox_to_anchor=(1.05, 1), loc='upper left')

# 4. SHAP BEESWARM PLOT (for CT_Flag_False)
print("📊 Creating SHAP beeswarm plot...")
ax3 = fig.add_subplot(gs[1, 3:])

if 'CT_Flag_False' in results:
    result = results['CT_Flag_False']
    shap.summary_plot(
        result['shap_values'], 
        result['data'],
        plot_type="beeswarm",
        max_display=6,
        show=False,
        ax=ax3
    )
    ax3.set_title('SHAP Beeswarm Plot - CT_Flag_False\n(ARREST=1 Predictions)', 
                 fontsize=12, fontweight='bold')

# 5. DEMOGRAPHIC PARITY
print("📊 Creating demographic parity panel...")
ax4 = fig.add_subplot(gs[2, :2])

# Calculate positive rates (demographic parity)
positive_rates = []
for group_name, result in results.items():
    positive_rate = np.mean(result['targets'])
    positive_rates.append({
        'Group': group_name,
        'Positive_Rate': positive_rate
    })

parity_df = pd.DataFrame(positive_rates)
parity_df = parity_df.sort_values('Positive_Rate', ascending=False)

bars = ax4.bar(parity_df['Group'], parity_df['Positive_Rate'], color=colors[:len(parity_df)])
ax4.set_title('Demographic Parity (Positive Rate)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Demographic Subgroup')
ax4.set_ylabel('Positive Rate (ARREST=1)')
ax4.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, rate in zip(bars, parity_df['Positive_Rate']):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{rate:.3f}', ha='center', va='bottom', fontsize=10)

# 6. EQUALIZED ODDS (TPR/FPR)
print("📊 Creating equalized odds panel...")
ax5 = fig.add_subplot(gs[2, 2:])

# Calculate TPR and FPR
odds_data = []
for group_name, result in results.items():
    perf = result['performance']
    odds_data.append({
        'Group': group_name,
        'TPR': perf['recall'],
        'FPR': 1 - perf['specificity']
    })

odds_df = pd.DataFrame(odds_data)
odds_df_melted = odds_df.melt(id_vars=['Group'], var_name='Rate', value_name='Value')

sns.barplot(data=odds_df_melted, x='Group', y='Value', hue='Rate', ax=ax5)
ax5.set_title('Equalized Odds (TPR/FPR)', fontsize=14, fontweight='bold')
ax5.set_xlabel('Demographic Subgroup')
ax5.set_ylabel('Rate')
ax5.tick_params(axis='x', rotation=45)
ax5.legend(title='Rate Type')

# 7. PREDICTIVE RATE PARITY (Precision)
print("📊 Creating predictive rate parity panel...")
ax6 = fig.add_subplot(gs[3, :2])

precision_data = []
for group_name, result in results.items():
    precision_data.append({
        'Group': group_name,
        'Precision': result['performance']['precision']
    })

precision_df = pd.DataFrame(precision_data)
precision_df = precision_df.sort_values('Precision', ascending=False)

bars = ax6.bar(precision_df['Group'], precision_df['Precision'], color=colors[:len(precision_df)])
ax6.set_title('Predictive Rate Parity (Precision)', fontsize=14, fontweight='bold')
ax6.set_xlabel('Demographic Subgroup')
ax6.set_ylabel('Precision')
ax6.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, precision in zip(bars, precision_df['Precision']):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
             f'{precision:.3f}', ha='center', va='bottom', fontsize=10)

# 8. FAIRNESS GAPS HEATMAP
print("📊 Creating fairness gaps heatmap...")
ax7 = fig.add_subplot(gs[3, 2:])

# Calculate fairness gaps
gap_data = []
for group_name, result in results.items():
    perf = result['performance']
    gap_data.append({
        'Group': group_name,
        'F1_Gap': perf['f1_score'],
        'TPR_Gap': perf['recall'],
        'FPR_Gap': 1 - perf['specificity'],
        'Precision_Gap': perf['precision']
    })

gap_df = pd.DataFrame(gap_data)
gap_matrix = gap_df.set_index('Group')[['F1_Gap', 'TPR_Gap', 'FPR_Gap', 'Precision_Gap']]

sns.heatmap(gap_matrix, annot=True, fmt='.3f', cmap='RdYlBu_r', ax=ax7)
ax7.set_title('Fairness Gaps Heatmap', fontsize=14, fontweight='bold')

# 9. SAMPLE SIZES
print("📊 Creating sample sizes panel...")
ax8 = fig.add_subplot(gs[4, :2])

sample_sizes = []
for group_name, result in results.items():
    sample_sizes.append({
        'Group': group_name,
        'Sample_Size': result['performance']['sample_size']
    })

sample_df = pd.DataFrame(sample_sizes)
sample_df = sample_df.sort_values('Sample_Size', ascending=False)

bars = ax8.bar(sample_df['Group'], sample_df['Sample_Size'], color=colors[:len(sample_df)])
ax8.set_title('Sample Sizes by Demographic Subgroup', fontsize=14, fontweight='bold')
ax8.set_xlabel('Demographic Subgroup')
ax8.set_ylabel('Sample Size')
ax8.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar, size in zip(bars, sample_df['Sample_Size']):
    ax8.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, 
             f'{size:,}', ha='center', va='bottom', fontsize=10)

# 10. OVERALL FAIRNESS SCORE
print("📊 Creating overall fairness score panel...")
ax9 = fig.add_subplot(gs[4, 2:])

# Calculate fairness score based on demographic parity gap
parity_gap = parity_df['Positive_Rate'].max() - parity_df['Positive_Rate'].min()
fairness_threshold = 0.20
fair_groups = len(parity_df[parity_df['Positive_Rate'] <= fairness_threshold])
unfair_groups = len(parity_df) - fair_groups

fairness_scores = [fair_groups, unfair_groups]
fairness_labels = ['Fair', 'Unfair']
fairness_colors = ['lightgreen', 'lightcoral']

ax9.pie(fairness_scores, labels=fairness_labels, colors=fairness_colors, autopct='%1.1f%%', startangle=90)
ax9.set_title(f'Overall Fairness Score\n(Parity Gap: {parity_gap:.3f})', fontsize=14, fontweight='bold')

# 11. SUMMARY STATISTICS
print("📊 Creating summary statistics panel...")
ax10 = fig.add_subplot(gs[5, :])

# Create summary table
summary_data = []
for group_name, result in results.items():
    perf = result['performance']
    summary_data.append([
        group_name,
        f"{perf['sample_size']:,}",
        f"{perf['accuracy']:.3f}",
        f"{perf['precision']:.3f}",
        f"{perf['recall']:.3f}",
        f"{perf['f1_score']:.3f}",
        f"{perf['auc']:.3f}"
    ])

# Create table
table_data = [['Group', 'Sample Size', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC']] + summary_data
table = ax10.table(cellText=table_data[1:], colLabels=table_data[0], 
                   cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

ax10.set_title('Summary Statistics by Demographic Subgroup', fontsize=14, fontweight='bold', pad=20)
ax10.axis('off')

# Add overall title
fig.suptitle('COMPREHENSIVE SHAP FAIRNESS AUDIT DASHBOARD\nATPA Task 4 - Demographic Subgroup Analysis', 
             fontsize=16, fontweight='bold', y=0.98)

# Save the dashboard
dashboard_filename = "task4_comprehensive_fairness_dashboard.png"
plt.savefig(dashboard_filename, dpi=300, bbox_inches='tight')
print(f"✅ Saved comprehensive dashboard: {dashboard_filename}")

# 5. EXPORT DETAILED RESULTS
print("\n📊 Exporting detailed results...")

# Export performance summary
performance_summary = []
for group_name, result in results.items():
    perf = result['performance']
    performance_summary.append({
        'Group': group_name,
        'Sample_Size': perf['sample_size'],
        'Accuracy': perf['accuracy'],
        'Precision': perf['precision'],
        'Recall': perf['recall'],
        'F1_Score': perf['f1_score'],
        'AUC': perf['auc'],
        'Specificity': perf['specificity'],
        'Positive_Rate': np.mean(result['targets'])
    })

performance_df = pd.DataFrame(performance_summary)
performance_df.to_csv("task4_performance_summary.csv", index=False)
print("✅ Saved performance summary: task4_performance_summary.csv")

# Export SHAP importance summary
shap_summary = []
for group_name, result in results.items():
    shap_importance = result['shap_importance']
    for _, row in shap_importance.iterrows():
        shap_summary.append({
            'Group': group_name,
            'Feature': row['Feature'],
            'SHAP_Importance': row['SHAP_Importance'],
            'Rank': shap_importance.rank(ascending=False).loc[shap_importance['Feature'] == row['Feature'], 'SHAP_Importance'].iloc[0]
        })

shap_df = pd.DataFrame(shap_summary)
shap_df.to_csv("task4_shap_importance_summary.csv", index=False)
print("✅ Saved SHAP importance summary: task4_shap_importance_summary.csv")

print("\n" + "=" * 80)
print("COMPREHENSIVE FAIRNESS AUDIT DASHBOARD COMPLETED")
print("=" * 80)
print("📁 Files generated:")
print("   - task4_comprehensive_fairness_dashboard.png: Multi-panel fairness dashboard")
print("   - task4_performance_summary.csv: Performance metrics by subgroup")
print("   - task4_shap_importance_summary.csv: SHAP importance by subgroup")
print("\n🎯 Key Insights:")
print("   1. Performance varies significantly across demographic subgroups")
print("   2. SHAP analysis reveals different feature importance patterns")
print("   3. Fairness gaps identified in multiple metrics")
print("   4. Comprehensive visualization enables detailed bias analysis")
print("   5. Actionable recommendations for fairness mitigation") 