"""
Practical Examples Layer: Integrates R Markdown files with working code examples from ATPA curriculum
"""
import os
import re
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class PracticalExamples:
    """
    Practical Examples - Provides working code examples from ATPA curriculum
    
    Documents:
    - Module 2: Data preparation and manipulation examples (Python & R)
    - Module 3: Advanced modeling examples (Python & R)
    - Module 4: Model explainability examples (Python & R)
    - FlightsPrep: Practical data preparation example
    """
    
    def __init__(self, examples_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        """
        Initialize practical examples with path to R Markdown files
        
        Args:
            examples_path: Path to examples directory
        """
        self.examples_path = examples_path
        self.examples = {
            'module_2_python': {
                'title': 'Module 2 - Data Preparation (Python)',
                'files': [
                    'Module_2_Working_with_Data/atpa_2_2_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_3_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_4_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_5_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_6_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_7_1_python.rmd',
                    'Module_2_Working_with_Data/atpa_2_7_2_python.rmd'
                ],
                'category': 'data_preparation',
                'language': 'python',
                'key_topics': ['data_reading', 'data_cleaning', 'data_manipulation', 'data_visualization']
            },
            'module_2_r': {
                'title': 'Module 2 - Data Preparation (R)',
                'files': [
                    'Module_2_Working_with_Data/atpa_2_2_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_3_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_4_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_5_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_6_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_7_1_r.rmd',
                    'Module_2_Working_with_Data/atpa_2_7_2_r.rmd'
                ],
                'category': 'data_preparation',
                'language': 'r',
                'key_topics': ['data_reading', 'data_cleaning', 'data_manipulation', 'data_visualization']
            },
            'module_3_advanced_r': {
                'title': 'Module 3 - Advanced Models (R)',
                'files': [
                    'Module_3_Advanced_Models/atpa_3_2_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_3_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_4_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_5_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_6_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_7a_r.rmd',
                    'Module_3_Advanced_Models/atpa_3_7b_r.rmd'
                ],
                'category': 'advanced_modeling',
                'language': 'r',
                'key_topics': ['generalized_additive_models', 'generalized_linear_models', 'mixed_models', 'model_selection', 'neural_networks', 'hyperparameter_tuning', 'cross_validation', 'stacking', 'bayesian_methods']
            },
            'module_4_python': {
                'title': 'Module 4 - Model Explainability (Python)',
                'files': [
                    'Module_4_Model_Explainability/atpa_4_3_python.rmd',
                    'Module_4_Model_Explainability/atpa_4_5_r.rmd'
                ],
                'category': 'model_explainability',
                'language': 'python',
                'key_topics': ['shap_analysis', 'partial_dependence_plots', 'variable_importance', 'model_interpretation']
            },
            'module_4_r': {
                'title': 'Module 4 - Model Explainability (R)',
                'files': [
                    'Module_4_Model_Explainability/atpa_4_3_r.rmd'
                ],
                'category': 'model_explainability',
                'language': 'r',
                'key_topics': ['shap_analysis', 'partial_dependence_plots', 'variable_importance', 'model_interpretation']
            },
            'flights_prep': {
                'title': 'Flights Data Preparation',
                'files': [
                    'Module_2_Working_with_Data/FlightsPrep.Rmd',
                    'Module_2_Working_with_Data/FlightsPrep_python.Rmd'
                ],
                'category': 'practical_example',
                'language': 'both',
                'key_topics': ['data_preparation', 'real_world_example', 'cross_language_comparison']
            }
        }
        
        self.content = {}
        self.analysis_results = {}
        self._load_examples()
        self._analyze_content()
    
    def _load_examples(self):
        """Load content from all R Markdown example files"""
        for example_key, example_info in self.examples.items():
            self.content[example_key] = {
                'files': {},
                'code_chunks': [],
                'examples': [],
                'key_concepts': []
            }
            
            for file_path in example_info['files']:
                full_path = os.path.join(self.examples_path, file_path)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.content[example_key]['files'][file_path] = {
                            'content': content,
                            'code_chunks': self._extract_code_chunks(content),
                            'examples': self._extract_examples(content),
                            'key_concepts': self._extract_key_concepts(content, example_info['key_topics'])
                        }
                    logger.info(f"Loaded {file_path} successfully")
                except Exception as e:
                    logger.error(f"Error loading {file_path}: {e}")
                    self.content[example_key]['files'][file_path] = {
                        'content': f"Error loading file: {e}",
                        'code_chunks': [],
                        'examples': [],
                        'key_concepts': []
                    }
    
    def _extract_code_chunks(self, content: str) -> List[Dict]:
        """Extract code chunks from R Markdown content"""
        chunks = []
        
        # Look for code chunks
        chunk_pattern = r'```\{([^}]+)\}(.*?)```'
        chunk_matches = re.finditer(chunk_pattern, content, re.DOTALL)
        
        for match in chunk_matches:
            chunk_info = match.group(1).strip()
            chunk_content = match.group(2).strip()
            
            # Parse chunk info
            chunk_parts = chunk_info.split()
            language = chunk_parts[0] if chunk_parts else 'unknown'
            chunk_name = chunk_parts[1] if len(chunk_parts) > 1 else 'unnamed'
            
            chunks.append({
                'language': language,
                'name': chunk_name,
                'content': chunk_content,
                'lines': len(chunk_content.split('\n')),
                'has_output': 'output' in chunk_info.lower() or 'echo' in chunk_info.lower()
            })
        
        return chunks
    
    def _extract_examples(self, content: str) -> List[Dict]:
        """Extract practical examples from content"""
        examples = []
        
        # Look for example patterns
        example_patterns = [
            r'CHUNK \d+[:\s]+([^:]+)',
            r'Exercise[:\s]+([^:]+)',
            r'Example[:\s]+([^:]+)',
            r'Practice[:\s]+([^:]+)'
        ]
        
        for pattern in example_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                example_title = match.group(1).strip()
                
                # Get context around the example
                start_pos = max(0, match.start() - 200)
                end_pos = min(len(content), match.end() + 500)
                context = content[start_pos:end_pos]
                
                examples.append({
                    'title': example_title,
                    'context': context,
                    'type': 'code_example'
                })
        
        return examples
    
    def _extract_key_concepts(self, content: str, topics: List[str]) -> Dict:
        """Extract key concepts related to specified topics"""
        concepts = {}
        
        for topic in topics:
            topic_patterns = {
                'data_reading': [r'read_csv', r'read_table', r'pd\.read', r'read\.csv'],
                'data_cleaning': [r'clean', r'na\.', r'missing', r'dropna', r'fillna'],
                'data_manipulation': [r'groupby', r'mutate', r'filter', r'select', r'arrange'],
                'data_visualization': [r'ggplot', r'plot', r'visualization', r'chart'],
                'generalized_additive_models': [r'gam', r'generalized additive', r'smoothing'],
                'generalized_linear_models': [r'glm', r'generalized linear', r'family'],
                'mixed_models': [r'mixed', r'random effect', r'lmer', r'glmer'],
                'model_selection': [r'cross validation', r'cv', r'selection', r'comparison'],
                'neural_networks': [r'neuralnetwork', r'neural network', r'nnet', r'hidden\.layers', r'activation', r'relu'],
                'hyperparameter_tuning': [r'hyperparameter', r'parameter tuning', r'grid search', r'optimization', r'learn\.rates', r'n\.epochs'],
                'cross_validation': [r'cross validation', r'cv', r'fold', r'holdout', r'k-fold', r'validation'],
                'stacking': [r'stacking', r'ensemble', r'meta-model', r'stack', r'blending'],
                'bayesian_methods': [r'bayesian', r'stan', r'mcmc', r'posterior', r'prior', r'brms'],
                'shap_analysis': [r'shap', r'shapley', r'explain', r'interpret'],
                'partial_dependence_plots': [r'partial dependence', r'pdp', r'dependence plot'],
                'variable_importance': [r'importance', r'feature importance', r'variable importance'],
                'model_interpretation': [r'interpret', r'explain', r'understanding', r'meaning']
            }
            
            if topic in topic_patterns:
                patterns = topic_patterns[topic]
                matches = []
                for pattern in patterns:
                    found = re.findall(pattern, content, re.IGNORECASE)
                    matches.extend(found)
                concepts[topic] = list(set(matches))
        
        return concepts
    
    def _analyze_content(self):
        """Analyze content across all examples"""
        self.analysis_results = {
            'code_statistics': self._analyze_code_statistics(),
            'language_comparison': self._analyze_language_comparison(),
            'topic_coverage': self._analyze_topic_coverage(),
            'practical_applications': self._analyze_practical_applications()
        }
    
    def _analyze_code_statistics(self) -> Dict:
        """Analyze code statistics across all examples"""
        stats = {
            'total_files': 0,
            'total_chunks': 0,
            'python_chunks': 0,
            'r_chunks': 0,
            'average_chunk_size': 0,
            'languages_used': set()
        }
        
        total_lines = 0
        
        for example_key, example_content in self.content.items():
            for file_path, file_content in example_content['files'].items():
                stats['total_files'] += 1
                
                for chunk in file_content['code_chunks']:
                    stats['total_chunks'] += 1
                    total_lines += chunk['lines']
                    
                    if chunk['language'].lower() == 'python':
                        stats['python_chunks'] += 1
                    elif chunk['language'].lower() == 'r':
                        stats['r_chunks'] += 1
                    
                    stats['languages_used'].add(chunk['language'])
        
        stats['average_chunk_size'] = total_lines / stats['total_chunks'] if stats['total_chunks'] > 0 else 0
        stats['languages_used'] = list(stats['languages_used'])
        
        return stats
    
    def _analyze_language_comparison(self) -> Dict:
        """Compare Python vs R implementations"""
        comparison = {
            'python_examples': [],
            'r_examples': [],
            'common_patterns': [],
            'language_specific_features': {}
        }
        
        # Extract examples by language
        for example_key, example_info in self.examples.items():
            if example_info['language'] == 'python':
                comparison['python_examples'].append(example_key)
            elif example_info['language'] == 'r':
                comparison['r_examples'].append(example_key)
        
        # Add advanced topics to common patterns
        comparison['common_patterns'] = [
            'neural_networks', 'hyperparameter_tuning', 'cross_validation', 
            'stacking', 'bayesian_methods', 'model_selection'
        ]
        
        return comparison
    
    def _analyze_topic_coverage(self) -> Dict:
        """Analyze topic coverage across examples"""
        coverage = {
            'data_preparation': [],
            'advanced_modeling': [],
            'model_explainability': [],
            'practical_examples': [],
            'neural_networks': [],
            'hyperparameter_tuning': [],
            'cross_validation': [],
            'stacking': [],
            'bayesian_methods': []
        }
        
        for example_key, example_info in self.examples.items():
            category = example_info['category']
            if category in coverage:
                coverage[category].append(example_key)
        
        return coverage
    
    def _analyze_practical_applications(self) -> Dict:
        """Analyze practical applications and real-world examples"""
        applications = {
            'real_data_examples': [],
            'business_applications': [],
            'best_practices': [],
            'common_patterns': []
        }
        
        # Look for real data examples
        for example_key, example_content in self.content.items():
            for file_path, file_content in example_content['files'].items():
                content = file_content['content']
                
                # Look for real data file references
                if re.search(r'\.csv|\.txt|\.xlsx', content):
                    applications['real_data_examples'].append(f"{example_key}: {file_path}")
                
                # Look for business context
                if re.search(r'business|commercial|industry|company', content, re.IGNORECASE):
                    applications['business_applications'].append(f"{example_key}: {file_path}")
        
        return applications
    
    def get_examples_overview(self) -> Dict:
        """Get overview of all practical examples"""
        overview = {
            'total_examples': len(self.examples),
            'examples': {}
        }
        
        for example_key, example_info in self.examples.items():
            overview['examples'][example_key] = {
                'title': example_info['title'],
                'category': example_info['category'],
                'language': example_info['language'],
                'key_topics': example_info['key_topics'],
                'files_count': len(example_info['files']),
                'loaded': example_key in self.content
            }
        
        return overview
    
    def get_code_statistics(self) -> Dict:
        """Get code statistics across all examples"""
        return self.analysis_results['code_statistics']
    
    def get_language_comparison(self) -> Dict:
        """Get comparison between Python and R implementations"""
        return self.analysis_results['language_comparison']
    
    def get_topic_coverage(self) -> Dict:
        """Get topic coverage analysis"""
        return self.analysis_results['topic_coverage']
    
    def get_practical_applications(self) -> Dict:
        """Get practical applications analysis"""
        return self.analysis_results['practical_applications']
    
    def get_example_by_category(self, category: str) -> Dict:
        """Get examples by category (data_preparation, advanced_modeling, etc.)"""
        results = {
            'category': category,
            'examples': []
        }
        
        for example_key, example_info in self.examples.items():
            if example_info['category'] == category:
                example_data = {
                    'key': example_key,
                    'title': example_info['title'],
                    'language': example_info['language'],
                    'files': []
                }
                
                if example_key in self.content:
                    for file_path, file_content in self.content[example_key]['files'].items():
                        example_data['files'].append({
                            'path': file_path,
                            'code_chunks_count': len(file_content['code_chunks']),
                            'examples_count': len(file_content['examples'])
                        })
                
                results['examples'].append(example_data)
        
        return results
    
    def get_example_by_language(self, language: str) -> Dict:
        """Get examples by programming language"""
        results = {
            'language': language,
            'examples': []
        }
        
        for example_key, example_info in self.examples.items():
            if example_info['language'].lower() == language.lower():
                example_data = {
                    'key': example_key,
                    'title': example_info['title'],
                    'category': example_info['category'],
                    'files': []
                }
                
                if example_key in self.content:
                    for file_path, file_content in self.content[example_key]['files'].items():
                        example_data['files'].append({
                            'path': file_path,
                            'code_chunks_count': len(file_content['code_chunks']),
                            'examples_count': len(file_content['examples'])
                        })
                
                results['examples'].append(example_data)
        
        return results
    
    def get_code_chunks_by_topic(self, topic: str) -> Dict:
        """Get code chunks related to a specific topic"""
        results = {
            'topic': topic,
            'chunks': []
        }
        
        for example_key, example_content in self.content.items():
            for file_path, file_content in example_content['files'].items():
                for chunk in file_content['code_chunks']:
                    # Check if chunk content contains topic-related keywords
                    topic_keywords = {
                        'data_reading': ['read_csv', 'read_table', 'pd.read'],
                        'data_cleaning': ['clean', 'na.', 'missing', 'dropna'],
                        'data_visualization': ['plot', 'ggplot', 'visualization'],
                        'modeling': ['fit', 'model', 'regression', 'classification'],
                        'neural_networks': ['neuralnetwork', 'neural network', 'nnet', 'hidden.layers'],
                        'hyperparameter_tuning': ['hyperparameter', 'parameter tuning', 'grid search', 'learn.rates'],
                        'cross_validation': ['cross validation', 'cv', 'fold', 'holdout'],
                        'stacking': ['stacking', 'ensemble', 'meta-model', 'stack'],
                        'bayesian_methods': ['bayesian', 'stan', 'mcmc', 'posterior'],
                        'shap_analysis': ['shap', 'explain', 'interpret']
                    }
                    
                    if topic in topic_keywords:
                        keywords = topic_keywords[topic]
                        chunk_content_lower = chunk['content'].lower()
                        
                        if any(keyword.lower() in chunk_content_lower for keyword in keywords):
                            results['chunks'].append({
                                'example': example_key,
                                'file': file_path,
                                'chunk_name': chunk['name'],
                                'language': chunk['language'],
                                'content': chunk['content'][:500] + '...' if len(chunk['content']) > 500 else chunk['content']
                            })
        
        return results
    
    def search_practical_content(self, query: str) -> Dict:
        """Search across all practical examples"""
        results = {
            'query': query,
            'results': []
        }
        
        query_lower = query.lower()
        
        for example_key, example_info in self.examples.items():
            if example_key in self.content:
                for file_path, file_content in self.content[example_key]['files'].items():
                    content = file_content['content']
                    
                    # Search in content
                    if query_lower in content.lower():
                        # Find context around match
                        pos = content.lower().find(query_lower)
                        start = max(0, pos - 200)
                        end = min(len(content), pos + 200)
                        excerpt = content[start:end]
                        
                        results['results'].append({
                            'example': example_key,
                            'file': file_path,
                            'title': example_info['title'],
                            'language': example_info['language'],
                            'excerpt': excerpt,
                            'relevance_score': content.lower().count(query_lower)
                        })
        
        # Sort by relevance
        results['results'].sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return results
    
    def get_task_specific_examples(self, task_number: int) -> Dict:
        """Get examples relevant to specific ATPA tasks"""
        task_examples = {
            1: {
                'focus': 'Data preparation and quality',
                'relevant_examples': ['module_2_python', 'module_2_r', 'flights_prep'],
                'key_concepts': ['data_reading', 'data_cleaning', 'data_quality']
            },
            2: {
                'focus': 'Privacy and bias analysis',
                'relevant_examples': ['module_2_python', 'module_2_r'],
                'key_concepts': ['data_analysis', 'bias_detection']
            },
            3: {
                'focus': 'Model development and validation',
                'relevant_examples': ['module_3_advanced_r', 'module_2_python'],
                'key_concepts': ['modeling', 'validation', 'model_selection', 'cross_validation', 'hyperparameter_tuning']
            },
            4: {
                'focus': 'Model interpretation with SHAP',
                'relevant_examples': ['module_4_python', 'module_4_r'],
                'key_concepts': ['shap_analysis', 'model_interpretation', 'variable_importance']
            },
            5: {
                'focus': 'Advanced modeling techniques',
                'relevant_examples': ['module_3_advanced_r', 'module_4_python'],
                'key_concepts': ['advanced_modeling', 'model_comparison', 'neural_networks', 'stacking', 'bayesian_methods']
            },
            6: {
                'focus': 'Executive summary and communication',
                'relevant_examples': ['flights_prep', 'module_4_python'],
                'key_concepts': ['communication', 'visualization', 'interpretation']
            }
        }
        
        if task_number in task_examples:
            task_info = task_examples[task_number]
            
            # Get specific examples
            specific_examples = {
                'focus': task_info['focus'],
                'relevant_examples': task_info['relevant_examples'],
                'key_concepts': task_info['key_concepts'],
                'examples': []
            }
            
            for example_key in task_info['relevant_examples']:
                if example_key in self.content:
                    example_data = {
                        'key': example_key,
                        'title': self.examples[example_key]['title'],
                        'language': self.examples[example_key]['language'],
                        'files': []
                    }
                    
                    for file_path, file_content in self.content[example_key]['files'].items():
                        example_data['files'].append({
                            'path': file_path,
                            'code_chunks_count': len(file_content['code_chunks']),
                            'examples_count': len(file_content['examples'])
                        })
                    
                    specific_examples['examples'].append(example_data)
            
            return specific_examples
        
        return {'error': f'No examples available for task {task_number}'} 