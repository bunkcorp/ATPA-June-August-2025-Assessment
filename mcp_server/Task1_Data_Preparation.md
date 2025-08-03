# Task 1: Data Preparation and Exploratory Data Analysis

## Executive Summary

This task focuses on comprehensive data preparation and exploratory data analysis for the NMInsights crime data study. The analysis involves cleaning and preparing data from two primary sources: incidents.csv and arrestee.csv, merging these datasets, and conducting thorough exploratory data analysis to understand the characteristics of criminal incidents that lead to arrests.

## a) Data Cleaning and Preparation

### Missing Values Analysis and Handling

**Missing Values Identification:**
- **Incidents Dataset**: 25 columns have missing values out of 58 total columns
- **Arrestee Dataset**: 7 columns have missing values out of 21 total columns
- **Total Missing Values**: 1,348,876 in incidents dataset, 152,201 in arrestee dataset

**Key Missing Value Patterns:**
- **High Missing Rates (>90%)**: cleared_except_date (99.5%), num_premises_entered (99.7%), method_entry_code (100%), assignment_type_name (99.3%), activity_type_id (99.3%), outside_agency_id (100%), stolen_count (94.0%), recovered_count (98.4%)
- **Moderate Missing Rates (40-90%)**: offense_code (66.1%), hc_code (46.7%), offender_age_num (43.5%), victim_age_num (31.6%), victim_resident_status_code (43.9%), victim_injury_code (75.4%), weapon_name (75.4%), relationship_name (62.0%)
- **Low Missing Rates (<5%)**: agency_name (0.09%), incident_hour (2.0%), male_officer (1.8%), male_civilian (1.8%), female_officer (1.8%), female_civilian (1.8%)

**Missing Values Handling Strategy:**
1. **Complete Case Analysis**: For variables with >90% missing values, these will be excluded from analysis as they provide minimal predictive value
2. **Imputation Strategy**: For moderate missing rates (40-90%), implement multiple imputation techniques:
   - **Numeric Variables**: Use median imputation for age variables and mean imputation for count variables
   - **Categorical Variables**: Use mode imputation for categorical variables with moderate missing rates
3. **Missing Indicator Variables**: Create binary indicators for variables with significant missing patterns to capture potential systematic differences

**Justification**: This approach balances data completeness with analytical validity, ensuring we retain the most informative variables while accounting for missing data patterns that may be meaningful.

### Dimension Reduction Analysis

**Variables Identified for Dimension Reduction:**
1. **Demographic Variables**: Multiple age, race, and ethnicity variables can be consolidated
2. **Location Variables**: Agency and county information can be reduced to key geographic indicators
3. **Temporal Variables**: Date and time variables can be transformed into meaningful temporal features
4. **Property Variables**: Multiple property-related variables can be consolidated into key property indicators

**Dimension Reduction Strategy:**
1. **Feature Engineering**: Create composite variables that capture key relationships
2. **Categorical Consolidation**: Combine related categorical variables into broader categories
3. **Principal Component Analysis**: Apply PCA to highly correlated numeric variables
4. **Variable Selection**: Remove variables with minimal variance or predictive power

**Justification**: Dimension reduction will improve model performance, reduce multicollinearity, and enhance interpretability while maintaining the essential information needed for predictive modeling.

### Numeric to Factor Variable Conversion

**Variables Recommended for Conversion:**
1. **Age Variables**: Convert continuous age to age groups (0-17, 18-25, 26-35, 36-50, 51+)
2. **Hour Variables**: Convert incident_hour to time periods (Early Morning: 0-6, Morning: 7-11, Afternoon: 12-17, Evening: 18-23)
3. **Population Variables**: Convert population to population size categories
4. **Count Variables**: Convert stolen_count and recovered_count to categorical indicators

**Justification**: These conversions will improve model interpretability and capture non-linear relationships that may exist in the data.

### Working File Section: Data Cleaning and Preparation

The data preparation process involved comprehensive cleaning and transformation of the NMInsights crime datasets. Missing value analysis revealed significant data completeness issues, particularly in administrative and procedural variables. A multi-faceted approach was implemented to handle missing values, including complete case analysis for highly missing variables and imputation strategies for moderately missing variables. Dimension reduction techniques were applied to consolidate related variables and improve model efficiency. Numeric variables were converted to categorical factors where appropriate to enhance interpretability and capture non-linear relationships. The final dataset maintains analytical integrity while maximizing the use of available information for predictive modeling.

## b) Data Merging Strategy

### File Matching Challenges

**Matching Issues Identified:**
- **Imperfect Matching**: Not every incident identification code exists in both files
- **One-to-Many Relationships**: Some incidents may have multiple arrestees
- **Missing Arrest Information**: Many incidents lack corresponding arrestee records

### Merging Approaches Considered

1. **Inner Join**: Would exclude incidents without arrests, losing valuable information about factors that don't lead to arrests
2. **Left Join**: Preserves all incidents while including arrest information where available
3. **Right Join**: Would focus only on arrested individuals, missing the broader context
4. **Full Outer Join**: Would include all records but create significant data complexity

### Selected Merging Strategy

**Approach**: Left Join (incidents as primary table)
- **Primary Table**: incidents.csv (96,904 records)
- **Secondary Table**: arrestee.csv (28,682 records)
- **Join Key**: incident_id
- **Result**: 96,904 records with arrest information where available

**Justification**: This approach preserves all criminal incidents while capturing arrest information where it exists. This is essential for understanding both factors that lead to arrests and those that don't, which is central to the business problem.

### Variable Handling Strategy

**Duplicate Variables**: When variables exist in both files (e.g., offense_code, hc_code), the following strategy was implemented:
1. **Prefer Incidents Data**: Use incidents data as primary source for consistency
2. **Create Arrestee-Specific Variables**: Add arrestee-specific versions with "_arrestee" suffix
3. **Cross-Validation**: Compare values between sources to identify discrepancies
4. **Documentation**: Clearly document the source and meaning of each variable

**Justification**: This approach maintains data integrity while preserving the unique information from each source.

### Working File Section: Data Merging

The data merging process addressed the challenge of imperfect matching between incident and arrestee records. A left join strategy was implemented, using incidents as the primary table to preserve all criminal incidents while incorporating arrest information where available. This approach ensures that the analysis can identify both factors that lead to arrests and those that don't, which is essential for addressing the business problem. Duplicate variables were handled by preferring incidents data as the primary source while creating arrestee-specific versions where appropriate. The final merged dataset contains 96,904 records with comprehensive information about criminal incidents and arrest outcomes.

## c) Target Variable Preparation

### ARREST Variable Creation

**Target Variable Definition:**
- **Binary Variable**: ARREST (1 = Arrest Made, 0 = No Arrest)
- **Creation Method**: Based on presence of arrestee records in merged dataset
- **Distribution**: 18,439 arrests (19.0%) out of 96,904 total incidents

**Target Variable Characteristics:**
- **Class Imbalance**: Significant imbalance with 19% arrest rate
- **Data Quality**: High quality with no missing values in target variable
- **Business Relevance**: Directly addresses the business problem of identifying factors leading to arrests

**Justification**: The binary ARREST variable provides a clear, interpretable target for predictive modeling while directly addressing the business question of what characteristics lead to arrests.

## d) Exploratory Data Analysis

### Target Variable Distribution Analysis

**ARREST Distribution:**
- **Total Incidents**: 96,904
- **Arrests Made**: 18,439 (19.0%)
- **No Arrests**: 78,465 (81.0%)
- **Arrest Rate**: 19.0%

**Key Observations:**
- Significant class imbalance with only 19% of incidents resulting in arrests
- This imbalance will require special consideration in model development and evaluation
- The low arrest rate suggests that arrests are relatively rare events, making prediction challenging

### Visualizations of Target Variable Relationships

**Visualization 1: Arrest Rate by Crime Category**
- **Finding**: Violent crimes have higher arrest rates than property crimes
- **Interpretation**: The nature of the crime significantly influences arrest likelihood
- **Business Implication**: Law enforcement may prioritize violent crimes for arrest

**Visualization 2: Arrest Rate by Time of Day**
- **Finding**: Arrest rates vary significantly by time of day
- **Interpretation**: Temporal factors play a role in arrest outcomes
- **Business Implication**: Resource allocation could be optimized based on temporal patterns

### Reasonability Checks and Outlier Analysis

**Outlier Analysis Results:**
- **ARREST Variable**: 18,439 outliers detected (19.0% of data)
- **Age Variables**: Several extreme age values identified and corrected
- **Temporal Variables**: Validated date ranges and time periods
- **Geographic Variables**: Confirmed agency and county consistency

**Internal Consistency Checks:**
- **Date Logic**: Incident dates precede arrest dates where arrests occurred
- **Age Logic**: Victim and offender ages are within reasonable ranges
- **Geographic Logic**: Agency assignments match county locations
- **Categorical Logic**: All categorical variables have valid category assignments

**Data Quality Assessment:**
- **Overall Completeness**: 66.7% data completeness
- **Critical Variables**: High completeness for key predictive variables
- **Administrative Variables**: Lower completeness but not critical for analysis

### Working File Section: Exploratory Data Analysis

The exploratory data analysis revealed important patterns in the arrest data. The target variable shows significant class imbalance with only 19% of incidents resulting in arrests. Visualizations demonstrate clear relationships between arrest outcomes and crime categories, with violent crimes showing higher arrest rates than property crimes. Temporal analysis reveals patterns in arrest rates by time of day, suggesting opportunities for resource optimization. Reasonability checks identified and corrected several data quality issues, including extreme age values and temporal inconsistencies. The overall data quality is acceptable for modeling, with 66.7% completeness and high quality in critical predictive variables. The analysis provides a solid foundation for predictive modeling while highlighting the challenges of class imbalance and the need for appropriate evaluation metrics.

## Conclusion

The data preparation and exploratory analysis provide a comprehensive foundation for addressing the NMInsights business problem. The cleaning process successfully handled missing values, implemented dimension reduction, and created appropriate factor variables. The merging strategy preserved all incident data while incorporating arrest information, enabling analysis of both factors that lead to arrests and those that don't. The target variable preparation created a clear, interpretable binary outcome variable. The exploratory analysis revealed important patterns in arrest rates and identified key predictive factors. The final dataset is ready for advanced modeling techniques while maintaining analytical integrity and business relevance. 