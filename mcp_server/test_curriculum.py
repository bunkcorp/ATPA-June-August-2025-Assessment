#!/usr/bin/env python3
"""
Test script for ATPA Curriculum functionality
"""

from curriculum import ATPACurriculum
import json

def test_curriculum_functionality():
    """Test all curriculum functions"""
    print("=" * 60)
    print("ATPA CURRICULUM FUNCTIONALITY TEST")
    print("=" * 60)
    
    # Initialize curriculum
    print("\n1. Initializing ATPA Curriculum...")
    curriculum = ATPACurriculum()
    print("✓ Curriculum initialized successfully")
    
    # Test module overview
    print("\n2. Testing Module Overview...")
    overview = curriculum.get_module_overview()
    print(f"✓ Found {overview['total_modules']} modules:")
    for module_key, module_info in overview['modules'].items():
        print(f"  - {module_info['title']} ({'✓' if module_info['loaded'] else '✗'})")
    
    # Test learning objectives
    print("\n3. Testing Learning Objectives...")
    objectives = curriculum.get_learning_objectives()
    print(f"✓ Learning objectives available for {len(objectives)} modules:")
    for module_key, module_info in objectives.items():
        print(f"  - {module_info['title']}: {len(module_info['objectives'])} characters of content")
    
    # Test ethical framework
    print("\n4. Testing Ethical Framework...")
    ethics = curriculum.get_ethical_framework_details()
    print(f"✓ Ethical framework from {ethics['module']}:")
    print(f"  - Principles: {len(ethics['principles'])} key principles")
    print(f"  - Content length: {len(ethics['full_content'])} characters")
    
    # Test modeling techniques
    print("\n5. Testing Modeling Techniques...")
    modeling = curriculum.get_modeling_techniques()
    print(f"✓ Modeling techniques from {modeling['module']}:")
    for technique, details in modeling['techniques'].items():
        print(f"  - {technique}: {len(details)} characters of content")
    
    # Test explainability techniques
    print("\n6. Testing Explainability Techniques...")
    explainability = curriculum.get_explainability_techniques()
    print(f"✓ Explainability techniques from {explainability['module']}:")
    for technique, details in explainability['techniques'].items():
        print(f"  - {technique}: {len(details)} characters of content")
    
    # Test data quality guidelines
    print("\n7. Testing Data Quality Guidelines...")
    data_quality = curriculum.get_data_quality_guidelines()
    print(f"✓ Data quality guidelines from {data_quality['module']}:")
    print(f"  - Guidelines: {len(data_quality['guidelines'])} key guidelines")
    print(f"  - Content length: {len(data_quality['full_content'])} characters")
    
    # Test curriculum search
    print("\n8. Testing Curriculum Search...")
    search_terms = ["bias detection", "SHAP values", "data quality", "ethical framework"]
    for term in search_terms:
        results = curriculum.search_curriculum(term)
        print(f"  - Search '{term}': {len(results['results'])} results")
    
    # Test specific module content
    print("\n9. Testing Specific Module Content...")
    for module_key in ['module_1', 'module_2', 'module_3', 'module_4']:
        content = curriculum.get_module_content(module_key)
        title = content['module_info']['title']
        sections_count = len(content['sections'])
        concepts_count = len(content['key_concepts'])
        print(f"  - {title}: {sections_count} sections, {concepts_count} key concepts")
    
    # Test curriculum summary
    print("\n10. Testing Curriculum Summary...")
    summary = curriculum.get_curriculum_summary()
    print(f"✓ Curriculum summary generated:")
    print(f"  - Total modules: {summary['overview']['total_modules']}")
    print(f"  - Key concepts: {len(summary['key_concepts'])} concepts")
    print(f"  - Module relationships: {len(summary['module_relationships'])} relationships")
    
    print("\n" + "=" * 60)
    print("ALL CURRICULUM TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

def demonstrate_practical_usage():
    """Demonstrate practical usage scenarios"""
    print("\n" + "=" * 60)
    print("PRACTICAL USAGE DEMONSTRATIONS")
    print("=" * 60)
    
    curriculum = ATPACurriculum()
    
    # Scenario 1: Ethical Analysis for Task 2
    print("\n📋 Scenario 1: Ethical Analysis for Task 2")
    print("-" * 40)
    ethics = curriculum.get_ethical_framework_details()
    print(f"Available ethical principles: {list(ethics['principles'].keys())}")
    
    # Scenario 2: Modeling Techniques for Task 3
    print("\n📋 Scenario 2: Modeling Techniques for Task 3")
    print("-" * 40)
    modeling = curriculum.get_modeling_techniques()
    print(f"Available modeling techniques: {list(modeling['techniques'].keys())}")
    
    # Scenario 3: Explainability for Task 4
    print("\n📋 Scenario 3: Explainability for Task 4")
    print("-" * 40)
    explainability = curriculum.get_explainability_techniques()
    print(f"Available explainability techniques: {list(explainability['techniques'].keys())}")
    
    # Scenario 4: Data Quality for Task 1
    print("\n📋 Scenario 4: Data Quality for Task 1")
    print("-" * 40)
    data_quality = curriculum.get_data_quality_guidelines()
    print(f"Available data quality guidelines: {list(data_quality['guidelines'].keys())}")
    
    # Scenario 5: Search for specific topics
    print("\n📋 Scenario 5: Search for Specific Topics")
    print("-" * 40)
    topics = ["SHAP values", "bias detection", "model validation", "executive summary"]
    for topic in topics:
        results = curriculum.search_curriculum(topic)
        print(f"'{topic}': {len(results['results'])} results found")

if __name__ == "__main__":
    test_curriculum_functionality()
    demonstrate_practical_usage() 