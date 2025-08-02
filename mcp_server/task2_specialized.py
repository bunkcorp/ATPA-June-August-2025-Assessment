#!/usr/bin/env python3
"""
Task 2 Specialized Module for ATPA MCP Server
Handles specific searches for demographic data, criminal justice, public policy, and professional standards
"""

from curriculum import ATPACurriculum
from typing import Dict, List, Optional
import re

class Task2SpecializedSearch:
    """
    Specialized search functionality for Task 2 requirements
    """
    
    def __init__(self):
        self.curriculum = ATPACurriculum()
        
    def search_demographic_data_benefits_risks(self) -> Dict:
        """
        Search for content specifically about benefits and risks of demographic data
        """
        search_terms = [
            "demographic",
            "race",
            "nationality", 
            "citizenship",
            "gender",
            "ethnicity",
            "bias",
            "discrimination",
            "fairness",
            "privacy",
            "protected classes",
            "victim",
            "offender",
            "criminal justice",
            "public policy",
            "anti-discrimination laws",
            "civil rights act",
            "equal credit opportunity act",
            "protected characteristics",
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
            "regulatory compliance",
            "data protection",
            "data privacy",
            "regulations on data",
            "united states regulations",
            "laws defining protected classes",
            "anti-discrimination laws regulations",
            "risk classification insurance",
            "discrimination insurance",
            "insurance laws united states",
            "guidelines principles predictive models",
            "data protection regulations",
            "privacy regulations",
            "insurance regulations",
            "predictive modeling guidelines",
            "modeling principles",
            "insurance risk classification",
            "discriminatory practices insurance",
            "protected class definitions",
            "regulatory framework",
            "compliance requirements",
            "data governance",
            "privacy protection",
            "insurance compliance"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} search terms"
        }
    
    def search_professional_standards_misuse_prevention(self) -> Dict:
        """
        Search for content about professional standards and misuse prevention
        """
        search_terms = [
            "ASOP 41",
            "ASOP 23", 
            "ASOP 56",
            "professional standards practice",
            "misuse prevention",
            "actuarial communications",
            "data quality standards",
            "modeling standards",
            "bias testing",
            "fairness assessment",
            "oversight mechanisms",
            "documentation standards",
            "transparency requirements",
            "ethical guidelines",
            "governance framework",
            "actuarial standards board",
            "professional responsibility",
            "ethical conduct",
            "actuarial professionalism",
            "standards of practice",
            "professional ethics",
            "actuarial code of conduct",
            "professional oversight",
            "ethical decision making",
            "professional accountability",
            "data protection standards",
            "privacy standards",
            "regulatory standards",
            "insurance standards",
            "predictive modeling standards",
            "modeling guidelines",
            "professional guidelines",
            "ethical modeling",
            "responsible modeling",
            "model governance",
            "data stewardship",
            "privacy protection standards",
            "regulatory compliance standards",
            "insurance compliance standards",
            "professional best practices",
            "ethical best practices"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} search terms"
        }
    
    def search_criminal_justice_specific(self) -> Dict:
        """
        Search for criminal justice specific content
        """
        search_terms = [
            "criminal justice",
            "law enforcement",
            "arrest patterns",
            "policing practices",
            "victim demographics",
            "offender demographics",
            "crime statistics",
            "justice system",
            "civil rights",
            "equal protection",
            "anti-discrimination",
            "racial profiling",
            "systemic bias",
            "community policing"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} search terms"
        }
    
    def get_task2_structured_content(self) -> Dict:
        """
        Get structured content specifically organized for Task 2 requirements
        """
        return {
            'task_2a_benefits_risks': self.search_demographic_data_benefits_risks(),
            'task_2b_professional_standards': self.search_professional_standards_misuse_prevention(),
            'criminal_justice_context': self.search_criminal_justice_specific(),
            'insurance_regulatory_content': self.search_insurance_regulatory_content(),
            'nminsights_guidance': self.get_nminsights_specific_guidance(),
            'ethical_framework': self.curriculum.get_ethical_framework_details(),
            'data_quality_guidelines': self.curriculum.get_data_quality_guidelines()
        }
    
    def search_specific_demographic_terms(self, terms: List[str]) -> Dict:
        """
        Search for specific demographic terms
        """
        results = {}
        for term in terms:
            search_result = self.curriculum.search_curriculum(term)
            results[term] = {
                'count': len(search_result['results']),
                'top_results': search_result['results'][:5] if search_result['results'] else []
            }
        return results
    
    def get_nminsights_specific_guidance(self) -> Dict:
        """
        Get specific guidance relevant to NMInsights as a trusted research organization
        """
        search_terms = [
            "trusted research organization",
            "impartial research",
            "public policy research",
            "research ethics",
            "data sensitivity",
            "policy recommendations",
            "research transparency",
            "stakeholder communication",
            "research governance",
            "independent review"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant guidance for {len([r for r in results.values() if r])} research organization terms"
        }
    
    def search_insurance_regulatory_content(self) -> Dict:
        """
        Search for content specifically about insurance regulations and data protection
        """
        search_terms = [
            "data protection",
            "data privacy",
            "regulations on data",
            "united states regulations",
            "laws defining protected classes",
            "anti-discrimination laws regulations",
            "risk classification insurance",
            "discrimination insurance",
            "insurance laws united states",
            "guidelines principles predictive models",
            "data protection regulations",
            "privacy regulations",
            "insurance regulations",
            "predictive modeling guidelines",
            "modeling principles",
            "insurance risk classification",
            "discriminatory practices insurance",
            "protected class definitions",
            "regulatory framework",
            "compliance requirements",
            "data governance",
            "privacy protection",
            "insurance compliance"
        ]
        
        results = {}
        for term in search_terms:
            search_result = self.curriculum.search_curriculum(term)
            if search_result['results']:
                results[term] = search_result['results'][:3]  # Top 3 results
        
        return {
            'search_terms': search_terms,
            'results': results,
            'summary': f"Found relevant content for {len([r for r in results.values() if r])} insurance regulatory terms"
        }

# Test function
def test_task2_search():
    """
    Test the Task 2 specialized search functionality
    """
    print("=== TASK 2 SPECIALIZED SEARCH TEST ===")
    
    task2_search = Task2SpecializedSearch()
    
    # Test demographic data search
    print("\n1. Testing Demographic Data Benefits/Risks Search...")
    demo_results = task2_search.search_demographic_data_benefits_risks()
    print(f"✅ Found content for {len([r for r in demo_results['results'].values() if r])} demographic terms")
    
    # Test professional standards search
    print("\n2. Testing Professional Standards Search...")
    prof_results = task2_search.search_professional_standards_misuse_prevention()
    print(f"✅ Found content for {len([r for r in prof_results['results'].values() if r])} professional standards terms")
    
    # Test criminal justice search
    print("\n3. Testing Criminal Justice Search...")
    cj_results = task2_search.search_criminal_justice_specific()
    print(f"✅ Found content for {len([r for r in cj_results['results'].values() if r])} criminal justice terms")
    
    # Test specific demographic terms
    print("\n4. Testing Specific Demographic Terms...")
    specific_terms = ["race", "nationality", "citizenship", "gender", "ethnicity"]
    specific_results = task2_search.search_specific_demographic_terms(specific_terms)
    for term, result in specific_results.items():
        print(f"   {term}: {result['count']} results")
    
    # Test NMInsights specific guidance
    print("\n5. Testing NMInsights Research Organization Guidance...")
    nminsights_results = task2_search.get_nminsights_specific_guidance()
    print(f"✅ Found guidance for {len([r for r in nminsights_results['results'].values() if r])} research organization terms")
    
    print("\n🎉 Task 2 Specialized Search Test Completed Successfully!")

if __name__ == "__main__":
    test_task2_search() 