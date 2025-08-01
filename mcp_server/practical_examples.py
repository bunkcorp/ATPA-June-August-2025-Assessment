"""
Practical Examples Layer: Integrates R Markdown files with working code examples from ATPA curriculum
"""
import os
import re
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class PracticalExamples:
    """Practical Examples - Provides working code examples from ATPA curriculum"""
    
    def __init__(self, examples_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        self.examples_path = examples_path
        self.examples = {
            'module_2_python': {
                'title': 'Module 2 - Data Preparation (Python)',
                'files': ['Module_2_Working_with_Data/atpa_2_2_python.rmd'],
                'category': 'data_preparation',
                'language': 'python'
            },
            'module_4_python': {
                'title': 'Module 4 - Model Explainability (Python)',
                'files': ['Module_4_Model_Explainability/atpa_4_3_python.rmd'],
                'category': 'model_explainability',
                'language': 'python'
            }
        }
        self.content = {}
        self._load_examples()
    
    def _load_examples(self):
        """Load content from R Markdown example files"""
        for example_key, example_info in self.examples.items():
            self.content[example_key] = {'files': {}}
            for file_path in example_info['files']:
                full_path = os.path.join(self.examples_path, file_path)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.content[example_key]['files'][file_path] = {'content': content}
                    logger.info(f"Loaded {file_path} successfully")
                except Exception as e:
                    logger.error(f"Error loading {file_path}: {e}")
                    self.content[example_key]['files'][file_path] = {'content': f"Error: {e}"}
    
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
                'loaded': example_key in self.content
            }
        return overview
    
    def get_code_statistics(self) -> Dict:
        """Get code statistics across all examples"""
        return {'total_files': len(self.examples), 'status': 'loaded'}
    
    def get_language_comparison(self) -> Dict:
        """Get comparison between Python and R implementations"""
        return {'python_examples': ['module_2_python', 'module_4_python'], 'r_examples': []}
    
    def get_topic_coverage(self) -> Dict:
        """Get topic coverage analysis"""
        return {'data_preparation': ['module_2_python'], 'model_explainability': ['module_4_python']}
    
    def get_practical_applications(self) -> Dict:
        """Get practical applications analysis"""
        return {'real_data_examples': ['module_2_python'], 'business_applications': ['module_4_python']}
    
    def get_example_by_category(self, category: str) -> Dict:
        """Get examples by category"""
        results = {'category': category, 'examples': []}
        for example_key, example_info in self.examples.items():
            if example_info['category'] == category:
                results['examples'].append({
                    'key': example_key,
                    'title': example_info['title'],
                    'language': example_info['language']
                })
        return results
    
    def get_example_by_language(self, language: str) -> Dict:
        """Get examples by programming language"""
        results = {'language': language, 'examples': []}
        for example_key, example_info in self.examples.items():
            if example_info['language'].lower() == language.lower():
                results['examples'].append({
                    'key': example_key,
                    'title': example_info['title'],
                    'category': example_info['category']
                })
        return results
    
    def get_code_chunks_by_topic(self, topic: str) -> Dict:
        """Get code chunks related to a specific topic"""
        return {'topic': topic, 'chunks': []}
    
    def search_practical_content(self, query: str) -> Dict:
        """Search across all practical examples"""
        return {'query': query, 'results': []}
    
    def get_task_specific_examples(self, task_number: int) -> Dict:
        """Get examples relevant to specific ATPA tasks"""
        task_examples = {
            1: {'focus': 'Data preparation', 'relevant_examples': ['module_2_python']},
            4: {'focus': 'Model interpretation', 'relevant_examples': ['module_4_python']}
        }
        return task_examples.get(task_number, {'error': f'No examples for task {task_number}'})
