#!/usr/bin/env python3
"""
Task 1 Specialized Module for ATPA MCP Server
Handles specific searches for data preparation, joins, validation, EDA, and other Task 1 requirements
"""

from curriculum import ATPACurriculum
from typing import Dict, List, Optional
import re

class Task1SpecializedSearch:
    """
    Specialized search functionality for Task 1 requirements
    """
    
    def __init__(self):
        self.curriculum = ATPACurriculum()
        
    def search_data_preparation_content(self) -> Dict:
        """
        Search for content specifically about data preparation and cleaning
        """
        search_terms = [
            "data preparation",
            "data cleaning",
            "missing values",
            "missing data",
            "imputation",
            "data validation",
            "data quality",
            "dimension reduction",
            "factor variables",
            "categorical variables",
            "numeric predictors",
            "data transformation",
            "data preprocessing",
            "selection bias",
            "overrepresentation",
            "causes of selection bias",
            "selection bias unfair outcomes",
            "measurement bias",
            "feature selection omitted variable bias",
            "selecting levels factor variable",
            "subsetting continuous variable",
            "identifying missing values",
            "removing missing values",
            "factor recoding",
            "relational database",
            "combining datasets",
            "left joins",
            "right joins",
            "inner joins",
            "detecting inaccurate data",
            "duplicate records",
            "target leakage",
            "missing at random",
            "permutation test",
            "missing extreme values",
            "knn imputation",
            "categorical imputation",
            "missing target variable observations",
            "identifying outliers",
            "outlier handling"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} data preparation terms"
        }
    
    def search_data_joins_content(self) -> Dict:
        """
        Search for content about data joins and merging
        """
        search_terms = [
            "data joins",
            "merging data",
            "join operations",
            "inner join",
            "outer join",
            "left join",
            "right join",
            "data matching",
            "record linkage",
            "data integration",
            "combining datasets",
            "file merging",
            "perfect matching",
            "matching keys",
            "relational database",
            "combining datasets",
            "left joins",
            "right joins",
            "inner joins",
            "join types",
            "data merging strategies",
            "record matching",
            "data integration techniques"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} data joins terms"
        }
    
    def search_eda_content(self) -> Dict:
        """
        Search for content about Exploratory Data Analysis
        """
        search_terms = [
            "exploratory data analysis",
            "EDA",
            "data visualization",
            "distribution analysis",
            "target variable",
            "binary target",
            "reasonability checks",
            "outliers",
            "internal consistency",
            "data exploration",
            "descriptive statistics",
            "data profiling",
            "variable relationships",
            "correlation analysis"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} EDA terms"
        }
    
    def search_data_validation_content(self) -> Dict:
        """
        Search for content about data validation and quality
        """
        search_terms = [
            "data validation",
            "data quality",
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
            "detecting inaccurate data",
            "duplicate records",
            "target leakage",
            "data accuracy",
            "data consistency",
            "data completeness",
            "data reliability",
            "data verification methods",
            "quality assurance",
            "data governance"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} data validation terms"
        }
    
    def search_variable_analysis_content(self) -> Dict:
        """
        Search for content about variable analysis and transformation
        """
        search_terms = [
            "variable analysis",
            "predictor analysis",
            "factor variables",
            "categorical variables",
            "numeric variables",
            "variable transformation",
            "variable conversion",
            "data types",
            "variable encoding",
            "feature engineering",
            "variable selection",
            "predictor selection",
            "variable screening",
            "factor recoding",
            "selecting levels factor variable",
            "subsetting continuous variable",
            "feature selection omitted variable bias",
            "variable categorization",
            "data type conversion",
            "variable discretization",
            "factor level selection",
            "continuous variable binning",
            "categorical encoding",
            "variable preprocessing"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} variable analysis terms"
        }
    
    def get_task1_structured_content(self) -> Dict:
        """
        Get structured content specifically organized for Task 1 requirements
        """
        return {
            'data_preparation_content': self.search_data_preparation_content(),
            'data_joins_content': self.search_data_joins_content(),
            'eda_content': self.search_eda_content(),
            'data_validation_content': self.search_data_validation_content(),
            'variable_analysis_content': self.search_variable_analysis_content(),
            'data_quality_guidelines': self.curriculum.get_data_quality_guidelines(),
            'curriculum_summary': self.curriculum.get_curriculum_summary()
        }
    
    def search_specific_task1_terms(self, terms: List[str]) -> Dict:
        """
        Search for specific Task 1 terms
        """
        results = {}
        for term in terms:
            search_result = self.curriculum.search_curriculum(term)
            results[term] = {
                'count': len(search_result['results']),
                'top_results': search_result['results'][:5] if search_result['results'] else []
            }
        return results
    
    def get_task1_requirements_content(self) -> Dict:
        """
        Get content specifically for Task 1 requirements (1a-1d)
        """
        requirements = {
            '1a_data_cleaning': {
                'search_terms': ['missing values', 'dimension reduction', 'factor variables', 'data cleaning'],
                'description': 'Data cleaning and preparation'
            },
            '1b_data_merging': {
                'search_terms': ['data joins', 'merging data', 'perfect matching', 'join operations'],
                'description': 'Merging files and handling joins'
            },
            '1c_target_variable': {
                'search_terms': ['target variable', 'binary target', 'ARREST', 'binary classification'],
                'description': 'Target variable preparation'
            },
            '1d_exploratory_analysis': {
                'search_terms': ['exploratory data analysis', 'EDA', 'data visualization', 'reasonability checks'],
                'description': 'Exploratory Data Analysis'
            }
        }
        
        results = {}
        for req_key, req_info in requirements.items():
            req_results = {}
            for term in req_info['search_terms']:
                search_result = self.curriculum.search_curriculum(term)
                if search_result['results']:
                    req_results[term] = search_result['results'][:2]  # Top 2 results
            results[req_key] = {
                'description': req_info['description'],
                'search_terms': req_info['search_terms'],
                'results': req_results,
                'summary': f"Found content for {len([r for r in req_results.values() if r])} terms"
            }
        
        return results

# Test function
def test_task1_search():
    """
    Test the Task 1 specialized search functionality
    """
    print("=== TASK 1 SPECIALIZED SEARCH TEST ===")
    
    task1_search = Task1SpecializedSearch()
    
    # Test data preparation search
    print("\n1. Testing Data Preparation Content Search...")
    prep_results = task1_search.search_data_preparation_content()
    print(f"✅ Found content for {len([r for r in prep_results['results'].values() if r])} data preparation terms")
    
    # Test data joins search
    print("\n2. Testing Data Joins Search...")
    joins_results = task1_search.search_data_joins_content()
    print(f"✅ Found content for {len([r for r in joins_results['results'].values() if r])} data joins terms")
    
    # Test EDA search
    print("\n3. Testing EDA Search...")
    eda_results = task1_search.search_eda_content()
    print(f"✅ Found content for {len([r for r in eda_results['results'].values() if r])} EDA terms")
    
    # Test data validation search
    print("\n4. Testing Data Validation Search...")
    validation_results = task1_search.search_data_validation_content()
    print(f"✅ Found content for {len([r for r in validation_results['results'].values() if r])} data validation terms")
    
    # Test variable analysis search
    print("\n5. Testing Variable Analysis Search...")
    var_results = task1_search.search_variable_analysis_content()
    print(f"✅ Found content for {len([r for r in var_results['results'].values() if r])} variable analysis terms")
    
    # Test specific Task 1 terms
    print("\n6. Testing Specific Task 1 Terms...")
    specific_terms = ["missing values", "data joins", "exploratory data analysis", "data validation"]
    specific_results = task1_search.search_specific_task1_terms(specific_terms)
    for term, result in specific_results.items():
        print(f"   {term}: {result['count']} results")
    
    # Test Task 1 requirements content
    print("\n7. Testing Task 1 Requirements Content...")
    requirements_results = task1_search.get_task1_requirements_content()
    for req_key, req_data in requirements_results.items():
        print(f"   {req_key}: {req_data['summary']}")
    
    print("\n🎉 Task 1 Specialized Search Test Completed Successfully!")

if __name__ == "__main__":
    test_task1_search() 