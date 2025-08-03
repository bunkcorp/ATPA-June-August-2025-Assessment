"""
Curriculum Layer: Integrates all four ATPA modules for comprehensive curriculum access
"""
import os
import re
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class ATPACurriculum:
    """
    ATPA Curriculum Integration - Provides access to all four ATPA modules
    
    Modules:
    - Module 1: Data and Model Ethics
    - Module 2: Working with Data  
    - Module 3: Advanced Models
    - Module 4: Model Explainability and Communication
    """
    
    def __init__(self, curriculum_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        """
        Initialize ATPA curriculum with path to module documents
        
        Args:
            curriculum_path: Path to ATPA curriculum directory
        """
        self.curriculum_path = curriculum_path
        self.modules = {
            'module_1': {
                'title': 'Data and Model Ethics',
                'file': 'ATPA_Module_1_document.doc.md',
                'sections': [
                    'Ethical Framework',
                    'Regulations and Standards of Practice', 
                    'Case Study'
                ],
                'key_topics': [
                    'Fairness', 'Safety', 'Transparency and Accountability',
                    'Protected Classes', 'Bias Detection', 'ASOPs',
                    'Data Protection Regulations', 'Anti-Discrimination Laws'
                ]
            },
            'module_2': {
                'title': 'Working with Data',
                'file': 'ATPA_Module_2_document.doc.md',
                'sections': [
                    'Data Pipeline',
                    'Reading and Writing Data',
                    'Data Transformation and Cleaning'
                ],
                'key_topics': [
                    'Data Bias', 'Selection Bias', 'Measurement Bias',
                    'Omitted Variable Bias', 'Data Quality', 'Tidy Data',
                    'Data Frames', 'Data Transformation'
                ]
            },
            'module_3': {
                'title': 'Advanced Models',
                'file': 'ATPA_Module_3_document.md',
                'sections': [
                    'Model Accuracy',
                    'Additive Models', 
                    'Linear Mixed Models',
                    'Neural Networks'
                ],
                'key_topics': [
                    'Model Validation', 'Generalized Additive Models (GAMs)',
                    'Mixed Models', 'Neural Networks', 'Activation Functions',
                    'Loss Functions', 'Overfitting', 'Model Evaluation'
                ]
            },
            'module_4': {
                'title': 'Model Explainability and Communication',
                'file': 'ATPA_Module_4_document.doc.md',
                'sections': [
                    'Explainability – Definitions and Communication',
                    'Explainability and Ethics',
                    'Techniques for Opaque Models',
                    'Reports',
                    'Model Selection Case Study'
                ],
                'key_topics': [
                    'Model Explainability', 'SHAP Values', 'Partial Dependence Plots',
                    'Lift and Gain Charts', 'ASOP 41', 'Technical Reports',
                    'Executive Summaries', 'Audience Communication'
                ]
            }
        }
        
        self.module_content = {}
        self._load_module_content()
    
    def _load_module_content(self):
        """Load content from all module markdown files"""
        for module_key, module_info in self.modules.items():
            file_path = os.path.join(self.curriculum_path, module_info['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.module_content[module_key] = {
                        'content': content,
                        'sections': self._extract_sections(content),
                        'key_concepts': self._extract_key_concepts(content)
                    }
                logger.info(f"Loaded {module_info['title']} successfully")
            except Exception as e:
                logger.error(f"Error loading {module_info['title']}: {e}")
                self.module_content[module_key] = {
                    'content': f"Error loading module: {e}",
                    'sections': [],
                    'key_concepts': []
                }
    
    def _extract_sections(self, content: str) -> List[Dict]:
        """Extract section headers and their content from markdown"""
        sections = []
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            if line.startswith('#'):
                # Save previous section
                if current_section:
                    sections.append({
                        'title': current_section,
                        'content': '\n'.join(current_content).strip()
                    })
                
                # Start new section
                current_section = line.strip('#').strip()
                current_content = []
            else:
                if current_section:
                    current_content.append(line)
        
        # Add last section
        if current_section:
            sections.append({
                'title': current_section,
                'content': '\n'.join(current_content).strip()
            })
        
        return sections
    
    def _extract_key_concepts(self, content: str) -> List[str]:
        """Extract key concepts and terms from module content"""
        # Common ATPA terms and concepts
        atpa_terms = [
            'bias', 'fairness', 'ethics', 'transparency', 'accountability',
            'protected class', 'demographic parity', 'equal opportunity',
            'selection bias', 'measurement bias', 'omitted variable bias',
            'data quality', 'model validation', 'overfitting', 'generalization',
            'explainability', 'interpretability', 'SHAP', 'partial dependence',
            'lift chart', 'gain chart', 'ASOP', 'regulations', 'compliance'
        ]
        
        found_terms = []
        content_lower = content.lower()
        
        for term in atpa_terms:
            if term in content_lower:
                found_terms.append(term)
        
        return found_terms
    
    def get_module_overview(self) -> Dict:
        """Get overview of all ATPA modules"""
        overview = {
            'total_modules': len(self.modules),
            'modules': {}
        }
        
        for module_key, module_info in self.modules.items():
            overview['modules'][module_key] = {
                'title': module_info['title'],
                'sections': module_info['sections'],
                'key_topics': module_info['key_topics'],
                'loaded': module_key in self.module_content
            }
        
        return overview
    
    def get_module_content(self, module_key: str) -> Dict:
        """Get content for a specific module"""
        if module_key not in self.modules:
            return {'error': f'Module {module_key} not found'}
        
        if module_key not in self.module_content:
            return {'error': f'Module {module_key} content not loaded'}
        
        return {
            'module_info': self.modules[module_key],
            'sections': self.module_content[module_key]['sections'],
            'key_concepts': self.module_content[module_key]['key_concepts']
        }
    
    def search_curriculum(self, query: str) -> Dict:
        """Search across all modules for specific content"""
        results = {
            'query': query,
            'results': []
        }
        
        query_lower = query.lower()
        
        for module_key, module_info in self.modules.items():
            if module_key in self.module_content:
                content = self.module_content[module_key]['content']
                sections = self.module_content[module_key]['sections']
                
                # Search in sections
                for section in sections:
                    if query_lower in section['title'].lower() or query_lower in section['content'].lower():
                        results['results'].append({
                            'module': module_key,
                            'module_title': module_info['title'],
                            'section_title': section['title'],
                            'relevance_score': self._calculate_relevance(query_lower, section['content']),
                            'excerpt': self._get_excerpt(section['content'], query_lower)
                        })
        
        # Sort by relevance score
        results['results'].sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return results
    
    def _calculate_relevance(self, query: str, content: str) -> float:
        """Calculate relevance score for search results"""
        content_lower = content.lower()
        query_words = query.split()
        
        score = 0
        for word in query_words:
            if word in content_lower:
                score += content_lower.count(word)
        
        return score
    
    def _get_excerpt(self, content: str, query: str, max_length: int = 200) -> str:
        """Get excerpt around query match"""
        content_lower = content.lower()
        query_pos = content_lower.find(query)
        
        if query_pos == -1:
            return content[:max_length] + "..." if len(content) > max_length else content
        
        start = max(0, query_pos - max_length // 2)
        end = min(len(content), query_pos + max_length // 2)
        
        excerpt = content[start:end]
        if start > 0:
            excerpt = "..." + excerpt
        if end < len(content):
            excerpt = excerpt + "..."
        
        return excerpt
    
    def get_learning_objectives(self) -> Dict:
        """Get learning objectives for all modules"""
        objectives = {}
        
        for module_key, module_info in self.modules.items():
            if module_key in self.module_content:
                content = self.module_content[module_key]['content']
                
                # Extract learning objectives
                learning_obj_match = re.search(r'Learning Objectives?[:\s]*(.*?)(?=\n\n|\n#|$)', 
                                             content, re.IGNORECASE | re.DOTALL)
                
                if learning_obj_match:
                    objectives[module_key] = {
                        'title': module_info['title'],
                        'objectives': learning_obj_match.group(1).strip()
                    }
                else:
                    objectives[module_key] = {
                        'title': module_info['title'],
                        'objectives': 'Learning objectives not found in content'
                    }
        
        return objectives
    
    def get_ethical_framework_details(self) -> Dict:
        """Get detailed ethical framework from Module 1"""
        if 'module_1' not in self.module_content:
            return {'error': 'Module 1 content not available'}
        
        content = self.module_content['module_1']['content']
        
        # Extract ethical principles
        principles = {}
        
        # Fairness
        fairness_match = re.search(r'Fairness[:\s]*(.*?)(?=\n\n|\n#|$)', content, re.IGNORECASE | re.DOTALL)
        if fairness_match:
            principles['fairness'] = fairness_match.group(1).strip()
        
        # Safety
        safety_match = re.search(r'Safety[:\s]*(.*?)(?=\n\n|\n#|$)', content, re.IGNORECASE | re.DOTALL)
        if safety_match:
            principles['safety'] = safety_match.group(1).strip()
        
        # Transparency
        transparency_match = re.search(r'Transparency[:\s]*(.*?)(?=\n\n|\n#|$)', content, re.IGNORECASE | re.DOTALL)
        if transparency_match:
            principles['transparency'] = transparency_match.group(1).strip()
        
        return {
            'module': 'Data and Model Ethics',
            'principles': principles,
            'full_content': content
        }
    
    def get_modeling_techniques(self) -> Dict:
        """Get modeling techniques from Module 3"""
        if 'module_3' not in self.module_content:
            return {'error': 'Module 3 content not available'}
        
        content = self.module_content['module_3']['content']
        
        techniques = {
            'additive_models': {},
            'mixed_models': {},
            'neural_networks': {},
            'model_validation': {}
        }
        
        # Extract GAM content
        gam_match = re.search(r'Generalized Additive Models?[:\s]*(.*?)(?=\n\n|\n#|$)', 
                             content, re.IGNORECASE | re.DOTALL)
        if gam_match:
            techniques['additive_models']['GAMs'] = gam_match.group(1).strip()
        
        # Extract Neural Network content
        nn_match = re.search(r'Neural Networks?[:\s]*(.*?)(?=\n\n|\n#|$)', 
                           content, re.IGNORECASE | re.DOTALL)
        if nn_match:
            techniques['neural_networks']['overview'] = nn_match.group(1).strip()
        
        return {
            'module': 'Advanced Models',
            'techniques': techniques,
            'full_content': content
        }
    
    def get_explainability_techniques(self) -> Dict:
        """Get explainability techniques from Module 4"""
        if 'module_4' not in self.module_content:
            return {'error': 'Module 4 content not available'}
        
        content = self.module_content['module_4']['content']
        
        techniques = {
            'shap_values': {},
            'partial_dependence': {},
            'lift_gain_charts': {},
            'global_surrogates': {}
        }
        
        # Extract SHAP content
        shap_match = re.search(r'Shapley Values?[:\s]*(.*?)(?=\n\n|\n#|$)', 
                              content, re.IGNORECASE | re.DOTALL)
        if shap_match:
            techniques['shap_values']['description'] = shap_match.group(1).strip()
        
        # Extract Partial Dependence content
        pdp_match = re.search(r'Partial Dependence[:\s]*(.*?)(?=\n\n|\n#|$)', 
                             content, re.IGNORECASE | re.DOTALL)
        if pdp_match:
            techniques['partial_dependence']['description'] = pdp_match.group(1).strip()
        
        return {
            'module': 'Model Explainability and Communication',
            'techniques': techniques,
            'full_content': content
        }
    
    def get_data_quality_guidelines(self) -> Dict:
        """Get data quality guidelines from Module 2"""
        if 'module_2' not in self.module_content:
            return {'error': 'Module 2 content not available'}
        
        content = self.module_content['module_2']['content']
        
        guidelines = {
            'bias_types': {},
            'data_quality': {},
            'data_transformation': {}
        }
        
        # Extract bias types
        bias_match = re.search(r'Bias[:\s]*(.*?)(?=\n\n|\n#|$)', 
                              content, re.IGNORECASE | re.DOTALL)
        if bias_match:
            guidelines['bias_types']['overview'] = bias_match.group(1).strip()
        
        return {
            'module': 'Working with Data',
            'guidelines': guidelines,
            'full_content': content
        }
    
    def get_curriculum_summary(self) -> Dict:
        """Get comprehensive curriculum summary"""
        summary = {
            'overview': self.get_module_overview(),
            'learning_objectives': self.get_learning_objectives(),
            'key_concepts': {},
            'module_relationships': {
                'ethics_foundation': 'Module 1 provides ethical foundation for all other modules',
                'data_foundation': 'Module 2 builds on ethics to address data quality and bias',
                'modeling_techniques': 'Module 3 applies ethical and data principles to advanced modeling',
                'communication': 'Module 4 focuses on explaining and communicating model results'
            }
        }
        
        # Collect key concepts from all modules
        for module_key, module_info in self.modules.items():
            if module_key in self.module_content:
                summary['key_concepts'][module_key] = {
                    'title': module_info['title'],
                    'concepts': self.module_content[module_key]['key_concepts']
                }
        
        return summary 