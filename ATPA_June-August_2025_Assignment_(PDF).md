ATPA Assessment – June to August 2025  

General Information for Candidates 

This examination has six tasks numbered 1 through 6\. Each task pertains to the business problem,  related data files and data dictionary. There is no Rmd file accompanying this assessment. Unless  otherwise specified, each task builds upon the work and conclusions from prior tasks. Each task  will be graded on a stand-alone basis. When a response refers to work from a prior task, response  to the current task should be complete on its own, providing all facts, observations or conclusions to support your conclusions. 

The responses to each specific task should be written in the provided Word template. Where code,  tables, or graphs from your own work are required, they should be copied and pasted into the Word  template. Instructions for pasting tables are included at the end of this document. 

You may use resources such as textbooks and the internet. You may use any analytics software you  wish to perform the analysis directed by the tasks. You may not consult with other individuals  about the specific business problem, data, and tasks.  

Each task will be graded on the quality of your thought process, conclusions, and how well you  present your findings as documented in your submission. Responses should be confined to the  prompt as set and written for the audience specified in the prompt. In tasks 1-4, various portions of  a technical working file are to be written but these are not intended to make up an entire report,  e.g., a statement of the business problem is not required for these tasks. Only write the report sections requested. When asked to write sections of a working file, assume the audience is familiar with predictive modeling and will be reading your documentation as a manager reviewing your work. The level of detail should be brief but complete enough for the reader to understand your thinking process and ideally agree with your conclusions based on the evidence you provide. When you are asked to decide or recommend, responses must include reasoning which justifies your decisions and recommendations. 

Effective communication is a skill tested in this assessment. The grading process rewards responses that are concise, clearly address each task requested, and provide appropriate evidence of the work performed, including appropriate technical results that support your conclusions (e.g.  output from model fitting, quoting the number of data records with specific characteristics, etc.).  No credit is given for discussion not directly related to the task presented or information provided  that is not in support of your findings. No credit is given for statements that a step was performed when no supporting evidence is given demonstrating the work was performed.  

Your completed Word template should be the only file submitted and will be the only file graded. If  any part of your assessment was answered in French, include “French” in the file name.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 1 of 8   
Business Problem 

NMInsights, a non-profit public policy research institute in New Mexico, is interested in studying  their state’s crime rates. New Mexico consistently ranks among the U.S. states with the highest  rates of violent crime and property crime. NMInsights informs the public, elected officials, and local  law enforcement with high-quality fact-based research. New Mexico has a diverse population; and  NMInsights is concerned that data-driven policy research may introduce bias into the political  discourse. Using publicly available information, NMInsights will identify potential drivers of crime  and arrest rates.  

NMInsights has tasked your data analytics consulting firm with identifying key characteristics of criminal incidents that lead to arrests being made. They are particularly interested in  understanding demographic and other characteristics of criminal activity that lead law  enforcement agencies to make an arrest.  

Your consulting firm is well-equipped to tackle this challenge by leveraging advanced data analysis  and predictive modeling techniques. By analyzing the provided datasets, you aim to uncover  actionable insights that will enable NMInsights to advise policymakers who aim to reduce the  overall rate of criminal activity in New Mexico.  

The datasets provided by NMInsights were sampled from the Federal Bureau of Investigation’s Crime Data Explorer, which includes detailed demographic and other information about criminal  incidents that occurred in the state of New Mexico during 2023\. The “incidents” dataset contains a  mix of useful variables, including the type and location of the criminal offense, demographic  information about the victim and the alleged offender, whether a weapon was used in the criminal  offense, and the law enforcement agency that investigated the criminal offense. The “arrestee”  dataset contains information about the crime that an individual was charged with, the arrested  individuals’ demographic information, and information about any weapons used. One of the main  challenges is to identify potential relationships between these variables and whether an arrest was  made.  

In the project brief, NMInsights has outlined two key questions they want you to address: 1\. What characteristics of a criminal incident are associated with an arrest? 

2\. Are there any specific categories of criminal offenses (robbery, motor vehicle theft, etc.) which are more likely to result in arrests than other types? 

You are expected to create both an executive summary to be provided to non-technical client  executives and sections of a working file which supports your work. Unless otherwise specified, the  audience of the working file is your manager or a peer reviewer with expertise in predictive  modeling.  

The most crucial part of your communication will be an executive summary with clear findings and  recommendations that NMInsights can communicate to policymakers. This must speak to the  business problem and to a non-technical audience. 

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 2 of 8   
**File List** 

• One CSV file called incidents.csv contains demographic and other information about  criminal incidents. 

• Another CSV file called arrestee.csv contains information about the crime that an arrested individual was charged with, and demographic information about the alleged criminal. • One Excel file called DataDictionary.xlsx: contains the data dictionary for the above files. 

By delivering this project, you will help NMInsights advise various stakeholders about various  aspects of crime and policing in New Mexico. Your detailed statistical analyses, visualizations, and  report will provide valuable insights that drive potential changes to public policy in law  enforcement. 

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 3 of 8   
Task 1 

Perform the following data preparation tasks: 

a) Clean and prepare the data for analysis:   
• Identify predictors with missing values in each data source. Recommend and apply one approach to handling missing values. Justify your decisions. 

• Identify predictors where dimension reduction may be appropriate. Recommend and  apply dimension reduction you believe is appropriate. Justify your decisions.  • Evaluate numeric predictors which may best be represented as a factor variable.  Convert as appropriate. Justify your decisions. 

• Write a brief section for your working file that documents the work above. b) Merge the files into one data file where there is one record for each incident of criminal  activity. Specifically address the following issues: 

• There is not a perfect matching of incident activities, meaning that not every incident  identification code exists in both files.  

• Discuss various approaches to joining the two files and justify the approach you used. • Justify your approach to handling any variables that are included in both files. c) Prepare the dataset in terms of using the following target variable: 

• ARREST: a binary target variable that indicates whether an incident of criminal activity  resulted in an arrest or did not result in an arrest. 

d) Exploratory Data Analysis:   
• Analyze the distribution of the target variable ARREST.   
• Create two visualizations illustrating informative relationships between the target  variable and predictors. Interpret the visualizations. 

• Perform reasonability checks on predictor variables. Determine if outliers exist. Check  for internal consistency of values.  

• Write a brief section for your working file that documents the work above. 

Task 2 

As a trusted and impartial research organization, NMInsights is sensitive to using data such as race,  nationality, citizenship status, and gender with respect to public policy in criminal justice. 

a) Using non-technical language, discuss the benefits and the risks of using these types of  demographic data for victims of crime and alleged offenders in a predictive modeling  assignment related to public policy. 

b) NMInsights has specifically asked you to include demographic data in this study. Considering  applicable guidance in the syllabus relating to professional standards of practice, discuss what  steps you might take to ensure that the results of this study are not misused.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 4 of 8   
Task 3 

Perform the following modeling tasks to predict the target variable ARREST: 

a) Using the data prepared in Task 1, create datasets for model training and testing. Perform  reasonability checks to assess if the data splits are appropriate.  

o Write a brief section for your working file that documents the work above. b) Choose two (2) performance measures to evaluate model performance for this task. Justify  your choices based on strengths and weaknesses of the performance metrics. o Write a brief section for your working file that documents the work above.  c) Fit a Generalized Linear Model to the target variable ARREST.  

o Outline and justify your variable selection approach and final variables included,  including any model tuning if appropriate. 

o Evaluate the model based on performance metrics chosen in Task 3(b) as applied to  the training and testing datasets, identify significant predictors, and briefly state  how they contribute to your predictions. 

o Write a brief section for your working file that documents the work above. d) Fit a Linear Mixed Model to the target variable ARREST using at least two (2) random  effects. You may use input variables as selected from the generalized linear model.  o Explain why you chose the random effects. 

o Tune the model as appropriate. Choose a final model by selecting significant  predictors.  

o Evaluate the model based on performance metrics chosen in Task 3(b) as applied to  the training and testing datasets and identify significant predictors. 

o Write a brief section for your working file that documents the work above. e) Recommend the best model from c) and d) for later use in Task 4\. Justify your  recommendation.  

o Write a brief section for your working file that documents the work above. 

Task 4 

Using the same training, validation and test data from Task 3, perform the following modeling  tasks: 

a) Fit a Random Forest model to the target variable ARREST.  

o Tune your model as appropriate, and justify your selection of hyperparameters. o Evaluate the model based on performance metrics chosen in Task 3(b) as applied to  the training and testing datasets and identify significant predictors. 

o Write a brief section for your working file that documents the work above. b) Choose three (3) criminal incidents that resulted in an arrest, and three (3) criminal  incidents that did not result in an arrest.  

o Calculate the Shapley values for these observations based on the random forest  model.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 5 of 8   
o Create a visualization of the Shapley values for each of the selected records and  interpret these values in the context of the business problem. 

o Write a brief section for your working file that documents the work above. c) Use partial dependence plots to determine the effect of the most significant predictors identified using the Shapley values. Interpret the plots both in terms of the magnitude and  direction of the predictor’s effect on ARREST.  

o Write a brief section for your working file that documents the work above. 

Task 5 

The second business problem is to explore the rates of arrests for various categories of criminal  activity (include variable name). 

a) Create a summary of the data that includes the categories of criminal offenses, the number  of incidents and the number of arrests in each category. 

b) Explore modeled ranges of arrest rates for each category of criminal offense using a  Bayesian model. For each type of criminal offense, assume a binomial likelihood where *Ni* is the number of criminal offenses, and *yi* is the number of arrests in each category (*i*). The  unknown parameter *pi* would be the true but unknown arrest rate. Assume a Beta(���� \= 2,  ���� \= 8) prior distribution for *pi* and compute, using conjugate methods, the posterior  distribution of *pi*, given your data. Based on these results, compute a 95% credible interval  for the true arrest rate in each category of criminal offense given the data. Note: you should  build one model for each crime rate, not a single nested model for all crime rates  simultaneously. Display your results in either tabular format or with a visualization that includes the lower and upper bounds of the 95% credible interval for the arrest rates for  each category of criminal offense. 

c) Write a brief section for your working file in which you document and interpret the above  work. 

Task 6 

Write a one-to-two-page executive summary to the NMInsights management team that summarizes  the information they need to inform policymakers and the public about the incidence of crime and  arrests by law enforcement. This summary will incorporate some of the work and findings from  prior tasks and will include sections such as: 

• **Statement of the Business Problem**: A clear and concise description of the challenge  NMInsights is facing. 

• **Key Findings**: Summarize the work performed, highlighting the most significant  characteristics of criminal activity and offenders or victims that either leads to arrest or  does not lead to arrest. 

• **Recommendations**: Provide actionable suggestions on how NMInsights can inform  policymakers and the public based on your analysis.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 6 of 8   
• **Limitations**: Briefly mention any limitations of your analysis that NMInsights should be  aware of. 

Ensure that the executive summary is written in clear, non-technical language suitable for an  audience without a data science background. 

Important Notes about Inserting Tables 

If you need to insert an Excel table into your document, then you must follow the instructions  below to copy and paste the table from Excel into your Word document. 

**Do:** 

• Ensure your table fits in the page margins by: 

o Selecting the table 

o Right-clicking on the table to view the pop-up menu 

o Hover your mouse over “Auto Fit” 

o Click “AutoFit to Window”. 

**Do not:** 

• Paste as Picture 

• Insert Object 

• Use Word’s “Insert, Table, Excel Spreadsheet” function, since this will not paste your table in  the correct format.  

Pasting a **table** as a picture or as an object will result in an automatic disqualification of your  submission. **Graphs** pasted as pictures are **not** affected by this requirement.  

**Steps for pasting tables (for Windows versions of Word/Excel):** 

1\. Copy the cells from your Excel spreadsheet. If you use the Copy command on the Home tab,  do **not** select the option to “copy as picture”. 

2\. In your Word document, turn on the “Show/Hide Paragraph Marks” feature. 3\. In your Word document, right-click where you want to insert your table. 4\. In the menu that pops up, under Paste Options, select any of the first four options: a. “Keep Source Formatting” 

b. “Use Destination Styles” 

c. “Link & Keep Source Formatting” 

d. “Link & Use Destination Styles” 

5\. If you have “Show/Hide Paragraph Marks” turned on, you should see small circles at the end  of each cell in your table. This is how you can know whether or not you have pasted your  table correctly.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 7 of 8   
**Steps for pasting tables (for Mac versions of Word/Excel):** 

1\. Copy the cells from your Excel spreadsheet. If you use the Copy command on the Home tab,  do **not** select the option to “copy as picture”. 

2\. In your Word document, turn on the “Show All Nonprinting Characters” feature. 3\. In your Word document, right-click where you want to insert your table. 4\. In the menu that pops up, click Paste (**not** Paste Special). 

5\. If you have “Show All Nonprinting Characters” turned on, you should see small circles at the  end of each cell in your table. This is how you can know whether or not you have pasted  your table correctly. 

As You Complete Your Tasks…  

Your name should not appear anywhere in your submission, or in the filename, or in any way  identify you as the author. If you believe you should refer to yourself in the context of an answer,  use “ATPA Candidate” instead of your actual name.

**THIS MATERIAL IS STRICTLY CONFIDENTIAL. DO NOT DISTRIBUTE TO ANY OTHER PERSON.** Copyright © 2025 Society of Actuaries | ATPA\_NMInsights\_20250602 Page 8 of 8 