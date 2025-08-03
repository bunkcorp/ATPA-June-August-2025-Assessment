#!/usr/bin/env python3
"""
Test script for Classification Metrics Layer
Demonstrates confusion matrices, sensitivity, specificity, and other essential metrics
"""

import requests
import json
import numpy as np

# Sample data for testing (simulating arrest prediction results)
# True labels: 1 = arrest, 0 = no arrest
y_true = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
y_pred = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
y_pred_proba = [0.8, 0.2, 0.9, 0.6, 0.4, 0.1, 0.3, 0.85, 0.15, 0.75, 0.25, 0.1, 0.9, 0.2, 0.65, 0.8, 0.3, 0.45, 0.2, 0.1]

def test_classification_metrics():
    """Test the classification metrics endpoints"""
    
    base_url = "http://localhost:8000"
    
    print("=" * 60)
    print("TESTING CLASSIFICATION METRICS LAYER")
    print("=" * 60)
    
    # Test 1: Get essential metrics explanation
    print("\n1. Essential Metrics Explanation:")
    print("-" * 40)
    try:
        response = requests.get(f"{base_url}/metrics/essential-metrics")
        if response.status_code == 200:
            data = response.json()
            print("✓ Essential metrics explanation retrieved")
            print(f"  - Confusion Matrix: {data['essential_metrics']['confusion_matrix']['description']}")
            print(f"  - Sensitivity: {data['essential_metrics']['sensitivity']['description']}")
            print(f"  - Specificity: {data['essential_metrics']['specificity']['description']}")
            print(f"  - Class Imbalance: {data['class_imbalance_considerations']['problem']}")
        else:
            print(f"✗ Error: {response.status_code}")
    except Exception as e:
        print(f"✗ Connection error: {e}")
    
    # Test 2: Calculate metrics for a sample model
    print("\n2. Calculate Classification Metrics:")
    print("-" * 40)
    try:
        payload = {
            "y_true": y_true,
            "y_pred": y_pred,
            "y_pred_proba": y_pred_proba,
            "model_name": "Sample_GLM_Model"
        }
        
        response = requests.post(f"{base_url}/metrics/calculate", json=payload)
        if response.status_code == 200:
            metrics = response.json()
            print("✓ Metrics calculated successfully")
            print(f"  - Accuracy: {metrics['accuracy']:.3f}")
            print(f"  - Sensitivity: {metrics['sensitivity']:.3f}")
            print(f"  - Specificity: {metrics['specificity']:.3f}")
            print(f"  - Precision: {metrics['precision']:.3f}")
            print(f"  - F1-Score: {metrics['f1_score']:.3f}")
            print(f"  - Balanced Accuracy: {metrics['balanced_accuracy']:.3f}")
            print(f"  - ROC-AUC: {metrics['roc_auc']:.3f}")
            
            # Show confusion matrix
            cm = metrics['confusion_matrix']
            print(f"  - Confusion Matrix:")
            print(f"    True Negatives: {cm['true_negatives']}")
            print(f"    False Positives: {cm['false_positives']}")
            print(f"    False Negatives: {cm['false_negatives']}")
            print(f"    True Positives: {cm['true_positives']}")
            
            # Show class distribution
            dist = metrics['class_distribution']
            print(f"  - Class Distribution:")
            print(f"    Total Samples: {dist['total_samples']}")
            print(f"    Positive Class (Arrests): {dist['positive_class']} ({dist['positive_rate']:.1%})")
            print(f"    Negative Class (No Arrests): {dist['negative_class']}")
            
        else:
            print(f"✗ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"✗ Connection error: {e}")
    
    # Test 3: Get business interpretation
    print("\n3. Business Interpretation:")
    print("-" * 40)
    try:
        response = requests.get(f"{base_url}/metrics/interpretation/Sample_GLM_Model")
        if response.status_code == 200:
            interpretation = response.json()
            print("✓ Business interpretation retrieved")
            
            print("  Business Impact:")
            for impact, description in interpretation['business_impact'].items():
                print(f"    - {impact.replace('_', ' ').title()}: {description}")
            
            print("  Policy Implications:")
            for implication in interpretation['policy_implications']:
                print(f"    - {implication}")
            
            print("  Recommendations:")
            for rec in interpretation['recommendations']:
                print(f"    - {rec}")
                
        else:
            print(f"✗ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"✗ Connection error: {e}")
    
    # Test 4: Get ATPA task guidance
    print("\n4. ATPA Task Guidance:")
    print("-" * 40)
    for task_num in [3, 4, 6]:  # Tasks that focus on modeling
        try:
            response = requests.get(f"{base_url}/metrics/task-guidance/{task_num}")
            if response.status_code == 200:
                guidance = response.json()
                print(f"✓ Task {task_num} guidance retrieved")
                print(f"  - Focus: {guidance['focus']}")
                print(f"  - Metrics Importance: {guidance['metrics_importance']}")
                print(f"  - Key Considerations:")
                for consideration in guidance['key_considerations']:
                    print(f"    * {consideration}")
                print()
            else:
                print(f"✗ Error for task {task_num}: {response.status_code}")
        except Exception as e:
            print(f"✗ Connection error for task {task_num}: {e}")
    
    # Test 5: Compare multiple models
    print("\n5. Model Comparison:")
    print("-" * 40)
    try:
        # Create sample results for multiple models
        model_results = {
            "GLM_Model": {
                "accuracy": 0.75,
                "sensitivity": 0.70,
                "specificity": 0.80,
                "precision": 0.65,
                "f1_score": 0.67,
                "balanced_accuracy": 0.75,
                "roc_auc": 0.82,
                "class_distribution": {"positive_rate": 0.19}
            },
            "Random_Forest": {
                "accuracy": 0.78,
                "sensitivity": 0.75,
                "specificity": 0.82,
                "precision": 0.70,
                "f1_score": 0.72,
                "balanced_accuracy": 0.78,
                "roc_auc": 0.85,
                "class_distribution": {"positive_rate": 0.19}
            },
            "Neural_Network": {
                "accuracy": 0.80,
                "sensitivity": 0.78,
                "specificity": 0.85,
                "precision": 0.75,
                "f1_score": 0.76,
                "balanced_accuracy": 0.81,
                "roc_auc": 0.88,
                "class_distribution": {"positive_rate": 0.19}
            }
        }
        
        response = requests.post(f"{base_url}/metrics/compare", json=model_results)
        if response.status_code == 200:
            comparison = response.json()
            print("✓ Model comparison completed")
            
            print("  Best Models by Metric:")
            for metric, best in comparison['best_models'].items():
                print(f"    - {metric}: {best['model']} ({best['value']:.3f})")
            
            print("  Recommendations:")
            for rec in comparison['recommendations']:
                print(f"    - {rec}")
                
        else:
            print(f"✗ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"✗ Connection error: {e}")
    
    print("\n" + "=" * 60)
    print("CLASSIFICATION METRICS TESTING COMPLETE")
    print("=" * 60)
    print("\nKey Points Demonstrated:")
    print("✓ Confusion Matrix with True Positives, False Positives, True Negatives, False Negatives")
    print("✓ Sensitivity (Recall) - Ability to identify actual arrests")
    print("✓ Specificity - Ability to identify non-arrests")
    print("✓ Precision - Accuracy of positive predictions")
    print("✓ F1-Score - Balanced metric for imbalanced data")
    print("✓ Balanced Accuracy - Better than accuracy for imbalanced data")
    print("✓ ROC-AUC - Overall discrimination ability")
    print("✓ Business interpretation for arrest prediction")
    print("✓ ATPA task-specific guidance")
    print("✓ Model comparison capabilities")

if __name__ == "__main__":
    test_classification_metrics() 