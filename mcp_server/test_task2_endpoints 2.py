#!/usr/bin/env python3
"""
Test script for Task 2 specialized endpoints
"""

from task2_specialized import Task2SpecializedSearch

def test_task2_endpoints():
    print("=== TASK 2 SPECIALIZED ENDPOINTS TEST ===")
    
    try:
        t2 = Task2SpecializedSearch()
        
        print("\n1. Testing demographic benefits/risks...")
        demo = t2.search_demographic_data_benefits_risks()
        print(f"✅ Found content for {len([r for r in demo['results'].values() if r])} terms")
        
        print("\n2. Testing professional standards...")
        prof = t2.search_professional_standards_misuse_prevention()
        print(f"✅ Found content for {len([r for r in prof['results'].values() if r])} terms")
        
        print("\n3. Testing criminal justice context...")
        cj = t2.search_criminal_justice_specific()
        print(f"✅ Found content for {len([r for r in cj['results'].values() if r])} terms")
        
        print("\n4. Testing specific demographic terms...")
        specific = t2.search_specific_demographic_terms(['race', 'nationality', 'citizenship', 'gender'])
        for term, result in specific.items():
            print(f"   {term}: {result['count']} results")
        
        print("\n5. Testing NMInsights guidance...")
        nminsights = t2.get_nminsights_specific_guidance()
        print(f"✅ Found guidance for {len([r for r in nminsights['results'].values() if r])} terms")
        
        print("\n6. Testing structured content...")
        structured = t2.get_task2_structured_content()
        print(f"✅ Structured content includes: {list(structured.keys())}")
        
        print("\n🎉 All Task 2 endpoints working correctly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_task2_endpoints() 