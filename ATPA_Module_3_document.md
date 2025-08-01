

# **ATPA Module 3**

**Contents**

ATPA Module 3	[1](#heading)  
1 Advanced Models	[7](#1-advanced-models)  
1.1 Model Accuracy	[7](#1.1-model-accuracy)  
1.1.1 Module 3 Learning Objectives	[7](#1.1.1-module-3-learning-objectives)  
1.1.2 Section 3.1 Learning Objective	[9](#1.1.2-section-3.1-learning-objective)  
1.1.3 Software for Module 3	[10](#1.1.3-software-for-module-3)  
1.1.4 Introduction	[11](#1.1.4-introduction)  
1.1.5 Purposes of a Model	[12](#1.1.5-purposes-of-a-model)  
1.1.6 Model Workflow	[13](#1.1.6-model-workflow)  
1.1.7 Safety in the Context of Analytics	[14](#1.1.7-safety-in-the-context-of-analytics)  
1.1.8 Safety in the Context of Analytics \- Classification	[16](#1.1.8-safety-in-the-context-of-analytics---classification)  
1.1.9 Analytical Accuracy: Model Validation	[17](#1.1.9-analytical-accuracy:-model-validation)  
1.1.10 Analytical Accuracy: Model Validation	[18](#1.1.10-analytical-accuracy:-model-validation)  
1.2 Additive Models	[19](#1.2-additive-models)  
1.2.1 Section 3.2 Learning Objective	[19](#1.2.1-section-3.2-learning-objective)  
1.2.2 Introduction	[20](#1.2.2-introduction)  
1.2.3 Motivating Example	[21](#1.2.3-motivating-example)  
1.2.4 Simple Regression	[22](#1.2.4-simple-regression)  
1.2.5 Polynomial Regression	[23](#1.2.5-polynomial-regression)  
1.2.6 Log Transformation	[24](#1.2.6-log-transformation)  
1.2.7 Generalized Additive Models	[25](#1.2.7-generalized-additive-models)  
1.2.8 Generalized Additive Models	[26](#1.2.8-generalized-additive-models)  
1.2.9 R Implementation	[27](#1.2.9-r-implementation)  
1.2.10 Interpreting GAM Output	[28](#1.2.10-interpreting-gam-output)  
1.2.11 Interpreting GAM Output	[29](#1.2.11-interpreting-gam-output)  
1.2.12 Model Evaluation	[30](#1.2.12-model-evaluation)  
1.2.13 Variable Selection	[31](#1.2.13-variable-selection)  
1.2.14 Visualizing the Smooths	[32](#1.2.14-visualizing-the-smooths)  
1.2.15 Multiple Explanatory Variables	[33](#1.2.15-multiple-explanatory-variables)  
1.2.16 GAMs in GLMs	[34](#1.2.16-gams-in-glms)  
1.2.17 Summary	[35](#1.2.17-summary)  
1.2.18 Exercise 3.2.1: Data	[36](#1.2.18-exercise-3.2.1:-data)  
1.2.19 Exercise 3.2.1: Activities	[38](#1.2.19-exercise-3.2.1:-activities)  
1.2.20 Exercise 3.2.1: Solution	[39](#1.2.20-exercise-3.2.1:-solution)  
1.2.21 Exercise 3.2.1: Solution	[40](#1.2.21-exercise-3.2.1:-solution)  
1.3 Linear Mixed Models	[41](#1.3-linear-mixed-models)  
1.3.1 Section 3.3 Learning Objective	[41](#1.3.1-section-3.3-learning-objective)  
1.3.2 Introduction	[42](#1.3.2-introduction)  
1.3.3 Fixed versus Random Effects	[43](#1.3.3-fixed-versus-random-effects)  
1.3.4 Fixed versus Random Effects	[44](#1.3.4-fixed-versus-random-effects)  
1.3.5 Fixed versus Random Effects	[45](#1.3.5-fixed-versus-random-effects)  
1.3.6 When and When Not to Use Random Effects	[46](#1.3.6-when-and-when-not-to-use-random-effects)  
1.3.7 Fixed versus Random Effects	[47](#1.3.7-fixed-versus-random-effects)  
1.3.8 Fixed versus Random Effects	[48](#1.3.8-fixed-versus-random-effects)  
1.3.9 Mixed Model	[49](#1.3.9-mixed-model)  
1.3.10 Knowledge Check	[50](#1.3.10-knowledge-check)  
1.3.11 Random Intercepts Model	[53](#1.3.11-random-intercepts-model)  
1.3.12 Random Intercepts Model	[54](#1.3.12-random-intercepts-model)  
1.3.13 Random Intercepts Model	[55](#1.3.13-random-intercepts-model)  
1.3.14 Random Intercepts Model	[56](#1.3.14-random-intercepts-model)  
1.3.15 Prediction Without the Random Effect	[57](#1.3.15-prediction-without-the-random-effect)  
1.3.16 Random Slopes Model	[58](#1.3.16-random-slopes-model)  
1.3.17 Random Slopes Model	[59](#1.3.17-random-slopes-model)  
1.3.18 Exercise 3.3.1	[60](#1.3.18-exercise-3.3.1)  
1.3.19 Exercise 3.3.1 Solution	[61](#1.3.19-exercise-3.3.1-solution)  
1.3.20 Repeated Measures and Longitudinal Data	[62](#1.3.20-repeated-measures-and-longitudinal-data)  
1.3.21 Repeated Measures and Longitudinal Data	[63](#1.3.21-repeated-measures-and-longitudinal-data)  
1.3.22 Repeated Measures and Longitudinal Data	[64](#1.3.22-repeated-measures-and-longitudinal-data)  
1.3.23 Generalized Linear Mixed Model	[65](#1.3.23-generalized-linear-mixed-model)  
1.3.24 Exercise 3.3.2	[66](#1.3.24-exercise-3.3.2)  
1.3.25 Bühlmann–Straub Credibility	[67](#1.3.25-bühlmann–straub-credibility)  
1.3.26 Bühlmann–Straub Credibility	[68](#1.3.26-bühlmann–straub-credibility)  
1.3.27 Bühlmann–Straub Credibility	[69](#1.3.27-bühlmann–straub-credibility)  
1.3.28 Bühlmann–Straub Credibility	[70](#1.3.28-bühlmann–straub-credibility)  
1.3.29 Exercise 3.3.3	[71](#1.3.29-exercise-3.3.3)  
1.4 Neural Networks	[72](#1.4-neural-networks)  
1.4.1 Section 3.4 Learning Objective	[72](#1.4.1-section-3.4-learning-objective)  
1.4.2 Introduction	[73](#1.4.2-introduction)  
1.4.3 Example	[74](#1.4.3-example)  
1.4.4 Example	[75](#1.4.4-example)  
1.4.5 Neurons	[76](#1.4.5-neurons)  
1.4.6 Layers	[77](#1.4.6-layers)  
1.4.7 Overview of the Neural Network Modeling Process	[78](#1.4.7-overview-of-the-neural-network-modeling-process)  
1.4.8 Types of Neural Network Architecture: Feedforward	[79](#1.4.8-types-of-neural-network-architecture:-feedforward)  
1.4.9 Types of Neural Network Architecture: Feedforward	[80](#1.4.9-types-of-neural-network-architecture:-feedforward)  
1.4.10 Beyond Feedforward	[81](#1.4.10-beyond-feedforward)  
1.4.11 Activation Functions	[82](#1.4.11-activation-functions)  
1.4.12 Rectified Linear Unit Activation Function	[83](#1.4.12-rectified-linear-unit-activation-function)  
1.4.13 Sigmoid Activation Function	[84](#1.4.13-sigmoid-activation-function)  
1.4.14 Hyperbolic Tangent Activation Function	[85](#1.4.14-hyperbolic-tangent-activation-function)  
1.4.15 Softmax Activation Function	[86](#1.4.15-softmax-activation-function)  
1.4.16 Training the Neural Network: Loss Functions	[87](#1.4.16-training-the-neural-network:-loss-functions)  
1.4.17 Cross Entropy Loss Function: Binary Classification	[88](#1.4.17-cross-entropy-loss-function:-binary-classification)  
1.4.18 Cross Entropy Loss Function: Binary Classification	[89](#1.4.18-cross-entropy-loss-function:-binary-classification)  
1.4.19 Cross Entropy Loss Function: Multiclass Classification	[90](#1.4.19-cross-entropy-loss-function:-multiclass-classification)  
1.4.20 Hinge Loss Function for Classification	[91](#1.4.20-hinge-loss-function-for-classification)  
1.4.21 Loss Functions for Regression Problems	[92](#1.4.21-loss-functions-for-regression-problems)  
1.4.22 Training the Neural Network: Optimization Algorithms	[94](#1.4.22-training-the-neural-network:-optimization-algorithms)  
1.4.23 Types of Gradient Descent Algorithms	[95](#1.4.23-types-of-gradient-descent-algorithms)  
1.4.24 Generalizations of Gradient Descent Algorithms	[96](#1.4.24-generalizations-of-gradient-descent-algorithms)  
1.4.25 Example: Binary Classification	[97](#1.4.25-example:-binary-classification)  
1.4.26 The ANN2 Package	[98](#1.4.26-the-ann2-package)  
1.4.27 Overfitting	[99](#1.4.27-overfitting)  
1.4.28 Predictions and Comparison to Logistic Regression	[100](#1.4.28-predictions-and-comparison-to-logistic-regression)  
1.4.29 One-Hot Encoding	[101](#1.4.29-one-hot-encoding)  
1.4.30 Adding Categorical Variables to Binary Classification	[103](#1.4.30-adding-categorical-variables-to-binary-classification)  
1.4.31 Cross-Validation and Model Hyperparameters	[104](#1.4.31-cross-validation-and-model-hyperparameters)  
1.4.32 Activation Function for Hidden Layer(s)	[105](#1.4.32-activation-function-for-hidden-layer\(s\))  
1.4.33 Exercise 3.4.1	[106](#1.4.33-exercise-3.4.1)  
1.4.34 Exercise 3.4.2	[107](#1.4.34-exercise-3.4.2)  
1.4.35 Exercise 3.4.2: Possible Solution	[108](#1.4.35-exercise-3.4.2:-possible-solution)  
1.4.36 Example: Regression	[109](#1.4.36-example:-regression)  
1.4.37 Effect of Mini-Batch Size on Training	[111](#1.4.37-effect-of-mini-batch-size-on-training)  
1.4.38 Effect of Learning Rate on Training	[113](#1.4.38-effect-of-learning-rate-on-training)  
1.4.39 Exercise 3.4.3	[115](#1.4.39-exercise-3.4.3)  
1.4.40 Multiclass Classification Example	[116](#1.4.40-multiclass-classification-example)  
1.4.41 Exercise 3.4.4	[117](#1.4.41-exercise-3.4.4)  
1.4.42 Prediction With Multiple Classes	[118](#1.4.42-prediction-with-multiple-classes)  
1.4.43 Exercise 3.4.5	[119](#1.4.43-exercise-3.4.5)  
1.4.44 Neural Network Summary	[120](#1.4.44-neural-network-summary)  
1.4.45 Summary of Neural Network Modeling Procedure	[121](#1.4.45-summary-of-neural-network-modeling-procedure)  
1.4.46 Exercise 3.4.6: Summary Exercise	[123](#1.4.46-exercise-3.4.6:-summary-exercise)  
1.4.47 Exercise 3.4.6: Possible Solution	[124](#1.4.47-exercise-3.4.6:-possible-solution)  
1.4.48 Exercise 3.4.6: Possible Solution	[125](#1.4.48-exercise-3.4.6:-possible-solution)  
1.5 Bayesian Models and Analysis	[127](#1.5-bayesian-models-and-analysis)  
1.5.1 Section 3.5 Learning Objective	[127](#1.5.1-section-3.5-learning-objective)  
1.5.2 Introduction	[128](#1.5.2-introduction)  
1.5.3 Bayes’ Rule	[129](#1.5.3-bayes’-rule)  
1.5.4 Example: Poisson–Gamma	[132](#1.5.4-example:-poisson–gamma)  
1.5.5 Example: Poisson–Gamma	[134](#1.5.5-example:-poisson–gamma)  
1.5.6 Why Bayesian?	[136](#1.5.6-why-bayesian?)  
1.5.7 Markov Chain Monte Carlo	[137](#1.5.7-markov-chain-monte-carlo)  
1.5.8 Gibbs Sampler	[138](#1.5.8-gibbs-sampler)  
1.5.9 Metropolis–Hastings Sampler	[140](#1.5.9-metropolis–hastings-sampler)  
1.5.10 Hamiltonian Monte Carlo	[141](#1.5.10-hamiltonian-monte-carlo)  
1.5.11 Stan	[142](#1.5.11-stan)  
1.5.12 Install Stan	[143](#1.5.12-install-stan)  
1.5.13 Manuals	[144](#1.5.13-manuals)  
1.5.14 Basic Syntax	[145](#1.5.14-basic-syntax)  
1.5.15 Other Modeling Considerations	[146](#1.5.15-other-modeling-considerations)  
1.5.16 Burn-in Samples	[147](#1.5.16-burn-in-samples)  
1.5.17 Model Diagnostics	[148](#1.5.17-model-diagnostics)  
1.5.18 Example: Poisson–Gamma	[149](#1.5.18-example:-poisson–gamma)  
1.5.19 Example: Poisson–Gamma	[150](#1.5.19-example:-poisson–gamma)  
1.5.20 Poisson–Gamma Results	[151](#1.5.20-poisson–gamma-results)  
1.5.21 Poisson–Gamma Results	[152](#1.5.21-poisson–gamma-results)  
1.5.22 Prior Sensitivity	[153](#1.5.22-prior-sensitivity)  
1.5.23 Exercise 3.5.1	[154](#1.5.23-exercise-3.5.1)  
1.5.24 Exercise 3.5.1 Solution	[155](#1.5.24-exercise-3.5.1-solution)  
1.5.25 Other Software	[156](#1.5.25-other-software)  
1.5.26 Bayesian Linear Regression	[157](#1.5.26-bayesian-linear-regression)  
1.5.27 brms	[158](#1.5.27-brms)  
1.5.28 Example	[159](#1.5.28-example)  
1.5.29 Example: Simple Model Diagnostics	[160](#1.5.29-example:-simple-model-diagnostics)  
1.5.30 Example: Simple Model Comparison	[162](#1.5.30-example:-simple-model-comparison)  
1.5.31 Horseshoe Prior	[163](#1.5.31-horseshoe-prior)  
1.5.32 Example: Horseshoe Prior	[164](#1.5.32-example:-horseshoe-prior)  
1.5.33 Example: Horseshoe Prior	[165](#1.5.33-example:-horseshoe-prior)  
1.5.34 Predictions	[166](#1.5.34-predictions)  
1.5.35 Predictions	[167](#1.5.35-predictions)  
1.5.36 Generalized Linear Models	[168](#1.5.36-generalized-linear-models)  
1.5.37 Example: Count Data	[169](#1.5.37-example:-count-data)  
1.5.38 Example: Count Data Model Selection	[170](#1.5.38-example:-count-data-model-selection)  
1.5.39 Example: Count Data Model Selection	[171](#1.5.39-example:-count-data-model-selection)  
1.5.40 Example: Count Data Prediction	[172](#1.5.40-example:-count-data-prediction)  
1.5.41 Model Evaluation	[173](#1.5.41-model-evaluation)  
1.5.42 Exercise 3.5.2	[174](#1.5.42-exercise-3.5.2)  
1.5.43 Exercise 3.5.2 Solution	[175](#1.5.43-exercise-3.5.2-solution)  
1.5.44 Exercise 3.5.2 Solution Continued	[176](#1.5.44-exercise-3.5.2-solution-continued)  
1.6 Stacking	[177](#1.6-stacking)  
1.6.1 Section 3.6 Learning Objective	[177](#1.6.1-section-3.6-learning-objective)  
1.6.2 Introduction	[178](#1.6.2-introduction)  
1.6.3 Example: Hotel	[179](#1.6.3-example:-hotel)  
1.6.4 Stage-0 Models	[180](#1.6.4-stage-0-models)  
1.6.5 Meta-models	[181](#1.6.5-meta-models)  
1.6.6 Model Comparison	[182](#1.6.6-model-comparison)  
1.6.7 Other Stacking Details	[183](#1.6.7-other-stacking-details)  
1.6.8 Exercise 3.6.1	[184](#1.6.8-exercise-3.6.1)  
1.6.9 Exercise 3.6.1 Solution	[185](#1.6.9-exercise-3.6.1-solution)  
1.7 Further Modeling Topics	[186](#1.7-further-modeling-topics)  
1.7.1 Section 3.7 Learning Objectives	[186](#1.7.1-section-3.7-learning-objectives)  
1.7.2 Introduction	[187](#1.7.2-introduction)  
1.7.3 Large p, Small n	[188](#1.7.3-large-p,-small-n)  
1.7.4 Naïve Models	[189](#1.7.4-naïve-models)  
1.7.5 Feature Selection or Engineering	[190](#1.7.5-feature-selection-or-engineering)  
1.7.6 Dimension Reduction	[191](#1.7.6-dimension-reduction)  
1.7.7 Regularization	[192](#1.7.7-regularization)  
1.7.8 How Many Data Sets?	[193](#1.7.8-how-many-data-sets?)  
1.7.9 How Many Data Sets?	[194](#1.7.9-how-many-data-sets?)  
1.7.10 Missing Data and Predictions	[196](#1.7.10-missing-data-and-predictions)  
1.7.11 Missing Data and Predictions	[197](#1.7.11-missing-data-and-predictions)  
1.7.12 Example: Method 1 \- Combined Imputation	[198](#1.7.12-example:-method-1---combined-imputation)  
1.7.13 Example: Method 2 \- Stored Imputation Scheme	[199](#1.7.13-example:-method-2---stored-imputation-scheme)  
1.7.14 Example: Comparison	[200](#1.7.14-example:-comparison)  
1.7.15 Other Hold-out Approaches	[201](#1.7.15-other-hold-out-approaches)  
1.7.16 Missing Data and Ethics	[202](#1.7.16-missing-data-and-ethics)  
1.7.17 Ethics in Modeling	[203](#1.7.17-ethics-in-modeling)  
1.7.18 Fairness in Analytics	[204](#1.7.18-fairness-in-analytics)  
1.7.19 Example: COMPAS	[205](#1.7.19-example:-compas)  
1.7.20 Fairness in Analytics	[206](#1.7.20-fairness-in-analytics)  
1.7.21 Concepts of Algorithmic Fairness	[207](#1.7.21-concepts-of-algorithmic-fairness)  
1.7.22 Disparate Treatment vs Disparate Impact	[208](#1.7.22-disparate-treatment-vs-disparate-impact)  
1.7.23 Direct and Indirect Discrimination	[209](#1.7.23-direct-and-indirect-discrimination)  
1.7.24 Unawareness and Demographic Parity	[210](#1.7.24-unawareness-and-demographic-parity)  
1.7.25 Example: Unawareness and Demographic Parity	[211](#1.7.25-example:-unawareness-and-demographic-parity)  
1.7.26 Predictive Parity	[212](#1.7.26-predictive-parity)  
1.7.27  Predictive Parity in Regression	[213](#1.7.27-predictive-parity-in-regression)  
1.7.28 Examples: Predictive Parity	[214](#1.7.28-examples:-predictive-parity)  
1.7.29 Group vs Individual Fairness Metrics	[215](#1.7.29-group-vs-individual-fairness-metrics)  
1.7.30 Example: Fairness Metrics	[216](#1.7.30-example:-fairness-metrics)  
1.7.31 Other Fairness Metrics	[217](#1.7.31-other-fairness-metrics)  
1.7.32 Demographic Parity	[218](#1.7.32-demographic-parity)  
1.7.33 Predictive Parity	[219](#1.7.33-predictive-parity)  
1.7.34 Proxy Discrimination	[220](#1.7.34-proxy-discrimination)  
1.7.35 Proxy Discrimination	[221](#1.7.35-proxy-discrimination)  
1.7.36 Proxy Discrimination	[222](#1.7.36-proxy-discrimination)  
1.7.37 Proxy Discrimination	[223](#1.7.37-proxy-discrimination)  
1.7.38 Types of Proxy Discrimination	[224](#1.7.38-types-of-proxy-discrimination)  
1.7.39 Types of Proxy Discrimination	[225](#1.7.39-types-of-proxy-discrimination)  
1.7.40 Addressing Proxy Discrimination	[226](#1.7.40-addressing-proxy-discrimination)  
1.7.41 Framework	[227](#1.7.41-framework)  
1.7.42 Orthogonal Variables	[228](#1.7.42-orthogonal-variables)  
1.7.43 Pope–Sydnor Model	[229](#1.7.43-pope–sydnor-model)  
1.7.44 Exercise 3.7.1	[230](#1.7.44-exercise-3.7.1)  
1.7.45 Exercise 3.7.1 Solution	[231](#1.7.45-exercise-3.7.1-solution)  
1.7.46 Exercise 3.7.2	[233](#1.7.46-exercise-3.7.2)  
1.7.47 Exercise 3.7.2 Solution	[234](#1.7.47-exercise-3.7.2-solution)  
1.7.48 Biases Introduced After Model Build	[235](#1.7.48-biases-introduced-after-model-build)  
1.7.49 Fairness Summary	[237](#1.7.49-fairness-summary)  
1.7.50 Module 3 Bibliography	[238](#1.7.50-module-3-bibliography)

# **1 Advanced Models** {#1-advanced-models}

## ***1.1 Model Accuracy*** {#1.1-model-accuracy}

### **1.1.1 Module 3 Learning Objectives** {#1.1.1-module-3-learning-objectives}

Advanced Models

Component Table1

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Module 3 Learning Objectives |
| Content |  Explain the importance of model accuracy. Explain, fit, evaluate, and make predictions with additive models. Explain, fit, evaluate, and make predictions with linear mixed models. Explain, fit, evaluate, and make predictions with neural networks. Apply Bayesian techniques to linear models. Explain the benefits of and demonstrate the combination of multiple models via stacking. Recognize and mitigate the effects of starting with too many variables. Recognize and mitigate the effects of repeated use of train/test/validate sets. Be able to make predictions with missing data. Explain why being blind to sensitive or prohibited variables is not sufficient to ensure lack of bias. Explain, evaluate, and correct for analytical bias, such as proxy bias.  |
| Footer | Panel Footer |

 Module 3

### **1.1.2 Section 3.1 Learning Objective** {#1.1.2-section-3.1-learning-objective}

Model Accuracy

Component Table2

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.1 Learning Objective**  Explain the importance of model accuracy.  |
| Footer | Panel Footer |

### **1.1.3 Software for Module 3** {#1.1.3-software-for-module-3}

Python currently has great functionality for processing data and implementing many predictive models. Unfortunately, the current Python implementation (as of March 2022\) of many of the models to be covered in Module 3 have significantly less functionality than their R counterparts. For example, additive models can be fit in Python using **statsmodels**, but it requires a lot of specification that the R package **mgcv** does automatically. An alternative is **pygam**, but the authors have documented that the AIC and *p*\-values they provide are incorrect. Therefore, we will only provide R implementations of the models in Module 3\. 

For the assessment, you can still use your language of choice, but we recommend that R be used for these models as the R code provided in this module will enable you to implement these models.  
Software for Module 3

### **1.1.4 Introduction** {#1.1.4-introduction}

As part of Exams SRM and PA, you have seen some very effective modeling techniques. Mastery of those techniques is an incredibly valuable skill to have in the modern age, where data drives decisions. The main models that served as the focus of those exams were (generalized linear) regression and tree-based models. 

In addition to these basic building blocks, extensions were made for additional purposes. Elastic net regression performs simultaneous estimation and inference on regression coefficients in linear models. Ensemble models use bagging or boosting to build many models and combine the outputs. 

Principal components analysis (PCA) and clustering were used for variable creation and data exploration. While these can be considered models for prediction or inference on their own, the focus was to investigate the data and support the other model building techniques.  
Introduction

### **1.1.5 Purposes of a Model** {#1.1.5-purposes-of-a-model}

A perfectly fit and perfectly tuned model is still not useful if the model itself is not properly chosen. Deciding which model to use is driven primarily by the purpose of the model. For example, if the only goal is prediction and minimizing prediction error, ensemble methods such as random forests are worth considering. In contrast, if the primary goal is model explainability, then a simpler model might be better than a more complicated model despite reduced accuracy. 

The type of model affects data preparation. For example, interaction terms can improve a linear model but do little for a decision tree. Missing data and outliers may be handled differently depending on which model is being used.   
Even when certain models have been chosen given the business problem, there are still several steps to build the model. Model settings need to be determined such as which variables to use in a regression model or how many nodes to include in a decision tree.  
Purposes of a Model

### **1.1.6 Model Workflow** {#1.1.6-model-workflow}

There are many steps to build a model, and in some applications, certain steps may be skipped or expanded in various ways, so there is not a single workflow that can apply to every possible scenario. Also, several steps may need to be iterated, so moving backward (even within stages) is possible. For example, perhaps you choose a suite of models, but then something seen in the model fits suggests that a different model should be added, which may cause a modeler to return to proposing a new model or preparing the data differently. Note that the first step in building any model is to understand the business problem. Once that is established, this is a possible modeling workflow. 

Another reason to follow a modeling process such as this one is to be accurate. By skipping steps or taking shortcuts, errors in the modeling process can lead to bias. The remainder of this section deals with the importance of being accurate.   
Model Workflow

### **1.1.7 Safety in the Context of Analytics** {#1.1.7-safety-in-the-context-of-analytics}

In the context of analytics, safety relates to analyzing the data in the model consistently and as intended. Modeling requires an appropriate understanding of the problem’s definition, data, and modeling approach.

Models should meet the intended purpose and efforts should be made so that they are not misused or misinterpreted. The design, development, and modification of the model should be consistent with the intended purpose.

In completing the modeling, causation and association should be distinguished. Further, it is important to avoid misusing or misinterpreting statistical features, such as Simpson’s paradox and P-hacking. These topics will be defined and covered later within this section.

Predictive models are optimized to maximize predictive power, given a data set and modeling parameters. Accuracy is also an aspect of safety, as the predictive model aims to minimize any potential prediction error. For example, a predictive model with no better accuracy than a random coin toss may not be of value.

While accuracy is a desired trait from a technical standpoint, poor predictions can cause significant harm.

Safety in the Context of Analytics

Component Table3

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Model Safety  |
| Content |  Does the model...  Analyze consistently Understand the problem's definition, data, and algorithm Meet the intended purpose Identify causation and association Avoid misuse or misinterpretation of statistical features Measure precision and accuracy Identify sensitivity and specificity measures  |
| Footer | Panel Footer |

### **1.1.8 Safety in the Context of Analytics \- Classification** {#1.1.8-safety-in-the-context-of-analytics---classification}

A classification problem can help demonstrate the connection between safety and model accuracy. In classification models, a true positive is when the actual category and the predicted category are both positive. A true negative happens when the actual category and predicted category are both negative. False positives occur when the actual category is negative and the predicted category is positive. False negatives occur when the actual category is positive and the predicted category is negative. A confusion matrix counts the number of observations that fall into each of these four groups. 

Several statistical measures can be calculated using confusion matrices. 

* As a general measure of model performance, the **overall accuracy** can be calculated as (true positive \+ true negative) / total number of records.   
* The **sensitivity** measures the proportion of actual positives correctly classified and can be measured as true positive / (true positive \+ false negative).  
* The **specificity** measures the performance of the model predicting negative outcomes and is calculated as true negative / (false positive \+ true negative). 

Models are not perfect, and generally decisions need to be made regarding the trade-off between true positives, true negatives, false positives and false negatives. This consideration is an important assessment to help understand which error is more costly and for which additional testing may be warranted. It is often a subjective judgement that requires evaluation of ethical considerations. A fire alarm is an example where most individuals believe that the cost of false negatives (the alarm not going off if there actually is a fire) significantly outweighs the cost of false positives (the annoyance of an alarm without a fire). This cost consideration results in a reasonably sensitive alarm that might warn when there is benign smoke coming from a cooking oven.  
Safety in the Context of Analytics \- Classification

### **1.1.9 Analytical Accuracy: Model Validation** {#1.1.9-analytical-accuracy:-model-validation}

Model validation helps inform us on how useful a model is (Hunton, n.d.) and how accurately it predicts the response. Model validation may also depend on the intended purpose of the model. Beyond validating the prediction of the model, model fit can be assessed in a variety of different ways.  
Analytical Accuracy: Model Validation

Component Table4

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | In-sample Validation |
| Tab 1 Content | In-sample validation refers to the goodness of fit the model has with the data it has been trained on. One example of in-sample validation is residual analysis. Residual analysis is calculating the difference between the actual outcome values and the outcome values predicted by the model and looking at the distribution of the errors. Residual analysis can help highlight if a systematic trend exists, which would indicate errors are not random. While in-sample validation may help interpret the training data, it may lead to overfitting to the data and not generalize well to new data. |
| Tab 2 Title | Out-of-sample Validation |
| Tab 2 Content | Out-of-sample validation refers to using data not used in model training to validate the model. Out-of-sample validation tests how well the model predicts results for unseen data. Actual vs expected plots, simple quantile plots, and double lift charts are some methods that can help assess and compare model fit between candidate models (Goldburd, Khare, Tevet, & Guller, 2019).  |

### **1.1.10 Analytical Accuracy: Model Validation** {#1.1.10-analytical-accuracy:-model-validation}

Validation and assessing the predictive power of a model helps to ensure that the features used in the model have a clear relationship to the risk, a key ethical consideration. The modeler should recognize balance is needed, so that the model is not overfit (identifying features that may not have a relationship to the risk) but also does not miss relevant relationships between the variables. 

**Bias** is the absolute difference between the average prediction of the model and the actual value being predicted. **Variance** is the variability of model prediction due to using estimated parameters rather than their true values. There is a trade-off between bias and variance that is important to consider, as a model with high bias may oversimplify findings, but a model with high variance may not generalize well to new data. 

Note that a third element of prediction error, the random nature of the observations, cannot be reduced by obtaining a better model or better or more data.  
Analytical Accuracy: Model Validation

## ***1.2 Additive Models*** {#1.2-additive-models}

### **1.2.1 Section 3.2 Learning Objective** {#1.2.1-section-3.2-learning-objective}

Additive Models

Component Table5

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.2 Learning Objective**  Explain, fit, evaluate, and make predictions with additive models.  |
| Footer | Panel Footer |

### **1.2.2 Introduction** {#1.2.2-introduction}

Generalized additive models are an extension of linear models that allow more flexibility in the relationship of each variable to the target. In this section the basic additive model will first be introduced and then the generalized version (akin to the generalized linear model) will be covered.  
Introduction

### **1.2.3 Motivating Example** {#1.2.3-motivating-example}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_3\_2\_r.rmd\]  
We begin our discussion of additive models with an example. At this time, download the Rmd file ( [atpa\_3\_2\_r.rmd](#bookmark=id.bihmgj1m410z) ) and the traffic data set ( [traffic\_data.csv](#bookmark=id.dqtjt76uttcq)). This data set records the traffic flow in both directions on an imaginary highway by the hour of the day. The plot below shows the data and which observations are in the training and holdout sets.  
\[END LINK\]  
Motivating Example

Component Table6

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 1 to load the data and make the plot. |

We see that there is little traffic in the early morning, increasing to the morning rush hour, decreasing slightly in the middle of the day, increasing to the afternoon rush hour, and then decreasing to the end of the day.

### **1.2.4 Simple Regression** {#1.2.4-simple-regression}

Simple linear regression will do a poor job of modeling this clearly non-linear process with respect to hour and predicting the holdout observations.  
Simple Regression

Component Table7

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 2 to fit the model and make the plot. |

### **1.2.5 Polynomial Regression** {#1.2.5-polynomial-regression}

What about adding polynomial terms to our model?  
Polynomial Regression

Component Table8

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 3 shows the model fits for a polynomial regression model with orders of 1 (linear), 2, 3, 5, 8, and 10\. |

The smaller order polynomials don’t properly model the process, especially the bimodality. The higher order polynomials overfit, providing extremely poor estimates outside the available data, i.e., hours 0, 1, 22, and 23\.

### **1.2.6 Log Transformation** {#1.2.6-log-transformation}

We see in the plots below that the model doesn’t do any better other than constraining the response to be positive.  
Log Transformation

Component Table9

| Type | Callout |
| :---- | :---- |
| Content | As an alternative, because the response is positive, we could model the log of traffic (CHUNK 4). |

### **1.2.7 Generalized Additive Models** {#1.2.7-generalized-additive-models}

Generalized Additive Models provide a flexible framework for modeling nonlinear relationships that doesn’t have the same extrapolation issues of polynomial regression.  
Generalized Additive Models

Component Table10

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 5 fits an additive model to this data. |

While the more general gam() function is used, the default normal distribution and identity link are used, making this model an analog of an ordinary linear model. From this point on, the broader term, Generalized Additive Model (GAM) will be used.

### **1.2.8 Generalized Additive Models** {#1.2.8-generalized-additive-models}

GAMs differ from standard regression models in that the relationship between the explanatory and response variables are flexibly defined with a smooth function rather than a straight line. More specifically, here is the standard linear regression model with a single explanatory variable:   
![][image1].   
The GAM model is:   
![][image1].   
Here *f*(*x*) is essentially any function of *x*. The linear regression model is a special case, where *f*( *x* ) \= *β*1*x*. To be able to efficiently estimate the function, we will define it as a sum of basis functions. Basis functions are functions that focus on a certain characteristic of the data. The model becomes:   
![][image1]  
where the *Bi*(*x*) are basis functions and the γ*i* are weights (they could also be considered as regression coefficients). It seems a little complicated until you realize that we did the exact same thing in polynomial regression where the basis functions were *x*, *x*2, ... , *xd*. 

Generalized Additive Models

### **1.2.9 R Implementation** {#1.2.9-r-implementation}

In R we will use the package **mgcv** which stands for “mixed GAM computation vehicle” (with Automatic Smoothness Estimation). The main function we will use is the gam() method, which outputs a gam object. Its implementation is similar to the glm() method in base R. There are many options that can be adjusted, but we will only focus on a few. Almost all the settings are the same as they are in glm(). 

The biggest difference is in the formula. In our traffic example, the standard linear regression model would be specified like this: 

lm(Traffic \~ Hour).

R Implementation

Component Table11

| Type | Callout |
| :---- | :---- |
| Content | We could specify a GAM the same way and it will give the exact same result (CHUNK 6): gam(Traffic \~ Hour). |

The power of the GAM comes from adding the smooths (the sum of basis functions described previously). By changing the model slightly we allow the relationship between the hour of day and the traffic to be nonlinear. 

gam(Traffic \~ s(Hour)).

The maximum dimension of the smooth can be set with the *k* option (this is the *d* in our formula). The package uses penalized regression to fit the model, which keeps the weights from getting unnecessarily large.

### **1.2.10 Interpreting GAM Output** {#1.2.10-interpreting-gam-output}

The summary statistics of a GAM are different from lm() or glm(). 

The first three lines show the family, the link function, and the formula. The next section provides the parametric (non-smooth) coefficients. This will include all variables where you didn’t include a smooth and the intercept. In this case it only has the intercept.  
Interpreting GAM Output

Component Table12

| Type | Callout |
| :---- | :---- |
| Content | This has the same interpretation as in a generalized linear model, and in CHUNK 6 we show that the results are exactly the same if we remove the smooth from *Hour*. |

Component Table13

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | CHUNK 5 Output |
| Content |  Family: gaussian Link function: identity Formula: Traffic \~ s(Hour) Parametric coefficients:  Estimate Std. Error t value Pr(\>|t|)  (Intercept) 1250.00 12.58 99.36 6.34e-14 \*\*\* Approximate significance of smooth terms:  edf Ref.df F p-value  s(Hour) 8.802 8.989 315.5 \<2e-16 \*\*\* R-sq.(adj) \= 0.994 Deviance explained \= 99.7% GCV \= 6254.8 Scale est. \= 2848.9 n \= 18  |
| Footer | Panel Footer |

The next section shows the summary of the smooth terms. The effective degrees of freedom (edf) are a measure of the “wigglyness” of the smooth. The Ref.df column can be ignored. The *p*\-value is an approximate measure of the significance of the smooth, based on the F-statistic. In this case, we can be confident that the smooth is significantly valuable in this model. 

The GCV is the generalized cross-validation score, which can be taken as an estimate of the mean squared prediction error based on leave-one-out (LOO) cross validation. As in other cases, it does not tell us much on its own, but can be used to compare GAMs.

### **1.2.11 Interpreting GAM Output** {#1.2.11-interpreting-gam-output}

A gam object can be passed into the AIC method for model comparison.  
Interpreting GAM Output

Component Table14

| Type | Callout |
| :---- | :---- |
| Content | In CHUNK 7 we see that the GAM model outperforms all the polynomial regression models (something we already knew by just looking at it). |

Just using the default specifications work well generally, but they should be checked. That is what we will do next. 

### **1.2.12 Model Evaluation** {#1.2.12-model-evaluation}

The main method we will use for model evaluation is gam.check(). It takes a gam model object and produces four residual plots, convergence information about the smoothness selection, and diagnostic tests of whether the basis choices are adequate (for this exam and most applications, thin-plate regression splines, the default, are sufficient). The four residual plots are all plots that you have seen before. The convergence information will make an issue obvious (in our case, there is no issue). You want to see that the smoothing parameter converged and the Hessian is positive definite. 

The final test determines whether the basis dimension for a smooth is adequate. The test statistic is called the *k*\-index. The further the *k*\-index is below one, the more likely it is that a pattern in the data was missed by having too small a dimension. The *p*\-value is computed through simulation. Low *p*\-values may also indicate that the basis dimension was set too low. If there is a potential issue, increasing *k* and refitting makes sense.  
Model Evaluation

Component Table15

| Type | Callout |
| :---- | :---- |
| Content | In our case (CHUNK 8\) there don’t appear to be any issues. The *p*\-value is large, and the *k*\-index is above 1\. In CHUNK 9 we fit a model with many fewer dimensions ( *k* \= 4). Looking at a plot of the model, we see that the fit is much worse. The same result is borne out in gam.check(). The *k*\-index is a good bit below 1 and the *p*\-value is very low. In CHUNK 10 we fit a model with many more dimensions ( *k* \= 17). We find this one passes the test as well as the test only determines if the dimension is too small, not too large. The penalization should protect the model from having too many dimensions. |

### **1.2.13 Variable Selection** {#1.2.13-variable-selection}

While the traffic example only has one predictor, which we make a smooth, you can have as many predictors (and smooths) in your model as you would like, at the cost of degrees of freedom and complexity. Just like a GAM is additive in terms of adding the basis functions to make a smooth, a GAM is additive in that you can add multiple predictors and smooths. The prediction function becomes:   
![][image2]  
Here each of the functions, which are independent from one another, is a sum of basis functions (which may be a single linear term if no smooth is applied). 

One of the options in a GAM is select. If select is TRUE, an additional penalty term is added to each smooth, enabling terms to shrink all the way to zero and out of the model. This will give you some information but should not be used like LASSO, which we depend on to remove all non-significant terms. 

Variable Selection

Component Table16

| Type | Callout |
| :---- | :---- |
| Content | An example is provided in CHUNK 11\. |

We fit a model where there are ten predictors, but only two relate to the target variable. *x1* relates linearly, while *x2* relates through the sine function. We then fit a GAM with smooths on all of the terms and set select \= TRUE. Only the fourth and ninth variables were removed from the model (as witnessed by their estimated degrees of freedom being essentially equal to 0).

### **1.2.14 Visualizing the Smooths** {#1.2.14-visualizing-the-smooths}

The plot() function provides plots and intervals of all the smooths. Looking at this smooth of *x1*, we see the strong positive linear relationship. In *x2*, we see the sine wave, with some uncertainty at the extremes. In *x4*, we see the perfectly flat line at 0\. 

With the *x1* term being so obviously linear, it would probably be good to refit the model with *x1* not having a smooth. 

The graphs also show how predictions are made. For each predictor variable, determine the corresponding value from the graph, add them up, and add the intercept.  
Visualizing the Smooths

### **1.2.15 Multiple Explanatory Variables** {#1.2.15-multiple-explanatory-variables}

As noted, GAMs can be used to fit models with any number of explanatory variables. Some can have smooths, while others are left as linear. Simply surround those you want to be a smooth with the s(). Those that are not smooth will be treated the same way that glm() would treat them. Categorical variables would never use smooths because after binarization they are just zero or one. We will fit some models with multiple predictors in the exercise.  
Multiple Explanatory Variables

### **1.2.16 GAMs in GLMs** {#1.2.16-gams-in-glms}

While in this module we focus on using GAMs within ordinary linear models, they can be used just as easily within GLMs, providing non-linear predictor relationships to any type of response variable. That is, alternative distributions and link functions can be selected.  
GAMs in GLMs

### **1.2.17 Summary** {#1.2.17-summary}

GAMs relax the requirement of linear effects in both LMs and GLMs while preserving interpretability. Smooth effects are easy to visualize and understand. With the implementation in R, adding smooths costs very little in coding or computing time and can pay large dividends if the effects are nonlinear.  
Summary

### **1.2.18 Exercise 3.2.1: Data** {#1.2.18-exercise-3.2.1:-data}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/hotel\_bookings\_small.csv\]  
We will use a small data set of hotel booking information ( [hotel\_bookings\_small.csv](#bookmark=id.9tgi9swxzx2b)). 

The data is originally from the article Hotel Booking Demand Datasets, written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019\. The data was downloaded and cleaned by Thomas Mock and Antoine Bichat for \#TidyTuesday during the week of February 11th, 2020\.  
\[END LINK\]  
Exercise 3.2.1: Data

Component Table17

| Type | Callout |
| :---- | :---- |
| Content | Space to do your analysis is in CHUNK 12 with a solution in CHUNK 13\. |

Component Table18

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **This data set contains the following variables:**  |
| Content |  ***is\_canceled:*** value indicating if the booking was canceled (1) or not (0) ***lead\_time*** *:* Number of days between the booking and the arrival date ***stays\_in\_weekend\_nights:*** Number of weekend nights (Sa–Su) booked to stay ***stays\_in\_week\_nights:*** Number of weekday nights (M–F) booked to stay ***adults:*** Number of adults ***children:*** Number of children ***babies:*** Number of babies ***market\_segment:*** Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators” ***previous\_cancellations:*** Number of previous bookings that were cancelled by the customer prior to the current booking ***previous\_bookings\_not\_canceled:*** Number of previous bookings not cancelled by the customer prior to the current booking ***booking\_changes:*** Number of changes/amendments made to the booking ***deposit\_type:*** Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories:  No Deposit: No deposit was made. Non Refund: A deposit was made in the value of the total stay cost. Refundable: A deposit was made with a value under the total stay cost. ***adr:*** Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of staying nights ***required\_car\_parking\_spaces:*** Number of car parking spaces required by the customer ***total\_of\_special\_requests:*** Number of special requests made by the customer (e.g. twin bed or high floor) |
| Footer | Panel Footer |

### **1.2.19 Exercise 3.2.1: Activities** {#1.2.19-exercise-3.2.1:-activities}

Exercise 3.2.1: Data  
For this exercise, we will try to predict the average daily rate ( *adr*) using the total length of the stay, the number of adults in the room, the lead time, and the market segment. The following activities are to be completed: 

1. Create the variable *total\_stay* by adding the number of weeknights (*stays\_in\_week\_nights*) and weekend nights (*stays\_in\_weekend\_nights*).  
2. Divide the dataset into train and test sets with an 80/20 split.  
3. Fit a GAM that only contains a smooth on *total\_stay* and no other predictors.  
4. Plot the predicted values of this model for the test set. Your plot should include a scatter plot of test set x and y values. Also plot the smooth using plot().  
5. Compare the following four models using test mean squared prediction error (the one above plus three more):   
   1. GAM with a smooth on *total\_stay* and no other predictors.  
   2. GAM with smooth on *total\_stay* and linear terms for *lead\_time*, *adults*, and *market\_segment*.  
   3. LM with only *total\_stay*.  
   4. LM with *total\_stay*, *lead\_time*, *adults*, and *market\_segment*.  
6. Perform model diagnostics on the two GAMs.  
7. With your chosen model, comment on the parameter estimates and the significance of the various predictors.  
8. Examine the predicted values for possible issues. How could you adjust the model to prevent these issues?

### **1.2.20 Exercise 3.2.1: Solution** {#1.2.20-exercise-3.2.1:-solution}

The plot for the model with only the smooth on total stay is at the right along with the plot of the smooth. As expected, the plots are similar, the difference being the need to add the intercept of 103 to obtain the predictions. 

We see that the GAM fit is nonlinear. We then fit all four of the models, run diagnostics on the GAMs (no issues) and compare their test MSEs. 

The GAM model with all the predictors had the best MSE. We also notice that moving from a linear model to a GAM had an impact, but the impact was dwarfed by the impact of including the other predictors.  
Exercise 3.2.1: Solution

| LM1 (only *total\_stay*) | LM2 (all) | GAM1 (only *total\_stay*) | GAM2 (all) |
| :---: | :---: | :---: | :---: |
| 2162.86 | 1814.57 | 2131.98 | 1798.51 |

### **1.2.21 Exercise 3.2.1: Solution** {#1.2.21-exercise-3.2.1:-solution}

Exercise 3.2.1: Solution

Component Table19

| Type | Callout |
| :---- | ----- |
| Content | We fit four models (CHUNK 14), a linear model, a GLM, an LM with a smooth on *total\_stay*, and a GLM with a smooth on *total\_stay*. The results are below:  **LM LM-GAM GLM GLM-GAM** 1814.57 1798.51 1757.09 1747.82  |

Looking at the summary of GAM2, the number of adults, whether the room was complimentary (that should have a large impact on the price), and the smooth on *total\_stay* all had a significant impact on the predictions. Looking more closely at the fitted values, we see that some of the predictions are negative. 

To address this problem, we could shift the negative predictions to zero (a little hacky), log transform the responses, or fit a GLM. We will use a gamma GLM on 1 \+ *adr* (since the gamma GLMs cannot handle zeros in the data).  
The best model is the GLM with the smooth term. It looks like using the gamma family had a larger impact but adding the smooth improved the model whether an LM or GLM.

## ***1.3 Linear Mixed Models*** {#1.3-linear-mixed-models}

### **1.3.1 Section 3.3 Learning Objective** {#1.3.1-section-3.3-learning-objective}

Linear Mixed Models

Component Table20

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.3 Learning Objective**  Explain, fit, evaluate, and make predictions with linear mixed models.  |
| Footer | Panel Footer |

### **1.3.2 Introduction** {#1.3.2-introduction}

A basic regression model assumes independence of observations. While this is a convenient assumption, it is often incorrect. One way to deal with correlation between observations is a **mixed model**. The basic idea of a mixed mode l is that certain observations will be treated as correlated or connected in ways that help make the model more realistic. We begin by discussing the difference between fixed and random effects. We will then fit and interpret a random intercepts mixed model and a random slopes mixed model. There are other types of mixed models that will not be covered, for example, to account for spatial variability or nonlinear growth over time. However, even the basic mixed models will be valuable tools in a wide variety of scenarios that may arise.  
Introduction

### **1.3.3 Fixed versus Random Effects** {#1.3.3-fixed-versus-random-effects}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/comp\_course.csv\]  
A fixed effect is a variable in a model that is treated as perfectly measured and constant for all observations. A standard regression model is a fixed effects model, because all the explanatory variables in the model are assumed to be fixed effects. Download the rmd file ( [atpa\_3\_3\_r.rmd](#bookmark=id.wcw9gm23nv7x)) and look the computer course data set ( [comp\_course.csv](#bookmark=id.thzy2hw1g8wm)). It includes grades for an introductory computing course for a specific semester at a university. The target variable, *grade*, is the final grade for the course. The explanatory variables are: 

* *professor*: The professor teaching the course  
* *year*: Collegiate year of the student (freshman, sophomore, …)  
* *major*: An indicator for if the student is a computer science major  
* *hours*: Hours spent studying for the final exam

Each of these variables can be placed as fixed effects into a standard regression model. 

Everything runs just fine and produces reasonable outputs. Each variable as a whole appears significant. Unlike other applications of categorical variables, we may not want to group levels that have insignificant differences as we are interested in each of the professors.  
\[END LINK\]  
Fixed versus Random Effects

Component Table21

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 1 loads in the data and plots the histogram of the target variable as seen here: CHUNK 2 runs a standard regression model assuming all the effects are fixed effects.  |

### **1.3.4 Fixed versus Random Effects** {#1.3.4-fixed-versus-random-effects}

From the boxplots it is clear that *professor* has a fairly strong relationship with *grade*. 

We can reasonably assume that future students who are taking this class will receive higher grades from Professor C than other professors. However, this data comes from a specific semester. What if Professor D is not teaching this class next year and is replaced by a new professor—is this model no longer valid or useful?  
Fixed versus Random Effects

### **1.3.5 Fixed versus Random Effects** {#1.3.5-fixed-versus-random-effects}

When the number of levels of a factor variable is fixed and will not change in the future, then they should be modeled as a fixed effect. When the levels of a factor variable that are observed are a subset of the total possible levels for that variable, it may not make sense to model it as a fixed effect. Instead, it can be modeled as a random effect. 

A **random effect** views an effect as a random sample from a population. One common indicator that a variable should be measured as a random effect is when the observed levels of a factor variable are a subset of the total possible levels that could be available for that variable. Professors teaching a computing course is a perfect example. Other professors could have taught that class. Treating the variable as a random effect accounts for the fact that the levels present are not the only possible levels.  
Fixed versus Random Effects

### **1.3.6 When and When Not to Use Random Effects** {#1.3.6-when-and-when-not-to-use-random-effects}

Why use random effects?   
It is important to properly account for random effects because there are multiple sources of variability. In the grade example, there is error that comes as the result of natural variation for each observation. This is accounted for by the variance term in a regression model. On top of this, there is an additional source of variability from the fact that the pool of possible professors that teach this class is larger than what is represented in the data. So, the reason to assign a variable as a random effect is to properly account for additional sources of variation. 

Why would you not use a random effect?   
You should assign a variable as a fixed effect when there are a fixed number of levels that are all represented in the data. Even when there are factor levels that are not represented, you may want to assign a variable as a fixed effect. If inference about a variable is important, it should be treated as a fixed effect. Assigning a variable as a random effect implies that the levels are random from a larger population. To specifically see what the effect of taking the class from Professor D is, treat professor as a fixed effect. But as we shall see, it is possible to still make an inference about Professor D even when treated as a random effect, though not all the customary diagnostic information will be available.  
When and When Not to Use Random Effects

### **1.3.7 Fixed versus Random Effects** {#1.3.7-fixed-versus-random-effects}

Like *professor*, the next variable in the model, *year*, is a significant variable, as can be seen in this plot. 

Also, like the variable *professor*, *year* is a factor variable with multiple levels. However, every single level of this factor variable is known and represented in the data. Every possible future individual would be one of these levels. For this reason, *year* should be modeled as a fixed effect.  
Fixed versus Random Effect

### **1.3.8 Fixed versus Random Effects** {#1.3.8-fixed-versus-random-effects}

The last two variables are an indicator for an individual having a specific college major and a variable for the hours studied for a test. In more advanced versions of mixed models, it is possible for nearly every variable type to be random in some way, however for the purposes of this course we can assume that binary and continuous variables are not appropriate candidates to be random effects. For this reason, both *major* and *hours* should be treated as fixed effects.  
Fixed versus Random Effect

### **1.3.9 Mixed Model** {#1.3.9-mixed-model}

To summarize, the variables in this data by type of effect are as follows:  
Mixed Model

| Variable | Type |
| ----- | ----- |
| *professor* | random |
| *year* | fixed |
| *major* | fixed |
| *hours* | fixed |

When there is a combination of fixed and random effects in a model, the result is called a **mixed model** or **mixed effects model**. You will use a mixed model whenever you have a random effect as one of your variables. As noted earlier, a standard regression model is a fixed effects model. Models with only random effects do exist, with an example later in this section. 

Consider the mixed model as a clustered model. There may be some grouping that separates the data according to the random effect. The model is fit to the whole data set, but each group is more similar within its own group than with the rest of the data as a whole. This can be seen in the computer course example where a certain professor's grades were more similar within each group than across groups. 

It can be shown that in a mixed model with a random effect that clusters or groups observations, the correlation between observations in the same group is non-zero. Independence is assumed in a standard regression model, meaning the correlation between observations is assumed to be zero. In contrast, adding a random effect creates a dependence between those observations that share a similar random effect.

### **1.3.10 Knowledge Check** {#1.3.10-knowledge-check}

Knowledge Check  
Choose the correct answer from the pulldowns.  
Determine whether you would use a fixed effect, random effect, or the type of effect is unclear for the designated variable in each of the following scenarios. Use the drop-down menus to make your selection.

The variable *country* in a study of how various factors affect population growth. Five countries are included in the study, but the model could be applied to many more. 

The variable *author* in a study of how many large words are in different types of novels. Twelve authors were included in the study. 

The variable *fertilizer* type in a study to determine how fertilizer affects plant growth. Three fertilizers were used in the study. 

The variable *education* level when studying how factors influence wealth. There are six education levels included in the study, incorporating everyone in the population. 

The variable *car brand* when studying how much damage costs to repair after accidents. Ten car brands were used in the study.  
Weight: 10  
Partial Scoring: Use Publishing Profile  
Circle one answer in each list

1.   
   * Fixed  
     * Random  
     * Unclear

**Correct:** Random  
**Feedback:** 

2.   
   * Unclear  
     * Random  
     * Fixed

**Correct:** Random  
**Feedback:** 

3.   
   * Fixed  
     * Unclear  
     * Random

**Correct:** Fixed  
**Feedback:** 

4.   
   * Fixed  
     * Random  
     * Unclear

**Correct:** Fixed  
**Feedback:** 

5.   
   * Unclear  
     * Fixed  
     * Random

**Correct:** Unclear  
**Feedback:** 

| Question Feedback |  |
| ----- | :---- |
| **All Correct** | country: random There are many more than five countries where factors could be measured to predict population growth. author: random There are more than the 12 authors included in the study. fertilizer: fixed There may be more fertilizer types, but the inference for fertilizer type is central to the study and should therefore be treated as fixed. education\_level:  fixed Because education level is split in such a way that it includes everyone in the population, all factor levels would already be accounted for. car brand: unclear The answer to this depends on the business problem. If car brand is an important inferential variable, it may work better as a fixed effect. If this model will be used in the future to predict damages for brands not included in this study or if there is some suspected clustering and dependence, it would be better as a random effect. |
| **All Incorrect** | country: random There are many more than five countries where factors could be measured to predict population growth. author: random There are more than the 12 authors included in the study. fertilizer: fixed There may be more fertilizer types, but the inference for fertilizer type is central to the study and should therefore be treated as fixed. education\_level:  fixed Because education level is split in such a way that it includes everyone in the population, all factor levels would already be accounted for. car brand: unclear The answer to this depends on the business problem. If car brand is an important inferential variable, it may work better as a fixed effect. If this model will be used in the future to predict damages for brands not included in this study or if there is some suspected clustering and dependence, it would be better as a random effect. |
| **Partially Correct** | country: random There are many more than five countries where factors could be measured to predict population growth. author: random There are more than the 12 authors included in the study. fertilizer: fixed There may be more fertilizer types, but the inference for fertilizer type is central to the study and should therefore be treated as fixed. education\_level:  fixed Because education level is split in such a way that it includes everyone in the population, all factor levels would already be accounted for. car brand: unclear The answer to this depends on the business problem. If car brand is an important inferential variable, it may work better as a fixed effect. If this model will be used in the future to predict damages for brands not included in this study or if there is some suspected clustering and dependence, it would be better as a random effect. |
| **Incorrect Attempt** |  |
| **Partially Correct Attempt** |  |

### **1.3.11 Random Intercepts Model** {#1.3.11-random-intercepts-model}

The most basic of any mixed model is a **random intercepts model**, which treats the random effect as if each group has a different intercept. For a simple regression model with one random effect and one fixed effect,   
![][image3]   
The term α*i* represents a random effect for group *i*. In this formula we index the data by group *i* and observation *j*. To extend this to the computer course example we have been discussing, the mixed model could be written as:   
![][image4]   
To make the indexing clear, for this example a subscript of 2,3 would mean the third observation from the second level of the random effect (Professor B in this case). 

Note that the random effect is not given a coefficient that needs to be estimated. Also note that there is still a fixed intercept term. The random effects in this case will sum to 0 so that the intercept maintains the interpretation from standard regression.  
Random Intercepts Model

Component Table22

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 3 fits a mixed model to the data and describes the syntax for a random intercepts model for the respective programming language. |

### **1.3.12 Random Intercepts Model** {#1.3.12-random-intercepts-model}

The following table provides the estimates for the fixed effects of the standard regression model and the mixed model.  
Random Intercepts Model

Component Table23

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 4 compares the estimates as well as the in-sample predictions between the linear model and the mixed model. The predictions are similar. |

Notice that the estimates are nearly identical. This is not always the case, but quite frequently changing a fixed effect to a random effect will not severely affect the other coefficient estimates.

| Variable | Year: Sophomore | Year: Junior | Year: Senior | hours | major |
| ----- | :---: | :---: | :---: | :---: | :---: |
| Standard | 2.49 | \-0.52 | \-6.54 | 0.968 | 4.26 |
| Mixed | 2.29 | \-0.51 | \-6.55 | 0.973 | 4.26 |

### **1.3.13 Random Intercepts Model** {#1.3.13-random-intercepts-model}

Each random effect still has a point estimate that can be found. 

Again, the effects are similar, although the random effect is consistently smaller in magnitude than the fixed effect. Such shrinkage is common in random effects models. The standard deviation of the random effect can be seen from the output. For this model the standard deviation of the random effect for professor is equal to 4.93. This means that a randomly drawn professor from the population of professors would have an effect with a mean of 0 and a standard deviation of 4.93.   
Random Intercepts Model

Component Table24

| Type | Callout |
| :---- | ----- |
| Content | CHUNK 5 finds the effect of each professor in the fixed effect only model and then it also finds the estimate for the random effect. These are given in the following table:  **Professor A B C D E** Fixed Effect \-4.01 1.15 6.40 2.60  \-6.14 Random Effect  \-3.87 1.11  6.08 2.46 \-5.77  |

This concept is important for prediction. Suppose a new observation is predicted and the professor is Professor C. The value for the random effect will be 6.08 as is estimated from the model fit. Suppose the professor is a new professor that is not included in the model. The value for the random effect will be 0, because that is the mean of the distribution of random effects. Then the variance of that estimate will increase by 4.932 2 or 24.29. This extra variation is needed because without any data we do not know if Professor F is an easier grader, such as Professor C, or a more difficult grader, like Professor E.

### **1.3.14 Random Intercepts Model** {#1.3.14-random-intercepts-model}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/comp\_course\_2.csv\]  
Download a new data set, ( [comp\_course\_2.csv](#bookmark=id.ti9rr6djy00f)), that includes 100 different students. It also includes a new professor, Professor F, who was not included in the data that was used to fit the data. A fixed effect only model would not be able to predict grades using the new data with Professor F. A mixed model can predict grades on all of the new data because it was built without the assumption that all possible levels of the professor variable were included.  
\[END LINK\]  
Random Intercepts Model  
Note that when the level of the random effect is included in the data that was used to fit the model, the effect should be included. For example, observations that include Professor C should be predicted using the random effect for Professor C because it will be more accurate. 

Notice how even though Professor F was not a professor included in the original model fit, their class is predicted with relative accuracy. Also, because it is unknown if Professor F is an easy or tough grader, predictions are centered around the center of all predictions for all professors.

Component Table25

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 6 to load the data and then make and plot the predictions. A plot of predictions against the actual grade is at the right. |

### **1.3.15 Prediction Without the Random Effect** {#1.3.15-prediction-without-the-random-effect}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/comp\_course\_2.csv\]  
When performing prediction for data from a mixed model, it is not necessary to add in the random effect. When the random effect is added in to a prediction, the predicted value will match very closely to a linear model. When the random effect is not included, the prediction means something else. In the computer course example, prediction without the effect for Professor provides an estimate of a student’s performance independent of the random effect. This might be important when you want to evaluate a student’s importance but you don’t want to arbitrarily inflate a student’s performance because they took the course from a Professor who is more likely to give higher grades. 

Predicting without the random effect may in many cases be the real prediction that applies to a business problem. In these cases the random effect is a nuisance effect, an effect that is observed but is in the way of the real effect we want to observe. 

Another example is judges at a competition. Suppose there are 5 judges and each competitor is only ever scored by one judge. Each judge has their own biases and methods that might result in slight deviations in scores, which could make it unfair for someone who gets a tougher judge. The judge effect is a nuisance effect that we do not want to include when we are predicting individual’s scores. We would rather have their scores independent of the judge to truly understand who is best. 

One last example that may be more pertinent to actuaries is the effect of an Emergency Room doctor on hospital visit costs. When somebody goes to the Emergency Room, they do not choose the doctor, but some doctors might approach things differently resulting in different costs. A mixed model with doctor as a random effect would make sense, and then when making predictions for individuals, making predictions without the doctor effect might give better information about how much the event really costs, independent of doctor. In every case, you must evaluate in a business context if the random effect is a nuisance parameter that is getting in the way of the real information we want to obtain or if the random effect is an important effect that needs to be considered in the prediction.  
\[END LINK\]  
Prediction Without the Random Effect

Component Table26

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 6 performs this prediction and plots the results. |

### **1.3.16 Random Slopes Model** {#1.3.16-random-slopes-model}

Models often have an interaction between a factor variable and a continuous variable. A random slopes model allows for such interactions in a mixed model. This type of model contains an interaction between a continuous fixed effect and a random effect. A random slopes model with one fixed and random effect can be written:   
![][image5]   
Both *α*0*i* and *α*1*i* are effects that cluster or group variables based on a random effect. While it is possible to fit a model with only the random effect, it is good practice to include a fixed effect for every variable that is added as a random effect, which is why *β*0 \+ *β*1*Xij* is included in the model. 

For the computer course data that we have been looking at, the only continuous variable is hours. An interaction between professor and hours might represent something such as how good a specific professor's study material is. In this case, the regression model would look like   
![][image6]   
where *professor0i* and *professor1i* represent random effects for the professor variable.  
Random Slopes Model

Component Table27

| Type | Callout |
| :---- | :---- |
| Content | The random slopes model is shown for the grade data in CHUNK 7\. |

### **1.3.17 Random Slopes Model** {#1.3.17-random-slopes-model}

The output for the random slopes model has the following estimates for fixed effects:  
Random Slopes Model  
There are now two random effects. The random effect for *professor* has a variance of 21.03 while the variance for the interaction between *professor* and *hours* is 0.30. These values represent the extra uncertainty that arises for the intercept of the model and the slope for the fixed effect hours respectively due to *professor* being a random effect. 

While the term “random slopes” suggests that the interaction needs to be between a continuous variable and a random effect, an interaction between a random effect and a categorical or binary variable is an appropriate model. For example, another mixed model could be constructed using an interaction between *professor* and *major* instead of or in addition to the random intercept term and the interaction between *Professor* and *hour*s.

| Variable | Year: Sophomore | Year: Junior | Year: Senior | hours | major |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Estimate | 2.33 | \-0.55 | \-6.65 | 1.10 | 4.12 |

### **1.3.18 Exercise 3.3.1** {#1.3.18-exercise-3.3.1}

CHUNK 8 creates a small data frame called emails. There are 5 variables: individual, an indicator for a weekday or weekend, weather, temperature, and number of emails sent. The goal is to build a model to predict the number of emails sent.  
Exercise 3.3.1

Component Table28

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 8 provides space for solutions. |

1. For each variable, determine if it should be a fixed or random effect and justify.  
2. Fit a random intercepts model using emails sent as the target, individual as a random effect, and the other variables as fixed effects.  
3. Fit a random slopes model using an interaction between individual and temperature.

### **1.3.19 Exercise 3.3.1 Solution** {#1.3.19-exercise-3.3.1-solution}

1. There could be many other individuals other than the ones listed, so that is a random effect. Weekend is a binary variable and temperature is continuous, so those should be fixed. Weather is a factor variable but with levels that are all defined and present, so it should also be fixed.  
2. and 3\.

Exercise 3.3.2 Solution

Component Table29

| Type | Callout |
| :---- | :---- |
| Content | The solution model fits are shown in CHUNK 9\. |

### **1.3.20 Repeated Measures and Longitudinal Data** {#1.3.20-repeated-measures-and-longitudinal-data}

Repeated Measures and Longitudinal Data

| Patient | Time (minutes) | Dosage (%) | Response |
| :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | 710 |
| 1 | 10 | 60 | 540 |
| 1 | 20 | 90 | 510 |
| 1 | 30 | 100 | 450 |
| 2 | 0 | 0 | 650 |
| 2 | 10 | 60 | 590 |
| 2 | 20 | 90 | 500 |
| 2 | 30 | 100 | 460 |
| 3 | 0 | 0 | 890 |
| 3 | 10 | 60 | 700 |
| 3 | 20 | 90 | 590 |
| 3 | 30 | 100 | 440 |

Two important types of data that are relevant for mixed models are **repeated measures** and **longitudinal data**. A repeated measures study does exactly as the name implies, measurements are repeated on the same subject and collected. You will then have multiple responses for each individual. 

A longitudinal study is a type of repeated measure where the time of each measurement is specific and recorded. For example, suppose the data is from a clinical trial where doses of medication are released over time. Each patient’s response (some measurable reaction to the drug) is recorded at regular time intervals, perhaps every ten minutes, for a total of 4 measurements. This data might look like:

### **1.3.21 Repeated Measures and Longitudinal Data** {#1.3.21-repeated-measures-and-longitudinal-data}

Repeated Measures and Longitudinal Data

Component Table30

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 10 creates this small data frame and fits these three models. The three models are compared using AIC. |

First of all, *Patient* is a random effect. These three particular patients are a subset of a larger collection of people who are not fully represented in the data. To treat this as repeated measures data, you would ignore the time component. You could model this data using a random intercepts model:   
![][image7]   
where *Patient* is a random effect. The *Time* variable can be added as a fixed effect, and this would still technically be considered a longitudinal model. In this case the model would be:   
![][image8]   
A more powerful model includes an interaction between *Patient* and *Time*, thus creating a longitudinal model where the time effect depends on the patient. Because *Patient* is a random effect, the resulting model is a random slopes model:   
![][image9]

### **1.3.22 Repeated Measures and Longitudinal Data** {#1.3.22-repeated-measures-and-longitudinal-data}

In many repeated measures and longitudinal studies, the object of the study will be a subset of a larger group. This may not be true in laboratory or hard science settings, but in social, financial, clinical, and most other settings this may be the case. One approach that can be used in this type of data is to simply aggregate the data by individual, especially in a repeated measures model. For example, suppose you are testing someone’s eyesight and you give the same test multiple times to an individual. They will have a certain score that is given for each test. One thing that can be done is to take the average of the scores. There is a potential issue with that. For example, what if one individual only had one test while another individual had 10? An average would assume the one data point and the average of 10 data points were interchangeable, whereas treating each result as an individual observation would fix that issue. (Note that using weights in a regression model may handle this problem.) 

The main takeaways from this discussion are that repeated measures data can be modeled using a random intercepts model. Longitudinal data can be modeled using a random slopes model where the random effect has an interaction with the time component.  
Repeated Measures and Longitudinal Data

### **1.3.23 Generalized Linear Mixed Model** {#1.3.23-generalized-linear-mixed-model}

A **generalized linear mixed model** (GLMM) is a generalized linear model with a random effect. This approach combines the GLM structure with the random effect approaches that have been outlined here.  
Generalized Linear Mixed Model

Component Table31

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 11 takes the computer course data and changes the response variable to whether a student received an A or not. |

A standard generalized linear model is then fit using a binomial family with a logit link function (an interaction term for *professor* and *hours* is included to mimic the random slopes model). A second model is then fit with *professor* being a random effect in a random intercepts model and then a third model with random slopes incorporating *hours*.

### **1.3.24 Exercise 3.3.2** {#1.3.24-exercise-3.3.2}

Exercise 3.3.2

Component Table32

| Type | Callout |
| :---- | :---- |
| Content | Return to the emails data set. CHUNK 12 recreates the data frame but where the indicator for weekend or weekday is replaced with a day number. |

These individuals were tracked for 5 days each. 

1. As this is now longitudinal data, create a mixed model that includes an interaction between day and the random effect for individual.  
2. Using a GLMM, fit a new model but with a Poisson distribution for emails sent and a log link function. Compare which model fit is better.

Component Table33

| Type | Callout |
| :---- | :---- |
| Content | The solution for both model fits is in CHUNK 13\. |

### **1.3.25 Bühlmann–Straub Credibility** {#1.3.25-bühlmann–straub-credibility}

Note to candidates: Familiarity with credibility concepts as covered in Exams STAM/FAM/ASTAM is not expected. One of the purposes of this section is to demonstrate that a commonly used credibility result can be obtained via a linear mixed model. 

A credibility estimate is a shrinkage estimator where individual predictions are scaled back toward a global mean. For example, there may be three groups where the means are 3, 5, and 9\. The global mean of all three groups (weighting by exposures) is 6\. A credibility estimate will be a weighted average of the individual mean and the global mean. Individual means based on larger samples will receive more weight relative to the global mean as they are more “credible.” A Bühlmann–Straub credibility estimate is a particular way of using the data to estimate the amount of shrinkage. The derivation is based on using squared error as the loss function and a method of moments approach to deriving the estimators. 

For the Bühlmann–Straub credibility estimate we need multiple groups with measured observations, such as multiple lines of business, the number of exposures for each group for each measurement, and the number or amount of losses. The following data is an example of what is needed for a Bühlmann–Straub credibility estimate.  
Bühlmann–Straub Credibility

|  | Year | Exposure | Losses |
| ----- | ----- | ----- | ----- |
| **Line 1** | 1 | 20 | 4000 |
|  | 2 | 30 | 4500 |
|  | 3 | 40 | 7000 |
| **Line 2** | 1 | 10 | 2000 |
|  | 2 | 5 | 1500 |
|  | 3 | 10 | 2500 |
| **Line 3** | 1 | 100 | 15000 |
|  | 2 | 70 | 13000 |
|  | 3 | 75 | 12000 |

### **1.3.26 Bühlmann–Straub Credibility** {#1.3.26-bühlmann–straub-credibility}

A linear mixed model can be used to provide the Bühlmann–Straub credibility estimate. Bühlmann–Straub credibility uses within group variance and between group variance to determine the weights for the weighted average of the individual and global means. This same between group and within group variance is used to find estimates in a random intercepts model. 

For the purposes of this discussion, we will assume that we are predicting losses, but the principles are universal. The approach for this model will be to fit a model where the target variable is the average loss for each measurement. In the case of the data on the previous page, the average loss is the loss divided by the exposure. The only predictor is the random effect for group, meaning the only fixed effect is the intercept. One key element is that exposures need to be included as weights in the model. Without getting into technical detail, adding weights into the model will scale the variances of each observation. Predictions of the model will then be Bühlmann–Straub estimates for each group.  
Bühlmann–Straub Credibility

Component Table34

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 14 creates the loss data and fits a random intercepts model in such a way to provide the Bühlmann–Straub credibility estimates. |

### **1.3.27 Bühlmann–Straub Credibility** {#1.3.27-bühlmann–straub-credibility}

The Bühlmann–Straub credibility estimates for each line are given in the following table. 

We can back out shrinkage. For Line 2, the observed average loss was 6,000/25 \= 240 while the overall average was estimated as 184.10 (the intercept term from the output). Note that this is not the overall average of 61,500/360 \= 170.83. The estimate is 212.42 \= *Z*(240) \+ (1 – *Z*)(184.10), which implies a credibility factor of *Z* \= 0.507.  
Bühlmann–Straub Credibility  
We can interpret these estimates as the per-exposure loss for each line. For example, suppose in year 4 that there will be 50 exposures for the first line of business. Then the expected losses for that year will be 174.75 times 50, which ends up being 8737.5. 

Another way to provide the Bühlmann–Straub credibility estimate is using empirical Bayes. Using the empirical Bayes formula, the credibility estimate is 175.08 per exposure for line 1 or 8574.00 for the year 4 credibility premium. Formulas for this can be found in Klugman et al, 2018\. This is not exactly the same because both approaches are estimates with differing assumptions made about the nature of the data. However, they are similar in that both attempt the same thing, using between-group and within-group variation to combine the individual mean for each line with the global mean. 

One feature of both approaches is that if the estimates are applied to the existing portfolio, the total claims will match the observed claims. This is shown for the linear mixed model at the end of CHUNK 14\. 

| Line | Credibility Estimate |
| ----- | ----- |
| 1 | 174.75 |
| 2 | 212.42 |
| 3 | 165.15 |

### **1.3.28 Bühlmann–Straub Credibility** {#1.3.28-bühlmann–straub-credibility}

With the mixed model approach to Bühlmann–Straub credibility estimates, another opportunity arises. Combining it with the generalized linear mixed model allows alternative distributions to be used.  
Bühlmann–Straub Credibility

Component Table35

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 15 fits a mixed model to this data and finds a credibility estimate using a gamma distribution for the data and a log link function. |

### **1.3.29 Exercise 3.3.3** {#1.3.29-exercise-3.3.3}

Exercise 3.3.3

Component Table36

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 16 creates a new variable for claim counts on the same group as the losses data. Run a mixed model to find the credibility estimate for the number of claims per exposure for all 3 groups. The solution is in CHUNK 17\. |

## ***1.4 Neural Networks*** {#1.4-neural-networks}

### **1.4.1 Section 3.4 Learning Objective** {#1.4.1-section-3.4-learning-objective}

Neural Networks

Component Table37

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.4 Learning Objective**  Explain, fit, evaluate, and make predictions with neural networks.  |
| Footer | Panel Footer |

### **1.4.2 Introduction** {#1.4.2-introduction}

**Neural networks** (sometimes referred to as artificial neural networks or ANN) are a type of machine learning method loosely based on a simplified model of biological neural networks. They are constructed from networks of artificial neurons (each circle represents a neuron in the diagram shown here). Neural networks can be used in either supervised or unsupervised learning settings, though all the applications considered in this course will be supervised. 

Through an iterative process, neural networks are trained to predict some target variable by approximating the functional relationship between the predictors and the target. Because they can be trained to generate approximations of any continuous function up to some specified level of accuracy, they are very a versatile tool and are sometimes referred to as “universal approximators.”  
Introduction

Basically, as the input data flows through the neural network, the network tries to find more meaningful — for the task at hand — representations of the data. As the data is manipulated through repeated transformations and combinations, however, it tends to lose its interpretability, leading to a lack of transparency as to the relationship between the inputs and outputs; that is, it functions as a bit of a “black box.” 

Neural networks can be applied to both classification (binary or multiclass) and regression problems. Some recent applications of neural networks in the insurance industry include estimating loss reserves for several lines of P\&C insurance by learning from past patterns of claim development for the individual company and the industry for that line (Kuo, 2019), pricing equity-indexed insurance and annuity products with secondary guarantees (Barigou and Delong, 2022), and detecting fraudulent automobile insurance claims (Wang and Xu, 2018).

### **1.4.3 Example** {#1.4.3-example}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_3\_4\_r.rmd\]  
As a motivating example to show the utility of even a small neural network, consider a binary classification problem using artificial data. The goal is to predict whether a job applicant was hired (H \= 1 or 0, respectively) using two continuous predictors: scores on a technical test (T) and a communications test (C). Download the rmd files ( [atpa\_3\_4\_r.rmd](#bookmark=id.gc70hcqlo95o)) and hiring data set ( [hiring.csv](#bookmark=id.sjd5h7uwgdop)).  
\[END LINK\]  
Example

Component Table38

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 1 to load the necessary libraries and load and plot the data. From the plot, we can see that it is not possible to efficiently separate the two regions with horizontal and vertical lines as in tree-based methods, indicating that more sophisticated methods may be required. Run CHUNK 2 to fit a neural network to the data. (The details behind the choices of how to set the various parameter values are explained later.) |

This code also performs classification predictions on the data. For simplicity, we are doing predictions on the same data the model was trained on, rather than the more typical procedure of using training, validation, and testing sets. We see that the network does quite well at classifying this data, misclassifying only 8 points\* out of a total of 250 observations. 

\*Some operating systems, e.g., macOS, may yield slightly different results for the examples in this section.

### **1.4.4 Example** {#1.4.4-example}

For comparison we will fit a classification tree of similar complexity to the same data set.   
Example

Component Table39

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 4 to see how the two models divide up the region with regard to predictions. |

Note that the classification tree performs a bit worse than the neural network, misclassifying 11 observations.

Component Table40

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 3 to fit this model and use it to make predictions on the same data set.  |

The greater flexibility of the neural network should be apparent. While this was a small example, we will see that neural networks are easily scalable to problems with large numbers of predictors and as such are less subject to the curse of dimensionality.

### **1.4.5 Neurons** {#1.4.5-neurons}

The (artificial) neuron is the basic building block of the neural network. Inputs to the neuron are multiplied by weights and summed, after which an additive adjustment called bias is applied to this sum. This adjusted sum is then passed to an activation function to produce the neuron’s output. Mathematically, the output *y* from a neuron is defined by   
![][image10]   
where *x*1,...,*xk* are the inputs, *w*1,...,*wk*are the respective weights, *b* is the bias, and *f*() represents the activation function. The bias and weights are parameters to be estimated while the activation function is selected by the modeler.  
Neurons

The following diagram illustrates the working of a single neuron with 3 inputs. 

The choice of activation function depends on the type of problem being investigated, the desired inputs and outputs to the neuron, and the location of the neuron within the network. Some common activation functions and their uses are discussed later.

### **1.4.6 Layers** {#1.4.6-layers}

In a neural network, neurons are arranged in **layers**, with the neurons operating in parallel within each layer. A typical neural network architecture will consist of an input layer (which simply passes the data to the rest of the network), one or more hidden layers, and an output layer. The outputs of one layer serve as the inputs to the next layer. The number of neurons in the input and output layers correspond to the number of inputs and outputs to the model, respectively. Networks with more than one hidden layer (or two hidden layers – the nomenclature isn’t universally agreed upon) are sometimes called **deep** neural networks. (This is the same meaning of “deep” as is used in “deep learning.”) 

The following diagram shows a neural network (in particular, a “feedforward” network, which is discussed later) with 8 inputs, 3 outputs, and a single hidden layer of 10 neurons.  
Layers  
A **dense** (or **fully connected**) **layer** is a layer in which all of its neurons receive inputs from each neuron in the previous layer, as in the layers of the above neural network; dense layers are frequently used in neural networks and are the default for many neural network implementations.

### **1.4.7 Overview of the Neural Network Modeling Process** {#1.4.7-overview-of-the-neural-network-modeling-process}

There are several steps in the process of designing, training, implementing, and evaluating a neural network; each of these steps requires choices to be made by the modeler. We cover some of the more commonly used choices, as well as the most important considerations regarding these decisions. The process generally involves the following steps (assuming any steps related to cleaning, imputing, or otherwise preparing the data have already been done): 

1. Determine the general type of neural network to be used, which will be informed by the type of problem being solved.  
2. Decide on a method (optimization algorithm) to train the chosen neural network to find the best set of parameter values (weights and biases). Adjust any optimizer settings as needed.  
3. Set the model hyperparameters for the network, which are the number of hidden layers, the number of neurons in each layer, and the activation function to be used.  
4. Train (fit) the neural network and check for under- or overfitting.  
5. Determine a good set of hyperparameters by repeating steps 3 and 4 for various configurations.

Overview of the Neural Network Modeling Process

### **1.4.8 Types of Neural Network Architecture: Feedforward** {#1.4.8-types-of-neural-network-architecture:-feedforward}

The **architecture** of a neural network describes its general structure, the layout of its layers of neurons, and how they are connected to each other. The choice of architecture for a neural network largely depends on the application, as some types of architectures lend themselves more readily to solving specific types of problems. 

A **feedforward neural network** (sometimes referred to as a multilayer perceptron\* or MLP) passes information through the network in one direction only: from the input layer through the hidden layer(s) to the output layer. There are no loops in the design, so that outputs from later layers in the network do not impact previous layers. The neural network used in the previous classification problem is an example of this type of architecture.   
Types of Neural Network Architecture: Feedforward  
\[BEGIN LINK \-https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon\]  
\*The term “perceptron” dates back to the earliest precursors of neural networks. If you are interested, you can read more about the history of the [perceptron](#bookmark=id.wyr2qp1apef1) specifically and the [neural network](#bookmark=id.usqrd7bm10mf) in general. These readings are optional.  
\[END LINK\]

### **1.4.9 Types of Neural Network Architecture: Feedforward** {#1.4.9-types-of-neural-network-architecture:-feedforward}

Feedforward networks are useful in situations involving data that is not sequential or temporally dependent. While they represent the simplest type of neural network architecture, they are nonetheless very powerful at performing many types of regression and classification tasks. In fact, it has been shown (Cybenko, 1989; Hornik, 1991\) that a neural network with a single hidden layer with a sufficient number of neurons can approximate any continuous function (such as a functional relationship between the predictors and target) to an arbitrary degree of accuracy. Recall that the neural network in the first example of this section was very simple, having only a single hidden layer of two neurons, yet nonetheless demonstrated impressive performance (especially in terms of its flexibility) in a binary classification task. 

Examples of the applications of feedforward neural networks with a single hidden layer in the insurance industry date back at least to the 1990s and continue today (Shapiro, 2011). They include problems in wide-ranging areas, such as predicting the propensity of an insurer’s insolvency (Brockett et al., 1994), estimating solvency requirements (Hejazi and Jackson, 2017), and modeling customer loyalty (Ansari and Riasi, 2016). 

Feedforward networks with only one or two hidden layers are sufficient for all of the neural network problems in this course. There are many applications, however (such as tasks involving language processing and image recognition, for example) for which feedforward networks are inadequate, and more complex architectures are needed.  
Types of Neural Network Architecture: Feedforward

### **1.4.10 Beyond Feedforward** {#1.4.10-beyond-feedforward}

Beyond Feedforward

Component Table41

| Type | Tabset |
| :---- | :---- |
| Tabs | 3 |
| Tab 1 Title | Recurrent Neural Networks |
| Tab 1 Content | Recurrent neural networks (RNNs) introduce loops into the architecture by feeding information from neurons back to themselves or to neurons in layers occurring earlier in the network. This feature allows the network to have a sort of “memory” whereby the current “state” of the network can be saved and updated. RNNs are often used in problems involving time series data or sequential data, where the order of the data is important; some common applications include natural language processing and [speech recognition](#bookmark=id.ggtu7aesl78j), where the context of knowing earlier words in a sequence can help to predict or recognize words occurring later in the same sequence. |
| Tab 2 Title | Convolutional Neural Networks |
| Tab 2 Content | Convolutional neural networks (CNNs or ConvNets) are used widely in image recognition and processing tasks, such as tagging photographs and recognizing handwriting. They excel at high-dimensional problems and those involving data with clusters of correlated inputs, such as recognition of abstract concepts in images. Typically, a convolutional layer applies a “filter” successively to all parts of the image before passing the data on to a “pooling” layer, which reduces the dimensionality of the data. This structure may be repeated before ultimately passing the data to an output layer. [GoogLeNet](#bookmark=id.rf147ex2609y) is an example of such a CNN that was constructed to perform image classification, based on supervised training. |
| Tab 3 Title | Generative Adversarial Networks |
| Tab 3 Content | Generative adversarial networks (GANs) are a relatively new type of neural network design (Goodfellow et al., 2014\) that consists of two component networks, a generator and a discriminator. In a classification task for example, the discriminator learns to classify inputs from an initial training set. Then the two components “compete” in a sort of game whereby the generator tries to generate inputs designed to “trick” the discriminator into incorrectly classifying them. Both networks learn from the process and get increasingly skilled at creating realistic but fake inputs (in the case of the generator) or separating artificial data from real data (in the case of the discriminator). GANs have been trained to, among other things, generate very realistic photos of [fake people](#bookmark=id.x4wfk1wfvci3) (Karras et al., 2021). |

There are several types of more complex neural network architectures that are especially helpful in solving specific classes of problems. See the tabs for details and examples; any material referenced in the links in these tabs is optional

### **1.4.11 Activation Functions** {#1.4.11-activation-functions}

Several different activation functions are commonly used in neural network applications; they can introduce non-linearity into a neuron’s output. Typically, all neurons in a given layer will use the same activation function. The choice of activation function will depend on several factors, including the type of problem (classification vs regression) and the location of the neuron’s layer within the network. Some of the more frequently used activation functions are: 

1. Rectified Linear Unit (ReLU)  
2. Sigmoid  
3. Hyperbolic Tangent  
4. Softmax

We will next define each of these functions and give some of their advantages, disadvantages, and common uses. In each activation function equation *f*( *z*), z is the linear combination of the neuron’s inputs, weights, and bias, that is:   
![][image11]  
Activation Functions

### **1.4.12 Rectified Linear Unit Activation Function** {#1.4.12-rectified-linear-unit-activation-function}

The **rectified linear unit** (or **ReLU**) is a common choice of activation function for hidden layers, especially for feedforward architectures, and works well in many neural network applications (Glorot et al., 2011). Some advantages of ReLU include its ease of calculation and its infinite range of output (unlike many activations, which have a finite range). Also, in some neural network applications, it can benefit from “sparse activation,” whereby a significant percentage of the neurons will output exactly zero (which neurons will output zero will depend on the values of the parameters in the trained network, especially the biases). 

ReLU activation function:   
![][image12]   
Rectified Linear Unit Activation Function

### **1.4.13 Sigmoid Activation Function** {#1.4.13-sigmoid-activation-function}

The **sigmoid** (or **logistic**) activation function is commonly used in situations where the output is interpreted as a probability, as its range is (0, 1). One such circumstance is the output layer of a neural network performing binary classification, in which the output is the probability of belonging to one class. While it is a popular way to introduce non-linearity into the network and has an intuitive interpretation, it sometimes has worse convergence properties than ReLU when used in hidden layers, especially in deep neural networks. In particular, the sigmoid curve becomes very flat on both sides as its input moves further from zero, with derivative values that are small in magnitude and decay to zero. This can hamper the training of the network in optimization algorithms that use the derivative to update the weights and is sometimes known as the “vanishing gradient” problem. 

Sigmoid activation function:   
![][image13]  
Sigmoid Activation Function

### **1.4.14 Hyperbolic Tangent Activation Function** {#1.4.14-hyperbolic-tangent-activation-function}

Hyperbolic Tangent Activation Function

The **hyperbolic tangent** (abbreviated **tanh** or **htan**) activation function is similar to the sigmoid activation in shape. Because its range is (-1, 1\) rather than (0, 1), it is generally not used in output layers of classification problems as it lacks interpretability as a probability. 

While the tanh and sigmoid activation functions have the same general shape (see diagram), there are nonetheless some significant differences between them. One property of the hyperbolic tangent function is that its output is symmetric about zero (it is an odd function), unlike the sigmoid activation, whose output is strictly positive. Because this property can be beneficial in the optimization of a neural network (LeCun et al., 2012), the hyperbolic tangent activation function is often preferred to the sigmoid as the activation function for hidden layers. 

Tanh activation function:   
![][image14]

### **1.4.15 Softmax Activation Function** {#1.4.15-softmax-activation-function}

The **softmax** activation function is a generalization of the sigmoid activation function. A layer of neurons using this activation function will have outputs that are each between 0 and 1, and whose values sum to 1\. This property means that it is ideally suited to be used as the activation function in the output layer of neural networks solving multiclass classification problems, in which the outputs are interpreted as the predicted probabilities of belonging to the various classes. 

For layer with *k* neurons, the output from neuron *j* is:   
![][image15]  
where each *zi* is a linear combination of its inputs, weights, and bias. Thus, the output from a neuron using this activation function can be interpreted as having an exponential activation function, scaled by the output of all neurons in the layer (which are using the same activation function).  
Softmax Activation Function

### **1.4.16 Training the Neural Network: Loss Functions** {#1.4.16-training-the-neural-network:-loss-functions}

Training the neural network consists of finding a good set of weights and biases for the neurons in the network. To determine how well a particular set of weights and biases is doing, a **loss function** is used to measure the error between the prediction and the response variable, which is often called a **target variable** in this context. The further the distance between the predictions and the targets, the greater the adjustments to be made to the weights and biases in the network. The appropriate loss function will depend on the type of problem being solved (classification vs. regression), desired sensitivity to outliers, as well as the relative costs of different errors.  
Training the Neural Network: Loss Functions

### **1.4.17 Cross Entropy Loss Function: Binary Classification** {#1.4.17-cross-entropy-loss-function:-binary-classification}

In classification settings, the **cross entropy** (or **log**) loss function is most often used. First consider a binary classification situation, in which the target variable *Y* can take the values 0 and 1\. For a given observation *i*, let *pi* be the probability predicted by the neural network that *Y* \= 1. Further, denote the actual value of *Y* for this observation by *yi*. Then the cross entropy loss for this observation is calculated as   
![][image16]   
This expression is identical to the negative loglikelihood for a Bernoulli random variable, so that minimizing this loss function is equivalent to maximizing the Bernoulli likelihood. 

Note that this cross entropy loss differs from plain entropy as used in decision trees. In that setting, there is only one probability distribution to evaluate, the proportions of zeros and ones at a node. Cross entropy compares two distributions. One is the observed distribution, which places probability 1 at *yi*. The other is the modeled distribution, which places probability *pi* at 1\. 

For example, suppose that *yi* \= 1 for a given observation. If the network predicts *pi* \= 0.7, the loss is 0.357, whereas if the network predicts *pi* \= 0.9, the loss associated with this observation is only 0.105. Thus, while both predictions are more consistent with a value of *yi* \= 1 than *yi* \= 0, the former prediction is much less confident in its prediction than the latter and leads to a greater loss under this loss function.  
Cross Entropy Loss Function: Binary Classification

### **1.4.18 Cross Entropy Loss Function: Binary Classification** {#1.4.18-cross-entropy-loss-function:-binary-classification}

The diagram on the right shows the loss as a function of the predicted probability *pi* for the cases when the true values are 0 and 1 (solid black line and dashed red line, respectively). The loss *Li* can be seen to be especially severe when the predicted probability is particularly incompatible with the actual value. 

For a small predicted probability of *Y* \= 1, say 0.1, the loss will be small in the many cases where the actual value is 0, but very large in the relatively few cases where it is 1\. Thus, these losses tend to balance each other in order to converge on the correct actual probability. 

Finally, the overall loss for the data set—for all loss functions considered here—is calculated as the mean of the losses associated with each observation.  
Cross Entropy Loss Function: Binary Classification

### **1.4.19 Cross Entropy Loss Function: Multiclass Classification** {#1.4.19-cross-entropy-loss-function:-multiclass-classification}

Cross entropy can be generalized to multiclass classification problems. For an output *Y* with *M* possible classes, the cross entropy loss for an individual observation *i* is calculated as   
![][image17]   
where ![][image1]if the observation belongs to class *c* and 0 otherwise and ![][image1]is the predicted probability of this observation belonging to class *c*. Note that only one term in the sum (the one corresponding to the correct class of the observation) will be non-zero. 

This expression is identical to the negative loglikelihood for a multinomial random variable, so that minimizing this loss function is equivalent to maximizing the multinomial likelihood.  
Cross Entropy Loss Function: Multiclass Classification

### **1.4.20 Hinge Loss Function for Classification** {#1.4.20-hinge-loss-function-for-classification}

While cross entropy is the most popular loss function for classification problems, other loss functions are possible. For example, the **hinge** loss function can be used in a neural network for binary classification problems. It is assumed that the target can take the values 1 or –1 (or can be recoded as such). The hinge loss is defined in this case for observation *i* as   
![][image18]   
Where *yi* is the actual class of the observation (–1 or 1\) and *pi* is the prediction for the observation; this prediction is not bound to the range (–1, 1\) and can be any real number. Then, if the actual observation is 1, any prediction greater than 1 incurs no loss at all, while predictions less than 1 are assigned a loss proportional to their distance from 1\. The situation is symmetric for an observation of –1. 

The hinge loss is also used in support vector machines, and seeks to maximize the distance between the decision boundary and the data. It can sometimes result in higher accuracy of classifications than using the log loss, but the predictions from the hinge loss are not interpretable as probabilities. There are multiple generalizations of the hinge loss function to the multiclass classification context.  
Hinge Loss Function for Classification

### **1.4.21 Loss Functions for Regression Problems** {#1.4.21-loss-functions-for-regression-problems}

For regression problems, the most common choice of loss function is **MSE** ( **mean squared error**), and this is the default loss function in many neural network implementations. It is calculated as   
![][image19] where ![][image20] and ![][image21] represent the actual and predicted values of the target variable for observation *i* .   
Another possibility is **MAE** ( **mean absolute error** ), which is calculated as  
![][image22]  
One major distinction between these two loss functions is that MSE is much more sensitive to outliers than is MAE. A loss function that incorporates properties of both MSE and MAE is the **Huber** loss function. Within some defined threshold , the loss is quadratic, while the loss becomes linear outside this threshold. Thus, the Huber loss for observation *i* is   
![][image23]  
Like MAE, the Huber loss function is robust to outliers. MAE, however, has the disadvantage of not being differentiable at zero, which can sometimes hinder convergence in the training of the network. The Huber loss function is smooth everywhere so it avoids these convergence issues. The obvious disadvantage of this loss function is its complexity, both in terms of its form and also requiring an additional hyperparameter to be estimated or chosen.  
Loss Functions for Regression Problems

### **1.4.22 Training the Neural Network: Optimization Algorithms** {#1.4.22-training-the-neural-network:-optimization-algorithms}

The other crucial component in training a neural network is the method used to find the best sets of weights and biases for the neurons in the network, called the **optimization algorithm**. The first step is usually to split the data into training, validation, and testing sets. Then the optimization algorithm works iteratively by adjusting the parameters (weights and biases), based on the calculated loss on the training set. 

To minimize the loss, most commonly used algorithms employ some sort of **gradient descent**, whereby the partial derivative of the loss with respect to each weight and bias is calculated based on the training data, and these weights and biases are then adjusted to cause the steepest “descent” down the loss curve. How far down the curve is controlled by a parameter called the **learning rate**. The process is repeated with the updated set of parameters, and continues until the algorithm finds a minimum (hopefully a global minimum, though sometimes the algorithm can get stuck in a local minimum), or some stopping criterion is satisfied. 

The gradient (set of partial derivatives) is typically calculated according to some type of **backpropagation** algorithm. These algorithms can efficiently calculate the gradient using just two passes through the network. After calculating the outputs from the neurons in a “forward” pass through the network, it will then calculate the derivatives using a “backward” pass through the network, making use of repeated applications of the chain rule.  
Training the Neural Network: Optimization Algorithms

### **1.4.23 Types of Gradient Descent Algorithms** {#1.4.23-types-of-gradient-descent-algorithms}

In the most straightforward version of gradient descent (sometimes called **batch gradient descent**), the entire training set is used to estimate the gradient (by averaging the gradients of the loss for the individual observations), the parameters are adjusted accordingly, and the process is repeated. It is usually possible, however, to reasonably estimate the gradient using only a relatively small sample taken from the training set, called a **mini-batch**. 

In **mini-batch gradient descent**, the gradient is estimated for each mini-batch, and the parameters are updated accordingly before repeating the process on the next mini-batch. This method updates the parameters more frequently, so that fewer passes through the data are required to get good estimates, at the cost of increased computational time and randomness in the training process. This trade-off can be controlled via the size of the mini-batch. One extreme is the batch gradient descent algorithm descried above, which sets the size of the mini-batch equal to the size of the training set; the other extreme is to treat each observation as its own mini-batch, which is referred to as **stochastic gradient descent** or **SGD**. (Though the terminology is not always consistent, and SGD is sometimes used to refer to any gradient descent algorithm not using the full training set for each update.) Pros and cons of these variations on the gradient descent algorithm are discussed later. 

In the training process, each **epoch** consists of one pass through the entirety of the training set, which may entail only one update of the parameters, or many such updates, depending on which variation of the algorithm is used. Periodically, typically after each epoch, the loss is calculated on the validation set, to measure how well the network is predicting data it has not used in training. (The validation loss results are not used to update the network’s parameters.)  
Types of Gradient Descent Algorithms

### **1.4.24 Generalizations of Gradient Descent Algorithms** {#1.4.24-generalizations-of-gradient-descent-algorithms}

One limitation of the gradient descent algorithms described thus far is that a single static learning rate parameter is applied to all of the partial derivatives in all epochs of the training, which can be overly constraining. A few ideas and generalizations have been proposed to remedy this and are often incorporated in implementations of gradient descent algorithms. 

A **momentum** parameter can be added that serves to incorporate the pattern of recent gradient updates into the learning rate. The main idea is that if the gradient keeps the same sign for many iterations, we can increase the learning rate with little fear of overshooting the minimum. On the other hand, a gradient that changes sign each iteration indicates that we are bouncing back and forth on opposite sides of a minimum, and a smaller learning rate would be preferable. 

Several other ideas have been proposed to improve gradient descent algorithms, such as having separate learning rates for the different parameters in the network. While these variations of gradient descent can often result in significant performance gains, their increased complexity can make the resulting model more difficult and time-consuming to train, because there are more parameters whose values must be tuned or estimated.  
Generalizations of Gradient Descent Algorithms

### **1.4.25 Example: Binary Classification** {#1.4.25-example:-binary-classification}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/hotel\_booking\_small.csv\]  
As an example of a binary classification problem, we will use a subset of the hotel booking data set, which can be downloaded here ( [hotel\_bookings\_small.csv](#bookmark=id.j4q4utd85l9i)). For this example, the task is to predict whether the hotel booking was canceled; the *is\_canceled* variable is our target and takes values of 0 and 1\. 

First, we will use several quantitative variables as our inputs, such as how far in advance the booking was made, how many guests were booked, etc.  
\[END LINK\]  
Example: Binary Classification

Component Table42

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 5 to read and prepare the data, split it (using a 80/10/10 train/validate/test split of the data, noting that validation is done within the function), and then fit a neural network on the training data. |

See the comments regarding the various parameters selected. It should take about one minute to run. If your computer is taking considerably longer, consider changing the learn.rates parameter to a larger value. 

The neuralnetwork() function gives output describing the structure of the network. In particular, this neural network has 12 inputs, a single hidden layer of 15 neurons (using the ReLU activation) and 2 outputs. We use a log loss function for this classification task, a mini-batch gradient descent (“sgd”) with momentum, with mini-batches of size 32 and a learning rate of 0.001. (Other than the learning rate, these are the default parameters for the optimizer.)

### **1.4.26 The ANN2 Package** {#1.4.26-the-ann2-package}

The **ANN2** package is used in this section to fit the neural networks. However, there are many other packages in R that have neural network training functionality, including **nnet**, **neuralnet**, and **keras**. 

Note that the **ANN2** package uses softmax for the output layer for all classification problems, including binary classification. (The user can choose the activation function for the hidden layers.) Thus, the two outputs correspond to the predicted probabilities of the observation falling in each of the two classes. Some other neural network packages performing binary classification have a single output indicating the probability of the observation belonging to one particular class. 

Then the complementary probability is the probability of the observation belonging to the other class and predictions are made on the basis of whether the single output falls above or below some threshold. Usually this threshold is set to 0.5, but if an error in one direction is considered more problematic than an error in the other (i.e., a false negative vs a false positive), the threshold could be adjusted in either direction. 

Note that, in general, the input variables to a neural network may take values on very different scales. Because this can negatively impact the learning and stability of the neural network, it is important to scale or normalize the continuous variables prior to using them to train the network. Some neural network implementations can do this scaling as part of the training procedure. The neuralnetwork() function in the **ANN2** package, for example, has a standardize parameter for this purpose.  
The ANN2 Package

### **1.4.27 Overfitting** {#1.4.27-overfitting}

Notice that while the training loss continues to decrease through the training process, the validation loss reaches its minimum by epoch 200, and then increases thereafter. This is an indication that **overfitting** is present. When a neural network has been overfit, the network has learned features of the data that are specific to the training set rather than general relationships between the inputs and target variable(s). In this case, the network will not perform as well on data it has not been trained on, such as the test data. 

When the validation loss starts increasing, this is a good sign that the training should be stopped. If it is determined after the training that the network has been overfit, it is recommended to retrain it (using a smaller number of epochs) before using it to make predictions. If, on the other hand, the validation loss continues to decrease throughout the training period, it suggests that training the model for a larger number of epochs could be beneficial. (Use the train() function in the **ANN2** package to continue training a neural network.)  
Overfitting

Component Table43

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 6 to produce a plot of the training loss and validation loss by epoch over the course of the training. |

### **1.4.28 Predictions and Comparison to Logistic Regression** {#1.4.28-predictions-and-comparison-to-logistic-regression}

This code also uses the resulting model to make predictions on the same test data set. The resulting confusion matrix shows an accuracy of 71.8% for the logistic regression model and the AUC is 0.782, both slightly worse than that of the neural network.  
Predictions and Comparison to Logistic Regression

Component Table44

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 7 to retrain the model for 200 epochs and make predictions for the test data set. |

The probabilities of belonging to class 0 and class 1 for the first six observations in the test set are shown in the output, and the class with the larger associated probability will be the predicted class for each observation. This code also produces a confusion matrix showing the accuracy of the predictions on the test data, and finally calculates the overall accuracy of the neural network model on the test data. In this case, the model correctly classifies 74.2% of the observations in the test data and has an AUC value of 0.821.

Component Table45

| Type | Callout |
| :---- | :---- |
| Content | Now run CHUNK 8 to fit a logistic regression model to the same data set, namely the combined training and validation data used to train and monitor the neural network model. |

### **1.4.29 One-Hot Encoding** {#1.4.29-one-hot-encoding}

All of the input variables used in this example were quantitative, though this data set also contains some categorical variables that we may want to use. Since the network expects quantitative inputs, we must first transform these categorical variables. The most common and straightforward method for doing this is to use a dummy variable approach, which is often called **one-hot encoding (OHE)**. In this method, for a categorical variable with *k* levels, *k* different binary (0 or 1\) variables are created. For each observation, exactly one of these binary variables will be equal to 1, while the other *k*\-1 are set to 0\. This is only slightly different from how dummy variables are used in, say, regression models, which would use one baseline level and only   
*k*\-1 dummy variables.  
One-Hot Encoding

| Observation | *deposit\_type* |
| :---: | :---: |
| 1 | No Deposit |
| 2 | Refundable |
| 3 | No Deposit |
| 4 | Refundable |
| 5 | No Deposit |
| ⋮ | ⋮ |

| Observation | No Deposit | Refundable | Non Refund |
| :---: | :---: | :---: | :---: |
| 1 | 1 | 0 | 0 |
| 2 | 0 | 1 | 0 |
| 3 | 1 | 0 | 0 |
| 4 | 0 | 1 | 0 |
| 5 | 1 | 0 | 0 |
| ⋮ | ⋮ | ⋮ | ⋮ |

In this data set, the *deposit\_type* variable is categorical variable with three levels: No Deposit, Non Refund, and Refundable. The tables show an excerpt of this variable in its original form (left) as well as after its transformation using one-hot encoding (right).

### **1.4.30 Adding Categorical Variables to Binary Classification** {#1.4.30-adding-categorical-variables-to-binary-classification}

The class.ind() function in the **nnet** package performs OHE on these categorical variables (an alternative function that you have seen previously is dummyVars() from the **caret** package). Also note that while some packages implementing neural networks require the target variable to be quantitative (i.e., for the user to recode them using OHE prior to training the model), the neuralnetwork() function in the **ANN2** package accepts categorical target variables, and internally performs OHE on them prior to fitting the model. 

From the output, we can see that 200 epochs shows signs of overfitting and that the validation error starts to increase at around epoch 30 in this case.  
Adding Categorical Variables to Binary Classification

Component Table46

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 10 to retrain the model for 30 epochs and make predictions on the fitted model. We see that including these two categorical variables slightly improves the accuracy of the predictions on the test data while the AUC is slightly smaller. |

body

Component Table47

| Type | Callout |
| :---- | :---- |
| Content | Now run CHUNK 9, which includes two categorical variables ( *market\_segment* and *deposit\_type*) in addition to the quantitative predictors used in the previous model. |

### **1.4.31 Cross-Validation and Model Hyperparameters** {#1.4.31-cross-validation-and-model-hyperparameters}

Cross-validation can be used to help make some of the decisions regarding model hyperparameters, such as the number of hidden layers, the number of neurons in each layer, and the activation function for the hidden layer(s). There are some general rules and heuristics to help guide each of these decisions or to use as starting points, but ultimately, some degree of experimentation is usually required to find good hyperparameters, with the final decision made using *k*\-fold cross-validation. We briefly discuss each of these in turn. 

Number of Hidden Layers   
For many problems using a feedforward network, a single hidden layer is sufficient, and this is usually a good starting point. When the target is a particularly complex function of the predictors, or the number of inputs and/or outputs is very large, a second hidden layer can sometimes help the network learn these complex relationships, though adding layers also increases the time and difficulty of training the network. 

Number of Neurons per Layer   
A larger number of neurons in the hidden layer(s) adds parameters and complexity to the network model. If there are fewer neurons, the network will be quicker to train, but may lack the flexibility to represent complex relationships in the data, and hence have inferior performance. Too many neurons, on the other hand, will not only require more training time, but can also cause the network to have too many parameters to be accurately inferred by the data. 

While there are no hard and fast rules regarding the optimal number of neurons to use in the hidden layer (or the first hidden layer, if there are two), some guidelines have been made that can at least be used to give a reasonable starting point. One such suggestion is that the number of neurons in the hidden layer should be between 2/3 and 2 times the size of the input later (Heaton, 2015). When there is a second hidden layer, its size usually falls between that of the first hidden layer and the output layer.  
Cross-Validation and Model Hyperparameters

### **1.4.32 Activation Function for Hidden Layer(s)** {#1.4.32-activation-function-for-hidden-layer(s)}

For feedforward networks, ReLU generally gives better performance in the hidden layers than sigmoidal or hyperbolic tangent activation functions, particularly for deep networks, and is often the default choice in neural network implementations. Several studies have compared performance of activation functions in various tasks, such as speech recognition (Zeiler et al., 2013; Maas et al., 2013), image recognition, and text classification (Glorot et al., 2011), and concluded that ReLU tends to provide superior performance. 

The tanh or sigmoid activation functions are superior in some circumstances for some networks using a feedforward architecture, but are more commonly used in other types of neural networks.  
Activation Function for Hidden Layer(s)

Component Table48

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 11 to perform 5-fold cross-validation using the ReLU and sigmoid activation functions to determine which makes more accurate predictions. |

Note the mean validation losses for each. In our simulations the ReLU function performed slightly better. Also note that during training, the **ANN2** package calculates training and validation loss based on the standardized data, so the validation losses seen in training will be on a different scale than those we calculate in cross-validation. 

Since we are doing the cross-validation manually, we set the val.prop parameter to 0\. Note that the output will display training error rather than validation error during the training process.

### **1.4.33 Exercise 3.4.1** {#1.4.33-exercise-3.4.1}

Perform 5-fold cross-validation on the above model using the tanh activation function. Based on the results of the cross-validation for the three activation functions, determine which one results in the best performance for this model.  
Exercise 3.4.1

Component Table49

| Type | Callout |
| :---- | :---- |
| Content | No solution code is provided as this exercise can be done by adjusting CHUNK 11\. A copy of the CHUNK 11 contents has been copied into CHUNK 12 for your use. |

### **1.4.34 Exercise 3.4.2** {#1.4.34-exercise-3.4.2}

Exercise 3.4.2

Component Table50

| Type | Callout |
| :---- | :---- |
| Content | Using the best activation function from the previous exercise, vary the number of neurons in the model, trying at least two different (from CHUNK 11\) numbers of neurons in the hidden layer. |

Also try adding a second hidden layer to the model. (The length of the vector for the hidden.layers parameter will be the number of hidden layers in the network, with the values in the vector specifying the number of neurons in each hidden layer. Thus, to get a network with a single hidden layer of 15 neurons, we use hidden.layers \= 15, and hidden.layers \= c(15, 10\) results in a network with two hidden layers containing 15 and 10 neurons, respectively.) Using 5-fold cross-validation, determine which of the configurations you tried is best.

Component Table51

| Type | Callout |
| :---- | :---- |
| Content | No solution code is provided as this exercise can be done by adjusting CHUNK 11\. A copy of the CHUNK 11 contents has been copied into CHUNK 13 for your use. A possible solution is on the next page. |

### **1.4.35 Exercise 3.4.2: Possible Solution** {#1.4.35-exercise-3.4.2:-possible-solution}

The baseline is one hidden layer with 15 nodes and the tanh activation function, which had a CV performance of 0.438 (lower than that of the ReLU or sigmoid activation functions). The following table shows this and the additional CV results from alternative specifications, all of which used the tanh activation function. 

All of the configurations performed very similarly for this problem, with the network with two hidden layers of 15 neurons each giving slightly better performance than the others.   
Exercise 3.4.2: Possible Solution

| Layers | Nodes | CV performance |
| :---: | :---: | :---: |
| 1 | 15 | 0.438 |
| 1 | 25 | 0.440 |
| 1 | 30 | 0.439 |
| 2 | 15 each | 0.437 |

### **1.4.36 Example: Regression** {#1.4.36-example:-regression}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/auto.csv\]  
The next example predicts a continuous quantitative target, the fuel efficiency (in miles per gallon) of different models of automobile, using various properties of the vehicle, such as its engine size and weight.   
\[END LINK\]  
Example: Regression

Component Table52

| Type | Callout |
| :---- | :---- |
| Content | Download the auto dataset\* ( [auto.csv](#bookmark=id.wa0ik4e1bhka)) and run CHUNK 14 to load the data, briefly examine the variables, and fit a neural network model using a single hidden layer of 5 neurons, using the ReLU activation function. |

Note that the regression parameter is set to TRUE (to indicate regression output rather than classification output, i.e., the final layer uses a linear output rather than softmax) and the loss.typ e parameter is set to “squared” to indicate that we are using the MSE loss function. 

This code also plots the training and validation loss. We can see from the plot that while the training curve continues to decrease (on average, the training loss is noisy because it is calculated for each mini-batch), the validation curve has flattened by epoch 200, indicating that the network has been adequately trained by this point. Previously we have averaged the losses by epoch to better visualize the trends, but the **ANN2** package also includes a plot() method that displays the loss by mini-batch. 

\*Quinlan (1993) Auto MPG data set contributed to UCI Machine Learning Repository \[http://archive.ics.uci.edu/ml\]. Irvine, CA: University of California, School of Information and Computer Science.

### **1.4.37 Effect of Mini-Batch Size on Training** {#1.4.37-effect-of-mini-batch-size-on-training}

To this point, all of the neural networks have been trained using mostly the default optimizer settings (with the exception of the learning rate, which is discussed next), but now we consider the effect of the size of the mini-batch used in training. Smaller values of the mini-batch lead to more efficient training, because the model parameters (weights and biases) are updated after each mini-batch. That is, the network will be trained in fewer epochs. However, each epoch will take longer to complete. The opposite is true for larger mini-batches. 

The previous training was done with the default mini-batch size of 32 observations.  
Effect of Mini-Batch Size on Training

Component Table53

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 15 to retrain the same model using the extreme mini-batch sizes of 1 and 313 (i.e., the entirety of the training data).  |

The plots of the training and validation losses clearly show the trade-off. In the former case (upper), the validation losses quickly approach a minimum, but the model takes much longer to run; we also see quite a bit of variability in the training loss due to using a single observation in each mini-batch. In the latter case (lower), the code runs very quickly, but takes a much larger number of epochs to train the network. In fact, 200 epochs is clearly inadequate here, as the validation loss continues to decrease even toward the end of the training period. (Note that the vertical axes of the plots are on different scales.)

### **1.4.38 Effect of Learning Rate on Training** {#1.4.38-effect-of-learning-rate-on-training}

Effect of Learning Rate on Training

Another optimizer setting we may want to adjust is the learning rate. The learning rate controls the size of the adjustment to the parameters when they are updated during the training process.   
Larger values of the learning rate enable quicker learning, but risk overshooting the minimum. A learning rate that is too large can cause the algorithm to jump over the minimum, and risks failing to converge. Smaller values of this parameter lessen this risk at the cost of taking longer to train the network. A learning rate that is too small will cause slower convergence and is more likely to get stuck in a local minimum. 

While many of the more sophisticated neural network optimization algorithms have learning rates that are adaptive, it is nonetheless sometimes important to choose a reasonable starting learning rate, for the sake of speed of convergence. The **ANN2** package uses a default learning rate of 0.0001 across all hidden layers. (Though we do not do so here, this package allows for the specification of different learning rates across the different hidden layers in a network.)

Component Table54

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 16 to retrain the same model using extreme learning rates of 0.1 and 0.00001 (with the mini-batch size reset to the default value of 32).  |

The plots on the right show the tradeoff, and also the drawbacks of choosing a learning rate that is too large or small. In the upper panel, the large learning rate prevents the algorithm from converging to optimal parameter values, and the resulting validation loss is unstable. In the lower panel, the tiny learning rate causes the algorithm to learn very slowly; more epochs would be needed to complete the training of this network.

### **1.4.39 Exercise 3.4.3** {#1.4.39-exercise-3.4.3}

Use the neural network trained with mini-batches of size 32 and a learning rate of 0.0001 (both default values) to make predictions for the test data. Create a scatter plot of the predicted values against the actual observations. Does the network appear to do a good job of predicting the test values?  
Exercise 3.4.3

Component Table55

| Type | Callout |
| :---- | :---- |
| Content | Are there areas where it seems to do better than others? Space for doing your work is in CHUNK 17 and a solution is in CHUNK 18\. |

### **1.4.40 Multiclass Classification Example** {#1.4.40-multiclass-classification-example}

Next we consider a classification problem involving predicting the risk level (high, mid, or low) of pregnancies, based on the characteristics of the mother, such as age, blood pressure, and heart rate, as well as geographic region code (A, B, C, D, or E).   
Multiclass Classification Example

Component Table56

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 19 to load the maternal risk data\* ( [maternal\_risk.csv](#bookmark=id.hieluym7v8uf)), perform some checks, remove two suspicious observations, and split it into the train/validate and test sets. |

\*Ahmed, Kashem, Rahman, and Khatun (2020) Maternal Health Risk data set contributed to UCI Machine Learning Repository \[http://archive.ics.uci.edu/ml\]. Irvine, CA: University of California, School of Information and Computer Science.

### **1.4.41 Exercise 3.4.4** {#1.4.41-exercise-3.4.4}

Fit a neural network to this data set. Use 5-fold cross-validation to choose the network architecture and activation function. After this is complete, make predictions on the test set and determine the accuracy of the network’s predictions.   
Exercise 3.4.4

Component Table57

| Type | Callout |
| :---- | :---- |
| Content | Space for doing your work is in CHUNK 20 and a solution is in CHUNK 21\. |

### **1.4.42 Prediction With Multiple Classes** {#1.4.42-prediction-with-multiple-classes}

Now suppose that we were particularly concerned about not missing any cases that might actually be high risk. Our neural network provides output that is more granular than the predicted class—namely, the predicted probabilities of falling into each class—and this information can be useful here. Consider two particular observations (31 and 97\) from our test set.  
Prediction With Multiple Classes

Component Table58

| Type | Callout |
| :---- | ----- |
| Content | Run CHUNK 22 to fit a neural network model using ReLU and a single hidden layer of seven neurons and see the predicted probabilities and actual target values for these observations (results shown below).  **Observation High risk Low risk Mid risk Actual** 31 0.015 0.454 0.531 mid risk 97 0.299 0.201 0.499 high risk  |

Both of these observations are predicted to be mid risk, but observation 97 is clearly more likely to be risky than observation 31, and we can see that observation 97 is in fact high risk.

### **1.4.43 Exercise 3.4.5** {#1.4.43-exercise-3.4.5}

Find any observations within the test set that have at least a 25% predicted probability of being high risk, but would be predicted by the model to be low or mid risk. These could be candidate observations to receive extra attention because they may be more likely to be riskier than other cases predicted to be low or mid risk.   
Exercise 3.4.5

Component Table59

| Type | Callout |
| :---- | :---- |
| Content | Space for doing your work is in CHUNK 23 and a solution is in CHUNK 24\. |

### **1.4.44 Neural Network Summary** {#1.4.44-neural-network-summary}

This section discussed artificial neural network models and how they can be used to solve classification and regression problems. Neural networks consist of layers of neurons, namely an input layer, an output layer, and one or more hidden layers. Each neuron calculates an output based on a combination of weights and biases, which are then transformed according to an activation function (common choices of which are the sigmoid, hyperbolic tangent, ReLU, and softmax), before being passed as output to the next layer of neurons. 

The individual weights and biases are the model parameters that are fit (trained) using an optimization algorithm and training data. Many optimization algorithms use some variety of gradient descent and backpropagation in order to update the parameters. A holdout validation set is used to assess the progress of the network training; the training should be stopped when the network begins to learn features specific to the training data set, as opposed to general relationships between the inputs and output(s). A loss function is used to measure the success of the network’s predictions. The log loss function is most commonly used for binary classification, its generalization, cross entropy, is used for multiclass classification, while the MSE, MAE, and Huber loss functions are popular choices for regression problems. 

The number of hidden layers, number of neurons per layer, and activation function are all important hyperparameters of a neural network model. The modeler can use *k*\-fold cross validation to choose among candidate model configurations.  
Neural Network Summary

### **1.4.45 Summary of Neural Network Modeling Procedure** {#1.4.45-summary-of-neural-network-modeling-procedure}

To recap, the general neural network modeling procedure as discussed in this section is summarized here.   
Summary of Neural Network Modeling Procedure

Component Table60

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  Determine the general type of network architecture to be used. For most straightforward problems, a feedforward network is sufficient, but recurrent and convolutional neural networks are useful for more complicated tasks.  Decide on a method (optimization algorithm) to train the chosen neural network to find the best set of parameter values (weights and biases). There are several popular optimization algorithms, and different neural network implementations use different algorithms. In many cases, the package’s default algorithm (and corresponding optimizer settings) is sufficient, though changing optimizer settings can help improve training efficiency and/or speed in some cases.  Set the model hyperparameters for the network, which involve the number of hidden layers, the number of neurons in each layer, and the activation function(s) to be used. A single hidden layer is often sufficient and is a good starting point. There are a few different guidelines regarding the number of neurons per hidden layer, for example, setting the number of neurons to some value between 2/3 the size and double the size of the input layer is a reasonable first choice.  Train (fit) the neural network and check for under- or overfitting. Under- and overfitting can be assessed by monitoring the loss on a holdout validation set as the training progresses. As long as validation loss is decreasing, the model is improving its predictive power; if the validation loss starts to noticeably increase, training should be stopped, as this is a sign of overfitting.  Determine a good set of hyperparameters by repeating steps 3 and 4 for various configurations. Different network configurations and activation functions can be compared by comparing the loss calculated for each configuration using *k*\-fold cross-validation, where k is often chosen to be 5 or 10\.   |
| Footer | Panel Footer |

### **1.4.46 Exercise 3.4.6: Summary Exercise** {#1.4.46-exercise-3.4.6:-summary-exercise}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/abalone.csv\]  
The final neural network exercise predicts the age of an abalone, using various characteristics of the mollusk as predictors. Download the abalone data set\* ( [abalone.csv](#bookmark=id.qdrtyhnaiu7t)). Then, do the following.  
\[END LINK\]  
Exercise 3.4.6: Summary Exercise

Component Table61

| Type | Callout |
| :---- | :---- |
| Content | Space for doing your work is in CHUNK 25 and a solution is in CHUNK 26 (this code will take some time to run given the number of cross-validations).  |

1. Randomly split the data into 80/10/10 train/validate/test sets. Fit a neural network model using the MAE loss function. Determine good values of the model hyperparameters (i.e., network architecture and activation function) using 5-fold cross-validation.  
2. Fit a linear regression model to the combined train and validate sets.  
3. Do predictions on the test set using both models and compare the two.

\*Nash, Sellers, Talbot, Cawthorn, and Ford (1994) Abalone data set contributed to UCI Machine Learning Repository \[http://archive.ics.uci.edu/ml\]. Irvine, CA: University of California, School of Information and Computer Science. 

### **1.4.47 Exercise 3.4.6: Possible Solution** {#1.4.47-exercise-3.4.6:-possible-solution}

Exercise 3.4.6: Possible Solution  
To do the predictions, we fit both a neural network model and a linear model to the data. The neural network model used was a feedforward neural network with a single hidden layer of 7 neurons. All of the layers of the network are densely connected. The sigmoid activation function was used in the neural network model. The network configuration and activation function were determined using 5-fold cross-validation and the MAE loss function. The candidate activation functions were the ReLU, sigmoid, and tanh. The candidate network configurations included networks with a single hidden layer of 7, 12, and 20 neurons, and a network with two hidden layers of 10 neurons each. 

The table at the right shows the CV losses from all configurations tested. The sigmoid activation function tended to yield superior performance in this task, with a single layer of 7 hidden neurons giving the smallest cross-validation error (bolded). 

Holdout validation was used to determine the length of the training period; by visual inspection (see plot on the next page), there is some evidence of minor overfitting. The validation loss starts to increase slightly at about epoch 1,000, so we retrain the chosen model for 1,000 epochs.

| Layers (Nodes)/Activation | ReLU | Sigmoid | Tanh |
| ----- | ----- | ----- | ----- |
| 1 (7) | 1.452 | **1.441** | 1.446 |
| 1 (12) | 1.460 | 1.444 | 1.450 |
| 1 (20) | 1.454 | 1.454 | 1.458 |
| 2 (10, 10\) | 1.460 | 1.442 | 1.460 |

### **1.4.48 Exercise 3.4.6: Possible Solution** {#1.4.48-exercise-3.4.6:-possible-solution}

Exercise 3.4.6: Possible Solution  
The other model used was a standard linear regression model,   
![][image24]  
where ɛ is assumed to have a Normal distribution with mean 0 and an unknown standard deviation (estimated during the fitting procedure). The **β** parameters (including an intercept parameter) were fit using a standard least squares methodology. No attempt at variable selection was made (all available predictors were used), but the results indicated that one or two of the predictors may not have significant relationships with the response variable. 

Accuracy was assessed using a holdout test data set that was unseen to either model during any part of the model fitting and tuning processes. According to the MAE metric, the neural network is a bit more accurate, having an MAE of 1.520 on the predictions of the holdout test set, compared to an MAE of 1.637 in the linear model for the same data set, indicating a slightly lower level of average error for the neural network model. 

It appears to be the case that both models tended to overpredict the youngest ages and underpredict the oldest ones (see plot of predictions). The neural network model seems to do slightly better at the most extreme data points. This likely indicates that the neural network is doing a little bit better job of picking up a non-linear relationship in the data.

## ***1.5 Bayesian Models and Analysis*** {#1.5-bayesian-models-and-analysis}

### **1.5.1 Section 3.5 Learning Objective** {#1.5.1-section-3.5-learning-objective}

Bayesian Models and Analysis

Component Table62

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.5 Learning Objective**  Apply Bayesian techniques to linear models.  |
| Footer | Panel Footer |

### **1.5.2 Introduction** {#1.5.2-introduction}

In classical (or frequentist) statistics, parameters are assumed to be fixed but unknown. Inference and intervals are based on the sampling distribution. For every possible sample of size *n*, how many of them would have summary statistics as extreme or more extreme than the statistic we obtained (a *p*\-value)? 

In Bayesian statistics, the parameters are unknown, and their uncertainty is modeled by assuming they follow a probability distribution. By treating them as a random variable, we can use all the distributional tools we have. By knowing the distribution of the parameter of interest, we can obtain any interval, inference, or estimate as needed.  
Introduction

### **1.5.3 Bayes’ Rule** {#1.5.3-bayes’-rule}

![][image25]

* *Pr*(*Y*|𝛉) is the **likelihood** of 𝛉 (that is, the probability of observing *Y* if the true value of the parameter is 𝛉.  
* *Pr*(𝛉) is the distribution of 𝛉 before accounting for any data. This is the **prior** distribution of 𝛉.  
* *Pr*(*Y*) is the **marginal** probability of the data, or![][image26]  
* *Pr*(𝛉|*Y*) is the updated distribution of 𝛉 after accounting for the data. This is the **posterior** distribution of 𝛉. This is our main interest and will be used for inference and estimation.

Notice that *Pr*(*Y*) does not depend on 𝛉, so we can simplify the process and say that   
![][image27]  
That is, the posterior is proportional to the product of the likelihood and the prior, where the scaling factor is that which makes the posterior distribution sum or integrate to 1\. 

Bayes’ Rule  
Notice that *Pr*(*Y*) does not depend on 𝛉, so we can simplify the process and say that   
![][image27]  
That is, the posterior is proportional to the product of the likelihood and the prior, where the scaling factor is that which makes the posterior distribution sum or integrate to 1\. 

Component Table63

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Bayes’ Rule |
| Content |   ![][image28] |
| Footer | Panel Footer |

Bayesian statistics are based on Bayes’ Rule. As a review, Bayes’ Rule is shown here. 

Generally, we will be building models where we are interested in estimating parameters expressed as random variables, and we will use Bayes’ rule as a foundation to estimate those parameters. Say that you have a parameter vector 𝛉 and observed data *Y*. Note that *Y* could be several observations of a single variable or an entire data set. Then,

### **1.5.4 Example: Poisson–Gamma** {#1.5.4-example:-poisson–gamma}

Example: Poisson–Gamma  
Assume that the variable of interest follows a Poisson distribution with mean *λ*. We obtain a random sample of *n* observations, *Y* \= (*y*1, *y*2, . . . , *yn*). Determining the Bayesian estimate of λ requires specification of a prior distribution on λ. 

Let’s choose gamma(2,4) (interpreting parameters as in the *Loss Models* text). This ensures *λ* is positive, as needed. In practice, this prior distribution will be chosen based on knowledge about the parameter before the data is collected. Then the posterior distribution of *λ* is:   
![][image29]

Then the posterior distribution of λ is:   
![][image30]Bayesian estimate of λ requires definition of a prior distribution on λ.   
![][image31]

### **1.5.5 Example: Poisson–Gamma** {#1.5.5-example:-poisson–gamma}

Focusing on *λ*, this is also a gamma distribution, with parameters   
![][image32] and ![][image33].  
When we have the full posterior distribution, we can calculate any posterior quantity we would like (e.g. mean, variance, quantiles). For this example, we might choose the mean of the posterior distribution (which would be optimal under squared error loss) as the estimate of the unknown Poisson mean. It is   
![][image34]  
As is common in Bayesian analyses, the estimate is a weighted average of the observed sample estimate (the sample mean) and the prior mean (8), with more weight on the sample estimate as the number of observations increases. In the same manner, this is similar to credibility analysis. 

Example: Poisson–Gamma  
Then the posterior distribution of λ is:   
![][image30]Bayesian estimate of λ requires definition of a prior distribution on λ.   
![][image31]

### **1.5.6 Why Bayesian?** {#1.5.6-why-bayesian?}

There was a time (in the 1990s) when the statistics community was divided into two camps, always Bayesian and always Frequentist. That is not the case today. To be a good analyst today, it is important to have both approaches available to use.  
Why Bayesian?

Component Table64

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | When Bayesian Models are Especially Useful |
| Content |  You want a structured way to incorporate prior knowledge. When you don’t have much data, your prior assumptions become even more important. You want a natural way to update your models as more data becomes available. Your model structure is rather complicated, so rather than attempting to fit your model all at once you can fit it iteratively.  |
| Footer | Panel Footer |

Component Table65

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Disadvantages of Bayesian Models |
| Content |  Potentially longer computation time. A closed-form solution rarely exists. Bayesian familiarity is less common than frequentist familiarity, meaning that you may need to explain the basics.  |
| Footer | Panel Footer |

### **1.5.7 Markov Chain Monte Carlo** {#1.5.7-markov-chain-monte-carlo}

When the model has only one or two parameters and the distributions are simple, we can often find an exact analytical form for the posterior distribution, as in the previous example. When this happens, it is said to have a **closed form**, or it is said that the **closed-form solution** is the resulting distribution. In the Poisson-gamma example, the posterior distribution is exactly a gamma distribution. That does not always happen. Most models have many more parameters or have more complicated structures, so we cannot find the exact posterior distribution. In that case, we can estimate the posterior distribution through **Markov chain Monte Carlo (MCMC)**. 

MCMC is a suite of sampling methods that provides random draws from the posterior distribution when the distribution itself in closed form is unavailable. If enough draws are made, a reliable understanding of the posterior distribution can be obtained. Two specific MCMC methods that are commonly used are Gibbs sampling and Metropolis–Hastings. Candidates will not be responsible for a deep understanding of the specific algorithms attached to these methods but knowing what each method does can be helpful when using Bayesian models. Hamiltonian Monte Carlo and No U-Turn Sampling are modifications of Metropolis–Hastings that will be useful to know for the software packages that we will be using.  
Markov Chain Monte Carlo

### **1.5.8 Gibbs Sampler** {#1.5.8-gibbs-sampler}

To solve the problem of multiple parameters, we will start with the Gibbs sampler. The basic idea is that the parameters in each model can be sampled one at a time. In a simple case with two parameters, *α* and *β*, you will draw a value from the posterior distribution for *α* assuming you know the value of *β*. Then you will assume that *α* is equal to the most recently sampled value for and use that to sample *β*. This process repeats, iterating back and forth, drawing one at a time while assuming the other is fixed. 

If we are looking for the posterior distribution of a vector of *p* parameters 𝛉 \= {*θ*1,*θ*2,...,*θp*}, we will estimate it by drawing *k* samples of **θ**. Because it is difficult to draw directly from the joint posterior distribution, we will perform the following step at the right. 

The Gibbs sampler only works if the marginal posterior distribution is available in closed form. Candidates will not be responsible for knowing how to code this process. The software introduced in this section performs this. It will also be rare that you will need to be able to explain Gibbs sampling or these other algorithms when you are using or presenting results of a Bayesian model. It is more important to be able to understand and explain the concepts of prior distributions and how the prior distribution and data combine to make the final estimates. 

Gibbs Sampler

1. Set an initial value of **θ**, say

   ![][image35]

2. Draw another sample of **θ** called **θ** (1) by drawing each individual element of **θ** in succession. You hold all other parameters constant based on the most recent draw (or initial value) for other parameters when you make each draw. Specifically, for

![][image36]draw ![][image37]  
from the **marginal posterior distribution** (the distribution of a single parameter with all other parameters fixed, sometimes also called the full conditional distribution), that is   
![][image38]

3. Repeat step 2 until you have a sufficient number of samples. We will discuss how to determine the number of samples later.

### **1.5.9 Metropolis–Hastings Sampler** {#1.5.9-metropolis–hastings-sampler}

The Gibbs sampler relies on being able to sample one variable at a time directly from the closed-form marginal posterior distribution while holding the others constant. If the marginal posterior distribution does not have a known closed form, the Metropolis–Hastings (M–H) algorithm can be used. 

The Metropolis–Hastings algorithm is a numerical method that also uses recursion, meaning that it produces a sequence of draws and each draw in some way depends on the previous draw. With a Gibbs sampler, the new draws are taken directly from the marginal posterior distribution. In Metropolis–Hastings, a new value is proposed from a separate distribution (called the **proposal distribution**), and it is either accepted or rejected based on how likely that value is to occur in the marginal posterior. After enough accepted draws, future draws can be considered to be from the posterior distribution. The draws which are discarded at the beginning are called **burn in**, or **warmup samples**. Inference and intervals can be calculated based on the remaining draws.  
Metropolis–Hastings Sampler

### **1.5.10 Hamiltonian Monte Carlo** {#1.5.10-hamiltonian-monte-carlo}

\[BEGIN LINK \-https://elevanth.org/blog/2017/11/28/build-a-better-markov-chain/\]  
Metropolis–Hastings used to be the best way to sample from a posterior distribution that you couldn’t directly sample from. But there are a few issues. 

1. The proposal distributions can spend too much time in low posterior probability locations.  
2. The proposal distribution, if not well-tuned, can lead to either too many proposals being accepted (the moves are too small) or too many proposals being rejected (the moves are too large). Both waste computer time and can make inferences suspect.

Hamiltonian Monte Carlo (HMC) improves on M-H by adjusting the proposals by the posterior distribution, leading to better proposals and therefore better inference. 

A fun and helpful visual explanation is available here: [http://elevanth.org/blog/2017/11/28/build-a-better-markov-chain/](#bookmark=id.dgkj923e3kmw)

The No U-turn Sampler (NUTS) improves upon HMC by helping the proposals to remain sufficiently different. We will use Stan to fit our models because it uses NUTS and is available with both R and Python wrappers.  
\[END LINK\]  
Hamiltonian Monte Carlo

### **1.5.11 Stan** {#1.5.11-stan}

\[BEGIN LINK \-https://mc-stan.org/\]  
Stan\* is a platform for statistical modeling and computation. We will focus on full MCMC Bayesian inference using NUTS, but it can also do approximate Bayesian inference and penalized maximum likelihood estimation. 

Stan interfaces with the most popular statistical languages (R, Python, shell, MATLAB, Julia, and Stata) and runs on Mac, Windows and Linux. 

\*Stan Development Team. 2019\. Stan Modeling Language Users Guide and Reference Manual, 2.28. [https://mc-stan.org](#bookmark=id.hlzr27dvlsn4)  
\[END LINK\]  
Stan

### **1.5.12 Install Stan** {#1.5.12-install-stan}

\[BEGIN LINK \-https://mc-stan.org/users/interfaces/\]  
To install Stan, follow the instructions here: [https://mc-stan.org/users/interfaces/](#bookmark=id.j0q0oq82a1we). We will focus on the R code, but other than the installation, Stan is relatively platform and language independent.   
We will use: 

* R 4.1.1  
* RStan 2.21.1  
* RStudio 2021.09.0+351

\[END LINK\]  
Install Stan

### **1.5.13 Manuals** {#1.5.13-manuals}

\[BEGIN LINK \-https://mc-stan.org/docs/2\_28/stan-users-guide/index.html\]  
While we will cover enough for the exam here in this module, the full details of the language and capabilities are available here: [https://mc-stan.org/users/documentation/.](#bookmark=id.u9xw6e8rfxud) Specifically, 

* User’s Guide – [https://mc-stan.org/docs/2\_28/stan-users-guide/index.html](#bookmark=id.j5hnhw7feg5w)  
* Language Reference Manual – [https://mc-stan.org/docs/2\_28/reference-manual/index.html](#bookmark=id.xtpkguvla08p)  
* Language Function Reference – [https://mc-stan.org/docs/2\_28/functions-reference/index.html](#bookmark=id.5n7e5kljs1cr)

\[END LINK\]  
Manuals

### **1.5.14 Basic Syntax** {#1.5.14-basic-syntax}

A Stan model has six program blocks: 

1. Data (required) – Reads in the data  
2. Transformed Data – Preprocessing of the data  
3. Parameters (required) – What are you going to sample?  
4. Transformed Parameters – Preprocessing of the parameters  
5. Model (required) – Define your prior distributions and likelihoods  
6. Generated Quantities – Postprocessing of the results

All of these program blocks either need to be in a separate file (often .stan) or in quotes in an R script. RStudio has nice features for .stan files (syntax highlighting, autocompletion, etc.), so we will always use a separate file.  
Basic Syntax

### **1.5.15 Other Modeling Considerations** {#1.5.15-other-modeling-considerations}

Before we do an example, there are a few things to consider when setting up your MCMC estimation. 

* **Priors** – You will need to choose prior distributions for each of the parameters that you estimate. The choice of prior can greatly impact your results or be relatively unimpactful (when choosing a non-informative prior).  
* **Burn-in samples** – Because the sampler wanders around the posterior distribution, it may move slowly from a poor starting value. The initial draws moving it towards the center of the posterior distribution should be discarded.  
* **Model diagnostics** – One danger of Bayesian models is that rather than throwing an error they will often give an answer, even if that answer is nonsense. There are many ways to assess an MCMC model. We will discuss using multiple chains, viewing trace plots, R-hat, and effective sample sizes.

Other Modeling Considerations

### **1.5.16 Burn-in Samples** {#1.5.16-burn-in-samples}

You do not want your estimated posterior distribution to depend on the starting point of the chain. Recall how Metropolis–Hastings and its variants depends on proposing values based on the previous value. If the starting point is already a good representative draw of the posterior, then there will likely be no issue. But, if the starting point is far away from where most draws from the posterior would be, then the first draws will not be representative of the posterior and subsequent draws would also suffer. It will spend those draws making its way to the higher-density regions. As such, you will want to discard the first draws. These are called the **burn-in**. 

The default in Stan is to discard the first half of the draws. For models that take a very long time for each draw but find good posterior draws shortly into the chain, it may make sense to make that number smaller. You can adjust this by changing the value for the warmup argument. In most cases, there will be no issue with keeping this value at the default.  
Burn-in Samples

### **1.5.17 Model Diagnostics** {#1.5.17-model-diagnostics}

Model Diagnostics

Component Table66

| Type | Tabset |
| :---- | :---- |
| Tabs | 4 |
| Tab 1 Title | Chains |
| Tab 1 Content | MCMC uses many (educated) guesses to explore a (posterior) distribution. Unfortunately, it is not easy to tell if the sampler has fully explored the posterior. One way to test that assumption is to run multiple chains, starting at different locations. If the results are similar between the different chains, then it is more likely that you are exploring the space well. |
| Tab 2 Title | Trace Plots |
| Tab 2 Content | Trace plots graph the parameter draw by the iteration number. Ideally, the trace plot should bounce around the posterior distribution without any apparent autocorrelation. Most posterior distributions are somewhat symmetric, so deviations from symmetry should be scrutinized. We will see examples of both good and poor trace plots in the examples in this section.  |
| Tab 3 Title | R-hat |
| Tab 3 Content | R-hat compares the values from the different chains to see if they agree on their results. The ideal value of R-hat is 1, and Stan suggests not using any sample with an R-hat greater than 1.05.  |
| Tab 4 Title | Effective sample size |
| Tab 4 Content | Depending on how efficiently the sampler generates posterior draws, the (say) 1000 posterior draws may be somewhat autocorrelated and therefore only equivalent to 500 random samples. The effective sample size gives the equivalent number of random samples in the posterior draws. This can help you understand how comfortable you should be with the estimates, as a larger sample provides better estimates. Stan provides both an effective sample size for the bulk of the distribution (Bulk\_ESS) and the tails (Tail\_ESS). The easiest way to increase the effective sample size is to increase the number of draws.  |

### **1.5.18 Example: Poisson–Gamma** {#1.5.18-example:-poisson–gamma}

Example: Poisson–Gamma  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/poisson\_gamma.stan\]  
We will illustrate stan by first analyzing the Poisson-gamma example introduced earlier. At this time download the files [poisson\_gamma.stan](#bookmark=id.ei9m4zd12q5p) and [atpa\_3\_5\_r.rmd](#bookmark=id.xn0w8bscyxjj) The .stan file has the code used to fit the model.  
\[END LINK\]

Component Table67

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  poisson\_gamma.stan data { int\<lower=0\> N; //Number of observations, the length of the data vector y\[N\] int\<lower=0\> y\[N\]; //Poisson data, will be one of the arguments in the lpmf below } parameters { real\<lower=0\> lambda; //Poisson Mean } model { target \+= gamma\_lpdf(lambda | 2,0.25); //Gamma prior (note that Stan’s gamma distribution has a mean of alpha/beta, so this one has a mean of 8 and a variance of 32\) target \+= poisson\_lpmf(y | lambda); //Poisson likelihood } |
| Footer | Panel Footer |

### **1.5.19 Example: Poisson–Gamma** {#1.5.19-example:-poisson–gamma}

Example: Poisson–Gamma

Component Table68

| Type | Callout |
| :---- | :---- |
| Content | The following code uses the .stan file created and fits a Bayesian model. It is also available in CHUNK 1\. Some operating systems, e.g., macOS, may yield slightly different results for the examples in this section. |

Component Table69

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  library(rstan) \#Load the rstan package options(mc.cores \= parallel::detectCores()) \#Use multiple cores when fitting the model rstan\_options(auto\_write \= TRUE) \#Automatically saves a bare version to the hard drive so the program does not need to be recompiled if you change it set.seed(1234) \#Set a seed so the simulated data is unchanged Pois\_data \<- rpois(500, 3\) \#Simulate Poisson(3) data fit \= stan(file \= "poisson\_gamma.stan", data=list(y \= Pois\_data, N \= length(Pois\_data)), iter \= 10000\) \#Fit the stan model by defining the location of the model file, the data to include, and the number of iterations. traceplot(fit) \#Make a traceplot print(fit) \#Print the parameter summary statistics |
| Footer | Panel Footer |

### **1.5.20 Poisson–Gamma Results** {#1.5.20-poisson–gamma-results}

Looking first at the trace plot, we see the draws appear to bounce randomly around the same area with no apparent autocorrelation. We also see that all four chains ended up in about the same place. Those are both good signs. The print(fit) command provides us the following results:  
Poisson–Gamma Results  
The lp\_\_ row has to do with the log density (to see how well the model fits). We will ignore it for this module. 

In the lambda row, we see that the R-hat is equal to 1 and the effective sample size is large.

|  | mean | se\_mean | sd | 2.5% | 25% | 50% | 75% | 97.5% | n\_eff | Rhat |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| lambda | 3.03 | 0.00 | 0.08 | 2.88 | 2.98 | 3.03 | 3.08 | 3.19 | 7320 | 1 |
| lp\_\_ | \-970.39 | 0.01 | 0.71 | \-972.41 | \-970.57 | \-970.11 | \-969.93 | \-969.88 | 9263 | 1 |

### **1.5.21 Poisson–Gamma Results** {#1.5.21-poisson–gamma-results}

The mean of the posterior distribution of lambda is 3.03. Comparing that to the point estimate derived earlier we see the estimates are the same. 

![][image39]

Poisson–Gamma Results

Component Table70

| Type | Callout |
| :---- | :---- |
| Content | Further to the point, we can see that the distribution of the posterior draws is similar to the exact posterior distribution (CHUNK 2). |

### **1.5.22 Prior Sensitivity** {#1.5.22-prior-sensitivity}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/poisson\_gamma.stan\]  
One of the advantages of using a package like Stan is that the posterior distribution is derived for you, so you can adjust your model and try alternatives easily. There is no need to work out any mathematical derivations of posteriors as in the introduction of this section. You only need to be able to define the likelihood and the prior. 

When fitting a Bayesian model, it is important to understand the impact of your prior distribution choices on the results. 

For a somewhat silly example, using a uniform prior from 1 to 2 will converge and give results, albeit after more draws, but looking at the trace plot shows that the lambda draws keep running into the upper bound. One feature of Bayesian analysis is that the posterior distribution cannot assign probability to values outside the domain of the prior distribution. In this example, with the true parameter value being 3, the closest a Bayesian analysis can get is the upper limit of the prior distribution. 

Using a uniform with a broader domain (0 to 100 in the example) provides the results you would expect. You can adjust the comments in the poisson\_gamma.stan file and rerun CHUNKs 1 and 2 to try those two priors.  
\[END LINK\]  
Prior Sensitivity

### **1.5.23 Exercise 3.5.1** {#1.5.23-exercise-3.5.1}

The impact of the prior is reduced as your sample size increases (and increased as your sample size decreases). Change the number of simulated Poisson random variables to 5 and 50 and compare those results to just the prior (essentially a sample size of 0\) and the original sample of 500\.  
Exercise 3.5.1

Component Table71

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 3 provides room for your solution. The solution is discussed on the next page. |

### **1.5.24 Exercise 3.5.1 Solution** {#1.5.24-exercise-3.5.1-solution}

The plot shows the density of the prior and each posterior distribution for the various sample sizes. Notice that between 0 and 10, the prior looks essentially flat. That is because the mean is 8 and the variance is 32\. Compare this to the true posterior distribution with *n* \= 50, where the mean is 2.826 and the variance is 0.056. As the sample size increases, the posterior distribution becomes narrower and more peaked, indicating more certainty about the value of lambda. If we had a more informative prior, its impact would also decrease as the sample size increases, though more slowly.  
Exercise 3.5.1 Solution

Component Table72

| Type | Callout |
| :---- | :---- |
| Content | The code for this solution is available in CHUNK 4\.  |

### **1.5.25 Other Software** {#1.5.25-other-software}

Other Software  
\[BEGIN LINK \-https://mcmc-jags.sourceforge.io/\]  
There are many other software packages to do Bayesian analysis. Here are some examples: 

* JAGS – [https://mcmc-jags.sourceforge.io/](#bookmark=id.n1hrr5dmhzfo)  
* PyMC – [https://docs.pymc.io/](#bookmark=id.aramv3hhlrzt)  
* ProcMCMC in SAS  
* MCMCPack in R

You are not required to use Stan or any specific software, so if you are already comfortable in any of these feel free to use them. Stan provides a general way to do any model for this exam, and so it is a good option.  
\[END LINK\]

### **1.5.26 Bayesian Linear Regression** {#1.5.26-bayesian-linear-regression}

Bayesian Linear Regression  
Because much of actuarial work employs linear models, the remainder of this section will focus on linear models and generalized linear models. This is a relatively straightforward application because the set of unknown parameters is well-defined, and it is easy to write the likelihood function. While there are Bayesian versions for decision trees and random forests, they are beyond the scope of this course. 

Bayesian models depend on the likelihood function; therefore, it is important to think of a regression model in these terms. 

The likelihood for the dependent variable *Y* in standard linear regression is normal with mean of   
*intercept* \+ *regressor* *s* \* *explanatory* *variables* and standard deviation of sigma. So,   
![][image40]   
Note that the intercept, *α*, is represented separately. 

Stan also has a normal\_id\_glm function which optimizes the fitting of the regression problem. 

Y \~ normal\_id\_glm(x, alpha, beta, sigma)

### **1.5.27 brms** {#1.5.27-brms}

brms  
A powerful tool that neatly condenses all the information you need for a Bayesian regression model is the **brms** (Bayesian Regression Models using Stan) package in R. The main function in **brms** is brm(), and many of the options are similar to the options found in the lm or glm functions in base R . The options we will focus on are on the right. 

The default prior in brm is an improper flat prior on the regression coefficients. An improper prior is one that does not integrate to one, so is not a proper distribution. The most common improper prior is the uniform prior with infinite domain (either all real numbers or all positive real numbers). Only when the prior is combined with a likelihood do you potentially get a proper posterior distribution. One reason you may want to use an improper uniform prior such as this is that that data will more quickly overwrite the prior. One reason not to use these priors is that you may have good information about the parameter of interest. Using a good proper prior will lead to a better model than using an improper uniform prior. Additionally, in a regression model, you may want to adjust the prior on the coefficients to account for various features like heavy tails or for shrinkage.

Component Table73

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  brm( formula, \#formula written just like in lm “Y \~ X1 \+ X2” data, \#which dataset family \= gaussian(), \#distributional family, gaussian for linear regression, many other options for glms prior \= NULL, \#choice of prior distributions, can be left unspecified inits \= "random", \#set the initial values for the sampler chains \= 4, \#number of chains iter \= 2000, \#number of iterations warmup \= floor(iter/2), \#number of burn-in samples. Discarded for inference. )  |
| Footer | Panel Footer |

### **1.5.28 Example** {#1.5.28-example}

We will start exploring Bayesian regression models using a simple example.  
Example

Component Table74

| Type | Callout |
| :---- | :---- |
| Content | The code to run these examples is found in CHUNK 5\. Note that the compilation step can take some time (maybe even more than the actual model fitting).  |

There are 10 explanatory variables ( *x1*, *x2*, *x3*, …, *x10*) which are each random samples from a Normal(0,1) distribution. The response variable, *y*, is equal to 3 \+ 2\* *x1* \+ 4\* *x2* \+ rnorm(0, 3). The variables *x3* through *x1* *0* are unrelated to the response variable. We will begin by fitting three different models using the brm defaults: 

* fit10 \<- brm(y \~ x1 \+ x2 \+ x3 \+ x4 \+ x5 \+ x6 \+ x7 \+ x8 \+ x9 \+ x10 , data \= data\_mat)  
* fit6 \<- brm(y \~ x1 \+ x2 \+ x3 \+ x4 \+ x5 \+ x6, data \= data\_mat)  
* fit2 \<- brm(y \~ x1 \+ x2, data \= data\_mat)

The last model, fit2, should be preferred. The output shows all estimated coefficient confidence intervals containing the true values.

### **1.5.29 Example: Simple Model Diagnostics** {#1.5.29-example:-simple-model-diagnostics}

Example: Simple Model Diagnostics

Component Table75

| Type | Callout |
| :---- | :---- |
| Content | The package brms provides many different model diagnostics (CHUNK 6). |

We will discuss the plot and conditional\_effects functions. There are many other model diagnostics available in the package documentation. 

**Plot –** When you pass a brmsfit object to the plot function it provides trace plots and posterior densities. Running plot(fit10) shows that all the chains appear to have good mixing (the values are randomly bouncing around and all the chains ended up in the same place). It also shows the posterior densities, and we can see that 0 is a reasonable value for x3 through x10. The figure shows the posterior distributions and trace plots for *x10* and sigma. 

**Conditional Effects –** The function conditional\_effects() provides plots with intervals of the relationships between each predictor and the dependent variable. The figure shows the relationship between *x2* and *y*. 

### **1.5.30 Example: Simple Model Comparison** {#1.5.30-example:-simple-model-comparison}

Example: Simple Model Comparison

Component Table76

| Type | Callout |
| :---- | :---- |
| Content | We now compare the three models using an approximated leave-one-out cross validation using the **loo** package, which is automatically loaded with **rstan**. (CHUNK 7). |

|  | elpd\_diff | se\_diff |
| ----- | :---: | :---: |
| fit2 | 0.0 | 0.0 |
| fit6 | \-2.9 | 1.4 |
| fit10 | \-4.7 | 2.5 |

Depending on your setup, loo() can take some time. Full details of the algorithm are available in these two papers and the brms documentation, which are not required reading: 

* Vehtari, A., Gelman, A., and Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. Statistics and Computing. 27(5), 1413--1432. \\doi:10.1007/s11222-016-9696-4  
* Vehtari, A., Simpson, D., Gelman, A., Yao, Y., and Gabry, J. (2019). Pareto smoothed importance sampling. arXiv:1507.04544.

The elpd is the expected log pointwise predictive density, which is akin to out-of-sample loglikelihood and basically a measure of how well the held-out predictions match the actual observations. Higher values mean that the held-out observation is more accurately predicted. This table provides the elpd\_diff which is the difference between the best model’s elpd and the given model’s elpd. The best model (in our case fit2) will always have an elpd\_diff of 0\. The se\_diff column gives the differences of the standard errors for the estimates of elpd. We see that the true model is best for predicting held-out data (no surprise there). 

The loo function provides some additional checks for outliers and model fit, but we will only focus on the table above.

### **1.5.31 Horseshoe Prior** {#1.5.31-horseshoe-prior}

Horseshoe Prior  
In the example, all of the priors are standard (flat improper priors on the regressors). We would like to set up our prior to allow for some of the coefficient estimates to get close to zero, while allowing the non-zero estimates the flexibility to be what they need to be. We can do that through the Horseshoe prior (Carvalho, C. M., Polson, N. G. and Scott, J. G. (2010). "The horseshoe estimator for sparse signals" *Biometrika* 97 465–480.). 

The Horseshoe prior shrinks small coefficients toward zero (maybe all the way to zero) while allowing non-zero coefficients to be where they need to be. This is like what elastic net regression does for non-Bayesian models but is better in that the non-zero coefficients do not shrink as much.

### **1.5.32 Example: Horseshoe Prior** {#1.5.32-example:-horseshoe-prior}

Example: Horseshoe Prior

Component Table77

| Type | Callout |
| :---- | :---- |
| Content | We fit a fourth model as follows, using CHUNK 8: fit10H \<- brm(y \~ x1 \+ x2 \+ x3 \+ x4 \+ x5 \+ x6 \+ x7 \+ x8 \+ x9 \+ x10 , data \= data\_mat, prior \= set\_prior("horseshoe(3)"), seed \= 1000\) |

| Explanatory Variable | fit10 | fit10H (Horseshoe) |
| ----- | ----- | ----- |
| Intercept | 3.04 | 3.04 |
| x1 | 2.04 | 2.04 |
| x2 | 3.96 | 3.96 |
| x3 | \-0.00 | \-0.00 |
| x4 | \-0.01 | \-0.01 |
| x5 | \-0.03 | \-0.03 |
| x6 | \-0.03 | \-0.02 |
| x7 | 0.03 | 0.02 |
| x8 | 0.03 | 0.02 |
| x9 | \-0.02 | \-0.01 |
| x10 | \-0.04 | \-0.03 |

We can first compare the estimates of fit10 and fit10H  
The non-zero estimates are the same, but for variables *x3* through *x10* the signs are the same, but the estimates are closer to zero and the confidence intervals are tighter around zero (not shown here).

### **1.5.33 Example: Horseshoe Prior** {#1.5.33-example:-horseshoe-prior}

In our example, the Horseshoe prior does a great job reducing the impact of the unrelated predictors.  
Example: Horseshoe Prior

Component Table78

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 9 to perform the cross validation. Alternatively, you could run loo only comparing fit2 and fit10H to speed up computational time. |

Obviously, if you know that a variable is unrelated, it is better to remove it than to use the horseshoe, but in most situations you will not know whether a variable should be included. The horseshoe is a great way to mitigate the impact of the unrelated covariates. If you will continue to collect data for using this model in the future, strict variable selection could be preferred to reduce the amount of data that you will need to collect.  
Model Comparisons: 

|  | elpd\_diff | se\_diff |
| ----- | :---: | :---: |
| fit2 | 0.0 | 0.0 |
| fit6 | \-2.9 | 1.4 |
| fit10H | \-3.4 | 1.9 |
| fit10 | \-4.7 | 2.5 |

### **1.5.34 Predictions** {#1.5.34-predictions}

Predictions

Component Table79

| Type | Callout |
| :---- | :---- |
| Content | As an example, let’s predict the value of the first observation in our data\_mat object using the fit2 model. We use the following command (CHUNK 10): predictions \<- predict(fit2, newdata \= data\_mat\[1,\])  |

One major advantage of the Bayesian model context is the ability to make predictions accounting for parameter uncertainty. In standard linear regression models, you will get a model fit and then will use the estimated coefficients to predict new values. To incorporate some uncertainty, you can calculate prediction intervals. Implicit in the prediction and the intervals is the assumption that the parameter estimates are correct without uncertainty. 

In Bayesian models, we have posterior draws of the parameter estimates and can use each one of those to make a separate prediction. The **brms** package has a predict command that works similarly to the predict command on lm or glm objects.

### **1.5.35 Predictions** {#1.5.35-predictions}

We obtain an estimated value and the 95% interval of the predictions. We can get a similar prediction interval using the following frequentist code (these are similar partially because we are using the default flat priors in brms): 

fit2freq \<- lm(y \~ x1 \+ x2, data \= data\_mat)

predict(fit2freq, newdata \= data\_mat\[1,\], interval \= "predict")

The big difference is that the Bayesian model gives us samples from the posterior predictive distribution. Those can be seen by adding summary=FALSE to the code. If you are using these predictions in a larger model (say the individual predictions are policy-level results and you want to see the possible impacts on your entire book of business) you can simply use each sample as a possible outcome. We see that the frequentist prediction (the vertical line) is in the center of the predictive distribution, but the Bayesian model gives us an entire distribution of potential outcomes.  
Predictions

### **1.5.36 Generalized Linear Models** {#1.5.36-generalized-linear-models}

Generalized Linear Models  
Many of the observations in actuarial science are not normally distributed. Claim counts are discrete and often full of zeros. Severities are typically positive and right skewed. The package **brms** can fit generalized linear models with only small adjustments to the code. 

There are a vast number of distributional families available in **brms**. Full details are available in the package manual. The package also allows the modeler to specify their own distributional family. In addition to standard models available in glm, there are many zero-inflated and hurdle models available.

### **1.5.37 Example: Count Data** {#1.5.37-example:-count-data}

Example: Count Data

Component Table80

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  *IDpol:* The policy ID (used to link with the claims dataset). *ClaimNb*: Number of claims during the exposure period. *Exposure*: The period of exposure for a policy, in years. *VehPower*: The power of the car (ordered values). *VehAge*: The vehicle age, in years. *DrivAge*: The driver age, in years (in France, people can drive a car at 18).BonusMalus: Bonus/malus, between 50 and 350: \<100 means bonus, \>100 means malus in France. Higher values imply higher premiums due to past accidents and violations. *VehBrand*: The car brand (unknown categories). *VehGas*: gas, diesel or regular. *Area*: The density value of the city community where the car driver lives: from "A" for rural area to "F" for urban center. *Density*: The density of inhabitants (number of inhabitants per square-kilometer) of the city where the car driver lives in. *Region*: The policy region in France (based on the 1970-2015 classification).  |
| Footer | Panel Footer |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/fremtpl2freq.csv\]  
The R package **CASdatasets** supports the book *Computational Actuarial Science*. The dataset freMTPL2freq contains information on 677,991 French third-party motor liability policies (observed mostly on one year). If you don't have this package, download the data directly ( [fremtpl2freq.csv](#bookmark=id.49mvhatf1v60)). Note that the file name we are using does not employ upper case letters. The variables included are listed here. 

For our models, we will use *VehAge* and *DrivAge* as predictors of *ClaimNb*. log(Exposure) will be used as an offset to reflect that the expected number of claims is proportional to the exposure period.  
\[END LINK\]

### **1.5.38 Example: Count Data Model Selection** {#1.5.38-example:-count-data-model-selection}

body  
Example: Count Data Model Selection

Component Table81

| Type | Callout |
| :---- | ----- |
| Content | The full code to download and process the data and then fit and evaluate the model as provided in CHUNK 11\. After running the loo function, we find that the zero-inflated negative binomial model seems to fit the best, with the zero-inflated Poisson and the negative binomial slightly behind.   **elpd\_diff se\_diff** ZINB 0.0 0.0 ZIP \-0.3 0.3 NB \-0.6 0.6 P \-1.9 2.3  |

For this example, we will select a subset of 3,000 rows for our analysis (for computational efficiency). We will compare four different models (with their default link functions, which is log in all four cases): 

* Poisson  
* Negative binomial  
* Zero-inflated Poisson  
* Zero-inflated Negative Binomial

(Zero-inflated distributions are called zero-modified in *Loss Models* and are also discussed in *Regression Modeling with Actuarial and Financial Applications*. They take the base distribution and change the assigned probability at zero and then proportionally reduce all the other probabilities so they sum to one.)

### **1.5.39 Example: Count Data Model Selection** {#1.5.39-example:-count-data-model-selection}

body  
Example: Count Data Model Selection  
Looking more closely at the zero-inflated negative binomial model, we see the parameter estimates and can look at when the 95% intervals do not include zero. We see that *VehAge* is a significant predictor and *DrivAge* may be (zero is on the boundary of the interval). This could also be seen through the plot function. We also see that the *Rhat* values and effective samples sizes are good.

|  | Estimate | Est.Error | l-95% CI | u-95% CI | Rhat | Bulk\_ESS | Tail\_ESS |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | \-0.91 | 0.43 | \-1.71 | \-0.04 | 1 | 1648 | 2363 |
| VehAge | \-0.05 | 0.02 | \-0.08 | \-0.02 | 1 | 2469 | 1743 |
| DrivAge | \-0.01 | 0.01 | \-0.02 | 0.00 | 1 | 3052 | 2389 |

### **1.5.40 Example: Count Data Prediction** {#1.5.40-example:-count-data-prediction}

Example: Count Data Prediction

Component Table82

| Type | Callout |
| :---- | :---- |
| Content | Using our chosen zero-inflated negative binomial model, we will predict values for another random sample of 3,000 policies and find the posterior predictive distribution of the total number of claims (CHUNK 12).  |

We can then plot the kernel density estimate, calculate intervals, or simply use the draws in other calculations. We see that the expected number of claims (mean of the posterior predictive distribution) is about 175, but the truth could reasonably be any value between 100 and 250\. This is one of the advantages of Bayesian models more broadly. This is a fully specified predictive distribution accounting for parameter uncertainty and able to easily provide simulated values. 

Note that the original analysis produced 4,000 samples from the posterior distribution. For a given sample (which is a list of possible parameter values), a predicted value is simulated for each of the 3,000 policies and then they are summed. The figure represents the distribution of the 4,000 simulated totals. 

### **1.5.41 Model Evaluation** {#1.5.41-model-evaluation}

Model Evaluation

Component Table83

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 13 to obtain the mean square error of the predictions made on the test set.  |

It is important to be able to compare the predictions of this model with alternative models that might be considered. A reasonable point estimate of a predicted value would be the mean of the predictions based on posterior sample. These estimated predictions can then be used to assess the accuracy of the model, using, for example, mean square error.

### **1.5.42 Exercise 3.5.2** {#1.5.42-exercise-3.5.2}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/freMTPL2fsev.csv\]  
The dataset freMTPL2sev (from CASDatasets or [fremtpl2sev.csv](#bookmark=id.df0xao74bxsj)) has two columns, *IDpol* (used to link to the frequency dataset) and *ClaimAmoun* *t*. Build a Bayesian GLM to estimate the severity, based on the variables in the frequency dataset. Here are some tasks to accomplish: 

1. Join the explanatory variables from the freMTPL2freq dataset with the severity values in fremtpl2sev.  
2. Remove the extremely large values (this is called an ex cat model, a model without the catastrophic values). Remove all observations above 25,000.  
3. Choose a few distributional families, appropriate for estimating severity, to compare.  
4. Take a sample of the data to speed computation. Note that depending on your computing power, these models may take a bit of time to run. We chose to sample 3,000 observations. Also, only use *DrivAge* and *VehAge* as predictors.

\[END LINK\]  
Exercise 3.5.2

Component Table84

| Type | Callout |
| :---- | :---- |
| Content | Space to do your work is in CHUNK 14 and a possible solution is in CHUNK 15\. |

Some questions to answer as you are working through this model. 

1. When combining the two datasets, there are some *IDpol* values in the severity dataset which are the same. Why might that be and how does that impact your join? Are there any other issues after the join?  
2. Should exposure be included in your model? Why or why not? What about *ClaimNb*?  
3. What characteristics should your candidate distributional families have?

### **1.5.43 Exercise 3.5.2 Solution** {#1.5.43-exercise-3.5.2-solution}

This is one possible solution, but there are many reasonable solutions. 

1. Some policies had more than one claim during the period of interest. They will have multiple rows in the severity dataset with their ID number. When joining the two datasets, you need to make sure that you join all records in the severity dataset to records in the frequency dataset. There are also several claims whose *IDpol* is not in the frequency dataset (about 200). We decided to remove those.  
2. Exposure impacts the number of claims but should not impact the size of a given claim. The number of claims also shouldn’t affect the size of an individual claim. Additionally, the number of claims is not known at the beginning of the year.  
3. The severities are positive and right skewed. They will also often have heavy tails. For our analysis we chose to compare the lognormal and gamma distributions.

Exercise 3.5.2 Solution

### **1.5.44 Exercise 3.5.2 Solution Continued** {#1.5.44-exercise-3.5.2-solution-continued}

The gamma model fits significantly better than the lognormal model. Looking at the coefficient estimates in the gamma model, they are mostly insignificant. We will fit both the gamma and the lognormal models without predictors and compare them below. Another option is to use the horseshoe prior.  
Exercise 3.5.2 Solution Continued  
Because all the predictors are essentially insignificant, the best model (given the data we have) is a simple gamma model where everyone is given the same parameters. The two predictors from this data set do a better job of modeling the frequency than the severity.

|  | elpd\_diff | se\_diff |
| ----- | :---: | :---: |
| Gamma (No pred) | 0.0 | 0.0 |
| Gamma | \-2.7 | 1.6 |
| Lognormal (No pred) | \-56.8 | 39.7 |
| Lognormal | \-57.6 | 39.6 |

Component Table85

| Type | Callout |
| :---- | ----- |
| Content | We compared the gamma and lognormal models by fitting them using brm and comparing them using the loo function (CHUNK 15). Our model selection results are shown here.  **elpd\_diff se\_diff** Gamma 0.0 0.0 Lognormal \-54.9 39.7  |

## ***1.6 Stacking*** {#1.6-stacking}

### **1.6.1 Section 3.6 Learning Objective** {#1.6.1-section-3.6-learning-objective}

Stacking

Component Table86

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.6 Learning Objective**  Explain the benefits of and demonstrate the combination of multiple models via stacking.  |
| Footer | Panel Footer |

### **1.6.2 Introduction** {#1.6.2-introduction}

Introduction  
**Stacking** combines the predictions of many different models to make a better overall prediction. The first step is to make out-of-sample predictions (either with cross validation or a validation set) on the training data with at least two different models. These predictions become inputs to a meta model that makes the final predictions. 

The initial models are called **stage-0 models**, **first-layer estimators**, or **basic learners**. These models are fit directly on the training data. Stacking works best when these models are different types, say, a linear model, a neural network, and a tree-based model. Those initial models are then combined using a meta-model, also called a **stage-1 model** or **meta-learner**. Only the predictions from the initial models, or the predictions plus the original variables, can be used as inputs to the meta-model. 

Let’s work through an example using the hotel bookings data first seen in the additive models section. We will predict the average daily rate using the total length of stay, the lead time, the number of adults, and the market segment.

### **1.6.3 Example: Hotel** {#1.6.3-example:-hotel}

Example: Hotel

Component Table87

| Type | Callout |
| :---- | :---- |
| Content | We first read in the data (CHUNK 1). |

Data  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_3\_6\_r.rmd\]  
At this time, download the .Rmd file ( [atpa\_3\_6\_r.rmd](#bookmark=id.t5qgrny5e8i0) ) and the reduced hotel bookings data set ( [hotel\_bookings\_small.csv](#bookmark=id.repqymu145wv)). We will be modeling the average daily rate using three stage-0 models: 

* Linear model with normal errors (LM)  
* Regression tree (RT)  
* Neural network (NN)

\[END LINK\]  
To focus on stacking, we will not spend time checking that the individual models capture important relationships. One benefit of stacking results when the stage-0 models capture different relationships in the data. Hence, the stage-0 models should both fit well and work together to predict better than any one model could do on its own. There is no requirement that the stage-0 models all use the same predictor variables. (For example, a linear model may work best with continuous predictors while a tree model may work best with categorical predictors.) Selecting these models will likely require splitting the data to do variable selection and hyperparameter tuning. After settling on the stage-0 model forms, the data should be repartitioned for building the stacked model. 

Because the neural network requires one-hot encoding, we perform the encoding on the market segment variable for use with that model. We divide the dataset into six parts, one holdout and five folds for use with building the stage-0 predctions.

### **1.6.4 Stage-0 Models** {#1.6.4-stage-0-models}

Stage-0 Models  
Because we are predicting a continuous variable, make sure that method=”anova” is used when fitting the tree. On the neural net, make sure not to use the log loss, as that only works in classification problems. Note that while there is a validation set in the neural net setup to look for overfitting within the folds, we will stick with the original number of epochs. 

A few words are in order regarding the use of folds here. This is not cross validation because no validation is being done at this step. As always, when constructing a model it must be done with a view toward applying that model on future, unseen, data. Thus, to obtain values to feed into the stage-1 model, each stage-0 model should be fit to one subset of the data and then predictions made on the remaining training data. Fitting to the full training set and then making predictions on that same set will lead to inputs to the stage-1 model that are likely far more accurate predictors than will occur when the model is deployed.

Component Table88

| Type | Callout |
| :---- | :---- |
| Content | Holding out each fold, we fit the models and then predict the held-out fold (CHUNK 2). |

### **1.6.5 Meta-models** {#1.6.5-meta-models}

Meta-models  
Using the original variables with the stage-0 model predictions can potentially lead to overfitting, because the predictors are already somewhat included in the stage-0 model predictions. Note from the output that meta2 leads to a significant change in the coefficient for the predictor based on the stage-0 linear model. This may be because a linear model is essentially being used twice. 

The meta-models are still models so we can use all of the techniques we have learned to make them better. We use a linear model for the meta-model, but you can use any model family you like. Additionally, you can perform variable selection or any other reasonable feature engineering. Note that in this case, all the predictors in the meta model (treating *market\_segment* as a single variable) are significant. There is a lot of room for creativity in these structures.

Component Table89

| Type | Callout |
| :---- | :---- |
| Content | We fit two meta-models (CHUNK 3), one with only the stage-0 model predictions (meta1) and the other with both the stage-0 predictions and the original predictors (meta2). |

### **1.6.6 Model Comparison** {#1.6.6-model-comparison}

Model Comparison  
When using a stacked model for predictions on future data, there is an additional step needed. In this example, we have five different models built using each of the stage-0 model types (a different set of estimated model parameters for each hold-out fold). When using these models on future data we need to apply a single model. This is accomplished by returning to the training set and refitting the stage-0 models on the entire set. The stage-1 model is NOT refit using these new predictors. As noted previously, doing so would lead to overfitting. 

We also include a null model (simply the mean *adr* from the training set) for comparison. We find the following results.

Component Table90

| Type | Callout |
| :---- | :---- |
| Content | We compare the models using test set root mean square prediction error (CHUNK 4). |

| Model | Null | LM | RT | NN | Meta1 | Meta2 |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: |
| RMSE | 51.16 | 45.92 | 45.63 | 44.87 | 44.74 | 44.77 |

The Meta2 model seems to slightly overfit, performing about the same as the neural network. Meta1 (the meta-model with only the initial model predictions) outperforms the individual models. Keep in mind that we didn’t go through the full model-building exercise here and so this example should not be taken as evidence that stacked models provide limited improvement.

### **1.6.7 Other Stacking Details** {#1.6.7-other-stacking-details}

Other Stacking Details  
Stacking is like other ensemble methods such as bagging and boosting. **Bagging** takes similar initial models and combines their estimates using a meta-model (which can be as simple as an average). **Boosting** uses similar initial models and fits subsequent models on the residuals of the previous models. Stacking can involve both but also allows you to combine predictions from different model types. 

**Blending** is sometimes used to describe stacking using a hold-out set instead of repeated use of hold-out folds. The term is not as well-defined (it has been used in other contexts) as stacking. While computationally more efficient, blending does not make full use of the available data. 

You can combine your initial model predictions with multiple meta-models and then use another meta-model to combine the meta-model predictions. This is called **multi-level stacking.** Particular care must be applied when doing multi-level stacking to avoid overfitting to a particular partition of train and test data. While stacking can provide predictive improvement, it comes at a cost in increased complexity and reduced model explainability.

Component Table91

| Type | Callout |
| :---- | :---- |
| Content | When using a relatively simple meta-model, the model summary (repeated in CHUNK 5\) can show which of the stage-0 models had the most impact. In our hotel example, all three models were significant contributors to the meta-model.  |

The second model (meta2) did not perform as well). Many of the predictors are significant, but the LM predictions have a negative coefficient. It appears that the linear meta model with the predictors and the linear stage-0 model are cancelling each other out (or making both difficult to identify). 

It is more important for the stage-0 models to be different than individually accurate, so that together they can make a stronger model.   
There is software for automatic stacking (like the R package **stacks**), but because manual implementation is relatively simple, we recommend that you code the stacking by hand to give access to any package you would like for the initial and meta models.

### **1.6.8 Exercise 3.6.1** {#1.6.8-exercise-3.6.1}

Using the hotel data, predict whether a booking will be cancelled ( *is\_cancele*d) using the following predictors: 

* Average daily rate (*adr*)  
* Total stay length (*total\_stay*)  
* Lead time (*lead\_time*)  
* Number of adults (*adults*)  
* Market\_segment (*market\_segment*) \- which has been one hot encoded

Exercise 3.6.1

Component Table92

| Type | Callout |
| :---- | :---- |
| Content | There is room to work in CHUNK 6 and a possible solution in CHUNK 7\. |

Perform the following tasks: 

1. Divide the dataset into a train and test set, with the training set further divided into cross validation folds.  
2. Fit multiple initial models. Note that this is a binary response variable, so you can’t use the same models used previously.  
3. Combine the initial predictions using a meta-model. Again, the response variable is binary.  
4. Compare the various models. Because the response is binary, MSE is probably not the best choice.  
5. Interpret the chosen meta-model.

### **1.6.9 Exercise 3.6.1 Solution** {#1.6.9-exercise-3.6.1-solution}

1. Dividing the dataset is the same as it was in the example in the module.  
2. We chose the following three stage-0 models. Any models that handle binary responses would have worked.   
   1. Logistic regression  
   2. Decision tree – If using the R package **rpart**, it is important to set method \= "class"  
   3. Neural network – Make sure to set regression \= FALSE and to use a loss function that works well in binary outcomes (we used log loss).  
3. We used logistic regression to create the meta-models, both without initial covariates (meta1) and with them (meta2).  
4. The meta-model with only the predictions (Meta1) does better than all the other models when comparing via log loss (recall that smaller values are better).

Exercise 3.6.1 Solution

5. The significant contributors to Meta1 are the GLM and neural net stage-0 predictions (see output at right). If we remove the classification tree from the meta-model (meta3 in the code), the log loss gets a little worse. So even though the predictions are not significant in the model, they do help prediction.

|  | Estimate | Std.Error | z value | Pr(\>|z|) |  |
| ----- | ----: | ----: | ----: | ----: | ----: |
| (Intercept) | \-2.3680 | 0.1051 | \-22.537 | \< 2e-16 | \*\*\* |
| GLMPred | 1.2327 | 0.3312 | 3.722 | 0.000198 | \*\*\* |
| CTPred | 0.3622 | 0.3332 | 1.087 | 0.276916 |  |
| NNPred | 3.1657 | 0.2627 | 12.051 | \< 2e-16 | \*\*\* |

| Model | Null | Logistic Reg | Class Tree | Neural Net | Meta1 | Meta2 |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: |
| Log loss | 0.65977 | 0.60249 | 0.60199 | 0.59828 | 0.587318 | 0.58832 |

## ***1.7 Further Modeling Topics*** {#1.7-further-modeling-topics}

### **1.7.1 Section 3.7 Learning Objectives** {#1.7.1-section-3.7-learning-objectives}

Further Modeling Topics

Component Table93

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 3.7 Learning Objectives**  Recognize and mitigate the effects of starting with too many variables. Recognize and mitigate the effects of repeated use of train/test/validate sets. Be able to make predictions with missing data. Explain why being blind to sensitive or prohibited variables is not sufficient to ensure lack of bias. Explain, evaluate, and correct for analytical bias, such as proxy bias.  |
| Footer | Panel Footer |

### **1.7.2 Introduction** {#1.7.2-introduction}

Introduction  
Whether building the models introduced in this module or using models learned previously, there are common pitfalls that may lead to a model that fails to predict well when applied to new data. Two pitfalls will be discussed here. The first is the case where there is an extremely large number of potential predictor variables. The second is overusing the data. Using train/test/validate sets and employing cross validation can help, but those methods can be overused. 

The next topic area for this section addresses the challenge making predictions when the observations have missing values. Techniques introduced in Module 2 will be applied to this situation. 

The final topic is a discussion of fairness in modeling. The focus will be on measures of bias and techniques for eliminating proxy discrimination.

### **1.7.3 Large p, Small n** {#1.7.3-large-p,-small-n}

Large *p*, Small *n*  
What happens when the number of predictors ( *p*) is much larger than the number of observations ( *n*)? This is rare and becoming rarer, but there are examples when measurements are cheap, but samples are expensive. In auto insurance, telematics data on a car can give you many predictors but when the project is first rolling out, you may not have many drivers. 

The problem is that the models we use are generally too flexible. In most situations flexibility is a benefit, but when you have at least as many predictors as observations the added flexibility allows the models to fit too well. The estimate of *R* 2 will go to one, and even penalized estimates (like AIC, BIC, and adjusted *R* 2) will not provide meaningful results because the estimates of *σ* 2 are inaccurate. 

It will be hard to determine which predictors are the most important. When you have a lot of possible predictors, the problem of collinearity will be extreme. 

Your main options when this occurs are: 

* Naïve models  
* Feature (variable) selection or engineering  
* Dimension reduction  
* Regularization

You have seen all these techniques, so here we will only briefly discuss them and their application to large *p*, small *n* problems.

### **1.7.4 Naïve Models** {#1.7.4-naïve-models}

Naïve Models  
You can simply fit the model as is. In that case, linear regression will return an NA for all but *n*\-1 of the regression coefficients. It will also provide an exactly perfect fit, which is almost certainly overfit. Neural networks will still run, as will some other machine learning models (like tree-based models). 

These models will still give you an answer (though probably not a good one). It is likely that the model will be like a polynomial regression model with too many powers, it will fit the in-sample data precisely, but will do a terrible job predicting out-of-sample data. In other words, there will be high variance and low bias to the extent that the model will not predict well on new data. 

These are not good choices, but they are fast and easy.

### **1.7.5 Feature Selection or Engineering** {#1.7.5-feature-selection-or-engineering}

Feature Selection or Engineering  
You can reduce the number of predictors to fewer than *n* in many ways. Some examples include: 

* Combining multiple predictors into a single predictor (as we did with the hotel data combining the number of weekday and weekend nights to get a single measure of the length of stay);  
* Forward stepwise selection (backward stepwise selection will not work because there are more predictors than observations, so you cannot fit the full model with all the possible predictors);  
* Removing obviously unimportant variables;  
* Removing variables with a high proportion of missing data; and  
* Removing all but one variable from a set of highly interdependent or collinear variables.

### **1.7.6 Dimension Reduction** {#1.7.6-dimension-reduction}

Dimension Reduction  
You can also summarize numeric predictors using principal components. Depending on how many components you use, you can greatly reduce the number of predictors and still retain much of the predictive information. This comes with the cost of reduced model understanding and requires that all the variables that make up the components be collected when making predictions.

### **1.7.7 Regularization** {#1.7.7-regularization}

Regularization  
You can also fit a model using regularization to either reduce the coefficients to zero (effectively removing the variable from the model) or simply penalize the size of the coefficients so the impact of each predictor is smaller. One challenge of this approach is that the tuning parameter must be carefully set as it ultimately controls the number of coefficients that become zero.

### **1.7.8 How Many Data Sets?** {#1.7.8-how-many-data-sets?}

How Many Data Sets?  
Another important issue in model building is the use of subsets of the data. 

Sometimes we use a train/test split while other times we use a train/validate/test split (keeping in mind that there is no standard terminology). How do we choose which to use? When should we use cross validation? The answers will become clearer as we look at the purposes and definitions of each set. 

* **Training set** – The training set is the data on which the models are trained. This data is seen by the model and if this data were used to compare different models you risk overfitting.  
* **Validation set** – This set is used with the training set to compare different models or hyperparameter settings. The models are fit on the training data and then evaluated on the validation data. You will then choose the best model and hyperparameter settings based on their performance in the validation set.  
* **Test set** – The test set is supposed to be as close to real life as possible. None of the models should see the test set before they are optimized. Those models should be fit on the training data (or a combination of the training and the validation data) and then used to predict the test data.

### **1.7.9 How Many Data Sets?** {#1.7.9-how-many-data-sets?}

How Many Data Sets?  
Using those definitions, the choice of the number of data sets and the relative sizes of those data sets will depend on your prioritization of model fit, model complexity, computational speed, and the realism of the results. Here are some potential splits and the pros and cons of each.

Component Table94

| Type | Panel |
| :---- | ----- |
| Title | Panel |
| Header | Panel Header |
| Content |  **Split Hyperparameter Tuning Model Comparison Prediction** Train only Cannot use models that require tuning on validation data. Great for models that don’t because there is more data available. Requires a complexity penalty (like AIC/BIC) because there is no validation data to directly compare predictions. If prediction is performed on the in-sample data, the predictions will be over-confident and could lead to overfitting. Train with cross-validation Hyperparameters can be tuned using cross-validation. Training datasets for each model are smaller than the train only split. Models can be compared directly using the predictions on the folds, unless the cross-validation was used to train the models. If the model is chosen based on out-of-sample predictions in cross-validation, the predictions could be too optimistic. Train/test No way to tune hyperparameters. Models can be compared directly using their predictions on the test data. If the model is chosen based on out-of-sample predictions in the test data, the predictions could be too optimistic. Train/validation/test The validation dataset can be used to tune the hyperparameters. If the hyperparameters were not tuned on the validation set, the models can be compared directly using their predictions on the validation set. Alternatively, the models can be tuned using the validation set and then compared using the predictions on the test set, but in this case the test set cannot be used to evaluate the final model. If the models are chosen using predictions on the test set, prediction accuracy may be optimistic. If the models are chosen using predictions on the validation set, then predictions on the test set are likely a good representation of expected future predictive accuracy. Train, test, with cross-validation The cross-validation holdouts can be used to tune the hyperparameters. If the hyperparameters were not tuned on the cross-validation holdouts, the models can be compared directly using their predictions on the holdouts. Alternatively, the models can be tuned using cross-validation and then compared using the predictions on the test set. If the models are chosen using predictions on the test set, prediction accuracy may be optimistic. If the models are chosen using cross-validated predictions, then predictions on the test set are likely a good representation of expected future predictive accuracy.  |
| Footer | Panel Footer |

### **1.7.10 Missing Data and Predictions** {#1.7.10-missing-data-and-predictions}

Missing Data and Predictions  
In Module 2 we covered several methods for imputing missing data. This allows a model to be built on incomplete data without needing to throw away potentially predictive data. In some scenarios, it is possible that future observations may be complete, but in most situations, if data was missing when the model is built, there will be missing data in the future, making it necessary to handle missing data when making predictions. We need a way to build imputation into a prediction mechanism and will explore two methods for doing this.

### **1.7.11 Missing Data and Predictions** {#1.7.11-missing-data-and-predictions}

Missing Data and Predictions  
The first and most basic approach is to combine all the data and impute missing data before splitting into train, validation, and test sets. This is the easiest approach, and once the missing data is imputed, the three sets can be created and used as normal. One consideration when imputing on the full data set before splitting is to check the percentage of imputed values for each group. For example, if one set has twice the percentage of imputed data than another, the sets would need to be resampled. 

A second approach is to treat the imputation process as a model that is fit on the training set and then applied to any future data. For example, a regression imputation approach builds a predictive model that uses complete variables to predict the incomplete variables. That formula can then be applied, without updating it, on the validation or test data. One advantage of this approach is that it simultaneously tests the effectiveness of the imputation scheme along with the main predictive model for the data. Another advantage is that this approach can be used more effectively on future predictions. For example, if the model is being used to predict a specific future value that has predictors that were not available when the model is being trained, then this approach makes more sense. Not all imputation schemes can be represented as models, however, so this approach is not always possible.

### **1.7.12 Example: Method 1 \- Combined Imputation** {#1.7.12-example:-method-1---combined-imputation}

Component Table95

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 2 imputes missing values for the data as a whole. CHUNK 3 then fits a GLM using this approach. |

Example: Method 1 \- Combined Imputation  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_3\_7a\_r.rmd\]  
At this time, download the code files ( [atpa\_3\_7a\_r.rmd](#bookmark=id.3aq5f1tdfezu)) and the data set ( [ckd.csv](#bookmark=id.k2bjcuuwho10)). There are several predictors including age, blood pressure, glucose level, white blood cell count, and appetite. The target variable is *Chronic\_Kidney\_Disease*, which is 1 for patients with this disease and 0 otherwise. 

There is also a variable in the data frame called *set*. This is a randomly assigned variable where 50% of the data is assigned to a training set and 50% is assigned to a test set. We will not split out a validation set in this example, but the same principles apply. Age has many missing values, and the other variables are complete. We will explore imputing values for the age variable and fitting a predictive model. 

This process includes: 

1. Splitting variables with missing values into test and train to check if the percentage of missing values is similar in both groups;  
2. Performing an imputation scheme on the full, unsplit data. In this example we are using linear regression imputation, but any imputation scheme can be used;  
3. Splitting the full data (using same split as the one checked in step 1); and  
4. Fitting a predictive model to the training set and use it to predict on the test set.

This is a straightforward approach and runs quickly. The results will be examined after Method 2 is employed.  
\[END LINK\]

Component Table96

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 1 loads a data set on chronic kidney disease. |

### **1.7.13 Example: Method 2 \- Stored Imputation Scheme** {#1.7.13-example:-method-2---stored-imputation-scheme}

Component Table97

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 5 then applies this linear model to impute missing values on the test set. |

Example: Method 2 \- Stored Imputation Scheme  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/ckd.csv\]  
In this case, it is a linear regression model since age is continuous. This approach uses complete variables to build a linear regression model to predict age on only the training set.  
\[END LINK\]

Component Table98

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 4 builds an imputation model using only the training set. |

The model to predict chronic kidney disease is then built on the training set and applied to the test set. The full method can be summarized as: 

1. Build imputation scheme using only the training data. This often takes the form of a predictive model using complete predictors of the training set to predict missing values for incomplete predictors.  
2. Apply the imputation scheme to training set.  
3. Build a predictive model for the target variable on the training set using imputed values.  
4. Use the predictive model from Step 1 as an imputation scheme for the test set. Do not refit the model.  
5. Use predictive model from Step 3 to predict the target in the test set.

This approach also runs quickly.

### **1.7.14 Example: Comparison** {#1.7.14-example:-comparison}

Component Table99

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 7 shows a computational trick that performs the second approach in a cleaner way. |

Example: Comparison  
The two approaches have very similar results and the predicted values are very close to each other. In this case it may have been appropriate to simply impute the whole data set because it is simpler, but again, there are reasons to build an imputation scheme on the training set first, especially when considering using a predictive model for observations that will be recorded in the future.

Component Table100

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 6 compares these two approaches, the first of which is imputing on the whole data set and then splitting, the second is building an imputation scheme on the training set and then applying it to the test set. |

It is less intuitive than stepping through the process as we did in CHUNKs 4 and 5, but the same goal is accomplished. This approach does not save the imputation scheme to be used on data that may come in the future but is especially useful for creating an imputation scheme on the training group to build a model and then applying the scheme to the test group to make predictions. 

Note that while a linear regression imputation was used for these examples, many other imputation schemes can be used. For the first approach any imputation method can be used. For the second approach, only methods where a model can be stored and used again for prediction can be used.

### **1.7.15 Other Hold-out Approaches** {#1.7.15-other-hold-out-approaches}

Other Hold-out Approaches  
If there is an additional hold-out set, such as a validation set, then the imputation approaches for prediction are the same as for the test set: either impute with the full data or use the training imputation scheme on the validation set. 

When using *K*\-fold cross validation, a full imputation is convenient because you can impute once and then perform *K*\-fold cross validation as normal. The second approach can still be used. In that case you would find an imputation scheme for the *K*–1 folds being used to train the model and then use it on the last fold. 

Leave one out, or LOO, cross validation fits a model on all but one observation and then predicts the one. In this case, using the second approach means that there are two models being fit each time, which doubles computation time. At this granularity, it makes a lot more sense to do a full imputation.

### **1.7.16 Missing Data and Ethics** {#1.7.16-missing-data-and-ethics}

Missing Data and Ethics  
One last consideration when making decisions on how to handle missing data is the ethical implications. There may also be government regulations that deal with when it is appropriate to impute missing values and how they may be imputed. These must be considered when imputing the missing data. 

The purpose of these regulations are to ensure that individuals with missing values are not penalized for the missingness of the data. For example, if a survey field asks for an individual’s race and there is an option for someone to enter “not willing to say,” this response should carry some implicit guarantee that the individual is not penalized in any way for that response. Predictions can be reviewed after the model is fit to see if there is an unusual correlation between predictions and the missingness of the data.

### **1.7.17 Ethics in Modeling** {#1.7.17-ethics-in-modeling}

Ethics in Modeling  
As discussed previously, there are many different aspects of fairness. A simple way to think about fairness is to consider whether one person is treated like the others. Algorithms may appear to be unbiased and objective because many are based on mathematical calculations that are viewed as hard, objective, logical, axiomatic and, therefore, trustworthy. In some ways, this is true; a mathematical calculation on its own is indeed objective. However, algorithms are subject to the choices of the humans building and implementing them. This is especially true in a business context, where models and other analytical output have implications for the business, customers, and society. 

### **1.7.18 Fairness in Analytics** {#1.7.18-fairness-in-analytics}

Fairness in Analytics  
Statistical models typically learn the correlations and distributions within a dataset by optimizing some **objective function** (e.g., sum of squared errors). The algorithm has no biases or suspect motivations of its own – it only considers the data it is fed and the objective function. 

So how could its outcome be biased and unfair? Ironically, it is this same dispassionate focus on the objective function that can cause problems. Just as the model does not know to discriminate against a protected class, it does not know to **not** discriminate against that class. If a certain relationship in the data results in an improvement according to the objective function, the model will reflect that relationship, regardless of its potential unfairness. 

This is one reason why the discussion in Module 2 about data is so important. The information we expose a model to can lead to unfair outcomes. While part of this involves asking what data we are going to use, another part involves deciding how to use the data in a chosen analytical method. Later in this section we will discuss proxy discrimination, which is a continuation of the feature selection and omitted variable bias discussion started in Module 2\. 

Preventing a model from learning to unfairly discriminate does not stop with the data step. Once we are building models based on the data, we need to be able to evaluate our model results for unfair outcomes. The first obstacle here is defining what we mean by “unfair.” In this section we will cover differing definitions of fairness and how they are measured. It is important to realize that satisfying all measures is not possible mathematically. Many disagreements about fair outcomes can be traced to disagreements about how to define a fair outcome.

### **1.7.19 Example: COMPAS** {#1.7.19-example:-compas}

Example: COMPAS  
One well-known example, which we will use to introduce the topic, is the COMPAS algorithm. In the United States, COMPAS is a decision-making algorithm in the criminal justice system (the acronym stands for “correctional offender management profiling for alternative sanctions”). It assigns a risk level to defendants that a judge can use to determine whether the defendant should remain in jail or be let out while waiting for a future court date (Hao & Stray, 2019). The algorithm considers historical rates of recidivism (whether a defendant commits a new crime) and assigns a score between 1 and 10 based on the characteristics of the individual. Generally, if a defendant has a score above a certain high-risk threshold, a judge will recommend jail. Defendants designated as a low risk based on the algorithm’s score are let free until the trial. 

COMPAS came under scrutiny for what was perceived to be a racial bias in the algorithm itself, even though, by law, it could not take race into account in the training of the algorithm. A *ProPublica* investigation highlighted concerning findings: a) black defendants were predicted to have a higher rate of recidivism than actually occurred; b) white defendants were often found less risky than future data indicated them to be; and c) black defendants were about twice as likely as white defendants to be classified as having a high risk of recidivism (Larson, Mattu, Kirchner, & Angwin, 2016).

### **1.7.20 Fairness in Analytics** {#1.7.20-fairness-in-analytics}

Fairness in Analytics  
Northpointe, the consulting firm that developed the COMPAS algorithm, did not agree with the *ProPublica* allegations of racial discrimination. Using different statistical measures, they found that, for each level of risk on their scale, the score provided by the algorithm had the same predictive accuracy regardless of race (Semenovich & Dolman, n.d.). In other words, Northpointe showed that, for each point along the scale produced by COMPAS, the result meant the same thing with regard to future recidivism regardless of race. Combined with the fact that the overall recidivism rate is higher for black defendants than for white defendants, this implies that a larger proportion of black defendants will be assigned higher risk scores. And hence, a larger proportion of black defendants who do not reoffend will also be assigned higher risk scores (Corbett-Davies, S., Pierson, E., Feller, A., & Goel, S., 2021). 

Mathematically, both *ProPublica* and Northpointe had justifications for their position. Which metric better indicates the outcome that is “more” fair? This example shows that results can be analyzed in different ways to support multiple perspectives, which complicates the assessment of fairness.

### **1.7.21 Concepts of Algorithmic Fairness** {#1.7.21-concepts-of-algorithmic-fairness}

Concepts of Algorithmic Fairness  
We will discuss several concepts related to algorithmic fairness. There are multiple ways to approach defining what is fair, and in general, there will not be a single metric that is best for all circumstances; the decision of the appropriate definition of fairness will depend on the situation.

### **1.7.22 Disparate Treatment vs Disparate Impact** {#1.7.22-disparate-treatment-vs-disparate-impact}

Disparate Treatment vs Disparate Impact  
Most of the legal considerations of fairness deal with unfair treatment along two primary dimensions—disparate treatment or disparate impact (Zhong, 2018). 

Click on the tabs to read more information.

Component Table101

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Disparate Treatment |
| Tab 1 Content | **Disparate treatment** refers to actions taken, either wholly or in part, with the intention of acting against a protected class. As far as predictive modeling is concerned, disparate treatment can take two primary forms — either intentionally setting up the model or algorithm to take into account the protected class (formal classification) or intentionally acting in a discriminating manner by the use or design of the model (Barocas & Selbst, 2016). The former is easier to address; characteristics like race are prohibited from being used explicitly in determining insurance premiums. The latter may be more difficult to identify and address, both because the effect is obscured and because the indirect nature of the impact may make determination of intent difficult.  |
| Tab 2 Title | Disparate Impact |
| Tab 2 Content | Disparate impact addresses this issue by focusing on impact instead of treatment. Disparate impact as a legal standard does not consider any intention on the part of the designer or user of a model. It instead is concerned with looking at the actual outcomes produced through a model or practice related to a protected class. However, while there is a large amount of case law dealing with how to prosecute under these two legal standards in cases such as employment discrimination, they remain abstract from a mathematical point of view and don’t allow for us to obtain an objective definition of what fairness is in a machine learning context. Instead, we present the proposed definitions in the following pages that have mathematical support for their determination. |

### **1.7.23 Direct and Indirect Discrimination** {#1.7.23-direct-and-indirect-discrimination}

Direct and Indirect Discrimination  
You were previously introduced to the concept of protected classes. Usually defined by law, protected classes exist to prevent discrimination based on specific characteristics. Discrimination can come in two forms — direct and indirect. 

**Direct discrimination** occurs when a choice is intentionally made to treat someone differently because of a protected characteristic or to produce a different outcome for one protected class versus another. 

**Indirect discrimination** occurs when a practice, policy, or rule is implemented that applies to everyone in the same way but puts certain protected groups at a disadvantage and the organization putting the practice, policy, or rule in place cannot provide legitimate justification for doing so.

### **1.7.24 Unawareness and Demographic Parity** {#1.7.24-unawareness-and-demographic-parity}

Unawareness and Demographic Parity  
Unawareness

In order to comply with anti-discrimination laws and rules around protected classes, one method that has been employed in setting up algorithms is to be unaware of the protected class. Strong correlations that may exist between the protected class and other characteristics actively used in the model have led some to consider unawareness as not sufficient to achieve fairness. 

Demographic Parity

A different definition of fairness has been proposed that has been called **demographic parity** (or statistical parity). A simplified mathematical formula for each method is as follows for a generic decision procedure *d* (Semenovich & Dolman, n.d.) 

* Unawareness: ![][image41]  
* Demographic parity: ![][image42]

In the above formulas, *A* is a given protected class that, for our example, has two attributes, *a* and *a*’. The set of attributes outside of the protected class that are considered by the algorithm is represented by *X*. The function *d* produces the decision made for those with given values of *X* and *A.* 

In plain language, the formula for unawareness states that the decision for any individual should not vary if we adjust the characteristic of the protected class (which is unknown to the procedure). 

Demographic parity, instead, says that the expected outcome (with the expectation taken over the possible values of *X*) of a procedure should be the same for each subpopulation of the protected characteristic. While unawareness concerns treatment at the individual level, demographic parity works at the group level.

### **1.7.25 Example: Unawareness and Demographic Parity** {#1.7.25-example:-unawareness-and-demographic-parity}

Example: Unawareness and Demographic Parity  
Suppose *A* is sex with *a* \= male and *a*’ \= female. Also suppose *X* is height in centimeters. 

The decision might be *d*( *x*, mal e) \= 1 if *x* \> 175 and 0 otherwise and *d*( *x*, female) \= 1 if *x* \> 175 and 0 otherwise. 

The example exhibits unawareness because males and females of the same height have the same decision. 

Now further suppose the heights of males are normally distributed with mean 175 and standard deviation 10 while for females the mean is 165 and the standard deviation is 10\. The expected decision for males is the probability of exceeding 175 centimeters, which is 0.5, while for females it is 0.159. Thus, demographic parity is not present. 

In the example, suppose a 1 means approval for a credit card. Then half of males will be selected while only roughly one in six females will qualify.

### **1.7.26 Predictive Parity** {#1.7.26-predictive-parity}

Predictive Parity  
Predictive parity states that, for each value that the decision algorithm can take, the expected value of the observed outcome *Y* does not vary across protected classes. Mathematically, this is stated as:   
![][image43]   
In other words, for each decision ( *d*) made by an algorithm across protected classes ( *A*), we want the probability of the true target to be the same. Where demographic parity considers the expected value of predicted outcomes, predictive parity considers the expected value of actual outcomes for a given prediction. 

In the context of a binary decision-making situation, for each protected class, we can calculate the probability that an individual who was predicted to have a positive outcome will actually have a positive outcome; this is known as positive predictive value (PPV). When the PPV does not vary by protected class, this is stated mathematically as:   
![][image44]   
Likewise, for each protected class, we can calculate the probability that an individual who was predicted to have a negative outcome will actually have a negative outcome; this is known as negative predictive value (NPV). When the NPV does not vary by protected class, this is stated mathematically as:   
![][image45]   
Predictive parity requires that both PPV and NPV do not vary across protected classes.

### **1.7.27  Predictive Parity in Regression** {#1.7.27-predictive-parity-in-regression}

Predictive Parity in Regression  
It is not obvious how to extend this concept to a regression setting. Here the decision, *d*, is not either 0 or 1, but takes on a wide range of values. It would not make sense to evaluate the outcomes segregated by each predicted value. One option would be to change the problem to one of classification by looking at cases where the prediction is above or below a certain value and then seeing if the observation was also above or below. 

Another option is not to consider the probability of making an error, but rather the average error that is made, that is, the bias (using the statistical meaning of the term). The parity equation then becomes:   
![][image46]   
That is, the difference between average predicted and observed values are the same regardless of the value of the protected variable.

### **1.7.28 Examples: Predictive Parity** {#1.7.28-examples:-predictive-parity}

Examples: Predictive Parity  
Click on the tabs to read information about two examples of predictive parity.

Component Table102

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Example 1 |
| Tab 1 Content | As an example, suppose we have a decision algorithm that is set up for college admissions and is meant to predict whether a student will have a GPA high enough to maintain good standing in the university. If the algorithm predicts this to be the case, the prospective student is admitted, otherwise the student is rejected. Acceptance will be represented as *d* \= 1, a rejection as *d* \= 0\. The realized outcome would be whether the student maintained a high enough GPA ( *Y* \= 1\) or did not ( *Y* \= 0\) to remain in good standing. For predictive parity to hold, if we take the protected class of sex with two levels, *a* \= male and *a’* \= female, the proportion of admitted students being in good standing for each level would be the same (given that *d* \= 1 for each student currently enrolled); this is equality of PPV. If it were possible to track rejected students’ ( *d* \= 0\) academic status (perhaps at another university with lower acceptance standards or a school with guaranteed admission), it should also hold that the proportion of students not in good standing should be the same for male and female, as well; this is equality of NPV. In other words, the test is checking whether or not the admissions process is taking into account factors that predict academic success regardless of sex. |
| Tab 2 Title | Example 2 |
| Tab 2 Content | In an insurance context, the predictive parity fairness metric states that a premium assigned by a pricing algorithm ( *d*) should be reflective of the actual claims experience ( *Y*) expected to emerge regardless of the level of the protected class, all else being equal. Under this fairness metric, a decision made (or premium assigned) by the algorithm should mean the same thing regardless of the protected class.  |

### **1.7.29 Group vs Individual Fairness Metrics** {#1.7.29-group-vs-individual-fairness-metrics}

Group vs Individual Fairness Metrics

Component Table103

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Benefits |
| Tab 1 Content | A benefit of individual fairness metrics is that they intuitively work the way most of us think about decision algorithms — individual to individual rather than averages across groups. |
| Tab 2 Title | Drawbacks |
| Tab 2 Content | One drawback with individual fairness metrics is the difficulty in designing a similarity metric, especially for the inputs to a model where categorical variables are used and sets of variables are large enough that comparisons become difficult. While it is fairly easy to say that credit scores of 704 and 705 are similar and outcomes of a decision algorithm in pricing of auto insurance using credit score should be similar (under individual fairness) for these two scores, all else being equal, it is more difficult to define how similar two accident history records are. Number of accidents, their severity, when they occurred—all of these must be considered to determine just how similar two distinct records are. |

Group Fairness Metrics   
The metrics of demographic parity and predictive parity previously discussed are group fairness metrics. You will notice that their equations focus on expected values such that the relationships hold across groups on average, but this does not necessarily apply to the individuals that are a part of these groups. 

Individual Fairness Metrics   
The motivation of individual fairness is based on the following statement: “similar individuals should be treated similarly” (Zhong, 2018). If an algorithm works according to individual fairness, then the outcome of the decision model, for each pair of individuals that have characteristics similar to each other, must also be similar to the same degree. Unawareness is an example of an individual fairness metric. 

Click on the tabs to read more information.

### **1.7.30 Example: Fairness Metrics** {#1.7.30-example:-fairness-metrics}

Example: Fairness Metrics  
\[BEGIN LINK \-https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients\]  
At this time download the Rmd file for this material ( [atpa\_3\_7b\_r.rmd](#bookmark=id.l2y0dudganhc)). We will now examine data involving credit card payment defaults ( [dccc.csv](#bookmark=id.ut05ji44pulo)) in Taiwan (Yeh and Lien, 2009).\* We will use logistic regression to model the probability of default as a function of several demographic variables of the customer, as well as some variables related to previous payment history. We will treat sex as a protected variable for this example.  
\[END LINK\]

Component Table104

| Type | Callout |
| :---- | :---- |
| Content | We first load the data, and fit the full model, as well as the model implementing unawareness, i.e., using all of the predictors in the full model except sex. Run CHUNK 1 do this. |

\[BEGIN LINK \-https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients\]  
Looking at means of the probabilities predicted by the full model, we can see a significant disparity by sex (24.2% vs 20.8%). Under the unawareness model, we can see that leaving out sex as a predictor results in a disparity that is smaller, but still present (22.6% vs 21.8%). 

\* Information about the data set is available at [https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients](#bookmark=id.vyt7t8iiihux)  
\[END LINK\]

### **1.7.31 Other Fairness Metrics** {#1.7.31-other-fairness-metrics}

Other Fairness Metrics  
\[BEGIN LINK \-http://www.datasciencepublicpolicy.org/our-work/tools-guides/aequitas/\]  
There are multiple ways to approach defining what is fair, and in general, there will not be a single metric that is best for all circumstances; the decision of the appropriate definition of fairness will depend on the situation (Verma and Rubin, 2018). 

How do we determine the most appropriate definition for a given situation? If we can articulate the type of result we are hoping to achieve, we can then translate this into a sensible notion of fairness and its corresponding metric. Some efforts have recently been made to provide tools to help map desired outcomes to fairness metrics. For example, [Aequitas](#bookmark=id.q05rzszbzzit) (Aequitas, 2021\) provides a decision tree (their “Fairness Tree”) which helps guide users toward an appropriate definition of fairness for a given situation. (This reading is optional.)  
\[END LINK\]

### **1.7.32 Demographic Parity** {#1.7.32-demographic-parity}

Demographic Parity  
Suppose that the lender seeks to make a decision to intervene in cases where the predicted probability exceeds some threshold, such as 25%. We may be interested in assessing the level of fairness (according to the fairness metrics defined previously) for such a decision rule based on our unawareness model.

Component Table105

| Type | Callout |
| :---- | :---- |
| Content | First we consider demographic parity. Run CHUNK 2 to perform the calculations. |

Demographic parity requires that the expected value of the decisions be equal across levels; in this case, that requires that the proportion of interventions is equal across levels of sex. This does not hold here as we have interventions (predicted probability of default exceeding 25%) for 47.2% of the males, but only 40.0% of the females.

|  | F | M |
| ----- | :---: | :---: |
| FALSE | 0.600 | 0.528 |
| TRUE | 0.400 | 0.472 |

### **1.7.33 Predictive Parity** {#1.7.33-predictive-parity}

Predictive Parity  
Next, we consider predictive parity for this model. Predictive parity requires the probability of a correct intervention decision to be constant across levels of sex.

Component Table106

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 3 to calculate the required values. |

The level of predictive parity for the unawareness model looks reasonably good, but still a bit unequal. The percent of correct interventions (PPV) is 32.5% for males and 29.8% for females, while the percent of correct non-interventions (NPV) is 83.3% for males and 85.2% for females; see tables below. 

Hence, we have seen in this example that unawareness of a protected characteristic does not necessarily result in fairness across the characteristic, according to the fairness metrics considered here. 

Note that while we did not do so in this example, in many cases it will be possible to formally test for the statistical significance of differences. 

| Males |  |  |
| :---: | :---: | :---: |
|  | **default** |  |
| intervene | 0 | 1 |
| 0 | 0.833 | 0.167 |
| 1 | 0.675 | 0.325 |

| Females |  |  |
| :---: | :---: | :---: |
|  | **default** |  |
| intervene | 0 | 1 |
| 0 | 0.852 | 0.148 |
| 1 | 0.702 | 0.298 |

### **1.7.34 Proxy Discrimination** {#1.7.34-proxy-discrimination}

Proxy Discrimination  
As discussed earlier in this section, one potential approach to fairness is through unawareness. Certain protected characteristics cannot be used by insurance algorithms such as pricing or underwriting models. However, as we saw, simply ignoring a characteristic may not mean we are avoiding discrimination. Both disparate treatment and disparate impact can involve indirect discrimination (note that indirect is not the same as unintentional). 

There may be variables that do not have the appearance of being unfair but are correlated with membership in a protected group and are useful predictors in a model. **Proxy discrimination** occurs when the inclusion of such variables produces disparate impact. 

An example we have touched on before is the, now illegal, practice of redlining, a mortgage lending and investment practice that used zip codes as a determining factor for issuing loans that resulted in unfair lending practices that impacted predominantly low-income minority populations. The practice of redlining fails scrutiny under both disparate treatment and disparate impact. It is also an example of proxy discrimination, which is a subset of disparate impact.

### **1.7.35 Proxy Discrimination** {#1.7.35-proxy-discrimination}

Proxy Discrimination  
Consider the following example from Prince & Schwarcz (2020). For the sake of this example, assume the following are true: 

* Particular genetic variants called BRCA are predictive of extra cancer deaths and hence a higher mortality rate.  
* There is a genetic test to determine if a person has a variant.  
* Genetic testing is prohibited in pricing.  
* Members of protected group A have the same incidence of the variant as the general population.  
* There is a Facebook group that encourages members of protected group A to be tested for the variant.  
* Members of this Facebook group have a higher incidence of cancer and hence higher mortality than the general population.

Using membership in the Facebook group for pricing is proxy discrimination with regard to genetic testing. There is disparate impact as members of this group have higher mortality and hence higher premiums. It is also proxy discrimination for genetic testing because the connection is directly useful to the pricing algorithm. One way to look at it is to note that if genetic testing were allowed, membership in the Facebook group would cease to be predictive. 

By the definition of proxy discrimination presented here, there is no proxy discrimination with respect to being a member of protected group A with regard to cancer deaths. There is still disparate impact due to the correlation of being in the Facebook group and being in the protected group. However, the predictive power has nothing to do with being in this protected group. Note that here if being a member of protected group A could be used in pricing, membership in the Facebook group would continue to be predictive.

### **1.7.36 Proxy Discrimination** {#1.7.36-proxy-discrimination}

Proxy Discrimination  
As mentioned above, intention is not required for proxy discrimination. With a complex model, the insurer could be unaware that the model is targeting membership in the Facebook group. The risk of unintentional proxy discrimination is especially high when using complex models, because models will by nature find new proxies when deprived of predictive variables (Prince & Schwarcz, 2020). The less human involvement there is in developing the model, for example with machine learning models that learn with little human input, the more likely proxy discrimination will occur and go unnoticed. For this reason, more testing will need to be done to minimize unintentional proxy discrimination. 

Note that human involvement does not preclude the occurrence of unintentional proxy discrimination. It simply means we have an opportunity – and therefore a responsibility – to be more deliberate about what goes into the model.

### **1.7.37 Proxy Discrimination** {#1.7.37-proxy-discrimination}

Proxy Discrimination  
With increased awareness around the potential for proxy discrimination, there have been efforts to restrict variables that might serve as proxies for protected characteristics like race or income. Education, occupation, and credit score have received heightened scrutiny for this reason (Wang, 2020). 

New York State restricted the use of both education and occupation for auto and homeowners insurance in 2019, designating their use as unfairly discriminatory (New York State Department of Financial Services, 2019). The Washington State Office of the Insurance Commissioner has advocated for banning the use of credit scores in determining auto insurance premiums, following the lead of states like California (Office of the Insurance Commissioner Washington State, n.d.). 

Restricting the use of protected characteristics and common proxies is a viable way to prevent intentional discrimination by humans. However, this approach fails to completely address unintentional proxy discrimination. Machine learning models, when deprived of a predictive variable, will learn less intuitive relationships within the data that help replace the restricted characteristics (Prince & Schwarcz, 2020). Hence, some regulators may require insurers to provide additional analysis regarding the presence of unintentional proxy discrimination.

### **1.7.38 Types of Proxy Discrimination** {#1.7.38-types-of-proxy-discrimination}

Types of Proxy Discrimination  
The most direct way to predict an outcome would be to perfectly understand the causes of the outcome. However, machine learning models are trained to learn correlations between variables. These models are not able to discern causal relationships. 

You are probably familiar with the phrase “correlation does not imply causation.” Models learn the correlations that exist within a dataset, but do not have the ability to distinguish between a variable that has a direct causal relationship with the target variable and a variable that is simply correlated with the true cause. A variable that exhibits a causal relationship with the target variable might be omitted from the model to prevent unfair discrimination.

### **1.7.39 Types of Proxy Discrimination** {#1.7.39-types-of-proxy-discrimination}

Types of Proxy Discrimination

Component Table107

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Causal |
| Tab 1 Content | A protected characteristic has a causal relationship with the target variable. A facially neutral variable (a variable that does not explicitly single out a protected group), which is correlated with the protected characteristic, acts as a proxy variable. Its predictive power is directly a result of the correlation with the causal variable. A common example of this is Huntington’s disease. Individuals with a certain variant of the HTT gene will develop the disease with essentially complete certainty. No other factors help predict the development of Huntington’s disease. If information about an individual’s HTT gene is withheld from a model, it might proxy discriminate using some correlated variable like family history of Huntington’s disease reported on an application or visits to a website for a Huntington’s disease support group (Prince & Schwarcz, 2020). |
| Tab 2 Title | Opaque |
| Tab 2 Content | A protected characteristic is correlated with a variable that has a direct causal relationship with the target variable. This causal variable is either unquantifiable or unavailable. A facially neutral variable proxies for the protected characteristic, which in turn proxies for the true causal variable. Consider auto insurance rating as an example. Sex is predictive of auto insurance claims, partly due to different levels of care. The true causal variable is the level of care taken by a driver. Sex, which in some cases is a protected class that can’t be used for rating, is a proxy for that. If sex is prohibited, another variable may proxy for it. Note that as more data points become available, a more direct representation of the causal variable may supersede the protected characteristic. In this example, auto insurance companies are starting to use telematics data, including information on driving habits, to more directly measure how careful a driver is (Prince & Schwarcz, 2020).  |

The model, not seeing any information about the prohibited and thus omitted variable with a causal relationship with the target, will not be able to tell if remaining variables are predictive due to their own causal relationship with the target variable or due to their correlation with the omitted, predictive variable. Proxy discrimination can occur in different ways, depending on the relationship between the protected characteristic and the target variable. 

Click on the tabs to read more information.

### **1.7.40 Addressing Proxy Discrimination** {#1.7.40-addressing-proxy-discrimination}

Addressing Proxy Discrimination  
\[BEGIN LINK \-https://doi.org/10.1080/10920277.2021.1951296\]  
Section 6 of “The Discriminating (Pricing) Actuary” (Frees and Huang, 2021\) discusses the strategies that have been used by policymakers to combat proxy discrimination, new strategies involving linear models, and machine learning approaches to solving this problem ( [The Discriminating (Pricing) Actuary](#bookmark=id.8m3zj7n275qo)). Please read this section at this time. 

Section 6.3 is an example of the ideas presented in the article; R code used for this example can be found in Section 2.4 of the appendix. The code is also reproduced in the Rmd file for this section. 

Note that. as is often the case, the authors use gender when they most likely mean sex. To be consistent with the article, gender will be used for this discussion. 

The following pages provide a summary of Section 6.2 of the paper. It is then followed by an overview of the Section 6.3 example and two exercises.  
\[END LINK\]

### **1.7.41 Framework** {#1.7.41-framework}

Framework  
It is assumed that a linear model is being used (which could be a GLM or an additive model). The model is built using two sets of variables. To simplify notation from that used in the paper, let *A* be the set of acceptable variables and *P* be the set of protected variables. From these variables, the following two models are easily constructed: 

Model 1: Using all available variables   
![][image47]   
This notation indicates that the model uses both sets of variables. 

Model 2: Using only acceptable variables   
![][image48]   
Model 2 would appear to meet any regulatory constraints as protected variables are not used. However, if any of the acceptable variables are correlated with the protected variables, proxy discrimination will occur. 

The next two pages provide alternative models that may reduce any proxy effect.

### **1.7.42 Orthogonal Variables** {#1.7.42-orthogonal-variables}

Orthogonal Variables  
This model is based on ensuring that all variables used are uncorrelated with the protected variables. Without going into the details (the formula is in the paper), do a linear transformation of the acceptable variables (similar to using PCA) to create an equal number of new variables. 

Model 3: Orthogonal predictors   
![][image49]   
Here the asterisk indicates use of transformed versions of the acceptable variables. The key to this method is that *A*\* and *P* are uncorrelated and hence *A*\* cannot be a proxy for *P*. However, a careful look at the formula shows that values of *P* are used to create *A*\*. Hence, even though *P* is not used in the traditional sense, it still must be collected. This model should meet regulatory constraints as again protected variables are not used. In cases where the collection of the protected variables is prohibited, it may be possible to use known proxies for them to achieve the same goal.

### **1.7.43 Pope–Sydnor Model** {#1.7.43-pope–sydnor-model}

Pope–Sydnor Model  
This model does not have a descriptive name. It comes from the paper (Pope and Sydnor, 2011\) that introduced it. 

Their proposal is to replace each variable in the protected set with its average value. For example, if *Sex* \= 0 is male and *Sex* \= 1 is female and 60% of the observations are female, all observations will have a *Sex* value of 0.6. The model used is the model fit to all variables, including the protected variable (it is not refit to these transformed variables). However, predictions are made used the transformed values. 

Model 6: Pope –Sydnor   
![][image50]   
Here *P* ( *t* ) represents the transformed versions of the protected variables. This approach ensures that people with the same values of acceptable variables but different values of protected variables will get the same prediction, but as with Model 2, there may be different predictions on average across protected groups. As with the previous model, it is necessary to collect data on the protected variable. 

Note: The paper also has Models 4 and 5, which will not be covered in this module.

### **1.7.44 Exercise 3.7.1** {#1.7.44-exercise-3.7.1}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/proxy.csv\]  
We further explore the ideas of fairness and proxy discrimination discussed above by analyzing two data sets. The first will be to replicate the analysis in the Frees paper. The second will continue an examination of the credit card default data. Begin by downloading the dataset used in the paper ( [proxy.csv](#bookmark=id.yn4s8w2gts2x)). 

For the claim severity data presented in “The Discriminating (Pricing) Actuary” (Frees and Huang, 2021), we will consider the full model (Model 1), the unawareness model excluding *Gende*r (Model 2), the model with orthogonalized coefficients (Model 3\) and the model with Pope-Sydnor coefficients (Model 6). We will follow the authors’ approach and use the predicted value of claim severity as the response/ decision, taking *Gender* to be a protected variable. As is often the case, the authors likely meant sex rather than gender, but we will retain the variable name from the paper to maintain consistency.  
\[END LINK\]  
Exercise 3.7.1  
For each of these four models, determine the extent to which fairness is achieved, as measured by: 

* Demographic parity  
* Predictive parity

Component Table108

| Type | Callout |
| :---- | :---- |
| Content | Run the code in CHUNKS 4–9 to reproduce the models and predicted values from the paper. |

Component Table109

| Type | Callout |
| :---- | :---- |
| Content | Use the space in CHUNK 10 for your work. Some code is provided to get you started. The solution is discussed on the next page. |

### **1.7.45 Exercise 3.7.1 Solution** {#1.7.45-exercise-3.7.1-solution}

Exercise 3.7.1 Solution

Component Table110

| Type | Tabset |
| :---- | ----- |
| Tabs | 2 |
| Tab 1 Title | Demographic Parity |
| Tab 1 Content | To assess demographic parity, we can compare the mean fitted claim values by gender for each model under consideration. The following table presents the results.  **Model E(claims | Female \= 1\) E(claims | Female \= 0\) Difference** 1 1863.01 2215.56 –352.55 2 2015.06 2011.80 3.25 3 2013.17 2014.34 –1.17 6 2018.17 2007.63 10.55  |
| Tab 2 Title | Predictive Parity |
| Tab 2 Content | To assess predictive parity, we can compare the mean discrepancy between actual and predicted values by gender. We see that while Model 1 largely accomplishes predictive parity, all of the other models fare poorly on this metric. In particular, for Model 1, the fitted values exceed the actual claim values, on average, by 9.25 for the females, whereas for the males, the actual claim values exceed the fitted values by 14.13. Thus, the discrepancy is just 23.38, a small amount relative to a mean claim amount of just over 2000\. Models 2, 3, and 6, however, have discrepancies between the genders of 379.18, 374.75, and 386.48; we conclude that none of these models exhibit predictive parity.  **Model Model 1 Model 2 Model 3 Model 6** Mean of (actual \- fitted) for males 14.13 217.88 215.35 222.06 Mean of (actual \- fitted) for females –9.25 –161.30 –159.41 –164.42 Difference –23.38 –379.18 –374.75 –386.48 This exercise serves to highlight the point that some fairness metrics can be incompatible with one another in some circumstances; that is, it may not be mathematically possible to simultaneously achieve two given metrics.   |

Component Table111

| Type | Callout |
| :---- | :---- |
| Content | The code in CHUNK 11 provides the numbers used in the solution. |

### **1.7.46 Exercise 3.7.2** {#1.7.46-exercise-3.7.2}

For the credit card default data, we previously fit full and unawareness models using several predictors. For the sake of simplicity, we will use only the *SEX*, *LIMIT\_BAL*, *BILL\_AMT1*, and *PAY\_AMT1* predictors.  
Exercise 3.7.2

Component Table112

| Type | Callout |
| :---- | :---- |
| Content | Space is provided in CHUNK 13 for your work. The solution is discussed on the next page. |

Component Table113

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 12 repeats the early analyses using only these variables. |

Using these same three predictors, fit a logistic regression model to this data set using orthogonalized coefficients (Model 3). Assess the level of fairness using demographic parity and predictive parity, employing the same intervention threshold of 25%. Then repeat this process using the Pope-Sydnor model (Model 6). Compare your results to those from the unawareness model (Model 2\) to see if either provides an improvement.

### **1.7.47 Exercise 3.7.2 Solution** {#1.7.47-exercise-3.7.2-solution}

We can check demographic parity for these models using the results calculated from all three models. (Columns represent the values of *SEX*, while rows represent the intervention decision.)  
Exercise 3.7.2 Solution

|  | Unawareness |  | Orthogonal |  | Pope–Sydnor |  |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: |
|  | Male-ND | Female-ND | Male-ND | Female-ND | Male-ND | Female-ND |
| No | 0.821  | 0.848 | 0.817 | 0.848 | 0.820 | 0.847 |
| Yes | 0.687 | 0.711 | 0.686 | 0.712 | 0.686 | 0.710 |

|  | Unawareness |  | Orthogonal |  | Pope–Sydnor |  |
| ----- | :---: | :---: | :---: | :---: | :---: | :---: |
|  | M | F | M | F | M | F |
| No | 0.534 | 0.595 | 0.550 | 0.589 | 0.540 | 0.598 |
| Yes | 0.466 | 0.405 | 0.450 | 0.411 | 0.460 | 0.402 |

We see that the orthogonalized model does slightly better than the unawareness model. For the orthogonalized model, the percentage of male interventions is 45.0% vs 41.1% for females, resulting in a discrepancy of 3.9%. For the unawareness model, the percentage of male interventions is 46.6% vs 40.5% for females, resulting in a larger discrepancy of 6.1%. The Pope-Sydnor model results in a similar discrepancy, 5.8%.  
In terms of predictive parity, the three models perform very similarly. All show relatively small disparities in their PPV and NPV between males and females. In the results to the right, ND represents “no default” events, whereas NI and I represent “no intervention” and “intervention” decisions, respectively. To save space, there is no column for “default” as the value is the complement of “no default.”

### **1.7.48 Biases Introduced After Model Build** {#1.7.48-biases-introduced-after-model-build}

Biases Introduced After Model Build

Component Table114

| Type | Tabset |
| :---- | :---- |
| Tabs | 4 |
| Tab 1 Title | Nested and stacked models |
| Tab 1 Content | Certain applications may involve multiple stacked and nested models. The combined result may be unexpected and difficult to explain. Even if we evaluated the fairness of individual component models, we should re-evaluate the fairness of the full model.  |
| Tab 2 Title | Post-hoc adjustments to model output |
| Tab 2 Content | We might make intentional adjustments to model output to account for other considerations. For example, in pricing a policy we might make adjustments to the cost model to account for changes in underwriting practices that were not reflected in the data. This could unintentionally undermine the fairness of our pricing for certain groups.  |
| Tab 3 Title | Grouping model output |
| Tab 3 Content | We often make judgments about how to map a specific prediction to an outcome. For example, implementing an underwriting process involves identifying a threshold for determining whether applicants should go through full underwriting. We might do this by mapping the prediction to a categorical ranking of risk such as accept, decline and uncertain. Choosing this mapping can introduce bias.  |
| Tab 4 Title | Gaming the model |
| Tab 4 Content | Models can be gamed by individuals with knowledge about how the model makes predictions. This might advantage certain groups with more access to information about deployed models. For example, insurance applicants with higher socio-economic status may have better access to agents than applicants with lower socio-economic status. As agents better understand the underwriting process, they may be able to locate the best price for an individual applicant. Agent incentives are aligned to service individuals applying for higher face amounts, which is a disadvantage to those with lower socio-economic status.  |

In implementing a predictive model, we are concerned with verifying that nothing has gone awry and that nothing is introduced that undermines previous fairness considerations. 

Implementing a model involves translating a prediction to a business outcome. This step can introduce new biases that were not considered while the model was being developed. Even when the data gathering and model building phases have perfectly anticipated how the models will be deployed, there is a risk of unintended consequences. Indeed, data we use to build a model may end up being very different than the data our model encounters in production. This has implications for the fairness of the business process the model supports. We previously talked about this concept – that the choice of data influences our model’s fairness. However, even if we did our best to ensure the choice of data was appropriate, we need to ensure that holds during and after operationalizing our model. 

A finished model does not mean our responsibility to ensure fairness has been fulfilled. Decisions we make about how our model is used can alter the fairness of the resulting process:

### **1.7.49 Fairness Summary** {#1.7.49-fairness-summary}

Fairness Summary  
This section examined different concepts of algorithmic fairness, including demographic parity and predictive parity. Through these different concepts and ideas, we were able to approach different ways for defining what is fair, as well as the benefits and limitations of each method. 

We then defined the important concept of proxy discrimination, and how unawareness impacts fairness. We reviewed some situations where proxy discrimination may impact modeling. Unfortunately, enacted restrictions and regulations, such as the protection of protected characteristics, cannot always help address and prevent unintentional proxy discrimination. We saw several types of proxy discrimination that exist, including causal and opaque, and reviewed some approaches for addressing proxy discrimination. 

Finally, we saw how implementing a model involves translating a prediction to a business outcome, where fairness should be taken into account.

### **1.7.50 Module 3 Bibliography** {#1.7.50-module-3-bibliography}

Module 3 Bibliography  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_m2\_bibliography.pdf\]  
A PDF copy of the bibliography is available as well ( [atpa\_m3\_bibliography.pdf](#bookmark=id.gdb603q2aic9)).  
\[END LINK\]

Component Table115

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  Aequitas. Center for Data Science and Public Policy. (2021, April 2). Retrieved October 26, 2021, from http://www.datasciencepublicpolicy.org/projects/aequitas/. Ansari, A., & Riasi, A. (2016). Modelling and evaluating customer loyalty using neural networks: Evidence from startup insurance companies. Future Business Journal, 2(1), 15-30. Barigou, K., & Delong, Ł. (2022). Pricing equity-linked life insurance contracts with multiple risk factors by neural networks. Journal of Computational and Applied Mathematics, 404, 113922\. Barocas, S., & Selbst, A. (2016). Big Data's Disparate Impact. 104 California Law Review, 671-732. Brockett, P. L., Cooper, W. W., Golden, L. L., & Pitaktong, U. (1994). A neural network method for obtaining an early warning of insurer insolvency. Journal of Risk and Insurance, 402-424. Carvalho, C. M., Polson, N. G., & Scott, J. G. (2010). The horseshoe estimator for sparse signals. Biometrika, 97(2), 465-480. Corbett-Davies, S., Pierson, E., Feller, A., & Goel, S. (2021, December 7). A computer program used for bail and sentencing decisions was labeled biased against blacks. it's actually not that clear. The Washington Post. Retrieved March 19, 2022, from https://www.washingtonpost.com/news/monkey-cage/wp/2016/10/17/can-an-algorithm-be-racist-our-analysis-is-more-cautious-than-propublicas/ Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. Mathematics of control, signals and systems, 2(4), 303-314. de Andrade, D. C. (2018, December 27). Recognizing speech commands using recurrent neural networks with attention. Medium. Retrieved April 11, 2022, from https://towardsdatascience.com/recognizing-speech-commands-using-recurrent-neural-networks-with-attention-c2b2ba17c837 Frees, E. W. (2009). Regression modeling with actuarial and financial applications. Cambridge University Press. Frees, E. W., & Huang, F. (2021). The discriminating (pricing) actuary. North American Actuarial Journal, 1-23. Glorot, X., Bordes, A., & Bengio, Y. (2011, June). Deep sparse rectifier neural networks. In Proceedings of the fourteenth international conference on artificial intelligence and statistics (pp. 315-323). JMLR Workshop and Conference Proceedings. Goldburd, M., Khare, A., Tevet, D., & Guller, D. (2016). Generalized linear models for insurance rating. Casualty Actuarial Society, CAS Monographs Series, 5\. Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... & Bengio, Y. (2014). Generative adversarial nets. Advances in neural information processing systems, 27\. Hao, K., & Stray, J. (2019, October 17). Can you make AI fairer than a judge? Play our courtroom algorithm game. Retrieved January 20, 2021, from MIT Technology Review: https://www.technologyreview.com/2019/10/17/75285/ai-fairer-than-judge-criminal-risk-assessment-algorithm/ Heaton, Jeff. Artificial Intelligence for Humans, Volume 3: Deep Learning and Neural Networks Heaton Research, Inc (2015): https://www.heatonresearch.com/2017/06/01/hidden-layers.html Hejazi, S. A., & Jackson, K. R. (2017). Efficient valuation of SCR via a neural network approach. Journal of Computational and Applied Mathematics, 313, 427-439. Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. Neural networks, 4(2), 251-257. Hunton, S. (n.d.). Approaches to Model Validation. Retrieved from Select Statistics: https://select-statistics.co.uk/blog/approaches-to-model-validation/ Karras, T., Aittala, M., Laine, S., Härkönen, E., Hellsten, J., Lehtinen, J., & Aila, T. (2021, May). Alias-free generative adversarial networks. In Thirty-Fifth Conference on Neural Information Processing Systems. Klugman, S. A., Panjer, H. H., & Willmot, G. E. (2012). Loss models: from data to decisions (Vol. 715). John Wiley & Sons. Kuo, K. (2019). DeepTriangle: A deep learning approach to loss reserving. Risks, 7(3), 97\. Larson, J., Mattu, S., Kirchner, L., & Angwin, J. (2016, May 23). How We Analyzed the COMPAS Recidivism Algorithm. Retrieved January 21, 2021, from ProPublica: https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm LeCun, Y. A., Bottou, L., Orr, G. B., & Müller, K. R. (2012). Efficient backprop. In Neural networks: Tricks of the trade (pp. 9-48). Springer, Berlin, Heidelberg. Lefcowitz, M. (2019, September 25). Professor's Perceptron paved the way for AI – 60 years too soon. Cornell Chronicle. Retrieved April 11, 2022, from https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon Maas, A. L., Hannun, A. Y., & Ng, A. Y. (2013, June). Rectifier nonlinearities improve neural network acoustic models. In Proc. ICML (Vol. 30, No. 1, p. 3). McElreath, R. (2020, February 4). Markov chains: Why walk when you can flow? Elements of Evolutionary Anthropology. Retrieved April 11, 2022, from https://elevanth.org/blog/2017/11/28/build-a-better-markov-chain/ New York State Department of Financial Services. (2019, January 18). RE: Use of External Consumer Data and Information Sources in Underwriting for Life Insurance. Retrieved from New York State Department of Financial Services: https://www.dfs.ny.gov/industry\_guidance/circular\_letters/cl2019\_01 Office of the Insurance Commissioner Washington State. (n.d.). Credit scoring ban. Retrieved January 19, 2021, from Office of the Insurance Commissioner Washington State: https://www.insurance.wa.gov/credit-scoring-ban Pope, D. G., & Sydnor, J. R. (2011). What’s in a Picture? Evidence of Discrimination from Prosper. com. Journal of Human resources, 46(1), 53-92. Prince, A. E., & Schwarcz, D. (2020). Proxy Discrimination in the Age of Artificial Intelligence and Big Data. Iowa Law Review. Retrieved January 2021 Sandhu, J. (2019, April 8). A concise history of neural networks. Medium. Retrieved April 11, 2022, from https://towardsdatascience.com/a-concise-history-of-neural-networks-2070655d3fec Semenovich, D., & Dolman, C. (n.d.). Algorithmic Fairness: Contemporary Ideas in the Insurance Context. Retrieved January 8, 2021, from Institute and Faculty of Actuaries: https://www.actuaries.org.uk/system/files/field/document/B9\_Chris%20Dolman%20%28paper%29.pdf Shapiro, A. F. (2003, April). Capital market applications of neural networks, fuzzy logic and genetic algorithms. In Proceedings of the 13th international AFIR colloquium (Vol. 1, pp. 493-514). Szegedy, C. et al. (2015). Going deeper with convolutions. GoogLeNet. Retrieved April 12, 2022, from https://www.cs.unc.edu/\~wliu/papers/GoogLeNet.pdf Verma, S., & Rubin, J. (2018, May). Fairness definitions explained. In 2018 ieee/acm international workshop on software fairness (fairware) (pp. 1-7). IEEE. Wang, P. (2020, July 23). Car Insurance Rates to Be Studied for Racial Bias. Consumer Reports. Retrieved January 2021, from https://www.consumerreports.org/car-insurance/car-insurance-rates-to-be-studied-for-racial-bias/ Wang, Y., & Xu, W. (2018). Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud. Decision Support Systems, 105, 87-95. Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480. Zeiler, M. D., Ranzato, M., Monga, R., Mao, M., Yang, K., Le, Q. V., ... & Hinton, G. E. (2013, May). On rectified linear units for speech processing. In 2013 IEEE International Conference on Acoustics, Speech and Signal Processing (pp. 3517-3521). IEEE. Zhong, Z. (2018, October 21). A Tutorial on Fairness in Machine Learning. Retrieved January 13, 2021, from towards data science: https://towardsdatascience.com/a-tutorial-on-fairness-in-machine-learning-3ff8ba1040cb  |
| Footer | Panel Footer |

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAAZ0lEQVR4XuWS2w6AIAxDN/H//7hekAhdNfiAL8YGkqWcrIPgbn1Naqg+Acy1ivddz6IBzdv7ouKPEW8DKZVNigDyMYIlETgWS4AcER2ZwQAh6KGstO9HXDUO0Az3bAMWckn+j28/DmwnOAxQNOtD6QAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAAnCAYAAACPB3XFAAAVDUlEQVR4Xu2d3Y8sRRXAj+gVFcWIiiKiC3oVBBURjCjIhQuIgCAofqCIiEQQuKCA8qEyiPJhDAooKogXCUHQgBhMkGBwHyAQY4gxxBCfNj6Y+MCL/4DWLzXnzukz1dPdszOzM7vnl1TY7antqT51vupU9UUkCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIJg2rwgtQ+l9s3UtqV2QWq7VHqsPd9K7eTUzkntitReW/04mALvlIHcQ+aLx0tTOzu1r6R2QmpHp7ZTpUcQBEV2Tq2X2v9S+21qr6x8GowLycZRqV0k85loLBovSu3LqR0nWba0r6X2vf5naw3jOUWqYzk1tV+Z34PJojI/QwZyV5nvqp2CuYZk+7upvdlcIw4da35vw3tS+2NqK5JjWRBsKP4uOZHDKQarh+RtObXLUvtPau+vfBp05aTUPiNV/aQa96RUnf9acXBqX3XX9k3taXctmBwqc5s0q8zfa64tCuj2p1M73n+wjqFyup+71kvtptRe7K43gfx6kmNZEGwoWLUQJIPVQ7Vte2p3pHZ3ar9J7XWVHkEX9kztBhmuqhyT2l9Te6u7PmsYF+NjnJZ3pfYPdy2YHKNkvogLphem9u3U3u4/WMewdeqLBtel9pPUXuKuN8HuEdU7WhBsGFTxY/t0MlAZIiH+rP9gA/MpyeeTxoFt0le5a6zan5J87mkSjDs+qgRUEfZ210nYH5K8hR6UGVfmgNy9zEFl7pOCYDrcKuMny1RJ/Tzx+3JqS9XLraAAEYWIepinrklxsACw7cCqhxVgsHo+L9mRfNB/sIEhmSXRGYdLJR9q3iu1LakdntrDks8WTur827jje0Nq35F8EHt3yeOjCnS75MQzzj7WM67MAbmrzNGHLZLlHjKfLT+T8f0cL/pgv++WPH+HSD7TeKjp0xYSP15uYvuUeBYMwzxhM8Eq4cWBj6d2fWqnp3aJ5APa9u0pVvC/6F/fJPlMFf2vTW0300/hIOi5koMaRnCElIMbzo17EnQoX/Pdn5P6VQtjurjfOJ/xg+rHcwGy+kZqV6f2itQOSu0qyc91oOkHPP8tkvvyM5/f2G+ls1RsZ6hsv5jaD6sfD6HnMJq29khImCPujVy/LuX5OlJyUEJfmAOcnod70c/2KRkqFdbzJQfNH6f2Eal+52GSv+teyas17sGLAowNWZbG15bVBGt0kwoc83aiZBtAf7GLSTHu+JATFR9WttdIlj9zf5dkXWwLesMbeHdJTkgsBCbs2i+w2tpmyTd8stIj2xDbd97ffEHK/mYSjCtz0GoCMufZVe5dZA7oNHJBx0m68QdUBlWmHIVgXpYkVwu5hpzQvzqQIc+lvv0AGf1mLN/JWb4LJet4iZIfslut6A9zi/1uljxnjJdnYyy+0jUpxk3gmDvsmKQNvT0utftTe8526oDdPmUHBFnoPI3S31EyBeYN3bhShhcGyNmf3+tqR+QC9Ge8xCz/ItQkGTeB47nRZRbN/03tEcmxhrFvOHAwt0lOOHSi3pfaPyWvIAFHjeGjiP9O7eeS+yOw5yU7GAv99NAuhkrQpQJUcmb3SQ7GBH3Q79DvtqBMj0n1QDDbFl6R1xKel6QEw/tbao9KVjZ9vmWpluPPlLxCY6WGXH8kWU44Dr+dw/w8INVzNrwd5Y1WYRw9yWdwnpAceLfaDn1wCndKTiLVoHgO35drOA7VE34/bfDxjms8L/30d/qcuqNHhoC3LNmh0IdnYm75W3XuPD+OtZfa46ndI1k2yKgpIW1i3GCNLXinCugxwXRSjDs+kmUfwLBTghIvsPikq45jJL+kwRj8cQZ0FV2yQZif29hmnW+4e0ePgb/h772/Qcbe30yKcWUOpYUM4+0ic8D3bpMsN5KR30lOuBSq6dgzQVxtlerfn3f0qEIAZ2FsfXudfwWSaX0R49WS36T01Pmhp8zv+0v+Zzh4jock2y7PwXg4g+uPIEyKcRM4rVx7eDGFxKgr6v+RNUkr6Dz5l4sAmZ4nZZmqf+dsKz4aGXJ/W+TAlrBJW+3rakeMgc/VrolZjBWdmQbjJHDMBbpEnEA/GTO+6kmZ3jjnGhy7NygE8wdzjUoQyoGgcLYc6MQwOfdBYmADKcr2tFSdOxPF39lroE7KTiLJBIHAn3/jb1FCf8aI/qt1BkdLTrS6NBS7VHF5jeRVJ0GK8fKzOk/AqNVweEY+x5mSMOPoME54VqqOiOfHEftkjefH8dQFCeYO5b5J6t+iYv69DoA38D2k6viZd+bfQh+CjvbTPlfs6JE/Qw4k7qoT/Lcnee65B+CgeK7rJK+0MNq9UvuT5NVpV+O3jBusmV+vm8AK1yc6q2Gc8SEP9KlUuVUnV/rMQ6CgGoE+kFjR7OILW/bBg4DQZJujfAP+RVF/g756f8PzWX8zScaROajcS7SVOSAXtuexD63grNgOMjhXZRNjTbS8PdBHZadoX/S4BM9h/T7jt4zyQ9iu+iGSFnwgerMiOTEEqnv4tjp/tVrGTeD4GyrXHsZfSria0FhJfNXKkMrexzyVKYtSi8pUE8sTJBcxgPvTFMaJnVr/09WOSLp/b35HJhQSfByYFF0TOMbeS+2N7vqGhsDoqyNMPEFTjQxFwbmhyCQldZkuk4FyonQWdToelHaru6bVKG/gS6k9KMNJBqsU3xds0mR5udQnMpMAB3W+ZHnxzFQcLDybBgkcNQ5b5ePnwcJKcEWGk2CcwqjEgUoXc0yCUYL7lb6bIO4rTdzrA+Z3HIy/L31WZNBP+5B4AfNHsliaS+SCfuH4mVO+XwNZqb+F1SJOzMunjnGDNXNW+g7uR1JqZXaoZJvhediW2Gw+a2Kc8WkVoeQUNVGywQ0bOUeGHTQ6zPaZLprsHHMNHbYr/SXJSbqfH2ubTb7BJoTqb2CUv1F07kt0sfdxZA511RvwMkd+BGL0goBrq2vYHPdB5wmuBPQbzeegPtiifb1e8jzYvkWTsjqZ2CSccfu/H+WHSE4YO3NBgkCSyPfdLM3bW+iiTTQt3FN3MJoYN4HDDkp/p3prbYqxninZLn4qef49LFhZlOMvFJ2nnlTlpzKlGm1RmeL/Nkne0txbsiyRKbJV8Dv4H3vfrnaEH2CBpewjOUbvZq4BsqjTn5LvqQN5d+nPM7ZNppviQRe/MLegUH51DSimVTwFw7eJnQfhemesAZhm0QqVFSLCZsWA4lvUiBjXln5DkZmEeYUK5h2pvcxd9/IBZFOaB0Wdrg9+gBHcJGVlRJ49GQ64Fv6ehApj3yL5DAiOt5QAc797JW+b8xxaFbPQ5yDJ/WwfNSTGWkps+c5HZLhioQHerja7QLD01VPaM5JXl/46DT0r6TgyrgvU22U4kWarly1gILlhdUuCaxlnfKWxAfbn5Qr0Z9xetmpXPoFTeBavlzjRngzmU+/BPG/pt5JtNvmG0gKEsY7yN6vBy7RJ5nU6AaPkbmXO7ySI6lt1S02DrOUKGU4AtD82ZOH7Cd4W9a+lvj4BLKHzav12kx9CB7wf4vtKsWS1kMT4OaKtSN529NexPXxbCZ7rBhn21bC/DCcNzOFd/Z+ZO5IyW83SRM3rrs4TNqRYmbLYtahM/RyqT7SovpRoa0ckPUdL/k7uvyKDyulqIEH180Fjnnhuf/0aKSf8XKM4gl+9PrWzJMeaDQvBpCfVLJWAQ6m1VGJnUkvOBvTvvNPhZ671zDUgaHglrEv2dCVig8+8wzN7wycQssIhwFno688UWZgnjAr5WujPqu1Ud13BIZFEkkySQJRgPv04m+B7N0u+L60O20e/n5+9wwM9m3OzDIwXh4Pj8U5vEvDcXast2ATnRUtwLsnaBjLCqSoaEOvsx9N1fNz/+1KW056SzxAyHuvEmxI4bNfrBom0TcLUNglCdbTxDSXdtxWEWdBV5tAkdytzkhsqatv7v6vsrJ6Abod5u1U/QDKpqM9kHi3qX21fvS9BswlNLLA/pckPeX+u31eKJdMCOZD4dIH+dgtf4bnOkeG5ZR51gYJ9+OMn6C2ysHZl58lWnaxMdbEHVqbWv6tPtNutVl9KdLUjEjnGRazy45okyL1tBY5+7GKwMAn6IEAOxVp0ledXUuAdsEWDAc7BriR0tcB/t8kgcKNQ3uAxFII1CrpV8luJoMqPwxvFLpIPbfpABXwvyQEODQW1sOrwq4CmhuFu4o9r4Nl81YjVHJUQP7ZSX4uupn1wwWk8KMMrN8Wu2EvzCcxLk3Fz//uketAc0B1Ntm2fXXf0GPTRCgs/E7T8XOKsVqTqfHXefRXI8zbp7rjHCdbMA4mQB73D0fFfBXuwgVntwwfrOrqOj4DL2LyDo5LKwWR7vlJpSuDQDauXBBUCnfUBOkfMaR1tfAP39kl9U/WGeb9cynPPvXD4JXuvo6vMoUnuXuYW/N1fJL+xbbHJk/UVPAt+wH6X+gbGziLo3P519a+2Mqj3xR8gr9PMZx4+J7GwutHkh2gW/T7v7yyHSZbTHVI9YoA+nCjZXrpUWUq60AR6VvKR+0muEpUWF/B6yT7PV1+5n4+Vdp5AtzPbyNTajPWJitUX4uYp5jNosiNs5QnJ294qA565JwO5oM/oH36aBYtNvBjflZLfoCW+tYV5apvA0dc/Vx1NPqEuD1g4cCCqUMqxMnzuAQigfkVoUedugzMB7XYZbOGhIBrI1UEo/D2H2nE6jOlSGSgdDgDFKCUqfMdb+j+fIfm+rFjsOPm5J/m+o55hUjBeb8BcwxmRVFm4XqpIWfaQHPx65prK6zlzzaPOAQOug6TSJ/HKBZKVXOfqMvOZzgkrVLB9MHbfR50gv/Msfi6RAd9nnSXyQ46jkh7mH73DKHkzry3ogneaTSAnHIMdo5738QnmrBM4gsidkh2Uyh8ulPzP/xBsPE0JHNetE9SVvt3u1DlmTj1qm218A/e099XvqrNVnXcONPu5V3tHx7rYe1eZg5W7srMM5F4HcsNW2A6yiT9oBcf6Zq1isiCzPoRApDLkrU/sGdQedf6sf0WPsTWfdFpKSUiTH/L30+eog/tdJblSSVLyCfMZ92KM6EFbm4FS4B4FuxRURX8p1WdFng9IdUwWdJWE6WNSTQRUbzkOYiuPdp6QGXMFVqbqV0bJFF1Gp3lOReXMvNq4CU12BOjZ85JfRNIxoJPoNfkAHCXZH5B4ooMac9F1kjfiF3K3lcEm6N82geO7S0UOxkseozbEf5t8As9r/cKuqb1DyseG5hqEj/PVFRLKQtmUoO9hgvyK0HOw5L/HiXDvSyQ7bd0CO18GCoLwKD0D17b0f+e7cYoERevYWA35lQ6ToRk/qwQmmGvbpRpk95F8qJ7xY6x+pTVpMG4MShMXGgZQCnLIAQPzCYCFvz9dBm8I6f2WZfhMlUW3UUqKr6C0OANrSDgkqp96bUny21QounKE5ACsAXlJmvsA87gsefwKDvw8GTagNuMnMTlcst6hf23pGqzRGRKGvSUHneMkO2WqBzyTZ9YJHMGO56daQTJxgmSHfqjUrzSbEjjsWLdvuAdBhaTA+wCdU4u1TWjyDQQGa7P4G4KB/y5F5537+blXe+dvu9h7V5mDlbvKnHuMkjtgG9h9qUJH8oQftMFbq+kkcSRzCn01MWYsakPqX8+Wgb+gmsN9eU78a11Q16MXPgnp6ofQdZLAOjZL/kdzt0q+x5L5jGs8Mw25tqVrAkf1CrtGFtjz8ZIDP3KzfqsEz3+RVN+I535PynBFz84T9sJcgZUpOt0kU10wkfAC+vNryXZ5pAzHzSY7AvTXLvx0TNfK4LkY0+6Svxs/jw0D146V/DfIj4pkW7okcEuS780zWrmeJXkOdOzIsMkn2DyAeMV9iTM6JwuLOgmUbxFBiSjxkjTgID3PSvObOJPgJBmddMwKnDBBYlRyuB7A+Z4peeWJobaha7DWikAXbLDFcbPqI7C3oev4CEJtExWlKYGzaODAMc4LzDuBTOfew7Uu9t5V5hr8u8qdoKuJGwHHL0zXGsZDQCMZnTYsiJ6QHJhLiRdJQV2iWaJrAtdUifS8SXJydW7/dxYfLELa2NCiw2KOpJ45I8G2kDs8LvUVyxJdErguWJ/g4wHXZpUHzBwESibP6mMRwdBZyZwsw+dK4DEZ/Btj04IkEqeOYa81rARZ+a13WKmymr9YyhWNEh9O7Uv+4giopnYJDHC/DLa7cBjbpX0w6jo+ko+ujErgOB/1L/O7Bqq2FcRZwLwvy2DuPSykuth7V5mzSOsqd6oj1ibRKWQ9L+gimMpZKSmeNOgelcIlGfZVJMYUE0ZVjzzoZ9tx6/EHW2VsAvul4kYSA1SfnpJu/0TQIsJClAUp1a4DZfgfLScJptJH9astzFPXxU8blqU+HuATZpEHTBWMlAmwDhrHwgSRRe9pri8SlFHZ0mIVbcvIwDPfKtPJ+C16yNSe55kVdl7ZCuDMRReDWlQwUuad8yjIYNLgvK6W4fOLTVCyZ1w4N7Yo9q1+PFHaBi2FbRwWOtg7drGb+UwTOyojwHYJ2yalFyHWEsbCOTOdewt60JPp2jsJRxe5k4hw7o3qljYWzKWtslnCNhtzTTKD70cn7DbZNEEP2SnoybAc2IZn23Fa8NyXS7cEEfaS7A9IvLETEpr1DvbEtipbjzw7c2OhWvuwNG87zwLrE2w8UJ8wizxgqmg2zYoaNPFhe6RLOXmRIKGaRWURh84/KaF78rNE5xVnTLJAsOjqnIJhCGQHyNrMaRuY40k6JBzdNhmcS8Nxs3WySFUGXUhNC2TO4miScl8rqILpIXbiABWxeUjUtaozLai8+S22oDtaKeWIxTzHG/UJs8gDps4hMvgfI1Md4CzAPGTPk2QnyZNG4CWxmmZyukmyI8QBaiPozxpWsayez5P1EVyCtYGKHIe5qWZzDslXtOcRb+9aQQxGQzWFt2GJAZwdWku/QTLAHDKXHFu4p/pxMEcwT8wXVdtHU/to9eO5AV2yPmGaeUAwQUignpG8NUCpexrba0EQzAfe3nlzLlgsqI5QdbsqtVtk8L/gC+YPXsq6TfKZQKq387pDgV+wPiHygCAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgnXK/wHAJfm53cgmGwAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,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>

[image10]: <data:image/png;base64,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>

[image11]: <data:image/png;base64,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>

[image12]: <data:image/png;base64,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>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKEAAAA4CAYAAACVOJg9AAAE1klEQVR4Xu2byYsdVRTGj8ZoVFTUiBM44EwwBIMiOMQZMRLjhFMQQUyIA4mCSHBqjEPUkAgiiKKSLIIDMRtBg6BZ6EZciYhrF4ILN/4Den45r9L1rlX16lXXe0lVfz/46KZu5aW7+txzv3PuLTMhhBBCCCGEEEIIIYQQQgghhBBCdJkjXI+57ksHhJg0C10rXa+6fjAF4dQ5xnV4erEmiyyyR1842vW+KQinxmGuO133Dr5vwqmuGdcpyfWuoiCcMitcT9vcM9klrtdcx6YDHURB2BJktRtc77g2uJ60/wfImRYP+7TkehP4/9ZYGPqmGfVQQUHYEgTgPteFrmddf7muzI0vcG1y3ZW7NldOdH3suigd6BgKwhYg433i+tB1umun63ML75ZxrmvXYLxNHnU9Y93OhgrCFjjf9bNFsVAWDA+5XrDy8aYscX3mWpwOdAgFYQtc6/rXItCKyB7yzelACxzn2mHDS3/XUBC2wMMWQXhVOjDgDNce18XpQAuQWWdc65LrXYEq/w7Xd653Xde7Thq6Q4wkCwKWY5blIpZaBOGovh7N63tcv7t+stnsRjvneYultwgmwesWxY+YR1CZPmERgL9ZbDvh+Z5z3Th7237IkF+4Tkiup9zi+tW1xfWNRXagrUPlTW+xLMhWWSxnLGtiHnK260fXNteRyVgGXnFUkFBhv2Wz2ZR78ZCbLarqqixKkH9lMTHy3OTa21AEPXu7ogOwZP5j1Z6sThCyFFNk5KtnvNGM64LctSIIQjLnyelAi2Apuq7eQkVHUUKFXEadIEwh871howMQphGEy1y3d1i3WU/JipJfrLryXWXjBSE+8JXB1zrU9Zyih3Aci12SIj+Wp8yzFYHHfNHGa1M0ybSiJ9D/+96qixJgb3e3xf1VsPQSgHjDPATm5cm1PPhR/l2KCpN5wHLXnxZ/sCrIgF9a3F8GTVuOZqUBmFXNZT1Cgp9JoN2GeUpWlIzajqO/h8dj2SyCgw4fWXzeS673LPqNZLd9FocUyvac2TPGDx6M6u8ci5+1js2YFlgfPPpai+SQHqfrHZuseqckDw3s7a6jkuv4OHqBZEJgd4RTMX9bPMz7B9fKuML1gU33YZ/l2mj1/PA0wT48YnGcjnOdNP97TVaUcGwrXUKL4A/FQYOyZbUJWYZt84ziONQtuLAMT1n9ar8I2k8PWgRZqvQ8JROT1yeqJm8vyHZKRvnBPGzUs8yWbb+NCw+fiTAqCCZF3SAk279p9VaMuYBloRhDJInzhoe7D78gS+MfFo3PzHuMk9myIqMN/8Ysxz/yzsrBYhJBeKlrq0UmwxOvHB6uhJ8Hm4C9wfqkGbLz8JolJpyDCjSm8W0c4x83q1GEvD342hQmxAMDlRUs06DtIGRC0fLK/DHPmY4Bz14MYJ+YWbre9bg1bw6zlPMZaZFSl8tcd1vz95bbos0gPN71qYVd4ffCP77suiZ/kxApZUHIZCWYMnHE7VuLM4/562TyrMmPReFIHI336yzeyanaABBiP2VBmFInE/JZddtdQhygzSDEonxtw4Ue35NFm9oe0WPoi15tUb2yhLKsspyWedQ6QUiBtdqiyXyrReHHDlJT3yzEEHWCUIiJQpbjhJCWVSGEEEIIIYQQQgghhBBCCCHEJPkPWujObg52lv4AAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,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>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAMAAAAKE/YAAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAABaUlEQVR4Xu3b3YoCMRAFYUd9/zf2BxPBIcOgxKaGA/VdLEtutrYhLaO4LKc85/EggdEUoylGU4ymGE0xmmI0xWiK0RSjKUZTjKYYTTGaYjTFaIrRFKMpkdHX8eAHtZ/iPcaD7yInbTTFaMrM9mgmLv1Kn9Xt9WNiF0VO2miK0RSjKUZTjKYYTTGaYjTFaIrRlMjo6bcQNi6fX9tbA287x3+JnLTRlMjouovYr1m7d6vL15VdwS5y0kZTjKbUbY+u7Yn19iheHE3kpI2mREZXX8TNK3g7KL6NkZM2mmI0pW577Dx2r54KynZI5KSNphhNqdseO7th5/gvkZM2mmI0xWiK0RSjKUZTjKYYTTGaYjRl+mn8yP/2yL89zWiK0ZSZ7XEfD2iRkzaaEhm9THzF9XCRkzaaYjTFaIrRFKMpRlOMphhNMZpiNMVoitEUoylGU4ymGE0xmmI0xWiK0RSjKUZTjKYYTYmMfgJlaxB5c2FThAAAAABJRU5ErkJggg==>

[image16]: <data:image/png;base64,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>

[image17]: <data:image/png;base64,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>

[image18]: <data:image/png;base64,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>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAABiElEQVR4Xu3cy2rCUBRA0dr2//+4D2gysJGAJDd09bLXQPFm4vbAQYJ4u73M4XV78F8VoilEU4imEE0hmkI0hWgK0RSiKURTiKYQTSGaQjSFaArRFKIpRFOIphBNIZr37cGzrvoNy9f24EnTTKQQTSGaw1trdXTJ3Fs/zI+fx6PbcJqJFKIpRFOIphBNIZpCNIVoCtEUoilEU4hmmpCzN+gevd2/WG66LXYvDDHNRArRFKIZv7XWfbTsqF+bajF8Xy2mmUghmkI004SMX7+rZcver9+L9u5qmokUoilEc9nWevy6uJ5ctLymmUghmkI047fW7n249cLyNHx3TTORQjSFaMZvrd19tHthiGkmUoimEE0hmkI0hWgK0RSiKURTiKYQTSGaaULO3qBjPgjmjZxViKYQzTQhh9fv5/bgj00zkUI0hWhuR/89STPNRArRFKIpRFOIphBNIZpCNIVoCtEUoilEU4imEE0hmkI0hWgK0RSiKURTiKYQTSGaQjSFaArRFKIpRPMNT20QoRTXNLcAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAMAAAC6V+0/AAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAASElEQVR4XmNkZMAETOgCIEC8IAuEgpn8H0wyo1jEBBHEqp2AIDMzFkEkABdk/vsXrpQR1fZ/EApZDAagjkeVQ9UOBVi100IQANyFBTjkbvPdAAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAAYElEQVR4XtWSwQ7AIAhDQfb/f9w5lykWMz14WdbEqH1QPKgqc6XRYH0Bj3bgV+e6O3RHElrhMnYf9plFVhboHjoRWYT2NLsYmgCB8sw7ch47agl77EuZw5PdKv3VH9qHF7blCz5mwNFJAAAAAElFTkSuQmCC>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAAC5CAMAAABDc25uAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAABZklEQVR4Xu3bwQrCMBAAUav+/x9rhe4lpARKskxdmHcQycVxoYtW3LZHUc/+oAzLeZbzLOdZzrOcZznPcp7lPMt5lvMs51nOs5xnOc9ynuU8y3mW8yznvfuDK9J/Q937gwvqztxynuW8qd0SZhZCI2b2OR5nllXdmVvOs5xnOc9ynuU8y3mW8yznWc6znFe3fOGuxcmreR53Iw6D41V1Z245z3Je5m6JxRGrpF0oh8StEurO3HKe5bzM3RLaDdMcpKs7c8t5lvPyd8vpE0scpG+YujO3nGc5L3O3DG6stF+SEjdM3ZlbzqtbnnmFDi6/wfGqujO3nGc5z3Ke5TzLeZbzLOdZzrOcZzmvbvnCXYub3/TNL7/Acp7lvKnd8u0P7lB35pbzLOdtM39Y/wt1Z245z3Ke5TzLeZbzLOdZzrOcZznPcp7lPMt5lvMs51nOs5xnOc9ynuU8y3mW8yznWc6znGc57wfrPRCDcVFUsgAAAABJRU5ErkJggg==>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWgAAAFoCAMAAABNO5HnAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAADl0lEQVR4Xu3du2rDQBBA0SjJ//9xHkWKDELGuNDRgu6pzKLG19PMgvC2vUV43x/kHIVGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umjkc39wirX/y+9nf3CGJhopNFJopNBIoZFCI4VGCo0UGik0YlbwiSy8x+ZUff1/JBcETTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihEf/S/VMf+4M/4y354aWHr9REI4VGCo0UGik0Umik0EihkUIjhUYWXMHn+jw27AfL9rDe3j000UihkUIjhUYKjRQaKTRSaKTQSKGRQiML3nVM4/ri+K5j6fuNqYlGCo0UGik0Umik0EihkUIjhUYKjSy+gh/v3cN8YOl1vIlGCo0UGik0Umik0EihkUIjhUYKjSy4gj9Yu48X7Pnw+Hz88JWaaKTQSKGRQiOFRgqNFBopNFJopNDIgiv4S+vzSw9fqYlGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNOJfur/pT3vTr+0VGik0Umik0EihkUIjhUYKjRQaKTRi7jq+9wf300QjhUYKjRQaKTRSaKTQSKGRQiOFRrZtf5JTNNFIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGCo0UGik0Umik0EihkUIjhUYKjRQaKTRSaKTQSKGRQiOFRgqNFBopNFJopNBIoZFCI4VGfgH/XRHhOontOQAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAAeCAYAAADnydqVAAACFElEQVR4Xu2Yvy8FQRDHR4QQhUSrxB+go1T4AzSiEX+HjkqnUKq1epVEwZ+gIqLUIcSPIEzu9r3vzdu992537t3lmU8yeXffmZub3cm7vVsiwzAMwzAMw+jD3Z/9gJ0U3YYPN1lf0vHHJ3X9TbJKxTrG4RxrOxI62xP434XvX7BD2WCXpIO6DW4aX0MeQJ8GfRd0eQ0T0mPRzFUboUH7tGHzQf76DkBfEz5s8Dfob7mmiXa+WvBNIJ8vCq0JsFnILehjwsfI69xjfbYToYOsq5U8UrFQXo/bUrhsVD/d8UrFmLLYFOrKycZPH3e8hwExcBJej+fz46pMUu9k9rNBkPHPcL7hggLE3K8q2nk5371HS6buiYhF1sWDl1oIfnEcNDYW7bza+Tq4x0HbCDUopCP7VIwri+2HW7aqWAwp15ZSW+JEQhM2VeJzsL6d/5bFpaCdk18YX6hbr3xcR5M6AcNag5FBfMw1nPtiU9DMV0d9HTjxhRRbQFljQj63Y4Vg7JXwpSDvE8sx6eXqYZ2y5NrfiBqEmngJ+groE7l2CBrjvg58uVLQyqVdVwGXfEY6WgA2hY3fjM+F5sB1+QZ0Zg588roUtPIwri7eYOJxurV4GYOqsinMtyvUJNiQLcq+g9nOMChHjqXMx7ZQiIhDs8HMKWXj45063n0bebT/cUbLsAaPONbgEccabBiGYRiGYRiGIr/WjR8E232n6QAAAABJRU5ErkJggg==>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPoAAAD6CAMAAAC/MqoPAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAABtElEQVR4Xu3dwWrCQBRA0dr2//+4tZtMoQMlIJOBcO7ZiJON17d4YhAfjzfV+3zgKF1Uuqh0Uemi0kWli0oXlS4qXVS6qHRR6aLSRaWLSheVLipdVLqodFHpotJFpYtKF5UuKl1UughO/5wPXrP3J2PP+eAl8NRLF5UuKl20aK8PazbubMzn63hc8ykCnnrpotJFpYtKF5UuKl1Uuqh0Uemi0kWli0oXlS4qXQSnL77J/J+Pv0/H3eLh5PI14KmXLipdVLpo014/NvXY39Me/7VnoR/gqZcuKl0Ep29aboexvObltnWpDfDUSxeVLipdtHevz/t8GOdb9zs89dJFpYtKF23a6yd3kacvqefL14CnXrqodFHpok17/WRTn1y+Bjz10kWli0oXlS4qXVS6qHRR6aLSRaWLSheVLipdVLoITl98k/lO7+SdXutipYtKF5UuWrTXv+eDG4CnXrqodFHposeav4C8I3jqpYtKF5UuKl1Uuqh0Uemi0kWli0oXlS4qXVS6qHRR6aLSRaWLSheVLipdVLqodFHpotJFpYtKF5UuKl1Uuqh0Uemi0kWli0oX/QDJSxEFsZZbQQAAAABJRU5ErkJggg==>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAMAAAC8EZcfAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAABRElEQVR4Xu3azaoCMRAFYUd9/zf2B3thIIwDSUU9i/oWco2LWzY2OuK2nbKd+4M0BlIGUgZSBlIGUgZSBlIGUgZSBlIGUgZSBlIGUgZSBlLxgdf+4NCa74sf/cGR+AkaSMUHji1JGXqNNzWK2+tmaNXiJ2ggZSBlIGUgZSBlIGUgZSBlIDVxTdK5vP+qC46PZ5PiJ2ggFR/Il6TWoLairUZ7AIufoIFUfCBfktI2pd1dI36CBlLxgYuWpHsTqbtrNiV+ggZS8YF8SfbeP9qnL7wp8RM0kIoP5EuytwZ7Z5PiJ2ggZSBlIGUgZSBlIGUgZSBlIDVxTfLb5/Tb/zbBQCo+cGxJ7v3B98VP0EAqPnAb+t36H8RP0EDKQMpAykDKQMpAykDKQMpAykDKQMpAykDKQMpAykDKQMpAykDKQMpAKj7wCXqREFF/qITGAAAAAElFTkSuQmCC>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAMAAABOo35HAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAC80lEQVR4Xu3cwU6DQABFUVH//4+1rgQD1HCTTiHNOcspm97O4i1Ip+mNo97XB9wnViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgVvC5PniEK/zb22198ABuViBWIFYgViBWIFYgViBWMGSULkZMwx3zT/41H40Yxm5WIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWMPht5f98rA/+vmz869BDz+JmBWIFYgViBWIFYgViBWIFJ47SeVwuw3Nngs7O26IzNysQKxArECsQKxArECsQKzhxlM6WubkdpReYogs3KxArECsQKxArECsQKxArECu4woLf7vbF8tkFtrybFYgViBWIFYgViBWIFYgVnDhKd7bodnjuvAexfehZ3KxArECsQKxArECsQKxArODEUXpoXB566FncrECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArECsQKxArGDw28qv9Vu81rcZTKxArECsQKxArECsQKxgyCj9Xh+8CDcrECsQKxArECsQKxArECsQK5im9Ql3uVmBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWIFYgViBWMEP53cRadfISnkAAAAASUVORK5CYII=>

[image28]: <data:image/png;base64,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>

[image29]: <data:image/png;base64,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>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH0AAAA1CAYAAABsi+QkAAADT0lEQVR4Xu2b26tNURTGh/ud3MmDQ4ScpEQkd8oDSpIiPEgU5ZJLitoJRQqJRF48iSRRSHkiHiVJyqs3L/4Bvq8xV2fueba998O2z1prf7/6OmfNtc5pn/WtOeYYY65jJoQQQgghhBBCCCGEEEIIkS/GQ5uhQekJUU76QUegW9DQ5JwoKQugDybTO4YR0Ikgmd4hbINWQrtMpjdFf2g9dM58TTwMDau6It90mX/ugSbTm4I36iR0Knw/HLpnfvOKAD/zUWh6OJbpDWC2uxN6A02Lxjnj71gxZvsqaGt0LNMbMA/6BO1Lxmk6H4SJyXge4d+wOlIFegRtsJ7ZLwIMixfNzZ2anKPpfBjmJONFQDO9DvOhr9B5aEA0zpDO0F4004dAy6H70CtoIzSu6ooOh2v5ceiPeRiMYUjn7OeNY0tTlIQJ0EvovfVe99jV+m6ewTOTFyVhEfQT+gW9hV5HYhuTEeCseUSI6YaeWfX1zeqKeddM9BFMdmjssWSca/sl6De0LjnXaiabR5UiaLCVAGbntdbzLOzXyuhbDU3fVBAV3nSWMixpPkNzk3NLzMM+k7w0tIsCk5VkafOFoZ3l20doRjQuSgBncMV6l2Q0mobvD9fUotvak8ixokiXnnbAuv4aNCs9UQbYdo1N5yw/Yx72mzXmf8Emy1Xzz9MueB/4sN+A3llJTeesfmE9HTduWjw0T676Gm7x/rDWms4MfE86WAPeDyaypTSd4XstdN18H5qlWx5allPMk0guBa00ne3ZZn5fqU3PI1xiDpjvmrGkjE1iBLoMPYH2QgfNew0XzB/aeO+gFjI9p7BLuNs8CqWms1ZmZKqYr7nZskQzmXzODMf/QqbnkNHmb+6MDcep6TScxj42n9lZdcHZ/twabwzJ9JxBA7ebG5ORmk6YjH2BloVjZvnMttOt4ZHm4f90pJvQ02SMmh1+JkOmtwkattCq3365C90O37M1TLZYdXuYFQhD/RrzB2ZSGK+FZnoBSGd6thHEaiN7I2aH+WtRXebVR73+gkzPMaPM63T2EB5AK8zN5FrP8MzMPYNZPvf8+YBwz6AejUznUrEUOgR9C18Xm/4frtA0Ml2UkDHmy4AQQgghhBBCCCGEEKLj+Qs4hKfcjnOVIAAAAABJRU5ErkJggg==>

[image31]: <data:image/png;base64,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>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAMAAABHPGVmAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAA3ElEQVR4Xu2YywrDIBREY9P//2P7IPYhFvSeYmYhcxbB3EWOMwQJSWk7n0s7OANLEJYgLEFYgrAEYQliHcm1HdSQL5l7O6iQJJFIunVt/RZePPeZ+9VKkliCsARhCWIdyeiA/LIf1/yzDiBJIpHE68pHS6WochtGkkQiide1vRsrC4IkiUSC6vq8WjtrTJJEIonX1ZxdpDFJEokkXlddTriogiSJJQhLEJYg1pGMDsgpm5jykBESSbeuWzv4E0kSiST1fiHNQpLEEoQlCEsQliAsQViCsARhCWIdyQNySA/ZGfANuQAAAABJRU5ErkJggg==>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAMAAAAPdrEwAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAAyklEQVR4Xu2X2wrDIBQEtfb//9heolTaAe0pdimFnYeQHMi42SAhOScVJw6+h9XAamA1sBpYDawGZw4G0Y/mlYMHwtRC9byQtHjWzj1WXRQnTG01sBpYDZYbfVCOQ+XpG4SphepYIfXooVXRr0L8PHVL2lMHIydpaqE6Wsh4hyXciTC1UB0r5HWjl1glwtRCdayQpwJCXTSEqa0GVgOrwXKj7627d/cSoXpeyIWDTxGmFqrz9Gd1G2Fqq4HVwGpgNbAaWA2sBv+pvgEVqQ/FX+96uAAAAABJRU5ErkJggg==>

[image34]: <data:image/png;base64,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>

[image35]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQQAAAEECAMAAAD51ro4AAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAACQElEQVR4Xu3dy4rbUBBF0e0k///HeTSHaKIQDI2sYLL2xPhq0iwXqMBq/HikL+eD/zEIQVgQgrAgBGFBCMKCEIQFIQgLQhAWhCAsCEFYEIKwIARhQQjCghCEBSEIC0IQFoQgLAhBWBCCsCAEYUEIwoIQhAUhCAtCEBaEICwIQVgQgrAgBGFB+Ojb+eDT3f9fpj/PB5/NJARhQQjCghCEBaEr94Sjy+7ef3R8YN9/v162mZiEICwIQVgQgrAgBGFBCMKCEIQFIQgLQhAWhCAsCEFYEIKwIARhQQjCghCEBSEIC0IQ1vUPafy1r6f3x7MWR8+uvy6TEIQFIQgLQhAWhG7dE477/rEPnPeCo/v2gyOTEIQFIQgLQhAWhG7dE47O+8LR/fvBkUkIwoIQhAUhCAtC/2RPOO8HR8f5/fuCSQjCghCEBSEIC0K37gnn/eC8D5y/jzhff10mIQgLQhAWhCAsCN26Jzy77z+7/rpMQhAWhCAsCEFYEIKwIARhQQjCghCEBSEIC0IQFoQgLAhBWBCCsCAEYUEIwoIQhAUhCOv6hzTekPUN/+TrgxCEBSEIC0IQ1nV7wo/zwftkEoKwIARhQQjCgvDR47Kf6X7jTEIQFoQgLAhBWBCCsCAEYUEIwoIQhAUhCAtCEBaEICwIQVgQgrAgBGFBCMKCEIQFIQgLQhAWhCAsCEFYEIKwIARhQQjCghCEBSEIC0IQFoQgLAhBWBCCsCAEYUEIwoIQhAUhCAtCEBaEICwIQVgQgrB+AQo5ERlSketPAAAAAElFTkSuQmCC>

[image36]: <data:image/png;base64,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>

[image37]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE4AAAA1CAYAAADvT90fAAAC9klEQVR4Xu2Zy6tOYRTGH9fjEuK4hIHICSkTh5RCbhOZSLmViSRRQuRaEk4kl0JESiYypZAyIgYGMpD8AWYm/gHneVr77dvf++1vb6ecst+9fvV0zn7f7xvs56z1rrXeAziO4ziO4ziO46TACmpLvJhjDLWPWhBvNJkl1CmqJ96ImEVdpWbEG01kPDVA9UXr06ib1MJofQ11lBoZrTeOldR5alT23Evtp25T79Fp3CSYofOi9UYxgjqL4rNtEfUKncYJRdyOeDE1lFIbYVF1hDoMS0+h6LkDMymmzDil6yUknK6jqRPUyez3CdRDak+2r0P+ETU7e85TZtwyWLqGP0BSKA13U2+publ1Rd592EvLnKfU1Nx+oMy4su/VHrUYX2C9Vx4ZJzMVbWUGNNI4peVlmEFxGso4GaqXV2V8jGIDqox7QE2ON+rOUuobdRGtNkMoPZWmwTgZ9gTdzelm3GrqFjUu3qgzOtuOUX+oTdGe0lNR+BrWr42lrlOr8h/KKDNOxUXVOSmmw174AzqbVFXDH7DKqgortqHdhB6YkYeo79lPzbGaVYXMHqD6s+dkWE79pH5R76g3OX2EReI5WGQKVVxNCVOy5yrmU9eQ4PmmNJI56u7z6Ky7Qv2mNkR7O6ld0VoRKjrHYWdccqhqFp1vIYWLKq0MOQhrYbqhCF0HS+0QrcmgKneX+kotjvY0zCuFVTiKXlzjUzj3itB3tF/03doT2o3Q4AaUpmpNPsHOKCdC0XABrXYjILNkmq6LkoyYf4FGrLxxirbTsBSeGD5UgSI3yQG+DEXXS7SuitZSz2DX3n+D2pLnsNRWz9YYlIrrYSOR7t/Uluga3HH+L1SFz8BudpWmSQ3ww4XmU5mmgV5Twefsd6eCmdRm2Pl4AFZMkptFhxNV0RvovMdzKpgDu1HZHm845ehKSuebbpCdIbCXeoH2cc2pwM+3IaAqqhFLpukmWLfEW9s+4RQiszTX3oP9Z143wbrUdBzHcRzHcRzHqRGDn+VmEfkFEQoAAAAASUVORK5CYII=>

[image38]: <data:image/png;base64,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>

[image39]: <data:image/png;base64,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>

[image40]: <data:image/png;base64,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>

[image41]: <data:image/png;base64,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>

[image42]: <data:image/png;base64,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>

[image43]: <data:image/png;base64,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>

[image44]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAesAAAAsCAYAAABFaZAZAAAOCklEQVR4Xu2d6askVxXAj0sc14hrZhzMTNSgIeKOviAaiRgNghqDJhNFCBIm0cSo0TjjKLZLDOMWjRglEScxwXHBjQgqIwxIRBEREZHgp/kk+CFf/Af0/jx9fPfdrqq+t7u2rnd+cJh5Vf26us69Z723+ok4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juPsJh4Z5PHpQcfZIB4zl6nx2CCPTg86zgbzCNF4w79OAU8IckuQC9ITEwXn940gV6YnnI2GefyJIOenJzaYi4LcILsnWGOT2CY26kyb1wY5LLtnbq8NivpQkIvTExPmcUG+FeRd6Qln4zknyBfn/246JM+3iiYhuwVsEtvERp1p8eIgNwZ5xvxnqupDc5l0hX2WaBaKYzoT5D9BfhXk40E+NpcTQX4tWm2c+7/fWuRS0d+Jsxucw7VB7g9yWvQ9HhS9Vl3V8irR1/I5fi967VfseMV4WDdY7wkyE71P7vdHQZ4cv2BikMhxj09JT4yUS0THZ6iMnXn/ySC/FZ0fD4kGXbPLL4ja1N2ilTNLUClnB/m67Ox2mc0zd3lv3oN/+Xkrel3Mc4L8RPRz/DnIySBv3vGKcbFusH6pqB88I3rPb9lxdlowNx4I8rz0xAghGM+C/DPIy6PjxJrbg7woOjZZ6Ptj9P8O8urkHDwpyJ2iDoO2Q8wzg3wnyHnJcYOg9DXRST+T5uyHc9cHuUu2M6c+2Sd67SodpKwbrI0XBPmrLNdNm3AdEqb7gjw/OdcFjCXO/i/Sz/XagHn7JVmc733zHlHbIVlO5wcB+t1B/hXko7KYWDA3PyyLvwcc4xzvje0v22tyWZBfiAbuvsHWSPzRQQ7rBmuwwIBtYqN9UeKD1gX9kMwxB/q43rpQzJDwV43tK0XvJT0+OZ4lWtEi/L8KMhkyGqrduKX29iCfCfKo6FjKG0QnxCnRyViHtexIDvqCoIUTwEDukfyJ21awJmvvK3uncvq06L0y6fsInji9m0TvsW/Hty6vF83YCdxDgE19XlR32FAV5sD+HuTC6DgdjHuTYylUIv+Qxd9NsWWB/emJDnlikOuC3CFqZ3xGOg05tBGsTa99dLxW9UHr8lbRAo3rDZ2U5oCv+pOoXaYQk9AfQXvS4MQZtKYMG0Xh3FGWtUwwhm/K8olFgCZQc40qRcMY1gm5j1xDaSNYD5W9A5+7j2BNAsZmH9qtubodC8zbH0j3OqqDgEs12zQ/bB6i23izI3rGNpsCFg6O5JvffW9yzuA1JNCM41A8TbQt3WewHqLjBSU+aB32iiZC3xe93jp+rC9IWNNiMYY5XNWBmhSHRQfsaHoiwgL674IcmB/Dif1Y6qtxgwqB6ptrUCmkVfgYHAKUGEobwbrP7D2lj2CNjj4ruinEAkofHYS2sMo2DoJ9YpUvAbturd8CeqxbnBVOC7teBg6O3/2uLHa0xrJxdIhg3WfHK6bEB60K85puF9dAp1yPcR47H5T6Yg+wF5LrOlvZeHim9CuiA1bXagML6LER8Pq7pb4aj2FipMEexuIQoMRQ2gjWlr1XJTBd00ewZuMhwYC11ZlsTgYfw5rxEOMDFjCarm8BPR5Lgi7BN6e1aR2zdNMOAX8su2z7DtbW8UKvfW9aKvFBq8I9HRP1vbYnIle3Y4a9MT+V/sesN7jBU9LcaiNTYYPQGdk5iQjgM8kzZnsPJgbr3DAmhwAlhlIarOkeoC86DASwm0U3Bw2RvUPXwZo223HZznLp2nCvTd2bLtkT5IogtwW5SrTyZJ2WsWjaNEXAq6o6u8YCBjrDoVYRbxJjg5kFdDpdOK06e45BL7YBlPcyOyR5JolON60NQZfBmvul80PBwlzgGm+S4TpeJT5oFayLeXD+M10jrjfUc+mmfzZzMs+PBHmNqE+kGCyJC7ZRuqno3Ghs41hdq42qiCDzsKiTi5XHxM5tn8SOBeeAkxiTQ4ASQykJ1qzDszZEcLZHbAgC6H2I7B26DNaM9fWyU49cD93O5uf7BAf11SCfkm0Hfl6QP4h+pibjxj5+Lhow+sSWSOhGbSXnjJeJbrzi3uJ1PMaUz3wgOtYEyTN6IJnGB7AchUOvWxvsm66CNfMQn8ZS3v75MbNr9NHU0eiKEh+0CgTBdG8D1yPI5XRI28T0/zPZnqtx8liqf+sS5/jkjcScaKoYAuhzRTd9Yfg4htjJlgQrg516BCiCxOWymkOgwmEw2bBUKjijpuBUYii598/9kbWmzsM6Gk3Z+wtFdZ/eR47wHG6TbrsM1iQfJGZxEkZygm5TPcR0MbZ8Bp5LJhndGx238VumA879UhafQ+1ybIDr8tlOy849Idggwesa0SWlq2Vxtzrzl+CWm2BY4kJi8A5ZbaPnWaLftZDea44wNk0t+66CNcXC32Tx2tYarut4dTFPjRIfVMp+0c5ePPdsKa5pvnQ1tqb/S5LjFpOW+dYqmCNH04NTwDbQoJj7ZPsLF0xwBGQ8Vg3G5AarGKsWuB7ZVKlD6JoSQ8m9f1prOMF0Y8SQ69XQVbBGLzNZfMxnS1QPfbeUrYPBOMTkbu5DPzidtvW0DKp95uKDoi372C7fJ1rxU0lUURqsrSLhegRtKusx0UWw3ieaLJ+QncGLZGgmw3W8SnxQCfgYNmil90QSyhM+aVLYNXw/B8luqn+g25ruociFOZI7TzYKWl5kPk2ttjpyg1VM7BSaWo9DUWIoOfePfsmkcQo4hxiy9qbsvWu6CtY8u3lSFhO/46IGWBJE1sVaalWOl585PpPmtvxQwZrqgPmxSpVQGqwBB8n1DqcnRkAXwdpa/6smcV1R4oNK4BvxKJCOyE67nIkupXThC5ow/afzzTZH4jNX+WKsyQZrc1irZFWrrA88XbSlGD+rPSZKDCUnWNt+APQUV0EEB6qlqiDSF10E6/2ihlLlJA+Itm37HHu7ZpXjzU2W0E/J+m8bmMNaNaktXWe3ubxK0t4HbQdr811V1ZstPwzV8SrxQbmcLaq7quCXszeibZr0bzab+sxcSvZRbRTmsNZRTEnmb8lB363QXEoMJSdYXynV2ePQ2Tu0Hazr2myGOdw2r7kMnA9OKHW8tvzDMsSyHdPMhdIqdV3MYSGrJAnol6Q4NykiUSdhXyVp74O2g7V1FKvuNzeJ64oSH5TLIdHHKKswP9b2NZto0r8t/9Q9AdFEjk/eSGxtpiqY5IJSUkfYhAWvdb5lZiybO3ImBud4v3SDRZq9s5592Y5XKF1uYmo7WNNmu1nq54I9VtGk37bH1sYzNfw0WeL3btzxim1wHlWOv8uxsc14qya1BDd2ONclTimW1FTdZy5dbUKCtoO1vR/zMd4BnXa8GCNaxVSmMW3P05gSH5TDwSCfk3pdxHGgzpe1PbZ1+od4vZrPfEyqn1KqwjpSbeluNJjDqmpF5IKR/1DyqsN4M9tQWesySgwlJ1jzPjjB+P0wDnu+mt/l549IvmNtC67dVrDGmd0u9X/MBeIMfpXW7ipYUpSOEbtPmfczUf0zH+vmJM7jaHqwY2z9eNV2Hs/L8gRC3T2lkKyvc72uaTtY21xMX7NXNLhwLa7J/CFI1SWgXVDig5bBkxAzWf592eh1naKtlGX6PyXasj8gmjzldn15PevyuR2ljeFC0Y0FpphV2Cf5351MdkRWmdN6HIoSQ8kJ1twzyYxtYiEwvG5+jGBBxokOb5XmSqsL6oI1jonHrvh8PMazjD2iwSw1vJQ4g08r3a7gs/FlCzyuYg6XivikbP9hCF7Dvwfn52NsjPtKLoB5cEKqOzIlMOdyOljcP1XiutfrkraDNbARksoP+wOqMoqJ07Jd8V0ji09xdE2TD8IesUvsc1kCwRM8FAUshyxbwrFH1WayfL60RZX+j4v+uVZLli6fvy4XdHavrNaNGh0MIApg0hMwUNZvRJ+rvFbKAwYTBkfIzr46aI+SnaJErkdygCF9QHT7/tCQzbHWik6YKExa/uVnjnO+ipxgDc8O8mVR/R4TNX4yRbJYfp9jfVXV54u29WiLkTRxrw+Ijs91on/pKK6Am9qwVG/vl+0vFnlY9D7TMaWFxvLHPaKO8EyQP4rql7nRNU+V7bFEcGA44reJfiYSDSrQKidFp+B7sriTvwtIIhibb4s6WOwE/d8izd+wVgfJODZX10LkPXnvtq7XNtjIIVGdMAZ0qM6I+iqObf3/lYvkBGuqzqtEE2WCMvdN0YKNoAe+Ee4GWXyGvQtyfBDzk+SLc9hRutZr4OPfKerXeS16u1+qx5RvartT9LUPzQV9cLxrUv0fEb2nWP9IbkxCPyQxVhg5FdBiuUvylToVcoP1JkJb+yJRQ1qWlU8ZDB8HUBXIxw5BhqWJvivDMZATrDcR7uclot/El3bEdjsk1CR1JNhODTiF22S8LbSumHKwBvYhkNnXVdZThw4BSejB5PgmQefiDple0FrGVIM10HGwKtTZhjG/STYzse6VC0Sz+HTX5JSZerCmNU+bezdOfu6Zqvrq+f83FVqNtHcvTU9MnCkHa4I07fA+2vObwn7RDZXnpCecai6Wcf1Rjq6ZcrBmDMned2urbUpzmeUpljNIqHcLUw3WJI6s7+62LmYTu3F+rw0TiV2zb0xPTBR7PIbNU1PjChnPny3tm3NFq+opVS5ssuM58rrNZlMDm8Q2h/iTj12yJdNJItuAzXR0v9hM6TiO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziO4ziOs3v5LxpBbymjSckQAAAAAElFTkSuQmCC>

[image45]: <data:image/png;base64,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>

[image46]: <data:image/png;base64,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>

[image47]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAAArCAYAAABxYspKAAADwElEQVR4Xu2a26tMYRjGH8ftEHIWOaaQ4oILpSgiUpSSpNy4kFw4FW2lJqeSnEIpyuGGiBsKKUopSZILF672lTs3/gHep3evZq01s9aeNTN75rP286unPXu+tfes9X3v956+AYQQQgghhBBCCCGEEEIIIYQQojFGmXabbps+mN70/+Tva2LXxVlkem76a/pqemTalrii+6w3PTVNTg90EM5Tr+kFfK5+my6bTvbrnOklfP62mHr8z8rDMNMx+MPfMY1LDtewFT4hnLjQmA43+m+mJamxbrAOPq/cqGNTY5z3DaY+0zXT+MRoCVhh+mn6YVqeGosz03TJNCc9EABcpMPwRfxuWpoc7goH4PfDn/UYbbpi+mPamBr77+EuuQefgP2psQhec960LD0QCLyvW/AwzudYmxzuOGPg98N7ocfK4jT8GobL0kFj4sM9NE1IjY00HYXnKyHC0HLWtBIeavgc2xNXNA5zsQemxemBgsw2vTd9Qfb/ihse57d0MAdhLvLLtCr2PsPKnn7xdYhshm+K4aYKfJH2xi8owFR4At1qTsY55FzW26QRkeEx/HXbsw4KrECuwxeEiXtkQPRO3EX0ViEyy3QR1WqPYaSVcNIuo9oHv48KsjfjTvg1N1CbyJeG6CFZQXGRmKcwjwq1MuFiHURyl9NDDbSYebTDqKIEnPfBtk095pnemZ7AC6DSstD0Ce6Od8ErvaIPzP7XKXjCXFRsVeQltWlYtdKrxr1oXhnfCO0wqmmmV/CKmvcYZxK8t/cRHgFC3bBtI77DaFyhVnqEBlNBbXuDjVtuirxcJo92GFW8RVNBtelJ0ZDoWUtvTHH40DSqrN5KKOyAL358wSjmV0yQX8MNpCjtMCqGPM4hKztWeEMa7n6GDe70rKOaEKB3Yn+nXnibDw8teaX8FNNN1IZfinkOjTI6ukrrsWkBshlhuoD/Y2N2hKjEpfg6RLhoR1Cbq0TQ09BLNXtU06qnYs7Es8d0a2bIEuUjzSa5ZLAT9dWm43DjqgfPLnmGSU/RTO+nVaPi8RCPiULemB2F7pqLEWp3d6LpKrxKzSIK4XyOTamxRmjVqNjJ52ez4GHhM6TpQbX5OZC36Aa8v14M7EXZm6rAn4MNyKK0YlT0nmfQ/GeXBn6F5YTpLry38hZejvO9EL7ewurpELzFwcWKvps0I34Rqt8Puw8PPX2mz/CEniGzUZoxqrnwfhk3JeeQofwZPA0o8tmipDRjVELkwryNR1P0PkIIIYQQQgghhBBCCCGEEEIIERz/AFSRxSzSe6QnAAAAAElFTkSuQmCC>

[image48]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGwAAAArCAYAAACdO20ZAAACcUlEQVR4Xu2Zu2uUQRTFT3w/iCDBB1qESCCKYAotBEErBREUBAkSsEkhkiI+QIkQWAgWQVQsBEFBsbEQrAQVC0EQRESCRYpUVnY2+QeSc7i7yfdNNsQgkmE8P/ixm72zsJN53DvzAcYYY4wxxhhjjDHGGJMH6+kAfUw/0ffNV/19tNKuyj76ms7S7/QlPVNrsfqcoK/o9jRQCh30OmIQntAt9fAiTtM3iMHLjR2ICTVJ+5JYURyi03SKHkxiVXbRu3RvGsgATbwRxMT7QffXw2WxlT5DdHYoibVQmzv0QBrIBP2uR4itXf04Vg+XhwZKHX1BO5PYOnoNkR9yZDMdp/2IHKx+nK21KBDt+dr7f9HDlc+11Vxsqvc5cgox4dbQBmLABqsNSmQjfYjorIqQ1uBoVWl1aZXlyG46gYWqcBTRB70Wz3lEZ1Vp6R+gvKC8pfyVI5pUV1DPV1pZ6kOjGS+aHvqFztALiIpQleFK0PnuNiL5r1QdF47jz1F1q92guvr1fQ2YcplyW9FsoPcRHdbA5VoRCg1GA4uPGDr0a8K1K56KRPlKA3Y5DWTGOcRNy61E5TMVTu9o13zrQtGs1VaiGbrU9VQOaFWNof2W100/02+0N4kVxx76sane58haehWRv9qhVaXVVfz1lGjt/3+TsP910XGE3kAMXDt0F6o70f/itkN5Sx1VHsuRbfQBoppdita2rn6cTGJFUT04LzfLVwP9vlEsv/p19mog+nGpHioDPSa5SZ/St/QDoiTWZzk8QtlEhxHHDA3Cb3qP7qw2wsLzveeIHPyTfkUUJ9pGjTHGGGOMMcYYY4wxxhhTNHPECXYU/10U6QAAAABJRU5ErkJggg==>

[image49]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAAuCAYAAADjs904AAAC10lEQVR4Xu2ZzYtPURjHH+/GW0njdSGaQooFC6UoRUlRU5KIzCwmWTCmhlHqV7KYhCyUomg2FkpNTSGLKaU0TZKFxaxmZWfjH+D79dzfzLln7ozfLzMc934/9Wlm7jlN97w+zznXTAghhBBCCCGEEEIIIYQQQggh5oxF8BR8BN/BN9lP/r0vqBeyFb6EP+BH+Bwey9VIg4PwBVwdFxSwArbED8vEPHjVfNAew2X54ikchUPmg50ireaT8BPcFpUVcRP2xQ/Lxi44Br/AnVFZyDp4B26KCxKBk/Wy+WT9DLfniyfg+z8x36nOwbPwkPnutTGoVxqWw6fmHdMZldVhndtwR1yQEHy3h+bhhm3Zny/OsQHeMJ/UDDfXs2elhQPLThmAK6OyhbDbPLalCuPoLbjbfCWyLcdzNfIsMc8fmHdQhh62s7QwXjFufYV7gufc9k5n8vdUOWI+SefDmvkAnwkrBHCLHoQXYQc8Dy9kz0q5RRPO6AfmHcOkqz6YXLVcvSnP7vWw3yazZiZNbEcjyRPr9MYPy0q7eccwC2VnMaYx7jL+pgonIldiGG+5ctmOWlY+E2xjynnFrLIFfoDf4UnzjJmZczPwfM3khYlOs/L4dcCagycA7jjhDsP/wQFmLC71GbdZFsN75p3DgU59ZnPwajb12MbjDydpUcJYeRhvOcBdcUGCnDC/TbsWyXjMZPE1XDNRW/xaEdzWOPunu65MBa5a3kIVbcGb4Xs4CtuiskrDI8JwZsrHhQXwinn8LYKrlqu30evKylCPXX+SnPyNJGsv7DEf6CJ4n857dYaamW6zKgfjLjuFcThVVsH75hn/dNRDDdtyOCqrLOFFRyOr6F/Ad+yz3+8wPPvWzNvCjwmVhp/9eJPDryuv4Fvz4wWfpfJJcCm8ZH5046B9g3fh2rCSTX7jfmaeR4zDEfNkjNu6EEIIIYQQQgghhBBCCCGEEP8BPwF2SoMK4/voIwAAAABJRU5ErkJggg==>

[image50]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKcAAAAuCAYAAABNqQn8AAAE7klEQVR4Xu2a/atlUxjHH+9vIRkv8cO9REY0TY0mUiiZSFFKiGKaJFGYacZLI+9vo7ymiPJaRIkipKiJ+EGTJMlPfvKbX/wD4/nMc1azzjp7n3vOPfvOWXf3/dS3e+9e+9yz91rf9aznWXubCSGEEEIIIYQQQgghhBBCCCG65SDXla6NZUPGYa4trjPLBiFWkktcd1iYdBynuJ5znVQ2CLESnOx63iY3HEa+z3Vw2SBE11xnsVyXHOLa4bqzOH6s60XXQnFciE45yvWKa33ZYBFJv3bdWDZYRM4byoNiZSDZp7Nfd+12fTP4yd8XZuflUBh86trr2uP60HX10BkHhmNct1tc678W1/Ox6/6BHrK4ti9cd7tOjI/t4zTXm6412bHEBtfv1mxclvYnra6lnX54zXo8aSgItloMMIN29HDzCFdZDHoNFSyR7lvXr65zijY43fWZ6wfb377WInIysAnabnN94PrZdZfrGtcR2TnrLJZ2Im8tEOH/cz1cNvQJOv4v1x+u84q2HCpXCgkGvQbSdb9nkRc2gcmYeI9b5JQXW0SbI/OTLExHJE7nlWDg910nlA1zYtFi0nFvj9rSuw6rFqLI2xY32lQoAOc85Tq3bJgjLGdLDQ5m5ByiPcZqMyfL/XfWnqbUZM5DLQq3FyzujUlVU0TvHEzJjTZFITqDguDS4vg8Ibo9bXHN43KuZOBPXMdb5JUv2ag5Me1v1r5yYM43XMeVDWMgd3/VRr9rVrjWeyzy4PzeegudT+72j8UAJohINw3UFp3mAYPBoLCss7w3kRt4p8X1n+V610YjIJPvIwvzLbguGm7eZ4gmU4+Dz3Qd1bi+Zy1SK/JnJhQ7DHnR1ztI/l+2GEgKpGREoiUDR/SsiTQwFERtm+lnWBQ46OzBMUxN4YdJExiOpR4Ds4txr40a/maLyn8aujYnY3KL69rB39zDLwPl99NL2JzGnGwXEVnIL8kz88q2FlKh05Q/ApONqPmnxfKXSLsTZW55vUXezVbUFTa8ShzuesZ1QXZsEro256LrEdv//4iWRE0mKZO116RIw/YEg0VlToU+DUQe9hnZN51WFC25kdrAOEQ5zMnz8RyMRNRj6UaLQ60B7exZcu4k0C+7bLp8E7o0JyvXAzZckLLtxypAP/BdvYbBShUgJq2pMs+hYKNw4zopONLmexJR9VRrz5HJRUlVJpkImGKbLW/wuzQn17rZhu8ppSP0A9G+9zBoTRGpJrrItUhVttv4lQEjXGaR7rQZfRxdmZMU6x3XEzY6Eb+0GC9y4l6TNqJZ1tkGqRWiBAPStO01DUTFpnw1gSFZOscZkzz0cxtNUdBPrr8tirayDT1mw0+hmuC7b7X2yJ2CyYNlQ99gI/r7gfi9VtKA8LNmuoicbPGRa7btlhAx6YteP8IEoiVRc5YOXemCKC8Cas+zZjUnUZXqHIO2kTbiZ/meVQF5Zu0RacH140D8XjOzmnOTxViMSyv4ji5SnKrJN+GXil7z5HKL6E70XOoNqnkziznPt9gxacs1E5M8jFi18OobLxG85frK4iaZhRyr4bU4oGihKOCNIV6BIwVg85kHBDw7J5WokeWYE1PS/+k91d0WW2MljA39QV9QeKUJy3uuNT40EZWxHHMKcUDgSRRbPJM+iRJCCCGEEEIIIYQQQgghhBBCCCFED/gf7qvq0voaxFgAAAAASUVORK5CYII=>