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
