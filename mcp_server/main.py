"""
Main FastAPI application for ATPA MCP Server
"""
from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn
import logging
import os
from typing import Optional, Dict, List
from pydantic import BaseModel

# Import our MCP layers
from context import DataContext
from loader import DataLoader
from protocol import DataProtocol
from insights import DataInsights
from ethics import EthicsFramework
from curriculum import ATPACurriculum
from exam_analysis import ExamAnalysis
from professional_resources import ProfessionalResources
from practical_examples import PracticalExamples
from classification_metrics import ClassificationMetrics
from task_implementation import ATPATaskImplementation
from task2_specialized import Task2SpecializedSearch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ATPA MCP Server",
    description="Model-Context-Protocol server for criminal incident and arrest data analysis",
    version="1.0.0"
)

# Data paths
DATA_DIR = "../Task1_DataPrep"
DATA_DICT_PATH = os.path.join(DATA_DIR, "Data_Dictionary.xlsx")
INCIDENTS_PATH = os.path.join(DATA_DIR, "incidents.csv")
ARRESTEE_PATH = os.path.join(DATA_DIR, "arrestee.csv")

# Initialize MCP layers
try:
    context = DataContext(DATA_DICT_PATH)
    loader = DataLoader(INCIDENTS_PATH, ARRESTEE_PATH)
    protocol = DataProtocol(loader)
    insights = DataInsights(protocol)
    ethics = EthicsFramework()
    curriculum = ATPACurriculum()
    exam_analysis = ExamAnalysis()
    professional_resources = ProfessionalResources()
    practical_examples = PracticalExamples()
    classification_metrics = ClassificationMetrics()
    task_implementation = ATPATaskImplementation(loader, protocol)
    task2_specialized = Task2SpecializedSearch()
    logger.info("MCP layers initialized successfully")
except Exception as e:
    logger.error(f"Error initializing MCP layers: {e}")
    context = None
    loader = None
    protocol = None
    insights = None
    ethics = None
    curriculum = None
    exam_analysis = None
    professional_resources = None
    practical_examples = None
    classification_metrics = None
    task_implementation = None
    task2_specialized = None

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pydantic models for request/response
class FilterRequest(BaseModel):
    column: str
    value: str
    operator: str = "eq"  # eq, gt, lt, gte, lte

class PaginationRequest(BaseModel):
    page: int = 1
    page_size: int = 100
    filters: Optional[List[FilterRequest]] = None

# ============================================================================
# CONTEXT LAYER ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint with server information"""
    return {
        "message": "ATPA MCP Server",
        "description": "Model-Context-Protocol server for criminal incident and arrest data analysis",
        "version": "1.0.0",
        "endpoints": {
            "context": "/fields",
            "task2_specialized": "/task2",
            "model": "/data",
            "protocol": "/merged",
            "insights": "/eda/summary"
        }
    }

@app.get("/fields")
async def get_fields():
    """Get metadata for all fields from the data dictionary"""
    if not context:
        raise HTTPException(status_code=500, detail="Context layer not initialized")
    
    return {
        "field_metadata": context.get_all_fields(),
        "field_summary": context.get_field_summary(),
        "incident_fields": context.get_incident_fields(),
        "arrestee_fields": context.get_arrestee_fields()
    }

@app.get("/fields/{field_name}")
async def get_field_metadata(field_name: str):
    """Get metadata for a specific field"""
    if not context:
        raise HTTPException(status_code=500, detail="Context layer not initialized")
    
    metadata = context.get_field_metadata(field_name)
    if not metadata:
        raise HTTPException(status_code=404, detail=f"Field {field_name} not found")
    
    return metadata

@app.get("/fields/source/{source}")
async def get_fields_by_source(source: str):
    """Get all fields from a specific source file"""
    if not context:
        raise HTTPException(status_code=500, detail="Context layer not initialized")
    
    return context.get_fields_by_source(source)

# ============================================================================
# MODEL LAYER ENDPOINTS
# ============================================================================

@app.get("/data/incidents")
async def get_incidents_data(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    sample_size: Optional[int] = Query(None, ge=100, le=10000)
):
    """Get paginated incidents data"""
    if not loader:
        raise HTTPException(status_code=500, detail="Loader layer not initialized")
    
    try:
        # Load data if not already loaded
        if loader.incidents_df is None:
            loader.load_incidents(sample_size)
        
        # Clean data if not already cleaned
        if not loader.incidents_cleaned:
            loader.clean_incidents_data()
        
        return loader.get_paginated_data('incidents', page, page_size)
    
    except Exception as e:
        logger.error(f"Error getting incidents data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/arrestee")
async def get_arrestee_data(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    sample_size: Optional[int] = Query(None, ge=100, le=10000)
):
    """Get paginated arrestee data"""
    if not loader:
        raise HTTPException(status_code=500, detail="Loader layer not initialized")
    
    try:
        # Load data if not already loaded
        if loader.arrestee_df is None:
            loader.load_arrestee(sample_size)
        
        # Clean data if not already cleaned
        if not loader.arrestee_cleaned:
            loader.clean_arrestee_data()
        
        return loader.get_paginated_data('arrestee', page, page_size)
    
    except Exception as e:
        logger.error(f"Error getting arrestee data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/summary")
async def get_data_summary():
    """Get summary statistics for both datasets"""
    if not loader:
        raise HTTPException(status_code=500, detail="Loader layer not initialized")
    
    return loader.get_data_summary()

# ============================================================================
# PROTOCOL LAYER ENDPOINTS
# ============================================================================

@app.post("/merged/create")
async def create_merged_dataset(sample_size: Optional[int] = Query(None, ge=100, le=50000)):
    """Create the merged dataset with ARREST target variable"""
    if not protocol:
        raise HTTPException(status_code=500, detail="Protocol layer not initialized")
    
    try:
        merged_df = protocol.create_merged_dataset(sample_size)
        return {
            "message": "Merged dataset created successfully",
            "records": len(merged_df),
            "columns": len(merged_df.columns),
            "arrest_rate": float(merged_df['ARREST'].mean())
        }
    
    except Exception as e:
        logger.error(f"Error creating merged dataset: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/merged/data")
async def get_merged_data(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000)
):
    """Get paginated merged data"""
    if not protocol:
        raise HTTPException(status_code=500, detail="Protocol layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    try:
        return protocol.get_paginated_merged_data(page, page_size)
    
    except Exception as e:
        logger.error(f"Error getting merged data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/merged/summary")
async def get_merged_summary():
    """Get summary statistics for the merged dataset"""
    if not protocol:
        raise HTTPException(status_code=500, detail="Protocol layer not initialized")
    
    return protocol.get_merged_summary()

@app.get("/merged/arrest-analysis")
async def get_arrest_analysis():
    """Get detailed analysis of arrest patterns"""
    if not protocol:
        raise HTTPException(status_code=500, detail="Protocol layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return protocol.get_arrest_analysis()

# ============================================================================
# INSIGHTS LAYER ENDPOINTS
# ============================================================================

@app.get("/eda/summary")
async def get_eda_summary():
    """Get comprehensive EDA summary statistics"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.get_summary_statistics()

@app.get("/eda/arrest-rate-viz")
async def get_arrest_rate_visualization():
    """Get arrest rate visualization by crime type"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.create_arrest_rate_visualization()

@app.get("/eda/temporal-analysis")
async def get_temporal_analysis():
    """Get temporal analysis visualizations"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.create_temporal_analysis()

@app.get("/eda/correlation-analysis")
async def get_correlation_analysis():
    """Get correlation analysis for numerical variables"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.create_correlation_analysis()

@app.get("/eda/feature-importance")
async def get_feature_importance():
    """Get feature importance analysis for predicting arrests"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.create_feature_importance_analysis()

@app.get("/eda/reasonability-checks")
async def get_reasonability_checks():
    """Get reasonability checks on the data"""
    if not insights:
        raise HTTPException(status_code=500, detail="Insights layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return insights.get_reasonability_checks()

# ============================================================================
# ETHICS LAYER ENDPOINTS
# ============================================================================

@app.get("/ethics/framework")
async def get_ethics_framework():
    """Get the ATPA Module 1 ethics framework"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    return {
        'principles': ethics.ethical_principles,
        'regulations': ethics.regulations,
        'protected_classes': ethics.protected_classes
    }

@app.get("/ethics/protected-variables")
async def get_protected_variables():
    """Identify protected variables in the merged dataset"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return ethics.identify_protected_variables(protocol.merged_df)

@app.get("/ethics/bias-assessment")
async def get_bias_assessment():
    """Get comprehensive bias assessment of the dataset"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return ethics.assess_data_bias(protocol.merged_df)

@app.get("/ethics/fairness-metrics")
async def get_fairness_metrics():
    """Get fairness metrics for the ARREST target variable"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return ethics.assess_model_fairness(protocol.merged_df, 'arrest')

@app.get("/ethics/recommendations")
async def get_ethical_recommendations():
    """Get ethical recommendations based on data analysis"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return ethics.generate_ethical_recommendations(protocol.merged_df)

@app.get("/ethics/summary")
async def get_ethical_summary():
    """Get comprehensive ethical summary"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    if not protocol.merged_created:
        raise HTTPException(status_code=400, detail="Merged dataset not created. Call /merged/create first.")
    
    return ethics.create_ethical_summary(protocol.merged_df)

@app.get("/ethics/compliance-checklist")
async def get_compliance_checklist():
    """Get ATPA compliance checklist"""
    if not ethics:
        raise HTTPException(status_code=500, detail="Ethics layer not initialized")
    
    return ethics._create_compliance_checklist()

# ============================================================================
# CURRICULUM LAYER ENDPOINTS
# ============================================================================

@app.get("/curriculum/overview")
async def get_curriculum_overview():
    """Get overview of all ATPA modules"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_module_overview()

@app.get("/curriculum/module/{module_key}")
async def get_module_content(module_key: str):
    """Get content for a specific module"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_module_content(module_key)

@app.get("/curriculum/search")
async def search_curriculum(query: str = Query(..., description="Search query")):
    """Search across all modules for specific content"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.search_curriculum(query)

@app.get("/curriculum/learning-objectives")
async def get_learning_objectives():
    """Get learning objectives for all modules"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_learning_objectives()

@app.get("/curriculum/ethical-framework")
async def get_ethical_framework_details():
    """Get detailed ethical framework from Module 1"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_ethical_framework_details()

@app.get("/curriculum/modeling-techniques")
async def get_modeling_techniques():
    """Get modeling techniques from Module 3"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_modeling_techniques()

@app.get("/curriculum/explainability-techniques")
async def get_explainability_techniques():
    """Get explainability techniques from Module 4"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_explainability_techniques()

@app.get("/curriculum/data-quality-guidelines")
async def get_data_quality_guidelines():
    """Get data quality guidelines from Module 2"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_data_quality_guidelines()

@app.get("/curriculum/summary")
async def get_curriculum_summary():
    """Get comprehensive curriculum summary"""
    if not curriculum:
        raise HTTPException(status_code=500, detail="Curriculum layer not initialized")
    
    return curriculum.get_curriculum_summary()

# ============================================================================
# TASK 2 SPECIALIZED ENDPOINTS
# ============================================================================

@app.get("/task2/demographic-benefits-risks")
async def get_demographic_benefits_risks():
    """Get content about benefits and risks of demographic data in criminal justice"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    return task2_specialized.search_demographic_data_benefits_risks()

@app.get("/task2/professional-standards-misuse")
async def get_professional_standards_misuse():
    """Get content about professional standards and misuse prevention"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    return task2_specialized.search_professional_standards_misuse_prevention()

@app.get("/task2/criminal-justice-context")
async def get_criminal_justice_context():
    """Get criminal justice specific content"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    return task2_specialized.search_criminal_justice_specific()

@app.get("/task2/structured-content")
async def get_task2_structured_content():
    """Get all Task 2 structured content organized by requirements"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    return task2_specialized.get_task2_structured_content()

@app.get("/task2/demographic-terms")
async def search_specific_demographic_terms(terms: str = Query(..., description="Comma-separated demographic terms")):
    """Search for specific demographic terms"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    term_list = [term.strip() for term in terms.split(",")]
    return task2_specialized.search_specific_demographic_terms(term_list)

@app.get("/task2/nminsights-guidance")
async def get_nminsights_guidance():
    """Get guidance specific to NMInsights as a trusted research organization"""
    if not task2_specialized:
        raise HTTPException(status_code=500, detail="Task 2 specialized layer not initialized")
    
    return task2_specialized.get_nminsights_specific_guidance()

# ============================================================================
# EXAM ANALYSIS LAYER ENDPOINTS
# ============================================================================

@app.get("/exam/overview")
async def get_exam_overview():
    """Get overview of all exam documents"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_exam_overview()

@app.get("/exam/task-analysis")
async def get_task_analysis():
    """Get comprehensive task analysis"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_task_analysis()

@app.get("/exam/writing-guidelines")
async def get_writing_guidelines():
    """Get writing and communication guidelines"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_writing_guidelines()

@app.get("/exam/technical-guidelines")
async def get_technical_guidelines():
    """Get technical methodology guidelines"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_technical_guidelines()

@app.get("/exam/grading-insights")
async def get_grading_insights():
    """Get grading and evaluation insights"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_grading_insights()

@app.get("/exam/current-assignment")
async def get_current_assignment_analysis():
    """Get specific analysis of current assignment (June-August 2025)"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_current_assignment_analysis()

@app.get("/exam/comparative-analysis")
async def get_comparative_analysis():
    """Get comparative analysis across all exams"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.get_comparative_analysis()

@app.get("/exam/search")
async def search_exam_content(query: str = Query(..., description="Search query")):
    """Search across all exam documents"""
    if not exam_analysis:
        raise HTTPException(status_code=500, detail="Exam analysis layer not initialized")
    
    return exam_analysis.search_exam_content(query)

# ============================================================================
# PROFESSIONAL RESOURCES LAYER ENDPOINTS
# ============================================================================

@app.get("/professional/overview")
async def get_professional_resources_overview():
    """Get overview of all professional resources"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_resources_overview()

@app.get("/professional/shap-guide")
async def get_shap_analysis_guide():
    """Get SHAP analysis methodology and guidelines"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_shap_analysis_guide()

@app.get("/professional/executive-summary-template")
async def get_executive_summary_template():
    """Get executive summary template and guidelines"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_executive_summary_template()

@app.get("/professional/asop-standards")
async def get_asop_standards():
    """Get ASOP 41 communication standards"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_asop_standards()

@app.get("/professional/task-guidance/{task_number}")
async def get_task_specific_guidance(task_number: int):
    """Get guidance specific to ATPA task numbers"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_task_specific_guidance(task_number)

@app.get("/professional/communication-checklist")
async def get_communication_checklist():
    """Get comprehensive communication checklist based on ASOP standards"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_communication_checklist()

@app.get("/professional/cross-references")
async def get_cross_references():
    """Get cross-references between resources"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.get_cross_references()

@app.get("/professional/search")
async def search_professional_content(query: str = Query(..., description="Search query")):
    """Search across all professional resources"""
    if not professional_resources:
        raise HTTPException(status_code=500, detail="Professional resources layer not initialized")
    
    return professional_resources.search_professional_content(query)

# ============================================================================
# PRACTICAL EXAMPLES LAYER ENDPOINTS
# ============================================================================

@app.get("/examples/overview")
async def get_practical_examples_overview():
    """Get overview of all practical examples"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_examples_overview()

@app.get("/examples/code-statistics")
async def get_code_statistics():
    """Get code statistics across all examples"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_code_statistics()

@app.get("/examples/language-comparison")
async def get_language_comparison():
    """Get comparison between Python and R implementations"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_language_comparison()

@app.get("/examples/topic-coverage")
async def get_topic_coverage():
    """Get topic coverage analysis"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_topic_coverage()

@app.get("/examples/practical-applications")
async def get_practical_applications():
    """Get practical applications analysis"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_practical_applications()

@app.get("/examples/category/{category}")
async def get_examples_by_category(category: str):
    """Get examples by category (data_preparation, advanced_modeling, etc.)"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_example_by_category(category)

@app.get("/examples/language/{language}")
async def get_examples_by_language(language: str):
    """Get examples by programming language"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_example_by_language(language)

@app.get("/examples/topic/{topic}")
async def get_code_chunks_by_topic(topic: str):
    """Get code chunks related to a specific topic"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_code_chunks_by_topic(topic)

@app.get("/examples/task/{task_number}")
async def get_task_specific_examples(task_number: int):
    """Get examples relevant to specific ATPA tasks"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.get_task_specific_examples(task_number)

@app.get("/examples/search")
async def search_practical_content(query: str = Query(..., description="Search query")):
    """Search across all practical examples"""
    if not practical_examples:
        raise HTTPException(status_code=500, detail="Practical examples layer not initialized")
    
    return practical_examples.search_practical_content(query)

# ============================================================================
# CLASSIFICATION METRICS LAYER ENDPOINTS
# ============================================================================

@app.post("/metrics/calculate")
async def calculate_classification_metrics(
    y_true: List[int],
    y_pred: List[int],
    y_pred_proba: Optional[List[float]] = None,
    model_name: str = "Model"
):
    """Calculate comprehensive classification metrics"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    try:
        y_true_array = np.array(y_true)
        y_pred_array = np.array(y_pred)
        y_pred_proba_array = np.array(y_pred_proba) if y_pred_proba else None
        
        metrics = classification_metrics.calculate_comprehensive_metrics(
            y_true_array, y_pred_array, y_pred_proba_array, model_name
        )
        return metrics
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error calculating metrics: {str(e)}")

@app.post("/metrics/compare")
async def compare_models(model_results: Dict[str, Dict]):
    """Compare multiple models using comprehensive metrics"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    return classification_metrics.compare_models(model_results)

@app.get("/metrics/confusion-matrix/{model_name}")
async def get_confusion_matrix_plot(model_name: str):
    """Generate confusion matrix plot for a model"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    if model_name not in classification_metrics.confusion_matrices:
        raise HTTPException(status_code=404, detail=f"Model {model_name} not found")
    
    cm = classification_metrics.confusion_matrices[model_name]
    plot_path = classification_metrics.generate_confusion_matrix_plot(cm, model_name)
    return {"plot_path": plot_path}

@app.get("/metrics/interpretation/{model_name}")
async def get_arrest_prediction_interpretation(model_name: str):
    """Get business interpretation for arrest prediction metrics"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    if model_name not in classification_metrics.metrics_history:
        raise HTTPException(status_code=404, detail=f"Model {model_name} not found")
    
    metrics = classification_metrics.metrics_history[model_name]
    return classification_metrics.get_arrest_prediction_interpretation(metrics)

@app.get("/metrics/summary-table")
async def get_metrics_summary_table():
    """Get summary table of all metrics for all models"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    if not classification_metrics.metrics_history:
        return {"message": "No models have been evaluated yet"}
    
    summary_df = classification_metrics.get_metrics_summary_table(classification_metrics.metrics_history)
    return {"summary_table": summary_df.to_dict('records')}

@app.get("/metrics/task-guidance/{task_number}")
async def get_atpa_task_guidance(task_number: int):
    """Get ATPA task-specific guidance for classification metrics"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    return classification_metrics.get_atpa_task_guidance(task_number)

@app.get("/metrics/essential-metrics")
async def get_essential_metrics_explanation():
    """Get explanation of essential classification metrics for arrest prediction"""
    if not classification_metrics:
        raise HTTPException(status_code=500, detail="Classification metrics layer not initialized")
    
    return {
        "essential_metrics": {
            "confusion_matrix": {
                "description": "Shows True Positives, False Positives, True Negatives, False Negatives",
                "importance": "Critical for understanding model performance in arrest prediction",
                "interpretation": "Helps identify if model is missing arrests (false negatives) or creating false alarms (false positives)"
            },
            "sensitivity": {
                "description": "True Positive Rate - ability to identify actual arrests",
                "importance": "Critical for arrest prediction - high sensitivity means fewer missed arrests",
                "target": "> 0.7 for operational use"
            },
            "specificity": {
                "description": "True Negative Rate - ability to identify non-arrests",
                "importance": "Prevents false alarms and resource waste",
                "target": "> 0.7 for operational use"
            },
            "precision": {
                "description": "Positive Predictive Value - accuracy of positive predictions",
                "importance": "Ensures predicted arrests are likely to be actual arrests",
                "target": "> 0.7 for operational use"
            },
            "f1_score": {
                "description": "Harmonic mean of precision and recall",
                "importance": "Balanced metric for imbalanced data (19% arrest rate)",
                "target": "> 0.6 for imbalanced data"
            },
            "balanced_accuracy": {
                "description": "Average of sensitivity and specificity",
                "importance": "Better than accuracy for imbalanced data",
                "target": "> 0.7 for operational use"
            },
            "roc_auc": {
                "description": "Area under ROC curve - overall discrimination ability",
                "importance": "Measures model's ability to rank predictions correctly",
                "target": "> 0.8 for good discrimination"
            }
        },
        "class_imbalance_considerations": {
            "problem": "19% arrest rate creates class imbalance",
            "solutions": [
                "Use balanced_accuracy instead of accuracy",
                "Focus on F1-score for balanced evaluation",
                "Consider sensitivity vs specificity trade-offs",
                "Use ROC-AUC for overall performance"
            ]
        }
    }

# ============================================================================
# ATPA TASK ENDPOINTS
# ============================================================================

@app.post("/tasks/run-task1")
async def run_task1_data_preparation(sample_size: Optional[int] = Query(None, ge=100, le=50000)):
    """Run Task 1: Data Preparation and Quality Analysis"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task1_data_preparation(sample_size)
        return {
            "status": "success",
            "task": "Task 1: Data Preparation",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 1: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 1: {str(e)}")

@app.post("/tasks/run-task2")
async def run_task2_privacy_ethics():
    """Run Task 2: Privacy and Ethics Analysis"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task2_privacy_ethics_analysis()
        return {
            "status": "success",
            "task": "Task 2: Privacy and Ethics Analysis",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 2: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 2: {str(e)}")

@app.post("/tasks/run-task3")
async def run_task3_generalized_linear_models():
    """Run Task 3: Generalized Linear Models"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task3_generalized_linear_models()
        return {
            "status": "success",
            "task": "Task 3: Generalized Linear Models",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 3: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 3: {str(e)}")

@app.post("/tasks/run-task4")
async def run_task4_random_forest_shap():
    """Run Task 4: Random Forest with SHAP Analysis"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task4_random_forest_shap()
        return {
            "status": "success",
            "task": "Task 4: Random Forest with SHAP Analysis",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 4: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 4: {str(e)}")

@app.post("/tasks/run-task5")
async def run_task5_bayesian_analysis():
    """Run Task 5: Bayesian Analysis"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task5_bayesian_analysis()
        return {
            "status": "success",
            "task": "Task 5: Bayesian Analysis",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 5: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 5: {str(e)}")

@app.post("/tasks/run-task6")
async def run_task6_executive_summary():
    """Run Task 6: Executive Summary"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.task6_executive_summary()
        return {
            "status": "success",
            "task": "Task 6: Executive Summary",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running Task 6: {e}")
        raise HTTPException(status_code=500, detail=f"Error running Task 6: {str(e)}")

@app.post("/tasks/run-all")
async def run_all_tasks(sample_size: Optional[int] = Query(None, ge=100, le=50000)):
    """Run all ATPA tasks in sequence"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        results = task_implementation.run_all_tasks(sample_size)
        return {
            "status": "success",
            "message": "All ATPA tasks completed successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error running all tasks: {e}")
        raise HTTPException(status_code=500, detail=f"Error running all tasks: {str(e)}")

@app.get("/tasks/status")
async def get_task_status():
    """Get status of completed tasks"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    completed_tasks = list(task_implementation.results.keys())
    return {
        "completed_tasks": completed_tasks,
        "total_tasks": 6,
        "progress": len(completed_tasks) / 6
    }

@app.get("/tasks/results/{task_number}")
async def get_task_results(task_number: int):
    """Get results for a specific task"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    task_key = f"task{task_number}"
    if task_key not in task_implementation.results:
        raise HTTPException(status_code=404, detail=f"Task {task_number} not completed yet")
    
    return {
        "task": f"Task {task_number}",
        "results": task_implementation.results[task_key]
    }

@app.post("/tasks/save-results")
async def save_task_results(filepath: str = Query(..., description="Path to save results")):
    """Save all task results to file"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        task_implementation.save_results(filepath)
        return {
            "status": "success",
            "message": f"Results saved to {filepath}"
        }
    except Exception as e:
        logger.error(f"Error saving results: {e}")
        raise HTTPException(status_code=500, detail=f"Error saving results: {str(e)}")

@app.post("/tasks/load-results")
async def load_task_results(filepath: str = Query(..., description="Path to load results from")):
    """Load task results from file"""
    if task_implementation is None:
        raise HTTPException(status_code=503, detail="Task implementation service unavailable")
    
    try:
        task_implementation.load_results(filepath)
        return {
            "status": "success",
            "message": f"Results loaded from {filepath}",
            "completed_tasks": list(task_implementation.results.keys())
        }
    except Exception as e:
        logger.error(f"Error loading results: {e}")
        raise HTTPException(status_code=500, detail=f"Error loading results: {str(e)}")

# ============================================================================
# FRONTEND ENDPOINTS (Optional)
# ============================================================================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Serve the main dashboard HTML page"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/status")
async def get_status():
    """Get server status and data availability"""
    status = {
        "server_status": "running",
        "layers": {
            "context": context is not None,
            "loader": loader is not None,
            "protocol": protocol is not None,
            "insights": insights is not None,
            "ethics": ethics is not None,
            "curriculum": curriculum is not None,
            "exam_analysis": exam_analysis is not None,
            "professional_resources": professional_resources is not None,
            "practical_examples": practical_examples is not None,
            "classification_metrics": classification_metrics is not None,
            "task_implementation": task_implementation is not None
        },
        "data_loaded": {
            "incidents": loader.incidents_df is not None if loader else False,
            "arrestee": loader.arrestee_df is not None if loader else False,
            "merged": protocol.merged_created if protocol else False
        }
    }
    
    if loader:
        status["data_summary"] = loader.get_data_summary()
    
    return status

# ============================================================================
# UTILITY ENDPOINTS
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

@app.get("/docs")
async def get_documentation():
    """Get API documentation"""
    return {
        "title": "ATPA MCP Server Documentation",
        "description": "Model-Context-Protocol server for criminal incident and arrest data analysis",
        "endpoints": {
            "context": {
                "GET /fields": "Get metadata for all fields",
                "GET /fields/{field_name}": "Get metadata for specific field",
                "GET /fields/source/{source}": "Get fields by source file"
            },
            "model": {
                "GET /data/incidents": "Get incidents data",
                "GET /data/arrestee": "Get arrestee data",
                "GET /data/summary": "Get data summary"
            },
            "protocol": {
                "POST /merged/create": "Create merged dataset",
                "GET /merged/data": "Get merged data",
                "GET /merged/summary": "Get merged summary",
                "GET /merged/arrest-analysis": "Get arrest analysis"
            },
            "insights": {
                "GET /eda/summary": "Get EDA summary",
                "GET /eda/arrest-rate-viz": "Get arrest rate visualization",
                "GET /eda/temporal-analysis": "Get temporal analysis",
                "GET /eda/correlation-analysis": "Get correlation analysis",
                "GET /eda/feature-importance": "Get feature importance",
                "GET /eda/reasonability-checks": "Get reasonability checks"
            },
            "ethics": {
                "GET /ethics/framework": "Get ATPA Module 1 ethics framework",
                "GET /ethics/protected-variables": "Identify protected variables",
                "GET /ethics/bias-assessment": "Get comprehensive bias assessment",
                "GET /ethics/fairness-metrics": "Get fairness metrics for ARREST target",
                "GET /ethics/recommendations": "Get ethical recommendations",
                "GET /ethics/summary": "Get comprehensive ethical summary",
                "GET /ethics/compliance-checklist": "Get ATPA compliance checklist"
            },
            "curriculum": {
                "GET /curriculum/overview": "Get overview of all ATPA modules",
                "GET /curriculum/module/{module_key}": "Get content for specific module",
                "GET /curriculum/search": "Search across all modules",
                "GET /curriculum/learning-objectives": "Get learning objectives for all modules",
                "GET /curriculum/ethical-framework": "Get detailed ethical framework from Module 1",
                "GET /curriculum/modeling-techniques": "Get modeling techniques from Module 3",
                "GET /curriculum/explainability-techniques": "Get explainability techniques from Module 4",
                "GET /curriculum/data-quality-guidelines": "Get data quality guidelines from Module 2",
                "GET /curriculum/summary": "Get comprehensive curriculum summary"
            },
            "exam_analysis": {
                "GET /exam/overview": "Get overview of all exam documents",
                "GET /exam/task-analysis": "Get comprehensive task analysis",
                "GET /exam/writing-guidelines": "Get writing and communication guidelines",
                "GET /exam/technical-guidelines": "Get technical methodology guidelines",
                "GET /exam/grading-insights": "Get grading and evaluation insights",
                "GET /exam/current-assignment": "Get current assignment analysis (June-August 2025)",
                "GET /exam/comparative-analysis": "Get comparative analysis across all exams",
                "GET /exam/search": "Search across all exam documents"
            },
            "professional_resources": {
                "GET /professional/overview": "Get overview of all professional resources",
                "GET /professional/shap-guide": "Get SHAP analysis methodology and guidelines",
                "GET /professional/executive-summary-template": "Get executive summary template and guidelines",
                "GET /professional/asop-standards": "Get ASOP 41 communication standards",
                "GET /professional/task-guidance/{task_number}": "Get guidance specific to ATPA task numbers",
                "GET /professional/communication-checklist": "Get comprehensive communication checklist",
                "GET /professional/cross-references": "Get cross-references between resources",
                "GET /professional/search": "Search across all professional resources"
            },
            "practical_examples": {
                "GET /examples/overview": "Get overview of all practical examples",
                "GET /examples/code-statistics": "Get code statistics across all examples",
                "GET /examples/language-comparison": "Get comparison between Python and R implementations",
                "GET /examples/topic-coverage": "Get topic coverage analysis",
                "GET /examples/practical-applications": "Get practical applications analysis",
                "GET /examples/category/{category}": "Get examples by category",
                "GET /examples/language/{language}": "Get examples by programming language",
                "GET /examples/topic/{topic}": "Get code chunks related to a specific topic",
                "GET /examples/task/{task_number}": "Get examples relevant to specific ATPA tasks",
                "GET /examples/search": "Search across all practical examples"
            },
            "classification_metrics": {
                "POST /metrics/calculate": "Calculate comprehensive classification metrics",
                "POST /metrics/compare": "Compare multiple models using comprehensive metrics",
                "GET /metrics/confusion-matrix/{model_name}": "Generate confusion matrix plot for a model",
                "GET /metrics/interpretation/{model_name}": "Get business interpretation for arrest prediction metrics",
                "GET /metrics/summary-table": "Get summary table of all metrics for all models",
                "GET /metrics/task-guidance/{task_number}": "Get ATPA task-specific guidance for classification metrics",
                "GET /metrics/essential-metrics": "Get explanation of essential classification metrics for arrest prediction"
            }
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 