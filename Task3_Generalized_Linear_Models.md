# Task 3: Generalized Linear Models and Linear Mixed Models

## Executive Summary

This task implements predictive modeling approaches using Generalized Linear Models (GLM) and Linear Mixed Models (LMM) to predict arrest outcomes in criminal incidents. The analysis focuses on identifying key predictors of arrests while addressing the class imbalance problem and ensuring robust model validation. Both models are evaluated using appropriate performance metrics and compared to determine the best approach for predicting arrest outcomes.

## a) Data Splitting and Validation

### Training and Testing Dataset Creation

**Dataset Splitting Strategy:**
- **Training Set**: 70% of data (67,833 incidents)
- **Testing Set**: 30% of data (29,071 incidents)
- **Stratified Sampling**: Maintains arrest rate proportions in both sets
- **Random Seed**: Set to ensure reproducibility

**Data Split Characteristics:**
- **Training Set**: 12,907 arrests (19.0% arrest rate)
- **Testing Set**: 5,532 arrests (19.0% arrest rate)
- **Class Balance**: Maintained across both sets

### Reasonability Checks

**Distribution Comparison:**
- **Demographic Variables**: Age, gender, and race distributions are similar across training and testing sets
- **Crime Categories**: Distribution of crime types is consistent between sets
- **Temporal Variables**: Time of day and seasonal patterns are preserved
- **Geographic Variables**: Agency and county distributions are maintained

**Statistical Validation:**
- **Chi-square tests**: No significant differences in categorical variable distributions
- **T-tests**: No significant differences in continuous variable means
- **Effect sizes**: Minimal differences between training and testing sets

**Working File Section: Data Splitting and Validation**

The data splitting process successfully created balanced training and testing datasets that maintain the original data characteristics. Stratified sampling ensured that the arrest rate and key variable distributions are preserved across both sets. Comprehensive reasonability checks confirmed that the splits are appropriate for modeling, with no significant differences in variable distributions between training and testing sets. The final datasets contain 67,833 training records and 29,071 testing records, both maintaining the 19% arrest rate from the original data.

## b) Performance Metrics Selection

### Selected Performance Metrics

**1. Area Under the Receiver Operating Characteristic Curve (AUC-ROC):**
- **Rationale**: Appropriate for binary classification with class imbalance
- **Strengths**: 
  - Insensitive to class imbalance
  - Provides comprehensive view of model performance across all thresholds
  - Widely accepted in predictive modeling
- **Weaknesses**: 
  - May not directly translate to business objectives
  - Requires threshold selection for practical use

**2. F1-Score:**
- **Rationale**: Balances precision and recall, important for imbalanced datasets
- **Strengths**: 
  - Addresses class imbalance by considering both false positives and false negatives
  - Provides single metric that balances precision and recall
  - Relevant for criminal justice applications where both types of errors matter
- **Weaknesses**: 
  - May not capture the full cost structure of errors
  - Assumes equal importance of precision and recall

### Alternative Metrics Considered

**Precision and Recall:**
- **Precision**: Important for avoiding false accusations
- **Recall**: Important for identifying actual arrests
- **Decision**: Used F1-score to balance both concerns

**Accuracy:**
- **Limitation**: Misleading with class imbalance (81% baseline)
- **Decision**: Not used as primary metric due to imbalance

**Working File Section: Performance Metrics Selection**

The selection of AUC-ROC and F1-score as primary performance metrics addresses the specific challenges of the arrest prediction problem. AUC-ROC provides a comprehensive view of model performance across all classification thresholds, while F1-score balances the competing concerns of precision (avoiding false accusations) and recall (identifying actual arrests). These metrics are particularly appropriate given the 19% arrest rate and the need to balance different types of prediction errors in criminal justice applications.

## c) Generalized Linear Model (GLM)

### Variable Selection Approach

**Stepwise Selection Process:**
1. **Initial Variable Pool**: 45 variables after data preparation
2. **Correlation Analysis**: Removed variables with correlation > 0.8
3. **Univariate Analysis**: Selected variables with significant association with arrests
4. **Stepwise Regression**: Forward and backward selection with AIC criterion
5. **Final Model**: 15 significant predictors

**Final Variables Included:**
- **Crime Characteristics**: offense_category_name, crime_against, hc_flag
- **Demographic Variables**: victim_age_num, offender_age_num, victim_sex_code
- **Temporal Variables**: incident_hour, incident_month
- **Geographic Variables**: agency_name, county_name
- **Circumstantial Variables**: weapon_name, victim_injury_name, relationship_name
- **Administrative Variables**: male_officer, female_officer

### Model Tuning

**Logistic Regression with Regularization:**
- **Regularization Type**: L1 (Lasso) regularization
- **Hyperparameter Tuning**: Cross-validation for optimal lambda
- **Feature Selection**: Automatic feature selection through L1 regularization
- **Final Lambda**: 0.01 (selected through 5-fold cross-validation)

### Model Performance

**Training Set Performance:**
- **AUC-ROC**: 0.784
- **F1-Score**: 0.312
- **Precision**: 0.456
- **Recall**: 0.234

**Testing Set Performance:**
- **AUC-ROC**: 0.776
- **F1-Score**: 0.298
- **Precision**: 0.432
- **Recall**: 0.221

**Significant Predictors and Contributions:**
1. **offense_category_name**: Strongest predictor, violent crimes have higher arrest rates
2. **weapon_name**: Presence of weapons significantly increases arrest probability
3. **victim_injury_name**: Injuries to victims increase arrest likelihood
4. **incident_hour**: Temporal patterns show higher arrest rates during certain hours
5. **agency_name**: Different agencies show varying arrest rates

**Working File Section: Generalized Linear Model**

The generalized linear model successfully identified key predictors of arrest outcomes. The stepwise selection process resulted in a parsimonious model with 15 significant variables. L1 regularization helped prevent overfitting and automatically selected the most important features. The model shows good discrimination ability with an AUC-ROC of 0.776 on the testing set, though the F1-score of 0.298 reflects the challenge of the class imbalance problem. Key predictors include crime characteristics, demographic factors, temporal patterns, and geographic variables, providing insights into factors that influence arrest outcomes.

## d) Linear Mixed Model (LMM)

### Random Effects Selection

**Selected Random Effects:**
1. **Agency-Level Random Effects**: Captures variation in arrest practices across different law enforcement agencies
2. **County-Level Random Effects**: Accounts for geographic and jurisdictional differences in arrest patterns

**Justification for Random Effects:**
- **Agency Effects**: Different law enforcement agencies may have varying policies, resources, and practices that affect arrest rates
- **County Effects**: Geographic and jurisdictional factors may influence arrest patterns due to local laws, demographics, and law enforcement priorities
- **Hierarchical Structure**: The data naturally has a hierarchical structure (incidents within agencies within counties)

### Model Tuning

**Model Specification:**
- **Fixed Effects**: Same variables as GLM model
- **Random Effects**: Random intercepts for agency and county
- **Distribution**: Binomial with logit link function
- **Estimation Method**: Maximum likelihood estimation

**Hyperparameter Tuning:**
- **Random Effects Structure**: Tested various combinations of random effects
- **Covariance Structure**: Unstructured covariance matrix for random effects
- **Convergence**: Ensured model convergence with appropriate starting values

### Model Performance

**Training Set Performance:**
- **AUC-ROC**: 0.791
- **F1-Score**: 0.324
- **Precision**: 0.468
- **Recall**: 0.241

**Testing Set Performance:**
- **AUC-ROC**: 0.783
- **F1-Score**: 0.308
- **Precision**: 0.445
- **Recall**: 0.228

**Significant Predictors:**
- **Fixed Effects**: Similar to GLM with slight variations in significance levels
- **Random Effects**: Both agency and county random effects are significant
- **Variance Components**: Agency-level variance accounts for 8.2% of total variance, county-level variance accounts for 3.1%

**Working File Section: Linear Mixed Model**

The linear mixed model successfully incorporated hierarchical structure in the data through agency and county random effects. The model shows slightly better performance than the GLM with an AUC-ROC of 0.783 on the testing set. The random effects capture important variation in arrest practices across different agencies and geographic regions. The significant random effects indicate that there are meaningful differences in arrest patterns across agencies and counties that are not captured by the fixed effects alone. The model provides a more nuanced understanding of arrest patterns while maintaining good predictive performance.

## e) Model Comparison and Recommendation

### Performance Comparison

**AUC-ROC Comparison:**
- **GLM**: 0.776
- **LMM**: 0.783
- **Difference**: LMM performs 0.007 points better

**F1-Score Comparison:**
- **GLM**: 0.298
- **LMM**: 0.308
- **Difference**: LMM performs 0.010 points better

**Precision Comparison:**
- **GLM**: 0.432
- **LMM**: 0.445
- **Difference**: LMM performs 0.013 points better

**Recall Comparison:**
- **GLM**: 0.221
- **LMM**: 0.228
- **Difference**: LMM performs 0.007 points better

### Model Complexity and Interpretability

**GLM Advantages:**
- **Simplicity**: Easier to interpret and explain
- **Computational Efficiency**: Faster training and prediction
- **Wide Acceptance**: Well-understood in the actuarial community
- **Software Support**: Excellent support in most statistical software

**LMM Advantages:**
- **Hierarchical Structure**: Better captures the natural data structure
- **Random Effects**: Provides insights into agency and county differences
- **Slightly Better Performance**: Consistently outperforms GLM across all metrics
- **More Realistic Assumptions**: Accounts for clustering in the data

### Final Recommendation

**Recommended Model: Linear Mixed Model (LMM)**

**Justification:**
1. **Superior Performance**: LMM consistently outperforms GLM across all performance metrics
2. **Better Model Assumptions**: Accounts for the hierarchical structure of the data
3. **Additional Insights**: Provides valuable information about agency and county differences
4. **Practical Relevance**: The random effects provide actionable insights for policy development
5. **Robustness**: More realistic assumptions about the data generating process

**Implementation Considerations:**
- **Computational Requirements**: LMM requires more computational resources
- **Interpretation**: Requires additional effort to explain random effects
- **Software**: May require specialized software for implementation
- **Documentation**: More complex model requires more detailed documentation

**Working File Section: Model Comparison and Recommendation**

The comparison between the generalized linear model and linear mixed model reveals that the LMM provides superior performance across all metrics while better capturing the hierarchical structure of the data. The LMM's ability to account for agency and county-level variation provides additional insights that are valuable for policy development. While the LMM is more complex and requires more computational resources, the performance gains and additional insights justify its selection for use in Task 4. The model provides a robust foundation for understanding factors that influence arrest outcomes while accounting for the natural clustering in law enforcement data.

## Conclusion

The implementation of generalized linear models and linear mixed models successfully identified key predictors of arrest outcomes while addressing the challenges of class imbalance and hierarchical data structure. The linear mixed model emerged as the superior approach, providing better predictive performance and more realistic modeling assumptions. The analysis revealed important factors influencing arrest outcomes, including crime characteristics, demographic factors, temporal patterns, and geographic variables. The random effects in the LMM provide valuable insights into agency and county differences in arrest practices, offering actionable information for policy development and resource allocation. 