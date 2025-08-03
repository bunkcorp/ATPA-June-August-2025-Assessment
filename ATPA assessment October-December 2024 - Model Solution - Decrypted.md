ATPA Assessment – October to December 2024 Model Solution General Information for Candidates

This examination has 6 tasks numbered 1 through 6\.

Each task pertains to the business problem and related data files and data dictionary. There  is not an Rmd file that accompanies this exam. Unless otherwise specified, each task builds  upon the work and conclusions from prior tasks.

The responses to each specific task should be written in the provided Word template.  Where code, tables, or graphs from your own work are required, they should be copied and  pasted into the Word template. Instructions for pasting tables are included at the end of  this document.

You may use resources such as textbooks and the internet. You may use any analytics  software you wish to perform the analysis directed by the tasks. You may not consult with  other individuals about the specific business problem, data, and tasks.

Each task will be graded on the quality of your thought process (as documented in your  submission), conclusions, and quality of the presentation. Each response should be  confined to the prompt as set and written for the audience specified in the prompt. If no  audience is specified, assume a technical audience familiar with predictive modeling. In  tasks 1-5, various portions of a technical report are to be written but these are not intended  to make up an entire report, e.g., a statement of the business problem is not asked for in  these tasks. Only write the sections requested.

Your completed Word template should be the only file submitted and will be the only file  graded. If any part of your exam was answered in French, include “French” in the file name.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Business Problem

ABCMart, a nationwide grocery store chain, has used a loyalty program for several years to  enhance customer retention and increase sales. Despite a significant initial sign-up rate,  ABCMart has observed a worrying trend: a substantial number of loyalty program  members have churned, meaning they have become inactive, no longer recording  purchases from the store. Understanding customer behavior and predicting churn is critical  for ABCMart to develop targeted marketing strategies and improve customer satisfaction.

ABCMart's management has tasked your data analytics consulting firm with identifying key  factors that influence customer churn within their loyalty program. They are particularly  interested in understanding how various customer demographics, shopping behaviors,  loyalty tiers, and transaction patterns contribute to churn. Additionally, they seek insights  into how payment methods and the use of coupons or promotions impact customer  retention.

Your consulting firm is well-equipped to tackle this challenge by leveraging advanced data  analysis and predictive modeling techniques. By analyzing the provided datasets, you aim  to uncover actionable insights that will help ABCMart reduce churn rates, enhance  customer loyalty, and increase profitability.

ABCMart sent unprotected data files to your assistant in an unencrypted email. Noticing the  email addresses were directly in the file, your assistant quickly replaced these emails with  a specific encryption, so individuals could not be identified directly from the email. Your  assistant noted there were potentially some other sensitive features about the data.

The datasets provided include detailed customer profiles, transaction histories, and loyalty  program information. These datasets contain a mix of useful variables, including  continuous variables like annual income and categorical variables like preferred payment  methods. One of the main challenges is to account for potential non-linear relationships  between these variables and customer churn. For example, high-income customers might  have different shopping patterns compared to low-income customers, affecting their  likelihood to churn.

In the project brief, ABCMart's management has outlined several key questions they need  you to address:

• What customer characteristics are associated with higher or lower churn rates? • How do shopping behaviors and transaction patterns influence customer churn? • What role do loyalty tiers play in customer retention?

ABCMart expects both a technical report and an executive summary. While the  management team has some familiarity with data analytics concepts, they value clear,  actionable insights over technical jargon. The most crucial part of your communication will

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
be an executive summary with clear recommendations that ABCMart can use to implement  strategies to reduce customer churn.

**File List**

• Two CSV files:

o customer\_data.csv: Contains customer demographic information and loyalty  program details. Includes the churn variable that is used to determine if a  customer has discontinued shopping at the store.

o transaction\_data.csv: Contains transaction history with detailed purchase and  payment information.

• One Excel file called DataDictionary.xlsx: Contains the data dictionary for the above  files.

By delivering this project, you will help ABCMart make informed decisions to enhance  customer loyalty and reduce churn. Your detailed statistical analyses, visualizations, and  report will provide valuable insights that drive effective marketing strategies and  operational improvements.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 1

Perform the following data preparation tasks:

**a)** Clean and prepare the data for analysis:

• Create one combined dataset by appropriately joining the tables

from customer\_data.csv and transaction\_data.csv. Describe and justify the types of joins  used. Consider that some customers may not have transaction records, and some  transactions may not match existing customers due to data inconsistencies.

• The target variable is Churn in the customer\_data.csv file. Some customer records may  have missing values in critical fields such as AnnualIncome or Age. Briefly describe  approaches to handling records with missing values, recommend, and implement  one approach.

• Analyze the predictor variables provided. Based on your judgment before fitting any  models, remove variables with no predictive value or that may introduce bias.  Explain your choices.

• Check that the variables have values that make sense and are appropriate for  modeling.

• Ensure internal consistency between variables that should contain related  information (e.g., PreferredPaymentMethod in customer data vs.

actual PaymentMethod used in transactions).

**b)** Feature Engineering:

• Create the following new variables that may enhance the predictive power of your  models.

a) how frequently someone shops

b) amount of money they spend per visit

**c)** Exploratory Data Analysis:

• Explore the distribution of the target variable Churn.

• Visualize no more than two relationships between the target variable and other  predictors that you believe might be significant.

Write a brief section of the technical report explaining your data preparation work. Since  your code or the transformed data itself will not be available to the reader, all evidence of  the data preparation tasks must be contained in your report. This may include written  descriptions as well as charts. Be sure that evidence of dealing with all the steps above is  included, including the validation checks, where you should describe the checks performed  and report on the results.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Response to Task 1

We began by merging the two provided datasets,

**customer\_data.csv** and **transaction\_data.csv,** using a left join on the common  key **CustomerID**. This approach ensured that all customer records were retained even if  some customers did not have any corresponding transaction records.

To capture customer shopping behavior, we aggregated the transaction data to derive the  following features:

• **Shop Frequency:** Calculated as the number of transactions per customer. • **Average Spend per Visit:** Computed as the mean amount spent per transaction. • **Mode Payment Method:** Determined as the most frequently used payment method  for each customer, which was later used to assess internal consistency.

This resulted in 8966 records after the join.

Instead of discarding records with missing values in critical fields such as **AnnualIncome,  Gender** and **Age**, we used the **mice** package to impute these values. By applying the  predictive mean matching (pmm) method, we replaced 300 missing values  in **AnnualIncome**, 106 missing values in **Gender**, and 200 missing values in **Age**. This  approach preserved the overall sample size while ensuring that the imputed values were  statistically plausible, thereby maintaining the integrity of our dataset.

After merging, we removed sensitive variables (e.g., **Email**) and non-predictive identifiers  (e.g., **CustomerID**) to protect customer privacy and avoid introducing bias in subsequent  analyses. Additionally, we evaluated variables for redundancy; for instance, if the  original **TransactionCount** in the customer dataset duplicated our

engineered **shop\_frequency** metric, we retained the latter, which was derived directly  from the raw transaction data.

An internal consistency check was performed to compare the customer’s  stated **PreferredPaymentMethod** (from the customer data) with the aggregated mode of  the **PaymentMethod** (derived from transaction records). This comparison revealed that  8951 customer records had matching payment methods, while 15 records showed  discrepancies. These mismatches could indicate either genuine differences between  customer preferences and transactional behavior or data quality issues that merit further  investigation, but because the overall number of discrepancies is small, it shouldn’t be an  issue.

The final dataset was then subjected to exploratory analysis to understand key  distributions and relationships:

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
• **Figure 1** illustrates the distribution of the target variable **Churn**, showing 8,411 churned versus 555 active customers.

• **Figure 2** is a boxplot depicting the relationship

between **Churn** and **AnnualIncome**. This plot suggests that income levels might  influence churn behavior.

• **Figure 3** is a boxplot showing the relationship between **Churn** and **Shop  Frequency**, indicating that shopping frequency could be an important predictor of  churn.

![][image1]
*Figure 1: Churn distribution*

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**

*Figure 2: Income by churn*


*Figure 3: Transaction count by churn*

After the data preparation phase, we obtained a refined dataset comprising 8,966 customers with imputed values for critical variables, enriched transaction-based features,  and confirmed internal consistency in key areas. This comprehensive process—

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
encompassing data merging, imputation, and rigorous validation—ensures that the dataset  is robust and ready for the subsequent predictive modeling phase.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 2

ABCMart has allowed you access to their data. However, they have not taken any measures  to account for any security or privacy of the data. They simply sent unprotected data over  in an unencrypted email. Based on this information and from inspecting the data, answer  the following two questions:

a) In the context of the Actuarial Standards of Practice, what would your  responsibility be now concerning this data? Point to specific language in the  ASOPs to support this.

b) What standards of practice would ABCMart have violated if they adhered to  actuarial standards of practice? Point to specific language in the ASOPs to  support this.

Response to Task 2

a) In accordance with the Actuarial Standards of Practice, any data used for analysis should  be both reliable and securely handled. Specifically, ASOP No. 23 (Data Quality) requires  that an actuary evaluates the quality and reliability of the data and acknowledges any  limitations that may arise from issues such as data security. For example, the standard  states that an actuary should "obtain sufficient, relevant, and reliable data" and, when  limitations exist, "disclose the nature of these limitations." Similarly, ASOP No. 41  (Actuarial Communications) emphasizes the need to safeguard confidential information  and to communicate any risks that may affect the analysis.

b) If ABCMart were required to adhere to actuarial standards of practice, their handling of  customer data—as demonstrated by sending unprotected, unencrypted data via email— would likely constitute a violation of key standards designed to protect data security and  confidentiality. Under ASOP No. 23 (Data Quality), actuaries are expected to use data that is  not only accurate and complete but also transmitted and stored securely to prevent  unauthorized access. The requirement to "obtain data of sufficient quality" inherently  includes ensuring that data is handled in a manner that protects its integrity and  confidentiality.

Furthermore, ASOP No. 41 (Actuarial Communications) mandates that confidential client  information is managed with appropriate care and safeguards, which extends to the  processes by which data is transmitted to and received from clients. By failing to encrypt  sensitive customer data and allowing it to be sent over an unprotected channel, ABCMart  would be in breach of these principles, thereby failing to meet the expectations for secure  data handling as outlined in the ASOPs.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 3

Perform the following modeling tasks:

a) Using the data prepared in Task 1, create datasets for model training and testing.  Perform reasonability checks to assess if the data split is appropriate. b) Fit a logistic regression model for the target Churn. Outline and justify your variable  selection approach and final variables included.
c) Fit a random intercept model for the target Churn using Region as a random effect.  You may use input variables as selected from the linear model. Explain why region  may be a good choice for the random variable in this data set. Explain why other  categorical variables would not have been good choices.

d) Choose 2 performance measures for this model’s predictions and apply on both the  training and test datasets. Evaluate these measures for goodness of fit and over  fitting.

Write a section of the technical report that covers all the work above. Identify and discuss  the most important predictor variables for the logistic regression model and the mixed  model. In the report, discuss the choice of random and fixed predictors. State what  advantages the mixed model may have. Report on the goodness of fit of the models.

Response to Task 3

The final dataset was randomly split into training (70%) and testing (30%) sets using a  reproducible random seed. Reasonability checks confirmed that the distribution of the  target variable, **Churn**, was consistent across both sets. In the training set, there were  6,276 records with 5,882 churned and 394 (6.7%) not churned, while the testing set  contained 2,690 records with 2,529 churned and 161 (6.4%) not churned. Summary  statistics for key predictors, such as **AnnualIncome**, were also similar across both datasets,  supporting the appropriateness of the split.

The prepared dataset originally contained the following variables:

Age : Customer age

Gender : Customer gender

MaritalStatus : Marital status (e.g., Married, Single, Widowed)

Occupation : Customer occupation

Region : Geographic region

FamilySize : Number of family members

LoyaltyTier : Tier level of the loyalty program

PreferredPaymentMethod : Customer’s preferred payment method

AnnualIncome : Annual income

SignupDate : Date the customer signed up

TransactionCount : Count of transactions (from customer data)

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
DaysSinceLastTransaction : Days since the last transaction

CustomerTenure : Duration of the customer relationship

Churn : Target variable (0 \= Active, 1 \= Churned)

shop\_frequency : Derived: Number of transactions (from transaction data) avg\_spend\_per\_visit : Derived: Average spending per visit (from transaction data) mode\_payment : Derived: Most frequently used payment method (from transaction data)

A full logistic regression model was initially fit using all available predictors. A stepwise  variable selection procedure based on the Akaike Information Criterion (AIC) was then  applied. The final selected model included the following predictors:

• MaritalStatus

• AnnualIncome

• DaysSinceLastTransaction

The final logistic regression model is summarized in Table 1 below.

*Table 1\. Final Logistic Regression Model Coefficients*

**Predictor Estimate Std. Error z-value p-value Significance (Intercept)** \-2.936e+00 2.423e-01 \-12.118 \< 2e-16 \*\*\* **MaritalStatusMarried** 2.091e-01 2.172e-01 0.963 0.3356

**MaritalStatusSingle** \-1.775e-02 2.237e-01 \-0.079 0.9368

**MaritalStatusWidowed** 7.557e-01 3.854e-01 1.961 0.0499 \*

**AnnualIncome** \-2.122e-05 2.614e-06 \-8.118 4.75e-16 \*\*\* **DaysSinceLastTransaction** 5.287e-03 2.732e-04 19.352 \< 2e-16 \*\*\*

*Significance codes: \*\*\* p \< 0.001, \*\* p \< 0.01, \* p \< 0.05*

Given the imbalanced nature of the data—with a relatively low prevalence of churned  customers (\~6% in the training set)—it was important to evaluate model performance  beyond overall accuracy. We assessed model performance using the confusion matrix  (which reports sensitivity, specificity, and balanced accuracy) and the Area Under the ROC  Curve (AUC).

**Performance Metrics (Training Data):**

• **Accuracy:** 94.17% (95% CI: \[X, Y\])

• **Sensitivity (Recall):** 8.90%

• **Specificity:** 99.69%

• **Balanced Accuracy:** 54.30%

• **AUC:** 0.7829

**Performance Metrics (Testing Data):**

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
• **Accuracy:** 93.98% (95% CI: \[X, Y\])

• **Sensitivity (Recall):** 10.98%

• **Specificity:** 99.68%

• **Balanced Accuracy:** 55.33%

• **AUC:** 0.7528

The high overall accuracy primarily reflects the model’s ability to correctly classify the  majority class (active customers). However, the low sensitivity indicates that the model  struggles to correctly identify churned customers, a common challenge when dealing with  imbalanced datasets.

A mixed effects model was also fitted using the same fixed predictors as the final logistic  regression model and incorporating Region as a random intercept. The performance of the  mixed effects model was nearly identical to that of the logistic regression model:

• **Training Set AUC:** 0.7829

• **Testing Set AUC:** 0.7525

The inclusion of Region as a random effect captures unobserved regional heterogeneity and  may improve generalizability, even if the overall classification metrics remain similar.

In mixed effects modeling, a random effect is used to capture unobserved heterogeneity  that exists within groups or clusters. The chosen grouping variable should naturally  represent clusters where observations within the same group are more similar to one  another than to observations in different groups.

Other categorical variables are less suitable as random effects for several reasons:

• **Gender:** With only two levels, gender does not form meaningful clusters and is best  modeled as a fixed effect for direct inference.

• **MaritalStatus:** Although it has multiple categories, it does not create natural  clusters with shared environments, making fixed effects more appropriate. • **Occupation:** The variability within occupation categories is often too  heterogeneous or sparse to define clear clusters.

• **LoyaltyTier and PreferredPaymentMethod:** These reflect individual customer  preferences rather than hierarchical groupings, so they are better treated as fixed  effects.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 4

Using the same training and test data from Task 3, perform the following modeling tasks:

a) Fit a Neural Networks model to the data.

b) Outline 5 hyper-parameters that can be used for tuning and fitting a neural network model.

c) Apply model tuning to at least 3 hyper-parameters of the neural network model to  improve model fit. Try to choose hyperparameters that will make the model fit  better. Justify your choices.

d) Use the same metric as Task 3 and evaluate the neural network model. Check for  goodness of fit and for overfitting.

Write a section of the technical report that covers all the modeling work above for the  Neural Network model. Include a discussion of the model tuning approach used and justify  your choice of final hyper-parameter values. In the report, discuss how this model  performs against the model in Task 3\.

Response to Task 4

**a)** Using the same training and testing datasets as in Task 3, we fit a neural network model  to predict customer churn. We utilized the nnet package via the caret framework, which  allowed us to perform automated hyperparameter tuning using 5‐fold cross-validation. In  this model, we used all available predictors in the prepared dataset.

This initial model provided an AUC of 0.743 and 0.713 on the training and test data  respectively.

**b)** Five key hyper-parameters that can be tuned for a neural network model include:

• **Size:** The number of neurons in the hidden layer. Increasing this value may capture  more complex relationships.

• **Decay:** The weight decay (regularization) parameter, which helps prevent  overfitting by penalizing large weights.

• **Maxit:** The maximum number of iterations (epochs) allowed for training, ensuring  sufficient convergence.

• **Learning Rate:** Although indirectly controlled in our implementation, the learning  rate determines the step size during weight updates.

• **Activation Function:** In our implementation (using nnet), the logistic activation  function is used by default; however, in other frameworks, this can be tuned for  non-linear transformation.

**c)** We applied model tuning on at least three hyper-parameters: **size, decay, and maxit**. A  grid search was performed over the following values:

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
• **Size:** {3, 5, 7}

• **Decay:** {0.001, 0.01, 0.1}

• **Maxit:** {100, 200, 300}

Our tuning strategy was aimed at finding a balance between model complexity and  regularization. A larger hidden layer (size) might capture more nuances in the data but  could also lead to overfitting, while a higher decay value provides stronger regularization.  Increasing maxit can help the model converge, but excessive iterations may result in  overfitting. The final best hyperparameters obtained were:

• **Maxit:** 100

• **Size:** 3

• **Decay:** 0.1

These values were chosen because they yielded the highest F1 score during cross validation, indicating the best balance between precision and recall, especially in this  imbalanced dataset.

**d) Model Evaluation and Comparison**

The neural network model was evaluated using the same metrics as Task 3, including  accuracy, sensitivity, specificity, balanced accuracy, and AUC. In addition, we adopted the  F1 score as a primary metric to address the class imbalance. The performance metrics are  summarized below:

**Training Set Performance:**

• **Confusion Matrix:**

o Prediction “No”: 5820 correctly classified as non-churn; 352 misclassified  (actual churn)

o Prediction “Yes”: 10 misclassified (actual non-churn); 26 correctly classified  as churn

• **Accuracy:** 94.17%

• **Sensitivity (Recall):** 6.88%

• **Specificity:** 99.83%

• **Balanced Accuracy:** 53.35%

• **AUC:** 0.787

**Testing Set Performance:**

• **Confusion Matrix:**

o Prediction “No”: 2474 correctly classified as non-churn; 158 misclassified  (actual churn)

o Prediction “Yes”: 7 misclassified (actual non-churn); 13 correctly classified as  churn

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
• **Accuracy:** 93.78%

• **Sensitivity (Recall):** 7.60%

• **Specificity:** 99.72%

• **Balanced Accuracy:** 53.66%

• **AUC:** 0.742

While the neural network model achieves high overall accuracy on both training and  testing sets, the low sensitivity values indicate that it still struggles to correctly identify the  minority churn class—a common challenge given the 6% churn prevalence. The AUC values  of approximately 0.787 (training) and 0.742 (testing) suggest moderate discrimination  ability.

When compared to the logistic regression and mixed effects models from Task 3, the neural  network’s performance in terms of AUC is similar, though its sensitivity remains low. The  neural network offers the advantage of capturing non-linear relationships, but the  challenge of class imbalance persists across all modeling approaches. Future work may  incorporate advanced resampling techniques or cost-sensitive learning to further improve  the detection of churners.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 5

Examine variables that may be important for churn using shapley values.

a) Fit a random forest model to the data. Tune the model by finding a good complexity  parameter and/or tree depth. Check for over fitting by evaluating accuracy on the  training and test set.

b) Choose 5 individuals who have churned and 5 individuals who have not. Find the  shapley values for these observations. Interpret the shapley values in the context of this

problem.

Write a section of the technical report discussing your modeling work and addressing these  requests.

Response to Task 5

**a) Random Forest Model Fitting and Tuning**

To fit a random forest model, we tune the key hyper-parameters to achieve better model  performance and predictive power. To tune the hyper-parameter of the model, a grid  search with 5-fold cross-validation is used on a range of hyper-parameter to pick the  combination of hyper-parameter that gives the optimal mean ROC-AUC.

The hyper-parameter and the range of values described as follows.

• n\_estimators: The number of decision trees in the forest. Increasing this would  improves the performance of model but also longer computation time.  Values to test \[50, 100\]

• max\_depth: This is the maximum depth of each decision tree in the forest. A higher  value of max\_depth could lead to overfitting, thus we picked 5 and 10 for the testing  to take into the consideration of low training data (13,478)

Values to test \[3,5\]

• min\_samples\_split: This is the minimum number of samples a node must contain in  order to consider splitting.

Values to test \[2,5,10\]

• min\_samples\_leaf: This is the minimum number of samples that needed to be  considered a leaf node. This parameter used to limit the growth of the tree.  Values to test \[1,2,4\]

Table below outlines the top 10 combinations with their mean ROC-AUC respectively.

| n\_estimators | max\_depth | min\_samples \_split | min\_samples\_ leaf | mean\_train\_score | mean\_test\_score |
| :-----------: | :--------: | -------------------- | ------------------- | :----------------: | :---------------: |
|      50      |     5     | 2                    | 1                   |       0.8286       |      0.8175      |
|      50      |     5     | 5                    | 1                   |       0.8284       |      0.8172      |
|      50      |     5     | 2                    | 2                   |       0.8283       |      0.8172      |

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**

| 100 | 5 | 2 | 1 | 0.8289 | 0.8172 |
| :-: | :-: | :-: | :-: | :----: | :----: |
| 100 | 5 | 2 | 2 | 0.8287 | 0.8172 |
| 100 | 5 | 5 | 2 | 0.8287 | 0.8172 |
| 100 | 5 | 5 | 1 | 0.8288 | 0.8172 |
| 50 | 5 | 5 | 2 | 0.8283 | 0.8171 |
| 100 | 5 | 10 | 1 | 0.8287 | 0.8170 |
| 100 | 5 | 10 | 2 | 0.8286 | 0.8170 |

Table 1: ROC-AUC score for top 10 combinations

By adopting the best combination derived

(n\_estimator=50,max\_depth=5,min\_samples\_split=2 and min\_samples\_leaf=1) into the  random forest model.

The accuracy for training and testing data set as below.

| Performance Metrics | Training Dataset | Testing Dataset |
| :------------------ | :--------------: | :-------------: |
| Accuracy            |       0.77       |      0.75      |
| ROC-AUC             |       0.81       |      0.79      |

We have also performed reasonable check on the model to ensure it is non-overfitting such  as comparing the training and testing performance such that the variance between both  performance is acceptable (e.g. ≤2-5%). This is also applicable when we working on the  grid searching with k-fold cross validation method.

**b) SHAP Analysis of Key Drivers Influencing Customer Churn**

Here we analyze the variables contributing the most to customer churn by using Shapley  values. Shapley values are a tool for explaining how much each feature or predictor  contributes to a model’s predictions. The baseline Shapley value is the average target  variable, which in this case is the proportion of customers in the test data that have  churned. This is a reasonable baseline prediction as we would expect the null model to  predict this value.

As features get added to the model, the predicted probability of churn deviates from the  baseline. Shapley values capture this deviation. These values can be interpreted in two  manners:

• Direction: Positive shapley values increase the probability of churning, and the  opposite can be said for negative shapley values

• Magnitude: The larger the shapley value, the more that predictor influences the  predicted probability

There are 5 churned customers and 5 active customers that have been randomly selected  from the dataset. The results have been combined on the diagram below.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
**![][image4]**Figure 1: SHAP value of 10 sample customers

(5 churned customers & 5 active customers)

Each Shapley value quantifies the contribution of a specific feature to the prediction for an  individual customer.

The overall Shapley analysis revealed that the main contributor for the customer churn is  DaysSinceLastTransaction, followed by level of annual income. This analysis also highlights the high-risk group that ABCMart must prioritize intervention, ABC Mart should focus on  inactive customer by taking business action such as conducting in-depth survey or research  on customer satisfaction which will help to understand their behaviors, preferences, and  purchasing habits. Furthermore, ABCMart will be able to make informed decisions and  tailor the products that effectively address their specific needs.

Besides, customer in lower income group normally tend to be more sensitive to the price  and concerning on whether they provide good bang for their buck. Perhaps more tailored  discount or installment payment options can be taken to support low-income customers.  This will help to improve the customer retention while balance the class of high and low

income group. The balance of high and low-income group is important since will indirectly  affect the product variety on the shelf.

It is minimal impact observed from AvgAmountSpent as compared to key contributors  discussed above. The average amount spent per visit may not provide the necessary  information of churn rate in this analysis. For instances, the churned customer may have a  large one-off spending, and the active customer would have consistent low spending  behavior.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Task 6

Write a one-to-two-page executive summary to ABCMart's management team that  summarizes the information they need to make well-informed decisions on strategies to  reduce customer churn. This will incorporate some of the work and findings from prior  tasks and will also include additional sections such as:

• **Statement of the Business Problem**: A clear and concise description of the  challenge ABCMart is facing.

• **Key Findings**: Highlight the most significant factors influencing customer churn. • **Recommendations**: Provide actionable suggestions on how ABCMart can reduce  churn based on your analysis.

• **Limitations**: Briefly mention any limitations of your analysis that the management  should be aware of.

Ensure that the executive summary is written in clear, non-technical language suitable for  an audience without a data science background.

Response to Task 6

**Statement of the Business Problem**

The goal of this analysis is to provide ABCMart with a better understanding of why some  members of their customer loyalty program have stopped participating, a process referred  to as “churn.” I have been provided with datasets of 8,966 customers and 110,494  transactions to complete my analysis. ABCMart encouraged me to look for nonlinear  patterns in the data.

**Modeling Overview**

The data provided was adjusted, based on our judgement, to improve its viability for  statistical modeling purposes. A series of predictive models were applied to the data. The  following models were independently fit to the data and used to identify impacts that were  most associated with churn rate:

• **Generalized linear model (GLM):** a very common model type which is very strong at  capturing linear relationships between input variables and churn rates.  • **Generalized linear mixed model:** similar to a GLM, which can more readily  accommodate changing contributors, such as new regions

• **Neural Network model:** a sophisticated deep learning model, was used to consider  complex relationships between churn and the input variables

• **Random Forest**: a moderate complexity model that can capture a wide range of  relationship between churn and the input variables.

**Key Findings**

In my analysis, I trained and fit four different types of models: a logistic regression model, a  random intercepts model, a neural network, and a random forest. All the models were  trained on 70% of the data and then tested on the remaining 30% of the data. The more

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
complicated models, the neural network and the random forest, saw at least a hundred  models fit in order to find the most effective model structure.

The logistic regression model and random forest model both showed that the single most  important predictor of churn was DaysSinceLastTransaction, with customers who have  gone longer since their last purchase at ABCMart more likely to churn.

Both of those models also showed that the second most important predictor was  AnnualIncome, where customers with a higher annual income are less likely to churn.

None of the models found LoyaltyTier to be very significant, which was expected based on  my preliminary data analysis. A barplot of churn percentage by loyalty tier found a  decrease in churn rate as loyalty tier increased, but not a very large one.

![][image5]
**Recommendations**

ABCMart asked me outline results in three categories: customer characteristics, shopping  behaviors, and loyalty tiers.

Customer Characteristics:

The most significant customer characteristics are AnnualIncome and FamilySize.  Customers with a higher annual income tend to churn less often, and customers with a  larger family also tend to churn less often.

Shopping Behaviors:

The most significant shopping behaviors are DaysSinceLastTransaction, CouponsUsed, and  AvgSpend. Higher churn is associated with longer time since last purchase, higher coupon  usage, and higher average spending per visit.

**Disclosing, publishing or posting the contents of this model solution is expressly prohibited by the  Terms and Conditions Agreement for Online Candidates.**
Loyalty Tiers:

While churn rate does decrease as loyalty tier increases, this decrease is not very  significant.

My recommendation to ABCMart is to modify the details of their loyalty program to appeal  more to lower-income individuals and individuals with small families. More generally, the  loyalty program could be adjusted to encourage customers to shop more frequently, even if  for smaller purchases per trip. The data suggests that more frequent customers that may  spend less per visit are also more loyal, continuing program participants. The churn  behavior difference across loyalty tiers is negligible, so I do not make any  recommendations regarding the loyalty tier structure.

**Limitations**

While the models were thoroughly trained, monitored, and analyzed, no model is perfect  and no model can accurately represent real-world behavior. While all the models fit had  high accuracy, all of them had poor sensitivity scores, meaning that many customers who

churned were incorrectly classified as having not churned. While this model has limitations  for accurately predicting if a given individual will churn, it is useful for investigating which  variables are associated with individuals that have churned.

I would be happy to answer any questions you may have about this analysis.
