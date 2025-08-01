"""
Ethics Layer: Incorporates ATPA Module 1 Data and Model Ethics framework
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class EthicsFramework:
    """
    Ethics Framework based on ATPA Module 1: Data and Model Ethics
    
    Core Principles:
    - Fairness: Impartial and just treatment without favoritism or discrimination
    - Safety: Protection from harm and ensuring beneficial outcomes  
    - Transparency and Accountability: Clear, explainable processes and responsible implementation
    """
    
    def __init__(self):
        """Initialize the ethics framework with ATPA guidelines"""
        self.protected_classes = {
            'race': ['race_desc', 'ethnicity_name'],
            'gender': ['sex_code', 'offender_sex_code', 'victim_sex_code'],
            'age': ['age_num', 'offender_age_num', 'victim_age_num'],
            'location': ['county_name', 'agency_name'],  # Potential proxy for socioeconomic status
            'residence': ['resident_code']
        }
        
        self.ethical_principles = {
            'fairness': {
                'description': 'Impartial and just treatment without favoritism or discrimination',
                'data_aspects': [
                    'Representative sampling',
                    'Bias detection in data collection',
                    'Protected class identification'
                ],
                'model_aspects': [
                    'Demographic parity testing',
                    'Equal opportunity assessment',
                    'Bias mitigation techniques'
                ],
                'implementation_aspects': [
                    'Regular bias audits',
                    'Stakeholder consultation',
                    'Impact monitoring'
                ]
            },
            'safety': {
                'description': 'Protection from harm and ensuring beneficial outcomes',
                'data_aspects': [
                    'Privacy protection',
                    'Data security',
                    'Informed consent considerations'
                ],
                'model_aspects': [
                    'Risk assessment',
                    'Harm prevention',
                    'Benefit maximization'
                ],
                'implementation_aspects': [
                    'Oversight mechanisms',
                    'Regular safety reviews',
                    'Emergency protocols'
                ]
            },
            'transparency': {
                'description': 'Clear, explainable processes and responsible implementation',
                'data_aspects': [
                    'Data source documentation',
                    'Collection methodology transparency',
                    'Limitations disclosure'
                ],
                'model_aspects': [
                    'Model interpretability',
                    'Decision rationale explanation',
                    'Assumption documentation'
                ],
                'implementation_aspects': [
                    'Clear communication',
                    'Stakeholder education',
                    'Regular reporting'
                ]
            }
        }
        
        self.regulations = {
            'data_protection': [
                'Health Insurance Portability and Accountability Act (HIPAA)',
                'General Data Protection Regulation (GDPR)',
                'California Consumer Privacy Act (CCPA)'
            ],
            'anti_discrimination': [
                'Civil Rights Act of 1964',
                'Fair Housing Act',
                'Equal Credit Opportunity Act'
            ],
            'actuarial_standards': [
                'ASOP No. 23 (Data Quality)',
                'ASOP No. 41 (Actuarial Communications)',
                'ASOP No. 56 (Modeling)'
            ]
        }
    
    def identify_protected_variables(self, df: pd.DataFrame) -> Dict:
        """Identify variables that may represent protected classes or proxies"""
        protected_vars = {}
        
        for protected_class, potential_vars in self.protected_classes.items():
            found_vars = []
            for var in potential_vars:
                if var in df.columns:
                    found_vars.append(var)
            
            if found_vars:
                protected_vars[protected_class] = found_vars
        
        return protected_vars
    
    def assess_data_bias(self, df: pd.DataFrame) -> Dict:
        """Assess potential biases in the dataset"""
        bias_assessment = {
            'selection_bias': self._assess_selection_bias(df),
            'measurement_bias': self._assess_measurement_bias(df),
            'representation_bias': self._assess_representation_bias(df),
            'protected_class_analysis': self._analyze_protected_classes(df)
        }
        
        return bias_assessment
    
    def _assess_selection_bias(self, df: pd.DataFrame) -> Dict:
        """Assess selection bias in the dataset"""
        assessment = {
            'missing_data_patterns': {},
            'geographic_coverage': {},
            'temporal_coverage': {},
            'agency_coverage': {}
        }
        
        # Check for systematic missing data
        missing_by_agency = df.groupby('agency_name').apply(lambda x: x.isnull().sum().sum())
        assessment['missing_data_patterns']['by_agency'] = missing_by_agency.to_dict()
        
        # Check geographic coverage
        if 'county_name' in df.columns:
            county_counts = df['county_name'].value_counts()
            assessment['geographic_coverage']['county_distribution'] = county_counts.to_dict()
        
        # Check temporal coverage
        if 'incident_date' in df.columns:
            df['year'] = df['incident_date'].dt.year
            year_counts = df['year'].value_counts().sort_index()
            assessment['temporal_coverage']['year_distribution'] = year_counts.to_dict()
        
        return assessment
    
    def _assess_measurement_bias(self, df: pd.DataFrame) -> Dict:
        """Assess measurement bias in the dataset"""
        assessment = {
            'data_quality_issues': {},
            'inconsistent_coding': {},
            'systematic_errors': {}
        }
        
        # Check for inconsistent coding in categorical variables
        categorical_vars = ['offense_category_name', 'crime_against', 'agency_name']
        for var in categorical_vars:
            if var in df.columns:
                unique_values = df[var].value_counts()
                assessment['inconsistent_coding'][var] = {
                    'unique_count': len(unique_values),
                    'top_values': unique_values.head(5).to_dict()
                }
        
        return assessment
    
    def _assess_representation_bias(self, df: pd.DataFrame) -> Dict:
        """Assess representation bias in the dataset"""
        assessment = {
            'demographic_representation': {},
            'geographic_representation': {},
            'temporal_representation': {}
        }
        
        # Analyze demographic representation
        if 'race_desc' in df.columns:
            race_dist = df['race_desc'].value_counts(normalize=True)
            assessment['demographic_representation']['race_distribution'] = race_dist.to_dict()
        
        if 'sex_code' in df.columns:
            sex_dist = df['sex_code'].value_counts(normalize=True)
            assessment['demographic_representation']['sex_distribution'] = sex_dist.to_dict()
        
        return assessment
    
    def _analyze_protected_classes(self, df: pd.DataFrame) -> Dict:
        """Analyze protected class variables and their relationships"""
        analysis = {}
        
        protected_vars = self.identify_protected_variables(df)
        
        for protected_class, variables in protected_vars.items():
            analysis[protected_class] = {}
            for var in variables:
                if var in df.columns:
                    # Basic statistics
                    value_counts = df[var].value_counts()
                    analysis[protected_class][var] = {
                        'unique_values': len(value_counts),
                        'distribution': value_counts.to_dict(),
                        'missing_count': df[var].isnull().sum(),
                        'missing_percentage': (df[var].isnull().sum() / len(df)) * 100
                    }
        
        return analysis
    
    def assess_model_fairness(self, df: pd.DataFrame, target_col: str = 'arrest') -> Dict:
        """Assess fairness metrics for the target variable"""
        fairness_metrics = {}
        
        protected_vars = self.identify_protected_variables(df)
        
        for protected_class, variables in protected_vars.items():
            fairness_metrics[protected_class] = {}
            
            for var in variables:
                if var in df.columns and target_col in df.columns:
                    # Calculate demographic parity
                    parity_metrics = self._calculate_demographic_parity(df, var, target_col)
                    fairness_metrics[protected_class][var] = parity_metrics
        
        return fairness_metrics
    
    def _calculate_demographic_parity(self, df: pd.DataFrame, protected_var: str, target_var: str) -> Dict:
        """Calculate demographic parity metrics"""
        metrics = {}
        
        # Group by protected variable and calculate arrest rates
        group_rates = df.groupby(protected_var)[target_var].agg(['count', 'sum', 'mean'])
        group_rates.columns = ['total_incidents', 'arrests', 'arrest_rate']
        
        # Calculate overall arrest rate
        overall_rate = df[target_var].mean()
        
        # Calculate parity ratios
        group_rates['parity_ratio'] = group_rates['arrest_rate'] / overall_rate
        
        # Identify potential bias (ratios far from 1.0)
        group_rates['bias_indicator'] = abs(group_rates['parity_ratio'] - 1.0)
        
        metrics['group_rates'] = group_rates.to_dict('index')
        metrics['overall_arrest_rate'] = overall_rate
        metrics['max_parity_deviation'] = group_rates['bias_indicator'].max()
        metrics['potential_bias_groups'] = group_rates[group_rates['bias_indicator'] > 0.2].index.tolist()
        
        return metrics
    
    def generate_ethical_recommendations(self, df: pd.DataFrame) -> Dict:
        """Generate ethical recommendations based on data analysis"""
        recommendations = {
            'data_collection': [],
            'model_development': [],
            'implementation': [],
            'monitoring': [],
            'documentation': []
        }
        
        # Analyze data for ethical concerns
        protected_vars = self.identify_protected_variables(df)
        bias_assessment = self.assess_data_bias(df)
        fairness_metrics = self.assess_model_fairness(df)
        
        # Data Collection Recommendations
        if len(protected_vars) > 0:
            recommendations['data_collection'].append({
                'concern': 'Protected class variables identified',
                'recommendation': 'Ensure data collection methods do not perpetuate existing biases',
                'priority': 'High'
            })
        
        # Model Development Recommendations
        if fairness_metrics:
            for protected_class, metrics in fairness_metrics.items():
                for var, var_metrics in metrics.items():
                    if var_metrics.get('max_parity_deviation', 0) > 0.2:
                        recommendations['model_development'].append({
                            'concern': f'Potential bias detected in {protected_class} ({var})',
                            'recommendation': 'Implement bias mitigation techniques and fairness constraints',
                            'priority': 'High'
                        })
        
        # Implementation Recommendations
        recommendations['implementation'].extend([
            {
                'concern': 'Criminal justice context',
                'recommendation': 'Establish independent oversight board for model deployment',
                'priority': 'Critical'
            },
            {
                'concern': 'High-stakes decisions',
                'recommendation': 'Implement human-in-the-loop review for model predictions',
                'priority': 'High'
            }
        ])
        
        # Monitoring Recommendations
        recommendations['monitoring'].extend([
            {
                'concern': 'Ongoing bias detection',
                'recommendation': 'Establish regular bias audits and fairness monitoring',
                'priority': 'High'
            },
            {
                'concern': 'Impact assessment',
                'recommendation': 'Monitor real-world impact of model predictions on communities',
                'priority': 'High'
            }
        ])
        
        # Documentation Recommendations
        recommendations['documentation'].extend([
            {
                'concern': 'Transparency requirements',
                'recommendation': 'Document all data sources, assumptions, and limitations',
                'priority': 'High'
            },
            {
                'concern': 'Stakeholder communication',
                'recommendation': 'Create clear, accessible documentation for all stakeholders',
                'priority': 'Medium'
            }
        ])
        
        return recommendations
    
    def create_ethical_summary(self, df: pd.DataFrame) -> Dict:
        """Create comprehensive ethical summary for the dataset"""
        summary = {
            'ethical_framework': {
                'principles': self.ethical_principles,
                'regulations': self.regulations
            },
            'data_assessment': {
                'protected_variables': self.identify_protected_variables(df),
                'bias_assessment': self.assess_data_bias(df),
                'fairness_metrics': self.assess_model_fairness(df)
            },
            'recommendations': self.generate_ethical_recommendations(df),
            'compliance_checklist': self._create_compliance_checklist(),
            'risk_assessment': self._assess_ethical_risks(df)
        }
        
        return summary
    
    def _create_compliance_checklist(self) -> Dict:
        """Create compliance checklist based on ATPA standards"""
        checklist = {
            'data_quality': [
                'Data sources are documented and reliable',
                'Data collection methods are transparent',
                'Missing data patterns are understood and documented',
                'Data limitations are clearly stated'
            ],
            'fairness': [
                'Protected classes are identified and monitored',
                'Bias detection methods are implemented',
                'Fairness metrics are regularly assessed',
                'Bias mitigation strategies are in place'
            ],
            'safety': [
                'Privacy protection measures are implemented',
                'Data security protocols are established',
                'Risk assessment has been conducted',
                'Harm prevention measures are in place'
            ],
            'transparency': [
                'Model methodology is documented',
                'Assumptions and limitations are clearly stated',
                'Decision rationale is explainable',
                'Stakeholder communication plan exists'
            ],
            'accountability': [
                'Oversight mechanisms are established',
                'Regular audits are scheduled',
                'Impact monitoring is implemented',
                'Grievance procedures are available'
            ]
        }
        
        return checklist
    
    def _assess_ethical_risks(self, df: pd.DataFrame) -> Dict:
        """Assess ethical risks associated with the dataset and analysis"""
        risks = {
            'high_risk': [],
            'medium_risk': [],
            'low_risk': []
        }
        
        # High-risk factors
        if 'race_desc' in df.columns or 'ethnicity_name' in df.columns:
            risks['high_risk'].append({
                'factor': 'Race/ethnicity data in criminal justice context',
                'concern': 'Potential for racial bias and discrimination',
                'mitigation': 'Implement strict bias monitoring and mitigation'
            })
        
        if 'county_name' in df.columns:
            risks['high_risk'].append({
                'factor': 'Geographic data as proxy for socioeconomic status',
                'concern': 'May perpetuate existing geographic disparities',
                'mitigation': 'Monitor for geographic bias and ensure fair representation'
            })
        
        # Medium-risk factors
        if 'age_num' in df.columns:
            risks['medium_risk'].append({
                'factor': 'Age data in criminal justice context',
                'concern': 'Potential age-based discrimination',
                'mitigation': 'Ensure age is not used inappropriately in predictions'
            })
        
        # Low-risk factors
        risks['low_risk'].append({
            'factor': 'General demographic data',
            'concern': 'Standard demographic analysis',
            'mitigation': 'Standard privacy and bias monitoring'
        })
        
        return risks 