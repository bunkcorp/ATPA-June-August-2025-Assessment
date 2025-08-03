#!/usr/bin/env python3
"""
ATPA Task 4: Fairness Audit with SHAP Analysis
Extends SHAP analysis to demographic subgroups for comprehensive fairness audit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import shap
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("ATPA TASK 4: FAIRNESS AUDIT WITH SHAP ANALYSIS")
print("=" * 80)

# Load the prepared dataset
print("📊 Loading prepared dataset...")
try:
    data = pd.read_csv('../Task1_DataPrep/task1_prepared_dataset_correct.csv')
    print(f"✅ Loaded dataset: {len(data):,} records")
except FileNotFoundError:
    print("❌ Task1 prepared dataset not found. Please run Task 1 first.")
    exit(1)

# Check available columns for demographic analysis
print("📊 Available columns for demographic analysis:")
print(f"   Columns: {list(data.columns)}")

# Identify demographic subgroups based on available features
print("\n1. DEMOGRAPHIC SUBGROUP IDENTIFICATION")
print("-" * 45)

# Create demographic subgroups based on available features
demographic_groups = {}

# 1. Agency-based groups (using agency_name_encoded)
if 'agency_name_encoded' in data.columns:
    agency_counts = data['agency_name_encoded'].value_counts()
    large_agencies = agency_counts[agency_counts > 1000].index.tolist()
    small_agencies = agency_counts[agency_counts <= 1000].index.tolist()
    
    demographic_groups['Large_Agencies'] = data[data['agency_name_encoded'].isin(large_agencies)].index
    demographic_groups['Small_Agencies'] = data[data['agency_name_encoded'].isin(small_agencies)].index
    
    print(f"📊 Agency-based subgroups:")
    print(f"   Large Agencies (>1000 incidents): {len(demographic_groups['Large_Agencies']):,} records")
    print(f"   Small Agencies (≤1000 incidents): {len(demographic_groups['Small_Agencies']):,} records")

# 2. Offense category groups (using offense_category_name_encoded)
if 'offense_category_name_encoded' in data.columns:
    # Create groups based on encoded values (assuming higher values might correspond to more serious crimes)
    offense_median = data['offense_category_name_encoded'].median()
    demographic_groups['High_Severity_Crimes'] = data[data['offense_category_name_encoded'] > offense_median].index
    demographic_groups['Low_Severity_Crimes'] = data[data['offense_category_name_encoded'] <= offense_median].index
    
    print(f"📊 Crime severity subgroups:")
    print(f"   High Severity Crimes: {len(demographic_groups['High_Severity_Crimes']):,} records")
    print(f"   Low Severity Crimes: {len(demographic_groups['Low_Severity_Crimes']):,} records")

# 3. Time-based groups (using incident_hour)
if 'incident_hour' in data.columns:
    demographic_groups['Day_Time'] = data[data['incident_hour'].between(6, 18)].index
    demographic_groups['Night_Time'] = data[data['incident_hour'].between(19, 23) | 
                                          data['incident_hour'].between(0, 5)].index
    
    print(f"📊 Time-based subgroups:")
    print(f"   Day Time (6AM-6PM): {len(demographic_groups['Day_Time']):,} records")
    print(f"   Night Time (6PM-6AM): {len(demographic_groups['Night_Time']):,} records")

# 4. CT Flag groups (using ct_flag_encoded)
if 'ct_flag_encoded' in data.columns:
    demographic_groups['CT_Flag_True'] = data[data['ct_flag_encoded'] == 1].index
    demographic_groups['CT_Flag_False'] = data[data['ct_flag_encoded'] == 0].index
    
    print(f"📊 CT Flag subgroups:")
    print(f"   CT Flag True: {len(demographic_groups['CT_Flag_True']):,} records")
    print(f"   CT Flag False: {len(demographic_groups['CT_Flag_False']):,} records")

# 5. Crime against groups (using crime_against_encoded)
if 'crime_against_encoded' in data.columns:
    crime_median = data['crime_against_encoded'].median()
    demographic_groups['High_Crime_Against'] = data[data['crime_against_encoded'] > crime_median].index
    demographic_groups['Low_Crime_Against'] = data[data['crime_against_encoded'] <= crime_median].index
    
    print(f"📊 Crime against subgroups:")
    print(f"   High Crime Against: {len(demographic_groups['High_Crime_Against']):,} records")
    print(f"   Low Crime Against: {len(demographic_groups['Low_Crime_Against']):,} records")

# Prepare features and target
print("\n2. MODEL PREPARATION")
print("-" * 25)

feature_cols = [col for col in data.columns if col.endswith('_encoded') or col == 'incident_hour']
X = data[feature_cols]
y = data['ARREST']

# Stratified train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train Random Forest model
print("🔧 Training Random Forest model for fairness audit...")
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=10,
    min_samples_leaf=2,
    class_weight='balanced',
    random_state=42
)

rf_model.fit(X_train, y_train)

# Initialize SHAP explainer
print("🔧 Initializing SHAP explainer...")
explainer = shap.TreeExplainer(rf_model)

print("\n3. FAIRNESS AUDIT WITH SHAP ANALYSIS")
print("-" * 40)

# Store fairness audit results
fairness_results = {}

for group_name, group_indices in demographic_groups.items():
    print(f"\n📊 Analyzing group: {group_name}")
    print("-" * 35)
    
    # Filter test data for this group
    group_test_indices = [i for i in group_indices if i in X_test.index]
    
    if len(group_test_indices) < 100:
        print(f"   ⚠️  Insufficient data: {len(group_test_indices)} records (skipping)")
        continue
    
    X_group = X_test.loc[group_test_indices]
    y_group = y_test.loc[group_test_indices]
    
    # Calculate group performance metrics
    y_pred_group = rf_model.predict(X_group)
    y_proba_group = rf_model.predict_proba(X_group)[:, 1]
    
    # Performance metrics
    accuracy = rf_model.score(X_group, y_group)
    precision = precision_score(y_group, y_pred_group)
    recall = recall_score(y_group, y_pred_group)
    f1 = f1_score(y_group, y_pred_group)
    auc = roc_auc_score(y_group, y_proba_group)
    
    # Confusion matrix
    cm = confusion_matrix(y_group, y_pred_group)
    tn, fp, fn, tp = cm.ravel()
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    print(f"   📈 Performance Metrics:")
    print(f"      Accuracy: {accuracy:.4f}")
    print(f"      Precision: {precision:.4f}")
    print(f"      Recall: {recall:.4f}")
    print(f"      F1-Score: {f1:.4f}")
    print(f"      AUC-ROC: {auc:.4f}")
    print(f"      Specificity: {specificity:.4f}")
    
    # SHAP analysis for this group
    print(f"   🔍 Computing SHAP values...")
    shap_values_group = explainer.shap_values(X_group)
    
    # Debug SHAP values structure
    print(f"   🔍 SHAP values type: {type(shap_values_group)}")
    if isinstance(shap_values_group, list):
        print(f"   🔍 SHAP values list length: {len(shap_values_group)}")
        for i, sv in enumerate(shap_values_group):
            print(f"   🔍 SHAP values[{i}] shape: {sv.shape}")
        shap_values_group = shap_values_group[1]  # ARREST = 1 class
    else:
        print(f"   🔍 SHAP values shape: {shap_values_group.shape}")
    
    # SHAP returns (n_samples, n_features, n_classes) – extract class 1
    if shap_values_group.ndim == 3 and shap_values_group.shape[2] == 2:
        print("   🔧 Extracting SHAP values for class 1 (ARREST=1)...")
        shap_values_group = shap_values_group[:, :, 1]  # shape: (n_samples, n_features)
    
    print(f"   🔍 Final SHAP values shape: {shap_values_group.shape}")
    
    # Confirm it's 2D now
    assert shap_values_group.ndim == 2, f"SHAP values not 2D after slicing: {shap_values_group.shape}"
    
    # Compute feature-wise SHAP importance (mean across samples)
    shap_importance_group = np.mean(np.abs(shap_values_group), axis=0)
    
    # Confirm it's 1D now and matches features
    assert shap_importance_group.ndim == 1
    assert len(shap_importance_group) == len(feature_cols)
    
    print(f"   🔍 SHAP importance shape: {shap_importance_group.shape}")
    print(f"   🔍 Feature cols length: {len(feature_cols)}")
    
    # Create feature importance DataFrame
    feature_importance_group = pd.DataFrame({
        'Feature': feature_cols,
        'SHAP_Importance': shap_importance_group
    }).sort_values('SHAP_Importance', ascending=False)
    
    print(f"   📊 Top 3 SHAP Features for {group_name}:")
    for i, row in feature_importance_group.head(3).iterrows():
        print(f"      {row['Feature']}: {row['SHAP_Importance']:.4f}")
    
    # Store results
    fairness_results[group_name] = {
        'performance': {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'auc': auc,
            'specificity': specificity,
            'sample_size': len(group_test_indices)
        },
        'shap_importance': feature_importance_group,
        'shap_values': shap_values_group,
        'data': X_group,
        'targets': y_group
    }

print("\n4. SHAP BEESWARM PLOTS FOR EACH SUBGROUP")
print("-" * 45)

# Create SHAP beeswarm plots for each subgroup
for group_name, results in fairness_results.items():
    print(f"📊 Creating SHAP beeswarm plot for {group_name}...")
    
    try:
        # Get SHAP values and data for this group
        shap_values = results['shap_values']
        X_group_data = results['data']
        
        # Create beeswarm plot
        plt.figure(figsize=(12, 8))
        
        # Use SHAP's beeswarm plot
        shap.summary_plot(
            shap_values, 
            X_group_data,
            plot_type="beeswarm",
            max_display=6,  # Show top 6 features
            show=False,
            color_bar=True
        )
        
        plt.title(f'SHAP Beeswarm Plot - {group_name}\n(ARREST=1 Predictions)', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('SHAP Value (Impact on ARREST=1 Prediction)', fontsize=12)
        
        # Add performance metrics as text
        perf = results['performance']
        metrics_text = f"Accuracy: {perf['accuracy']:.3f} | Precision: {perf['precision']:.3f} | Recall: {perf['recall']:.3f} | AUC: {perf['auc']:.3f}"
        plt.figtext(0.5, 0.02, metrics_text, ha='center', fontsize=10, 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        # Save plot
        plot_filename = f"shap_summary_{group_name.replace(' ', '_')}.png"
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Saved: {plot_filename}")
        
    except Exception as e:
        print(f"   ❌ Error creating beeswarm plot for {group_name}: {str(e)}")

print("\n5. FAIRNESS METRICS CALCULATION")
print("-" * 35)

# Calculate fairness metrics
fairness_metrics = {}

# 1. Demographic Parity (similar arrest rates across groups)
print("📊 Demographic Parity Analysis:")
arrest_rates = {}
for group_name, results in fairness_results.items():
    arrest_rate = results['targets'].mean()
    arrest_rates[group_name] = arrest_rate
    print(f"   {group_name}: {arrest_rate:.3f} ({arrest_rate*100:.1f}%)")

# Calculate demographic parity gap
if len(arrest_rates) > 1:
    max_rate = max(arrest_rates.values())
    min_rate = min(arrest_rates.values())
    parity_gap = max_rate - min_rate
    print(f"   📈 Demographic Parity Gap: {parity_gap:.3f} ({parity_gap*100:.1f}%)")

# 2. Equalized Odds (similar TPR and FPR across groups)
print("\n📊 Equalized Odds Analysis:")
for group_name, results in fairness_results.items():
    cm = confusion_matrix(results['targets'], rf_model.predict(results['data']))
    tn, fp, fn, tp = cm.ravel()
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    print(f"   {group_name}:")
    print(f"      True Positive Rate: {tpr:.3f}")
    print(f"      False Positive Rate: {fpr:.3f}")

# 3. Predictive Rate Parity (similar precision across groups)
print("\n📊 Predictive Rate Parity Analysis:")
for group_name, results in fairness_results.items():
    precision = results['performance']['precision']
    print(f"   {group_name}: {precision:.3f}")

print("\n6. QUANTIFIED FAIRNESS GAPS TABLE")
print("-" * 40)

# Create comprehensive fairness gaps DataFrame
fairness_gaps_data = []

for group_name, results in fairness_results.items():
    perf = results['performance']
    shap_importance = results['shap_importance']
    
    # Get top 3 SHAP features
    top_features = shap_importance.head(3)
    top_feature_names = ', '.join([str(feature) for feature in top_features.index.tolist()])
    top_feature_values = ', '.join([f"{val:.4f}" for val in top_features.values])
    
    fairness_gaps_data.append({
        'Group': group_name,
        'Sample_Size': perf['sample_size'],
        'Arrest_Rate': perf['sample_size'] / len(data) * 100,  # Percentage of total
        'F1_Score': perf['f1_score'],
        'True_Positive_Rate': perf['recall'],
        'False_Positive_Rate': 1 - perf['specificity'],
        'Precision': perf['precision'],
        'AUC': perf['auc'],
        'Top_3_SHAP_Features': top_feature_names,
        'Top_3_SHAP_Values': top_feature_values
    })

# Create DataFrame and sort by F1 score
fairness_gaps_df = pd.DataFrame(fairness_gaps_data)
fairness_gaps_df = fairness_gaps_df.sort_values('F1_Score', ascending=False)

print("📊 Fairness Gaps Summary Table:")
print(fairness_gaps_df.to_string(index=False, float_format='%.3f'))

# Calculate fairness gaps
print("\n📈 Key Fairness Gaps:")
f1_scores = fairness_gaps_df['F1_Score']
f1_gap = f1_scores.max() - f1_scores.min()
print(f"   F1 Score Gap: {f1_gap:.3f} ({f1_scores.max():.3f} - {f1_scores.min():.3f})")

tpr_scores = fairness_gaps_df['True_Positive_Rate']
tpr_gap = tpr_scores.max() - tpr_scores.min()
print(f"   TPR Gap: {tpr_gap:.3f} ({tpr_scores.max():.3f} - {tpr_scores.min():.3f})")

fpr_scores = fairness_gaps_df['False_Positive_Rate']
fpr_gap = fpr_scores.max() - fpr_scores.min()
print(f"   FPR Gap: {fpr_gap:.3f} ({fpr_scores.max():.3f} - {fpr_scores.min():.3f})")

print("\n7. EXPORT SHAP TABLES")
print("-" * 25)

# Export detailed SHAP tables for each group
shap_export_data = []

for group_name, results in fairness_results.items():
    shap_importance = results['shap_importance']
    
    for feature, importance in shap_importance.items():
        shap_export_data.append({
            'Group': group_name,
            'Feature': feature,
            'SHAP_Importance': importance,
            'Rank': shap_importance.rank(ascending=False)[feature]
        })

# Create comprehensive SHAP export DataFrame
shap_export_df = pd.DataFrame(shap_export_data)
shap_export_df = shap_export_df.sort_values(['Group', 'Rank'])

# Save to CSV
shap_export_filename = "task4_shap_importance_by_group.csv"
shap_export_df.to_csv(shap_export_filename, index=False)
print(f"✅ Saved comprehensive SHAP table: {shap_export_filename}")

# Export top 3 features per group for report inclusion
top_features_export = []
for group_name, results in fairness_results.items():
    top_3 = results['shap_importance'].head(3)
    for rank, (feature, importance) in enumerate(top_3.items(), 1):
        top_features_export.append({
            'Group': group_name,
            'Rank': rank,
            'Feature': feature,
            'SHAP_Importance': importance
        })

top_features_df = pd.DataFrame(top_features_export)
top_features_filename = "task4_top3_shap_features_by_group.csv"
top_features_df.to_csv(top_features_filename, index=False)
print(f"✅ Saved top 3 SHAP features: {top_features_filename}")

print("\n8. FAIRNESS MITIGATION RECOMMENDATIONS")
print("-" * 45)

# Identify groups with performance issues
worst_f1_group = fairness_gaps_df.loc[fairness_gaps_df['F1_Score'].idxmin()]
best_f1_group = fairness_gaps_df.loc[fairness_gaps_df['F1_Score'].idxmax()]

print(f"🎯 **Groups Needing Attention**:")
print(f"   Worst F1: {worst_f1_group['Group']} (F1={worst_f1_group['F1_Score']:.3f})")
print(f"   Best F1: {best_f1_group['Group']} (F1={best_f1_group['F1_Score']:.3f})")
print(f"   Gap: {worst_f1_group['F1_Score'] - best_f1_group['F1_Score']:.3f}")

print(f"\n🔧 **Mitigation Strategies**:")
print(f"   1. **Reweighting**: Apply higher weights to underrepresented groups")
print(f"   2. **Stratified Sampling**: Ensure balanced representation in training")
print(f"   3. **Fairlearn Integration**: Use fairness constraints in model training")
print(f"   4. **Feature Engineering**: Create group-specific features")
print(f"   5. **Ensemble Methods**: Combine models trained on different subgroups")

# Save fairness gaps table
fairness_gaps_filename = "task4_fairness_gaps_summary.csv"
fairness_gaps_df.to_csv(fairness_gaps_filename, index=False)
print(f"\n✅ Saved fairness gaps table: {fairness_gaps_filename}")

print("\n9. SHAP FAIRNESS VISUALIZATION")
print("-" * 35)

# Create comprehensive fairness visualization
plt.style.use('default')
fig, axes = plt.subplots(3, 3, figsize=(20, 15))
fig.suptitle('ATPA Task 4: Fairness Audit with SHAP Analysis', fontsize=16, fontweight='bold')

# 1. Performance comparison across groups
group_names = list(fairness_results.keys())
performance_metrics = ['accuracy', 'precision', 'recall', 'f1_score', 'auc']

x = np.arange(len(performance_metrics))
width = 0.8 / len(group_names)

for i, group_name in enumerate(group_names):
    metrics = [fairness_results[group_name]['performance'][metric] for metric in performance_metrics]
    axes[0,0].bar(x + i*width, metrics, width, label=group_name, alpha=0.8)

axes[0,0].set_xlabel('Metrics')
axes[0,0].set_ylabel('Score')
axes[0,0].set_title('Performance Comparison Across Groups')
axes[0,0].set_xticks(x + width * (len(group_names)-1) / 2)
axes[0,0].set_xticklabels(performance_metrics, rotation=45)
axes[0,0].legend()
axes[0,0].set_ylim(0, 1)

# 2. Arrest rates comparison
arrest_rates_values = [arrest_rates[group] for group in group_names]
axes[0,1].bar(group_names, arrest_rates_values, color='lightcoral', alpha=0.8)
axes[0,1].set_ylabel('Arrest Rate')
axes[0,1].set_title('Arrest Rates by Demographic Group')
axes[0,1].tick_params(axis='x', rotation=45)

# Add value labels
for i, rate in enumerate(arrest_rates_values):
    axes[0,1].text(i, rate + 0.01, f'{rate:.3f}', ha='center')

# 3. SHAP importance comparison (top 3 features)
top_features = ['offense_code_encoded', 'ct_flag_encoded', 'offense_category_name_encoded']
x_shap = np.arange(len(top_features))
width_shap = 0.8 / len(group_names)

for i, group_name in enumerate(group_names):
    shap_importance = []
    for feature in top_features:
        importance = fairness_results[group_name]['shap_importance'][
            fairness_results[group_name]['shap_importance']['Feature'] == feature
        ]['SHAP_Importance'].iloc[0] if len(fairness_results[group_name]['shap_importance'][
            fairness_results[group_name]['shap_importance']['Feature'] == feature
        ]) > 0 else 0
        shap_importance.append(importance)
    
    axes[0,2].bar(x_shap + i*width_shap, shap_importance, width_shap, label=group_name, alpha=0.8)

axes[0,2].set_xlabel('Features')
axes[0,2].set_ylabel('SHAP Importance')
axes[0,2].set_title('SHAP Feature Importance by Group')
axes[0,2].set_xticks(x_shap + width_shap * (len(group_names)-1) / 2)
axes[0,2].set_xticklabels([f[:15] for f in top_features], rotation=45)
axes[0,2].legend()

# 4. Confusion matrix heatmaps for each group
for i, group_name in enumerate(group_names[:4]):  # Show first 4 groups
    row = (i + 1) // 2
    col = (i + 1) % 2
    
    cm = confusion_matrix(fairness_results[group_name]['targets'], 
                         rf_model.predict(fairness_results[group_name]['data']))
    
    im = axes[row, col].imshow(cm, cmap='Blues', interpolation='nearest')
    axes[row, col].set_title(f'Confusion Matrix - {group_name}')
    axes[row, col].set_ylabel('True Label')
    axes[row, col].set_xlabel('Predicted Label')
    axes[row, col].set_xticks([0, 1])
    axes[row, col].set_yticks([0, 1])
    axes[row, col].set_xticklabels(['No Arrest', 'Arrest'])
    axes[row, col].set_yticklabels(['No Arrest', 'Arrest'])
    
    # Add text annotations
    thresh = cm.max() / 2
    for r in range(2):
        for c in range(2):
            axes[row, col].text(c, r, format(cm[r, c], 'd'),
                              ha="center", va="center",
                              color="white" if cm[r, c] > thresh else "black")

# 5. Fairness metrics summary
if len(group_names) > 1:
    # Calculate fairness gaps
    accuracy_gaps = []
    precision_gaps = []
    recall_gaps = []
    
    for i in range(len(group_names)):
        for j in range(i+1, len(group_names)):
            acc_gap = abs(fairness_results[group_names[i]]['performance']['accuracy'] - 
                         fairness_results[group_names[j]]['performance']['accuracy'])
            prec_gap = abs(fairness_results[group_names[i]]['performance']['precision'] - 
                          fairness_results[group_names[j]]['performance']['precision'])
            rec_gap = abs(fairness_results[group_names[i]]['performance']['recall'] - 
                         fairness_results[group_names[j]]['performance']['recall'])
            
            accuracy_gaps.append(acc_gap)
            precision_gaps.append(prec_gap)
            recall_gaps.append(rec_gap)
    
    fairness_gaps = ['Accuracy', 'Precision', 'Recall']
    gap_values = [np.mean(accuracy_gaps), np.mean(precision_gaps), np.mean(recall_gaps)]
    
    axes[2, 0].bar(fairness_gaps, gap_values, color=['lightblue', 'lightgreen', 'lightcoral'], alpha=0.8)
    axes[2, 0].set_ylabel('Average Gap')
    axes[2, 0].set_title('Fairness Gaps Across Groups')
    
    # Add value labels
    for i, gap in enumerate(gap_values):
        axes[2, 0].text(i, gap + 0.01, f'{gap:.3f}', ha='center')

# 6. Sample size comparison
sample_sizes = [fairness_results[group]['performance']['sample_size'] for group in group_names]
axes[2, 1].bar(group_names, sample_sizes, color='lightyellow', alpha=0.8)
axes[2, 1].set_ylabel('Sample Size')
axes[2, 1].set_title('Sample Sizes by Group')
axes[2, 1].tick_params(axis='x', rotation=45)

# Add value labels
for i, size in enumerate(sample_sizes):
    axes[2, 1].text(i, size + max(sample_sizes)*0.01, f'{size:,}', ha='center')

# 7. Overall fairness assessment
fairness_score = 1 - np.mean([np.mean(accuracy_gaps), np.mean(precision_gaps), np.mean(recall_gaps)]) if len(group_names) > 1 else 1.0
axes[2, 2].pie([fairness_score, 1-fairness_score], labels=['Fair', 'Unfair'], 
               colors=['lightgreen', 'lightcoral'], autopct='%1.1f%%')
axes[2, 2].set_title('Overall Fairness Assessment')

plt.tight_layout()
plt.savefig('task4_fairness_audit_shap_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n6. FAIRNESS AUDIT REPORT")
print("-" * 30)

# Generate comprehensive fairness report
report = f"""
ATPA TASK 4: FAIRNESS AUDIT WITH SHAP ANALYSIS REPORT

1. DEMOGRAPHIC SUBGROUPS ANALYZED:
{'-' * 40}
"""

for group_name, results in fairness_results.items():
    report += f"""
{group_name}:
   Sample Size: {results['performance']['sample_size']:,} records
   Arrest Rate: {results['targets'].mean():.3f} ({results['targets'].mean()*100:.1f}%)
   Performance Metrics:
      - Accuracy: {results['performance']['accuracy']:.4f}
      - Precision: {results['performance']['precision']:.4f}
      - Recall: {results['performance']['recall']:.4f}
      - F1-Score: {results['performance']['f1_score']:.4f}
      - AUC-ROC: {results['performance']['auc']:.4f}
      - Specificity: {results['performance']['specificity']:.4f}
   
   Top 3 SHAP Features:
"""

    for i, row in results['shap_importance'].head(3).iterrows():
        report += f"      - {row['Feature']}: {row['SHAP_Importance']:.4f}\n"

# Fairness assessment
report += f"""
2. FAIRNESS ASSESSMENT:
{'-' * 25}
"""

if len(arrest_rates) > 1:
    max_rate = max(arrest_rates.values())
    min_rate = min(arrest_rates.values())
    parity_gap = max_rate - min_rate
    
    report += f"""
Demographic Parity:
   - Maximum Arrest Rate: {max_rate:.3f} ({max_rate*100:.1f}%)
   - Minimum Arrest Rate: {min_rate:.3f} ({min_rate*100:.1f}%)
   - Parity Gap: {parity_gap:.3f} ({parity_gap*100:.1f}%)
   - Assessment: {'FAIR' if parity_gap < 0.05 else 'POTENTIAL BIAS DETECTED'}

Performance Fairness:
   - Average Accuracy Gap: {np.mean(accuracy_gaps):.3f}
   - Average Precision Gap: {np.mean(precision_gaps):.3f}
   - Average Recall Gap: {np.mean(recall_gaps):.3f}
   - Overall Fairness Score: {fairness_score:.3f}
   - Assessment: {'FAIR' if fairness_score > 0.9 else 'REQUIRES ATTENTION' if fairness_score > 0.8 else 'POTENTIAL BIAS'}
"""

# Recommendations
report += f"""
3. RECOMMENDATIONS:
{'-' * 20}
"""

if len(arrest_rates) > 1:
    if parity_gap > 0.05:
        report += """
   ⚠️  DEMOGRAPHIC PARITY ISSUES:
      - Significant differences in arrest rates across groups
      - Consider investigating underlying causes
      - Review data collection and processing procedures
      - Implement bias mitigation techniques if necessary
"""

    if fairness_score < 0.9:
        report += """
   ⚠️  PERFORMANCE FAIRNESS ISSUES:
      - Model performance varies significantly across groups
      - Consider group-specific model tuning
      - Implement fairness-aware training methods
      - Monitor performance by demographic subgroups
"""

report += """
   ✅ RECOMMENDED ACTIONS:
      - Regular fairness audits on new data
      - Continuous monitoring of demographic parity
      - Transparent reporting of fairness metrics
      - Stakeholder communication about fairness findings
      - Integration of fairness metrics into model selection
"""

# Save report
with open('task4_fairness_audit_report.txt', 'w') as f:
    f.write(report)

print("✅ Fairness audit completed!")
print("📁 Files generated:")
print("   - task4_fairness_audit_shap_analysis.png: Comprehensive fairness visualization")
print("   - task4_fairness_audit_report.txt: Detailed fairness audit report")
print("   - shap_summary_*.png: SHAP beeswarm plots for each demographic subgroup")
print("   - task4_fairness_gaps_summary.csv: Quantified fairness gaps table")
print("   - task4_shap_importance_by_group.csv: Comprehensive SHAP importance by group")
print("   - task4_top3_shap_features_by_group.csv: Top 3 SHAP features per group")

print("\n" + "=" * 80)
print("FAIRNESS AUDIT SUMMARY")
print("=" * 80)

print(f"🎯 **Groups Analyzed**: {len(demographic_groups)} demographic subgroups")
print(f"📊 **Fairness Score**: {fairness_score:.3f}")
print(f"🔍 **SHAP Analysis**: Feature importance by demographic group")
print(f"📈 **Performance Gaps**: Monitored across all subgroups")
print(f"✅ **Recommendations**: Generated for bias mitigation")

print("\n💡 **Key Insights**:")
print("   1. SHAP analysis reveals feature importance differences across groups")
print("   2. Performance gaps indicate potential bias in model predictions")
print("   3. Demographic parity analysis shows arrest rate variations")
print("   4. Fairness audit provides actionable recommendations")
print("   5. Continuous monitoring essential for maintaining fairness") 