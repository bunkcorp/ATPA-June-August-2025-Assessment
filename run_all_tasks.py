#!/usr/bin/env python3
"""
ATPA Assessment - Master Execution Script
June to August 2025

This script runs all tasks in sequence for the ATPA assessment.
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def run_task(task_name, script_path):
    """Run a specific task and return success status"""
    print(f"\n{'='*60}")
    print(f"RUNNING {task_name}")
    print(f"{'='*60}")
    
    try:
        # Change to the task directory
        task_dir = os.path.dirname(script_path)
        script_name = os.path.basename(script_path)
        
        # Run the script
        result = subprocess.run(
            ['python3', script_name],
            cwd=task_dir,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per task
        )
        
        if result.returncode == 0:
            print(f"✅ {task_name} COMPLETED SUCCESSFULLY")
            return True
        else:
            print(f"❌ {task_name} FAILED")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {task_name} TIMED OUT")
        return False
    except Exception as e:
        print(f"❌ {task_name} ERROR: {str(e)}")
        return False

def main():
    """Main execution function"""
    print("ATPA Assessment - Master Execution Script")
    print("June to August 2025")
    print("=" * 60)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Define all tasks
    tasks = [
        ("Task 1: Data Preparation", "Task1_DataPrep/task1_data_preparation.py"),
        ("Task 2: Privacy & Bias Analysis", "Task2_Privacy/task2_privacy_analysis.py"),
        ("Task 3: Generalized Linear Models", "Task3_Modeling/task3_generalized_linear_models.py"),
        ("Task 4: Random Forest & SHAP", "Task4_RandomForest/task4_random_forest_shap.py"),
        ("Task 5: Bayesian Analysis", "Task5_Bayesian/task5_bayesian_analysis.py"),
        ("Task 6: Executive Summary", "Task6_ExecutiveSummary/task6_executive_summary.py")
    ]
    
    # Track results
    results = []
    start_time = time.time()
    
    # Run each task
    for task_name, script_path in tasks:
        success = run_task(task_name, script_path)
        results.append((task_name, success))
        
        # Brief pause between tasks
        time.sleep(2)
    
    # Summary
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n{'='*60}")
    print("EXECUTION SUMMARY")
    print(f"{'='*60}")
    print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Execution Time: {total_time:.2f} seconds ({total_time/60:.2f} minutes)")
    
    successful_tasks = sum(1 for _, success in results if success)
    total_tasks = len(results)
    
    print(f"\nTask Results:")
    for task_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {task_name}: {status}")
    
    print(f"\nOverall Status: {successful_tasks}/{total_tasks} tasks completed successfully")
    
    if successful_tasks == total_tasks:
        print("🎉 ALL TASKS COMPLETED SUCCESSFULLY!")
        print("ATPA Assessment is ready for submission.")
    else:
        print("⚠️  Some tasks failed. Please review the errors above.")
    
    print(f"\n{'='*60}")

if __name__ == "__main__":
    main() 