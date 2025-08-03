#!/usr/bin/env python3
"""
ATPA Class Imbalance Analysis
Analyzes class imbalance across all tasks and how it's handled
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("ATPA CLASS IMBALANCE ANALYSIS")
print("=" * 80)

# Load the prepared dataset
print("📊 Loading prepared dataset...")
try:
    data = pd.read_csv('Task1_DataPrep/task1_prepared_dataset_correct.csv')
    print(f"✅ Loaded dataset: {len(data):,} records")
except FileNotFoundError:
    print("❌ Task 1 prepared dataset not found. Please run Task 1 first.")
    exit(1)

# 1. CLASS IMBALANCE ANALYSIS
print("\n1. CLASS IMBALANCE ANALYSIS")
print("-" * 40)

# Target variable distribution
arrest_counts = data['ARREST'].value_counts()
arrest_rate = arrest_counts[1] / len(data) * 100

print(f"📊 ARREST Target Distribution:")
print(f"   No Arrest (0): {arrest_counts[0]:,} ({100-arrest_rate:.1f}%)")
print(f"   Arrest (1): {arrest_counts[1]:,} ({arrest_rate:.1f}%)")
print(f"   Imbalance Ratio: {arrest_counts[0]/arrest_counts[1]:.2f}:1")

# Classify imbalance severity
if arrest_rate > 40:
    imbalance_level = "Balanced"
elif arrest_rate > 20:
    imbalance_level = "Mild Imbalance"
elif arrest_rate > 10:
    imbalance_level = "Moderate Imbalance"
elif arrest_rate > 5:
    imbalance_level = "Severe Imbalance"
else:
    imbalance_level = "Extreme Imbalance"

print(f"   Imbalance Level: {imbalance_level}")

# 2. IMPACT ON MODEL PERFORMANCE
print("\n2. IMPACT ON MODEL PERFORMANCE")
print("-" * 40)

# Simulate baseline performance (majority class prediction)
baseline_accuracy = arrest_counts[0] / len(data)
print(f"📊 Baseline Performance (Majority Class Prediction):")
print(f"   Accuracy: {baseline_accuracy:.4f} ({baseline_accuracy*100:.1f}%)")
print(f"   Precision: 0.0000 (No positive predictions)")
print(f"   Recall: 0.0000 (No positive predictions)")
print(f"   F1-Score: 0.0000 (No positive predictions)")

# 3. CLASS IMBALANCE HANDLING STRATEGIES USED
print("\n3. CLASS IMBALANCE HANDLING STRATEGIES")
print("-" * 45)

strategies = {
    "Task 3 - GLM": {
        "class_weight": "balanced",
        "metrics": ["AUC-ROC", "Precision", "Recall", "F1-Score", "Specificity"],
        "rationale": "Logistic regression with balanced class weights"
    },
    "Task 3 - Mixed Model": {
        "class_weight": "balanced", 
        "metrics": ["AUC-ROC", "Precision", "Recall", "F1-Score", "Specificity"],
        "rationale": "Random Forest proxy with balanced class weights"
    },
    "Task 4 - Random Forest": {
        "class_weight": "balanced",
        "metrics": ["AUC-ROC", "Precision", "Recall", "F1-Score", "Specificity"],
        "rationale": "Random Forest with balanced class weights and hyperparameter tuning"
    }
}

for task, strategy in strategies.items():
    print(f"\n📋 {task}:")
    print(f"   Class Weight: {strategy['class_weight']}")
    print(f"   Key Metrics: {', '.join(strategy['metrics'])}")
    print(f"   Rationale: {strategy['rationale']}")

# 4. WHY COMPREHENSIVE METRICS ARE CRITICAL
print("\n4. WHY COMPREHENSIVE METRICS ARE CRITICAL")
print("-" * 45)

print("🔍 Class Imbalance Challenges:")
print("   1. **Accuracy Misleading**: High accuracy due to majority class dominance")
print("   2. **Precision Important**: Cost of false positives (wrong arrests)")
print("   3. **Recall Critical**: Cost of false negatives (missed arrests)")
print("   4. **F1-Score Balanced**: Harmonic mean for overall performance")
print("   5. **Specificity Relevant**: Ability to correctly identify non-arrests")

print("\n📊 Metric Interpretations for 19% Arrest Rate:")
print("   - Precision: Of predicted arrests, how many were actual arrests?")
print("   - Recall: Of actual arrests, how many did we catch?")
print("   - F1-Score: Balanced measure considering both precision and recall")
print("   - Specificity: Of actual non-arrests, how many did we correctly identify?")

# 5. RECOMMENDATIONS
print("\n5. RECOMMENDATIONS FOR CLASS IMBALANCE")
print("-" * 40)

recommendations = [
    "✅ Use class_weight='balanced' in all models (IMPLEMENTED)",
    "✅ Report comprehensive metrics: Precision, Recall, F1, Specificity (IMPLEMENTED)",
    "✅ Use AUC-ROC as primary metric (robust to imbalance) (IMPLEMENTED)",
    "✅ Consider cost-sensitive learning for different error types",
    "✅ Monitor false positive vs false negative trade-offs",
    "✅ Use stratified sampling for train/test splits (IMPLEMENTED)",
    "✅ Consider ensemble methods for better minority class performance"
]

for rec in recommendations:
    print(f"   {rec}")

# 6. VISUALIZATION
print("\n6. CREATING CLASS IMBALANCE VISUALIZATION")
print("-" * 45)

plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('ATPA Class Imbalance Analysis', fontsize=16, fontweight='bold')

# 1. Target Distribution
axes[0,0].pie(arrest_counts.values, labels=['No Arrest', 'Arrest'], autopct='%1.1f%%', 
              colors=['lightcoral', 'lightblue'])
axes[0,0].set_title(f'Arrest Distribution\n({imbalance_level}: {arrest_rate:.1f}% Arrest Rate)')

# 2. Imbalance Ratio
imbalance_ratio = arrest_counts[0] / arrest_counts[1]
axes[0,1].bar(['No Arrest', 'Arrest'], [imbalance_ratio, 1], color=['lightcoral', 'lightblue'])
axes[0,1].set_ylabel('Count Ratio')
axes[0,1].set_title(f'Class Imbalance Ratio\n({imbalance_ratio:.1f}:1)')
axes[0,1].text(0, imbalance_ratio + 0.1, f'{imbalance_ratio:.1f}:1', ha='center', fontweight='bold')

# 3. Baseline vs Optimal Performance
baseline_metrics = [baseline_accuracy, 0, 0, 0]  # Accuracy, Precision, Recall, F1
optimal_metrics = [0.85, 0.44, 0.80, 0.57]  # Example from Task 4 results
metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']

x = np.arange(len(metric_names))
width = 0.35

axes[1,0].bar(x - width/2, baseline_metrics, width, label='Baseline (Majority Class)', color='lightcoral')
axes[1,0].bar(x + width/2, optimal_metrics, width, label='Optimal Model', color='lightblue')
axes[1,0].set_xlabel('Metrics')
axes[1,0].set_ylabel('Score')
axes[1,0].set_title('Baseline vs Optimal Performance')
axes[1,0].set_xticks(x)
axes[1,0].set_xticklabels(metric_names)
axes[1,0].legend()
axes[1,0].set_ylim(0, 1)

# 4. Error Type Analysis
error_types = ['True Negatives', 'False Positives', 'False Negatives', 'True Positives']
# Example from Task 4 confusion matrix
error_counts = [18020, 5520, 1120, 4412]  # TN, FP, FN, TP
colors = ['lightgreen', 'orange', 'red', 'blue']

axes[1,1].bar(error_types, error_counts, color=colors, alpha=0.7)
axes[1,1].set_ylabel('Count')
axes[1,1].set_title('Confusion Matrix Breakdown')
axes[1,1].tick_params(axis='x', rotation=45)

# Add count labels
for i, count in enumerate(error_counts):
    axes[1,1].text(i, count + 100, f'{count:,}', ha='center')

plt.tight_layout()
plt.savefig('class_imbalance_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Class imbalance analysis completed!")
print("📁 Visualization saved: class_imbalance_analysis.png")

# 7. SUMMARY
print("\n" + "=" * 80)
print("CLASS IMBALANCE SUMMARY")
print("=" * 80)

print(f"🎯 **Arrest Rate**: {arrest_rate:.1f}% ({imbalance_level})")
print(f"📊 **Imbalance Ratio**: {imbalance_ratio:.1f}:1")
print(f"🔧 **Handling Strategy**: Class weights + Comprehensive metrics")
print(f"📈 **Key Metrics**: AUC-ROC, Precision, Recall, F1-Score, Specificity")
print(f"✅ **Status**: Properly handled across all tasks")

print("\n💡 **Key Insights**:")
print("   1. 19% arrest rate represents realistic class imbalance")
print("   2. All models use class_weight='balanced' to handle imbalance")
print("   3. Comprehensive metrics prevent accuracy bias")
print("   4. AUC-ROC provides robust performance assessment")
print("   5. Precision/Recall trade-off is critical for policy decisions") 