"""
Exam Analysis Layer: Extracts patterns, expectations, and best practices from ATPA model solutions and assignments
"""
import os
import re
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ExamAnalysis:
    """
    Exam Analysis - Provides insights from model solutions and assignments
    
    Documents:
    - October-December 2024 Model Solution
    - Sample Assessment Model Solution  
    - June-August 2025 Assignment
    """
    
    def __init__(self, exam_docs_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        """
        Initialize exam analysis with path to exam documents
        
        Args:
            exam_docs_path: Path to exam documents directory
        """
        self.exam_docs_path = exam_docs_path
        self.exam_documents = {
            'oct_dec_2024': {
                'title': 'October-December 2024 Model Solution',
                'file': 'ATPA assessment October-December 2024 - Model Solution - Decrypted.md',
                'type': 'model_solution',
                'business_problem': 'ABCMart customer churn prediction',
                'key_insights': []
            },
            'sample_assessment': {
                'title': 'Sample Assessment Model Solution',
                'file': 'ATPA Sample Assessment - Model Solution.md',
                'type': 'model_solution',
                'business_problem': 'Boise airport ground time analysis',
                'key_insights': []
            },
            'june_aug_2025': {
                'title': 'June-August 2025 Assignment',
                'file': 'ATPA_June-August_2025_Assignment_(PDF).md',
                'type': 'assignment',
                'business_problem': 'NMInsights crime and arrest analysis',
                'key_insights': []
            }
        }
        
        self.document_content = {}
        self.analysis_results = {}
        self._load_exam_documents()
        self._analyze_patterns()
    
    def _load_exam_documents(self):
        """Load content from all exam documents"""
        for doc_key, doc_info in self.exam_documents.items():
            file_path = os.path.join(self.exam_docs_path, doc_info['file'])
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.document_content[doc_key] = {
                        'content': content,
                        'tasks': self._extract_tasks(content),
                        'grading_criteria': self._extract_grading_criteria(content),
                        'writing_patterns': self._extract_writing_patterns(content),
                        'technical_requirements': self._extract_technical_requirements(content)
                    }
                logger.info(f"Loaded {doc_info['title']} successfully")
            except Exception as e:
                logger.error(f"Error loading {doc_info['title']}: {e}")
                self.document_content[doc_key] = {
                    'content': f"Error loading document: {e}",
                    'tasks': [],
                    'grading_criteria': [],
                    'writing_patterns': [],
                    'technical_requirements': []
                }
    
    def _extract_tasks(self, content: str) -> List[Dict]:
        """Extract task information from exam content"""
        tasks = []
        
        # Find task sections
        task_pattern = r'Task (\d+)[\s\S]*?(?=Task \d+|$)'
        task_matches = re.finditer(task_pattern, content, re.IGNORECASE)
        
        for match in task_matches:
            task_text = match.group(0)
            task_num = re.search(r'Task (\d+)', task_text).group(1)
            
            # Extract points if available
            points_match = re.search(r'\((\d+)\s*points?\)', task_text)
            points = int(points_match.group(1)) if points_match else None
            
            # Extract requirements
            requirements = []
            bullet_pattern = r'[•\-\*]\s*(.*?)(?=\n[•\-\*]|\n\n|$)'
            bullet_matches = re.findall(bullet_pattern, task_text, re.DOTALL)
            requirements.extend([req.strip() for req in bullet_matches if req.strip()])
            
            tasks.append({
                'task_number': task_num,
                'points': points,
                'requirements': requirements,
                'full_text': task_text.strip()
            })
        
        return tasks
    
    def _extract_grading_criteria(self, content: str) -> List[str]:
        """Extract grading criteria and expectations"""
        criteria = []
        
        # Look for grading-related text
        grading_patterns = [
            r'graded on.*?quality.*?thought process',
            r'grading.*?criteria',
            r'evaluation.*?standards',
            r'quality.*?presentation',
            r'thought process.*?conclusions',
            r'effective communication',
            r'concise.*?clearly address',
            r'appropriate evidence',
            r'no credit.*?not directly related'
        ]
        
        for pattern in grading_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            criteria.extend(matches)
        
        return list(set(criteria))
    
    def _extract_writing_patterns(self, content: str) -> Dict:
        """Extract writing patterns and formatting expectations"""
        patterns = {
            'audience_specifications': [],
            'formatting_requirements': [],
            'length_guidelines': [],
            'technical_vs_nontechnical': [],
            'evidence_requirements': []
        }
        
        # Audience specifications
        audience_patterns = [
            r'written for.*?audience',
            r'assume.*?audience',
            r'technical audience',
            r'non-technical',
            r'executive summary',
            r'manager.*?reviewing'
        ]
        
        for pattern in audience_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            patterns['audience_specifications'].extend(matches)
        
        # Formatting requirements
        formatting_patterns = [
            r'Word template',
            r'copy.*?paste',
            r'brief section',
            r'working file',
            r'technical report',
            r'executive summary'
        ]
        
        for pattern in formatting_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            patterns['formatting_requirements'].extend(matches)
        
        return patterns
    
    def _extract_technical_requirements(self, content: str) -> Dict:
        """Extract technical requirements and methodologies"""
        requirements = {
            'data_preparation': [],
            'modeling_techniques': [],
            'visualization_requirements': [],
            'performance_metrics': [],
            'validation_approaches': []
        }
        
        # Data preparation requirements
        data_patterns = [
            r'data cleaning',
            r'missing values',
            r'feature engineering',
            r'data validation',
            r'exploratory data analysis',
            r'data preparation'
        ]
        
        for pattern in data_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            requirements['data_preparation'].extend(matches)
        
        # Modeling techniques
        modeling_patterns = [
            r'generalized linear model',
            r'mixed model',
            r'random effects',
            r'logistic regression',
            r'neural network',
            r'random forest',
            r'cross-validation'
        ]
        
        for pattern in modeling_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            requirements['modeling_techniques'].extend(matches)
        
        return requirements
    
    def _analyze_patterns(self):
        """Analyze patterns across all exam documents"""
        self.analysis_results = {
            'task_patterns': self._analyze_task_patterns(),
            'writing_expectations': self._analyze_writing_expectations(),
            'technical_expectations': self._analyze_technical_expectations(),
            'grading_insights': self._analyze_grading_insights(),
            'common_mistakes': self._analyze_common_mistakes(),
            'success_factors': self._analyze_success_factors()
        }
    
    def _analyze_task_patterns(self) -> Dict:
        """Analyze patterns in task structure and requirements"""
        patterns = {
            'task_count': {},
            'point_distribution': {},
            'common_requirements': {},
            'task_dependencies': {},
            'business_context': {}
        }
        
        # Analyze task counts
        for doc_key, doc_content in self.document_content.items():
            if 'tasks' in doc_content:
                patterns['task_count'][doc_key] = len(doc_content['tasks'])
        
        # Analyze common requirements
        all_requirements = []
        for doc_content in self.document_content.values():
            if 'tasks' in doc_content:
                for task in doc_content['tasks']:
                    all_requirements.extend(task.get('requirements', []))
        
        # Count common requirements
        requirement_counts = {}
        for req in all_requirements:
            req_lower = req.lower()
            requirement_counts[req_lower] = requirement_counts.get(req_lower, 0) + 1
        
        patterns['common_requirements'] = dict(sorted(requirement_counts.items(), 
                                                     key=lambda x: x[1], reverse=True)[:10])
        
        return patterns
    
    def _analyze_writing_expectations(self) -> Dict:
        """Analyze writing and communication expectations"""
        expectations = {
            'audience_types': [],
            'formatting_standards': [],
            'length_guidelines': [],
            'evidence_requirements': [],
            'communication_style': []
        }
        
        # Collect audience specifications
        for doc_content in self.document_content.values():
            if 'writing_patterns' in doc_content:
                expectations['audience_types'].extend(
                    doc_content['writing_patterns'].get('audience_specifications', [])
                )
                expectations['formatting_standards'].extend(
                    doc_content['writing_patterns'].get('formatting_requirements', [])
                )
        
        # Remove duplicates
        expectations['audience_types'] = list(set(expectations['audience_types']))
        expectations['formatting_standards'] = list(set(expectations['formatting_standards']))
        
        return expectations
    
    def _analyze_technical_expectations(self) -> Dict:
        """Analyze technical requirements and methodologies"""
        expectations = {
            'data_preparation_standards': [],
            'modeling_approaches': [],
            'validation_methods': [],
            'performance_metrics': [],
            'visualization_requirements': []
        }
        
        # Collect technical requirements
        for doc_content in self.document_content.values():
            if 'technical_requirements' in doc_content:
                for category, requirements in doc_content['technical_requirements'].items():
                    if f'{category}_standards' in expectations:
                        expectations[f'{category}_standards'].extend(requirements)
        
        # Remove duplicates
        for category in expectations:
            expectations[category] = list(set(expectations[category]))
        
        return expectations
    
    def _analyze_grading_insights(self) -> Dict:
        """Analyze grading criteria and evaluation standards"""
        insights = {
            'evaluation_criteria': [],
            'quality_indicators': [],
            'penalty_factors': [],
            'bonus_factors': []
        }
        
        # Collect grading criteria
        for doc_content in self.document_content.values():
            if 'grading_criteria' in doc_content:
                insights['evaluation_criteria'].extend(doc_content['grading_criteria'])
        
        # Identify quality indicators
        quality_patterns = [
            'thought process',
            'conclusions',
            'presentation quality',
            'effective communication',
            'appropriate evidence',
            'justification'
        ]
        
        for pattern in quality_patterns:
            for doc_content in self.document_content.values():
                if pattern in doc_content['content'].lower():
                    insights['quality_indicators'].append(pattern)
        
        # Remove duplicates
        insights['evaluation_criteria'] = list(set(insights['evaluation_criteria']))
        insights['quality_indicators'] = list(set(insights['quality_indicators']))
        
        return insights
    
    def _analyze_common_mistakes(self) -> List[str]:
        """Analyze common mistakes and pitfalls"""
        mistakes = []
        
        # Look for warning patterns
        warning_patterns = [
            r'no credit.*?not directly related',
            r'not.*?appropriate evidence',
            r'going off topic',
            r'too much.*?too little',
            r'not.*?justified',
            r'missing.*?evidence'
        ]
        
        for pattern in warning_patterns:
            for doc_content in self.document_content.values():
                matches = re.findall(pattern, doc_content['content'], re.IGNORECASE)
                mistakes.extend(matches)
        
        return list(set(mistakes))
    
    def _analyze_success_factors(self) -> Dict:
        """Analyze factors that contribute to success"""
        factors = {
            'communication_skills': [],
            'technical_competence': [],
            'business_understanding': [],
            'methodology_rigor': [],
            'evidence_provision': []
        }
        
        # Success indicators from grading criteria
        success_patterns = {
            'communication_skills': ['effective communication', 'clear', 'concise', 'appropriate audience'],
            'technical_competence': ['thought process', 'methodology', 'technical accuracy'],
            'business_understanding': ['business problem', 'context', 'practical application'],
            'methodology_rigor': ['justification', 'evidence', 'validation'],
            'evidence_provision': ['supporting evidence', 'results', 'conclusions']
        }
        
        for category, patterns in success_patterns.items():
            for pattern in patterns:
                for doc_content in self.document_content.values():
                    if pattern in doc_content['content'].lower():
                        factors[category].append(pattern)
        
        # Remove duplicates
        for category in factors:
            factors[category] = list(set(factors[category]))
        
        return factors
    
    def get_exam_overview(self) -> Dict:
        """Get overview of all exam documents"""
        overview = {
            'total_documents': len(self.exam_documents),
            'documents': {}
        }
        
        for doc_key, doc_info in self.exam_documents.items():
            overview['documents'][doc_key] = {
                'title': doc_info['title'],
                'type': doc_info['type'],
                'business_problem': doc_info['business_problem'],
                'loaded': doc_key in self.document_content
            }
        
        return overview
    
    def get_task_analysis(self) -> Dict:
        """Get comprehensive task analysis"""
        return {
            'task_patterns': self.analysis_results['task_patterns'],
            'common_requirements': self._get_common_requirements(),
            'task_dependencies': self._get_task_dependencies(),
            'point_distribution': self._get_point_distribution()
        }
    
    def get_writing_guidelines(self) -> Dict:
        """Get writing and communication guidelines"""
        return {
            'audience_expectations': self.analysis_results['writing_expectations']['audience_types'],
            'formatting_requirements': self.analysis_results['writing_expectations']['formatting_standards'],
            'communication_style': self._get_communication_style_guidelines(),
            'evidence_requirements': self._get_evidence_requirements()
        }
    
    def get_technical_guidelines(self) -> Dict:
        """Get technical methodology guidelines"""
        return {
            'data_preparation': self.analysis_results['technical_expectations']['data_preparation_standards'],
            'modeling_approaches': self.analysis_results['technical_expectations']['modeling_approaches'],
            'validation_methods': self.analysis_results['technical_expectations']['validation_methods'],
            'performance_metrics': self.analysis_results['technical_expectations']['performance_metrics'],
            'visualization_requirements': self.analysis_results['technical_expectations']['visualization_requirements']
        }
    
    def get_grading_insights(self) -> Dict:
        """Get grading and evaluation insights"""
        return {
            'evaluation_criteria': self.analysis_results['grading_insights']['evaluation_criteria'],
            'quality_indicators': self.analysis_results['grading_insights']['quality_indicators'],
            'common_mistakes': self.analysis_results['common_mistakes'],
            'success_factors': self.analysis_results['success_factors']
        }
    
    def get_current_assignment_analysis(self) -> Dict:
        """Get specific analysis of current assignment (June-August 2025)"""
        if 'june_aug_2025' not in self.document_content:
            return {'error': 'Current assignment not loaded'}
        
        content = self.document_content['june_aug_2025']
        
        return {
            'business_problem': self.exam_documents['june_aug_2025']['business_problem'],
            'tasks': content.get('tasks', []),
            'key_requirements': self._extract_key_requirements(content['content']),
            'grading_expectations': content.get('grading_criteria', []),
            'technical_requirements': content.get('technical_requirements', {})
        }
    
    def get_comparative_analysis(self) -> Dict:
        """Get comparative analysis across all exams"""
        return {
            'task_comparison': self._compare_task_structures(),
            'writing_comparison': self._compare_writing_expectations(),
            'technical_comparison': self._compare_technical_requirements(),
            'grading_comparison': self._compare_grading_criteria()
        }
    
    def search_exam_content(self, query: str) -> Dict:
        """Search across all exam documents"""
        results = {
            'query': query,
            'results': []
        }
        
        query_lower = query.lower()
        
        for doc_key, doc_info in self.exam_documents.items():
            if doc_key in self.document_content:
                content = self.document_content[doc_key]['content']
                
                # Search in content
                if query_lower in content.lower():
                    # Find context around match
                    pos = content.lower().find(query_lower)
                    start = max(0, pos - 200)
                    end = min(len(content), pos + 200)
                    excerpt = content[start:end]
                    
                    results['results'].append({
                        'document': doc_key,
                        'title': doc_info['title'],
                        'excerpt': excerpt,
                        'relevance_score': content.lower().count(query_lower)
                    })
        
        # Sort by relevance
        results['results'].sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return results
    
    def _get_common_requirements(self) -> List[str]:
        """Get most common task requirements"""
        if 'task_patterns' in self.analysis_results:
            return list(self.analysis_results['task_patterns'].get('common_requirements', {}).keys())
        return []
    
    def _get_task_dependencies(self) -> Dict:
        """Get task dependency patterns"""
        dependencies = {}
        
        for doc_content in self.document_content.values():
            if 'tasks' in doc_content:
                for task in doc_content['tasks']:
                    task_text = task.get('full_text', '')
                    if 'prior task' in task_text.lower() or 'previous task' in task_text.lower():
                        dependencies[task['task_number']] = 'Depends on prior tasks'
        
        return dependencies
    
    def _get_point_distribution(self) -> Dict:
        """Get point distribution analysis"""
        distribution = {}
        
        for doc_content in self.document_content.values():
            if 'tasks' in doc_content:
                for task in doc_content['tasks']:
                    points = task.get('points')
                    if points:
                        distribution[task['task_number']] = points
        
        return distribution
    
    def _get_communication_style_guidelines(self) -> List[str]:
        """Get communication style guidelines"""
        guidelines = []
        
        style_patterns = [
            'concise',
            'clear',
            'appropriate for audience',
            'technical vs non-technical',
            'executive summary',
            'working file'
        ]
        
        for pattern in style_patterns:
            for doc_content in self.document_content.values():
                if pattern in doc_content['content'].lower():
                    guidelines.append(pattern)
        
        return list(set(guidelines))
    
    def _get_evidence_requirements(self) -> List[str]:
        """Get evidence and justification requirements"""
        requirements = []
        
        evidence_patterns = [
            'supporting evidence',
            'justification',
            'reasoning',
            'validation',
            'results',
            'conclusions'
        ]
        
        for pattern in evidence_patterns:
            for doc_content in self.document_content.values():
                if pattern in doc_content['content'].lower():
                    requirements.append(pattern)
        
        return list(set(requirements))
    
    def _extract_key_requirements(self, content: str) -> List[str]:
        """Extract key requirements from current assignment"""
        requirements = []
        
        # Look for key requirement patterns
        requirement_patterns = [
            r'[•\-\*]\s*(.*?)(?=\n[•\-\*]|\n\n|$)',
            r'Specifically.*?address',
            r'Justify.*?approach',
            r'Explain.*?choices',
            r'Recommend.*?approach'
        ]
        
        for pattern in requirement_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            requirements.extend([match.strip() for match in matches if match.strip()])
        
        return requirements[:20]  # Return top 20 requirements
    
    def _compare_task_structures(self) -> Dict:
        """Compare task structures across exams"""
        comparison = {}
        
        for doc_key, doc_content in self.document_content.items():
            if 'tasks' in doc_content:
                # Calculate total points safely, handling None values
                total_points = 0
                for task in doc_content['tasks']:
                    points = task.get('points')
                    if points is not None:
                        total_points += points
                
                comparison[doc_key] = {
                    'task_count': len(doc_content['tasks']),
                    'total_points': total_points,
                    'task_types': [task.get('task_number') for task in doc_content['tasks'] if task.get('task_number') is not None]
                }
        
        return comparison
    
    def _compare_writing_expectations(self) -> Dict:
        """Compare writing expectations across exams"""
        return self.analysis_results['writing_expectations']
    
    def _compare_technical_requirements(self) -> Dict:
        """Compare technical requirements across exams"""
        return self.analysis_results['technical_expectations']
    
    def _compare_grading_criteria(self) -> Dict:
        """Compare grading criteria across exams"""
        return self.analysis_results['grading_insights'] 