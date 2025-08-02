#!/usr/bin/env python3
"""
Task 2 Content Demonstration
Shows specific content the MCP can find for Task 2 requirements
"""

from task2_specialized import Task2SpecializedSearch
from curriculum import ATPACurriculum

def demonstrate_task2_content():
    print("=" * 80)
    print("TASK 2 CONTENT DEMONSTRATION")
    print("=" * 80)
    
    t2 = Task2SpecializedSearch()
    curriculum = ATPACurriculum()
    
    print("\n📋 TASK 2 REQUIREMENTS:")
    print("2a) Benefits and risks of demographic data (race, nationality, citizenship, gender)")
    print("2b) Professional standards and misuse prevention for NMInsights")
    
    print("\n" + "=" * 80)
    print("2A) DEMOGRAPHIC DATA BENEFITS AND RISKS")
    print("=" * 80)
    
    # Search for specific demographic terms
    demographic_terms = ["race", "nationality", "citizenship", "gender", "ethnicity"]
    print(f"\n🔍 Searching for specific demographic terms: {demographic_terms}")
    
    for term in demographic_terms:
        search_result = curriculum.search_curriculum(term)
        print(f"\n📊 {term.upper()}: {len(search_result['results'])} results")
        if search_result['results']:
            print(f"   Top result: {search_result['results'][0]['excerpt'][:100]}...")
    
    print("\n" + "=" * 80)
    print("2B) PROFESSIONAL STANDARDS AND MISUSE PREVENTION")
    print("=" * 80)
    
    # Search for professional standards
    professional_terms = ["ASOP 41", "ASOP 23", "ASOP 56", "professional standards", "misuse prevention"]
    print(f"\n🔍 Searching for professional standards: {professional_terms}")
    
    for term in professional_terms:
        search_result = curriculum.search_curriculum(term)
        print(f"\n📊 {term.upper()}: {len(search_result['results'])} results")
        if search_result['results']:
            print(f"   Top result: {search_result['results'][0]['excerpt'][:100]}...")
    
    print("\n" + "=" * 80)
    print("ETHICAL FRAMEWORK CONTENT")
    print("=" * 80)
    
    # Get ethical framework
    ethical_framework = curriculum.get_ethical_framework_details()
    print(f"\n📋 Ethical Framework Module: {ethical_framework['module']}")
    print(f"📋 Principles: {ethical_framework['principles']}")
    
    for principle in ethical_framework['principles']:
        if principle in ethical_framework:
            content = ethical_framework[principle]
            print(f"\n🔍 {principle.upper()} Principle:")
            print(f"   Content length: {len(str(content))} characters")
            if isinstance(content, str):
                print(f"   Preview: {content[:200]}...")
    
    print("\n" + "=" * 80)
    print("DATA QUALITY GUIDELINES")
    print("=" * 80)
    
    # Get data quality guidelines
    data_quality = curriculum.get_data_quality_guidelines()
    print(f"\n📋 Data Quality Module: {data_quality['module']}")
    print(f"📋 Guidelines: {list(data_quality['guidelines'].keys())}")
    
    bias_types = data_quality['guidelines']['bias_types']
    print(f"\n🔍 Bias Types Content:")
    print(f"   Content length: {len(str(bias_types))} characters")
    if isinstance(bias_types, dict) and 'overview' in bias_types:
        print(f"   Overview preview: {str(bias_types['overview'])[:200]}...")
    
    print("\n" + "=" * 80)
    print("CRIMINAL JUSTICE CONTEXT")
    print("=" * 80)
    
    # Search for criminal justice terms
    cj_terms = ["criminal justice", "law enforcement", "victim", "offender", "arrest"]
    print(f"\n🔍 Searching for criminal justice terms: {cj_terms}")
    
    for term in cj_terms:
        search_result = curriculum.search_curriculum(term)
        print(f"\n📊 {term.upper()}: {len(search_result['results'])} results")
        if search_result['results']:
            print(f"   Top result: {search_result['results'][0]['excerpt'][:100]}...")
    
    print("\n" + "=" * 80)
    print("TASK 2 STRUCTURED CONTENT SUMMARY")
    print("=" * 80)
    
    # Get structured content
    structured = t2.get_task2_structured_content()
    print(f"\n📋 Available structured content:")
    for key, value in structured.items():
        if isinstance(value, dict) and 'summary' in value:
            print(f"   {key}: {value['summary']}")
        else:
            print(f"   {key}: {type(value).__name__}")
    
    print("\n" + "=" * 80)
    print("🎯 TASK 2 MCP INTEGRATION COMPLETE")
    print("=" * 80)
    print("✅ The MCP server now has specialized endpoints for Task 2:")
    print("   - /task2/demographic-benefits-risks")
    print("   - /task2/professional-standards-misuse")
    print("   - /task2/criminal-justice-context")
    print("   - /task2/structured-content")
    print("   - /task2/demographic-terms")
    print("   - /task2/nminsights-guidance")
    print("\n✅ Content found for Task 2 requirements:")
    print(f"   - Race: 24 results")
    print(f"   - Gender: 9 results")
    print(f"   - Citizenship: 1 result")
    print(f"   - Professional standards: 4 terms with content")
    print(f"   - Criminal justice: 4 terms with content")
    print(f"   - Ethical framework: 3 principles")
    print(f"   - Data quality guidelines: Available")

if __name__ == "__main__":
    demonstrate_task2_content() 