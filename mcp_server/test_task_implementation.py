"""
Test script for ATPA Task Implementation in MCP Server
"""
import requests
import json
import time
from typing import Dict, Any

# MCP Server base URL
BASE_URL = "http://localhost:8000"

def test_server_status():
    """Test if the server is running and task implementation is available"""
    try:
        response = requests.get(f"{BASE_URL}/api/status")
        if response.status_code == 200:
            status = response.json()
            print("✅ Server is running")
            print(f"Task implementation available: {status['layers']['task_implementation']}")
            return status['layers']['task_implementation']
        else:
            print(f"❌ Server status check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        return False

def test_task_status():
    """Test task status endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/tasks/status")
        if response.status_code == 200:
            status = response.json()
            print(f"✅ Task status: {status['completed_tasks']}/{status['total_tasks']} completed")
            print(f"Progress: {status['progress']:.1%}")
            return status
        else:
            print(f"❌ Task status check failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Task status check error: {e}")
        return None

def run_task(task_number: int, sample_size: int = 1000) -> Dict[str, Any]:
    """Run a specific task"""
    print(f"\n🔄 Running Task {task_number}...")
    
    try:
        if task_number == 1:
            response = requests.post(f"{BASE_URL}/tasks/run-task1", params={"sample_size": sample_size})
        elif task_number == 2:
            response = requests.post(f"{BASE_URL}/tasks/run-task2")
        elif task_number == 3:
            response = requests.post(f"{BASE_URL}/tasks/run-task3")
        elif task_number == 4:
            response = requests.post(f"{BASE_URL}/tasks/run-task4")
        elif task_number == 5:
            response = requests.post(f"{BASE_URL}/tasks/run-task5")
        elif task_number == 6:
            response = requests.post(f"{BASE_URL}/tasks/run-task6")
        else:
            print(f"❌ Invalid task number: {task_number}")
            return {}
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Task {task_number} completed successfully")
            return result
        else:
            print(f"❌ Task {task_number} failed: {response.status_code}")
            print(f"Error: {response.text}")
            return {}
            
    except Exception as e:
        print(f"❌ Error running Task {task_number}: {e}")
        return {}

def run_all_tasks(sample_size: int = 1000):
    """Run all tasks in sequence"""
    print(f"\n🚀 Running all ATPA tasks with sample size {sample_size}...")
    
    try:
        response = requests.post(f"{BASE_URL}/tasks/run-all", params={"sample_size": sample_size})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ All tasks completed successfully")
            return result
        else:
            print(f"❌ Running all tasks failed: {response.status_code}")
            print(f"Error: {response.text}")
            return {}
            
    except Exception as e:
        print(f"❌ Error running all tasks: {e}")
        return {}

def get_task_results(task_number: int):
    """Get results for a specific task"""
    try:
        response = requests.get(f"{BASE_URL}/tasks/results/{task_number}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Retrieved results for Task {task_number}")
            return result
        else:
            print(f"❌ Failed to get results for Task {task_number}: {response.status_code}")
            return {}
            
    except Exception as e:
        print(f"❌ Error getting results for Task {task_number}: {e}")
        return {}

def save_results(filepath: str):
    """Save all results to file"""
    try:
        response = requests.post(f"{BASE_URL}/tasks/save-results", params={"filepath": filepath})
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Results saved to {filepath}")
            return result
        else:
            print(f"❌ Failed to save results: {response.status_code}")
            return {}
            
    except Exception as e:
        print(f"❌ Error saving results: {e}")
        return {}

def main():
    """Main test function"""
    print("🧪 Testing ATPA Task Implementation in MCP Server")
    print("=" * 60)
    
    # Test server status
    if not test_server_status():
        print("❌ Server not available. Please start the MCP server first.")
        return
    
    # Test task status
    task_status = test_task_status()
    if task_status is None:
        print("❌ Cannot get task status")
        return
    
    # Run individual tasks
    print("\n📋 Testing individual tasks...")
    
    # Task 1: Data Preparation
    task1_result = run_task(1, sample_size=1000)
    if task1_result:
        print(f"   - Missing values analyzed: {len(task1_result['results']['missing_analysis']['incidents']['missing_counts'])} columns")
        print(f"   - Data quality score: {100 - task1_result['results']['quality_report']['missing_values']['missing_percentage']:.1f}%")
    
    # Task 2: Privacy and Ethics
    task2_result = run_task(2)
    if task2_result:
        protected_vars = task2_result['results']['protected_variables']
        print(f"   - Protected variables identified: {len(protected_vars)}")
        print(f"   - Ethics recommendations: {len(task2_result['results']['ethics_recommendations'])}")
    
    # Task 3: Generalized Linear Models
    task3_result = run_task(3)
    if task3_result:
        best_model = task3_result['results']['best_model']
        best_auc = task3_result['results']['model_comparison']['models'][best_model]['auc']
        print(f"   - Best model: {best_model}")
        print(f"   - Best AUC: {best_auc:.3f}")
    
    # Task 4: Random Forest with SHAP
    task4_result = run_task(4)
    if task4_result:
        rf_auc = task4_result['results']['random_forest']['metrics']['auc']
        top_features = task4_result['results']['feature_importance']['top_features'][:3]
        print(f"   - Random Forest AUC: {rf_auc:.3f}")
        print(f"   - Top features: {[f[0] for f in top_features]}")
    
    # Task 5: Bayesian Analysis
    task5_result = run_task(5)
    if task5_result:
        bayesian_auc = task5_result['results']['bayesian_analysis']['metrics']['auc']
        print(f"   - Bayesian AUC: {bayesian_auc:.3f}")
    
    # Task 6: Executive Summary
    task6_result = run_task(6)
    if task6_result:
        summary = task6_result['results']['executive_summary']
        print(f"   - Total incidents: {summary['overview']['total_incidents']}")
        print(f"   - Arrest rate: {summary['overview']['arrest_rate']:.1%}")
        print(f"   - Key insights: {len(summary['key_insights'])}")
    
    # Test getting results
    print("\n📊 Testing result retrieval...")
    for task_num in range(1, 7):
        results = get_task_results(task_num)
        if results:
            print(f"   - Task {task_num} results retrieved successfully")
    
    # Save results
    print("\n💾 Testing result saving...")
    save_results("test_results.json")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main() 