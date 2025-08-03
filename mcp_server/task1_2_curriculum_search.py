#!/usr/bin/env python3
"""
Task 1 and 2 Comprehensive Curriculum Search
Extract key terms from Tasks 1 and 2 and search curriculum content
"""

from curriculum import ATPACurriculum

def search_task1_2_curriculum():
    print("=" * 80)
    print("TASK 1 & 2 COMPREHENSIVE CURRICULUM SEARCH")
    print("=" * 80)
    
    curriculum = ATPACurriculum()
    
    # Task 1 specific terms
    task1_terms = {
        "1a_data_cleaning": [
            "missing values",
            "missing data", 
            "imputation",
            "dimension reduction",
            "factor variables",
            "categorical variables",
            "numeric predictors",
            "data transformation",
            "data preprocessing"
        ],
        "1b_data_merging": [
            "data joins",
            "merging data",
            "join operations",
            "inner join",
            "outer join",
            "perfect matching",
            "matching keys",
            "record linkage",
            "data integration"
        ],
        "1c_target_variable": [
            "target variable",
            "binary target",
            "ARREST",
            "binary classification",
            "response variable",
            "outcome variable"
        ],
        "1d_exploratory_analysis": [
            "exploratory data analysis",
            "EDA",
            "data visualization",
            "distribution analysis",
            "reasonability checks",
            "outliers",
            "internal consistency",
            "descriptive statistics"
        ]
    }
    
    # Task 2 specific terms (enhanced for Module 1 ethical content)
    task2_terms = {
        "2a_demographic_benefits_risks": [
            "demographic data",
            "race",
            "nationality",
            "citizenship",
            "gender",
            "ethnicity",
            "protected classes",
            "discrimination",
            "bias",
            "fairness"
        ],
        "2b_professional_standards": [
            "ASOP 41",
            "ASOP 23",
            "ASOP 56",
            "professional standards",
            "misuse prevention",
            "actuarial communications",
            "ethical guidelines",
            "regulations",
            "anti-discrimination",
            "civil rights",
            "equal protection",
            "protected characteristics"
        ],
        "2c_criminal_justice": [
            "criminal justice",
            "law enforcement",
            "victim",
            "offender",
            "arrest",
            "public policy",
            "trusted research organization",
            "impartial research"
        ]
    }
    
    print("\n📋 TASK 1 REQUIREMENTS SEARCH")
    print("=" * 50)
    
    task1_total = 0
    for section, terms in task1_terms.items():
        print(f"\n🔍 {section.upper()}:")
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            task1_total += len(search_result['results'])
            print(f"   {term}: {len(search_result['results'])} results")
            if search_result['results']:
                print(f"      Top result: {search_result['results'][0]['excerpt'][:80]}...")
    
    print("\n📋 TASK 2 REQUIREMENTS SEARCH (ENHANCED)")
    print("=" * 50)
    
    task2_total = 0
    for section, terms in task2_terms.items():
        print(f"\n🔍 {section.upper()}:")
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            task2_total += len(search_result['results'])
            print(f"   {term}: {len(search_result['results'])} results")
            if search_result['results']:
                print(f"      Top result: {search_result['results'][0]['excerpt'][:80]}...")
    
    print("\n📋 MODULE 1 SPECIFIC ETHICAL CONTENT")
    print("=" * 50)
    
    # Search for Module 1 specific content
    module1_terms = [
        "anti-discrimination laws",
        "civil rights act",
        "equal credit opportunity act",
        "protected classes",
        "race color religion",
        "national origin",
        "sex gender",
        "age discrimination",
        "disability",
        "sexual orientation",
        "gender identity",
        "transgender",
        "zip code correlation",
        "redlining",
        "fair lending",
        "discriminatory practices",
        "bias detection",
        "fairness assessment",
        "ethical principles",
        "regulatory compliance"
    ]
    
    module1_total = 0
    for term in module1_terms:
        search_result = curriculum.search_curriculum(term)
        module1_total += len(search_result['results'])
        if search_result['results']:
            print(f"   {term}: {len(search_result['results'])} results")
    
    print("\n📋 ADDITIONAL DATA QUALITY TERMS")
    print("=" * 50)
    
    data_quality_terms = [
        "data quality",
        "data validation",
        "quality control",
        "data integrity",
        "consistency checks",
        "validation rules",
        "data verification",
        "quality assessment",
        "data profiling",
        "data auditing",
        "validation procedures",
        "quality metrics",
        "data standards",
        "tidy data",
        "data frames",
        "data transformation"
    ]
    
    data_quality_total = 0
    for term in data_quality_terms:
        search_result = curriculum.search_curriculum(term)
        data_quality_total += len(search_result['results'])
        if search_result['results']:
            print(f"   {term}: {len(search_result['results'])} results")
    
    print("\n" + "=" * 80)
    print("🎯 SUMMARY OF CURRICULUM COVERAGE")
    print("=" * 80)
    
    print(f"Task 1 Total Results: {task1_total}")
    print(f"Task 2 Total Results: {task2_total}")
    print(f"Module 1 Ethical Content: {module1_total} results")
    print(f"Data Quality Content: {data_quality_total} results")
    
    # Get data quality guidelines
    data_quality_guidelines = curriculum.get_data_quality_guidelines()
    print(f"Data Quality Guidelines Module: {data_quality_guidelines['module']}")
    print(f"Available Guidelines: {list(data_quality_guidelines['guidelines'].keys())}")
    
    # Get ethical framework
    ethical_framework = curriculum.get_ethical_framework_details()
    print(f"Ethical Framework Module: {ethical_framework['module']}")
    print(f"Ethical Principles: {list(ethical_framework['principles'].keys())}")

if __name__ == "__main__":
    search_task1_2_curriculum() 