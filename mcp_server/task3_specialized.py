#!/usr/bin/env python3
"""
Task 3 Specialized Module for ATPA MCP Server
Handles specific searches for Generalized Linear Models, mixed models, model validation, and other Task 3 requirements
"""

from curriculum import ATPACurriculum
from typing import Dict, List, Optional
import re

class Task3SpecializedSearch:
    """
    Specialized search functionality for Task 3 requirements
    """
    
    def __init__(self):
        self.curriculum = ATPACurriculum()
        
    def search_glm_content(self) -> Dict:
        """
        Search for content specifically about Generalized Linear Models
        """
        search_terms = [
            "generalized linear model",
            "GLM",
            "logistic regression",
            "linear regression",
            "regression model",
            "model fitting",
            "coefficient interpretation",
            "odds ratio",
            "link function",
            "exponential family",
            "generalized additive models",
            "GAM",
            "additive models",
            "smooth functions",
            "spline functions",
            "nonlinear relationships",
            "model interpretation",
            "variable effects",
            "predictor effects",
            "model coefficients",
            "log transformation",
            "model evaluation",
            "visualizing smooths",
            "multiple explanatory variables",
            "GAMs in GLMs"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} GLM terms"
        }
    
    def search_mixed_models_content(self) -> Dict:
        """
        Search for content about mixed models and random effects
        """
        search_terms = [
            "mixed model",
            "random effects",
            "fixed effects",
            "linear mixed model",
            "hierarchical model",
            "multilevel model",
            "variance components",
            "random intercept",
            "random slope",
            "intraclass correlation",
            "fixed versus random effects",
            "when to use random effects",
            "random intercepts model",
            "random slopes model",
            "prediction without random effect",
            "repeated measures",
            "longitudinal data",
            "generalized linear mixed model",
            "bühlmann straub credibility",
            "credibility theory",
            "mixed model interpretation",
            "random effects selection",
            "variance components analysis",
            "hierarchical modeling",
            "multilevel analysis"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} mixed model terms"
        }
    
    def search_model_validation_content(self) -> Dict:
        """
        Search for content about model validation and assessment
        """
        search_terms = [
            "model validation",
            "cross validation",
            "k-fold",
            "model assessment",
            "overfitting",
            "underfitting",
            "bias variance tradeoff",
            "model diagnostics",
            "residual analysis",
            "goodness of fit",
            "analytical accuracy",
            "model validation accuracy",
            "purposes of a model",
            "model workflow",
            "safety in analytics",
            "safety classification",
            "model evaluation",
            "validation procedures",
            "model assessment methods",
            "accuracy assessment",
            "model performance evaluation",
            "validation techniques",
            "model reliability",
            "model robustness"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} validation terms"
        }
    
    def search_variable_selection_content(self) -> Dict:
        """
        Search for content about variable selection and feature engineering
        """
        search_terms = [
            "variable selection",
            "feature selection",
            "stepwise selection",
            "forward selection",
            "backward elimination",
            "polynomial regression",
            "model complexity",
            "multicollinearity",
            "feature importance",
            "variable screening",
            "variable selection methods",
            "feature engineering",
            "predictor selection",
            "variable screening techniques",
            "model complexity management",
            "variable importance",
            "feature selection algorithms",
            "variable reduction",
            "dimensionality reduction",
            "variable screening procedures",
            "feature selection criteria",
            "variable selection criteria",
            "model parsimony",
            "variable screening methods"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} variable selection terms"
        }
    
    def search_performance_metrics_content(self) -> Dict:
        """
        Search for content about performance metrics and evaluation
        """
        search_terms = [
            "performance metrics",
            "accuracy",
            "precision",
            "recall",
            "F1 score",
            "ROC curve",
            "AUC",
            "confusion matrix",
            "classification metrics",
            "model evaluation"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} performance metric terms"
        }
    
    def get_task3_structured_content(self) -> Dict:
        """
        Get structured content specifically organized for Task 3 requirements
        """
        return {
            'data_splitting_content': self.search_data_splitting_content(),
            'glm_content': self.search_glm_content(),
            'mixed_models_content': self.search_mixed_models_content(),
            'model_validation_content': self.search_model_validation_content(),
            'variable_selection_content': self.search_variable_selection_content(),
            'performance_metrics_content': self.search_performance_metrics_content(),
            'modeling_techniques': self.curriculum.get_modeling_techniques(),
            'curriculum_summary': self.curriculum.get_curriculum_summary()
        }
    
    def search_specific_modeling_terms(self, terms: List[str]) -> Dict:
        """
        Search for specific modeling terms
        """
        results = {}
        for term in terms:
            search_result = self.curriculum.search_curriculum(term)
            results[term] = {
                'count': len(search_result['results']),
                'top_results': search_result['results'][:5] if search_result['results'] else []
            }
        return results
    
    def search_data_splitting_content(self) -> Dict:
        """
        Search for content about data splitting and reasonability checks
        """
        search_terms = [
            "data splitting",
            "train test split",
            "stratified sampling",
            "data partitioning",
            "training data",
            "testing data",
            "validation data",
            "reasonability checks",
            "data split validation",
            "split assessment",
            "data division",
            "sample splitting",
            "cross validation splits",
            "holdout validation",
            "data split evaluation",
            "split reasonability",
            "training testing validation",
            "data split assessment"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} data splitting terms"
        }
    
    def get_task3_requirements_content(self) -> Dict:
        """
        Get content specifically for Task 3 requirements (3a-3e)
        """
        requirements = {
            '3a_data_splitting': {
                'search_terms': ['data splitting', 'train test split', 'stratified sampling', 'reasonability checks'],
                'description': 'Data splitting and reasonability checks'
            },
            '3b_performance_measures': {
                'search_terms': ['performance measures', 'model evaluation', 'metrics selection', 'analytical accuracy'],
                'description': 'Performance measures selection and justification'
            },
            '3c_generalized_linear_model': {
                'search_terms': ['generalized linear model', 'logistic regression', 'variable selection', 'generalized additive models'],
                'description': 'GLM implementation and variable selection'
            },
            '3d_linear_mixed_model': {
                'search_terms': ['mixed model', 'random effects', 'linear mixed model', 'fixed versus random effects'],
                'description': 'Linear mixed model implementation'
            },
            '3e_model_recommendation': {
                'search_terms': ['model comparison', 'model selection', 'recommendation', 'model evaluation'],
                'description': 'Model comparison and recommendation'
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
def test_task3_search():
    """
    Test the Task 3 specialized search functionality
    """
    print("=== TASK 3 SPECIALIZED SEARCH TEST ===")
    
    task3_search = Task3SpecializedSearch()
    
    # Test GLM content search
    print("\n1. Testing GLM Content Search...")
    glm_results = task3_search.search_glm_content()
    print(f"✅ Found content for {len([r for r in glm_results['results'].values() if r])} GLM terms")
    
    # Test mixed models search
    print("\n2. Testing Mixed Models Search...")
    mixed_results = task3_search.search_mixed_models_content()
    print(f"✅ Found content for {len([r for r in mixed_results['results'].values() if r])} mixed model terms")
    
    # Test model validation search
    print("\n3. Testing Model Validation Search...")
    validation_results = task3_search.search_model_validation_content()
    print(f"✅ Found content for {len([r for r in validation_results['results'].values() if r])} validation terms")
    
    # Test variable selection search
    print("\n4. Testing Variable Selection Search...")
    selection_results = task3_search.search_variable_selection_content()
    print(f"✅ Found content for {len([r for r in selection_results['results'].values() if r])} variable selection terms")
    
    # Test performance metrics search
    print("\n5. Testing Performance Metrics Search...")
    metrics_results = task3_search.search_performance_metrics_content()
    print(f"✅ Found content for {len([r for r in metrics_results['results'].values() if r])} performance metric terms")
    
    # Test specific modeling terms
    print("\n6. Testing Specific Modeling Terms...")
    specific_terms = ["logistic regression", "polynomial regression", "stepwise selection", "cross validation"]
    specific_results = task3_search.search_specific_modeling_terms(specific_terms)
    for term, result in specific_results.items():
        print(f"   {term}: {result['count']} results")
    
    # Test Task 3 requirements content
    print("\n7. Testing Task 3 Requirements Content...")
    requirements_results = task3_search.get_task3_requirements_content()
    for req_key, req_data in requirements_results.items():
        print(f"   {req_key}: {req_data['summary']}")
    
    print("\n🎉 Task 3 Specialized Search Test Completed Successfully!")

if __name__ == "__main__":
    test_task3_search() 