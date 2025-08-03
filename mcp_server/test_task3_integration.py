#!/usr/bin/env python3
"""
Test Task 3 integration with MCP server
"""

from task3_specialized import Task3SpecializedSearch

def test_task3_integration():
    print("=== TASK 3 MCP INTEGRATION TEST ===")
    
    try:
        task3 = Task3SpecializedSearch()
        
        print("\n1. Testing GLM content...")
        glm = task3.search_glm_content()
        print(f"✅ Found content for {len([r for r in glm['results'].values() if r])} GLM terms")
        
        print("\n2. Testing mixed models content...")
        mixed = task3.search_mixed_models_content()
        print(f"✅ Found content for {len([r for r in mixed['results'].values() if r])} mixed model terms")
        
        print("\n3. Testing model validation content...")
        validation = task3.search_model_validation_content()
        print(f"✅ Found content for {len([r for r in validation['results'].values() if r])} validation terms")
        
        print("\n4. Testing variable selection content...")
        selection = task3.search_variable_selection_content()
        print(f"✅ Found content for {len([r for r in selection['results'].values() if r])} variable selection terms")
        
        print("\n5. Testing performance metrics content...")
        metrics = task3.search_performance_metrics_content()
        print(f"✅ Found content for {len([r for r in metrics['results'].values() if r])} performance metric terms")
        
        print("\n6. Testing Task 3 requirements content...")
        requirements = task3.get_task3_requirements_content()
        for req_key, req_data in requirements.items():
            print(f"   {req_key}: {req_data['summary']}")
        
        print("\n7. Testing specific modeling terms...")
        specific = task3.search_specific_modeling_terms(['logistic regression', 'polynomial regression', 'stepwise selection'])
        for term, result in specific.items():
            print(f"   {term}: {result['count']} results")
        
        print("\n🎉 Task 3 MCP Integration Test Completed Successfully!")
        print("\n📋 Available Task 3 Endpoints:")
        print("   - /task3/glm-content")
        print("   - /task3/mixed-models-content")
        print("   - /task3/model-validation-content")
        print("   - /task3/variable-selection-content")
        print("   - /task3/performance-metrics-content")
        print("   - /task3/structured-content")
        print("   - /task3/modeling-terms")
        print("   - /task3/requirements-content")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_task3_integration() 