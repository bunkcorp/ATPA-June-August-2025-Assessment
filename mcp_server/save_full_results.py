#!/usr/bin/env python3
"""
Save full dataset ATPA task results - Simplified version
"""
from task_implementation import ATPATaskImplementation
from loader import DataLoader
from protocol import DataProtocol
import json
import numpy as np
import pandas as pd
from datetime import datetime

def clean_for_json(obj):
    """Recursively clean objects for JSON serialization"""
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            # Convert keys to strings if they're not already
            if not isinstance(k, (str, int, float, bool, type(None))):
                k = str(k)
            cleaned[k] = clean_for_json(v)
        return cleaned
    elif isinstance(obj, list):
        return [clean_for_json(item) for item in obj]
    elif isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif hasattr(obj, 'dtype') and hasattr(obj, 'tolist'):  # pandas Series, etc.
        return obj.tolist()
    elif hasattr(obj, 'to_dict'):  # pandas DataFrame
        return obj.to_dict('records')
    elif hasattr(obj, 'isoformat'):  # pandas Timestamp, datetime objects
        return obj.isoformat()
    elif pd.isna(obj):
        return None
    elif isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    else:
        return str(obj)

def safe_get(data, *keys, default=None):
    """Safely get nested dictionary values"""
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError, IndexError):
        return default

def extract_key_metrics(task1, task2, task3, task4, task5, task6):
    """Extract only the key metrics and results, not all raw data"""
    
    # Task 1 - Data Preparation
    task1_summary = {
        'total_records': safe_get(task1, 'quality_report', 'total_records'),
        'total_columns': safe_get(task1, 'quality_report', 'total_columns'),
        'missing_data_summary': {
            'total_missing_values': safe_get(task1, 'quality_report', 'missing_values', 'total_missing'),
            'missing_percentage': safe_get(task1, 'quality_report', 'missing_values', 'missing_percentage')
        },
        'data_types_summary': safe_get(task1, 'quality_report', 'data_types'),
        'duplicate_records': safe_get(task1, 'quality_report', 'duplicate_records'),
        'missing_analysis': safe_get(task1, 'missing_analysis', default={}),
        'imputation_summary': safe_get(task1, 'imputation_summary', default={})
    }
    
    # Task 2 - Privacy & Ethics
    task2_summary = {
        'protected_variables': safe_get(task2, 'protected_variables', default=[]),
        'protected_variables_count': len(safe_get(task2, 'protected_variables', default=[])),
        'ethics_recommendations': safe_get(task2, 'ethics_recommendations', default=[]),
        'detailed_bias_analysis': safe_get(task2, 'detailed_bias_analysis', default={}),
        'risk_assessment': safe_get(task2, 'risk_assessment', default={})
    }
    
    # Task 3 - Generalized Linear Models
    best_model = safe_get(task3, 'best_model', default='unknown')
    task3_summary = {
        'best_model': best_model,
        'best_model_metrics': safe_get(task3, 'models', best_model, 'metrics', default={}),
        'model_comparison': {},
        'coefficient_analysis': safe_get(task3, 'coefficient_analysis', default={})
    }
    
    # Add model comparison if available
    models = safe_get(task3, 'models', default={})
    for model, data in models.items():
        task3_summary['model_comparison'][model] = {
            'accuracy': safe_get(data, 'metrics', 'accuracy'),
            'precision': safe_get(data, 'metrics', 'precision'),
            'recall': safe_get(data, 'metrics', 'recall'),
            'f1_score': safe_get(data, 'metrics', 'f1_score'),
            'auc': safe_get(data, 'metrics', 'auc')
        }
    
    # Task 4 - Random Forest with SHAP
    task4_summary = {
        'random_forest_metrics': safe_get(task4, 'random_forest', 'metrics', default={}),
        'top_features': safe_get(task4, 'shap_analysis', 'feature_importance_ranking', default=[])[:10],  # Top 10 features
        'detailed_shap_analysis': safe_get(task4, 'detailed_shap_analysis', default={})
    }
    
    # Task 5 - Bayesian Analysis
    task5_summary = {
        'bayesian_metrics': safe_get(task5, 'bayesian_analysis', 'metrics', default={}),
        'coefficient_analysis': {
            'significant_features': safe_get(task5, 'bayesian_analysis', 'coefficient_analysis', 'significant_features', default=[])[:10]  # Top 10
        },
        'uncertainty_analysis': safe_get(task5, 'uncertainty_analysis', default={})
    }
    
    # Task 6 - Executive Summary
    task6_summary = {
        'overview': safe_get(task6, 'executive_summary', 'overview', default={}),
        'key_insights': safe_get(task6, 'executive_summary', 'key_insights', default=[]),
        'recommendations': safe_get(task6, 'executive_summary', 'recommendations', default=[]),
        'risk_assessment': safe_get(task6, 'risk_assessment', default={}),
        'action_items': safe_get(task6, 'action_items', default=[])
    }
    
    return {
        'task1': task1_summary,
        'task2': task2_summary,
        'task3': task3_summary,
        'task4': task4_summary,
        'task5': task5_summary,
        'task6': task6_summary
    }

def main():
    print("🎯 Saving Full Dataset ATPA Results (Simplified)...")
    
    # Initialize with full dataset
    loader = DataLoader('../Task1_DataPrep/incidents.csv', '../Task1_DataPrep/arrestee.csv')
    protocol = DataProtocol(loader)
    task_impl = ATPATaskImplementation(loader, protocol)
    
    # Run all tasks with full dataset
    print("🔄 Running all tasks with full dataset (96,904 records)...")
    
    task1 = task_impl.task1_data_preparation(sample_size=None)
    print("✅ Task 1 completed")
    
    task2 = task_impl.task2_privacy_ethics_analysis()
    print("✅ Task 2 completed")
    
    task3 = task_impl.task3_generalized_linear_models()
    print("✅ Task 3 completed")
    
    task4 = task_impl.task4_random_forest_shap()
    print("✅ Task 4 completed")
    
    task5 = task_impl.task5_bayesian_analysis()
    print("✅ Task 5 completed")
    
    task6 = task_impl.task6_executive_summary()
    print("✅ Task 6 completed")
    
    # Extract only key metrics and results
    print("📊 Extracting key metrics...")
    summary_results = extract_key_metrics(task1, task2, task3, task4, task5, task6)
    
    # Clean the results for JSON serialization
    print("🧹 Cleaning results for JSON serialization...")
    cleaned_results = clean_for_json(summary_results)
    
    # Save the simplified results
    with open('full_dataset_results_simplified.json', 'w') as f:
        json.dump(cleaned_results, f, indent=2)
    
    print("✅ Simplified results saved to full_dataset_results_simplified.json")
    
    # Print summary
    print("\n🎯 FULL DATASET RESULTS SUMMARY")
    print("=" * 60)
    print(f"📊 Task 1 - Total Records: {safe_get(task1, 'quality_report', 'total_records', default='N/A'):,}")
    print(f"📊 Task 1 - Total Columns: {safe_get(task1, 'quality_report', 'total_columns', default='N/A')}")
    print(f"📊 Task 2 - Protected Variables: {len(safe_get(task2, 'protected_variables', default=[]))}")
    print(f"📊 Task 3 - Best Model: {safe_get(task3, 'best_model', default='N/A')}")
    print(f"📊 Task 4 - Random Forest AUC: {safe_get(task4, 'random_forest', 'metrics', 'auc', default='N/A')}")
    print(f"📊 Task 5 - Bayesian AUC: {safe_get(task5, 'bayesian_analysis', 'metrics', 'auc', default='N/A')}")
    print(f"📊 Task 6 - Arrest Rate: {safe_get(task6, 'executive_summary', 'overview', 'arrest_rate', default='N/A')}")
    print("✅ ALL TASKS COMPLETED WITH FULL DATASET!")
    print("📁 Results saved to: full_dataset_results_simplified.json")

if __name__ == "__main__":
    main() 