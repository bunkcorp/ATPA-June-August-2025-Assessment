# Chapter 2: Additive Models

## 1.2.2 Introduction

Generalized additive models (GAMs) are an extension of linear models that allow more flexibility in the relationship of each variable to the target. Instead of assuming a linear relationship between predictors and the response, GAMs use smooth functions that can capture non-linear patterns. This provides a middle ground between the interpretability of linear models and the flexibility of more complex machine learning approaches.

## 1.2.3 Motivating Example

We begin our discussion of additive models with an example. This data set records the traffic flow in both directions on an imaginary highway by the hour of the day. The plot shows the data and which observations are in the training and holdout sets. We can see that traffic flow varies non-linearly with the hour of day, with peaks during rush hours and lower values overnight.
