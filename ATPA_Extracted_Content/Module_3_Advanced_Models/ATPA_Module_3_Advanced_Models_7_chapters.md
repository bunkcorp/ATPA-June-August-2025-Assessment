# Chapter 1: Model Accuracy

## 1.1.3 Software for Module 3

Python currently has great functionality for processing data and implementing many predictive models. Unfortunately, the current Python implementation (as of March 2022) of many of the models to be covered in Module 3 have significantly less functionality than their R counterparts. For example, additive models can be fit in Python using statsmodels, but it requires a lot of specification that the R package mgcv does automatically. An alternative is pygam, but the authors have documented that the AIC and p-values they provide are incorrect. Therefore, we will only provide R implementations of the models in Module 3.

## 1.1.4 Introduction

As part of Exams SRM and PA, you have seen some very effective modeling techniques. Mastery of those techniques is an incredibly valuable skill to have in the modern age, where data drives decisions. The main models that served as the focus of those exams were (generalized linear) regression and tree-based models. In addition to these basic building blocks, extensions were made for additional purposes.

## 1.1.5 Purposes of a Model

A perfectly fit and perfectly tuned model is still not useful if the model itself is not properly chosen. Deciding which model to use is driven primarily by the purpose of the model. For example, if the only goal is prediction and minimizing prediction error, ensemble methods such as random forests are worth considering. If the model will be used for explanation or coefficient interpretation, then the model choice should prioritize interpretability. If the model will be used for both prediction and explanation, then model choice becomes more complex as there is a trade-off between interpretability and prediction accuracy.

## 1.1.6 Model Workflow

There are many steps to build a model, and in some applications, certain steps may be skipped or expanded in various ways, so there is not a single workflow that can apply to every possible scenario. Also, several steps may need to be iterated, so moving backward (even within stages) is possible. The general stages are: 1) Problem definition and data understanding, 2) Data preparation and feature engineering, 3) Model selection and training, 4) Model evaluation and validation, 5) Model deployment and monitoring.

## 1.1.7 Safety in the Context of Analytics

In the context of analytics, safety relates to analyzing the data in the model consistently and as intended. Modeling requires an appropriate understanding of the problem's definition, data, and modeling approach. Models should meet the intended purpose and efforts should be made so that they are not misused or misinterpreted. Safety considerations include data quality, model assumptions, validation procedures, and ethical implications.

## 1.1.8 Section

Safety in the Context of Analytics - Classification 16


# Chapter 2: Additive Models

## 1.2.2 Introduction

Generalized additive models (GAMs) are an extension of linear models that allow more flexibility in the relationship of each variable to the target. Instead of assuming a linear relationship between predictors and the response, GAMs use smooth functions that can capture non-linear patterns. This provides a middle ground between the interpretability of linear models and the flexibility of more complex machine learning approaches.

## 1.2.3 Motivating Example

We begin our discussion of additive models with an example. This data set records the traffic flow in both directions on an imaginary highway by the hour of the day. The plot shows the data and which observations are in the training and holdout sets. We can see that traffic flow varies non-linearly with the hour of day, with peaks during rush hours and lower values overnight.


# Chapter 3: Linear Mixed Models

## 1.3.2 Introduction

Linear mixed models are used when data has hierarchical or grouped structure. These models allow for both fixed effects (consistent across all groups) and random effects (varying by group). Mixed models are particularly useful in actuarial applications where we have repeated observations within groups, such as multiple claims from the same policyholder or multiple years of data from the same company.


# Chapter 4: Neural Networks

## 1.4.2 Introduction

Neural networks are a machine learning technique inspired by the way biological neural networks in the brain process information. They consist of interconnected nodes (neurons) that can learn to recognize patterns in data. Each neuron receives inputs, applies a transformation, and passes the result to other neurons. Through training, the network learns to adjust the connections to make accurate predictions.

## 1.4.5 Neurons

The building block of a neural network is a neuron (also called a node or unit). Each neuron receives input from other neurons, processes that input using an activation function, and produces an output that can be sent to other neurons. The neuron applies weights to its inputs, sums them, adds a bias term, and then applies an activation function to produce the output.

## 1.4.8 Section

Types of Neural Network Architecture: Feedforward 79

## 1.4.22 Section

Training the Neural Network: Optimization Algorithms 94


# Chapter 5: Bayesian Models

## 1.5.2 Introduction

Bayesian statistics provides a framework for updating our beliefs about parameters as we observe data. Unlike frequentist statistics, Bayesian methods treat parameters as random variables with probability distributions. This allows us to incorporate prior knowledge and quantify uncertainty in our parameter estimates in a principled way.

## 1.5.3 Bayes' Rule

Bayes' rule can be stated as: posterior probability is proportional to prior probability times likelihood. Mathematically: P(θ|data) ∝ P(data|θ) × P(θ), where θ represents the parameters, P(θ|data) is the posterior distribution, P(data|θ) is the likelihood, and P(θ) is the prior distribution. This fundamental rule allows us to update our beliefs about parameters after observing data.


# Chapter 6: Stacking

## 1.6.2 Introduction

Model stacking is an ensemble method that combines predictions from multiple models. Rather than using simple averaging, stacking learns optimal weights for combining different models' predictions. The idea is to use a meta-learning algorithm to learn how to best combine the predictions from multiple base models, potentially capturing different aspects of the underlying patterns in the data.


# Chapter 7: Further Modeling Topics

## 1.7.18 Fairness in Analytics

Fairness in analytics refers to ensuring that predictive models do not discriminate against protected groups or classes of people. This includes considerations of both direct discrimination (explicitly using protected characteristics) and indirect discrimination (using proxy variables that correlate with protected characteristics). Different definitions of fairness exist, including demographic parity, equalized odds, and individual fairness.

## 1.7.2 Introduction

This chapter covers additional modeling considerations including high-dimensional data, missing data handling, and ethical considerations in modeling, particularly around fairness and bias detection. These topics are increasingly important in modern actuarial practice as data becomes more complex and society places greater emphasis on fair and ethical use of predictive models.

## 1.7.18 Fairness in Analytics

Fairness in analytics refers to ensuring that predictive models do not discriminate against protected groups or classes of people. This includes considerations of both direct discrimination (explicitly using protected characteristics) and indirect discrimination (using proxy variables that correlate with protected characteristics). Different definitions of fairness exist, including demographic parity, equalized odds, and individual fairness.

## 1.7.21 Concepts of Algorithmic Fairness

There are several mathematical definitions of algorithmic fairness: 1) Demographic parity requires that the probability of a positive prediction is the same across groups, 2) Equalized odds requires that true positive and false positive rates are equal across groups, 3) Individual fairness requires that similar individuals receive similar predictions. These different fairness criteria can sometimes conflict with each other.
