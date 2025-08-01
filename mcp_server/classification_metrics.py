"""
Classification Metrics Layer: Comprehensive binary classification evaluation metrics
"""
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
import logging
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_auc_score, 
    precision_score, recall_score, f1_score, accuracy_score,
    roc_curve, precision_recall_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger(__name__)

class ClassificationMetrics:
    """
    Classification Metrics - Comprehensive evaluation for binary classification problems
    
    Essential metrics for arrest prediction with class imbalance:
    - Confusion Matrix (True Positives, False Positives, True Negatives, False Negatives)
    - Sensitivity (Recall) - Ability to identify actual arrests
    - Specificity - Ability to identify non-arrests
    - Precision - Accuracy of positive predictions
    - F1-Score - Harmonic mean of precision and recall
    - ROC-AUC - Overall model discrimination ability
    """
    
    def __init__(self):
        """Initialize classification metrics calculator"""
        self.metrics_history = {}
        self.confusion_matrices = {}
        self.roc_curves = {}
        self.precision_recall_curves = {}
    
    def calculate_comprehensive_metrics(self, y_true: np.ndarray, y_pred: np.ndarray, 
                                      y_pred_proba: Optional[np.ndarray] = None,
                                      model_name: str = "Model") -> Dict:
        """
        Calculate comprehensive classification metrics
        
        Args:
            y_true: True labels (0 or 1)
            y_pred: Predicted labels (0 or 1)
            y_pred_proba: Predicted probabilities (optional)
            model_name: Name of the model for tracking
            
        Returns:
            Dictionary with all classification metrics
        """
        try:
            # Basic metrics
            accuracy = accuracy_score(y_true, y_pred)
            
            # Confusion matrix
            cm = confusion_matrix(y_true, y_pred)
            tn, fp, fn, tp = cm.ravel()
            
            # Essential binary classification metrics
            sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0  # Recall
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = sensitivity  # Same as sensitivity
            
            # F1-score
            f1 = f1_score(y_true, y_pred)
            
            # Additional metrics
            balanced_accuracy = (sensitivity + specificity) / 2
            positive_predictive_value = precision
            negative_predictive_value = tn / (tn + fn) if (tn + fn) > 0 else 0
            
            # ROC-AUC if probabilities available
            roc_auc = None
            if y_pred_proba is not None:
                roc_auc = roc_auc_score(y_true, y_pred_proba)
            
            # Store results
            metrics = {
                'model_name': model_name,
                'accuracy': accuracy,
                'sensitivity': sensitivity,
                'specificity': specificity,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'balanced_accuracy': balanced_accuracy,
                'positive_predictive_value': positive_predictive_value,
                'negative_predictive_value': negative_predictive_value,
                'roc_auc': roc_auc,
                'confusion_matrix': {
                    'true_negatives': tn,
                    'false_positives': fp,
                    'false_negatives': fn,
                    'true_positives': tp,
                    'matrix': cm.tolist()
                },
                'class_distribution': {
                    'total_samples': len(y_true),
                    'positive_class': int(np.sum(y_true)),
                    'negative_class': int(len(y_true) - np.sum(y_true)),
                    'positive_rate': float(np.mean(y_true))
                }
            }
            
            # Store in history
            self.metrics_history[model_name] = metrics
            self.confusion_matrices[model_name] = cm
            
            logger.info(f"Calculated comprehensive metrics for {model_name}")
            return metrics
            
        except Exception as e:
            logger.error(f"Error calculating metrics for {model_name}: {e}")
            return {'error': str(e)}
    
    def compare_models(self, model_results: Dict[str, Dict]) -> Dict:
        """
        Compare multiple models using comprehensive metrics
        
        Args:
            model_results: Dictionary with model names as keys and metrics as values
            
        Returns:
            Comparison summary
        """
        comparison = {
            'model_comparison': {},
            'best_models': {},
            'recommendations': []
        }
        
        # Compare each metric across models
        metrics_to_compare = ['accuracy', 'sensitivity', 'specificity', 'precision', 
                             'f1_score', 'balanced_accuracy', 'roc_auc']
        
        for metric in metrics_to_compare:
            metric_values = {}
            for model_name, metrics in model_results.items():
                if metric in metrics and metrics[metric] is not None:
                    metric_values[model_name] = metrics[metric]
            
            if metric_values:
                best_model = max(metric_values.items(), key=lambda x: x[1])
                comparison['best_models'][metric] = {
                    'model': best_model[0],
                    'value': best_model[1]
                }
        
        # Generate recommendations
        recommendations = []
        
        # Check for class imbalance considerations
        for model_name, metrics in model_results.items():
            positive_rate = metrics.get('class_distribution', {}).get('positive_rate', 0)
            if positive_rate < 0.2:  # Class imbalance
                recommendations.append(f"{model_name}: Consider using balanced_accuracy or F1-score due to class imbalance ({positive_rate:.1%} positive rate)")
        
        # Check for high false positive/negative rates
        for model_name, metrics in model_results.items():
            cm = metrics.get('confusion_matrix', {})
            if cm:
                fp_rate = cm['false_positives'] / (cm['false_positives'] + cm['true_negatives']) if (cm['false_positives'] + cm['true_negatives']) > 0 else 0
                fn_rate = cm['false_negatives'] / (cm['false_negatives'] + cm['true_positives']) if (cm['false_negatives'] + cm['true_positives']) > 0 else 0
                
                if fp_rate > 0.3:
                    recommendations.append(f"{model_name}: High false positive rate ({fp_rate:.1%}) - consider adjusting threshold")
                if fn_rate > 0.3:
                    recommendations.append(f"{model_name}: High false negative rate ({fn_rate:.1%}) - consider adjusting threshold")
        
        comparison['recommendations'] = recommendations
        return comparison
    
    def generate_confusion_matrix_plot(self, cm: np.ndarray, model_name: str = "Model") -> str:
        """
        Generate confusion matrix visualization
        
        Args:
            cm: Confusion matrix
            model_name: Name of the model
            
        Returns:
            HTML string with confusion matrix plot
        """
        try:
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=['No Arrest', 'Arrest'],
                       yticklabels=['No Arrest', 'Arrest'])
            plt.title(f'Confusion Matrix - {model_name}')
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            
            # Add metrics text
            tn, fp, fn, tp = cm.ravel()
            sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            
            metrics_text = f'Sensitivity: {sensitivity:.3f}\nSpecificity: {specificity:.3f}\nPrecision: {precision:.3f}'
            plt.figtext(0.02, 0.02, metrics_text, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            
            # Save plot
            plot_path = f"confusion_matrix_{model_name.replace(' ', '_')}.png"
            plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            return plot_path
            
        except Exception as e:
            logger.error(f"Error generating confusion matrix plot: {e}")
            return f"Error: {str(e)}"
    
    def get_arrest_prediction_interpretation(self, metrics: Dict) -> Dict:
        """
        Provide business interpretation for arrest prediction metrics
        
        Args:
            metrics: Classification metrics dictionary
            
        Returns:
            Business interpretation
        """
        cm = metrics.get('confusion_matrix', {})
        sensitivity = metrics.get('sensitivity', 0)
        specificity = metrics.get('specificity', 0)
        precision = metrics.get('precision', 0)
        
        interpretation = {
            'business_impact': {},
            'policy_implications': [],
            'risk_assessment': {},
            'recommendations': []
        }
        
        # Business impact analysis
        if cm:
            tn, fp, fn, tp = cm['true_negatives'], cm['false_positives'], cm['false_negatives'], cm['true_positives']
            
            interpretation['business_impact'] = {
                'true_positives': f"{tp} actual arrests correctly identified",
                'false_positives': f"{fp} non-arrests incorrectly flagged as arrests",
                'false_negatives': f"{fn} actual arrests missed by the model",
                'true_negatives': f"{tn} non-arrests correctly identified"
            }
        
        # Policy implications
        if sensitivity < 0.7:
            interpretation['policy_implications'].append(
                "Low sensitivity: Model misses many actual arrests - may need intervention"
            )
        if specificity < 0.7:
            interpretation['policy_implications'].append(
                "Low specificity: Model incorrectly flags many non-arrests - may waste resources"
            )
        if precision < 0.7:
            interpretation['policy_implications'].append(
                "Low precision: Many predicted arrests are false alarms - may reduce trust"
            )
        
        # Risk assessment
        interpretation['risk_assessment'] = {
            'high_risk_scenarios': [],
            'low_risk_scenarios': [],
            'uncertainty_level': 'medium'
        }
        
        if sensitivity > 0.8 and specificity > 0.8:
            interpretation['risk_assessment']['uncertainty_level'] = 'low'
            interpretation['risk_assessment']['low_risk_scenarios'].append(
                "Model performs well across all metrics - suitable for operational use"
            )
        elif sensitivity < 0.6 or specificity < 0.6:
            interpretation['risk_assessment']['uncertainty_level'] = 'high'
            interpretation['risk_assessment']['high_risk_scenarios'].append(
                "Model has significant limitations - requires careful validation before deployment"
            )
        
        # Recommendations
        if sensitivity < 0.7:
            interpretation['recommendations'].append(
                "Consider collecting additional features to improve arrest detection"
            )
        if specificity < 0.7:
            interpretation['recommendations'].append(
                "Review model threshold to reduce false positive predictions"
            )
        if precision < 0.7:
            interpretation['recommendations'].append(
                "Implement additional validation steps before acting on predictions"
            )
        
        return interpretation
    
    def get_metrics_summary_table(self, model_results: Dict[str, Dict]) -> pd.DataFrame:
        """
        Create a summary table of all metrics for all models
        
        Args:
            model_results: Dictionary with model results
            
        Returns:
            Pandas DataFrame with metrics summary
        """
        summary_data = []
        
        for model_name, metrics in model_results.items():
            row = {
                'Model': model_name,
                'Accuracy': f"{metrics.get('accuracy', 0):.3f}",
                'Sensitivity': f"{metrics.get('sensitivity', 0):.3f}",
                'Specificity': f"{metrics.get('specificity', 0):.3f}",
                'Precision': f"{metrics.get('precision', 0):.3f}",
                'F1-Score': f"{metrics.get('f1_score', 0):.3f}",
                'Balanced Accuracy': f"{metrics.get('balanced_accuracy', 0):.3f}",
                'ROC-AUC': f"{metrics.get('roc_auc', 'N/A')}",
                'Positive Rate': f"{metrics.get('class_distribution', {}).get('positive_rate', 0):.1%}"
            }
            summary_data.append(row)
        
        return pd.DataFrame(summary_data)
    
    def get_atpa_task_guidance(self, task_number: int) -> Dict:
        """
        Provide ATPA task-specific guidance for classification metrics
        
        Args:
            task_number: ATPA task number (1-6)
            
        Returns:
            Task-specific guidance
        """
        guidance = {
            1: {
                'focus': 'Data preparation and target variable definition',
                'metrics_importance': 'Low - focus on data quality and target definition',
                'key_considerations': [
                    'Ensure ARREST target is correctly defined (19% arrest rate)',
                    'Check for class imbalance in target variable',
                    'Document data quality issues affecting model performance'
                ]
            },
            2: {
                'focus': 'Privacy and ethics analysis',
                'metrics_importance': 'Low - focus on ethical considerations',
                'key_considerations': [
                    'Consider fairness metrics across demographic groups',
                    'Assess potential bias in model predictions',
                    'Document ethical implications of false positives/negatives'
                ]
            },
            3: {
                'focus': 'GLM and mixed models',
                'metrics_importance': 'High - comprehensive model evaluation',
                'key_considerations': [
                    'Compare accuracy, sensitivity, specificity across models',
                    'Consider class imbalance in model selection',
                    'Use balanced accuracy or F1-score for imbalanced data',
                    'Document model assumptions and limitations'
                ]
            },
            4: {
                'focus': 'Random Forest and SHAP analysis',
                'metrics_importance': 'High - advanced model evaluation',
                'key_considerations': [
                    'Include confusion matrix with SHAP analysis',
                    'Compare feature importance with model performance',
                    'Assess model interpretability vs. performance trade-offs',
                    'Document business implications of predictions'
                ]
            },
            5: {
                'focus': 'Bayesian analysis',
                'metrics_importance': 'Medium - focus on uncertainty quantification',
                'key_considerations': [
                    'Include credible intervals for performance metrics',
                    'Compare Bayesian vs. frequentist model performance',
                    'Document uncertainty in predictions',
                    'Assess robustness of conclusions'
                ]
            },
            6: {
                'focus': 'Executive summary and communication',
                'metrics_importance': 'High - business interpretation',
                'key_considerations': [
                    'Translate technical metrics to business language',
                    'Focus on policy implications of model performance',
                    'Provide clear recommendations based on metrics',
                    'Address limitations and uncertainties'
                ]
            }
        }
        
        return guidance.get(task_number, {'error': f'No guidance for task {task_number}'}) 