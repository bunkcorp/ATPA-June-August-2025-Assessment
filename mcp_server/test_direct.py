#!/usr/bin/env python3
"""
Direct test of ATPA Task Implementation
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from task_implementation import ATPATaskImplementation
from loader import DataLoader
from protocol import DataProtocol

def test_task_implementation():
    """Test the task implementation directly"""
    print("🧪 Testing ATPA Task Implementation Directly")
    print("=" * 60)
    
    # Initialize data layers
    print("📊 Initializing data layers...")
    data_dir = "../Task1_DataPrep"
    incidents_path = os.path.join(data_dir, "incidents.csv")
    arrestee_path = os.path.join(data_dir, "arrestee.csv")
    
    try:
        # Create data loader
        loader = DataLoader(incidents_path, arrestee_path)
        print("✅ DataLoader created successfully")
        
        # Create protocol layer
        protocol = DataProtocol(loader)
        print("✅ DataProtocol created successfully")
        
        # Create task implementation
        task_impl = ATPATaskImplementation(loader, protocol)
        print("✅ ATPATaskImplementation created successfully")
        
        # Test Task 1
        print("\n🔄 Running Task 1: Data Preparation...")
        task1_results = task_impl.task1_data_preparation(sample_size=1000)
        print("✅ Task 1 completed successfully!")
        print(f"   - Missing values analyzed: {len(task1_results['missing_analysis']['incidents']['missing_counts'])} columns")
        print(f"   - Data quality score: {100 - task1_results['quality_report']['missing_values']['missing_percentage']:.1f}%")
        
        # Test Task 2
        print("\n🔄 Running Task 2: Privacy and Ethics...")
        task2_results = task_impl.task2_privacy_ethics_analysis()
        print("✅ Task 2 completed successfully!")
        print(f"   - Protected variables: {len(task2_results['protected_variables'])}")
        print(f"   - Ethics recommendations: {len(task2_results['ethics_recommendations'])}")
        
        # Test Task 3
        print("\n🔄 Running Task 3: Generalized Linear Models...")
        task3_results = task_impl.task3_generalized_linear_models()
        print("✅ Task 3 completed successfully!")
        best_model = task3_results['best_model']
        best_auc = task3_results['model_comparison']['models'][best_model]['auc']
        print(f"   - Best model: {best_model}")
        print(f"   - Best AUC: {best_auc:.3f}")
        
        # Test Task 4
        print("\n🔄 Running Task 4: Random Forest with SHAP...")
        task4_results = task_impl.task4_random_forest_shap()
        print("✅ Task 4 completed successfully!")
        rf_auc = task4_results['random_forest']['metrics']['auc']
        top_features = task4_results['feature_importance']['top_features'][:3]
        print(f"   - Random Forest AUC: {rf_auc:.3f}")
        print(f"   - Top features: {[f[0] for f in top_features]}")
        
        # Test Task 5
        print("\n🔄 Running Task 5: Bayesian Analysis...")
        task5_results = task_impl.task5_bayesian_analysis()
        print("✅ Task 5 completed successfully!")
        bayesian_auc = task5_results['bayesian_analysis']['metrics']['auc']
        print(f"   - Bayesian AUC: {bayesian_auc:.3f}")
        
        # Test Task 6
        print("\n🔄 Running Task 6: Executive Summary...")
        task6_results = task_impl.task6_executive_summary()
        print("✅ Task 6 completed successfully!")
        summary = task6_results['executive_summary']
        print(f"   - Total incidents: {summary['overview']['total_incidents']}")
        print(f"   - Arrest rate: {summary['overview']['arrest_rate']:.1%}")
        print(f"   - Key insights: {len(summary['key_insights'])}")
        
        print("\n🎉 All tasks completed successfully!")
        print("=" * 60)
        
        # Save results
        print("\n💾 Saving results...")
        task_impl.save_results("direct_test_results.json")
        print("✅ Results saved to direct_test_results.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_task_implementation()
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Tests failed!")
        sys.exit(1) 