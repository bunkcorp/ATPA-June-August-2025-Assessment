#!/usr/bin/env python3
"""
Test Advanced Modeling Content Coverage
"""

from task3_specialized import Task3SpecializedSearch

def test_advanced_modeling():
    print("=" * 60)
    print("ADVANCED MODELING CONTENT COVERAGE TEST")
    print("=" * 60)
    
    task3_search = Task3SpecializedSearch()
    
    # Test advanced modeling content
    advanced_results = task3_search.search_advanced_modeling_content()
    
    print(f"✅ Advanced Modeling: {len([r for r in advanced_results['results'].values() if r])} terms with content")
    
    # Show specific advanced modeling content found
    print("\n🔍 SPECIFIC ADVANCED MODELING CONTENT FOUND:")
    advanced_terms = [
        "binary classification", "neural networks", "overfitting",
        "predictions comparison", "one-hot encoding", "model comparison",
        "bayesian models", "bayesian analysis", "bayes rule",
        "poisson gamma", "markov chain monte carlo", "MCMC",
        "stan", "model diagnostics", "bayesian linear regression",
        "brms", "horseshoe prior", "count data", "model selection",
        "model evaluation", "stacking"
    ]
    
    found_count = 0
    for term in advanced_terms:
        search_result = task3_search.curriculum.search_curriculum(term)
        if search_result['results']:
            found_count += 1
            print(f"   ✅ {term}: {len(search_result['results'])} results")
    
    print(f"\n📊 Advanced Modeling Content Found: {found_count}/{len(advanced_terms)} terms")
    
    print("\n🎯 WHERE TO USE THIS CONTENT:")
    print("   • Task 3c (GLM): Binary classification, one-hot encoding, overfitting")
    print("   • Task 3e (Model Recommendation): Model comparison, predictions comparison")
    print("   • Advanced Alternatives: Bayesian models, neural networks, MCMC")
    print("   • Model Diagnostics: Model evaluation, diagnostics, selection")

if __name__ == "__main__":
    test_advanced_modeling() 