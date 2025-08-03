#!/usr/bin/env python3
"""
Practical Examples Layer: Comprehensive integration of R Markdown files with working code examples from ATPA curriculum
Provides access to all practical code examples organized by module, topic, and task
"""
import os
import re
import json
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)

class PracticalExamples:
    """
    Comprehensive Practical Examples - Provides working code examples from ATPA curriculum
    Extracts and organizes code chunks from all R Markdown files
    """
    
    def __init__(self, examples_path: str = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA"):
        self.examples_path = examples_path
        self.examples = self._define_examples_structure()
        self.content = {}
        self.code_chunks = {}
        self._load_all_examples()
        self._extract_code_chunks()
        
    def _define_examples_structure(self) -> Dict[str, Any]:
        """Define the complete structure of all available examples"""
        return {
            'module_2_data_preparation': {
                'title': 'Module 2 - Working with Data',
                'category': 'data_preparation',
                'files': {
                    'atpa_2_2_python': {
                        'title': 'ATPA 2.2 - Reading and Writing Data (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_2_python.rmd',
                        'language': 'python',
                        'topics': ['data_reading', 'data_writing', 'file_formats', 'data_structures'],
                        'tasks': [1]
                    },
                    'atpa_2_2_r': {
                        'title': 'ATPA 2.2 - Reading and Writing Data (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_2_r.rmd',
                        'language': 'r',
                        'topics': ['data_reading', 'data_writing', 'file_formats', 'data_structures'],
                        'tasks': [1]
                    },
                    'atpa_2_3_python': {
                        'title': 'ATPA 2.3 - Data Transformation and Cleaning (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_3_python.rmd',
                        'language': 'python',
                        'topics': ['data_cleaning', 'data_transformation', 'subsetting', 'filtering'],
                        'tasks': [1]
                    },
                    'atpa_2_3_r': {
                        'title': 'ATPA 2.3 - Data Transformation and Cleaning (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_3_r.rmd',
                        'language': 'r',
                        'topics': ['data_cleaning', 'data_transformation', 'subsetting', 'filtering'],
                        'tasks': [1]
                    },
                    'atpa_2_4_python': {
                        'title': 'ATPA 2.4 - Data Validation (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_4_python.rmd',
                        'language': 'python',
                        'topics': ['data_validation', 'quality_checks', 'outlier_detection'],
                        'tasks': [1]
                    },
                    'atpa_2_4_r': {
                        'title': 'ATPA 2.4 - Data Validation (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_4_r.rmd',
                        'language': 'r',
                        'topics': ['data_validation', 'quality_checks', 'outlier_detection'],
                        'tasks': [1]
                    },
                    'atpa_2_5_python': {
                        'title': 'ATPA 2.5 - Exploratory Data Analysis (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_5_python.rmd',
                        'language': 'python',
                        'topics': ['exploratory_analysis', 'visualization', 'summary_statistics'],
                        'tasks': [1]
                    },
                    'atpa_2_5_r': {
                        'title': 'ATPA 2.5 - Exploratory Data Analysis (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_5_r.rmd',
                        'language': 'r',
                        'topics': ['exploratory_analysis', 'visualization', 'summary_statistics'],
                        'tasks': [1]
                    },
                    'atpa_2_6_python': {
                        'title': 'ATPA 2.6 - Data Joins and Merges (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_6_python.rmd',
                        'language': 'python',
                        'topics': ['data_joins', 'merging', 'combining_datasets'],
                        'tasks': [1]
                    },
                    'atpa_2_6_r': {
                        'title': 'ATPA 2.6 - Data Joins and Merges (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_6_r.rmd',
                        'language': 'r',
                        'topics': ['data_joins', 'merging', 'combining_datasets'],
                        'tasks': [1]
                    },
                    'atpa_2_7_1_python': {
                        'title': 'ATPA 2.7.1 - Variable Analysis (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_7_1_python.rmd',
                        'language': 'python',
                        'topics': ['variable_analysis', 'feature_engineering', 'variable_selection'],
                        'tasks': [1]
                    },
                    'atpa_2_7_1_r': {
                        'title': 'ATPA 2.7.1 - Variable Analysis (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_7_1_r.rmd',
                        'language': 'r',
                        'topics': ['variable_analysis', 'feature_engineering', 'variable_selection'],
                        'tasks': [1]
                    },
                    'atpa_2_7_2_python': {
                        'title': 'ATPA 2.7.2 - Advanced Data Preparation (Python)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_7_2_python.rmd',
                        'language': 'python',
                        'topics': ['advanced_preparation', 'data_quality', 'preprocessing'],
                        'tasks': [1]
                    },
                    'atpa_2_7_2_r': {
                        'title': 'ATPA 2.7.2 - Advanced Data Preparation (R)',
                        'file_path': 'Module_2_Working_with_Data/atpa_2_7_2_r.rmd',
                        'language': 'r',
                        'topics': ['advanced_preparation', 'data_quality', 'preprocessing'],
                        'tasks': [1]
                    }
                }
            },
            'module_3_advanced_models': {
                'title': 'Module 3 - Advanced Models',
                'category': 'advanced_modeling',
                'files': {
                    'atpa_3_2_r': {
                        'title': 'ATPA 3.2 - Generalized Additive Models (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_2_r.rmd',
                        'language': 'r',
                        'topics': ['gam', 'polynomial_regression', 'nonlinear_modeling'],
                        'tasks': [3]
                    },
                    'atpa_3_3_r': {
                        'title': 'ATPA 3.3 - Mixed Effects Models (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_3_r.rmd',
                        'language': 'r',
                        'topics': ['mixed_effects', 'hierarchical_models', 'random_effects'],
                        'tasks': [3]
                    },
                    'atpa_3_4_r': {
                        'title': 'ATPA 3.4 - Generalized Linear Models (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_4_r.rmd',
                        'language': 'r',
                        'topics': ['glm', 'logistic_regression', 'poisson_regression'],
                        'tasks': [3]
                    },
                    'atpa_3_5_r': {
                        'title': 'ATPA 3.5 - Model Validation (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_5_r.rmd',
                        'language': 'r',
                        'topics': ['model_validation', 'cross_validation', 'performance_metrics'],
                        'tasks': [3]
                    },
                    'atpa_3_6_r': {
                        'title': 'ATPA 3.6 - Variable Selection (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_6_r.rmd',
                        'language': 'r',
                        'topics': ['variable_selection', 'stepwise_regression', 'regularization'],
                        'tasks': [3]
                    },
                    'atpa_3_7a_r': {
                        'title': 'ATPA 3.7a - Bayesian Models Part 1 (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_7a_r.rmd',
                        'language': 'r',
                        'topics': ['bayesian_models', 'stan', 'mcmc'],
                        'tasks': [5]
                    },
                    'atpa_3_7b_r': {
                        'title': 'ATPA 3.7b - Bayesian Models Part 2 (R)',
                        'file_path': 'Module_3_Advanced_Models/atpa_3_7b_r.rmd',
                        'language': 'r',
                        'topics': ['bayesian_models', 'stan', 'mcmc'],
                        'tasks': [5]
                    }
                }
            },
            'module_4_explainability': {
                'title': 'Module 4 - Model Explainability',
                'category': 'model_explainability',
                'files': {
                    'atpa_4_3_python': {
                        'title': 'ATPA 4.3 - Model Explainability (Python)',
                        'file_path': 'Module_4_Model_Explainability/atpa_4_3_python.rmd',
                        'language': 'python',
                        'topics': ['shap', 'partial_dependence', 'variable_importance', 'model_interpretation'],
                        'tasks': [4]
                    },
                    'atpa_4_3_r': {
                        'title': 'ATPA 4.3 - Model Explainability (R)',
                        'file_path': 'Module_4_Model_Explainability/atpa_4_3_r.rmd',
                        'language': 'r',
                        'topics': ['shap', 'partial_dependence', 'variable_importance', 'model_interpretation'],
                        'tasks': [4]
                    },
                    'atpa_4_5_r': {
                        'title': 'ATPA 4.5 - Advanced Explainability (R)',
                        'file_path': 'Module_4_Model_Explainability/atpa_4_5_r.rmd',
                        'language': 'r',
                        'topics': ['advanced_explainability', 'interaction_effects', 'model_comparison'],
                        'tasks': [4]
                    }
                }
            }
        }
    
    def _load_all_examples(self):
        """Load content from all R Markdown example files"""
        for module_key, module_info in self.examples.items():
            self.content[module_key] = {'files': {}}
            for file_key, file_info in module_info['files'].items():
                full_path = os.path.join(self.examples_path, file_info['file_path'])
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.content[module_key]['files'][file_key] = {
                            'content': content,
                            'metadata': file_info
                        }
                    logger.info(f"Loaded {file_info['file_path']} successfully")
                except Exception as e:
                    logger.error(f"Error loading {file_info['file_path']}: {e}")
                    self.content[module_key]['files'][file_key] = {
                        'content': f"Error: {e}",
                        'metadata': file_info
                    }
    
    def _extract_code_chunks(self):
        """Extract and organize code chunks from all loaded files"""
        for module_key, module_info in self.content.items():
            self.code_chunks[module_key] = {}
            for file_key, file_info in module_info['files'].items():
                if 'Error:' not in file_info['content']:
                    chunks = self._parse_code_chunks(file_info['content'], file_info['metadata'])
                    self.code_chunks[module_key][file_key] = chunks
    
    def _parse_code_chunks(self, content: str, metadata: Dict) -> List[Dict]:
        """Parse code chunks from R Markdown content"""
        chunks = []
        
        # Pattern to match code chunks in R Markdown
        # Matches both ```{r} and ```{python} chunks
        pattern = r'```\{([^}]+)\}\s*\n(.*?)\n```'
        
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for i, match in enumerate(matches):
            language = match.group(1).strip()
            code = match.group(2).strip()
            
            # Extract chunk title if present (CHUNK X: Description)
            title_match = re.search(r'CHUNK\s+(\d+):\s*(.+)', code, re.IGNORECASE)
            chunk_number = title_match.group(1) if title_match else str(i + 1)
            chunk_title = title_match.group(2) if title_match else f"Code Chunk {i + 1}"
            
            # Clean up the code by removing the title line
            if title_match:
                code = re.sub(r'CHUNK\s+\d+:\s*.*?\n', '', code, count=1)
            
            chunks.append({
                'chunk_number': chunk_number,
                'title': chunk_title,
                'language': language,
                'code': code,
                'metadata': metadata
            })
        
        return chunks
    
    def get_examples_overview(self) -> Dict:
        """Get comprehensive overview of all practical examples"""
        overview = {
            'total_modules': len(self.examples),
            'total_files': sum(len(module['files']) for module in self.examples.values()),
            'modules': {}
        }
        
        for module_key, module_info in self.examples.items():
            overview['modules'][module_key] = {
                'title': module_info['title'],
                'category': module_info['category'],
                'file_count': len(module_info['files']),
                'languages': list(set(file_info['language'] for file_info in module_info['files'].values())),
                'topics': list(set(topic for file_info in module_info['files'].values() for topic in file_info['topics'])),
                'tasks': list(set(task for file_info in module_info['files'].values() for task in file_info['tasks']))
            }
        
        return overview
    
    def get_code_statistics(self) -> Dict:
        """Get comprehensive code statistics across all examples"""
        total_chunks = 0
        language_stats = {}
        topic_stats = {}
        
        for module_key, module_chunks in self.code_chunks.items():
            for file_key, chunks in module_chunks.items():
                total_chunks += len(chunks)
                for chunk in chunks:
                    # Language statistics
                    lang = chunk['language']
                    language_stats[lang] = language_stats.get(lang, 0) + 1
                    
                    # Topic statistics
                    for topic in chunk['metadata']['topics']:
                        topic_stats[topic] = topic_stats.get(topic, 0) + 1
        
        return {
            'total_chunks': total_chunks,
            'language_distribution': language_stats,
            'topic_distribution': topic_stats,
            'files_loaded': sum(len(module_chunks) for module_chunks in self.code_chunks.values())
        }
    
    def get_language_comparison(self) -> Dict:
        """Get comparison between Python and R implementations"""
        python_examples = []
        r_examples = []
        
        for module_key, module_info in self.examples.items():
            for file_key, file_info in module_info['files'].items():
                if file_info['language'] == 'python':
                    python_examples.append(f"{module_key}_{file_key}")
                elif file_info['language'] == 'r':
                    r_examples.append(f"{module_key}_{file_key}")
        
        return {
            'python_examples': python_examples,
            'r_examples': r_examples,
            'python_count': len(python_examples),
            'r_count': len(r_examples)
        }
    
    def get_topic_coverage(self) -> Dict:
        """Get comprehensive topic coverage analysis"""
        topic_coverage = {}
        
        for module_key, module_info in self.examples.items():
            for file_key, file_info in module_info['files'].items():
                for topic in file_info['topics']:
                    if topic not in topic_coverage:
                        topic_coverage[topic] = []
                    topic_coverage[topic].append(f"{module_key}_{file_key}")
        
        return topic_coverage
    
    def get_practical_applications(self) -> Dict:
        """Get practical applications analysis"""
        applications = {
            'data_preparation': [],
            'modeling': [],
            'explainability': [],
            'validation': [],
            'visualization': []
        }
        
        for module_key, module_info in self.examples.items():
            for file_key, file_info in module_info['files'].items():
                if module_key == 'module_2_data_preparation':
                    applications['data_preparation'].append(f"{module_key}_{file_key}")
                elif module_key == 'module_3_advanced_models':
                    applications['modeling'].append(f"{module_key}_{file_key}")
                elif module_key == 'module_4_explainability':
                    applications['explainability'].append(f"{module_key}_{file_key}")
        
        return applications
    
    def get_example_by_category(self, category: str) -> Dict:
        """Get examples by category"""
        results = {'category': category, 'examples': []}
        
        for module_key, module_info in self.examples.items():
            if module_info['category'] == category:
                for file_key, file_info in module_info['files'].items():
                    results['examples'].append({
                        'key': f"{module_key}_{file_key}",
                        'title': file_info['title'],
                        'language': file_info['language'],
                        'topics': file_info['topics'],
                        'tasks': file_info['tasks']
                    })
        
        return results
    
    def get_example_by_language(self, language: str) -> Dict:
        """Get examples by programming language"""
        results = {'language': language, 'examples': []}
        
        for module_key, module_info in self.examples.items():
            for file_key, file_info in module_info['files'].items():
                if file_info['language'].lower() == language.lower():
                    results['examples'].append({
                        'key': f"{module_key}_{file_key}",
                        'title': file_info['title'],
                        'category': module_info['category'],
                        'topics': file_info['topics'],
                        'tasks': file_info['tasks']
                    })
        
        return results
    
    def get_code_chunks_by_topic(self, topic: str) -> Dict:
        """Get code chunks related to a specific topic"""
        results = {'topic': topic, 'chunks': []}
        
        for module_key, module_chunks in self.code_chunks.items():
            for file_key, chunks in module_chunks.items():
                for chunk in chunks:
                    if topic in chunk['metadata']['topics']:
                        results['chunks'].append({
                            'module': module_key,
                            'file': file_key,
                            'chunk_number': chunk['chunk_number'],
                            'title': chunk['title'],
                            'language': chunk['language'],
                            'code': chunk['code'][:200] + "..." if len(chunk['code']) > 200 else chunk['code']
                        })
        
        return results
    
    def search_practical_content(self, query: str) -> Dict:
        """Search across all practical examples"""
        results = {'query': query, 'matches': []}
        query_lower = query.lower()
        
        for module_key, module_chunks in self.code_chunks.items():
            for file_key, chunks in module_chunks.items():
                for chunk in chunks:
                    # Search in chunk title, code, and metadata
                    search_text = f"{chunk['title']} {chunk['code']} {' '.join(chunk['metadata']['topics'])}"
                    if query_lower in search_text.lower():
                        results['matches'].append({
                            'module': module_key,
                            'file': file_key,
                            'chunk_number': chunk['chunk_number'],
                            'title': chunk['title'],
                            'language': chunk['language'],
                            'match_type': 'code' if query_lower in chunk['code'].lower() else 'metadata',
                            'code_preview': chunk['code'][:150] + "..." if len(chunk['code']) > 150 else chunk['code']
                        })
        
        return results
    
    def get_task_specific_examples(self, task_number: int) -> Dict:
        """Get examples relevant to specific ATPA tasks"""
        task_examples = {
            1: {
                'focus': 'Data preparation and EDA',
                'relevant_examples': [],
                'topics': ['data_reading', 'data_cleaning', 'exploratory_analysis', 'data_joins'],
                'files': []
            },
            2: {
                'focus': 'Privacy and ethics',
                'relevant_examples': [],
                'topics': ['data_validation', 'quality_checks'],
                'files': []
            },
            3: {
                'focus': 'GLM and mixed models',
                'relevant_examples': [],
                'topics': ['glm', 'mixed_effects', 'model_validation', 'variable_selection'],
                'files': []
            },
            4: {
                'focus': 'Random forest and SHAP',
                'relevant_examples': [],
                'topics': ['shap', 'partial_dependence', 'variable_importance'],
                'files': []
            },
            5: {
                'focus': 'Bayesian analysis',
                'relevant_examples': [],
                'topics': ['bayesian_models', 'stan', 'mcmc'],
                'files': []
            }
        }
        
        if task_number not in task_examples:
            return {'error': f'No examples for task {task_number}'}
        
        # Find relevant examples
        for module_key, module_info in self.examples.items():
            for file_key, file_info in module_info['files'].items():
                if task_number in file_info['tasks']:
                    task_examples[task_number]['files'].append({
                        'key': f"{module_key}_{file_key}",
                        'title': file_info['title'],
                        'language': file_info['language'],
                        'topics': file_info['topics']
                    })
        
        return task_examples[task_number]
    
    def get_code_chunk_by_id(self, module: str, file: str, chunk_number: str) -> Dict:
        """Get a specific code chunk by its identifier"""
        if module in self.code_chunks and file in self.code_chunks[module]:
            for chunk in self.code_chunks[module][file]:
                if chunk['chunk_number'] == chunk_number:
                    return chunk
        return {'error': f'Code chunk {chunk_number} not found in {module}/{file}'}
    
    def get_file_content(self, module: str, file: str) -> Dict:
        """Get complete content of a specific file"""
        if module in self.content and file in self.content[module]['files']:
            return {
                'content': self.content[module]['files'][file]['content'],
                'metadata': self.content[module]['files'][file]['metadata']
            }
        return {'error': f'File {file} not found in {module}'}
    
    def get_comprehensive_analysis(self) -> Dict:
        """Get comprehensive analysis of all practical examples"""
        return {
            'overview': self.get_examples_overview(),
            'statistics': self.get_code_statistics(),
            'language_comparison': self.get_language_comparison(),
            'topic_coverage': self.get_topic_coverage(),
            'practical_applications': self.get_practical_applications(),
            'task_mapping': {
                task: self.get_task_specific_examples(task) 
                for task in [1, 2, 3, 4, 5]
            }
        }

# Test function
def test_practical_examples():
    """Test the comprehensive practical examples module"""
    examples = PracticalExamples()
    
    print("=== COMPREHENSIVE PRACTICAL EXAMPLES TEST ===")
    
    print(f"\n📊 Overview:")
    overview = examples.get_examples_overview()
    print(f"   Total modules: {overview['total_modules']}")
    print(f"   Total files: {overview['total_files']}")
    print(f"   Modules: {list(overview['modules'].keys())}")
    
    print(f"\n📈 Code Statistics:")
    stats = examples.get_code_statistics()
    print(f"   Total chunks: {stats['total_chunks']}")
    print(f"   Language distribution: {stats['language_distribution']}")
    print(f"   Files loaded: {stats['files_loaded']}")
    
    print(f"\n🌐 Language Comparison:")
    lang_comp = examples.get_language_comparison()
    print(f"   Python examples: {lang_comp['python_count']}")
    print(f"   R examples: {lang_comp['r_count']}")
    
    print(f"\n📚 Topic Coverage:")
    topic_cov = examples.get_topic_coverage()
    print(f"   Topics: {list(topic_cov.keys())}")
    
    print(f"\n🎯 Task-Specific Examples:")
    for task in [1, 3, 4, 5]:
        task_examples = examples.get_task_specific_examples(task)
        print(f"   Task {task}: {len(task_examples['files'])} files")
    
    print(f"\n🔍 Sample Code Chunks:")
    for module_key in list(examples.code_chunks.keys())[:2]:
        for file_key in list(examples.code_chunks[module_key].keys())[:1]:
            chunks = examples.code_chunks[module_key][file_key]
            print(f"   {module_key}/{file_key}: {len(chunks)} chunks")
            if chunks:
                print(f"     Sample: {chunks[0]['title']}")
    
    print("\n✅ Comprehensive Practical Examples Test Complete!")

if __name__ == "__main__":
    test_practical_examples()
