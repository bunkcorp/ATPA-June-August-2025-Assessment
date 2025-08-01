# ATPA Assessment - June to August 2025
## NMInsights Crime Analysis Project

### Overview
This project addresses NMInsights' crime analysis problem using advanced data analysis and predictive modeling techniques to understand factors leading to arrests in New Mexico.

### Business Problem
NMInsights, a non-profit public policy research institute in New Mexico, is studying their state's crime rates. New Mexico consistently ranks among the U.S. states with the highest rates of violent crime and property crime. The goal is to identify key characteristics of criminal incidents that lead to arrests being made, particularly understanding demographic and other characteristics that influence law enforcement decisions.

### Key Business Questions
1. What characteristics of a criminal incident are associated with an arrest?
2. Are there specific categories of criminal offenses more likely to result in arrests than others?

### Project Structure

#### Task 1 (Data Preparation)
- **Location**: `Task1_DataPrep/`
- **Objectives**:
  - Clean and prepare data for analysis
  - Handle missing values and dimension reduction
  - Merge arrestee and incidents data
  - Create ARREST target variable
  - Exploratory Data Analysis

#### Task 2 (Privacy & Bias Analysis)
- **Location**: `Task2_Privacy/`
- **Objectives**:
  - Discuss benefits and risks of demographic data usage
  - Address bias concerns in criminal justice modeling
  - Professional standards compliance

#### Task 3 (Generalized Linear Models)
- **Location**: `Task3_Modeling/`
- **Objectives**:
  - Create training/testing datasets
  - Fit Generalized Linear Model
  - Fit Linear Mixed Model with random effects
  - Model comparison and selection

#### Task 4 (Random Forest & SHAP)
- **Location**: `Task4_RandomForest/`
- **Objectives**:
  - Fit and tune Random Forest model
  - Calculate SHAP values for selected incidents
  - Partial dependence plots for key predictors

#### Task 5 (Bayesian Analysis)
- **Location**: `Task5_Bayesian/`
- **Objectives**:
  - Summary of arrest rates by crime category
  - Bayesian model for arrest rates
  - 95% credible intervals for each crime type

#### Task 6 (Executive Summary)
- **Location**: `Task6_ExecutiveSummary/`
- **Objectives**:
  - Write 1-2 page executive summary
  - Include business problem, key findings, recommendations, limitations

### Data Files
- `arrestee.csv.csv`: Arrestee information with demographic and crime details
- `Data_Dictionary.xlsx`: Data dictionary for understanding variables

### Target Variable
- **ARREST**: Binary variable indicating whether an incident resulted in an arrest

### Key Challenges
- **Data Integration**: Merging arrestee and incidents data with imperfect matching
- **Bias Concerns**: Addressing demographic data usage in criminal justice context
- **Missing Data**: Handling missing values appropriately
- **Model Selection**: Choosing appropriate models for arrest prediction

### Deliverables
- Technical report sections for each task
- Executive summary for NMInsights management
- All code, tables, and visualizations properly formatted for Word template
- Comprehensive analysis addressing both business questions

### Professional Standards
- Address bias and fairness concerns in criminal justice modeling
- Ensure results are not misused for discriminatory purposes
- Follow actuarial standards of practice for data analysis 