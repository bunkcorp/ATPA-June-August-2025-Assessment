"""
Professional Resources Layer: Integrates SHAP analysis, executive summary templates, and ASOP standards
"""
import os
import re
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class ProfessionalResources:
    """
    Professional Resources - Provides SHAP analysis, executive summary templates, and ASOP standards
    
    Documents:
    - 4.3_jobaid_shapley_values.md: SHAP analysis methodology and interpretation
    - 4.4_executive_summary.md: Executive summary template and structure
    - asop041_120.md: ASOP 41 Actuarial Communications standards
    """
    
    def __init__(self, resources_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        """
        Initialize professional resources with path to documents
        
        Args:
            resources_path: Path to resources directory
        """
        self.resources_path = resources_path
        self.resources = {
            'shap_analysis': {
                'title': 'SHAP Analysis Guide',
                'file': '4.3_jobaid_shapley_values.md',
                'type': 'technical_guide',
                'category': 'model_interpretation',
                'key_topics': ['shapley_values', 'shap', 'feature_importance', 'model_explanation']
            },
            'executive_summary': {
                'title': 'Executive Summary Template',
                'file': '4.4_executive_summary.md',
                'type': 'template',
                'category': 'communication',
                'key_topics': ['executive_summary', 'business_communication', 'non_technical_audience']
            },
            'asop_41': {
                'title': 'ASOP 41 Actuarial Communications',
                'file': 'asop041_120.md',
                'type': 'professional_standard',
                'category': 'compliance',
                'key_topics': ['actuarial_communications', 'professional_standards', 'disclosure_requirements']
            }
        }
        
        self.content = {}
        self.analysis_results = {}
        self._load_resources()
        self._analyze_content()
    
    def _load_resources(self):
        """Load content from all professional resource documents"""
        for resource_key, resource_info in self.resources.items():
            file_path = os.path.join(self.resources_path, resource_info['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.content[resource_key] = {
                        'content': content,
                        'sections': self._extract_sections(content),
                        'key_concepts': self._extract_key_concepts(content, resource_info['key_topics']),
                        'examples': self._extract_examples(content),
                        'guidelines': self._extract_guidelines(content)
                    }
                logger.info(f"Loaded {resource_info['title']} successfully")
            except Exception as e:
                logger.error(f"Error loading {resource_info['title']}: {e}")
                self.content[resource_key] = {
                    'content': f"Error loading document: {e}",
                    'sections': [],
                    'key_concepts': [],
                    'examples': [],
                    'guidelines': []
                }
    
    def _extract_sections(self, content: str) -> List[Dict]:
        """Extract section information from content"""
        sections = []
        
        # Look for section headers
        section_patterns = [
            r'Section (\d+)[\.\s]+([^\n]+)',
            r'(\d+\.\d+)[\s]+([^\n]+)',
            r'([A-Z][A-Z\s]+)[\n\r]',
            r'([A-Z][a-z\s]+)[\n\r]'
        ]
        
        for pattern in section_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                if len(match.groups()) >= 2:
                    sections.append({
                        'number': match.group(1),
                        'title': match.group(2).strip(),
                        'content': self._get_section_content(content, match.start())
                    })
                else:
                    sections.append({
                        'title': match.group(1).strip(),
                        'content': self._get_section_content(content, match.start())
                    })
        
        return sections[:10]  # Limit to first 10 sections
    
    def _get_section_content(self, content: str, start_pos: int) -> str:
        """Get content for a section starting at given position"""
        # Get next 500 characters as section content
        end_pos = min(start_pos + 500, len(content))
        return content[start_pos:end_pos].strip()
    
    def _extract_key_concepts(self, content: str, topics: List[str]) -> Dict:
        """Extract key concepts related to specified topics"""
        concepts = {}
        
        for topic in topics:
            topic_patterns = {
                'shapley_values': [r'shapley value', r'contribution', r'marginal impact'],
                'shap': [r'shap', r'shapley additive explanations', r'local interpretability'],
                'feature_importance': [r'feature.*importance', r'variable.*contribution', r'predictor.*impact'],
                'model_explanation': [r'model.*explanation', r'interpretability', r'explain.*model'],
                'executive_summary': [r'executive summary', r'business.*summary', r'executive.*report'],
                'business_communication': [r'business.*communication', r'non.*technical', r'stakeholder'],
                'non_technical_audience': [r'non.*technical', r'business.*audience', r'executive.*audience'],
                'actuarial_communications': [r'actuarial.*communication', r'actuarial.*report', r'actuarial.*document'],
                'professional_standards': [r'professional.*standard', r'actuarial.*standard', r'asop'],
                'disclosure_requirements': [r'disclosure', r'requirement', r'standard.*practice']
            }
            
            if topic in topic_patterns:
                patterns = topic_patterns[topic]
                matches = []
                for pattern in patterns:
                    found = re.findall(pattern, content, re.IGNORECASE)
                    matches.extend(found)
                concepts[topic] = list(set(matches))
        
        return concepts
    
    def _extract_examples(self, content: str) -> List[str]:
        """Extract examples and case studies from content"""
        examples = []
        
        # Look for example patterns
        example_patterns = [
            r'example[:\s]+([^.\n]+)',
            r'for example[,\s]+([^.\n]+)',
            r'such as[:\s]+([^.\n]+)',
            r'illustrate[:\s]+([^.\n]+)',
            r'case study[:\s]+([^.\n]+)'
        ]
        
        for pattern in example_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            examples.extend(matches)
        
        return examples[:10]  # Limit to first 10 examples
    
    def _extract_guidelines(self, content: str) -> List[str]:
        """Extract guidelines and best practices from content"""
        guidelines = []
        
        # Look for guideline patterns
        guideline_patterns = [
            r'should[:\s]+([^.\n]+)',
            r'must[:\s]+([^.\n]+)',
            r'recommend[:\s]+([^.\n]+)',
            r'best practice[:\s]+([^.\n]+)',
            r'guideline[:\s]+([^.\n]+)',
            r'requirement[:\s]+([^.\n]+)'
        ]
        
        for pattern in guideline_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            guidelines.extend(matches)
        
        return guidelines[:15]  # Limit to first 15 guidelines
    
    def _analyze_content(self):
        """Analyze content across all resources"""
        self.analysis_results = {
            'shap_insights': self._analyze_shap_content(),
            'executive_summary_insights': self._analyze_executive_summary_content(),
            'asop_insights': self._analyze_asop_content(),
            'cross_references': self._find_cross_references()
        }
    
    def _analyze_shap_content(self) -> Dict:
        """Analyze SHAP analysis content"""
        if 'shap_analysis' not in self.content:
            return {}
        
        content = self.content['shap_analysis']['content']
        
        insights = {
            'methodology': [],
            'interpretation_guidelines': [],
            'business_applications': [],
            'technical_requirements': []
        }
        
        # Extract methodology insights
        methodology_patterns = [
            r'shapley.*value.*calculation',
            r'marginal.*contribution',
            r'feature.*importance.*calculation',
            r'permutation.*analysis'
        ]
        
        for pattern in methodology_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['methodology'].extend(matches)
        
        # Extract interpretation guidelines
        interpretation_patterns = [
            r'interpret.*shap',
            r'explain.*prediction',
            r'feature.*interpretation',
            r'business.*insight'
        ]
        
        for pattern in interpretation_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['interpretation_guidelines'].extend(matches)
        
        return insights
    
    def _analyze_executive_summary_content(self) -> Dict:
        """Analyze executive summary content"""
        if 'executive_summary' not in self.content:
            return {}
        
        content = self.content['executive_summary']['content']
        
        insights = {
            'structure_elements': [],
            'writing_style': [],
            'business_focus': [],
            'technical_translation': []
        }
        
        # Extract structure elements
        structure_patterns = [
            r'executive.*summary.*structure',
            r'business.*problem',
            r'methodology.*summary',
            r'key.*findings',
            r'recommendations'
        ]
        
        for pattern in structure_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['structure_elements'].extend(matches)
        
        # Extract writing style guidelines
        style_patterns = [
            r'non.*technical.*language',
            r'business.*audience',
            r'clear.*communication',
            r'concise.*writing'
        ]
        
        for pattern in style_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['writing_style'].extend(matches)
        
        return insights
    
    def _analyze_asop_content(self) -> Dict:
        """Analyze ASOP content"""
        if 'asop_41' not in self.content:
            return {}
        
        content = self.content['asop_41']['content']
        
        insights = {
            'communication_requirements': [],
            'disclosure_standards': [],
            'professional_obligations': [],
            'quality_standards': []
        }
        
        # Extract communication requirements
        comm_patterns = [
            r'actuarial.*communication.*requirement',
            r'clarity.*requirement',
            r'completeness.*requirement',
            r'professional.*communication'
        ]
        
        for pattern in comm_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['communication_requirements'].extend(matches)
        
        # Extract disclosure standards
        disclosure_patterns = [
            r'disclosure.*requirement',
            r'standard.*disclosure',
            r'required.*disclosure',
            r'professional.*disclosure'
        ]
        
        for pattern in disclosure_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            insights['disclosure_standards'].extend(matches)
        
        return insights
    
    def _find_cross_references(self) -> Dict:
        """Find cross-references between resources"""
        cross_refs = {
            'shap_to_executive': [],
            'asop_to_communication': [],
            'technical_to_business': []
        }
        
        # Look for connections between SHAP and executive summary
        if 'shap_analysis' in self.content and 'executive_summary' in self.content:
            shap_content = self.content['shap_analysis']['content']
            exec_content = self.content['executive_summary']['content']
            
            # Find business interpretation patterns
            business_patterns = [
                r'business.*interpretation',
                r'stakeholder.*communication',
                r'executive.*explanation'
            ]
            
            for pattern in business_patterns:
                if re.search(pattern, shap_content, re.IGNORECASE):
                    cross_refs['shap_to_executive'].append(pattern)
        
        return cross_refs
    
    def get_resources_overview(self) -> Dict:
        """Get overview of all professional resources"""
        overview = {
            'total_resources': len(self.resources),
            'resources': {}
        }
        
        for resource_key, resource_info in self.resources.items():
            overview['resources'][resource_key] = {
                'title': resource_info['title'],
                'type': resource_info['type'],
                'category': resource_info['category'],
                'key_topics': resource_info['key_topics'],
                'loaded': resource_key in self.content
            }
        
        return overview
    
    def get_shap_analysis_guide(self) -> Dict:
        """Get SHAP analysis methodology and guidelines"""
        if 'shap_analysis' not in self.content:
            return {'error': 'SHAP analysis guide not loaded'}
        
        content = self.content['shap_analysis']
        
        return {
            'methodology': self.analysis_results['shap_insights'].get('methodology', []),
            'interpretation_guidelines': self.analysis_results['shap_insights'].get('interpretation_guidelines', []),
            'business_applications': self.analysis_results['shap_insights'].get('business_applications', []),
            'technical_requirements': self.analysis_results['shap_insights'].get('technical_requirements', []),
            'key_concepts': content.get('key_concepts', {}),
            'examples': content.get('examples', []),
            'guidelines': content.get('guidelines', [])
        }
    
    def get_executive_summary_template(self) -> Dict:
        """Get executive summary template and guidelines"""
        if 'executive_summary' not in self.content:
            return {'error': 'Executive summary template not loaded'}
        
        content = self.content['executive_summary']
        
        return {
            'structure_elements': self.analysis_results['executive_summary_insights'].get('structure_elements', []),
            'writing_style': self.analysis_results['executive_summary_insights'].get('writing_style', []),
            'business_focus': self.analysis_results['executive_summary_insights'].get('business_focus', []),
            'technical_translation': self.analysis_results['executive_summary_insights'].get('technical_translation', []),
            'key_concepts': content.get('key_concepts', {}),
            'examples': content.get('examples', []),
            'guidelines': content.get('guidelines', [])
        }
    
    def get_asop_standards(self) -> Dict:
        """Get ASOP 41 communication standards"""
        if 'asop_41' not in self.content:
            return {'error': 'ASOP 41 standards not loaded'}
        
        content = self.content['asop_41']
        
        return {
            'communication_requirements': self.analysis_results['asop_insights'].get('communication_requirements', []),
            'disclosure_standards': self.analysis_results['asop_insights'].get('disclosure_standards', []),
            'professional_obligations': self.analysis_results['asop_insights'].get('professional_obligations', []),
            'quality_standards': self.analysis_results['asop_insights'].get('quality_standards', []),
            'key_concepts': content.get('key_concepts', {}),
            'examples': content.get('examples', []),
            'guidelines': content.get('guidelines', [])
        }
    
    def get_cross_references(self) -> Dict:
        """Get cross-references between resources"""
        return self.analysis_results['cross_references']
    
    def search_professional_content(self, query: str) -> Dict:
        """Search across all professional resources"""
        results = {
            'query': query,
            'results': []
        }
        
        query_lower = query.lower()
        
        for resource_key, resource_info in self.resources.items():
            if resource_key in self.content:
                content = self.content[resource_key]['content']
                
                # Search in content
                if query_lower in content.lower():
                    # Find context around match
                    pos = content.lower().find(query_lower)
                    start = max(0, pos - 200)
                    end = min(len(content), pos + 200)
                    excerpt = content[start:end]
                    
                    results['results'].append({
                        'resource': resource_key,
                        'title': resource_info['title'],
                        'category': resource_info['category'],
                        'excerpt': excerpt,
                        'relevance_score': content.lower().count(query_lower)
                    })
        
        # Sort by relevance
        results['results'].sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return results
    
    def get_task_specific_guidance(self, task_number: int) -> Dict:
        """Get guidance specific to ATPA task numbers"""
        task_guidance = {
            1: {
                'focus': 'Data preparation and quality',
                'resources': ['asop_41'],
                'key_considerations': ['data_quality', 'methodology_documentation', 'professional_standards']
            },
            2: {
                'focus': 'Privacy and bias analysis',
                'resources': ['asop_41'],
                'key_considerations': ['ethical_considerations', 'disclosure_requirements', 'professional_obligations']
            },
            3: {
                'focus': 'Model development and validation',
                'resources': ['asop_41'],
                'key_considerations': ['methodology_documentation', 'assumption_justification', 'professional_standards']
            },
            4: {
                'focus': 'Model interpretation with SHAP',
                'resources': ['shap_analysis', 'asop_41'],
                'key_considerations': ['feature_importance', 'business_interpretation', 'professional_communication']
            },
            5: {
                'focus': 'Advanced modeling techniques',
                'resources': ['asop_41'],
                'key_considerations': ['methodology_documentation', 'assumption_justification', 'professional_standards']
            },
            6: {
                'focus': 'Executive summary and business communication',
                'resources': ['executive_summary', 'asop_41'],
                'key_considerations': ['business_communication', 'non_technical_audience', 'professional_standards']
            }
        }
        
        if task_number in task_guidance:
            guidance = task_guidance[task_number]
            
            # Add specific content from relevant resources
            specific_guidance = {
                'focus': guidance['focus'],
                'resources': guidance['resources'],
                'key_considerations': guidance['key_considerations'],
                'content': {}
            }
            
            for resource in guidance['resources']:
                if resource == 'shap_analysis':
                    specific_guidance['content']['shap_analysis'] = self.get_shap_analysis_guide()
                elif resource == 'executive_summary':
                    specific_guidance['content']['executive_summary'] = self.get_executive_summary_template()
                elif resource == 'asop_41':
                    specific_guidance['content']['asop_41'] = self.get_asop_standards()
            
            return specific_guidance
        
        return {'error': f'No guidance available for task {task_number}'}
    
    def get_communication_checklist(self) -> Dict:
        """Get comprehensive communication checklist based on ASOP standards"""
        checklist = {
            'professional_standards': [
                'Identify responsible actuary',
                'Include appropriate disclosures',
                'Ensure clarity and completeness',
                'Document methodology and assumptions',
                'Address uncertainty and limitations'
            ],
            'technical_communication': [
                'Use appropriate technical language',
                'Provide sufficient detail for technical audience',
                'Include relevant statistical measures',
                'Document data sources and quality',
                'Explain methodology choices'
            ],
            'business_communication': [
                'Translate technical findings to business insights',
                'Focus on actionable recommendations',
                'Use non-technical language for executive audience',
                'Highlight key business implications',
                'Provide clear next steps'
            ],
            'quality_assurance': [
                'Review for accuracy and completeness',
                'Ensure professional presentation',
                'Verify compliance with ASOP standards',
                'Check for appropriate audience targeting',
                'Validate business relevance'
            ]
        }
        
        return checklist 