# Module 3: Advanced Models - Content Summary

## Overview
Module 3 covers advanced statistical modeling techniques including Generalized Additive Models (GAMs), Linear Mixed Models, Neural Networks, Bayesian Methods, Stacking, and Fairness in Analytics. The module consists of 7 main sections with comprehensive practical applications.

## Module 3 Learning Objectives

Upon completion of this module, students will be able to:

1. **Explain the importance of model accuracy**
2. **Explain, fit, evaluate, and make predictions with additive models**
3. **Explain, fit, evaluate, and make predictions with linear mixed models**
4. **Explain, fit, evaluate, and make predictions with neural networks**
5. **Apply Bayesian techniques to linear models**
6. **Explain the benefits of and demonstrate the combination of multiple models via stacking**
7. **Recognize and mitigate the effects of starting with too many variables**
8. **Recognize and mitigate the effects of missing data in predictive modeling**

---

## Section 3.2: Generalized Additive Models (`atpa_3_2_r.rmd`)

### Key Topics Covered:

#### **Traffic Data Analysis**
- **Data visualization**: Plotting traffic patterns by hour
- **Linear regression**: Basic linear model fitting
- **Polynomial regression**: Fitting polynomials of various degrees (2, 3, 5, 8, 10)
- **Log-transformed responses**: Handling non-linear relationships with log transformations

#### **Generalized Additive Models (GAMs)**
- **GAM fitting**: Using `mgcv` package with `gam()` function
- **Smooth functions**: Using `s()` for smooth terms
- **Model comparison**: AIC comparison between linear and GAM models
- **Model diagnostics**: Using `gam.check()` for model validation

#### **Smooth Function Control**
- **Dimension reduction**: Using `k` parameter to control smoothness
- **Overfitting prevention**: Balancing model complexity
- **Variable selection**: Using `select=TRUE` for automatic variable selection

#### **Practical Applications**
- **Hotel booking analysis**: Predicting average daily rate (ADR)
- **Model comparison**: Linear models vs GAMs vs GLMs
- **Cross-validation**: Training/test splits for model evaluation
- **Performance metrics**: Mean squared prediction error (MSPE)

#### **Advanced Features**
- **Gamma GLMs**: Handling non-normal response distributions
- **Multiple predictors**: Combining smooth and linear terms
- **Model diagnostics**: Residual analysis and goodness-of-fit

---

## Section 3.3: Linear Mixed Models (`atpa_3_3_r.rmd`)

### Key Topics Covered:

#### **Computer Course Data Analysis**
- **Standard regression**: Basic linear model with categorical predictors
- **Random intercepts model**: Using `lmer()` with `(1|prof)` syntax
- **Model comparison**: Comparing fixed vs mixed effects approaches
- **Random effects extraction**: Using `ranef()` function

#### **Prediction with New Factor Levels**
- **Handling new levels**: Using `re.form=NA` for predictions
- **Conditional predictions**: Incorporating random effects when available
- **Prediction strategies**: Different approaches for known vs unknown groups

#### **Random Slopes Models**
- **Slope variation**: Using `(0+variable|group)` syntax
- **Complex random effects**: Combining intercepts and slopes
- **Model interpretation**: Understanding variance components

#### **Generalized Linear Mixed Models (GLMMs)**
- **Binary outcomes**: Logistic mixed models for binary responses
- **Count data**: Poisson mixed models for count responses
- **Model comparison**: AIC comparison between different model types

#### **Practical Applications**
- **Email analysis**: Modeling email sending patterns
- **Repeated measures**: Longitudinal data analysis
- **Credibility theory**: Insurance applications with mixed models
- **Dose-response studies**: Medical/pharmaceutical applications

#### **Advanced Topics**
- **Credibility premiums**: Insurance pricing applications
- **Gamma GLMMs**: Handling skewed continuous responses
- **Model diagnostics**: Assessing mixed model fit

---

## Section 3.4: Neural Networks (`atpa_3_4_r.rmd`)

### Key Topics Covered:

#### **Basic Neural Network Concepts**
- **Hiring data example**: Simple classification problem
- **Network architecture**: Hidden layers and neurons
- **Activation functions**: Sigmoid vs ReLU comparison
- **Decision boundaries**: Visualizing classification regions

#### **Hotel Booking Classification**
- **Data preparation**: Handling categorical variables with one-hot encoding
- **Network training**: Using `ANN2` package
- **Overfitting detection**: Training vs validation loss monitoring
- **Hyperparameter tuning**: Learning rates, epochs, batch sizes

#### **Model Comparison**
- **Neural networks vs decision trees**: Performance comparison
- **Neural networks vs logistic regression**: Classification accuracy
- **Cross-validation**: K-fold cross-validation for model selection
- **Performance metrics**: Accuracy, ROC curves, AUC

#### **Regression Applications**
- **Auto MPG prediction**: Continuous outcome prediction
- **Mini-batch sizes**: Impact on training stability
- **Learning rate effects**: Convergence behavior analysis
- **Model diagnostics**: Residual analysis and prediction plots

#### **Advanced Neural Network Topics**
- **Multi-class classification**: Maternal risk assessment
- **Multi-layer networks**: Deep learning architectures
- **Different loss functions**: Squared error, absolute error, cross-entropy
- **Activation function comparison**: Sigmoid, tanh, ReLU performance

#### **Practical Applications**
- **Abalone age prediction**: Regression with multiple predictors
- **Maternal risk classification**: Healthcare applications
- **Model interpretation**: Understanding prediction probabilities
- **Outlier detection**: Identifying unusual predictions

---

## Section 3.5: Bayesian Methods (`atpa_3_5_r.rmd`)

### Key Topics Covered:

#### **Stan Programming**
- **Poisson-Gamma model**: Conjugate prior example
- **MCMC sampling**: Using Stan for posterior sampling
- **Model compilation**: Stan model setup and execution
- **Trace plots**: Assessing MCMC convergence

#### **Posterior Analysis**
- **Exact vs MCMC**: Comparing analytical vs numerical solutions
- **Sample size effects**: How data quantity affects posterior precision
- **Prior influence**: Understanding prior-posterior relationships
- **Posterior visualization**: Density plots and credible intervals

#### **Regression Applications**
- **Bayesian regression**: Using `brms` package
- **Model comparison**: LOO cross-validation for model selection
- **Horseshoe priors**: Sparse regression with shrinkage
- **Variable selection**: Automatic relevance determination

#### **Count Data Modeling**
- **Poisson regression**: Basic count data model
- **Negative binomial**: Overdispersed count data
- **Zero-inflated models**: Handling excess zeros
- **Model comparison**: LOO for count model selection

#### **Severity Modeling**
- **Gamma regression**: Modeling claim amounts
- **Lognormal regression**: Alternative severity distribution
- **Model diagnostics**: Assessing distributional assumptions
- **Prediction intervals**: Uncertainty quantification

#### **Advanced Bayesian Topics**
- **Prediction**: Generating predictive distributions
- **Model checking**: Posterior predictive checks
- **Cross-validation**: Bayesian model comparison
- **Uncertainty quantification**: Credible intervals and prediction intervals

---

## Section 3.6: Stacking (`atpa_3_6_r.rmd`)

### Key Topics Covered:

#### **Stacking Fundamentals**
- **Meta-learning**: Combining multiple base models
- **Cross-validation**: Generating out-of-fold predictions
- **Meta-model fitting**: Linear combination of base predictions
- **Two-stage process**: Base models then meta-model

#### **Hotel Booking Regression**
- **Base models**: Linear regression, regression trees, neural networks
- **Cross-validation setup**: 5-fold CV for generating predictions
- **Meta-models**: Simple and complex meta-model formulations
- **Performance comparison**: RMSE comparison across models

#### **Classification Stacking**
- **Binary classification**: Hotel cancellation prediction
- **Base models**: Logistic regression, decision trees, neural networks
- **Meta-model**: Logistic regression on base predictions
- **Performance metrics**: Log loss evaluation

#### **Stacking Variations**
- **Simple meta-models**: Using only base predictions
- **Complex meta-models**: Including original features
- **Model selection**: Choosing optimal base model combinations
- **Ensemble methods**: Understanding stacking vs other ensemble approaches

#### **Practical Considerations**
- **Data splitting**: Training, validation, and test sets
- **Overfitting prevention**: Careful cross-validation
- **Model diversity**: Ensuring base models are different
- **Computational efficiency**: Managing training time

---

## Section 3.7: Advanced Topics

### Section 3.7a: Predictions with Missing Data (`atpa_3_7a_r.rmd`)

#### **Missing Data Strategies**
- **Full imputation**: Imputing all data before model fitting
- **Train-only imputation**: Building imputation scheme on training data
- **MICE package**: Multiple imputation by chained equations
- **Imputation consistency**: Ensuring proper train/test separation

#### **Chronic Kidney Disease Example**
- **Data exploration**: Understanding missing patterns
- **Imputation methods**: Norm.predict vs regression imputation
- **Model performance**: AUC comparison across imputation strategies
- **Prediction consistency**: Comparing different approaches

#### **Best Practices**
- **Data leakage prevention**: Proper train/test separation
- **Imputation validation**: Checking imputation quality
- **Model robustness**: Assessing sensitivity to imputation method
- **Practical considerations**: Real-world implementation challenges

### Section 3.7b: Fairness in Analytics (`atpa_3_7b_r.rmd`)

#### **Fairness Metrics**
- **Demographic parity**: Equal prediction rates across groups
- **Predictive parity**: Equal accuracy across groups
- **Equal opportunity**: Equal true positive rates
- **Equalized odds**: Equal true positive and false positive rates

#### **Credit Card Default Example**
- **Protected variables**: Gender as sensitive attribute
- **Full vs unawareness models**: Including vs excluding protected variables
- **Fairness assessment**: Quantifying bias in predictions
- **Intervention thresholds**: Setting appropriate decision boundaries

#### **Fairness Methods**
- **Unawareness**: Simply excluding protected variables
- **Orthogonalization**: Removing correlation with protected variables
- **Pope-Sydnor approach**: Replacing protected variables with means
- **Model comparison**: Assessing fairness across different approaches

#### **Insurance Applications**
- **Claims modeling**: Fairness in insurance pricing
- **Protected characteristics**: Gender, age, location considerations
- **Regulatory compliance**: Meeting fairness requirements
- **Business implications**: Balancing fairness and accuracy

---

## Key Skills Developed

### **Technical Skills**
- Advanced statistical modeling (GAMs, Mixed Models, Neural Networks)
- Bayesian inference and MCMC methods
- Ensemble methods and model stacking
- Fairness assessment and bias mitigation
- Missing data handling strategies

### **Analytical Skills**
- Model comparison and selection
- Cross-validation and performance assessment
- Uncertainty quantification
- Bias detection and mitigation
- Practical model implementation

### **Software Proficiency**
- **R packages**: `mgcv`, `lme4`, `brms`, `rstan`, `ANN2`, `mice`
- **Stan programming**: Bayesian model specification
- **Neural networks**: Architecture design and training
- **Model diagnostics**: Comprehensive model assessment

---

## Assessment Relevance

This module provides essential skills for the ATPA assessment, covering:
- Advanced modeling techniques beyond basic regression
- Model selection and comparison methodologies
- Handling complex data structures (missing data, hierarchical data)
- Fairness considerations in predictive modeling
- Practical implementation of cutting-edge methods

The comprehensive coverage of GAMs, mixed models, neural networks, and Bayesian methods prepares students for sophisticated modeling challenges they will encounter in actuarial practice.

---

## Real-World Applications

### **Insurance Applications**
- **Credibility theory**: Mixed models for experience rating
- **Claims modeling**: Severity and frequency prediction
- **Fair pricing**: Ensuring equitable treatment across groups
- **Risk assessment**: Advanced predictive modeling

### **Healthcare Applications**
- **Medical risk assessment**: Neural networks for patient outcomes
- **Longitudinal studies**: Mixed models for repeated measures
- **Missing data**: Handling incomplete medical records
- **Fair treatment**: Ensuring equitable healthcare access

### **Business Applications**
- **Hotel booking**: Revenue optimization and cancellation prediction
- **Credit scoring**: Default prediction with fairness considerations
- **Customer behavior**: Advanced segmentation and targeting
- **Performance prediction**: Employee and student outcomes

The module provides a comprehensive toolkit for addressing complex modeling challenges in actuarial science and related fields. 