#!/usr/bin/env python3
"""
Task 3 and 4 Curriculum Search
Extract key terms from Tasks 3 and 4 and search curriculum content
"""

from curriculum import ATPACurriculum

def search_task3_4_curriculum():
    print("=" * 80)
    print("TASK 3 & 4 CURRICULUM CONTENT SEARCH")
    print("=" * 80)
    
    curriculum = ATPACurriculum()
    
    # Task 3 specific terms
    task3_terms = {
        "3a_data_splitting": [
            "data splitting",
            "train test split", 
            "reasonability checks",
            "data splits",
            "training testing datasets",
            "stratified sampling"
        ],
        "3b_performance_measures": [
            "performance measures",
            "performance metrics",
            "model evaluation",
            "accuracy",
            "precision",
            "recall",
            "F1 score",
            "ROC curve",
            "AUC"
        ],
        "3c_generalized_linear_model": [
            "generalized linear model",
            "GLM",
            "logistic regression",
            "variable selection",
            "model tuning",
            "significant predictors",
            "coefficient interpretation",
            "odds ratio"
        ],
        "3d_linear_mixed_model": [
            "linear mixed model",
            "mixed model",
            "random effects",
            "fixed effects",
            "variance components",
            "model tuning",
            "significant predictors"
        ],
        "3e_model_recommendation": [
            "model comparison",
            "model selection",
            "recommendation",
            "best model"
        ]
    }
    
    # Task 4 specific terms
    task4_terms = {
        "4a_random_forest": [
            "random forest",
            "ensemble methods",
            "hyperparameters",
            "model tuning",
            "significant predictors"
        ],
        "4b_shapley_values": [
            "shapley values",
            "SHAP",
            "feature importance",
            "model interpretability",
            "individual predictions"
        ],
        "4c_partial_dependence": [
            "partial dependence plots",
            "partial dependence",
            "PDP",
            "predictor effects",
            "magnitude direction"
        ]
    }
    
    print("\n📋 TASK 3 REQUIREMENTS SEARCH")
    print("=" * 50)
    
    for section, terms in task3_terms.items():
        print(f"\n🔍 {section.upper()}:")
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            print(f"   {term}: {len(search_result['results'])} results")
            if search_result['results']:
                print(f"      Top result: {search_result['results'][0]['excerpt'][:80]}...")
    
    print("\n📋 TASK 4 REQUIREMENTS SEARCH")
    print("=" * 50)
    
    for section, terms in task4_terms.items():
        print(f"\n🔍 {section.upper()}:")
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            print(f"   {term}: {len(search_result['results'])} results")
            if search_result['results']:
                print(f"      Top result: {search_result['results'][0]['excerpt'][:80]}...")
    
    print("\n📋 ADDITIONAL MODELING TERMS SEARCH")
    print("=" * 50)
    
    additional_terms = [
        "ARREST",
        "target variable",
        "binary classification",
        "model fitting",
        "cross validation",
        "overfitting",
        "underfitting",
        "bias variance tradeoff",
        "model diagnostics",
        "residual analysis",
        "goodness of fit",
        "feature engineering",
        "multicollinearity",
        "stepwise selection",
        "forward selection",
        "backward elimination",
        "polynomial regression",
        "model complexity",
        "ensemble learning",
        "decision trees",
        "bagging",
        "boosting",
        "gradient boosting",
        "XGBoost",
        "LightGBM",
        "model interpretability",
        "feature importance",
        "permutation importance",
        "individual conditional expectation",
        "ICE plots"
    ]
    
    for term in additional_terms:
        search_result = curriculum.search_curriculum(term)
        if search_result['results']:
            print(f"   {term}: {len(search_result['results'])} results")
    
    print("\n📋 EXPLAINABILITY TECHNIQUES")
    print("=" * 50)
    
    explainability_techniques = curriculum.get_explainability_techniques()
    print(f"Module: {explainability_techniques['module']}")
    print(f"Available Techniques: {list(explainability_techniques['techniques'].keys())}")
    
    for technique, content in explainability_techniques['techniques'].items():
        if content:
            print(f"   {technique}: Available")
    
    print("\n📋 MODELING TECHNIQUES")
    print("=" * 50)
    
    modeling_techniques = curriculum.get_modeling_techniques()
    print(f"Module: {modeling_techniques['module']}")
    print(f"Available Techniques: {list(modeling_techniques['techniques'].keys())}")
    
    for technique, content in modeling_techniques['techniques'].items():
        if content:
            print(f"   {technique}: Available")
    
    print("\n" + "=" * 80)
    print("🎯 SUMMARY OF CURRICULUM COVERAGE")
    print("=" * 80)
    
    # Count total results for each task
    task3_total = 0
    task4_total = 0
    
    for section, terms in task3_terms.items():
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            task3_total += len(search_result['results'])
    
    for section, terms in task4_terms.items():
        for term in terms:
            search_result = curriculum.search_curriculum(term)
            task4_total += len(search_result['results'])
    
    print(f"Task 3 Total Results: {task3_total}")
    print(f"Task 4 Total Results: {task4_total}")
    print(f"Explainability Techniques: {len(explainability_techniques['techniques'])}")
    print(f"Modeling Techniques: {len(modeling_techniques['techniques'])}")

if __name__ == "__main__":
    search_task3_4_curriculum() 