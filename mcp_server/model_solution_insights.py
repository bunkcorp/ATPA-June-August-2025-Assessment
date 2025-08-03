#!/usr/bin/env python3
"""
Model Solution Analysis Module
Extracts specific patterns, language, and structure from ATPA model solutions
"""

import re
from typing import Dict, List, Any
from pathlib import Path

class ModelSolutionAnalyzer:
    """
    Analyzes ATPA model solution documents to extract:
    - Header and subheader patterns
    - Metrics and functions used
    - Test results and comparisons
    - Shapes, theorems, fitting, transforming, weighting
    - Commentary on predictors
    - Residual plots, starting/final models, effects
    - Converting to random intercepts, benefits, factor levels
    - Impacts, comparables, distinguish
    - Bayesian models, brm() function, sampling, chains, iterations
    - Parameter distributions, uncertainty of predictions
    - Family-specific parameters, NUTS, standard deviation
    - Bayesian point estimates
    - Distinction between random forest and GLM
    - Stacked model challenges and training/test sets
    - Partial dependence plots, variable importance
    - Executive summary structure (business problem, data overview, etc.)
    """
    
    def __init__(self, model_solution_path: str = None):
        self.model_solution_path = model_solution_path or "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA Sample Assessment - Model Solution.md"
        self.content = self._load_content()
        
    def _load_content(self) -> str:
        """Load the model solution content"""
        try:
            with open(self.model_solution_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
    
    def extract_header_patterns(self) -> Dict[str, List[str]]:
        """Extract header and subheader patterns"""
        headers = {
            'main_sections': [],
            'subsections': [],
            'task_headers': [],
            'executive_summary_sections': []
        }
        
        # Main section patterns
        main_patterns = [
            r'^#+\s*(Business Problem)',
            r'^#+\s*(Data Overview)',
            r'^#+\s*(Modeling Overview)',
            r'^#+\s*(Model Results)',
            r'^#+\s*(Next Steps)',
            r'^#+\s*(Task \d+)',
            r'^#+\s*(General Information)',
            r'^#+\s*(File List)'
        ]
        
        # Executive summary section patterns
        exec_patterns = [
            r'Business Problem',
            r'Data Overview', 
            r'Modeling Overview',
            r'Model Results:',
            r'Next Steps'
        ]
        
        lines = self.content.split('\n')
        for line in lines:
            # Main sections
            for pattern in main_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    headers['main_sections'].append(line.strip())
                    break
            
            # Executive summary sections
            for pattern in exec_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    headers['executive_summary_sections'].append(line.strip())
                    break
            
            # Task headers
            if re.search(r'Task \d+', line, re.IGNORECASE):
                headers['task_headers'].append(line.strip())
            
            # Subsections (## or ###)
            if re.match(r'^#{2,3}\s+', line):
                headers['subsections'].append(line.strip())
        
        return headers
    
    def extract_metrics_and_functions(self) -> Dict[str, List[str]]:
        """Extract metrics, functions, and test results"""
        metrics = {
            'performance_metrics': [],
            'functions_used': [],
            'test_results': [],
            'comparisons': []
        }
        
        # Performance metrics
        metric_patterns = [
            r'RMSE',
            r'root mean square error',
            r'accuracy',
            r'precision',
            r'recall',
            r'F1 score',
            r'AUC',
            r'ROC curve',
            r'confusion matrix',
            r'log-likelihood',
            r'R-squared',
            r'adjusted R-squared',
            r'AIC',
            r'BIC'
        ]
        
        # Functions used
        function_patterns = [
            r'brm\(\)',
            r'glm\(\)',
            r'glmm\(\)',
            r'randomForest\(\)',
            r'stan\(\)',
            r'brms\(\)',
            r'predict\(\)',
            r'plot\(\)',
            r'summary\(\)',
            r'confint\(\)',
            r'vcov\(\)',
            r'residuals\(\)',
            r'fitted\(\)',
            r'coef\(\)'
        ]
        
        # Test results patterns
        test_patterns = [
            r'test.*result',
            r'validation.*result',
            r'cross.*validation',
            r'out.*of.*sample',
            r'holdout.*test',
            r'performance.*on.*test',
            r'prediction.*accuracy'
        ]
        
        # Comparison patterns
        comparison_patterns = [
            r'compare.*model',
            r'versus',
            r'compared.*to',
            r'better.*than',
            r'worse.*than',
            r'superior.*to',
            r'inferior.*to',
            r'difference.*between',
            r'similar.*to',
            r'distinct.*from'
        ]
        
        content_lower = self.content.lower()
        
        for pattern in metric_patterns:
            if re.search(pattern, content_lower):
                metrics['performance_metrics'].append(pattern)
        
        for pattern in function_patterns:
            if re.search(pattern, content_lower):
                metrics['functions_used'].append(pattern)
        
        for pattern in test_patterns:
            if re.search(pattern, content_lower):
                metrics['test_results'].append(pattern)
        
        for pattern in comparison_patterns:
            if re.search(pattern, content_lower):
                metrics['comparisons'].append(pattern)
        
        return metrics
    
    def extract_modeling_concepts(self) -> Dict[str, List[str]]:
        """Extract modeling concepts and terminology"""
        concepts = {
            'shapes_theorems': [],
            'fitting_transforming': [],
            'weighting': [],
            'predictor_commentary': [],
            'residual_plots': [],
            'starting_final_models': [],
            'effects': [],
            'random_intercepts': [],
            'benefits_factor_levels': [],
            'impacts_comparables': []
        }
        
        # Shapes and theorems
        shape_patterns = [
            r'normal.*distribution',
            r'log.*normal',
            r'gamma.*distribution',
            r'poisson.*distribution',
            r'binomial.*distribution',
            r'beta.*distribution',
            r'central.*limit.*theorem',
            r'law.*of.*large.*numbers',
            r'bayes.*theorem',
            r'likelihood.*ratio'
        ]
        
        # Fitting and transforming
        fit_patterns = [
            r'model.*fitting',
            r'fit.*model',
            r'transform.*variable',
            r'log.*transform',
            r'square.*root.*transform',
            r'polynomial.*transform',
            r'spline.*function',
            r'smooth.*function',
            r'link.*function',
            r'generalized.*linear.*model'
        ]
        
        # Weighting
        weight_patterns = [
            r'weight.*model',
            r'weighted.*analysis',
            r'importance.*weight',
            r'sample.*weight',
            r'frequency.*weight',
            r'probability.*weight'
        ]
        
        # Predictor commentary
        predictor_patterns = [
            r'significant.*predictor',
            r'important.*variable',
            r'key.*factor',
            r'primary.*driver',
            r'secondary.*effect',
            r'interaction.*effect',
            r'main.*effect',
            r'confounding.*variable',
            r'collinear.*variable'
        ]
        
        # Residual plots
        residual_patterns = [
            r'residual.*plot',
            r'residual.*analysis',
            r'residual.*diagnostic',
            r'residual.*check',
            r'residual.*pattern',
            r'residual.*distribution'
        ]
        
        # Starting and final models
        model_patterns = [
            r'starting.*model',
            r'initial.*model',
            r'final.*model',
            r'baseline.*model',
            r'null.*model',
            r'reference.*model',
            r'improved.*model',
            r'optimized.*model'
        ]
        
        # Effects
        effect_patterns = [
            r'fixed.*effect',
            r'random.*effect',
            r'interaction.*effect',
            r'main.*effect',
            r'marginal.*effect',
            r'conditional.*effect',
            r'direct.*effect',
            r'indirect.*effect'
        ]
        
        # Random intercepts
        intercept_patterns = [
            r'random.*intercept',
            r'convert.*to.*random',
            r'mixed.*effect',
            r'hierarchical.*model',
            r'multilevel.*model',
            r'variance.*component'
        ]
        
        # Benefits and factor levels
        benefit_patterns = [
            r'benefit.*of',
            r'advantage.*of',
            r'improvement.*from',
            r'factor.*level',
            r'categorical.*level',
            r'reference.*level',
            r'baseline.*level'
        ]
        
        # Impacts and comparables
        impact_patterns = [
            r'impact.*on',
            r'effect.*on',
            r'influence.*on',
            r'contribution.*to',
            r'comparable.*to',
            r'similar.*to',
            r'distinguish.*from',
            r'different.*from'
        ]
        
        content_lower = self.content.lower()
        
        for pattern in shape_patterns:
            if re.search(pattern, content_lower):
                concepts['shapes_theorems'].append(pattern)
        
        for pattern in fit_patterns:
            if re.search(pattern, content_lower):
                concepts['fitting_transforming'].append(pattern)
        
        for pattern in weight_patterns:
            if re.search(pattern, content_lower):
                concepts['weighting'].append(pattern)
        
        for pattern in predictor_patterns:
            if re.search(pattern, content_lower):
                concepts['predictor_commentary'].append(pattern)
        
        for pattern in residual_patterns:
            if re.search(pattern, content_lower):
                concepts['residual_plots'].append(pattern)
        
        for pattern in model_patterns:
            if re.search(pattern, content_lower):
                concepts['starting_final_models'].append(pattern)
        
        for pattern in effect_patterns:
            if re.search(pattern, content_lower):
                concepts['effects'].append(pattern)
        
        for pattern in intercept_patterns:
            if re.search(pattern, content_lower):
                concepts['random_intercepts'].append(pattern)
        
        for pattern in benefit_patterns:
            if re.search(pattern, content_lower):
                concepts['benefits_factor_levels'].append(pattern)
        
        for pattern in impact_patterns:
            if re.search(pattern, content_lower):
                concepts['impacts_comparables'].append(pattern)
        
        return concepts
    
    def extract_bayesian_content(self) -> Dict[str, List[str]]:
        """Extract Bayesian modeling content"""
        bayesian = {
            'bayesian_models': [],
            'brm_function': [],
            'sampling_chains': [],
            'parameter_distributions': [],
            'uncertainty': [],
            'family_parameters': [],
            'nuts_algorithm': [],
            'standard_deviation': [],
            'bayesian_point_estimates': []
        }
        
        # Bayesian models
        bayesian_patterns = [
            r'bayesian.*model',
            r'bayes.*rule',
            r'prior.*distribution',
            r'posterior.*distribution',
            r'likelihood.*function',
            r'bayesian.*inference',
            r'bayesian.*analysis'
        ]
        
        # BRM function
        brm_patterns = [
            r'brm\(\)',
            r'brms.*package',
            r'bayesian.*regression',
            r'bayesian.*mixed.*model'
        ]
        
        # Sampling and chains
        sampling_patterns = [
            r'markov.*chain.*monte.*carlo',
            r'MCMC',
            r'gibbs.*sampler',
            r'metropolis.*hastings',
            r'hamiltonian.*monte.*carlo',
            r'chains',
            r'iterations',
            r'burn.*in',
            r'convergence'
        ]
        
        # Parameter distributions
        param_patterns = [
            r'parameter.*distribution',
            r'posterior.*distribution',
            r'prior.*distribution',
            r'credible.*interval',
            r'confidence.*interval',
            r'parameter.*uncertainty'
        ]
        
        # Uncertainty
        uncertainty_patterns = [
            r'uncertainty.*of.*prediction',
            r'prediction.*uncertainty',
            r'parameter.*uncertainty',
            r'posterior.*uncertainty',
            r'credible.*interval',
            r'confidence.*interval'
        ]
        
        # Family-specific parameters
        family_patterns = [
            r'family.*specific.*parameter',
            r'gaussian.*family',
            r'poisson.*family',
            r'binomial.*family',
            r'gamma.*family',
            r'exponential.*family'
        ]
        
        # NUTS algorithm
        nuts_patterns = [
            r'NUTS',
            r'no.*u.*turn.*sampler',
            r'hamiltonian.*monte.*carlo',
            r'HMC'
        ]
        
        # Standard deviation
        sd_patterns = [
            r'standard.*deviation',
            r'std.*dev',
            r'variance',
            r'standard.*error'
        ]
        
        # Bayesian point estimates
        point_patterns = [
            r'bayesian.*point.*estimate',
            r'posterior.*mean',
            r'posterior.*median',
            r'posterior.*mode',
            r'map.*estimate'
        ]
        
        content_lower = self.content.lower()
        
        for pattern in bayesian_patterns:
            if re.search(pattern, content_lower):
                bayesian['bayesian_models'].append(pattern)
        
        for pattern in brm_patterns:
            if re.search(pattern, content_lower):
                bayesian['brm_function'].append(pattern)
        
        for pattern in sampling_patterns:
            if re.search(pattern, content_lower):
                bayesian['sampling_chains'].append(pattern)
        
        for pattern in param_patterns:
            if re.search(pattern, content_lower):
                bayesian['parameter_distributions'].append(pattern)
        
        for pattern in uncertainty_patterns:
            if re.search(pattern, content_lower):
                bayesian['uncertainty'].append(pattern)
        
        for pattern in family_patterns:
            if re.search(pattern, content_lower):
                bayesian['family_parameters'].append(pattern)
        
        for pattern in nuts_patterns:
            if re.search(pattern, content_lower):
                bayesian['nuts_algorithm'].append(pattern)
        
        for pattern in sd_patterns:
            if re.search(pattern, content_lower):
                bayesian['standard_deviation'].append(pattern)
        
        for pattern in point_patterns:
            if re.search(pattern, content_lower):
                bayesian['bayesian_point_estimates'].append(pattern)
        
        return bayesian
    
    def extract_model_comparisons(self) -> Dict[str, List[str]]:
        """Extract model comparison content"""
        comparisons = {
            'random_forest_vs_glm': [],
            'stacked_model_challenges': [],
            'training_test_sets': [],
            'partial_dependence_plots': [],
            'variable_importance': []
        }
        
        # Random Forest vs GLM distinctions
        rf_glm_patterns = [
            r'random.*forest.*versus.*glm',
            r'glm.*versus.*random.*forest',
            r'distinction.*between.*random.*forest.*and.*glm',
            r'difference.*between.*random.*forest.*and.*glm',
            r'random.*forest.*compared.*to.*glm',
            r'glm.*compared.*to.*random.*forest'
        ]
        
        # Stacked model challenges
        stacked_patterns = [
            r'stacked.*model.*challenge',
            r'stacking.*difficulty',
            r'two.*stage.*model',
            r'managing.*training.*and.*test.*sets',
            r'overfitting.*in.*stacking',
            r'benefit.*from.*stacking'
        ]
        
        # Training and test sets
        train_test_patterns = [
            r'training.*set',
            r'test.*set',
            r'validation.*set',
            r'holdout.*set',
            r'data.*splitting',
            r'cross.*validation',
            r'out.*of.*sample'
        ]
        
        # Partial dependence plots
        pdp_patterns = [
            r'partial.*dependence.*plot',
            r'PDP',
            r'partial.*dependence',
            r'dependence.*plot',
            r'marginal.*effect.*plot'
        ]
        
        # Variable importance
        importance_patterns = [
            r'variable.*importance',
            r'feature.*importance',
            r'predictor.*importance',
            r'importance.*score',
            r'relative.*importance'
        ]
        
        content_lower = self.content.lower()
        
        for pattern in rf_glm_patterns:
            if re.search(pattern, content_lower):
                comparisons['random_forest_vs_glm'].append(pattern)
        
        for pattern in stacked_patterns:
            if re.search(pattern, content_lower):
                comparisons['stacked_model_challenges'].append(pattern)
        
        for pattern in train_test_patterns:
            if re.search(pattern, content_lower):
                comparisons['training_test_sets'].append(pattern)
        
        for pattern in pdp_patterns:
            if re.search(pattern, content_lower):
                comparisons['partial_dependence_plots'].append(pattern)
        
        for pattern in importance_patterns:
            if re.search(pattern, content_lower):
                comparisons['variable_importance'].append(pattern)
        
        return comparisons
    
    def extract_executive_summary_structure(self) -> Dict[str, List[str]]:
        """Extract executive summary structure and content"""
        executive = {
            'business_problem': [],
            'data_overview': [],
            'modeling_overview': [],
            'model_results': [],
            'next_steps': [],
            'titles_and_headers': []
        }
        
        # Business problem
        business_patterns = [
            r'business.*problem',
            r'problem.*statement',
            r'objective',
            r'goal',
            r'purpose',
            r'context'
        ]
        
        # Data overview
        data_patterns = [
            r'data.*overview',
            r'data.*description',
            r'data.*summary',
            r'dataset.*description',
            r'data.*source',
            r'data.*quality'
        ]
        
        # Modeling overview
        modeling_patterns = [
            r'modeling.*overview',
            r'model.*description',
            r'modeling.*approach',
            r'methodology',
            r'analysis.*approach'
        ]
        
        # Model results
        results_patterns = [
            r'model.*results',
            r'results.*summary',
            r'findings',
            r'conclusions',
            r'key.*findings',
            r'main.*results'
        ]
        
        # Next steps
        steps_patterns = [
            r'next.*steps',
            r'recommendations',
            r'future.*work',
            r'follow.*up',
            r'action.*items'
        ]
        
        # Titles and headers
        title_patterns = [
            r'^#+\s*(.*)',
            r'^[A-Z][A-Za-z\s]+:',
            r'^[A-Z][A-Za-z\s]+$'
        ]
        
        content_lower = self.content.lower()
        
        for pattern in business_patterns:
            if re.search(pattern, content_lower):
                executive['business_problem'].append(pattern)
        
        for pattern in data_patterns:
            if re.search(pattern, content_lower):
                executive['data_overview'].append(pattern)
        
        for pattern in modeling_patterns:
            if re.search(pattern, content_lower):
                executive['modeling_overview'].append(pattern)
        
        for pattern in results_patterns:
            if re.search(pattern, content_lower):
                executive['model_results'].append(pattern)
        
        for pattern in steps_patterns:
            if re.search(pattern, content_lower):
                executive['next_steps'].append(pattern)
        
        # Extract actual titles and headers
        lines = self.content.split('\n')
        for line in lines:
            if re.match(r'^#+\s+', line):
                executive['titles_and_headers'].append(line.strip())
            elif re.match(r'^[A-Z][A-Za-z\s]+:', line):
                executive['titles_and_headers'].append(line.strip())
        
        return executive
    
    def get_comprehensive_analysis(self) -> Dict[str, Any]:
        """Get comprehensive analysis of the model solution"""
        return {
            'header_patterns': self.extract_header_patterns(),
            'metrics_and_functions': self.extract_metrics_and_functions(),
            'modeling_concepts': self.extract_modeling_concepts(),
            'bayesian_content': self.extract_bayesian_content(),
            'model_comparisons': self.extract_model_comparisons(),
            'executive_summary_structure': self.extract_executive_summary_structure(),
            'summary': {
                'total_sections': len(self.extract_header_patterns()['main_sections']),
                'total_metrics': len(self.extract_metrics_and_functions()['performance_metrics']),
                'total_functions': len(self.extract_metrics_and_functions()['functions_used']),
                'total_bayesian_terms': len(self.extract_bayesian_content()['bayesian_models']),
                'total_comparisons': len(self.extract_model_comparisons()['random_forest_vs_glm'])
            }
        }

# Test function
def test_model_solution_analysis():
    """Test the model solution analyzer"""
    analyzer = ModelSolutionAnalyzer()
    analysis = analyzer.get_comprehensive_analysis()
    
    print("=== MODEL SOLUTION ANALYSIS RESULTS ===")
    
    print(f"\n📊 Summary:")
    print(f"   Total sections: {analysis['summary']['total_sections']}")
    print(f"   Total metrics: {analysis['summary']['total_metrics']}")
    print(f"   Total functions: {analysis['summary']['total_functions']}")
    print(f"   Total Bayesian terms: {analysis['summary']['total_bayesian_terms']}")
    print(f"   Total comparisons: {analysis['summary']['total_comparisons']}")
    
    print(f"\n📋 Executive Summary Structure:")
    for section, patterns in analysis['executive_summary_structure'].items():
        if patterns:
            print(f"   {section}: {len(patterns)} patterns found")
    
    print(f"\n🔧 Metrics and Functions:")
    for category, items in analysis['metrics_and_functions'].items():
        if items:
            print(f"   {category}: {len(items)} items found")
    
    print(f"\n📈 Modeling Concepts:")
    for category, items in analysis['modeling_concepts'].items():
        if items:
            print(f"   {category}: {len(items)} concepts found")
    
    print(f"\n🎯 Bayesian Content:")
    for category, items in analysis['bayesian_content'].items():
        if items:
            print(f"   {category}: {len(items)} terms found")
    
    print(f"\n🔄 Model Comparisons:")
    for category, items in analysis['model_comparisons'].items():
        if items:
            print(f"   {category}: {len(items)} comparisons found")
    
    print("\n✅ Model Solution Analysis Complete!")

if __name__ == "__main__":
    test_model_solution_analysis() 

