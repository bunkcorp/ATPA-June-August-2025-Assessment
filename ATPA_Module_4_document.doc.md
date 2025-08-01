

# **ATPA Module 4**

**Contents**

ATPA Module 4	[1](#heading)  
1 Model Explainability and Communication	[5](#1-model-explainability-and-communication)  
1.1 Explainability – Definitions and Communication	[5](#1.1-explainability-–-definitions-and-communication)  
1.1.1 Module 4 Learning Objectives	[5](#1.1.1-module-4-learning-objectives)  
1.1.2 Section 4.1 Learning Objectives	[6](#1.1.2-section-4.1-learning-objectives)  
1.1.3 Introduction	[7](#1.1.3-introduction)  
1.1.4 Explanation versus Interpretation	[8](#1.1.4-explanation-versus-interpretation)  
1.1.5 Explanation versus Interpretation	[9](#1.1.5-explanation-versus-interpretation)  
1.1.6 Characteristics of Good Explanations	[10](#1.1.6-characteristics-of-good-explanations)  
1.1.7 Know Your Audience	[11](#1.1.7-know-your-audience)  
1.1.8 Example	[12](#1.1.8-example)  
1.1.9 Example Continued	[13](#1.1.9-example-continued)  
1.1.10 Characteristics of a Good Interpretation	[14](#1.1.10-characteristics-of-a-good-interpretation)  
1.1.11 Knowledge Check	[15](#1.1.11-knowledge-check)  
1.1.12 Knowledge Check	[16](#1.1.12-knowledge-check)  
1.1.13 Knowledge Check	[17](#1.1.13-knowledge-check)  
1.1.14 Don't Write to Impress; Write to Communicate	[18](#1.1.14-don't-write-to-impress;-write-to-communicate)  
1.1.15 Other Considerations	[19](#1.1.15-other-considerations)  
1.2 Explainability and Ethics	[22](#1.2-explainability-and-ethics)  
1.2.1 Section 4.2 Learning Objective	[22](#1.2.1-section-4.2-learning-objective)  
1.2.2 Introduction	[23](#1.2.2-introduction)  
1.2.3 Transparency	[24](#1.2.3-transparency)  
1.2.4 Model Explainability – Importance	[25](#1.2.4-model-explainability-–-importance)  
1.2.5 Model Explainability	[26](#1.2.5-model-explainability)  
1.3 Techniques for Opaque Models	[28](#1.3-techniques-for-opaque-models)  
1.3.1 Section 4.3 Learning Objectives	[28](#1.3.1-section-4.3-learning-objectives)  
1.3.2 Introduction	[29](#1.3.2-introduction)  
1.3.3 Global versus Local Interpretability	[30](#1.3.3-global-versus-local-interpretability)  
1.3.4 Example	[31](#1.3.4-example)  
1.3.5 Variable Importance	[32](#1.3.5-variable-importance)  
1.3.6 Example	[33](#1.3.6-example)  
1.3.7 Partial Dependence Plot (PDP)	[35](#1.3.7-partial-dependence-plot-\(pdp\))  
1.3.8 PDP for Ordinary Regression	[36](#1.3.8-pdp-for-ordinary-regression)  
1.3.9 PDP for a GLM	[37](#1.3.9-pdp-for-a-glm)  
1.3.10 PDP for a Random Forest	[38](#1.3.10-pdp-for-a-random-forest)  
1.3.11 Two-dimensional PDPs	[39](#1.3.11-two-dimensional-pdps)  
1.3.12 Issues with PDP	[40](#1.3.12-issues-with-pdp)  
1.3.13 Global Surrogate Models	[41](#1.3.13-global-surrogate-models)  
1.3.14 Example: Global Surrogate Model	[42](#1.3.14-example:-global-surrogate-model)  
1.3.15 Local Interpretability	[43](#1.3.15-local-interpretability)  
1.3.16 Individual Conditional Expectation	[44](#1.3.16-individual-conditional-expectation)  
1.3.17 Example: ICE	[45](#1.3.17-example:-ice)  
1.3.18 Shapley Values	[46](#1.3.18-shapley-values)  
1.3.19 Example: SHAP and OLS	[47](#1.3.19-example:-shap-and-ols)  
1.3.20 Example: SHAP and Random Forest	[48](#1.3.20-example:-shap-and-random-forest)  
1.3.21 Example: Using SHAP for Global Explanation	[49](#1.3.21-example:-using-shap-for-global-explanation)  
1.3.22 Example: Using SHAP for Global Explanation	[50](#1.3.22-example:-using-shap-for-global-explanation)  
1.3.23 Lift and Gain Charts	[52](#1.3.23-lift-and-gain-charts)  
1.3.24 Lift Charts	[53](#1.3.24-lift-charts)  
1.3.25 Lift Charts	[54](#1.3.25-lift-charts)  
1.3.26 Lift Charts	[55](#1.3.26-lift-charts)  
1.3.27 Gain Charts	[56](#1.3.27-gain-charts)  
1.3.28 Difference Between Gain Chart and ROC Curve	[57](#1.3.28-difference-between-gain-chart-and-roc-curve)  
1.3.29 Gain Chart	[58](#1.3.29-gain-chart)  
1.4 Reports	[59](#1.4-reports)  
1.4.1 Section 4.4 Learning Objective	[59](#1.4.1-section-4.4-learning-objective)  
1.4.2 Introduction	[60](#1.4.2-introduction)  
1.4.3 ASOP 41	[61](#1.4.3-asop-41)  
1.4.4 Reports	[62](#1.4.4-reports)  
1.4.5 Reproducibility	[63](#1.4.5-reproducibility)  
1.4.6 ATPA Assessment and Reproducibility	[64](#1.4.6-atpa-assessment-and-reproducibility)  
1.4.7 Exercise 4.4.1	[65](#1.4.7-exercise-4.4.1)  
1.4.8 Justification	[66](#1.4.8-justification)  
1.4.9 Justification	[67](#1.4.9-justification)  
1.4.10 Exercise 4.4.2	[68](#1.4.10-exercise-4.4.2)  
1.4.11 Justification Discussion	[69](#1.4.11-justification-discussion)  
1.4.12 Data Dictionaries and Summaries	[70](#1.4.12-data-dictionaries-and-summaries)  
1.4.13 Summary Statistics	[71](#1.4.13-summary-statistics)  
1.4.14 Types of Written Reports	[72](#1.4.14-types-of-written-reports)  
1.4.15 Technical Report	[73](#1.4.15-technical-report)  
1.4.16 Structure of Data and Models Sections	[74](#1.4.16-structure-of-data-and-models-sections)  
1.4.17 Memo	[75](#1.4.17-memo)  
1.4.18 Executive Summary	[76](#1.4.18-executive-summary)  
1.4.19 Executive Summary	[77](#1.4.19-executive-summary)  
1.4.20 Making the Final Recommendation	[79](#1.4.20-making-the-final-recommendation)  
1.4.21 Report Writing by Audience	[80](#1.4.21-report-writing-by-audience)  
1.4.22 Technical Peer	[81](#1.4.22-technical-peer)  
1.4.23 Partially Technical Supervisor	[82](#1.4.23-partially-technical-supervisor)  
1.4.24 Non-technical Executive	[83](#1.4.24-non-technical-executive)  
1.4.25 Conclusion	[84](#1.4.25-conclusion)  
1.5 Model Selection Case Study	[85](#1.5-model-selection-case-study)  
1.5.1 Section 4.5 Learning Objective	[85](#1.5.1-section-4.5-learning-objective)  
1.5.2 Introduction	[86](#1.5.2-introduction)  
1.5.3 Evaluating a Modeling Method	[87](#1.5.3-evaluating-a-modeling-method)  
1.5.4 Accuracy	[88](#1.5.4-accuracy)  
1.5.5 Explainability	[89](#1.5.5-explainability)  
1.5.6 Stability	[90](#1.5.6-stability)  
1.5.7 Analytical Effort	[91](#1.5.7-analytical-effort)  
1.5.8 Computational Efficiency	[92](#1.5.8-computational-efficiency)  
1.5.9 Case Study Description and Data	[93](#1.5.9-case-study-description-and-data)  
1.5.10 Exploratory Data Analysis – Continuous Predictors	[94](#1.5.10-exploratory-data-analysis-–-continuous-predictors)  
1.5.11 Exploratory Data Analysis – Factor Predictor	[95](#1.5.11-exploratory-data-analysis-–-factor-predictor)  
1.5.12 Exploratory Data Analysis – Target Variable	[96](#1.5.12-exploratory-data-analysis-–-target-variable)  
1.5.13 Models	[97](#1.5.13-models)  
1.5.14 Accuracy	[98](#1.5.14-accuracy)  
1.5.15 Comments on the Remaining Dimensions	[99](#1.5.15-comments-on-the-remaining-dimensions)  
1.5.16 Explainability	[100](#1.5.16-explainability)  
1.5.17 Stability	[101](#1.5.17-stability)  
1.5.18 Analytical Effort	[102](#1.5.18-analytical-effort)  
1.5.19 Computational Efficiency	[103](#1.5.19-computational-efficiency)  
1.5.20 Case Study Conclusions	[104](#1.5.20-case-study-conclusions)  
1.5.21 Module 4 Bibliography (copy)	[105](#1.5.21-module-4-bibliography-\(copy\))

# **1 Model Explainability and Communication** {#1-model-explainability-and-communication}

## ***1.1 Explainability – Definitions and Communication*** {#1.1-explainability-–-definitions-and-communication}

### **1.1.1 Module 4 Learning Objectives** {#1.1.1-module-4-learning-objectives}

Model Explainability and Communication

Component Table1

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Module 4 Learning Objectives |
| Content |  Explain the difference between explanation and interpretation. Recognize how explanations will differ by audience. Explain the connection between ethics and explainability. Understand the difference between local and global interpretability. Understand and be able to apply variable importance plots, partial dependence plots, individual conditional expectation plots, Shapley values, and lift and gain charts. Write reports that effectively communicate with the intended audience. Recommend the best model for a given problem.  |
| Footer | Panel Footer |

 Module 4

### **1.1.2 Section 4.1 Learning Objectives** {#1.1.2-section-4.1-learning-objectives}

Explainability – Definitions and Communication

Component Table2

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 4.1 Learning Objectives**  Explain the difference between explanation and interpretation. Recognize how explanations will differ by audience.  |
| Footer | Panel Footer |

### **1.1.3 Introduction** {#1.1.3-introduction}

The process of preparing data and building a predictive model involves a variety of valuable tools that can answer business problems in effective ways. However, you can be the best at data manipulation or know the ins and outs of every advanced model that exists and you will find that you will not be successful if you are not able to communicate the results of your efforts. The purpose of this module is to establish good forms of communication for predictive analytics work.  
Introduction

### **1.1.4 Explanation versus Interpretation** {#1.1.4-explanation-versus-interpretation}

The paper "Understanding Artificial Intelligence Ethics and Safety" describes the process of explaining a model’s behavior (Leslie, 2019).  
Explanation versus Interpretation  
Explaining an algorithmic model’s decision or behavior should involve making explicit how the particular set of factors which determined that outcome can play the role of evidence in supporting the conclusion reached. It should involve making intelligible to affected individuals the rationale behind that decision or **behavior as if it had been produced by a reasoning, evidence-using, and inference-making person**.  
The key is highlighted in bold above. The paper goes on to describe in detail the different levels at which a human would reason and thus the different aspects that an explanation must include to satisfy the above. In summary, these include both a technical breakdown of the model and context-based clarification and justifications. We will refer to these two aspects as an explanation and an interpretation.

Component Table3

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Explanation |
| Tab 1 Text | Explanation |
| Tab 1 Content |  Logic, which refers to the steps the algorithm goes through to make decisions or produce the output. Semantics, which refers to the meaning or impact of different aspects of the model, e.g., the influence of a factor on the prediction.  |
| Tab 2 Title | Interpretation |
| Tab 2 Text | Interpretation |
| Tab 2 Content | Implications of the model output in the context of the business problem. The social understanding of practices, beliefs, and intentions as reflected in the conclusions and recommendations. Moral justification of the conclusions and recommendations.  |

### **1.1.5 Explanation versus Interpretation** {#1.1.5-explanation-versus-interpretation}

The difference between an explanation and an interpretation is important. All models can be both explained and interpreted, but it is not necessary that they should be in all cases. The degree to which a predictive model is explained or interpreted depends entirely on the audience. For this module we will assume that there are three different audiences, although in reality there will be many different types of audiences (and a given communication may reach multiple audiences) and you will have to discern how to adjust. 

In this module we will focus on three particular audiences: 

* A peer who has a similar knowledge of predictive modeling as you;  
* A supervisor who knows some predictive modeling but not enough to be able to carry out a robust modeling process; and  
* An executive who understands the terminology of the business context but has no explicit knowledge of predictive modeling methods.

We will come back to the idea of explaining and interpreting predictive modeling methods for these three different audiences throughout this module.  
Explanation versus Interpretation

### **1.1.6 Characteristics of Good Explanations** {#1.1.6-characteristics-of-good-explanations}

Some models may be easy to explain because they are inherently explainable. For example, generalized linear models, which provide a direct relation of input variables to predicted response, fall into this category. Other model forms require further work to generate explanations. For example, neural network models are considered opaque because the relationship between input variables and predictions are non-linear and complex (potentially involving multiple layers). 

The key characteristics of a good explanation are: 

* **Alignment with human intuition:** The human that is going to consume your explanation should be able to understand it. Subtleties include the level of experience of that human, e.g., your colleague reviewing the model for biases or the customer who by law can request an explanation of the outcome of the model.  
* **Appropriateness:** The explanation must be appropriate for the objective. The explanation must accurately represent what the model sees, and how it makes its decisions.  
* **Completeness:** The explanation must provide the right level of information and be in a format such that it is easy to review and not obfuscate important details. For example, if you are using a variable transformation or data compression technique, such as principal component analysis, then showing the explanation in terms of the transformed principal component may hide the fact that the variable contains information about untransformed variables (e.g., an individual’s weight and blood pressure).

Characteristics of Good Explanations

### **1.1.7 Know Your Audience** {#1.1.7-know-your-audience}

Whenever you set out to provide written communication, become familiar with your audience by considering the following questions: 

* What is their current knowledge with respect to the problem?  
* How much time will they spend understanding the explanation?  
* Will they read all of it?  
* What questions will they need answered?  
* Will they read different parts of the document at different times?  
* Will they use the document as reference material?  
* Have they been involved in defining the problem or designing the solution that resulted in this communication?  
* Will they comprehend the concepts being communicated?

Written communication is the medium we use on Exam ATPA. However, in many contexts, oral communication is just as important. The language used in these modules assumes written communication but many of these principles also apply to oral communication. There may be an extra decision to be made about whether the communication is best done orally or in writing.  
Know Your Audience

### **1.1.8 Example** {#1.1.8-example}

Suppose that you have modeled the number of times a person uses a credit card in a day using day of the week, age of the individual, and the individual’s income. We will show examples of how to explain the model choice to a technical peer, a partially technical supervisor, and an executive. 

In each case, pay attention to how the explanation aligns with human intuition, is appropriate, and is complete. 

* **Technical Peer:** The number of credit card purchases are non-negative integers, so a Poisson GLM with a log link function was fit first. Day of week, age, and income were included as predictor variables. We assessed their significance using *p*\-values on fitting training data, and all variables were significant at a 5% level. We tested for overdispersion using a Quasi-Poisson GLM with a log link function and compared the predictions between the two models on a test set using loglikelihood as a test metric. The results were similar, so the simpler Poisson model was chosen as the model form.  
* **Technical Supervisor:** A Generalized Linear Model (GLM) with Poisson distribution was built using day of week, age, and income, all of which proved to be significant predictors, to predict the number of credit card purchases. This model is applicable when the variable being predicted is counting the number of occurrences, such as the number of credit card purchases. The Poisson assumption that the mean and variance of the target variable are equal was verified.  
* **Executive:** After examining the nature of the data that was provided, we have fit a Generalized Linear Model (GLM) appropriate for predicting frequency, as with credit card purchases. The predicted number of credit card purchases is based on day of week, age, and income using a straightforward calculation that makes clear the relative impact of each factor.

Example

### **1.1.9 Example Continued** {#1.1.9-example-continued}

We will now compare these explanations with the characteristics of a good explanation.  
Example Continued

Component Table4

| Type | Tabset |
| :---- | :---- |
| Tabs | 3 |
| Tab 1 Title | Alignment with human intuition |
| Tab 1 Text | Intuitiveness |
| Tab 1 Content | Notice how when talking to an equally technical peer, using language such as “log link function” and “overdispersion” is okay without further explanation, but when talking to a partially technical supervisor or an executive these terms would either need to be explained more or, in this case, left out. Even using the acronym GLM is okay with someone who knows what a GLM is but would not be okay by itself when talking to someone less technical.  |
| Tab 2 Title | Appropriateness |
| Tab 2 Text | Appropriateness |
| Tab 2 Content | The model choice is justified in all three cases. For the peer it is justified briefly using technical language, “non-negative and integer valued,” while it is justified using more plain language to the partially technical supervisor. For the executive, the justification is non-technical but still expresses appropriate confidence in the statement.  |
| Tab 3 Title | Completeness |
| Tab 3 Text | Completeness |
| Tab 3 Content | Talking about model assumptions when building a predictive model is important. For the technical peer, it is considered complete to talk about model assumptions as well as possible remedies or alternative models and how the assumptions are being tested. The supervisor might also want to hear about the alternative models used. In this case we opted to describe the model assumption that we were concerned with and that it was verified. The executive was not told anything about model assumptions.  |

In the simple three-audience world we created, a technical peer should know about the details of each step, the supervisor should know each step, and the executive cares mostly about results, so simple and brief justifications and explanations are sufficient. This is not true in every case, but this is an easy way to start thinking about how to treat the different audiences.

### **1.1.10 Characteristics of a Good Interpretation** {#1.1.10-characteristics-of-a-good-interpretation}

One difference between an explanation and an interpretation is that a simple model and a complicated model can both have a similar interpretation. Suppose the current price of a commodity is 75 and you are building a model to determine what the price of the commodity will be next year to know if you should buy now or wait. Consider the following interpretation of the model output: “The price will most likely be between 80 and 90\. There is only a 1% chance it will be less than 75, so it is probably best to buy now”. It could have come from many different models. 

Consider the case where the business context is determining the relationship of a certain variable to the target. The interpretation “income has a strong positive relationship with the number of credit card purchases” could have come from a model as simple as a GLM or as complicated as a neural network. We will examine several tools later in this module that can be used to interpret model output from the advanced models introduced in Module 3 without needing to delve into explaining the specific model structures. 

Some key characteristics of a good interpretation are: 

* **Appropriateness.** As with explanations, the interpretation of a model should be appropriate for the objective and the audience. This also refers to giving the interpretation in terms of the business problem and in the language of the business context. For example, suppose “years” is the name of a variable in a data set. This is a vague variable name and so if it shows up in an interpretation it should be given appropriate language for the context, such as “years working at the company.”  
* **Accuracy and honesty:** While many audiences will not need to know all the explanations behind model choices and results, when we skip important details and convert to plain language, certain important features and aspects could be lost. Things such as important assumptions or model weaknesses should be explicit when they are attached to certain interpretations.  
* **Evidence-based:** Being able to justify interpretations that are being made. This is where explanations and interpretations meet. Understanding how a model works helps to prove that certain model output means what we are claiming that it means.

Characteristics of a Good Interpretation

### **1.1.11 Knowledge Check** {#1.1.11-knowledge-check}

Knowledge Check  
Determine if the interpretation is appropriate, accurate, and evidence-based. Do not assume there is additional information available.

Component Table5

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 2 |
| Option 1 | Yes, this interpretation is appropriate, accurate, and evidence based. |
| Option 2 | No, at least one of the three characteristics does not apply. |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| This interpretation is not appropriate as it uses language that is not in the proper business context. The interpretation is brief and therefore could potentially be inaccurate. Perhaps it could be improved by stating what is meant by \&ldquo;best model\&rdquo; as well as stating more about the model. There is evidence stated for the interpretation. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| This interpretation is not appropriate as it uses language that is not in the proper business context. The interpretation is brief and therefore could potentially be inaccurate. Perhaps it could be improved by stating what is meant by \&ldquo;best model\&rdquo; as well as stating more about the model. There is evidence stated for the interpretation. |

The best model for predicting *num\_purchases* is a neural network. When compared to a Poisson GLM and a random forest, the neural network provides the lowest mean squared error for predictions on a holdout set.

### **1.1.12 Knowledge Check** {#1.1.12-knowledge-check}

Knowledge Check  
Age is a significant variable when predicting the number of credit card purchases. Fitting a Generalized Linear Mixed Model for the data, the variable age was tested for significance using its *p*\-value and was determined that it could not be removed from the model without reducing the model’s predictive power.  
Determine if the interpretation below is appropriate, accurate, and evidence based. Do not assume there is additional information available.

Component Table6

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 2 |
| Option 1 | Yes, this interpretation is appropriate, accurate, and evidence based. |
| Option 2 | No, at least one of the three characteristics does not apply. |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| The interpretation seems appropriate. Assumptions are stated so the interpretation is honest. It is also justified using both technical and non-technical language. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| The interpretation seems appropriate. Assumptions are stated so the interpretation is honest. It is also justified using both technical and non-technical language. |

### **1.1.13 Knowledge Check** {#1.1.13-knowledge-check}

Knowledge Check  
The predicted number of credit card purchases on a Tuesday for a 40-year old who makes $80,000 per year is 4\.  
Determine if the interpretation below is appropriate, accurate, and evidence based. Do not assume there is additional information available.

Component Table7

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 2 |
| Option 1 | Yes, this interpretation is appropriate, accurate, and evidence based. |
| Option 2 | No, at least one of the three characteristics does not apply. |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| The interpretation is appropriate and well stated, but there are no details on the model or on the accuracy of the model predictions, which would be useful for assessing the honesty and accuracy of the interpretation. Also, there is no evidence provided. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| The interpretation is appropriate and well stated, but there are no details on the model or on the accuracy of the model predictions, which would be useful for assessing the honesty and accuracy of the interpretation. Also, there is no evidence provided. |

### **1.1.14 Don't Write to Impress; Write to Communicate** {#1.1.14-don't-write-to-impress;-write-to-communicate}

Having decided what your audience needs to know, the next step is to ensure the communication is about just that, and not designed to impress. 

Wait. You don’t want to impress the audience? You don’t want to impress your manager or those evaluating your work in this course? Why would we all be working so hard on reports if we didn’t want someone to be impressed? Actually, you don’t want to impress the audience; you want to persuade them to action. Consider that mathematicians sometimes complete a proof and are dissatisfied because the proof is complex and so is not considered to be an elegant proof. In contrast, very elegant proofs are so simple that they appear obvious. And that is impressive. Moreover, it is immediately persuasive. It is a simple, easy-to-follow solution that was previously unknown. That will truly make an impression with your audience. So, for report writing, think of your style as impressing by elegance rather than flash. 

The specific words, technical phrasing, acronyms, and so forth that you choose to communicate with your audience may ultimately determine whether you do, in fact, communicate with your audience. Read the excerpt in the box to the right from “The Standard Deviations of Writing” by Roger MacBride Allen. How often do you encounter the type of writing he describes? Have you yourself written this way?  
Don't Write to Impress; Write to Communicate

Component Table8

| Type | Callout |
| :---- | :---- |
| Content | I am convinced that this is in large part a product of what passes for writing in school, government, and business. We are taught, over and over again, to impress the boss or the teacher with how much we know, how many big words we can use, how important we can make our subject seem. If the meaning itself is lost in a blizzard of jargon, all the better. Few people have the nerve to admit they don’t know what you meant, and if you yourself are unsure, a little bureaucratic vagueness can often serve to hide what you don’t know. Inevitably, something is lost when things are made pompous. “Never enumerate your feathered progeny until the incubation process is thoroughly realized” just doesn’t have the same punch as “Don’t count your chickens before they’re hatched.” Do not, under any circumstances, dumb down your work; but why be deliberately obscure? A good rule of thumb: *Use the shortest words and simplest sentence structure that will convey the meaning, mood, and tone you intend.*–Roger MacBride Allen, from The Standard Deviations of Writing. [https://www.sfwa.org/2005/01/mistakes-in-writing/](#bookmark=id.xzzawh55bgsl) |

### **1.1.15 Other Considerations**  {#1.1.15-other-considerations}

Here are a few additional items that are important to consider when explaining and interpreting predictive modeling.   
Other Considerations

Component Table9

| Type | Tabset |
| :---- | :---- |
| Tabs | 5 |
| Tab 1 Title | Severity |
| Tab 1 Text | Severity |
| Tab 1 Content | The appropriate explanation for a model differs depending on the use of the model and the severity of risk the model carries. For example, we might require a more rigorous explanation for a self-driving car algorithm given questions about its safety versus a model predicting whether a customer is likely to purchase additional products. The stakes of the two are vastly different and therefore warrant different levels of scrutiny. We might also worry less about the precision of an explanation when the severity of risk is low. For example, an inaccurate, but intuitive, explanation of a complex model might indicate that mortality increases as age increases, missing some of the actual model behavior which might show a decrease in mortality between ages 22 and 25 for males who live in Seattle. The less severe the potential negative impact of oversimplifying this relationship, the more willing we would be to make the tradeoff for a more intuitive explanation.  |
| Tab 2 Title | User Expertise |
| Tab 2 Text | User Expertise |
| Tab 2 Content | The end user is an important consideration when creating explanations. The amount of expertise the individuals have with the subject matter will determine how simple or complex your explanations can be. For example, a colleague with a strong predictive modeling background may be able to review and comprehend a model explanation with interactions between variables. In contrast, a customer, who by law can request an explanation of the outcome of the model, may only be able to understand explanations that discuss the overall impact of single factors at a time.  |
| Tab 3 Title | Data |
| Tab 3 Text | Data |
| Tab 3 Content | Data pre-processing can impact the explainability and interpretability of a model. If data transformations have obscured the understanding of a variable’s meaning, interpreting the transformed variable’s impact on model predictions will not be intuitive to a human. Principal component analysis (PCA) is a good example of this. In PCA, we transform a large set of variables into a smaller set, the principal components, which retains most of the information of the full set. The principal components are linear combinations of the original variables. A model that contains principal components as predictors would obscure the relationship between the original variables and the target variable. Each original predictor variable might contribute to multiple principal components; that variable’s impact on the target variable would have to be parsed through the impact of each of the principal components. Other data transformations can similarly make interpretation more difficult. Transforming a variable with the natural log function, a step sometimes performed to adjust highly skewed variables, is one example. To illustrate, suppose we are modeling the claim severity for auto insurance and we have log-transformed the vehicle value variable. It is more complicated for a human to interpret the impact on severity of a one-unit increase on the log-scale than to interpret the impact on severity of a one-dollar increase. |
| Tab 4 Title | Model Form |
| Tab 4 Text | Model Form |
| Tab 4 Content | The selected model form, specifically its complexity, impacts the interpretability of a model. The properties of different model forms in general that impact interpretability are described below, with specific examples following. **Linearity** A linear model form is one in which the parameters of the model are related to the variables in a linear way. For example, a linear regression of the form *y* \= *ax* \+ *b* is linear, but a decision tree is not. Linearity is important for interpretability because of the prominence of education in linear equations. **Monotonicity** A model form is monotonic if the relationship between input variables and the model output are consistent in direction. For example, if you were to increase the age of an individual and the model output increases for all ages, then that is monotonic. If, however, increasing age up to age 50 results in an increase in the model prediction, but after age 50 the model prediction starts to decrease then that would be a non-monotonic relationship. Monotonicity is important because of the human brain’s capacity to understand and justify the actions of the model. Non-monotonic relationships require more careful interpretations to make intuitive sense.  |
| Tab 5 Title | Complexity (or Flexibility) |
| Tab 5 Text | Complexity (or Flexibility) |
| Tab 5 Content | There are many ways models forms can be considered complex or flexible, but typically it can be summarized as when the model is non-linear and contains interactions, especially interactions that involve more than two variables. A model form that automatically includes interactions can result in interpretation difficulties because of the complexity of the relationship that is being expressed, making it difficult to understand and justify. We use complexity and flexibility interchangeably since flexible models can capture complexity (non-linearity and multiple interactions). Some simple (or non-flexible) models can be, in themselves, a good explanation. Consider a linear model of the form *y* \= *ax* \+ *b*. If the objective is to review the model and check if is fair and reasonable, then the model itself provides an appropriate (it says exactly how the outputs are calculated) and intuitive (the simplicity of the formula makes it easy to understand) explanation.Types of explainable models include ordinary least squares models, generalized linear models, and generalized additive models, although the degree of the complexity and explainability may vary. Types of models with lower inherent explainability include random forests, boosting machines, neural networks, and support vector machines. The book *An Introduction to Statistical Learning* (James, Witten, Hastie, & Tibshirani, 2013\) illustrates the trade-off between flexibility and interpretability. It is worth noting that flexibility and interpretability have a trade-off relationship in general. |

## ***1.2 Explainability and Ethics*** {#1.2-explainability-and-ethics}

### **1.2.1 Section 4.2 Learning Objective** {#1.2.1-section-4.2-learning-objective}

Explainability and Ethics

Component Table10

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 4.2 Learning Objective**  Explain the connection between ethics and explainability.  |
| Footer | Panel Footer |

### **1.2.2 Introduction** {#1.2.2-introduction}

Communication and ethics are very closely related. We have already seen how accuracy and honesty are important when interpreting model output. To review the ethical framework we have established, these four aspects are reviewed in brief detail: 

* **Fairness** refers to being impartial, equitable, not harming anyone, and functions against bias or discrimination. Fairness is related to the following principles: justice, consistency, inclusion, equality, equity, (non-) bias, (non-) discrimination, diversity, plurality, accessibility, reversibility, remedy, redress, challenge, access, and distribution.  
* **Safety** refers to the operational and technical sustainability aspects of the data, model, and implementation. The qualities, such as accuracy, robustness, reliability, technical integrity, stability, security, and ensuring privacy, are considered safe and technically sustainable.  
* **Transparency** refers to the quality of how the process is documented and disclosed, explained, interpreted, and communicated. Interpretability, explainability, explicability, and understandability are related principles.  
* **Accountability** refers to defining, identifying, and allocating responsibility throughout the workflow. Responsibility may relate to owning the processes and the results and determining who will answer when questions arise.

Introduction

### **1.2.3 Transparency** {#1.2.3-transparency}

Transparency is very important to reduce the incidence of bias within the process or the outcome. We discuss transparency related to both below.

Transparency

Component Table11

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Outcome Transparency |
| Tab 1 Text | Outcome Transparency |
| Tab 1 Content | Transparency of how the outcome relates to the input is also important. One proposed set of standards on ensuring that model outcomes (its decisions, behaviors, and problem-solving) are explainable is the following (Leslie, 2019):  Properly inform anyone making a decision based on the output of the model. Be offered to affected stakeholders and concerned parties in an accessible way. In other words, this framework states that model results from the predictive process should be explainable to those in non-technical fields who will be making decisions based on the outcomes. Explanations should be delivered in plain language and should be presented in the context of the human characteristics and relationships rather than just trying to interpret the technical or mathematical characteristics of the model.  |
| Tab 2 Title | Process Transparency |
| Tab 2 Text | Process Transparency |
| Tab 2 Content | Transparency in building the model is important so that the decisions that result in the ultimate model can be effectively audited and steps taken can be easily reviewed. Transparency also provides an understanding of each step in the final pipeline such that it can be easy to see the path data travels and which data is used. For example, if we create transformed variables using a dimension reduction technique such as PCA, it can be very easy to lose sight of the potentially risky variables that went into the derived variables. Transparency is also important for reproducibility. Biases can arise at any point during the model building process, from being in the data used, to the decisions made by humans, to those made by algorithms, to even the implementation. Making sure the whole process is documented and reproducible at least provides a mechanism for further review by other parties to hopefully detect and reduce biases. If bias is identified, being able to modify the actual process being used is critical, which is why it is important to be able to identify the process that will fully reproduce the results. |

### **1.2.4 Model Explainability – Importance** {#1.2.4-model-explainability-–-importance}

Model explainability and model interpretability are core components of analytic transparency. It is important to understand what model explainability/interpretability helps us achieve and why we need to consider it. The paper “Towards a Rigorous Science of Interpretable Machine Learning” (Doshi-Velez & Kim, 2017\) defines interpretability in the context of modeling systems as the ability to explain or to present in understandable terms to a human. Interpretability is the mechanism by which we can validate several desirable qualities (including other ethical principles) of the modeling process for which we have no other complete way of confirming. It is the validation of these qualities that is our objective when it comes to model explainability.   
Model Explainability – Importance

### **1.2.5 Model Explainability** {#1.2.5-model-explainability}

Model Explainability

Component Table12

| Type | Tabset |
| :---- | :---- |
| Tabs | 4 |
| Tab 1 Title | Fairness |
| Tab 1 Text | Fairness |
| Tab 1 Content | Validating that an algorithm conforms to a chosen definition of fairness can sometimes be done using additional algorithms and calculations, but those methods require a complete definition of fairness and the attributes that are to be tested. Having explanations of a model in terms understandable to a human allows us to potentially identify issues leading to unfair outcomes that we may not have anticipated. Additionally, problems identified in the model and outputs (if they are interpretable) can point to problems further upstream such as data biases, or problematic variable selection processes that might have been missed.  |
| Tab 2 Title | Accuracy |
| Tab 2 Text | Accuracy |
| Tab 2 Content | We already have some measures of accuracy of our models, but even these are just estimates and not perfect predictors of how accurate our model will be on future data because the future is unknown. Being able to interpret our models can help us identify problems after the model is built that, as humans, we understand will cause reductions in future accuracy, but didn’t pre-specify during model development (and may not be captured in out of sample validation data). We may identify that the model is picking up spurious correlations or is overly reliant on a variable for which we know the data isn’t trustworthy or is likely to change because of recent events. An example of changes due to recent events is that credit scores may become less reliable in the future as individuals learn how to raise their score without changing the behaviors that previously linked credit score to, say, driving behavior. |
| Tab 3 Title | Trust |
| Tab 3 Text | Trust |
| Tab 3 Content | Being able to understand a model and its outputs, especially when there is an inability to completely specify every potential outcome, is a key part of being able to trust a model. Crucially, this is not only important for the individuals building the model (who might have access to more information about how it was built and thus inherently have more trust), but also those who are impacted by the results of the model. For example, a customer who has received an increase in their insurance renewal price and hasn’t been able to get an adequate explanation may consequently lose trust in the insurance company.  |
| Tab 4 Title | Internal |
| Tab 4 Text | Internal |
| Tab 4 Content | There are also internal motivations for model explainability. Understanding model behavior helps gain management approval for proposed changes, informs strategy based on model insights, and can improve internal domain knowledge. For example, a model that predicts high severity claims can augment a claim adjuster’s knowledge of factors contributing to more expensive claims.  |

## ***1.3 Techniques for Opaque Models*** {#1.3-techniques-for-opaque-models}

### **1.3.1 Section 4.3 Learning Objectives** {#1.3.1-section-4.3-learning-objectives}

Techniques for Opaque Models 

Component Table13

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 4.3 Learning Objectives**  Understand the difference between local and global interpretability. Understand and be able to apply variable importance plots, partial dependence plots, individual conditional expectation plots, Shapley values, and lift and gain charts.   |
| Footer | Panel Footer |

### **1.3.2 Introduction** {#1.3.2-introduction}

Relying on the inherent explainability of a model isn’t the only option you have when interpretability is required. If the model isn’t directly explainable, there are techniques available to produce explanations from those models that are more “human-friendly.” Note, generally due to the complexity inherent in opaque models, a completely accurate explanation fundamentally isn’t possible and thus these methods work on a trade-off between being completely accurate representations of the model and producing a summary explanation that is easily understood by a human. 

A particularly useful group of techniques for explaining opaque models are **model agnostic methods**. One of the key benefits of these techniques is the separation of the technique from the actual model chosen, which allows you to maintain consistency in the chosen explanation method without restricting yourself to a single model type. 

Much of the content in this section is based on *Interpreting Machine Learning: A Guide for Making Black Box Models Explainable* by Christoph Molnar. If you are interested, a search will lead you to an online version of this text. Reading the material is not required for this course.  
Introduction

### **1.3.3 Global versus Local Interpretability** {#1.3.3-global-versus-local-interpretability}

Model interpretability can be either global or local in scope. **Global interpretability** considers a holistic view of how the model makes predictions. Which variables are important? What relationships does each variable have with the target variable? What interactions exist between variables? The more complex a model, the more difficult it is to achieve global interpretability. Humans can only comprehend a limited number of data points, so understanding a model with hundreds of variables and complex interactions is not feasible. An example of global interpretability is understanding that a mortality model predicts higher mortality than average for policyholders over the age of 80 who smoke. 

**Local interpretability** contemplates how a model makes a prediction for a specific observation. How does this observation compare to a typical observation? Which variables set this observation apart? What contribution did each variable have in determining the prediction for this observation? Note that locally, an otherwise complex model may behave more intuitively. Going back to our example of a mortality model, even if the model is too complex to understand globally, we might be able to explain the prediction for a single observation: the fact that the observed policyholder was 80 years old (compared to the average age) and a smoker (compared to a non-smoker) contributed significantly to the model predicting a high rate of mortality. In this case the local interpretation may also identify the relative contribution of age and smoking status to the increased mortality. Local interpretability can be desirable for customer-facing applications of models, for example a customer calling into the call center asking for an explanation of why their renewal premium is higher than usual. 

Local explanations can also be aggregated to give an approximately global explanation. As an example, we could notice after reviewing a large number of individual outcomes that individual mortality predictions are typically driven higher by the older age of policyholders. Aggregated, we would make the global observation that older policyholders have a higher likelihood of mortality.  
Global versus Local Interpretability

### **1.3.4 Example** {#1.3.4-example}

\[BEGIN LINK \-https://meps.ahrq.gov/mepsweb/about\_meps/survey\_back.jsp\]  
At this time download the Rmd file for this section ( [atpa\_4\_3\_r.rmd](#bookmark=id.hod4h5eslzlr) and [atpa\_4\_3\_python.rmd](#bookmark=id.ddc22hdrow7l)) and a data file containing dental data ( [dental.csv](#bookmark=id.xw88bjrgnqt)).\* 

The variables are: 

* *Target*: The amount paid on a dental claim  
* *age*: The age of the individual having the claim  
* *bmi*: The body mass index of the individual  
* *familyIncome*: The total income of the family  
* *occupation\_group*: The occupation of the individual having the claim  
* *sex*: The sex of the individual with male \= 0 and female \= 1

\[END LINK\]  
Example

Component Table14

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 0 to install required packages if not already available to you. Run CHUNK 1 to load and prepare the data. Then run CHUNK 2 to fit three models.  |

\[BEGIN LINK \-https://meps.ahrq.gov/mepsweb/about\_meps/survey\_back.jsp\]  
The first two models (ordinary regression and a GLM) are easy to interpret and can be used to check that the methods used here provide sensible answers. The third model is a random forest. No variable or model selection has been done. The purpose of this section is to explain a fitted model. 

\*This data set comes from Agency for Healthcare Research and Quality and is adapted from their Medical Expenditure Panel Survey. Information about the survey (not required reading) is available at the [MEPS website](#bookmark=id.dbwrh1ybit41).  
\[END LINK\]

### **1.3.5 Variable Importance** {#1.3.5-variable-importance}

One form of explanation describes the variables that contribute the most to the model’s decisions. Variable importance assigns a score to each variable used in a predictive model. A variable that explains the predictor variable more gets a higher score, i.e., higher importance. 

Techniques that calculate variable importance typically do so for the overall model, so are considered a global method and usually for single variables at a time (although variants that look at interactions of a specified depth also exist). This makes them rank quite highly when it comes to explanations that are intuitive for humans to understand. However, because they are essentially summarizing an entire model down to a single number per variable (often not even a directional number) this means they lack accuracy and hide a lot of the complexity of the model. This makes them less useful in high severity situations. Typically, variable importance methods are useful as a first inspection of the model, to understand at a high level which variables have the most impact and identifying any serious issues quickly before delving into more detailed explanations. They can be used to ensure at a high level that the model is not using any variables that could lead to unfair outcomes. 

It is also worth noting that variables of greater importance can appear to take away some of the importance of lower ranked variables. Consider a mortality study that includes income level and sex, where for this data income level is more predictive than sex. Because income level is driven to some extent by differences by sex in our society, the predictive power of income level by itself includes an element of sex, leaving the actual sex variable less powerful in explaining the remaining mortality differences in the data. For this reason, one may wonder why sex has so little impact on the results whereas we know from experience that sex is a significant contributor to mortality experience. This is an example also of collinearity impacting the results.  
Variable Importance

### **1.3.6 Example** {#1.3.6-example}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_4\_3\_python.rmd\]  
The output from the OLS model and GLM (not shown) shows that *age* is the most important variable, followed in order by *bmi*, *SALES*, *sex*, *MANAGEMENT* , *OTHER*, *familyIncome*, *ADMIN*, *PRODUCTION*, *PROFESSIONAL*, and *SERVICE*. 

*Age* is the most important variable for the OLS and the GLM model. For both of these models, the *t*\-values are used to make the variable importance plot, and you can see that it has the largest *t*\-value in both models. The random forest plot shows some differences. This may be because where relationships are not linear the random forest can pick up their importance while the other models cannot. For this model, importance is based on examining how much the objective function (MSE here) is reduced when that variable is used in a split, with the reduction over all the trees being averaged.  
\[END LINK\]  
Example

Component Table15

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 3 to construct variable importance plots for the three models. |

### **1.3.7 Partial Dependence Plot (PDP)** {#1.3.7-partial-dependence-plot-(pdp)}

**Partial dependence plots** show the average marginal effect of a variable on the response variable. The name derives from the fact that they illustrate the model’s partial dependence on a variable of interest. The plots, with the levels/values of a variable on the x-axis and the response variable on the y-axis, are derived one variable at a time by the following steps: 

* For each level/value of the variable (for a continuous variable this would be done for selected points along the continuous scale):   
  * Set the variable to this level/value for all observations  
  * Generate predictions from the model for all adjusted observations  
  * Calculate the average prediction and plot  
* Repeat the above with the remaining levels/values of the variable

For example, suppose we are interested in the effect of age on mortality in our model. For a given age, say 40, we take each observation in the dataset, change the age to 40, and use our model to estimate mortality. We then calculate the average predicted mortality and plot it. After repeating for other ages, we see what the average model prediction would be if everyone was 40 years old, if everyone was 50 years old, etc. By changing only the age variable, we get an approximation for the marginal effect of age.  
Partial Dependence Plot (PDP)

### **1.3.8 PDP for Ordinary Regression** {#1.3.8-pdp-for-ordinary-regression}

For a very simple model, this marginal effect would be straightforward. For example, a linear regression model's slope coefficient explains how a predictor variable change will affect the response variable. The marginal effect is explicit in the coefficients and the PDP is an exact representation of the actual marginal effect. 

As expected, the plots for the continuous variables are straight lines with slopes matching the estimated coefficients. For the categorical variable, note that for UNKNOWN the plot is at about 775 and for SALES it is at about 475\. The difference of –300 aligns with the regression coefficient of SALES of –296.  
PDP for Ordinary Regression

Component Table16

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 4 to make PDP plots for *age*, *bmi*, *familyIncome*, and *occupation\_group* using the ordinary least squares model. |

### **1.3.9 PDP for a GLM** {#1.3.9-pdp-for-a-glm}

As expected, there is an exponential curve for the continuous variables and the approximate growth rate matches the estimated coefficients.  
PDP for a GLM

Component Table17

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 5 to make PDP plots for the four variables using the GLM. With the log link, we expect the partial dependence plots to reproduce an exponential curve. |

### **1.3.10 PDP for a Random Forest** {#1.3.10-pdp-for-a-random-forest}

It is clear from the plots that the random forest model is able to note that the average costs by *age* or *bmi* are not linear or monotonic. For *age*, the plot shows that the model is able to reflect the fact that dental costs are higher for those in the 12-18 age range relative to nearby ages, likely due to orthodontic work typical at this age.  
PDP for a Random Forest

Component Table18

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 6 to make the PDP plots for the four variables using the random forest model. This is where we expect the plot to produce information about the model that we don’t already know. |

### **1.3.11 Two-dimensional PDPs** {#1.3.11-two-dimensional-pdps}

A PDP can be developed using two variables. In this case, an interaction between the two variables can be visible. However, this is more difficult to interpret and will require a 3-D plot or a heat map. The default plot for the **pdp** package is a heat map.  
Two-dimensional PDPs

Component Table19

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 7 to make a heat map for the random forest model. This may take a while. As is often the case, these are difficult to interpret. Here it appears that the effect of family income is more pronounced at the younger and older ages. |

### **1.3.12 Issues with PDP** {#1.3.12-issues-with-pdp}

Capturing the marginal effect for a complex model, however, is not straightforward. The PDP simplifies the interactions and non-linearities by taking the average effect and examining one variable at a time. This simplification is a key strength of the PDP – it makes the marginal effect (or the partial dependence) more intuitive to explain. 

While altering one variable at a time is what allows us to tease out the marginal effect, it is the biggest weakness of a PDP. Because we are fixing all variables other than the one we are calculating the PDP for, we are assuming this variable is independent of the others. As an example where this is not the case, consider the dental data. About 21% of the sample is under age 16 and all of them have *occupation\_group* \= UNKNOWN. When evaluating the average cost for *occupation\_group* \= MANAGEMENT, predictions for six-year old managers will be included. 

The other simplification, averaging effects across all observations, allows us to understand global effects. However, because of this approach the PDP may generalize too much and may miss important heterogeneous relationships created by interactions. 

Consider a variable for which half the observations have a positive relationship with the target variable and for which the other half has a negative relationship. The PDP would average across these observations and show a flat line. We would mistakenly believe this variable to be unimportant in predicting the target variable. However, it is important to remember that any method that explains complex models will by necessity oversimplify the model. Whether or not a PDP can be an effective tool to demonstrate that the model is yielding fair outcomes depends on the use of the model and the severity of the consequences of the model.  
Issues with PDP

### **1.3.13 Global Surrogate Models** {#1.3.13-global-surrogate-models}

One possibility for explaining a complex model is to use an interpretable model, such as linear regression or a decision tree, to approximate the complex model. The interpretable model is a surrogate for the complex model. The surrogate model is fit to the predictions of the more complex model. It is not able to pick up all the nuances (and is therefore less accurate), but because it is inherently interpretable, we are able to explain the predictions. Because this solution applies a model to all the data, it is a global method. 

Global surrogate models provide flexibility (any interpretable model can be used) and intuitiveness. However, because the surrogate model is built on another model’s predictions, it does not say anything about the actual data, it simply provides insights about the model. This is still very useful in instances where we need to explain the model and the modeled result to a policyholder or internal stakeholders to demonstrate that the model is fair.  
Global Surrogate Models

### **1.3.14 Example: Global Surrogate Model** {#1.3.14-example:-global-surrogate-model}

Using our continuing example, a GLM, which is easily explained, can be fit to the predictions from a random forest.  
Example: Global Surrogate Model

Component Table20

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 8 to do this. Do you notice any differences relative to the GLM fit earlier? |

This model has a much better fit. That is because we are fitting to a model that has already smoothed out many of the fluctuations in the data. The closer the random forest model is to using (log)linear relationships without interactions, the better the GLM will serve as a surrogate model. In this case, we know the relationship of age to the target is not linear, something the GLM surrogate cannot capture.

### **1.3.15 Local Interpretability** {#1.3.15-local-interpretability}

Local interpretability contemplates why a model makes a prediction for a specific observation. How does this observation compare to a typical observation? Which variables set this observation apart? What contribution did each variable have in determining the prediction for this observation? Locally, an otherwise complex model may behave more intuitively. 

The next two methods introduced address this aspect of explaining model output. The first is a local version of the partial dependence plot. The other one is a surrogate method that approximates the complex model, but only in the vicinity of the observation under consideration.  
Local Interpretability

### **1.3.16 Individual Conditional Expectation** {#1.3.16-individual-conditional-expectation}

**Individual conditional expectation** (ICE) plots follow the same concept as PDPs but at the individual observation level. ICE plots are a local interpretability method. Instead of averaging the marginal effects of a variable, an ICE plot displays the marginal effect for all observations (each observation is represented by a line). This approach solves one of the problems with PDPs: it captures heterogenous effects of interactions. We can see every observation, so we can see if there are different patterns for different observations. 

ICE plots still suffer from the assumption of independence we discussed with PDPs. Other potential downsides are that the plot can become overcrowded – adding transparency to the lines or taking a sample of observations can remedy this – and it can be difficult to see the average among all the lines – simply combine with a PDP to get best of both. Because there are so many lines, plotting two variables is not feasible.  
Individual Conditional Expectation

### **1.3.17 Example: ICE** {#1.3.17-example:-ice}

As expected, the straight line holds for local predictions as well as global predictions. The graph (not shown) does show that the other factors can make significant adjustments to the line, moving it up or down.  
Example: ICE

Component Table21

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 9 to make an ICE plot for the age variable using the ordinary regression model.  |

The trend over age seems to be fairly consistent, though at the older ages there is much more variability due to other factors.

Component Table22

| Type | Callout |
| :---- | :---- |
| Content | The CHUNK also takes a 5% sample of the data and plots those observations. Now run CHUNK 10 to make an ICE plot for age using the random forest model and the sampled data. |

### **1.3.18 Shapley Values** {#1.3.18-shapley-values}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/4.3\_jobaid\_shapley\_values.pdf\]  
**Shapley Values** are a clever way of approaching the task of model explanation. The approach originated as a solution to a coalitional game theory problem. Suppose a team of players is playing some game where they win money. At the end of the game, what is the fairest way to distribute the earnings among the team members? When applied to explaining models, this technique is usually called **Shapley Additive Explanations (SHAP)**. 

To learn more about how this is done, read the job aid provided ( [4.3\_jobaid\_shapley\_values.pdf](#bookmark=id.m935olaizsdd)).  
\[END LINK\]  
Shapley Values

### **1.3.19 Example: SHAP and OLS** {#1.3.19-example:-shap-and-ols}

For the program to work the categorical variable had to be binarized. The CHUNK produces Shapley values for two of the observations in the test set. 

The model predictions for the two observations were 544.2 and 894.6. The SHAP predictions obtained by adding the Shapley values are seen to be identical. The graphs show the contribution of each predictor. The base (called none here and equal to 714.55) is simply the average of the target variable. So, the relative importance here is how each characteristic moved the observation away from this value.  
Example: SHAP and OLS

Component Table23

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 11 to analyze the ordinary regression model. |

### **1.3.20 Example: SHAP and Random Forest** {#1.3.20-example:-shap-and-random-forest}

We now do the same for a random forest model.   
Example: SHAP and Random Forest

Component Table24

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 12 to perform the analysis. |

The model predictions are 528.2 and 1174.6. As can be seen from the graph, the explanation indicates that the random forest model is using age to a different extent than the linear regression model. 

It is possible to aggregate the Shapley values to provide global explanations. To do this it is necessary to obtain those values for all the observations in the training set. This will be illustrated on the next page.

### **1.3.21 Example: Using SHAP for Global Explanation** {#1.3.21-example:-using-shap-for-global-explanation}

We will switch to boosted decision trees to see how global explanations might work.   
Example: Using SHAP for Global Explanation

Component Table25

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 13 to clear the environment and reload and prepare the data. Then run CHUNK 14 to fit a boosted regression tree and then apply SHAP. |

A variable importance plot from the model shows *familyIncome* as most important. Variable importance can also be determined using the Shapley values. Simply sum the absolute values of the Shapley values for each variable and scale by dividing by the total of all the values. This shows *age* and *bmi* as most important, which aligns better with previous importance calculations. 

Because importance is related to contribution to the prediction, it is possible that large target values accompanied by large predictions may distort this calculation.

### **1.3.22 Example: Using SHAP for Global Explanation** {#1.3.22-example:-using-shap-for-global-explanation}

Example: Using SHAP for Global Explanation

Component Table26

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | age |
| Tab 1 Text | age |
| Tab 1 Content |  |
| Tab 2 Title | bmi |
| Tab 2 Text | bmi |
| Tab 2 Content |  |

The output includes the Shapley values for each observation. They can be summed and when the bias is added the prediction results. 

The equivalent of a partial dependence plot can be obtained by taking each value (or range of values) for a variable and obtaining the average Shapley value. For *age* we can see the model makes small predictions for the first age group, higher for the next two. Then a drop off followed by increasing predictions. 

It is also possible to look for an interaction in the predictions. This plot splits each *age* range by *bmi* range. The plot doesn’t show much of an interaction. Note that any interaction we see is in the model, not necessarily in the data (and conversely there may be interactions in the data that are not picked up by the model).

### **1.3.23 Lift and Gain Charts** {#1.3.23-lift-and-gain-charts}

The methods introduced in this section all relate to finding a way to connect the inputs to the output of the model. Another type of explanation (also model agnostic) is designed to show the value of the model in making predictions. We have numeric methods for demonstrating model quality such as confusion matrices (and associated metrics) and mean squared error. 

We now present two graphical methods of demonstrating model quality, lift and gain charts.  
Lift and Gain Charts

### **1.3.24 Lift Charts** {#1.3.24-lift-charts}

The examples shown thus far have been for a regression problem. They will also work with classification problems.  
Lift Charts

Component Table27

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 15 to create a new data set that has a binary target variable, created from the original target variable split at 300, where observations above 300 represent a positive outcome. Two of the previously employed methods are presented. |

An additional model agnostic outcome that is available for classification problems is a **lift char** **t**.\* This method requires only the predicted probabilities of a positive outcome on a holdout/test set. Many models, both simple and complex, can provide these predictions, which can then be used in lift charts to assess model performance. 

\*There are a variety of charts called “lift charts.” One such chart is presented here.

### **1.3.25 Lift Charts** {#1.3.25-lift-charts}

Lift Charts  
A lift chart is created by splitting the data into bins. A typical number of bins is 10\. The assignment to these bins is not random. Rather, the observations with the highest predicted probabilities are placed into the first bin, the next highest are put into the second bin, and so on. With 10 bins, 10% of the observations are placed in each bin. A lift chart compares the cumulative number of positive responses in these bins with the cumulative expected number of positive responses assuming the bins were randomly assigned. 

For example, suppose 300 out of 1,000 observations are positive responses and the data is split into 10 bins. If they are assigned randomly, about 30 would be in each bin. Then the cumulative number of positive responses if the bins are assigned randomly is 30, 60, 90, and so on. For the bin assignments that are ordered based on predicted probabilities of positive outcomes, the first bin will ideally have many more positive responses than if they were assigned randomly. Suppose there are 60 positive responses in the first bin. Then the ratio of the ordered bin to the random bin is 60/30 \= 2. This is the first data point for the lift chart. If the next bin has 40 positive responses, then the cumulative number of responses is 100\. Compared to the cumulative number in the random bins, the ratio is 100/60 \= 1.67. This is the next point of the lift chart. The *x*\-axis then is the bin number and the *y*\-axis is the ratio of cumulative number of positive responses in the ordered bins to the expected number of positive responses in the random bins. 

This chart can reveal model fit because if the model has effectively detected positive outcomes, the lift chart values will be much larger than 1\. Regardless of how good the model is, the lift chart will always decrease toward 1 on the right.

### **1.3.26 Lift Charts** {#1.3.26-lift-charts}

The R program that generated this figure sets the number of “bins” equal to the number of observations. The resulting lift chart converges to 1 as it should. The highest it ever gets is close to 1.5, meaning that the first bin has one and a half as many positive outcomes as the expected amount for a random bin. This suggests that there is some predictive power, especially for the highest predicted probabilities of a positive outcome. Values of the lift chart above 1 suggest a model that is predicting better than random.  
Lift Charts

Component Table28

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 16 to obtain the predictions for the GLM model and to construct a lift chart. |

### **1.3.27 Gain Charts** {#1.3.27-gain-charts}

A gain chart can be compared against the *y* \= *x* line, which is shown in red in the plot. Ideally, the gain line is well above the *y* \= *x* line. In this case it is slightly above the line, suggesting there is a small amount of predictive power.  
Gain Charts

Component Table29

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 17 to construct a gain chart. |

A gain chart is calculated based on the same ordered binning as a lift chart. The lift chart is the ratio of a cumulative number of predicted positive outcomes to the expected number of cumulative positive outcomes from random binning. The gain chart plots the cumulative proportion of predicted positive outcomes against the total proportion of data in each bin. In the example with 300 positive outcomes in 1000 observations, there are 100 in each bin and 60 positive outcomes in the first bin. The cumulative proportion of positive outcomes is 60/300 \= 0.2 and the total proportion of data is 100/1000 \= 0.1. The first point on the gain chart is then (0.1,0.2). The second bin has 40 positive outcomes. The cumulative proportion of positive outcomes is 100/300 \= 0.33 and the proportion of total data is 200/1000 \= 0.2, so the second point on the gain chart is (0.2,0.33). This continues through all the bins.

### **1.3.28 Difference Between Gain Chart and ROC Curve** {#1.3.28-difference-between-gain-chart-and-roc-curve}

An ROC curve is very similar to a gain chart and it has the same purpose, visually showing model fit. The points on the gain chart have a more specific interpretation. Specifically the (x,y)-point represents that 100 *x*% of the data has 100 *y*% of the true positives. The ROC curve is similar but does not have that simple interpretation. Instead, the ROC curve is often summarized into a single interpretable statistic, the AUC, which can be used to compare model fits. For visual comparisons, they will likely tell you the same story and you would not need both. For a single metric to compare models with, using ROC to get AUC is better. For reporting predictive power of the model in terms of how well we can predict true positives, the gain chart is better.  
Difference Between Gain Chart and ROC Curve

### **1.3.29 Gain Chart** {#1.3.29-gain-chart}

Both lift and gain charts can be used to compare models.   
Gain Chart

Component Table30

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 18 fits a neural network model to the data and calculates the predictions. |

Because lift and gain charts are model agnostic, the fact that predictions between the GLM and neural network models are generated in completely different ways is irrelevant. In both cases, the model that has larger values for the lift and gain charts would be a better model for the data.

Component Table31

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 19 to plot the gain chart for both the GLM and neural network models. |

The gain chart lines are nearly right on top of each other. There does not seem to be a predictive advantage in this case for the more complex model.

## ***1.4 Reports*** {#1.4-reports}

### **1.4.1 Section 4.4 Learning Objective** {#1.4.1-section-4.4-learning-objective}

Reports 

Component Table32

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 4.4 Learning Objectives**  Write reports that effectively communicate with the intended audience.  |
| Footer | Panel Footer |

### **1.4.2 Introduction** {#1.4.2-introduction}

This section provides guidelines for writing reports both in practice and for answering questions on Exam ATPA.  
Introduction

### **1.4.3 ASOP 41** {#1.4.3-asop-41}

\[BEGIN LINK \-https://www.soa.org/globalassets/assets/Files/static-pages/sections/entrepreneur-innovate/Stonewall-ASOP41DosDonts.pdf\]

Actuaries are required to follow published standards of practice where applicable. These are usually developed by the appropriate national organization in the actuary’s country. In the United States, standards are brought forth by the Actuarial Standards Board. Among those is Actuarial Standard of Practice (ASOP) 41 (Communication), [asop041\_120.pdf](#bookmark=id.r6xnvl7wmbon). Although this standard only applies to credentialed actuaries practicing in the United States, similar standards apply elsewhere. Regardless, there is a lot of good advice in this standard. 

Alan Stonewall wrote an article in 2004 stating that “ASOP 41 has more day-to-day applicability to our work as actuaries than any other actuarial standard of practice.” More on ASOP 41 can be found on the SOA website ( [Stonewall-ASOP41DosDonts.pdf](#bookmark=id.e9fi66sz8te)). 

While ASOP 41 has been revised since this article was written, it contains valuable advice. However, when it comes to complying with ASOP 41 in practice, as well as any other ASOP, you should always refer to the most current version.  
\[END LINK\]  
ASOP 41

### **1.4.4 Reports** {#1.4.4-reports}

Part of ASOP 41 dictates that an actuarial communication should be done in physical or electronic writing unless agreed upon specifically by both parties. Knowing what to include in an actuarial communication, which we are referring to as a report, is important. For Exam ATPA, you will be asked to prepare data and to build and use predictive models. No code will be expected as a deliverable. Instead, you will have to show that you built appropriate models through a series of tasks answered in the format of report components. 

We will first discuss a series of principles that are useful when writing reports. Then we will explain how reports will differ by audience.  
Reports

### **1.4.5 Reproducibility** {#1.4.5-reproducibility}

Reproducibility  
Some of the observations with missing data were removed while others were imputed.  
Reproducibility is the idea that your methods can be repeated exactly by someone else and the same results can be achieved. For example, the action described by the following statement about preparing data is not reproducible:   
Observations with missing values for the target variable were removed. Missing values for Variable 1 were imputed.  
Observations with missing values for the target variable were removed. This reduced the data set from 780 rows to 712 rows. There were also missing values in Variable 1\. These values were imputed on the full data set using a linear regression imputation using Variables 2 and 3 as predictors. For example, observation 4 had a missing value for Variable 1 and the imputed value was 14.2. Code is supplied in the appendix.  
While this is useful information to know, if your goal is reproducibility, we need more detail. Something like this would be better:  
Clearly, this better indicates how to repeat your work, and yet it still isn’t completely reproducible. What imputation method was used? Are there important settings or details for the imputation method? It is also useful to provide details to help someone who is trying to reproduce your work to know they are on the right track. Consider the following description:   
Imagine that you are receiving this information. You now know how to repeat the process that was performed. Also, you have some exact values to check. This can be important for a few reasons. Perhaps you have made a mistake and these values can help you identify it. Or maybe the person who gave you this report has written what they intended to do, but they made a mistake, and again these details can help you identify that.

### **1.4.6 ATPA Assessment and Reproducibility** {#1.4.6-atpa-assessment-and-reproducibility}

ATPA Assessment and Reproducibility  
In practice, reproducibility is important. Your work may be carried on after you leave and the next person should be confident they are starting where you left off. Or there may be a change in systems or software. For example, the random number generator in R was changed. As a result, running old code on a newer version of R could produce different results. If the original work should have been reproduced it becomes easier to uncover the reason the output changed. 

For the ATPA assessment graders will not reproduce your results with your code or their own. Therefore you should provide sufficient detail so that the graders understand what you did to the extent that they could write code to closely mimic your results.

### **1.4.7 Exercise 4.4.1** {#1.4.7-exercise-4.4.1}

Using your knowledge of these data preparation and modeling methods, state which details might be missing from these statements that would make them reproducible. Also, state which additional details might help identify if reproduced work is being done correctly. Think about your response before clicking on the bar at the right to see a possible answer. 

1. The two data sets were joined using ID number as a primary key.  
2. The income variable was given a log transform to account for outliers. There were still some extreme values even after the transformation and so these records were removed.  
3. A Bayesian linear regression model was fit to the data.  
4. The models were compared using mean squared prediction error on a holdout set.

Exercise 4.4.1

Component Table33

| Type | Tabset |
| :---- | :---- |
| Tabs | 4 |
| Tab 1 Title | Show Answer 1 |
| Tab 1 Text | Show Answer 1 |
| Tab 1 Content | Missing details include what kind of join it was (e.g., inner or full). Other helpful information would be how many observations are in the final data set after the join. There are other details that are important to consider when performing a join, such as if there are any duplicate variables or any mismatched key values. It would be important to know that these were checked and cleared or fixed in some way. |
| Tab 2 Title | Show Answer 2 |
| Tab 2 Text | Show Answer 2 |
| Tab 2 Content |  Missing details include how many records were removed and what the exact criteria were for removing these records. Also, a plot of the transformed variable would help confirm the process. |
| Tab 3 Title | Show Answer 3 |
| Tab 3 Text | Show Answer 3 |
| Tab 3 Content | Missing details include the variables used in the model, both the target and the predictors as well as the choice of prior distribution (e.g., default non-informative or horseshoe prior). It would also be helpful to know whether data was fit to all or just some of the data. Model output would help confirm the process. |
| Tab 4 Title | Show Answer 4 |
| Tab 4 Text | Show Answer 4 |
| Tab 4 Content | Missing details include how the holdout set was created and what the size of it is. The resulting MSE values will help confirm. Because random selection plays a large role in sampling the training and test sets, supplemental code with a seed would also be useful.  |

### **1.4.8 Justification** {#1.4.8-justification}

Other people may be placing a significant amount of trust in your work. For this reason, they should understand your actions and you should justify your decisions clearly. 

One helpful practice when justifying a decision is to describe the consequences of reasonable alternatives. For example, suppose you are building an additive model and you decide that the effect for Variable 1 should be smoothed but the effect for Variable 2 should be linear. You might justify this by saying something like:  
Justification  
Variable 1 appears to have a non-linear relationship with the target while Variable 2 appears to have a linear relationship and this allows the model output for Variable 2 to be more interpretable.  
If we made both variables smooth, we are adding unnecessary complexity to the model that makes it harder to explain and runs the risk of overfitting; by choosing both variables to be linear we ignore the potential non-Iinear relationship between Variable 1 and the target, which can result in a poor model fit.  
You can strengthen your justification by adding the consequences of the alternatives:

### **1.4.9 Justification** {#1.4.9-justification}

Justification  
By imputing the missing values of Variable 1 using linear regression we can use relationships between Variable 1 and the other variables to fill in missing values that are close to what they would be if they were observed.  
We found that Variable 1 is a meaningful predictor of the target variable, so removing the variable would negatively impact the accuracy of our predictions. We did not choose to use a mean imputation because it is not as accurate as a linear regression imputer would be. We expect other imputation methods such a K-nearest neighbors to perform similarly, but they are less intuitive and harder to apply to new observations.  
When available, you should have numeric evidence to support your claim. For example, you might decide to choose one model over another based on a metric that is compared over several models. Then, when you are addressing alternatives in your justification, you can report the values of the metrics.  
Another example is the decision to impute data using a linear regression imputation. You might justify this by saying something like:  
Then you could discuss the consequences of the alternative actions. You might say:

### **1.4.10 Exercise 4.4.2** {#1.4.10-exercise-4.4.2}

For each of the following justifications, determine what alternatives could be discussed. You don’t have any information on the alternatives, so you don’t have to make up information describing why they were not chosen. Simply identify the alternatives. Think about your response before clicking on the bar at the right to see a possible answer. 

1. To create a variable that has fewer factor levels for the generalized linear model, I combined the ten different factor levels of the weather variable into five factors: sun, cloudy, rain, snow, and the remainder of the smallest six factor levels into an “Other” category.  
2. For the Bayesian regression model, we chose to use a horseshoe prior for the coefficients.

Exercise 4.4.2

Component Table34

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Show Answer 1 |
| Tab 1 Text | Show Answer 1 |
| Tab 1 Content | The alternatives include not combining the factor levels or combining them in a different way (resulting in four or six factor levels instead of five perhaps).  |
| Tab 2 Title | Show Answer 2 |
| Tab 2 Text | Show Answer 2 |
| Tab 2 Content |  The main alternative that was introduced in Module 3 was a non-informative prior. |

### **1.4.11 Justification Discussion** {#1.4.11-justification-discussion}

Justification Discussion  
If variables are not combined there will be factor levels in the model with very few observations, which might result in unreliable coefficient estimates and *p*\-values.  
There are 70%, 85% and 88% of the data in the first three, four, and five factor levels respectively. We are uncomfortable combining 30% of the data into an “Other” category and so we needed more than three named factor levels and an “Other” category. The difference in the amount of data in the first four and five factor levels was so small that we chose to use the one with fewer factors for simplicity.  
Item 2 from Exercise 4.4.2 could be justified by noting this consequence of the alternative:  
To continue the idea of justifying by explaining the consequences of the alternatives, the consequence of the first alternative in Item 1 of Exercise 4.4.2 (not combining factor levels) could be stated:  
The consequence of the second alternative (choosing four or six factor levels) could be justified using numeric values that have been made up for this example:  
This could also be justified numerically, such as the following:  
An alternative is a non-informative prior that does not perform any simultaneous inference by shrinking insignificant parameters to near zero. Because we want only significant variables to affect predictions, we chose to use a horseshoe prior.  
“Using a horseshoe prior and then predicting on a holdout set gave an MSE of 15.6 while using a non-informative prior gave an MSE of 17.9, so the horseshoe prior was chosen. “

### **1.4.12 Data Dictionaries and Summaries** {#1.4.12-data-dictionaries-and-summaries}

Another feature that is useful when constructing a report is providing a data dictionary. This is different from a summary. A data dictionary is a list of all the variable names in a data set (the names as they appear on the columns of the file) along with all relevant information that will help someone who wants to use the variables in a predictive model. 

For example, a variable name in a data set might be *lawyer\_used*. This variable name could indicate that it is a binary variable specifying whether or not a lawyer was used for a particular observation. Alternatively, this variable name could indicate that it is the name of the lawyer. A data dictionary can be in the form of a table or list. It is most useful when it includes the following: (1) variable name, (2) data type, (3) a brief description, and (4) a range of values for a continuous variable or the number of factor levels if a factor variable. For example, here is a data dictionary for a made-up data set:  
Data Dictionaries and Summaries

| Variable Name | Data Type | Description | Values |
| ----- | ----- | ----- | ----- |
| *dog* | Binary | A logical for if an individual owns a dog | 0 or 1 |
| *yard* | Numeric | The size of the individual’s yard in square feet | From 0 to 43,000 |
| *car* | Factor | A variable for the type of car an individual drives | 7 levels, e.g., sedan, truck, van |

Your data dictionary may have more or different elements. There are three possible times you may want to provide a data dictionary: (1) on receipt of the data, to help someone who will be working with the raw data, (2) after cleaning and transforming the data, to help someone who will be building models, and (3) after modeling is complete, to help someone who wants to interpret or deploy the model. For the third case, only variables used in the selected model will be included. Deciding which data to use to make a data dictionary depends on what you expect your audience to do with the data. If you expect someone to clean the data themselves, the first is used. If this is for someone to test different models on the data, use the second one. If you only needed to understand the variables in a final predictive model, the third will become most useful.

### **1.4.13 Summary Statistics** {#1.4.13-summary-statistics}

Data summaries, both tabular and graphical, are useful for a more detailed look at the data. They are also often necessary when justifying certain transformations or modifications to the data, so data summaries and plots can be useful both before and after data cleaning, transformations, or feature generation. 

A collection of summary statistics can be found in R using summary() and in Python using describe()from the **pandas** library. These give values for continuous variables such as minimum, maximum, and mean. For categorical variables, summary() in R gives the number of observations in the top several categories and describe(include=\["object"\]) in Python provides the number of unique categories and the category with the most occurrences. While copying and pasting output directly from the output provided to a report document is easy, this information can also be placed in a table for a cleaner document and more readability. For example, the continuous variables from the dental data set from Section 4.3 can be summarized in the table on the right.  
Summary Statistics

|  | *Target* | *Age* | *Bmi* | *familyIncome* |
| ----- | ----- | ----- | ----- | ----- |
| Mean | 716 | 38.63 | 26.03 | 79,366 |
| Median | 268 | 38 | 25.20 | 62,000 |
| Std Dev | 1,442 | 21.80 | 6.80 | 68,383 |
| Range | \[5, 38,432\] | \[6, 85\] | \[9.2, 141.3\] | \[26, 492,501\] |

At a glance we can see potential skewness in the target variable because of the large disparity between the mean and median. This can then lead to a plot showing the data followed by a transformation intended to stabilize the target variable for modeling purposes. 

### **1.4.14 Types of Written Reports** {#1.4.14-types-of-written-reports}

There are many different types of written reports. These reports are produced for different purposes and different audiences. The following types of reports are described in this section. 

* A **technical report** is a report on findings from an analysis that will include precise model details and a thorough examination of the model output.  
* A **memo** is a less formal report that can contain any necessary information for a specific audience.  
* An **executive summary** is a high-level overview of the most important details pertaining to a business problem. It can stand alone or be part of a technical report.

Frequently a report is in the form of a presentation or a set of slides. While these aren’t considered explicitly in these modules, there are several principles that should apply in those cases as well.  
Types of Written Reports

### **1.4.15 Technical Report** {#1.4.15-technical-report}

The exact structure of a technical report will vary by personal convention, a company’s convention, or by the business problem itself. A full technical report will often contain the following elements. 

1. Executive Summary  
2. Introduction  
3. Data  
4. Models  
5. Summary  
6. References  
7. Appendices

For Exam ATPA, you will not need to write a full technical report, but rather will be asked to provide pieces of what could become a technical report. For example, you might be asked to present the work you did to prepare the data for a predictive model, which might comprise the data section of the technical report. 

We will go into more detail as to what goes into data and models sections of a report for each respective audience later in this section as well as how to write an executive summary. The introduction and summary sections are important and yet brief, and the contents depend a lot on writing style. Typically, an introduction states the purpose of a report and lays out the contents. A summary will review the major points and make next steps clear.  
Technical Report

### **1.4.16 Structure of Data and Models Sections** {#1.4.16-structure-of-data-and-models-sections}

We will discuss the data and models sections by audience later in this section. Regardless of what goes into these sections of a technical report, some simple structure can help organize the overall message. Exact elements will vary by business problem and by the extent of the data and modeling work you perform. You can always provide an introduction that highlights the goal that you are trying to accomplish. Each section can also have a summary at the end that provides the relevant information from the section at a glance.  
Structure of Data and Models Sections

### **1.4.17 Memo** {#1.4.17-memo}

A memo is an unstructured communication. This might be a passing of information from one individual to another in preparation for writing a full report. For ATPA, you might be asked to write a memo to an individual on a specific topic. This would not be a broad question such as describing what was done to the data, but perhaps something more specific such as describing how variable selection differs in a Bayesian model versus a GLM or a neural network.   
Memo

### **1.4.18 Executive Summary** {#1.4.18-executive-summary}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/4.4\_business\_problem.pdf\]  
Despite the name, the audience of an executive summary need not be limited to executives. It is a more formal exposition that is brief yet contains all the most important details. It also can be attached at the beginning of a technical report as a high-level summary of the most important details in the technical report. 

The business problem should be cited frequently in a technical report or a memo. The executive summary, though, should be extremely focused on the business problem, only including information that will help to understand the problem and how it was addressed. 

Conside r this business problem that is adapted from SOA Exam PA in December 2020, [4.4\_business\_problem.pdf](#bookmark=id.us52bibk90h9). The executive summary for this problem should be focused on the business problem of identifying factors related to pedestrian activity. 

[4.4\_executive\_summary.pdf](#bookmark=id.73boz016oi0b) contains a modified version (to fit the above description) of the executive summary that was provided as a solution for this problem.  
\[END LINK\]  
Executive Summary

### **1.4.19 Executive Summary** {#1.4.19-executive-summary}

We will identify the elements of this executive summary and describe why they are important to include.  
Executive Summary

Component Table35

| Type | Tabset |
| :---- | :---- |
| Tabs | 6 |
| Tab 1 Title | Statement of business problem – Paragraph 1 |
| Tab 1 Text | Statement of business problem – Paragraph 1 |
| Tab 1 Content | It is important that you state the business problem as you understand it at the very beginning to establish the context for the rest of the document.  |
| Tab 2 Title | Description of Data Sources – Paragraph 2 |
| Tab 2 Text | Description of Data Sources – Paragraph 2 |
| Tab 2 Content | The sources of the data should be established as well as a brief description of the data. This can be described using a graph, but only if the graph gives some information that is helpful to understanding how the data applies to the business problem. In this example it is important to be clear when and where the data was collected. |
| Tab 3 Title | Description of the Data Preparation – Preparing for Modeling Section |
| Tab 3 Text | Description of the Data Preparation – Preparing for Modeling Section |
| Tab 3 Content | This is not necessary for every executive summary. When included, it should focus on what steps were taken to make the data more suitable for solving the business problem. This should also include any limiting assumptions that were made when preparing the data and any ethical concerns. In this case, the business problem is identifying important features, and so the author describes how factors were modified so that when important features are discussed the reader can understand them. |
| Tab 4 Title | Description of the Models Used – Model Selection Section |
| Tab 4 Text | Description of the Models Used – Model Selection Section |
| Tab 4 Content | The final model or models should be stated and briefly described. The decision regarding the selected model should be justified and the strengths and the weaknesses of the model should be stated. As with the data, any limiting assumptions and any ethical considerations should be included. In this case, the author decided to justify the decision of the model choice by describing three different models that were considered and why they selected the final model out of the three, and in doing so also stated the strengths of the model for solving the business problem.  |
| Tab 5 Title | Model Results – Model Section |
| Tab 5 Text | Model Results – Model Section |
| Tab 5 Content | The results of the model should be reported in terms of what is most important in the business context. In this case it is the important factors and how they relate to pedestrian traffic. If there are any helpful plots or tables that help illustrate these results, they can be included. These results should be interpreted in a clear manner. Because the selected model was a decision tree, the author could include specific comments and examples. For Exam ATPA, the models may be too advanced to provide a summary for a non-technical audience in the executive summary. However, this is where model-agnostic methods can be extremely useful in describing the relationship between factors and the target or in displaying the goodness of the model fit. You may be asked to describe how to interpret the model in more detail in other parts of the exam. |
| Tab 6 Title | Recommendation – Insights and Next Step Section |
| Tab 6 Text | Recommendation – Recommendation Section |
| Tab 6 Content | You should give a clear and decisive recommendation along with the level of certainty you have about the recommendation. This is often the most important part of an executive summary. In fact, if the other information provided in other parts of the executive summary does not serve to support this final recommendation, you should consider removing it.  |

### **1.4.20 Making the Final Recommendation** {#1.4.20-making-the-final-recommendation}

The final recommendation should address the business problem and is the single most important part of an executive summary. An effective way to state a final recommendation is to have the following elements: 

1. Clearly state the recommendation: The recommendation should be easy to find. It could easily be found if it begins with something like “We recommend that…” or “Our final recommendation is…”  
2. Cite relevant model-based evidence: Repeat the main reasons why you have made this recommendation. This is likely repeating other elements of your report, which is okay. Be specific and brief.  
3. Acknowledge alternatives: Your recommendation should be your first choice, but perhaps there is a second choice that is almost as good or that emphasizes a different modeling strength. These alternative choices can be included as part of the final recommendation.  
4. Describe model limitations: Being honest about what your model does not do well is important. If your model is used by others, the people using it to motivate their decisions should know what it cannot do.

Making the Final Recommendation

### **1.4.21 Report Writing by Audience** {#1.4.21-report-writing-by-audience}

We will continue to work with the paradigm that we have three different audiences: 

1. A peer who has a similar knowledge of predictive modeling as you;  
2. A supervisor who knows some predictive modeling but not enough to be able to build models without help; and  
3. An executive who understands the terminology of the business context but has no explicit knowledge of predictive modeling methods.

As stated previously, this is an oversimplification. There are many considerations discussed previously as to the nature of the audience. However, the remainder of this section will rely on this framework. 

We will now provide some guidance on what types of specific details these three audiences might want to know about ethics, data, and models. This advice will not be strictly applicable in all cases, but it provides a framework to start from that you can modify as the situation needs.  
Report Writing by Audience

### **1.4.22 Technical Peer** {#1.4.22-technical-peer}

Reporting on Ethics and Regulation 

You will need to justify your reasoning for data and model choices. This will include explaining choices you made that were influenced by ethical considerations and regulations. These explanations can be brief and might include a reference. There will be situations where you specifically have a more detailed description of ethical considerations or regulations with a technical peer, but in many cases these discussions are more commonly found in correspondence with a supervisor or executive.

Reporting on Data 

Reproducibility is important when discussing methods that were used to transform data for a predictive model. This includes justifications for these methods at all steps. This would also be an appropriate place to provide a data dictionary. Include plots and tables that help justify the modifications made to the data as well as exploratory analysis for the final data. Typically, a technical peer can make more sense out of a large number of plots and tables than a less technical audience, who might be better served with fewer but more directed figures.

Reporting on Models   
Reproducibility in model building is extremely important. Listing the models that were run on the data and whether or not they were successful in modeling the data can help save time later if a peer wants to try the same thing. Include goodness of fit metrics, *p*\-values, and other inferential values. Explore post-model analysis. Try different ways to view and display model results. This might take the form of some of the model-agnostic methods discussed in the previous section. Again, it is easier for a technical peer to comprehend a large volume of technical information and it can sometimes be very helpful to be as detailed and thorough as possible while keeping the document clean and readable. In both data and code work, code can be provided and referenced. It is also reasonable for small code chunks to be included in the report itself when it could be helpful describing a process.  
Technical Peer

### **1.4.23 Partially Technical Supervisor** {#1.4.23-partially-technical-supervisor}

Reporting on Ethics and Regulations 

In Module 1 we established an ethical framework. This includes fairness, safety, transparency, and accountability. We established ways to address each of these principles. When discussing a particular business problem with a supervisor, each of these should be addressed. Ethical mistakes often have the most extreme consequences. It should be evident that each aspect of our ethical framework has been addressed. Likewise, it should be evident that regulations that could influence the data preparation and modeling steps have been considered.

Reporting on Data 

The choices that led to the final data should be listed and justified. A full list of variables should be included as well as a brief description. A full data dictionary can do this, although details such as data type are less important, depending on the situation. Include figures based on the final data to show that it is appropriate for the models we want to try and suitable to address the business problem. For example, a plot of a predictor variable against a target variable can demonstrate that there is a non-linear relationship and therefore we want to try an additive model or add higher order terms as opposed to fitting a strictly linear model.

Reporting on Models   
While you need less detail for a partially technical supervisor than a technical peer, you should still be thorough. Provide the most important pieces of information from the model output. This could include coefficient estimates, *p*\-values, predictive scoring measures, and so on. Things that are most important are evidence that the model is good and information that is relevant to addressing the business problem. If there are figures or tables that help demonstrate this, they should be included.  
Partially Technical Supervisor

### **1.4.24 Non-technical Executive** {#1.4.24-non-technical-executive}

Reporting on Ethics and Regulations 

All decisions that have an ethical consequence or are influenced by regulations should be stated. It is perhaps less important to prove that you followed a rigid framework as you might to a supervisor, but you should be honest about where ethics and regulation influenced decision making and in what ways it was ensured that ethical principles and regulations were accounted for.

Reporting on Data 

Both data sources and a general overview of the data are important. You do not need to list all the variables, especially if there are a large number of them, but make clear what the target variable is and identify some key predictors that are used to explain it. Plots and figures can be included but only if they help to make a specific point that is relevant to the business problem. An example of this might be a plot that highlights a weakness of the data that diminishes its suitability for the business problem.

Reporting on Models   
The final model should be named along with justification as to why the model was chosen. Details that are most important to include are those that help support a final recommendation, such as why a specific model with the chosen predictor variables are best. You do not need to describe exactly how the model works, especially for the advanced models used on ATPA, but a description of features of the model as well as strengths and weaknesses is useful. For example, in a stacking model you could state that the model is a composite of several different models along with a brief description of how predictions are made.  
Non-technical Executive

### **1.4.25 Conclusion** {#1.4.25-conclusion}

This section covered some important principles about writing reports that should be applied on Exam ATPA and can also be relevant outside of the exam setting. While writing can be subjective to an extent, these principles discussed here should be considered in your technical writing.   
Conclusion

## ***1.5 Model Selection Case Study*** {#1.5-model-selection-case-study}

### **1.5.1 Section 4.5 Learning Objective** {#1.5.1-section-4.5-learning-objective}

Model Selection Case Study

Component Table36

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 4.5 Learning Objective**  Recommend the best model for a given problem.  |
| Footer | Panel Footer |

### **1.5.2 Introduction** {#1.5.2-introduction}

In this section we provide a case study that compares the basic models and those introduced in Module 3 along the following five dimensions of model comparison: 

1. Accuracy  
2. Explainability  
3. Stability  
4. Analytical Effort  
5. Computational Efficiency

The data set and the application are simple, as are the model fitting and checking. The focus of the case study is on model comparison and selection.   
Introduction

### **1.5.3 Evaluating a Modeling Method** {#1.5.3-evaluating-a-modeling-method}

Every modeling method has strengths and weaknesses, and every modeling problem has objectives to be met by the selected method. The challenge is to find a method whose strengths aligns with the problem’s objectives. For example, if the objective is to determine the drivers of the target variable, then methods that that are highly interpretable will be favored. 

In this section we will introduce five dimensions on which a model may be evaluated. After describing each of them, a case study will be introduced that provides an opportunity to evaluate candidate models against each of the dimensions. 

The relative importance of the five dimensions will depend on the business problem. For example, if the model is going to only be developed by highly skilled technicians, then the analytical effort is less important. As another example, if the model will need to be run often on large datasets and return answers quickly, computational efficiency becomes more important.  
Evaluating a Modeling Method

### **1.5.4 Accuracy** {#1.5.4-accuracy}

**Accuracy** is the expected quality of the predictions made by the model. There are many measures describing the predictive power (or the prediction error) when evaluating models on the testing and validation sets. Mean squared error and AUC are two examples. The measure to use should be consistent with the modeling objective and then applied consistently across all candidate models. 

One difference for this dimension versus the others is that there is no hierarchy of accuracy because a model’s accuracy will depend on how well it aligns with the process being modeled. For example, if the process is truly linear, a linear model may be more accurate than a neural network. But for complex relationships, a neural network may be more accurate. 

As will be seen in the case study (and we have seen in many previous examples), accuracy can be measured and hence candidate models can be formally ranked on this dimension.  
Accuracy

### **1.5.5 Explainability** {#1.5.5-explainability}

**Explainability** represents the degree of difficulty in understanding the relationship between the input variables and the response variable. As has been seen, some models are easy to explain (e.g., single decision trees and linear models) and some are challenging, requiring methods such as partial dependence plots or Shapley values to provide insights (e.g., random forests and neural networks).  
Explainability

### **1.5.6 Stability** {#1.5.6-stability}

**Stability** refers to the amount of change expected if you were to refit the same model with new data. This is the same as variance, a familiar concept. Low variance (provided it is not achieved at the expense of high bias) is not only good when developing the initial model but is also valuable when the model is recalibrated using updated data. If the parameters change, having high stability implies that the changes are due to actual changes in the underlying environment and not just random fluctuations. 

Note that stability is not the same as the accuracy of predictions, which always balances variance and bias.  
Stability

### **1.5.7 Analytical Effort** {#1.5.7-analytical-effort}

Analytical effort refers to the time and human resources required to build the model. Note that analytical time and effort also depends on what tools are available and the skill level of the analysts involved. As you have likely seen, doing analytics on a personal computer may lead to long run times that lead to extra time needed by the analysts. Access to distributed or cloud-based computing may make this dimension less important. 

Another aspect of effort is that required by the analytics team. Some models are simple to implement and tune while other require significant effort and expertise.  
Analytical Effort

### **1.5.8 Computational Efficiency** {#1.5.8-computational-efficiency}

**Computational efficiency** refers specifically to the speed and computational resources required to apply the model to new data. An automated underwriting system should respond quickly and use limited resources. Users want quick results and the system may have to handle a large number of quotes. In contrast, a quarterly analysis can use significant resources and run overnight. 

While both analytical effort and computational efficiency can relate to computer capacity and speed, there is a key difference. Analytical effort applies at the model building stage where there may be a large amount of data and multiple runs needed to tune the model, consuming a lot of human resources. Computational efficiency relates to running the model a single time on a modest data set.  
Computational Efficiency

### **1.5.9 Case Study Description and Data** {#1.5.9-case-study-description-and-data}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/bodyfat.csv\]  
Bodyfat, the percentage of a person’s body that is fat, is an important health factor. To accurately measure it, you need specialized equipment that is expensive and hard to find. Our goal is to build a model that uses simple body measurements to accurately approximate bodyfat. At a minimum, it should be possible to implement the model in an app or, if simple enough, give the formula directly to practitioners and the general public.\*   
The dataset ( [bodyfat.csv](#bookmark=id.bd95copmfer6)) provides 252 observations of men with the following variables: 

* *ID*  
* *BodyFat* – Bodyfat percentage measured using underwater weighing. The response variable.  
* *Weight* – in pounds  
* *Abdomen* – Size of the abdomen (circumference in centimeters)  
* *Forearm* – Size of the forearm (circumference in centimeters)  
* *Wrist* – Size of the wrist (circumference in centimeters)  
* *State* – State of residence (either A, B, C, or D)

\[END LINK\]  
Case Study Description and Data  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_4\_5\_r.rmd\]  
This dataset with observations on 252 men was adapted from the dataset found here ( [https://www.kaggle.com/fedesoriano/body-fat-prediction-dataset](#bookmark=id.ou73yb6tzvlf)). The *State* variable was added to have a factor variable related to the response with which to work. It does not represent any actual states nor is it reflective of any actual relationship between state and bodyfat. At this time download the .Rmd file for this section ( [atpa\_4\_5\_r.rmd](#bookmark=id.84sqak7g6m0) or [atpa\_4\_5\_python.rmd](#bookmark=id.mqn1fcsit69w)).  
\[END LINK\]

Component Table37

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 1 to read in the data, one-hot encode the factor variable, perform a simple exploratory data analysis, and split it into train and test sets.  |

\* A commonly used approximation to body fat is the body mass index (BMI). The formula is BMI \= weight (in kilograms) divided by the square of height (in meters). However, BMI is considered to be a very poor approximation in that it cannot distinguish between fat and muscle (Roberts, 2020).

### **1.5.10 Exploratory Data Analysis – Continuous Predictors** {#1.5.10-exploratory-data-analysis-–-continuous-predictors}

We first plot the quantitative predictors ( *Abdomen*, *Forearm*, *Weight*, and *Wrist*) against *Bodyfat* to get some understanding of the univariate relationships and to check for unusual observations. The variables appear to be relatively linearly related to *Bodyfat*, especially *Abdomen* and *Weight*. There is one observation (ID \= 39\) that could use some additional scrutiny. The individual’s weight (363) and abdomen (148) are much higher than the rest of the sample, but the forearm, wrist, and bodyfat measurements are much closer to the rest. We decided to leave that observation in, but it could be removed.  
Exploratory Data Analysis – Continuous Predictors

### **1.5.11 Exploratory Data Analysis – Factor Predictor** {#1.5.11-exploratory-data-analysis-–-factor-predictor}

Exploratory Data Analysis – Factor Predictor

Next, we make side-by-side boxplots to see the distribution of bodyfat by state. It appears that state B has the lowest bodyfat on average, while the other three states’ averages are rather close. It is also possible that state D has more variation than the other states.

### **1.5.12 Exploratory Data Analysis – Target Variable** {#1.5.12-exploratory-data-analysis-–-target-variable}

Exploratory Data Analysis – Target Variable

A histogram of *Bodyfat* shows that the distribution is reasonably symmetric. This makes the Gaussian distribution a plausible assumption for a linear model. Because the distribution assumption is conditional on the predictors, it can only be checked after the model is fit. 

There appears to be an outlier or two, but we have elected to keep them in the data set. Where a link function is needed, the identity link will be used. This will lead to simpler explanations of the resulting model, but we will need to be confident that the model does not produce negative predictions.

### **1.5.13 Models** {#1.5.13-models}

We will fit the following models to the bodyfat data set (CHUNKs 2-7). See commentary in the code regarding modeling choices made. We have already reduced the dataset to only the predictor variables with a significant impact. In practice, you will need to do that before fitting candidate models. 

Two models not tried were random forests and tree-based gradient boosting machines. Given the business problem, the fact that these models could not be easily programmed into an app makes them unsuitable for consideration. While the linear regression model used here is a basic model, the comments in this section apply equally to GLMs, including those using regularization for coefficient estimation.  
Models

Component Table38

| Type | Callout |
| :---- | :---- |
| Content |  Null model – Simply the mean bodyfat of the training set (CHUNK 2\) Linear regression (CHUNK 2\) – All variables were significant, and the residual and q-q plots indicate that the distribution choice (Gaussian) was reasonable. Regression tree (CHUNK 2\) – The tree was pruned to reduce overfitting. GAM (CHUNK 3\) – None of the variables look to have an extremely strong nonlinear trend in the univariate plots, but just in case this model may outperform the linear model we first fit one using smooths for all four continuous variables. All of the smooths are significant, except for *Forearm*, so the model used for prediction will only have smooths on the other three quantitative variables. Linear mixed model (CHUNK 4\) – *State* is a random effect because we are assuming that states A, B, C, and D are not the only states where we will use this model. Neural network (CHUNK 5\) – Investigated models with one and two hidden layers The model with two layers and 10 and 9 neurons produced the smallest cross validation error. Bayesian regression (CHUNK 6\) – All variables are significant (the credible intervals do not include zero). Stacked model (CHUNK 7\) – Stage-0 models are linear regression, single regression tree, and neural network. The stage-1 model is linear regression using only the stage-0 models as predictors. The stage-0 neural network does not make a significant contribution to the stage-1 model, so is dropped.  |

### **1.5.14 Accuracy** {#1.5.14-accuracy}

1. Mixed model (RMSE \= 2.567)  
2. Bayesian regression (2.573)  
3. Linear regression (2.575)  
4. GAM (2.853)  
5. Stacked model (3.156)  
6. Neural network (3.227)  
7. Regression tree (4.136)  
8. Null model (8.122)

Accuracy

Component Table39

| Type | Callout |
| :---- | :---- |
| Content | In this case we compared the root mean squared error of the various models on the test set and found the following results (CHUNK 8). |

Of the five model comparison dimensions, accuracy is the one that will change the most from application to application. You can use many different metrics to measure accuracy.  
As noted earlier, accuracy is not necessarily a general property of the model but relates to the model and the data. In this case the mixed model, Bayesian regression, and linear regression models have similar performance, and so any of them might be a candidate for being the final choice. Single trees are often poor predictors when most of the variables are continuous, and that is the case here. 

The stacked model performed poorly and worse than one of its stage-0 components, linear regression. This may be due to overfitting where the root mean squared error against the training data was better than that for the plain linear model but then underperformed against the test data. 

Finally, it is comforting to know that whichever model is selected, it will be clearly better than having no model. 

The two models not fit (random forest and gradient boosting machine) were not tested for accuracy. When discussing the other four dimensions, they will be included.

### **1.5.15 Comments on the Remaining Dimensions** {#1.5.15-comments-on-the-remaining-dimensions}

Before discussing the other four dimensions, a clarification regarding stacked models is in order. For a given stacked model, the ratings will depend on the models selected for the stage-0 components. In setting the ratings for stacked models on the following pages the ratings of the stage-0 models will be ignored and it is assumed that the stage-1 model is relatively simple, such as a linear model.

Also, note that a ranking of "High" does not mean a lot, but rather that the method scores well on that dimension. For example, when applied to Analytical Effort it means relatively little effort (not high effort).

Comments on the Remaining Dimensions

### **1.5.16 Explainability** {#1.5.16-explainability}

The other four measures of model comparison are rather similar from application to application. The rankings presented apply to these models in general, not just for this case study. For explainability, the simpler models score higher. This is especially important when you need to justify your model, the inputs, and the model form to those who are not involved in your model development. Unfortunately, this often is inversely related to accuracy. This is often as important as accuracy, or nearly so.

High   
These are the simplest models and therefore the easiest to explain. 

* Null model  
* Linear regression (though some GLMs may be more difficult to explain)  
* Decision tree  
* Bayesian regression

Medium   
These are slightly more complicated. You can write out their form and show how to use them. 

* GAM  
* Mixed model  
* Stacked model

Low   
These are essentially black boxes, and difficult to explain. 

* Neural network  
* Random forest  
* Gradient boosting machine

Explainability

### **1.5.17 Stability** {#1.5.17-stability}

This is how consistent the results are from run to run and data set to data set. Again, the simplest models are the most consistent. These rankings are almost the same as the explainability rankings because simpler models tend to be both easy to explain and have low variance. An exception is Bayesian models, which under the current implementation can be unstable from time to time. For models with low stability, it becomes important to take steps to reduce overfitting and hence increase stability.

High 

* Null model  
* Linear regression (assuming extraneous variables have been removed or regularized and high leverage points removed)  
* Stacked model (independent of the stage-0 models)

Medium 

* GAM  
* Mixed model  
* Random forest  
* Bayesian regression  
* Gradient boosting machine

Low 

* Regression tree (even with pruning, they tend to be unstable)  
* Neural network

Stability

### **1.5.18 Analytical Effort** {#1.5.18-analytical-effort}

The ranking of analytical effort depends on who is working on the model. Essentially everyone knows how to take a mean (the null model) and almost everyone knows about linear regression. The rest of the models depend on your familiarity. The ranking below is based on how easy they are to implement, if you know about them. Things that make implementation challenging include understanding the array of choices to make (e.g., the number of hidden layers in a neural network) and how best to make those choices.

High 

* Null model  
* Linear regression (but higher effort if regularization is used)  
* Regression tree

Medium 

* GAM  
* Random forest  
* Stacked model (independent of the stage-0 models)  
* Mixed model

Low 

* Neural network  
* Bayesian regression  
* Gradient bosting machine

Analytical Effort

### **1.5.19 Computational Efficiency** {#1.5.19-computational-efficiency}

The importance of computational efficiency depends on your problem, data set, and computational resources. If your setup is poor, or your data and model are large and complicated, you may not be able to implement a particular model. Or, if your setup is really good and your data is simple, then the difference between the most and least efficient models will be small.

High 

* Null Model  
* Linear regression  
* Stacked model (independent of the stage-0 models)  
* Regression tree

Medium 

* GAM  
* Mixed model

Low 

* Neural network (very simple neural networks can be more efficient)  
* Random forest  
* Bayesian regression (though if Bayesian methods are used only to obtain the regression coefficient, the model can be highly efficient)  
* Gradient boosting machine

Computational Efficiency

### **1.5.20 Case Study Conclusions** {#1.5.20-case-study-conclusions}

In the bodyfat example, we are trying to develop a model that uses simple measurements to approximate bodyfat without the need for expensive equipment. In comparing various models, we want the model to be accurate enough to be credible, but we are not tied to taking the most accurate model at any cost. Many of the other dimensions, especially explainability, are more important in this situation than accuracy. 

Looking specifically at our results, the three most accurate models are the mixed, Bayesian, and linear regression models. They are all very similar in accuracy, but the linear regression model is the simplest and most explainable. Linear regression is also the best in terms of stability, analytical effort, and computational efficiency. 

We would use the linear regression model for making the app and for distributing the model directly to practitioners and the general public. The linear regression model may still be too technical for many and that is what the app is for. Others would like to see the model and may use it to make better apps to make it even easier for people to get an estimate of their bodyfat. 

One complication is the role of state. If we only plan to make predictions for those four states, the linear model can be used. If we plan to make predictions for other states, the options are to refit the linear model without the state variable (which may worsen its accuracy compared to alternatives) or use the mixed model (which allows for predictions when state is not one of the four analyzed).  
Case Study Conclusions

### **1.5.21 Module 4 Bibliography (copy)** {#1.5.21-module-4-bibliography-(copy)}

Module 4 Bibliography  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_m3\_bibliography.pdf\]  
A PDF copy of the bibliography is available as well ( [atpa\_m4\_bibliography.pdf](#bookmark=id.e978i7wnimkb)).  
\[END LINK\]

Component Table40

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  Actuarial Standards Board. (2010, December). *Actuarial Standard of Practice (ASOP) No. 41*. Retrieved from Actuarial Standards Board: http://www.actuarialstandardsboard.org/wp-content/uploads/2014/02/asop041\_120.pdf Allen, R. M. (2009, June 22). *Mistakes in writing*. SFWA. Retrieved April 12, 2022, from https://www.sfwa.org/2005/01/mistakes-in-writing/ Doshi-Velez, F., & Kim, B. (2017). *Towards a rigorous science of interpretable machine learning*. Retrieved from Cornell University: https://arxiv.org/abs/1702.08608 Fisher, A. G. and Johnson, R. W. (2021, June). *Body Fat Prediction Dataset*, Version 1\. Retrieved March 1, 2022 from [https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset](#bookmark=id.gqkm2ax7dqyd). James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An introduction to statistical learning* (Vol. 112, p. 18). New York: Springer. Leslie, D. (2019). *Understanding artificial intelligence ethics and safety: A guide for the responsible design and implementation of AI systems in the public sector*. Retrieved from The Alan Turing Institute: https://www.turing.ac.uk/sites/default/files/2019-06/understanding\_artificial\_intelligence\_ethics\_and\_safety.pdf Molnar, C. (2019). *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*. Retrieved January 2021, from https://christophm.github.io/interpretable-ml-book/ Roberts, C. (2020), Body mass index vs. body fat percentage: Only one of them actually matters, *CNET*, [https://www.cnet.com/health/whats-the-difference-between-bmi-and-body-composition/](#bookmark=id.9fgfvenkp4ti) Stonewall, A. J. (2004). *ASOP 41 – The Do’s and Don’t’s of Effective Actuarial Communication*, Society of Actuaries.  |
| Footer | Panel Footer |

