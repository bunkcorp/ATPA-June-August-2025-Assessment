#!/usr/bin/env python3
"""
Enhanced Models with Oversampling
ATPA Assessment - June to August 2025

This script implements oversampling techniques to address class imbalance
and improve sensitivity for multiple arrest prediction.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, roc_auc_score, classification_report, 
    confusion_matrix, precision_recall_curve, roc_curve
)
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_prepare_data():
    """Load and prepare the dataset"""
    print("Loading and preparing data...")
    
    # Load the prepared dataset
    try:
        data = pd.read_csv('incidents_with_arrests.csv')
        print(f"Loaded {len(data)} incidents")
    except FileNotFoundError:
        print("Error: incidents_with_arrests.csv not found. Please run Task 1 first.")
        return None, None, None
    
    # Prepare features and target
    feature_cols = [
        'num_arrests', 'num_offenses', 'num_victims', 'num_offenders',
        'weapon_present', 'violent_offense', 'property_offense', 'drug_offense',
        'age_num', 'hc_code', 'resident_code', 'under_18_disposition_code'
    ]
    
    # Ensure all feature columns exist
    missing_cols = [col for col in feature_cols if col not in data.columns]
    if missing_cols:
        print(f"Warning: Missing columns: {missing_cols}")
        feature_cols = [col for col in feature_cols if col in data.columns]
    
    X = data[feature_cols]
    y = data['MULTIPLE_ARRESTS']
    
    # Handle missing values
    print("Handling missing values...")
    print(f"Missing values before: {X.isnull().sum().sum()}")
    
    # For numeric columns, fill with median
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if X[col].isnull().sum() > 0:
            median_val = X[col].median()
            X[col] = X[col].fillna(median_val)
    
    # For categorical columns, fill with mode
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if X[col].isnull().sum() > 0:
            mode_val = X[col].mode().iloc[0] if len(X[col].mode()) > 0 else 'Unknown'
            X[col] = X[col].fillna(mode_val)
    
    print(f"Missing values after: {X.isnull().sum().sum()}")
    
    # Convert categorical variables to numeric
    categorical_cols = ['weapon_name', 'under_18_disposition_code', 'resident_code']
    for col in categorical_cols:
        if col in X.columns:
            X[col] = pd.Categorical(X[col]).codes
    
    print(f"Features: {X.shape[1]}, Target distribution: {y.value_counts().to_dict()}")
    return X, y, feature_cols

def calculate_comprehensive_metrics(y_true, y_pred, y_proba, model_name=""):
    """Calculate comprehensive performance metrics"""
    
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    # Basic metrics
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) > 0 else 0
    
    # AUC
    auc = roc_auc_score(y_true, y_proba)
    
    return {
        'model_name': model_name,
        'accuracy': accuracy,
        'sensitivity': sensitivity,
        'specificity': specificity,
        'precision': precision,
        'f1_score': f1_score,
        'auc': auc,
        'confusion_matrix': cm,
        'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn
    }

def plot_performance_comparison(results_dict):
    """Plot performance comparison across different approaches"""
    
    models = list(results_dict.keys())
    metrics = ['accuracy', 'sensitivity', 'specificity', 'f1_score', 'auc']
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.ravel()
    
    for i, metric in enumerate(metrics):
        values = [results_dict[model][metric] for model in models]
        
        bars = axes[i].bar(models, values, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
        axes[i].set_title(f'{metric.upper()} Comparison')
        axes[i].set_ylabel(metric.upper())
        axes[i].tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            axes[i].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                        f'{value:.3f}', ha='center', va='bottom')
    
    # Confusion matrix comparison
    axes[5].axis('off')
    axes[5].text(0.5, 0.5, 'Confusion Matrices\n(See detailed results below)', 
                ha='center', va='center', fontsize=12, transform=axes[5].transAxes)
    
    plt.tight_layout()
    plt.savefig('enhanced_performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def implement_oversampling_techniques(X_train, y_train, X_test, y_test):
    """Implement various oversampling techniques and compare results"""
    
    print("\n" + "="*60)
    print("IMPLEMENTING OVERSAMPLING TECHNIQUES")
    print("="*60)
    
    results = {}
    
    # 1. Baseline (No oversampling)
    print("\n1. Baseline Model (No Oversampling)")
    baseline_model = RandomForestClassifier(n_estimators=100, random_state=42)
    baseline_model.fit(X_train, y_train)
    
    y_pred_baseline = baseline_model.predict(X_test)
    y_proba_baseline = baseline_model.predict_proba(X_test)[:, 1]
    
    results['Baseline'] = calculate_comprehensive_metrics(
        y_test, y_pred_baseline, y_proba_baseline, "Baseline"
    )
    
    # 2. SMOTE
    print("\n2. SMOTE Oversampling")
    smote = SMOTE(random_state=42, k_neighbors=5)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
    
    smote_model = RandomForestClassifier(n_estimators=100, random_state=42)
    smote_model.fit(X_train_smote, y_train_smote)
    
    y_pred_smote = smote_model.predict(X_test)
    y_proba_smote = smote_model.predict_proba(X_test)[:, 1]
    
    results['SMOTE'] = calculate_comprehensive_metrics(
        y_test, y_pred_smote, y_proba_smote, "SMOTE"
    )
    
    # 3. ADASYN
    print("\n3. ADASYN Oversampling")
    adasyn = ADASYN(random_state=42)
    X_train_adasyn, y_train_adasyn = adasyn.fit_resample(X_train, y_train)
    
    adasyn_model = RandomForestClassifier(n_estimators=100, random_state=42)
    adasyn_model.fit(X_train_adasyn, y_train_adasyn)
    
    y_pred_adasyn = adasyn_model.predict(X_test)
    y_proba_adasyn = adasyn_model.predict_proba(X_test)[:, 1]
    
    results['ADASYN'] = calculate_comprehensive_metrics(
        y_test, y_pred_adasyn, y_proba_adasyn, "ADASYN"
    )
    
    # 4. Class Weights
    print("\n4. Class Weights")
    class_weight_model = RandomForestClassifier(
        n_estimators=100, 
        class_weight='balanced',
        random_state=42
    )
    class_weight_model.fit(X_train, y_train)
    
    y_pred_weights = class_weight_model.predict(X_test)
    y_proba_weights = class_weight_model.predict_proba(X_test)[:, 1]
    
    results['Class Weights'] = calculate_comprehensive_metrics(
        y_test, y_pred_weights, y_proba_weights, "Class Weights"
    )
    
    # 5. SMOTE + ENN (Combined)
    print("\n5. SMOTE + ENN (Combined)")
    smoteenn = SMOTEENN(random_state=42)
    X_train_smoteenn, y_train_smoteenn = smoteenn.fit_resample(X_train, y_train)
    
    smoteenn_model = RandomForestClassifier(n_estimators=100, random_state=42)
    smoteenn_model.fit(X_train_smoteenn, y_train_smoteenn)
    
    y_pred_smoteenn = smoteenn_model.predict(X_test)
    y_proba_smoteenn = smoteenn_model.predict_proba(X_test)[:, 1]
    
    results['SMOTE+ENN'] = calculate_comprehensive_metrics(
        y_test, y_pred_smoteenn, y_proba_smoteenn, "SMOTE+ENN"
    )
    
    return results

def optimize_threshold_for_sensitivity(y_true, y_proba, target_sensitivity=0.8):
    """Find optimal threshold to achieve target sensitivity"""
    
    fpr, tpr, thresholds = roc_curve(y_true, y_proba)
    
    # Find threshold closest to target sensitivity
    idx = np.argmin(np.abs(tpr - target_sensitivity))
    optimal_threshold = thresholds[idx]
    
    # Apply threshold
    y_pred_optimized = (y_proba >= optimal_threshold).astype(int)
    
    return calculate_comprehensive_metrics(y_true, y_pred_optimized, y_proba, f"Threshold Optimized (Sens={target_sensitivity})")

def print_detailed_results(results):
    """Print detailed results for each approach"""
    
    print("\n" + "="*80)
    print("DETAILED PERFORMANCE RESULTS")
    print("="*80)
    
    for model_name, metrics in results.items():
        print(f"\n{model_name.upper()}")
        print("-" * 40)
        print(f"Accuracy:    {metrics['accuracy']:.4f}")
        print(f"Sensitivity: {metrics['sensitivity']:.4f}")
        print(f"Specificity: {metrics['specificity']:.4f}")
        print(f"Precision:   {metrics['precision']:.4f}")
        print(f"F1-Score:    {metrics['f1_score']:.4f}")
        print(f"AUC:         {metrics['auc']:.4f}")
        
        # Confusion matrix
        cm = metrics['confusion_matrix']
        print(f"\nConfusion Matrix:")
        print(f"                Predicted")
        print(f"Actual  0 (Single)  1 (Multiple)")
        print(f"0 (Single)   {cm[0,0]:6d}      {cm[0,1]:6d}")
        print(f"1 (Multiple) {cm[1,0]:6d}      {cm[1,1]:6d}")

def save_results_to_json(results):
    """Save results to JSON file"""
    import json
    
    # Convert numpy arrays to lists for JSON serialization
    results_json = {}
    for model_name, metrics in results.items():
        results_json[model_name] = {
            'accuracy': float(metrics['accuracy']),
            'sensitivity': float(metrics['sensitivity']),
            'specificity': float(metrics['specificity']),
            'precision': float(metrics['precision']),
            'f1_score': float(metrics['f1_score']),
            'auc': float(metrics['auc']),
            'confusion_matrix': metrics['confusion_matrix'].tolist(),
            'tp': int(metrics['tp']),
            'fp': int(metrics['fp']),
            'fn': int(metrics['fn']),
            'tn': int(metrics['tn'])
        }
    
    with open('enhanced_oversampling_results.json', 'w') as f:
        json.dump(results_json, f, indent=2)
    
    print("\nResults saved to 'enhanced_oversampling_results.json'")

def main():
    """Main execution function"""
    
    print("Enhanced Models with Oversampling - ATPA Assessment")
    print("="*60)
    
    # Load data
    X, y, feature_cols = load_and_prepare_data()
    if X is None:
        return
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"\nTraining set: {X_train.shape[0]} samples")
    print(f"Testing set: {X_test.shape[0]} samples")
    print(f"Class distribution - Training: {np.bincount(y_train)}")
    print(f"Class distribution - Testing: {np.bincount(y_test)}")
    
    # Implement oversampling techniques
    results = implement_oversampling_techniques(X_train, y_train, X_test, y_test)
    
    # Print detailed results
    print_detailed_results(results)
    
    # Plot performance comparison
    plot_performance_comparison(results)
    
    # Save results
    save_results_to_json(results)
    
    # Threshold optimization for best model
    print("\n" + "="*60)
    print("THRESHOLD OPTIMIZATION FOR SENSITIVITY")
    print("="*60)
    
    # Find best model based on sensitivity
    best_model_name = max(results.keys(), key=lambda x: results[x]['sensitivity'])
    best_sensitivity = results[best_model_name]['sensitivity']
    
    print(f"\nBest model for sensitivity: {best_model_name} ({best_sensitivity:.4f})")
    
    # Optimize threshold for 80% sensitivity
    print("\nOptimizing threshold for 80% sensitivity...")
    
    # Get predictions from best model (you would need to refit and predict)
    print("Note: Threshold optimization requires refitting the best model")
    print("This would be implemented in a production environment")
    
    print("\n" + "="*60)
    print("RECOMMENDATIONS")
    print("="*60)
    
    # Find best approach for each metric
    best_sensitivity_model = max(results.keys(), key=lambda x: results[x]['sensitivity'])
    best_f1_model = max(results.keys(), key=lambda x: results[x]['f1_score'])
    best_auc_model = max(results.keys(), key=lambda x: results[x]['auc'])
    
    print(f"\nBest for Sensitivity: {best_sensitivity_model}")
    print(f"Best for F1-Score: {best_f1_model}")
    print(f"Best for AUC: {best_auc_model}")
    
    print("\nFor criminal justice applications:")
    print("- High sensitivity is critical for public safety")
    print("- Consider threshold optimization for 80% sensitivity")
    print("- Monitor false positive rates for resource impact")
    print("- Balance public safety with resource efficiency")

if __name__ == "__main__":
    main() 