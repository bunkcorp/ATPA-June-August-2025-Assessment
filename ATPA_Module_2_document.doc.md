

# **ATPA Module 2**

**ATPA Module 2**

**Contents**

ATPA Module 2	[1](#heading)  
1 Working with Data	[8](#1-working-with-data)  
1.1 Data Pipeline	[8](#1.1-data-pipeline)  
1.1.1 Module 2 Learning Objectives	[8](#1.1.1-module-2-learning-objectives)  
1.1.2 Section 2.1 Learning Objectives	[10](#1.1.2-section-2.1-learning-objectives)  
1.1.3 Module Introduction	[11](#1.1.3-module-introduction)  
1.1.4 Section Introduction	[12](#1.1.4-section-introduction)  
1.1.5 Data Pipeline	[13](#1.1.5-data-pipeline)  
1.1.6 Data Pipeline	[14](#1.1.6-data-pipeline)  
1.1.7 Data Pipeline	[15](#1.1.7-data-pipeline)  
1.1.8 Data Warehouse Versus Data Lake	[16](#1.1.8-data-warehouse-versus-data-lake)  
1.1.9 Data for Predictive Analytics	[17](#1.1.9-data-for-predictive-analytics)  
1.1.10 Data for Predictive Analytics	[18](#1.1.10-data-for-predictive-analytics)  
1.1.11 Data for Predictive Analytics	[19](#1.1.11-data-for-predictive-analytics)  
1.1.12 Fairness in the Context of Data	[20](#1.1.12-fairness-in-the-context-of-data)  
1.1.13 Sources of Data Bias: Selection Bias	[21](#1.1.13-sources-of-data-bias:-selection-bias)  
1.1.14 Sources of Data Bias: Selection Bias	[22](#1.1.14-sources-of-data-bias:-selection-bias)  
1.1.15 Example: Selection Bias	[23](#1.1.15-example:-selection-bias)  
1.1.16 Under- and Overrepresentation	[24](#1.1.16-under--and-overrepresentation)  
1.1.17 Under- and Overrepresentation	[25](#1.1.17-under--and-overrepresentation)  
1.1.18 Other Issues with Non-Representative Data	[26](#1.1.18-other-issues-with-non-representative-data)  
1.1.19 Causes of Selection Bias	[27](#1.1.19-causes-of-selection-bias)  
1.1.20 Causes of Selection Bias	[28](#1.1.20-causes-of-selection-bias)  
1.1.21 Example: Selection Bias Can Lead to Unfair Outcomes	[29](#1.1.21-example:-selection-bias-can-lead-to-unfair-outcomes)  
1.1.22 Example: Selection Bias Can Lead to Unfair Outcomes  (copy)	[30](#1.1.22-example:-selection-bias-can-lead-to-unfair-outcomes-\(copy\))  
1.1.23 Measurement Bias	[31](#1.1.23-measurement-bias)  
1.1.24 Example: Measurement Bias	[32](#1.1.24-example:-measurement-bias)  
1.1.25 Causes of Measurement Bias	[33](#1.1.25-causes-of-measurement-bias)  
1.1.26 Measurement Bias can Lead to Unfair Outcomes	[34](#1.1.26-measurement-bias-can-lead-to-unfair-outcomes)  
1.1.27 Feature Selection and Omitted Variable Bias	[35](#1.1.27-feature-selection-and-omitted-variable-bias)  
1.1.28 The Feature Selection Process Can Lead to Unfair Outcomes	[36](#1.1.28-the-feature-selection-process-can-lead-to-unfair-outcomes)  
1.1.29 Omitted Variable Bias	[37](#1.1.29-omitted-variable-bias)  
1.1.30 Addressing Data Fairness	[38](#1.1.30-addressing-data-fairness)  
1.1.31 Addressing Data Fairness	[39](#1.1.31-addressing-data-fairness)  
1.1.32 Knowledge Check	[40](#1.1.32-knowledge-check)  
1.1.33 Knowledge Check	[41](#1.1.33-knowledge-check)  
1.1.34 Knowledge Check	[43](#1.1.34-knowledge-check)  
1.1.35 Knowledge Check	[45](#1.1.35-knowledge-check)  
1.1.36 Knowledge Check	[47](#1.1.36-knowledge-check)  
1.2 Reading and Writing Data	[49](#1.2-reading-and-writing-data)  
1.2.1 Section 2.2 Learning Objective	[49](#1.2.1-section-2.2-learning-objective)  
1.2.2 Section 2 Introduction	[50](#1.2.2-section-2-introduction)  
1.2.3 Software	[51](#1.2.3-software)  
1.2.4 Software	[52](#1.2.4-software)  
1.2.5 Tidy Data	[53](#1.2.5-tidy-data)  
1.2.6 Data Frames	[54](#1.2.6-data-frames)  
1.2.7 Data Frames	[56](#1.2.7-data-frames)  
1.2.8 Lists and Dictionaries	[58](#1.2.8-lists-and-dictionaries)  
1.2.9 Read Files	[59](#1.2.9-read-files)  
1.2.10 Read Files	[60](#1.2.10-read-files)  
1.2.11 Read Files	[61](#1.2.11-read-files)  
1.2.12 Read Files	[62](#1.2.12-read-files)  
1.2.13 Read Files	[63](#1.2.13-read-files)  
1.2.14 Read Files	[64](#1.2.14-read-files)  
1.2.15 Exercise 2.2.1	[65](#1.2.15-exercise-2.2.1)  
1.2.16 Structured Data Files	[66](#1.2.16-structured-data-files)  
1.2.17 Structured Data Files	[67](#1.2.17-structured-data-files)  
1.2.18 Structured Data Files	[68](#1.2.18-structured-data-files)  
1.2.19 Structured Data Files	[69](#1.2.19-structured-data-files)  
1.2.20 Structured Data Files	[71](#1.2.20-structured-data-files)  
1.2.21 Structured Data Files	[72](#1.2.21-structured-data-files)  
1.2.22 Structured Data Files	[73](#1.2.22-structured-data-files)  
1.2.23 Exercise 2.2.2	[74](#1.2.23-exercise-2.2.2)  
1.2.24 Structured Data Files	[75](#1.2.24-structured-data-files)  
1.2.25 Structured Data Files	[77](#1.2.25-structured-data-files)  
1.2.26 Structured Data Files	[79](#1.2.26-structured-data-files)  
1.2.27 Structured Data Files	[81](#1.2.27-structured-data-files)  
1.2.28 Exercise 2.2.3	[83](#1.2.28-exercise-2.2.3)  
1.2.29 Special File Types	[84](#1.2.29-special-file-types)  
1.2.30 Exercise 2.2.4	[85](#1.2.30-exercise-2.2.4)  
1.2.31 Tall vs Wide Data	[86](#1.2.31-tall-vs-wide-data)  
1.2.32 Tall vs Wide Data	[87](#1.2.32-tall-vs-wide-data)  
1.2.33 Tall vs Wide Data	[88](#1.2.33-tall-vs-wide-data)  
1.2.34 Exercise 2.2.5	[89](#1.2.34-exercise-2.2.5)  
1.2.35 Write to File	[90](#1.2.35-write-to-file)  
1.2.36 Delimiters	[91](#1.2.36-delimiters)  
1.2.37 Headers	[92](#1.2.37-headers)  
1.2.38 Appending to Files	[93](#1.2.38-appending-to-files)  
1.3 Data Transformation and Cleaning	[94](#1.3-data-transformation-and-cleaning)  
1.3.1 Section 2.3 Learning Objectives	[94](#1.3.1-section-2.3-learning-objectives)  
1.3.2 Introduction	[95](#1.3.2-introduction)  
1.3.3 Tidyverse and Pipes	[96](#1.3.3-tidyverse-and-pipes)  
1.3.4 Manipulating Data	[97](#1.3.4-manipulating-data)  
1.3.5 Selecting Rows of Data	[98](#1.3.5-selecting-rows-of-data)  
1.3.6 Practice Data	[99](#1.3.6-practice-data)  
1.3.7 Selecting Levels of a Factor Variable	[100](#1.3.7-selecting-levels-of-a-factor-variable)  
1.3.8 Subsetting Observations	[101](#1.3.8-subsetting-observations)  
1.3.9 Selecting Levels of a Factor Variable	[102](#1.3.9-selecting-levels-of-a-factor-variable)  
1.3.10 Selecting Levels of a Factor Variable	[103](#1.3.10-selecting-levels-of-a-factor-variable)  
1.3.11 Exercise 2.3.1	[105](#1.3.11-exercise-2.3.1)  
1.3.12 Subsetting on a Continuous Variable	[106](#1.3.12-subsetting-on-a-continuous-variable)  
1.3.13 Subsetting on a Continuous Variable	[107](#1.3.13-subsetting-on-a-continuous-variable)  
1.3.14 Subsetting on a Continuous Variable	[108](#1.3.14-subsetting-on-a-continuous-variable)  
1.3.15 Subsetting on Values in a String	[109](#1.3.15-subsetting-on-values-in-a-string)  
1.3.16 Subsetting on Values in a String	[110](#1.3.16-subsetting-on-values-in-a-string)  
1.3.17 Exercise 2.3.2	[112](#1.3.17-exercise-2.3.2)  
1.3.18 Subsetting on Multiple Conditions	[113](#1.3.18-subsetting-on-multiple-conditions)  
1.3.19 Exercise 2.3.3	[114](#1.3.19-exercise-2.3.3)  
1.3.20 Exercise 2.3.4	[115](#1.3.20-exercise-2.3.4)  
1.3.21 Subsetting Variables	[116](#1.3.21-subsetting-variables)  
1.3.22 Subsetting by Variables	[117](#1.3.22-subsetting-by-variables)  
1.3.23 Subsetting by Variables	[119](#1.3.23-subsetting-by-variables)  
1.3.24 Subsetting by Both Observation and Variable	[120](#1.3.24-subsetting-by-both-observation-and-variable)  
1.3.25 Exercise 2.3.5	[121](#1.3.25-exercise-2.3.5)  
1.3.26 Ordering Data Sets	[122](#1.3.26-ordering-data-sets)  
1.3.27 Ordering Data Sets	[123](#1.3.27-ordering-data-sets)  
1.3.28 Ordering Data Sets	[124](#1.3.28-ordering-data-sets)  
1.3.29 Creating New Variables	[125](#1.3.29-creating-new-variables)  
1.3.30 Creating New Variables	[126](#1.3.30-creating-new-variables)  
1.3.31 Creating New Variables	[127](#1.3.31-creating-new-variables)  
1.3.32 Overwriting Existing Variables	[128](#1.3.32-overwriting-existing-variables)  
1.3.33 Exercise 2.3.6	[129](#1.3.33-exercise-2.3.6)  
1.3.34 Grouping and Aggregating	[130](#1.3.34-grouping-and-aggregating)  
1.3.35 Grouping and Aggregating	[131](#1.3.35-grouping-and-aggregating)  
1.3.36 Grouping and Aggregating	[132](#1.3.36-grouping-and-aggregating)  
1.3.37 Exercise 2.3.7	[133](#1.3.37-exercise-2.3.7)  
1.3.38 Exercise 2.3.8: Check for Understanding	[134](#1.3.38-exercise-2.3.8:-check-for-understanding)  
1.3.39 Exercise 2.3.9: Advanced Exercise	[135](#1.3.39-exercise-2.3.9:-advanced-exercise)  
1.3.40 Exercise 2.3.10: Advanced Exercise	[136](#1.3.40-exercise-2.3.10:-advanced-exercise)  
1.3.41 Data Types	[137](#1.3.41-data-types)  
1.3.42 Renaming	[138](#1.3.42-renaming)  
1.3.43 Identifying Missing Values	[139](#1.3.43-identifying-missing-values)  
1.3.44 Removing Missing Values	[140](#1.3.44-removing-missing-values)  
1.3.45 Removing Missing Values	[141](#1.3.45-removing-missing-values)  
1.3.46 Removing Missing Values	[142](#1.3.46-removing-missing-values)  
1.3.47 Exercise 2.3.11	[143](#1.3.47-exercise-2.3.11)  
1.3.48 Data Types	[144](#1.3.48-data-types)  
1.3.49 Data Types	[145](#1.3.49-data-types)  
1.3.50 Strings	[147](#1.3.50-strings)  
1.3.51 Strings	[149](#1.3.51-strings)  
1.3.52 Strings	[151](#1.3.52-strings)  
1.3.53 Strings	[152](#1.3.53-strings)  
1.3.54 Strings	[154](#1.3.54-strings)  
1.3.55 Exercise 2.3.12	[155](#1.3.55-exercise-2.3.12)  
1.3.56 Dates	[156](#1.3.56-dates)  
1.3.57 Dates	[157](#1.3.57-dates)  
1.3.58 Dates	[158](#1.3.58-dates)  
1.3.59 Dates	[159](#1.3.59-dates)  
1.3.60 Exercise 2.3.13	[160](#1.3.60-exercise-2.3.13)  
1.3.61 Factors	[161](#1.3.61-factors)  
1.3.62 Factor Recoding	[162](#1.3.62-factor-recoding)  
1.3.63 Factor Recoding	[163](#1.3.63-factor-recoding)  
1.3.64 Factor Recoding	[164](#1.3.64-factor-recoding)  
1.3.65 Factor Recoding	[165](#1.3.65-factor-recoding)  
1.3.66 Factor Combining	[166](#1.3.66-factor-combining)  
1.3.67 Factor Combining	[167](#1.3.67-factor-combining)  
1.3.68 Other Conversion Notes	[169](#1.3.68-other-conversion-notes)  
1.3.69 Other Conversion Notes	[170](#1.3.69-other-conversion-notes)  
1.3.70 Exercise 2.3.14: Check For Understanding	[171](#1.3.70-exercise-2.3.14:-check-for-understanding)  
1.4 Relational Databases	[172](#1.4-relational-databases)  
1.4.1 Section 2.4 Learning Objective	[172](#1.4.1-section-2.4-learning-objective)  
1.4.2 Introduction	[173](#1.4.2-introduction)  
1.4.3 Relational Database	[174](#1.4.3-relational-database)  
1.4.4 Relational Database	[175](#1.4.4-relational-database)  
1.4.5 Combining Datasets	[176](#1.4.5-combining-datasets)  
1.4.6 Left Joins	[177](#1.4.6-left-joins)  
1.4.7 Right Joins	[178](#1.4.7-right-joins)  
1.4.8 Inner Joins	[179](#1.4.8-inner-joins)  
1.4.9 Outer or Full Joins	[180](#1.4.9-outer-or-full-joins)  
1.4.10 Joins	[181](#1.4.10-joins)  
1.4.11 Keys Using Multiple Variables	[182](#1.4.11-keys-using-multiple-variables)  
1.4.12 Keys With Duplicate Entries	[184](#1.4.12-keys-with-duplicate-entries)  
1.4.13 Keys With Duplicate Values	[185](#1.4.13-keys-with-duplicate-values)  
1.4.14 Combining Columns	[186](#1.4.14-combining-columns)  
1.4.15 Combining Rows	[188](#1.4.15-combining-rows)  
1.4.16 Exercise 2.4.1	[190](#1.4.16-exercise-2.4.1)  
1.5 Data Validation	[192](#1.5-data-validation)  
1.5.1 Section 2.5 Learning Objectives	[192](#1.5.1-section-2.5-learning-objectives)  
1.5.2 Introduction	[193](#1.5.2-introduction)  
1.5.3 Components of Data Accuracy	[194](#1.5.3-components-of-data-accuracy)  
1.5.4 Common Causes of Inaccuracies	[195](#1.5.4-common-causes-of-inaccuracies)  
1.5.5 Data Accuracy Example	[196](#1.5.5-data-accuracy-example)  
1.5.6 Data Accuracy Review	[197](#1.5.6-data-accuracy-review)  
1.5.7 Detecting Inaccurate Data	[198](#1.5.7-detecting-inaccurate-data)  
1.5.8 Data Cleaning	[199](#1.5.8-data-cleaning)  
1.5.9 Duplicate Records	[200](#1.5.9-duplicate-records)  
1.5.10 Duplicate Records	[202](#1.5.10-duplicate-records)  
1.5.11 Duplicate Records	[203](#1.5.11-duplicate-records)  
1.5.12 Duplicate Variables	[204](#1.5.12-duplicate-variables)  
1.5.13 Internal Consistency	[205](#1.5.13-internal-consistency)  
1.5.14 Internal Consistency	[206](#1.5.14-internal-consistency)  
1.5.15 Internal Consistency	[207](#1.5.15-internal-consistency)  
1.5.16 Internal Consistency	[208](#1.5.16-internal-consistency)  
1.5.17 Target Leakage	[209](#1.5.17-target-leakage)  
1.5.18 Target Leakage	[210](#1.5.18-target-leakage)  
1.5.19 Value Checking	[211](#1.5.19-value-checking)  
1.5.20 Exercise 2.5.1	[212](#1.5.20-exercise-2.5.1)  
1.5.21 Exercise 2.5.2	[213](#1.5.21-exercise-2.5.2)  
1.6 Missing and Extreme Values	[214](#1.6-missing-and-extreme-values)  
1.6.1 Section 2.6 Learning Objectives	[214](#1.6.1-section-2.6-learning-objectives)  
1.6.2 Introduction	[215](#1.6.2-introduction)  
1.6.3 Missing Data	[216](#1.6.3-missing-data)  
1.6.4 Missing at Random	[217](#1.6.4-missing-at-random)  
1.6.5 Missing at Random	[218](#1.6.5-missing-at-random)  
1.6.6 Permutation Test	[219](#1.6.6-permutation-test)  
1.6.7 Permutation Test	[220](#1.6.7-permutation-test)  
1.6.8 Permutation Test	[221](#1.6.8-permutation-test)  
1.6.9 Permutation Test Shortcut	[222](#1.6.9-permutation-test-shortcut)  
1.6.10 Imputation	[223](#1.6.10-imputation)  
1.6.11 Mean Imputation	[224](#1.6.11-mean-imputation)  
1.6.12 Mean Imputation	[225](#1.6.12-mean-imputation)  
1.6.13 Regression Imputation	[226](#1.6.13-regression-imputation)  
1.6.14 Regression Imputation	[227](#1.6.14-regression-imputation)  
1.6.15 KNN Imputation	[228](#1.6.15-knn-imputation)  
1.6.16 KNN Imputation	[229](#1.6.16-knn-imputation)  
1.6.17 Categorical Imputation	[230](#1.6.17-categorical-imputation)  
1.6.18 Categorical Imputation R	[231](#1.6.18-categorical-imputation-r)  
1.6.19 Categorical Imputation Python	[232](#1.6.19-categorical-imputation-python)  
1.6.20 Missing Target Variable Observations	[233](#1.6.20-missing-target-variable-observations)  
1.6.21 Missing Target Variable Observations	[234](#1.6.21-missing-target-variable-observations)  
1.6.22 Exercise 2.6.1	[235](#1.6.22-exercise-2.6.1)  
1.6.23 Identifying Outliers	[236](#1.6.23-identifying-outliers)  
1.6.24 Identifying Outliers	[238](#1.6.24-identifying-outliers)  
1.6.25 Identifying Outliers	[239](#1.6.25-identifying-outliers)  
1.6.26 Outlier Handling	[240](#1.6.26-outlier-handling)  
1.6.27 Outlier Handling	[241](#1.6.27-outlier-handling)  
1.6.28 DBSCAN	[242](#1.6.28-dbscan)  
1.6.29 DBSCAN	[243](#1.6.29-dbscan)  
1.7 Case Studies	[244](#1.7-case-studies)  
1.7.1 Section 2.7 Learning Objective	[244](#1.7.1-section-2.7-learning-objective)  
1.7.2 Introduction	[245](#1.7.2-introduction)  
1.7.3 Case Study 1.1: Website Visit Duration	[246](#1.7.3-case-study-1.1:-website-visit-duration)  
1.7.4 Case Study 1.1: Solution	[247](#1.7.4-case-study-1.1:-solution)  
1.7.5 Case Study 1.2	[248](#1.7.5-case-study-1.2)  
1.7.6 Case Study 1.2: Report	[249](#1.7.6-case-study-1.2:-report)  
1.7.7 Case Study 2.1: Chiropractic Visits	[250](#1.7.7-case-study-2.1:-chiropractic-visits)  
1.7.8 Case Study 2.1: Solution	[251](#1.7.8-case-study-2.1:-solution)  
1.7.9 Case Study 2.2	[252](#1.7.9-case-study-2.2)  
1.7.10 Case Study 2.2: Solution	[253](#1.7.10-case-study-2.2:-solution)  
1.7.11 Case Study 2.3: Report	[254](#1.7.11-case-study-2.3:-report)  
1.7.12 Case Study 2.3: Solution	[255](#1.7.12-case-study-2.3:-solution)  
1.7.13 Module 2 Bibliography	[256](#1.7.13-module-2-bibliography)

# **1 Working with Data** {#1-working-with-data}

## ***1.1 Data Pipeline*** {#1.1-data-pipeline}

### **1.1.1 Module 2 Learning Objectives** {#1.1.1-module-2-learning-objectives}

Working with Data 

Component Table1

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Module 2 Learning Objectives |
| Content |  Explain the basic concepts of database management, in particular, extract, transform, and load (ETL) operations. Explain the difference between a database, data lake, and data warehouse. Describe how different data structures can be used in different analytical tasks. Detect possible biases introduced when preparing data for a predictive model. Extract data from various file structures. Subset, aggregate, summarize, and otherwise modify data for specific exploratory or modeling purposes. Create data sets as a final product of extracting and transforming data that can be used in a predictive model. Explain the terminology and structure of relational databases. Describe how data collection practices and assumptions affect data quality. Evaluate the quality of appropriate data sources for a problem. Validate the data with regard to internal consistency. Handle missing data (including understanding the types of missing data) by selecting the appropriate action from deletion of the record, imputation, and adding a missing value flag. Check for outliers, both univariate and multivariate. Apply the information from this module to realistic examples.  |
| Footer | Panel Footer |

 Module 2

### **1.1.2 Section 2.1 Learning Objectives** {#1.1.2-section-2.1-learning-objectives}

Data Pipeline

Component Table2

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.1 Learning Objectives**  Explain the basic concepts of database management, in particular, extract, transform, and load (ETL) operations. Explain the difference between a database, data lake, and data warehouse. Describe how different data structures can be used in different analytical tasks. Detect possible biases introduced when preparing data for a predictive model.  |
| Footer | Panel Footer |

### **1.1.3 Module Introduction**  {#1.1.3-module-introduction}

“The goal is to turn data into information and information into insight.” (Fiorina, 2004\) 

Predictive modeling is typically performed for a specific purpose. This drives many of the decisions that are made in the modeling process, such as which model to use and what predictors to include. These decisions, however, should start before any models are built. Data comes in many forms. Very rarely will data be ready to implement in a predictive model when collected. Besides that, data being ready for modeling means different things depending on not only the model but also the purpose for the modelling. 

The purpose of this module is to provide tools for working with data and preparing it for a predictive model. This includes examining the ethics and implications of using certain data, accessing and using data that is provided in various formats, cleaning and manipulating data, combining data from multiple sources, making logical checks on data, and dealing with cases of extreme or missing data. By the end of this module, you should be able to understand and have confidence in the data you are using when you fit a predictive model. 

Module Introduction 

### **1.1.4 Section Introduction** {#1.1.4-section-introduction}

Before we look at tools to use when working with data, it is important to understand where data comes from and what it looks like at various stages between collection and analysis. In this section we will also examine principles of fairness and bias when it comes to working with data and how to assess the quality of data. These ethical principles should be considered while moving data through its various stages prior to analysis.  
Section Introduction

### **1.1.5 Data Pipeline** {#1.1.5-data-pipeline}

A data pipeline is a set of processes that are established to organize the flow of data from the source to the analysis. A good data pipeline is often crucial for improving operations. There are individuals at the beginning of the pipeline who get the data from the source. Those at the end of the pipeline use the data in its final form. 

Initially data can take various shapes and forms. Think of the following examples of data that may come from different sources. 

* Survey of questions about political preferences  
* Transcription of words from a conversation  
* Times individuals check in and out of work  
* List of medications taken and how often they are taken  
* GPS information for a car

Each of these sources of data will be introduced to the data pipeline looking very different.  
Data Pipeline

### **1.1.6 Data Pipeline** {#1.1.6-data-pipeline}

The data at the end of a data pipeline can also take various shapes. One way to define the process of a data pipeline is through Extract-Transform-Load operations, or ETL. 

* **Extract** refers to collecting the data from several sources into a staging area.  
* **Transform** refers to the process of combining or synthesizing the data in ways to make it more useful to get information.  
* **Load** refers to placing the transformed data into a place that can be accessed by those who may use the data to answer questions.

Data Pipeline

### **1.1.7 Data Pipeline** {#1.1.7-data-pipeline}

Once extracted, the raw untransformed data is collected into a **data lake**. Once the data has been transformed into something more usable, the final data is loaded into a **data warehouse**. A **database** is a collection of usable data suited for a specific task. A data warehouse is a type of databas e, but it can also be a collection of several databases. 

The following diagram is a very simple ETL data pipeline. This process can be done multiple times, meaning that there are several steps where data is collected and stored for various purposes at various stages, so any specific data pipeline can take many forms or shapes.  
Data Pipeline

### **1.1.8 Data Warehouse Versus Data Lake** {#1.1.8-data-warehouse-versus-data-lake}

Data inside a data lake will be raw untransformed data. There is no guarantee that data from different sources will be compatible with each other. A data warehouse, on the other hand, contains data that has been cleaned and combined to be able to be used. Note that data is often lost in the transformation step of the data pipeline. As a result, when a data warehouse is created from a data lake, the data lake will likely have more information than the corresponding data warehouse. 

For example, there may be individual level data from a certain source that includes geographical locations. However, in the data warehouse, the individual data was aggregated and summarized by location, meaning that average values for each location are available, but specific individual level data has been lost. Observations that are incomplete may not be transferred at all to a data warehouse. Other information not deemed to be vital could be shrunk, summarized, or just left out. 

In other words, a data warehouse contains databases that were created for a specific purpose. It is possible, however, that it is not well suited for predictive analytics. In some cases it will be, but not every database resulting from ETL operations will be appropriate for every possible application of data. For this reason, it is important to understand how to work with data in data lakes as well as data warehouses.  
Data Warehouse Versus Data Lake

### **1.1.9 Data for Predictive Analytics** {#1.1.9-data-for-predictive-analytics}

It is then important to consider what makes good data for predictive analytics. This depends on which model will be used and the overall purpose. However, it is typical for data that is useful for predictive analytics to be in the form of a data frame. A **data frame** is a collection of data that is organized into rows and columns. Each row is considered to be a **record** where each column is considered to be a **variable**. Each individual element of the data frame is the **value** of the variable for a specific record.  
Data for Predictive Analytics

|  | Variable 1 | Variable 2 | Variable 3 | Variable 4 |
| ----- | ----- | ----- | ----- | ----- |
| Record 1 | Value of Variable 1 for Record 1 (V11) | V12 | V13 | V14 |
| Record 2 | V21 | V22 | V23 | V24 |
| Record 3 | V31 | V32 | V33 | V34 |
| Record 4 | V41 | V42 | V43 | V44 |

Examples of records include individual trials in a clinical study and individual insurance policies. Examples of variables include dosage amounts of a drug and the city in which the policyholder lives.

### **1.1.10 Data for Predictive Analytics** {#1.1.10-data-for-predictive-analytics}

Data frames are useful for many applications. Many databases and data warehouses are designed in the form of data frames as it is easy to look up either specific information about a certain record or to examine trends regarding a certain variable. A **data set** is the same as a data frame with the only difference being that each variable has a specific label that will classify it as a certain type. For example, one variable might be numeric while another is qualitative. A data frame does not need to have these classifications, and can therefore be more efficient in some cases, but understanding variable types is important and will be discussed in more detail later in this module. 

While these definitions are specific, be aware that it is quite common to see them incorrectly used in context. A collection of data in any form may be referred to a data set, data frame, database, or even just data in various situations you may encounter. Here is a review of the various terms with their definitions as used in this course: 

* Data frame \- data structured with rows and columns where records are given their own row and variables are given their own column  
* Data set \- data frame where each variable has a specific type classification  
* Database \- collection of data suitable for a specific purpose, perhaps containing one or more data frames or data sets   
* Data warehouse \- final form of data collected from various sources in a version that is usable for specific tasks, perhaps containing one or more databases  
* Data lake \- raw, unfiltered data extracted from source material and ready to be transformed and loaded into data warehouses

Data for Predictive Analytics

### **1.1.11 Data for Predictive Analytics** {#1.1.11-data-for-predictive-analytics}

The shape and structure of data is not the only thing to consider when preparing data for analysis. It is also important to examine the data for accuracy and consider the ethical implications of using certain types of data. Also there is a trade-off between safety and security of individuals represented by the data and the need for transparency and openness. For the remainder of this section we will cover principles of fairness and bias when working with data, working alongside the ethical framework established in Module 1\. The principle of data accuracy is covered in a later section of this module. 

The principles of fairness that we cover should be applied in all ETL operations and in any efforts made to prepare data for analysis.  
Data for Predictive Analytics

### **1.1.12 Fairness in the Context of Data**  {#1.1.12-fairness-in-the-context-of-data}

While discussions of fairness within an analytical context often focus on the analysis methodology itself, it is important to keep in mind the adage “garbage in, garbage out" often abbreviated GIGO. A model or analytical insight is limited by the quality of the data upon which it is based. If biased data is used to build a model, the model will result in flawed predictions. Issues of bias and unfair discrimination may originate in the data collection and selection process itself. Because these issues are often an unintentional consequence of the collection and selection of data for analysis: a) attempts to remove bias during the modeling process may give a false sense of confidence in the fairness of the analytical output; and b) even if bias is suspected, it may be difficult to identify and address the cause. Therefore, it is important to think about fairness when selecting data to begin with, rather than simply taking the data available without considering what biases it might contain. Being proactive during the data stage can help reduce the prevalence of problems found during the modeling phase or compilation of results. 

So, how does data impact fairness? Doesn’t data simply consist of objective measurements? As noted by Raden,  
Fairness in the Context of Data  
“How data \[is\] construed, recorded, and collected is the result of human decisions about what to measure, when and where and by what methods” (Raden, 2019).   
Data is created from certain input processes or devices, which may capture noise and errors. The data may go through mapping, merging, conversion/transformation, and compression before being used in predictive models. Each of these presents an opportunity to introduce bias into the data. Given the automated nature of many of these steps, the bias may be unintended and undetected. In addition to these, the data may contain fields that capture human decisions, which may be biased. It is imperative to understand potential sources of data bias and how to address them. 

Three such potential sources of data bias covered in this section are: 

* Selection bias  
* Measurement bias  
* Omitted variable bias

### **1.1.13 Sources of Data Bias: Selection Bias**  {#1.1.13-sources-of-data-bias:-selection-bias}

The most basic opportunity for data bias is also potentially the most overlooked. The choice of data to collect or use for an analysis may seem obvious, an after-thought. Many analysts have a database of information that they pull from – whatever observations are there is what they use. There may be some thought about observations to include or exclude, such as a decision to use a specific time period, but generally actuaries and their peers are limited by the data available. While databases are generally designed to answer specific questions, they sometimes end up being used to answer different questions. This can create bias in the results and illustrates the importance of using different data for different questions. 

Actuaries and other analysts may not be involved directly in designing the data collection and storage process. The further removed you are from the process, the easier it is to use the output without questioning. For example, these decisions may be siloed in an IT department. Whether available data is suitable for analytical purposes depends on the level and quality of communication between data engineers and data users, such as actuaries. External data sources are also becoming an increasingly important resource for analytics departments within organizations. End users have even less involvement in the curation of these data sources and may have less access to the context and background related to them. 

Another reason the choice of data may be overlooked is that good data is often scarce. This makes it seem justifiable to take data without carefully considering how the choices that shaped that data may impact an analysis.   
Sources of Data Bias: Selection Bias

### **1.1.14 Sources of Data Bias: Selection Bias** {#1.1.14-sources-of-data-bias:-selection-bias}

**Selection bias** occurs when the data in a sample is not representative of the target population. This can lead us to mistakenly generalize findings from the sample to the target population. For example, if a company wanted to gauge its customers’ satisfaction in experiences with the company and sent out an optional survey for customers to complete, there would be a self-selection bias problem. In this case, customers would have the option to participate or not in the survey. Customers may be more inclined to participate if they have had strong positive or strong negative experiences with the company. Therefore, those with more neutral thoughts may end up underrepresented, and ultimately create a biased result that does not embody the full population of customers. 

Both under- and over-representation of a group can result in an adverse outcome for that group. Analysis of data that underrepresents a group may overlook that group’s needs and mischaracterize their risk profile. Decisions may be made without an understanding of how they will impact groups that are underrepresented in the data. This possibility is especially acute for people who do not engage as frequently in activities that generate data. While many people are concerned with the safety issues around excessive data collection, the other side of this coin is “the nonrandom, systemic omission of people who live on big data’s margins, whether due to poverty, geography, or lifestyle, and whose lives are less 'datafied' than the general population’s” (Lerman, 2013).  
Sources of Data Bias: Selection Bias

### **1.1.15 Example: Selection Bias** {#1.1.15-example:-selection-bias}

An example in auto insurance where self-selection bias comes into play is with usage-based insurance (UBI) or telematics programs. These programs use devices (either smartphones or a device that plugs into the car itself) to collect detailed driving data from policyholders. Insurers believe this information, including mileage driven, time of day driven, and measurements of speed and acceleration, will be predictive of future losses. While the ultimate goal is to use this information to charge drivers based on their driving behavior and consistent with their risk profile, insurers recognize that policyholders that exhibit more risky behaviors may be reluctant to join a program that is likely to result in a higher rate for them. In order to encourage participants, companies often do not adjust rates based on the driving behavior or offer a discount-only program, where good drivers receive discounts and others see no change. Some programs even offer a discount simply for joining the program. 

The data collected through these programs is valuable and insurers are gleaning insights about which driver behaviors are most correlated with claims. However, one issue with relying on this data for the full population of drivers is that participants in these programs have self-selected to be included in them. The participants may be more likely to believe themselves to be “good” drivers – for others, who may not believe they will earn a lower rate through participation, the tradeoff of their personal data may not be worthwhile. This selection of “good” drivers could bias any analytical insights based on the resulting data. Self-selection bias would result if the insurer applied the findings, insights, and analysis from these “good” drivers to the full population of insured drivers.   
Example: Selection Bias

### **1.1.16 Under- and Overrepresentation**  {#1.1.16-under--and-overrepresentation}

Selection bias can result in certain groups being under-represented or over-represented in a data set. The impact of this bias depends on the intended use for the data. Extrapolating overall statistics will lead to inaccuracies if the data sample is not representative. This is seen in public opinion polling, where certain groups may be more likely to respond to the survey. 

For example, we might be interested in the adequacy of retirement savings. To analyze this, we could obtain data on defined contribution retirement accounts from an investment management company and compare the average savings to the average cost of living in retirement. Can you see the big problem that exists in our data sample? 

We are missing people who don’t have a retirement account at all\! Looking only at people with a retirement account will overestimate the adequacy of retirement savings as we are removing the population with the most inadequate retirement savings. To improve our analysis, we would need data on the group of people with no account.  
Under- and Over-representation

### **1.1.17 Under- and Overrepresentation**  {#1.1.17-under--and-overrepresentation}

Even if we are interested in relationships within the data (e.g., relativities of two different groups), as opposed to summary metrics, under- and over-representation poses a problem. Suppose we are interested not just in the overall adequacy of retirement savings, but also in how adequacy differs by profession (controlling for other factors). Specifically, we compare social workers and those who work in manufacturing. For illustration purposes, assume the following are true: 

* Our analysis shows social workers and manufacturing workers have similar retirement savings adequacy (after accounting for other factors)  
* Social workers are more likely to have student loan debt and as a result many social workers have opted to pay off their debt before opening a retirement account

Our data sample, drawn from retirement accounts at an investment management company, undersamples people who have no retirement account. Because these omitted data points would bring down the average savings for social workers disproportionately (as a result of their being more likely to have not opened an account), our estimate of social workers’ retirement savings adequacy is inaccurate. Our understanding of the relationship of profession to retirement savings adequacy is flawed. 

Note, however, that there are times when a population might be intentionally oversampled. For example, if a side effect of a drug correlated with ethnicity, we would want the sample to include an adequate number of people of each ethnicity to assure the ability to statistically isolate this interaction.  
Under- and Over-representation

### **1.1.18 Other Issues with Non-Representative Data**  {#1.1.18-other-issues-with-non-representative-data}

Even when groups are present in a data set in representative proportions, the completeness of certain data elements may differ across groups. Analysis based on this data may be disproportionately inaccurate for the affected groups. 

An example in life insurance is the use of data collected from wearable technology. Insurance companies see opportunities in collecting this data from policyholders. One potential benefit is the development of rating factors that will improve the prediction of claims. While the health metrics collected through these devices may lead to more accurate life insurance premiums, this data source is inherently skewed to people who can afford these devices. A 2019 Gallup poll on wearable technology illustrates this (McCarthy, 2019). For U.S. adults, it found: 

* About half of those in upper-income households either used or had used fitness trackers and health apps; this was true for about one third of middle-income households and just one quarter of lower-income households.  
* Adults younger than 55 are about twice as likely to have used these products as are adults aged 55 and older.

These two findings suggest that using wearable data would lead to a difference in data completeness across income levels and ages. Specifically, our wearable data would be less representative of older adults and adults from lower-income households. Therefore, predictions of claims costs would be less accurate for these groups because we have less information about their health (assuming metrics collected by wearable devices do indeed improve the accuracy of premiums). In using non-representative data, the modeler should be prudent and consider ethical values when adjusting the data for any incomplete, missing, or unbalanced data.   
Other Issues with Non-Representative Data

### **1.1.19 Causes of Selection Bias**  {#1.1.19-causes-of-selection-bias}

Causes of Selection Bias  
As we have noted, collecting data appears to be an objective process. However, there are many factors shaping which data is collected, and this shaping can lead to selection bias. 

The data we have available to us are shaped by nature, physical and logical realities, and human behavior. Sometimes the underlying process that produces data is unavoidably biased. 

Self-Selection   
Participation in some data-generating processes is dependent on certain characteristics that may correlate with metrics we observe. 

The example of drivers who sign up for a telematics program involves self-selection bias. The drivers who agree to participate likely view themselves as “good” drivers. The resulting data is limited to this group and ignores drivers who do not consider themselves to be “good” drivers. Whether drivers consider themselves “good” is likely to correlate with actual driving performance. This will affect the insights from any analysis of this data. 

Survivorship Bias   
Collected data is limited to subjects that “survived” some process. 

An example of this is looking at investment performance for a group of asset managers over a 10-year period. Those asset managers that performed poorly during the 10-year period may have not stayed in business over the study period, so the remainder included in the sample are the ones that did better.

### **1.1.20 Causes of Selection Bias** {#1.1.20-causes-of-selection-bias}

Causes of Selection Bias  
Data is Collected only for Observations that Meet Some Criteria   
Actuaries face this issue with insurance claims data in several ways. For example, insurable events that could result in claims may not be reported if their costs are below a deductible amount. Policyholders may also refrain from reporting claims that are only modestly above the deductible amount if they believe a claim will result in a higher rate. Further, two policyholders with the same size loss may handle this situation differently. A higher income bracket policyholder may not put in the claim to the insurer. However, a lower income bracket policyholder likely would file their claim, as they may not have the financial means to otherwise pay for their loss. The two policyholders in this example have the same loss history, but the data would reflect otherwise. If used to calculate potential future claims in setting premiums, this would more favorably, and unfairly, benefit the higher income bracket individual. 

Data Is Not Available Due to Technical Or Practical Limitations   
This is often the case for data collected using technology. As technology advances, we gain the ability to collect more information. Vehicle telematics and wearable devices are two examples that have been discussed in this section. This data is only available for recent time periods. Data collection might also be limited in certain geographies. Weather station data tends to correlate with population density. Rural areas with lower population density will likely have reduced granularity/completeness in these datasets. 

### **1.1.21 Example: Selection Bias Can Lead to Unfair Outcomes**  {#1.1.21-example:-selection-bias-can-lead-to-unfair-outcomes}

Consider the data collected for two hypothetical individuals (Lerman, 2013). 

Individual \#1   
She uses technology readily in all aspects of her life. She owns a smartphone, regularly executes Google searches, and has Gmail, Netflix, Spotify and Amazon accounts. She uses Facebook and Snapchat, with their default privacy settings, to keep in touch with friends. She dates through the website OkCupid. She travels frequently, tweeting and posting geotagged photos to Flickr and Instagram. Her wallet holds a debit card, credit cards, and a MetroCard for the subway and bus system. On her keychain are plastic barcoded cards for the customer rewards programs of her grocery and drugstore. In her car, a GPS sits on the dash, and a transponder (for bridge, tunnel, and highway tolls) hangs from the windshield. 

Individual \#2   
He does not rely on technology in most aspects of his life. He works a job that pays him in cash. He has no cell phone , no computer, no cable. He rarely travels and has no passport, car, or GPS. He uses the Internet, but only at the local library on public terminals. He purchases his goods and services in local stores, pays in cash and doesn’t bother with “customer rewards” programs. He primarily uses the public bus system to get around and pays the fare in cash.  
Example: Selection Bias Can Lead to Unfair Outcomes

### **1.1.22 Example: Selection Bias Can Lead to Unfair Outcomes  (copy)** {#1.1.22-example:-selection-bias-can-lead-to-unfair-outcomes-(copy)}

Much of the data generated by our hypothetical Individual \#1 is being used increasingly by businesses and the government. This data has the potential to improve access to financial services and other products. In the insurance industry, external data sources have supported, among other examples, more accurate underwriting, better service, and fraud detection. Those individuals without a record in these external data sets may be rated less favorably. In 2019, the New York State Department of Financial Services issued Circular Letter No. 1, providing guidance on the use of external data in underwriting for life insurance (New York State Department of Financial Services, 2019). The circular noted that certain models and algorithms attempted to make predictions about a consumer’s health status based on external data elements, including: 

* Retail purchase history  
* Social media, internet or mobile activity  
* Geographic location tracking  
* The condition or type of an applicant’s electronic devices  
* How the consumer appears in a photograph

While there are potential benefits from the use of these data sources, they may underrepresent economically disadvantaged groups (as well as any groups that voluntarily decide to limit their data tracking through their behaviors).  
Example: Selection Bias Can Lead to Unfair Outcomes

### **1.1.23 Measurement Bias**  {#1.1.23-measurement-bias}

A key concept we discussed in relation to selection bias was representativeness. In any example where we attempt to use data to answer some question, the data must be representative of the intended population in our question. Non-representative data may lead to potential inaccuracies and unfair outcomes. This may not only be true for our selection of data, but also for how we define elements within our data. 

**Measurement bias** is the systematic bias that arises due to the method of measurement. This could refer to errors in measurement of some quantity if they are systematic errors impacting one group differently than another. In the context of fairness, however, we will mostly focus on how certain methods for defining or measuring a metric of interest (not necessarily numeric) can impact the fairness of an analysis. 

Setting up an analytical problem requires defining each data element. In a predictive model we are interested in a “target variable” – that which we want to predict. The target variable should closely represent the problem we are trying to solve. This is simple and obvious in some cases. An actuary who wants to predict the claims costs for a policyholder can gather data on prior claims costs. However, sometimes the definition of the target variable requires judgement. If you wanted to know which job candidates would turn into the most productive workers, how would you define “productive”? 

To answer this question, you need to come up with a measure of job performance. An easy option might be to use the employee ratings that are determined annually. These are, theoretically, a measure of the best employees. However, are the ratings objective? Are there any issues that may bias an analysis that focuses solely on ratings as the measure of performance? If employee ratings have been affected by past or current bias, any analysis that uses them as an objective measure will be biased as well.   
Measurement Bias

### **1.1.24 Example: Measurement Bias** {#1.1.24-example:-measurement-bias}

Even if our measure of choice seems objective, there may be underlying processes that bias it. In one example, researchers examined an algorithm that was widely used to identify medical patients who require extra care. The algorithm used health care costs to measure patients’ needs. While this appears to be an objective metric, it resulted in biased decisions. Outcomes from the algorithm demonstrated that amongst patients assigned the same level of risk, black patients were sicker than white patients. Researchers found the cause of the discrepancy was the target variable (health costs). Health care spending is lower for black patients than for white patients with the same needs. While many factors determine why health costs for black patients are lower than white patients, the algorithm did not take any of those factors into account and therefore, relying solely on health costs to determine level of care needed introduced bias into the algorithm. As a result, the algorithm rated black patients healthier and in need of less care than equally sick white patients (Ziad Obermeyer, 2019).  
Measurement Bias

### **1.1.25 Causes of Measurement Bias**  {#1.1.25-causes-of-measurement-bias}

The examples above illustrate two ways measurement bias can creep into our data. Daniel Kahneman, psychologist and Nobel Prize winner, explains the underlying issue: “When faced with a difficult question, we often answer an easier one instead, usually without noticing the substitution” (Kahneman, 2011). 

In the first example, we replace the question “Who is a high-performing employee?” with the question “Who has a high annual rating?” In the second, the algorithm replaced “What are this person’s health needs?” with “What are this person’s health care costs?” 

As Kahneman notes, it is easy to make this substitution without noticing. This is especially true when we are asking a question about the future but answering the question by substituting with a question about the past. In predictive modeling, this is exactly what we are doing. We are “translating \[a problem\] into a question about the value of some target variable” (Barocas & Selbst, 2016). We need to be careful that the information we have about the past is relevant to our question about the future. Otherwise, we are answering a different question.   
Causes of Measurement Bias

### **1.1.26 Measurement Bias can Lead to Unfair Outcomes**  {#1.1.26-measurement-bias-can-lead-to-unfair-outcomes}

If our choice of measurement is biased, then any decision made using that measurement will likely be biased as well. “Big Data’s Disparate Impact” (Barocas & Selbst, 2016\) sums up the issues with measurement bias succinctly:  
Measurement Bias can Lead to Unfair Outcomes

So long as prior decisions affected by some form of prejudice serve as examples of correctly rendered determinations, data mining will necessarily infer rules that exhibit the same prejudice.  
In the previous module we discussed the Amazon hiring algorithm, which exhibited bias against female candidates (Dastin, 2018). If past hiring decisions disadvantaged female candidates, a model trained on these examples is likely to pick up the same bias, i.e., it is being trained to reproduce biased decisions. Even if we do not intentionally give the model any information about candidate sex, it can learn associations with proxy variables. 

Another example of this is St. George’s Hospital, which ran into difficulties developing a computer program to screen medical school applicants (Barocas & Selbst, 2016). The algorithm was trained on previous admission decisions, but as it turns out, those decisions discriminated against racial minorities and women. The resulting algorithm retained these same prejudices, formalizing into rules the previous decision-makers’ conscious or implicit bias. 

These examples demonstrate the need to carefully select measurements used in data analysis. Metrics that are subject to human judgement, such as employee ratings, are especially susceptible to measurement bias. However, as we have shown, seemingly objective metrics can also reproduce existing bias.

### **1.1.27 Feature Selection and Omitted Variable Bias**  {#1.1.27-feature-selection-and-omitted-variable-bias}

Up until now we have discussed how unfairness can result from the selection of our data and the definition of our metrics. If we are thinking in predictive modeling terms, these relate to the rows (or observations) in our data set and the target variable that we are predicting. In addition to these, unfairness can arise from our choice of explanatory or predictor variables, which are also called **features**. 

As with our target variable, the choice of features must be representative of the problem we are trying to solve. Explanatory variables are used to explain the target variable. Our understanding of this relationship depends on a solid understanding of these features; a feature may be picking up a relationship that we did not intend. 

**Feature generation** involves transforming the initially collected data into features that better represent or predict the target variable. Through feature generation we derive new features from data elements that can be used in analysis or predictive modeling. For example, if we have birth date and policy issue date in our dataset, we can derive the issue age feature. **Feature selection** involves using this transformed data and choosing which subset of features should be included within the model.  
Feature Selection and Omitted Variable Bias

### **1.1.28 The Feature Selection Process Can Lead to Unfair Outcomes**  {#1.1.28-the-feature-selection-process-can-lead-to-unfair-outcomes}

Feature generation and selection both involve judgment and domain expertise, which leaves the possibility for bias to creep into an analysis. Feature selection is also limited by the available data elements. 

One issue with feature selection is that we may revert to data features that are more convenient and less granular, resulting in modeled relationships that are less precise. An example of this in auto insurance has been the historical use of proxy factors such as sex, marital status and rough estimates from the policyholder of miles driven. This data was easy to capture, but not always representative of the underlying risk. In reality, individual driving habits may be more indicative of the risk, and can now be better captured by telematic devices if agreed to by the policyholder, though this in itself may introduce bias via data selection risk. Another example is the consideration companies give to the reputation of a job applicant’s college or university when hiring. This feature is imprecise and often provides little insight to an individual candidate’s qualifications. Individuals from economically disadvantaged groups may graduate from these schools at disproportionately low rates. Candidates from these groups may be less likely to be hired than equally qualified, or even less qualified, candidates who attended these prestigious schools. 

Sometimes the features selected for an analysis carry underlying bias, similar to what we saw for target variables impacted by measurement bias. Consider credit scores as an example. Historically, certain groups have had less access to credit due to discriminatory mortgage practices. Some theorize that this makes it more difficult for those in such groups to build credit over time through the mortgage lending process or build wealth through homeownership. While credit scores may provide important information for actuaries, there are concerns that credit-based features perpetuate discrimination. 

Some state insurance regulators have taken a closer look at variables that may perpetuate past unfair practices, such as credit-based insurance scores, education, and occupation. New York outlawed the use of education and occupation for auto insurance underwriting and rating in a 2017 regulation. The regulation followed an investigation from the Superintendent of Financial Services, which found that “insurers failed to establish that their use of education and/or occupation in establishing initial tier placement was not unfairly discriminatory” (Vullo, 2017).  
Feature Selection Can Lead to Unfair Outcomes

### **1.1.29 Omitted Variable Bias**  {#1.1.29-omitted-variable-bias}

**Omitted variable bias** occurs when a relevant explanatory variable is omitted from a predictive model. The model attributes the effect of the omitted variable to those that were included. This can lead to inappropriate underlying relationships in the model. We might inflate the importance of a variable that is merely correlated with the omitted variable. Decisions and predictions made based on a model that suffers omitted variable bias will be inherently inaccurate. 

Omitted variable bias has the potential to hide discriminatory effects and disguise them as benign. Earlier we covered an example of how the admissions process at St. George’s Hospital disadvantaged candidates from underrepresented groups and women (Barocas & Selbst, 2016). While we introduced this example in the context of measurement bias, omitted variable bias contributed to underrepresented groups and women being disadvantaged. Because past admissions decisions reflected fewer students from these groups, the algorithm learned that these candidates were less likely to be admitted, but it did not know to attribute those past decisions to the race or sex of the candidate. At face value, it seems non-discriminatory to exclude race and sex as explanatory variables in the model. In fact, organizations are often prohibited from collecting protected characteristics such as race. However, because these two factors were directly related to admissions decisions, omitting them resulted in the signal being attributed to other variables – for example, attendance at women’s colleges. Such unintentional discrimination is easy to overlook. It also makes intentional discrimination easier to disguise.  
Omitted Variable Bias

### **1.1.30 Addressing Data Fairness**  {#1.1.30-addressing-data-fairness}

A point we have stressed in this section is how easy it is to overlook bias that arises through the data collection and manipulation process. Because of this, awareness of the potential issues is an important first step. Knowing the potential pitfalls and causes can help identify cases that may lead to unfair outcomes. 

How can we address potential data fairness issues? First, we must proactively look for these problems. A deliberate and thoughtful approach to data collection is necessary. We mentioned that most actuaries and data analysts are removed from the initial data collection step. Whether internal or external data, actuaries may not have control over the data available to them. This should not discourage them from considering carefully the data they use. We should ask ourselves questions such as: 

* What processes shaped the data? What was it originally designed to answer?  
* Is this data representative of the intended population for my analysis?  
* Do certain segments within my data have too little data for accurate analytical insights?  
* Has my target variable (or any explanatory variable) been objectively defined? How might existing biases have impacted the choice or definition of this variable? Are there appropriate offsets?  
* Is it possible that training examples incorporate implicit or explicit bias, historical or otherwise?  
* Do my explanatory variables precisely and directly relate to my target variable?  
* Are any of my data features prohibited characteristics or strongly correlated with prohibited characteristics?

Addressing Data Fairness

### **1.1.31 Addressing Data Fairness** {#1.1.31-addressing-data-fairness}

We might not always be able to correct for issues we find when asking these questions. However, even if data is flawed, awareness can help us adjust when interpreting analytical results or determine if the data is so flawed that we cannot use it for our intended purpose. 

There may also be disagreement about what qualifies as “fair” or how to address concerns about fairness. We will cover some approaches to determining fairness later. Is prohibiting the use of a variable the best way to ensure fairness? Some might argue that excessive prohibition of any variable that is correlated with a protected characteristic would lead to less accurate results and inappropriate risk classification. This tension between multiple ethical values means there is not always a single correct or obvious approach. 

We should acknowledge the potential issues inherent in assembling data for analysis. We should be vigilant that we do not carelessly allow bias into our data. When possible, we should remove biases. Most of all, we should exercise care. The biggest mistake we can make with data is to be inattentive and careless about how we use it. This carelessness could be the result of many possible factors, including unrealistic expectations regarding predictive models, time pressure, or being asked to analyze unfamiliar data without access to important contextual information regarding the data.   
Addressing Data Fairness

### **1.1.32 Knowledge Check** {#1.1.32-knowledge-check}

A company offers a service to other businesses in which they can store the data their business generates from various sources in the cloud, without having to first organize or process it. What type of data structure does this represent?

Component Table3

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 4 |
| Option 1 | Database |
| Option 2 | Data frame |
| Option 3 | Data lake |
| Option 4 | Data warehouse |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| C \- A data lake consists of raw, unfiltered data extracted from source material, which is the structure being described here.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Options\</span\>\<br /\> A \- A database is a collection of data suitable for a specific purpose, perhaps containing one or more data frames or data sets, which is not what is being described here.\<br /\> B \- A data frame consists of data structured with rows and columns where records are given their own row and variables are given their own column, which is not the case here.\<br /\> D \- A data warehouse contains the final form of data collected from various sources in a version that is usable for specific tasks. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| C \- A data lake consists of raw, unfiltered data extracted from source material, which is the structure being described here.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Options\</span\>\<br /\> A \- A database is a collection of data suitable for a specific purpose, perhaps containing one or more data frames or data sets, which is not what is being described here.\<br /\> B \- A data frame consists of data structured with rows and columns where records are given their own row and variables are given their own column, which is not the case here.\<br /\> D \- A data warehouse contains the final form of data collected from various sources in a version that is usable for specific tasks. |

Knowledge Check

### **1.1.33 Knowledge Check** {#1.1.33-knowledge-check}

Which of the following are reasons that data bias in the data selection process may be overlooked by actuaries? Select all that apply.

Component Table4

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 4 |
| Option 1 | Actuaries are often not involved with their organization’s collection of data. |
| Option 2 | Data sources can be difficult to find; actuaries may be reluctant to disregard a potential data source even if there are potential bias issues. |
| Option 3 | Actuaries generally do not have strong data analysis experience. |
| Option 4 | Actuaries may not have access to background or context about third-party data sets when used to supplement internal data. |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| A \- Data collection and storage may be siloed in the IT department, leaving actuaries with little control over these decisions.\<br /\> B \- When data sources are scarce, it is easy to take them as they are, without scrutinizing \&ndash; take what you can get. D \- When using third-party data sets, actuaries may not have access to the kind of background information that would uncover potential biases in the collection process.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> C \- Generally, actuaries are skilled at handling data. |
| When the final attempt partially correct Show Popup |
| Incorrect |
| A \- Data collection and storage may be siloed in the IT department, leaving actuaries with little control over these decisions.\<br /\> B \- When data sources are scarce, it is easy to take them as they are, without scrutinizing \&ndash; take what you can get. D \- When using third-party data sets, actuaries may not have access to the kind of background information that would uncover potential biases in the collection process.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> C \- Generally, actuaries are skilled at handling data. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| A \- Data collection and storage may be siloed in the IT department, leaving actuaries with little control over these decisions.\<br /\> B \- When data sources are scarce, it is easy to take them as they are, without scrutinizing \&ndash; take what you can get. D \- When using third-party data sets, actuaries may not have access to the kind of background information that would uncover potential biases in the collection process.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> C \- Generally, actuaries are skilled at handling data. |

Knowledge Check

### **1.1.34 Knowledge Check** {#1.1.34-knowledge-check}

You are an actuary working for an insurance company that is launching a new wellness-based insurance product. This wellness product will adapt pricing based on data provided by policyholders’ wearable devices. That is, the more active a policyholder is, the lower the price they will pay for your company’s product. Which of the following are ethical issues that may arise from such a product and its data use? Select all that apply.

Component Table5

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 4 |
| Option 1 | The policyholder has her son use the wearable device, since he is much more active than she. She does this even though the insurance policy is for her, not her son. |
| Option 2 | The policyholder has a disability that has rendered him paralyzed, so he is not able to use the wearable device in the same way that non-disabled users are. |
| Option 3 | The policyholder decides not to participate, since he is concerned about what data is being sent to the insurance company and how this data is being protected. |
| Option 4 | The policyholder decides not to participate in the wearable program, since she doesn’t like the design and material the wearable is made of. |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| A \- This depicts fraud and abuse, as well as several potential data issues. By having a different individual use the wearable, the data your company is receiving is not accurate or reliable. Using such information may result in actions or decisions that are not ethical or fair.\<br /\> B \- This relates to the idea of fairness. Policyholders\&rsquo; fitness and ability levels may vary, which should be considered in the creation of such a program in an effort for fairness. Additionally, disability is a protected class that is covered in some anti-discrimination laws.\<br /\> C \- This illustrates a privacy concern policyholders may have, as well as the importance of a data security program to protect the personal data being collected by the wearables.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Options\</span\>\<br /\> D \- This is a personal preference, but not an ethical issue raised by the insurance product or data usage. |
| When the final attempt partially correct Show Popup |
| Incorrect |
| A \- This depicts fraud and abuse, as well as several potential data issues. By having a different individual use the wearable, the data your company is receiving is not accurate or reliable. Using such information may result in actions or decisions that are not ethical or fair.\<br /\> B \- This relates to the idea of fairness. Policyholders\&rsquo; fitness and ability levels may vary, which should be considered in the creation of such a program in an effort for fairness. Additionally, disability is a protected class that is covered in some anti-discrimination laws.\<br /\> C \- This illustrates a privacy concern policyholders may have, as well as the importance of a data security program to protect the personal data being collected by the wearables.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Options\</span\>\<br /\> D \- This is a personal preference, but not an ethical issue raised by the insurance product or data usage. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| A \- This depicts fraud and abuse, as well as several potential data issues. By having a different individual use the wearable, the data your company is receiving is not accurate or reliable. Using such information may result in actions or decisions that are not ethical or fair.\<br /\> B \- This relates to the idea of fairness. Policyholders\&rsquo; fitness and ability levels may vary, which should be considered in the creation of such a program in an effort for fairness. Additionally, disability is a protected class that is covered in some anti-discrimination laws.\<br /\> C \- This illustrates a privacy concern policyholders may have, as well as the importance of a data security program to protect the personal data being collected by the wearables.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Options\</span\>\<br /\> D \- This is a personal preference, but not an ethical issue raised by the insurance product or data usage. |

Knowledge Check

### **1.1.35 Knowledge Check** {#1.1.35-knowledge-check}

You are an actuary working on pricing a new auto insurance product. In completing the modeling work, you have included several explanatory variables including age, value of vehicle, and coverage level. Your supervisor has requested that sex not be included within the model as an explanatory variable. What type of data bias does this situation illustrate?

Component Table6

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 3 |
| Option 1 | Selection bias |
| Option 2 | Omitted variable bias |
| Option 3 | Measurement bias |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| A \- Selection bias occurs when data selection results in a data sample that is not representative of the target population. We do not see selection bias mentioned within this situation.\<br /\> \<br /\> B \- This appears to be an example of omitted variable bias, based on sex not being included in pricing. In setting up the model in this manner, it may result in attributions to other variables, despite sex actually having an impact on pricing.\<br /\> \<br /\> C \- Measurement bias is the systematic bias that arises due to the method of measurement. We do not see measurement bias mentioned within this situation. |
| When the final attempt partially correct Show Popup |
| Incorrect |
| A \- Selection bias occurs when data selection results in a data sample that is not representative of the target population. We do not see selection bias mentioned within this situation.\<br /\> \<br /\> B \- This appears to be an example of omitted variable bias, based on sex not being included in pricing. In setting up the model in this manner, it may result in attributions to other variables, despite sex actually having an impact on pricing.\<br /\> \<br /\> C \- Measurement bias is the systematic bias that arises due to the method of measurement. We do not see measurement bias mentioned within this situation. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| A \- Selection bias occurs when data selection results in a data sample that is not representative of the target population. We do not see selection bias mentioned within this situation.\<br /\> \<br /\> B \- This appears to be an example of omitted variable bias, based on sex not being included in pricing. In setting up the model in this manner, it may result in attributions to other variables, despite sex actually having an impact on pricing.\<br /\> \<br /\> C \- Measurement bias is the systematic bias that arises due to the method of measurement. We do not see measurement bias mentioned within this situation. |

Knowledge Check

### **1.1.36 Knowledge Check** {#1.1.36-knowledge-check}

Which of the following are questions you may ask in assessing and addressing data fairness for a model you are working with? Select all that apply.

Component Table7

| Type | Multiple Choice Question |
| :---- | :---- |
| Option Number | 4 |
| Option 1 | Is the data representative of the intended population for the analysis? |
| Option 2 | Could the training examples I used incorporate implicit or explicit bias, historically or otherwise? |
| Option 3 | Do the explanatory variables I used directly relate to the target variable? |
| Option 4 | Is the data stored in a password protected location? |

| When the question is answered correctly Show Popup |
| :---- |
| Correct |
| A \- Reviewing if the data is representative for the intended population is an important consideration related to data fairness.\<br /\> B \- It is important to train the model with examples that won\&rsquo;t create implicit or explicit biases, in using the data in a fair manner.\<br /\> C \- We should aim to use data where explanatory variables directly relate to the target variable.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> D \- Ensuring that the data is in a secure, password protected location is related to data security, not data fairness. |
| When the final attempt partially correct Show Popup |
| Incorrect |
| A \- Reviewing if the data is representative for the intended population is an important consideration related to data fairness.\<br /\> B \- It is important to train the model with examples that won\&rsquo;t create implicit or explicit biases, in using the data in a fair manner.\<br /\> C \- We should aim to use data where explanatory variables directly relate to the target variable.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> D \- Ensuring that the data is in a secure, password protected location is related to data security, not data fairness. |
| When the final attempt is incorrect Show Popup |
| Incorrect |
| A \- Reviewing if the data is representative for the intended population is an important consideration related to data fairness.\<br /\> B \- It is important to train the model with examples that won\&rsquo;t create implicit or explicit biases, in using the data in a fair manner.\<br /\> C \- We should aim to use data where explanatory variables directly relate to the target variable.\<br /\> \<br /\> \<span class="dki-text-style-bold"\>Incorrect Option\</span\>\<br /\> D \- Ensuring that the data is in a secure, password protected location is related to data security, not data fairness. |

Knowledge Check

## ***1.2 Reading and Writing Data*** {#1.2-reading-and-writing-data}

### **1.2.1 Section 2.2 Learning Objective** {#1.2.1-section-2.2-learning-objective}

Reading and Writing Data

Component Table8

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.2 Learning Objective**  Extract data from various file structures.  |
| Footer | Panel Footer |

### **1.2.2 Section 2 Introduction** {#1.2.2-section-2-introduction}

Recall that the final form for data that is ready for predictive analytics is a data frame or data set. Specifically, the data needs to have each record in its own row and each variable in its own column. This section will explore the Extract and the Load steps of the ETL process. After this section you will be able to read in data from a variety of formats and be able to manipulate the shape of the data into a data set that can be used for predictive modeling. You will then be able to write the data to a file for later use.   
Section 2 Introduction

### **1.2.3 Software** {#1.2.3-software}

The principles in this course are valid in any computing environment. However, we will focus on examples using syntax for R and Python. In that regard, we make the following assumptions about the computing environment:  
Software

Component Table9

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Using R  |
| Content |  Version 4.1.1 or higher RStudio Version 2021.09.0+351 or higher Installed libraries: tidyverse  |
| Footer | Panel Footer |

Component Table10

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Using Python  |
| Content |  Version 3.10.0 or higher Pandas version 1.3.4 or higher Installed libraries: pandas, matplotlib, seaborn, numpy, scikit-learn, autoimpute  |
| Footer | Panel Footer |

There will be instances where other libraries are used, but they are specific enough to a certain task that they will be introduced as they arise. 

It is assumed that the audience has a basic understanding of the language they will be using. For example, this module will not be teaching explicitly how to install and load libraries, perform basic mathematical operations, and use loops, functions, and if-else statements.

### **1.2.4 Software** {#1.2.4-software}

\[BEGIN LINK \-https://www.tidyverse.org/\]  
There are several ways to accomplish the same task. With that in mind, as the following principles are being taught, it is possible to accomplish the same task using a different syntax than the one presented.   
\[END LINK\]  
Software

Component Table11

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | Python Syntax Notes |
| Tab 1 Text | Python Syntax Notes |
| Tab 1 Content | The Python code provided should work in every environment. Popular ones include Spyder, and Jupyter Notebooks. However, the code provided will be in the form of an R Markdown File. Using the R package **reticulate**, RStudio can fully support a python computing environment. The first rmd file you work with contains instructions for setting up and running Python within RStudio. |
| Tab 2 Title | R Syntax Notes |
| Tab 2 Text | R Syntax Notes |
| Tab 2 Content | The R syntax introduced in this section relies heavily on the [446436\_1](#bookmark=id.ic697eodo5oc)[tidyverse](#bookmark=id.4f39eau2efw) suite of packages and functions. One of the biggest differences between **tidyverse** and base R that is encountered in this section is that tidyverse loads data in as an object called a **tibble**. In many ways a tibble and an R data frame work in exactly the same way. Tibbles have an advanced print feature that makes it easier to see large data at a glance. There are some other subtle differences that make tibbles slightly less flexible in certain situations, but more secure in the sense that fewer unexpected results will occur. In the majority of cases, data frames and tibbles will produce the same results. |

### **1.2.5 Tidy Data** {#1.2.5-tidy-data}

The ideal shape of data to use in predictive analytics has specific features. Namely the data should have the following three characteristics: 

* Each variable has its own column  
* Each record has its own row  
* Each value has its own cell

Data with these characteristics is called **tidy data**. Data that is not tidy is often called messy. The reason why tidy data is important is summed up by the quote by Hadley Wickham, “Tidy datasets are all alike, but every messy dataset is messy in its own way.” Many algorithms and models assume tidy data, and while there may be external reasons an algorithm or model may fail, the data structure will not cause them to fail. Because every messy data set is messy in a different way, there is no way to guarantee that the algorithm will function correctly. It is unreasonable to assume that a model can be built with every possible shape of data. For that reason, models will often assume the data is tidy. 

How might a data set contain data that is messy? It is possible to have multiple variables in one column. It is also possible to have cells in the data set that contain multiple values. This latter case is often called a nested structure, and is quite common when working with data coming from web applications.  
Tidy Data

### **1.2.6 Data Frames** {#1.2.6-data-frames}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_2\_python.rmd\]  
At this time download either the Python or R rmd file for this section ( [atpa\_2\_2\_python.rmd](#bookmark=id.txhan9lbs1iy) or [atpa\_2\_2\_r.rmd](#bookmark=id.bdnulfof32nq)). Also download two sets of data files that will be used in this section and in Section 7 ( [xml\_files.zip](#bookmark=id.cydu9s1oomt5) and [json\_files.zip](#bookmark=id.x7xqphwqutiy)).  
\[END LINK\]  
Data Frames

Component Table12

| Type | Callout |
| :---- | :---- |
| Content | If using Python within RStudio, run CHUNK 0 to set up the environment. |

Data frames are names of objects within R and Python that can store data in a tidy format. As mentioned in the introduction, R also has an object called a tibble that functions similarly to a data frame. You can create a data frame from a collection of vectors.

Component Table13

| Type | Callout |
| :---- | :---- |
| Content | For example, the code in CHUNK 1, which is also provided here, creates two vectors, (1,2,3) and ("a","b","c"). A data frame is then created using the vectors. The vectors are given names inside the data frames as *Numbers* and *Letters*. |

Component Table14

| Type | Tabset |
| :---- | ----- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **Var1 \<- c(1,2,3)Var2 \<- c("a","b","c")Df \<- tibble("Numbers" \= Var1, "Letters" \= Var2)Df**  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **Var1 \= \[1,2,3\]Var2 \= \["a","b","c"\]Df \= pd.DataFrame({"Numbers":Var1,"Letters":Var2})Df**  |
| Tab 3 Title | Output |
| Tab 3 Text | Output |
| Tab 3 Content | The output is shown here. **Numbers Letters** 1 a 2 b 3 c  |

### **1.2.7 Data Frames** {#1.2.7-data-frames}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_2\_python.rmd\]  
You can add additional variables to a data frame from existing vectors.  
\[END LINK\]  
Data Frames

Component Table15

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 2 creates a new vector of trues and falses. It is then added to the existing data frame that was previously created and named *Boolean*. |

In R, a positive boolean is denoted as TRUE while in Python it is denoted as True. When discussing boolean or logicals throughout this course for principles that apply to both it will be denoted as in R as TRUE and FALSE. Hence the output in the table below shows the R version of the boolean variable.

Component Table16

| Type | Tabset |
| :---- | :---- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **Var3 \<- c(TRUE, FALSE, FALSE)Df$Boolean \= Var3 \# adds Var3 and names it BooleanDf** |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **Var3 \= \[True,False,False\]Df\["Boolean"\] \= Var3 \# adds Var3 and names it BooleanDf**  |
| Tab 3 Title | Output |
| Tab 3 Text | Output |
| Tab 3 Content | The output is ![][image1]  |

Individual vectors can be accessed after a data frame is formed. For example, **Df$Numbers** in R or **Df\["Numbers"\]** in Python will provide the Numbers vector from the data frame. You can, instead, extract a specific column or row based on its numerical location. In R, **Df\[,1\]** will return the first column and **Df\[1,\]** will return the first row. In Python **Df.iloc\[:,0\]** will return the first column and **Df\[0,:\]** will return the first row.

### **1.2.8 Lists and Dictionaries** {#1.2.8-lists-and-dictionaries}

As a first example of data that is potentially messy, consider an object that collects other objects of varying sizes. In a data frame, each variable must be the same length, but a list in R and a dictionary in Python are able to store items of varying lengths. Consider a study where health measurements are taken every year for a group of individuals. However, for one reason or another, individuals stop getting health measurements taken and maybe others start part way through the study. In this case, having a data frame where every record is the same size might not make sense. One solution is to store the data as a list or dictionary.  
Lists and Dictionaries

Component Table17

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 3 creates a list or dictionary called food, where different types of foods are included in the list. |

Notice how the size of the objects in the list are different. In R, the list does not need to have names, but it is helpful. It is also important to understand how to extract values from lists or dictionaries. In R, list subsetting is done using double brackets, using either the number or the name, meaning **food\[\[1\]\]** is the same as **food\[\["breakfast"\]\]**. For Python dictionaries, single brackets are used, but the same convention holds, **food\[0\]** is the same as **food\["breakfast"\]**.

### **1.2.9 Read Files** {#1.2.9-read-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/txt\_files.zip\]  
The [txt\_files.zip](#bookmark=id.xirqfg9x44mx) file contains two files. The file football\_space.txt contains the following data exactly as is shown here: 

**Game Win Keeper**  
**1 1 Robertson**  
**2 1 Robertson**  
**3 0 Robertson**  
**4 1 Matthews**  
**5 1 Robertson**  
**6 0 Matthews**  
**7 1 Smith**

Text files treat each line as a new record. The columns for each record are then separated by a fixed value known as a delimiter. A delimiter denotes the end of the current value and the beginning of the next. In the example above, the delimiter is a space. This data is already tidy because each variable has its own columns (Game, Win, and Keeper), each record is given its own row, and each value has its own cell.  
\[END LINK\]  
Read Files

Component Table18

| Type | Callout |
| :---- | :---- |
| Content | Using the read\_table() function loads a data frame with the variables *Game*, *Win*, and *Keeper*. Run the code in CHUNK 4 to read the data into your computing environment. |

### **1.2.10 Read Files** {#1.2.10-read-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/football\_space.txt\]  
The default delimiter in the basic **read\_table()**function is a space. Perhaps more common than spaces as delimiters are commas. Here’s the same football data set but with commas as delimiters [football\_comma.csv](#bookmark=id.ftpyvk4or5pg). 

**Game,Win,Keeper**  
**1,1,Robertson**  
**2,1,Robertson**  
**3,0,Robertson**  
**4,1,Matthews**  
**5,1,Robertson**  
**6,0,Matthews**  
**7,1,Smith**

In this file, a comma is being used as a delimiter. This can be read in using csv read-in functions, where csv stands for Comma Separated Values.  
\[END LINK\]  
Read Files

Component Table19

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 5 to read in this data file. The function read\_csv() assumes the data is comma delimited. |

### **1.2.11 Read Files** {#1.2.11-read-files}

There may be reasons to use different delimiters. Spaces may be a convenient delimiter, but it is possible that a value has a space in it, such as a first and last name. Similarly, commas might be included in a data value. Other common delimiters include tabs, pipes, colons, and semicolons. To use a specific delimiter, use **delim \= "\[delimiter\]"** as a function argument in R or **sep \= "\[delimiter\]"** in Python. 

For example, the data file football\_semicolon.txt downloaded earlier uses semicolons as the delimiter. 

**Game;Win;Keeper**  
**1;1;Robertson**  
**2;1;Robertson**  
**3;0;Robertson**  
**4;1;Matthews**  
**5;1;Robertson**  
**6;0;Matthews**  
**7;1;Smith**

Read Files

Component Table20

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 6 to read this data in with a semicolon as the delimiter. Tab delimited files require the argument to be **delim \= "\\t"** in R and **sep \= "\\t"** in Python. |

### **1.2.12 Read Files** {#1.2.12-read-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/football\_skip.csv\]  
A text file may have an introduction, some lines at the beginning of the file that aren’t part of the data to be read in, such as the file [football\_skip.csv](#bookmark=id.r9dofod0oq06). 

**\# This file contains records for the**  
**\# first 7 games of the season**  
**\# with an indicator for a winning result**  
**\# and the name of the keeper**  
**Game,Win,Keeper**  
**1,1,Robertson**  
**2,1,Robertson**  
**3,0,Robertson**  
**4,1,Matthews**  
**5,1,Robertson**  
**6,0,Matthews**  
**7,1,Smith**

As a whole, this file no longer contains a tidy data set. Including the first several lines of this file may lead to unwanted results when using this data. Explicitly skip these files using the function argument **skip \= 4** in R and **skiprows \= 4** in Python. 

\[END LINK\]  
Read Files

Component Table21

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 7 to read in this file while explicitly skipping the first 4 lines. The resulting data set removes those extra lines and is tidy. |

### **1.2.13 Read Files** {#1.2.13-read-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/football\_nohead.csv\]  
Stored files will often come with header labels and typical read-in operations will recognize those. If the header is not offered, you have to tell the read-in operations to manually name the columns as with the file [football\_nohead.csv](#bookmark=id.v1bmbu9fb5qs). 

**1,1,Robertson**  
**2,1,Robertson**  
**3,0,Robertson**  
**4,1,Matthews**  
**5,1,Robertson**  
**6,0,Matthews**  
**7,1,Smith**

When this data is read in as is, the variable names are not useful. Provide a vector of variable names in R using the argument **col\_names \= c("Game","Win","Keeper")** and in Python using **names=\["Game","Win","Keeper"\]**.  
\[END LINK\]  
Read Files

Component Table22

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 8 to read in the files with the column names included manually. This procedure can also be used to overwrite the existing names of variables even when they already exist. |

### **1.2.14 Read Files** {#1.2.14-read-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/football\_nohead.csv\]  
Files can be used without headers, but when data has meaningful variable names, these should be included. It is worth noting what makes a good variable name or not. 

The characters that are allowable for variable names in both R and Python include 

* Lowercase (a-z) and uppercase (A-Z) letters  
* Numbers (0-9)  
* Underscores (\_)

In R, periods are also allowed in variable names, although standard conventions are moving away from the use of periods to underscores. The first character of a variable name must be a letter in R and must be either a letter or an underscore in Python. The first character cannot be a number in either. 

Variable names can be one word or several words. Spaces are not valid characters in variable names. Instead, using an underscore is quite common. For example, eye color could be written as **eye\_color**. Other examples include capitalizing each word ( **EyeColor**), camel case ( **eyeColor**), or simply ignoring the spaces ( **eyecolor**). 

It is important to make variable names that have meaning. For example, suppose your variable measures how soon after an incident an insurance claim was made. There is no small variable name that can encapsulate the details needed to understand exactly what that variable means, but something along the lines of **time\_to\_claim** does give a lot of information about what it could mean. Variable names can be too long to be functional. There isn’t a character limit, but having to retype long variable names repeatedly can be tedious. 

For example, **time\_until\_an\_insured\_makes\_an\_insurance\_claim\_after\_an\_accident** is clearly more descriptive but is much too long.  
\[END LINK\]  
Read Files

### **1.2.15 Exercise 2.2.1** {#1.2.15-exercise-2.2.1}

Exercise 2.2.1

Component Table23

| Type | Callout |
| :---- | :---- |
| Content | The labels for the column headers are given to you to use in CHUNK 9\. Use the rest of the chunk to load the data and add the variable names. A solution is presented in CHUNK 10\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/automobile.csv\]  
The [automobile.csv](#bookmark=id.evxj0temhvlw) data set\* contains several features regarding certain cars. Load the data into your environment. Note that there is no column header information. 

\*Schlimmer, J. (1987). Automobile Data Set, UCI Machine Learning Repository \[https://archive.ics.uci.edu/ml/datasets/Automobile\]. Irvine, CA: University of California, School of Information and Computer Science.  
\[END LINK\]

### **1.2.16 Structured Data Files** {#1.2.16-structured-data-files}

Suppose that a variable in a data frame is something more complicated than a number, character, or logical can provide. For example, a data set about test results can include information about a student, such as their name, address, ID, but then also contain information about each question on the exam they are taking. This question information could essentially be a data frame all on its own, with question numbers, correct answer, provided answer, points, etc. 

While we typically will try to take any data and make it tidy for a predictive model, many find the need for more flexibility. One option is to nest the data. A nested data set has values that are additional data frames or vectors. In this example, question information could be a data frame on its own that is nested within the data about the student. 

This type of data, while not directly useful for predictive modeling, can be very useful for other reasons. Displaying web pages in a neat manner where information can be grouped together or labeled in certain ways is more easily done when the data structure can provide such information. Besides nesting, there are other ways data can have a more complicated structure. Data values could have additional characteristics provided. For example, the question information could also include a reference to which number in a question bank the question came from. In either of these cases, it can be useful to know how to work with specific types of data structures with the goal of extracting information needed from these structures for an analysis or a predictive model.  
Structured Data Files

### **1.2.17 Structured Data Files** {#1.2.17-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/test\_simple.xml\]  
An XML (Extensible Markup Language) file has data elements that begin with the variable name enclosed in angle brackets (\<\>). 

Elements are often accompanied by **attributes** inside the brackets. The end of an element is marked the same as the beginning but with a forward slash. Earlier you downloaded a zip file with several XML files. One is called test\_simple.xml. The blue text called “bank” is an attribute and the green text called “Number” is an element. The *value* of the first Number element is 1\.  
\[END LINK\]  
Structured Data Files

Component Table24

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  **\<Scores\>**  **\<Question bank="78"\>** **\<Number\>1\</Number\>\<Correct\>A\</Correct\>\<Answered\>A\</Answered\>\<Points\>1\</Points\>** **\</Question\>** **\<Question bank="42"\>** **\<Number\>2\</Number\>\<Correct\>C\</Correct\>\<Answered\>C\</Answered\>\<Points\>1\</Points\>** **\</Question\>\<Question bank="59"\>** **\<Number\>3\</Number\>\<Correct\>C\</Correct\>\<Answered\>D\</Answered\>\<Points\>0\</Points\>** **\</Question\>** **\</Scores\>**  |
| Footer | Panel Footer |

### **1.2.18 Structured Data Files** {#1.2.18-structured-data-files}

In R, the XML package is required. The syntax for both R and Python with the expected output is shown here.  
Structured Data Files

Component Table25

| Type | Callout |
| :---- | :---- |
| Content | Run the code in CHUNK 11 to read in the test\_simple.xml file as a data frame. |

Component Table26

| Type | Tabset |
| :---- | ----- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **install.packages(“XML”) \# Run this only once to get the library installedlibrary(XML)\# View the file contents in XML formattest\_xml \<- xmlParse("test\_simple.xml")test\_xml\# Read the data and convert to a data frametest\_df \<- xmlToDataFrame("test\_simple.xml")test\_df** |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **pd.read\_xml(“test\_simple.xml”,parser=”etree”)** |
| Tab 3 Title | Output |
| Tab 3 Text | Output |
| Tab 3 Content |  **Number Correct Answered Points** 1 A A 1 2 C C 1 3 C D 0  |

### **1.2.19 Structured Data Files** {#1.2.19-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/test\_one\_student.xml\]  
The file test\_simple.xml has a very simple XML file structure. More complicated XML files require different solutions. For example, the file test\_one\_student.xml (downloaded earlier in a zip file) contains the information on the scores, but it is nested deeper in the file. Also included is information about the student. This is typical for XML files. 

Note that the structure that contains the data we want is completely within the Scores element. In this case, before converting to a data frame, the Scores element must first be extracted.  
\[END LINK\]  
Structured Data Files

Component Table27

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 12 provides code to do this. |

Component Table28

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  **\<Test\_Results\>**  **\<Candidate\>** **\<Name\>Steven\</Name\>\<ID\>07309198\</ID\>\<Scores\>** **\<Question bank="78"\>** **\<Number\>1\</Number\>\<Correct\>A\</Correct\>\<Answered\>A\</Answered\>\<Points\>1\</Points\>** **\</Question\>** **\<Question bank="42"\>** **\<Number\>2\</Number\>\<Correct\>C\</Correct\>\<Answered\>C\</Answered\>\<Points\>1\</Points\>** **\</Question\>\<Question bank="59"\>** **\<Number\>3\</Number\>\<Correct\>C\</Correct\>\<Answered\>D\</Answered\>\<Points\>0\</Points\>** **\</Question\>** **\</Scores\>** **\</Candidate\>** **\</Test\_Results\>** |
| Footer | Panel Footer |

The code uses what is called an **xpath** where a path must be created to inform the function where the element is that needs to be extracted. In this case, *Score* needs to be extracted, so the path to *Score* is first *Test\_Results,* then *Candidate*, then *Scor* *e*. The variables *Name* and *ID* are nested inside of *Candidate* and therefore are not on the path to *Score*. The Python code is simpler as you only need to specify the element name. 

### **1.2.20 Structured Data Files** {#1.2.20-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/test\_two\_students.xml\]  
The file test\_two\_students.xml (downloaded earlier in a zip file) contains candidate information for multiple candidates. When this occurs, it is possible to extract the data frames individually.  
\[END LINK\]  
Structured Data Files

Component Table29

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 13 to read in data with multiple candidates. |

### **1.2.21 Structured Data Files** {#1.2.21-structured-data-files}

Two more specific tools will be helpful in extracting data from XML files. 

1. Extract values from every element of a certain type  
2. Extract attributes from every element of a certain type

For example, every value associated with the *Points* element can be extracted in the test\_one\_student.xml file. To do this in R, a path must be established to the desired elements. To get to the *Points* element, the path is *Test\_Results*, *Candidate*, *Score*, *Question*, and finally *Points*. This is represented in the syntax shown here for the path arguments of these functions.  
Structured Data Files

Component Table30

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **test\_xml \<- xmlParse("test\_one\_student.xml")points \<- xpathSApply(test\_xml, path \= "/Test\_Results/Candidate/Scores/Question/Points", xmlValue)** Each Question element has a *bank* attribute. Attributes can be extracted in the same manner in R, with attributes specified instead of values. The label used for the attribute ( *ba* *nk* in this case) must be specified as follows: **bank \<- xpathSApply(test\_xml, path \= "/Test\_Results/Candidate/Scores/Question", xmlGetAttr,name="bank")** CHUNK 14 provides this code and combines the two resulting vectors into a data frame. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | In Python, you simply specify the element name; the full path is not required. By using “.//element\_name” you can extract the attribute with the specific element\_name. The following snippet extracts the values from the language element. **pd.read\_xml("test\_one\_student.xml",parser="etree",xpath=".//Points")** The *bank* attribute was already extracted when the data was read-in in CHUNK 11\. CHUNK 14 takes the bank variable from that and creates a data frame. |

### **1.2.22 Structured Data Files** {#1.2.22-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/mort.xml\]  
The file mort.xml\* (downloaded earlier in a zip file) contains mortality data. There is a lot of extra information before the actual data is provided. You can tell when the data begins when there are several repeated elements with single values for each. The data begins with the elements labeled as *Y*. These also have attributes labeled as *t*. The information above the data labels the data values as mortality rates and the attributes as age.  
\[END LINK\]  
Structured Data Files

Component Table31

| Type | Callout |
| :---- | :---- |
| Content | The code that extracts the data and creates a data frame with variables *age* and *mortality* are shown in CHUNK 15\. |

\[BEGIN LINK \-https://mort.soa.org\]  
In R, the path must be found from the beginning to the data values. By looking carefully at where elements begin and end, the path can be seen to be *XTbML*, *Table*, *Values*, *Axis*, and finally *Y*. 

Another approach to handling XML files is to open the file in Excel. When loaded into Excel, find the columns that label the path of the data, in this case Table/Values/Axis/Y. The attributes will also be loaded into the column labeled *Table*/ *Values*/ *Axis*/ *Y@t*. This data can be copied or saved and then exported into R or Python for using in an analysis. 

\*from [mort.soa.org](#bookmark=id.9nflvh1hc9xr)  
\[END LINK\]

### **1.2.23 Exercise 2.2.2** {#1.2.23-exercise-2.2.2}

Exercise 2.2.2

Component Table32

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 16 provides space to perform this task. CHUNK 17 provides a possible solution. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/disablement.xml\]  
Read in the data from the file disablement.xml\* (downloaded earlier in a zip file). Convert the variables into a data frame with appropriate labels.  
\[END LINK\]  
\[BEGIN LINK \-https://mort.soa.org\]  
\*from [mort.soa.org](#bookmark=id.1vybgsqisw4e)  
\[END LINK\]

### **1.2.24 Structured Data Files** {#1.2.24-structured-data-files}

Structured Data Files

Component Table33

| Type | Callout |
| :---- | :---- |
| Content | When the structure is simple, as is the case in test\_simple.json, the data can be read in with the syntax provided in CHUNK 18 and shown here. In R, the jsonlite package is required. |

Component Table34

| Type | Tabset |
| :---- | ----- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | \# install.packages("jsonlite") \# Run this only once library(jsonlite) test\_df1 \<- fromJSON("test\_simple.json") test\_df1  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **pd.read\_json(“test\_simple.json”)**  |
| Tab 3 Title | Output |
| Tab 3 Text | Output |
| Tab 3 Content | The output is shown here.  **name id q1\_points q2\_points q3\_points** Steven 07309198 1 1 0 Chalise 12985540 0 1 1  |

Component Table35

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  **\[**  **{** **"name":"Steven","id":"07309198","q1\_points":"1",** **"q2\_points":"1",** **"q3\_points":"0"** **},** **{** **"name":"Chalise","id":"12985540","q1\_points":"0",** **"q2\_points":"1",** **"q3\_points":"1"** **}** **\]**  |
| Footer | Panel Footer |

A JSON (JavaScript Object Notation) file is structured where variable names and values are in quotation marks separated by colons. JSON files are very popular in web applications, and so data collected from web applications are often in this form. This is an example of a simple JSON file called test\_simple.json (downloaded earlier in a zip file).

### **1.2.25 Structured Data Files** {#1.2.25-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/test\_nested.json\]  
The structure of JSON files can become complicated, for example, by using a nested structure, as in test\_nested.json (downloaded earlier in a zip file) and shown here.   
**\[**   
**{**  
**"name":"Steven",**  
**"id":"07309198",**  
**"results":{**  
**"q1\_points":"1",**  
**"q2\_points":"1",**  
**"q3\_points":"0"**  
**}**  
**},**  
**{**  
**"name":"Chalise",**  
**"id":"12985540",**  
**"results":{**  
**"q1\_points":"0",**  
**"q2\_points":"1",**  
**"q3\_points":"1"**  
**}**  
**}**  
**\]**  
\[END LINK\]  
Structured Data Files

Component Table36

| Type | Callout |
| :---- | :---- |
| Content | The syntax is shown here and is provided in CHUNK 19\. |

\[   
{   
"name":"Steven",   
"id":"07309198",   
"results":{   
"q1\_points":"1",   
"q2\_points":"1",   
"q3\_points":"0"   
}   
},   
{   
"name":"Chalise",   
"id":"12985540",   
"results":{   
"q1\_points":"0",   
"q2\_points":"1",   
"q3\_points":"1"   
}   
}   
\]

Component Table37

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | Note how in R, the specific name of the nested item must be labeled. **fromJSON(“books\_nested.json”) %\>% unpack(Topics)**  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | In Python, the data must be loaded in the specific method shown. **import jsonwith open(“test\_nested.json”) as f:test\_df \= json.load(f)pd.json\_normalize(test\_df)** |

The results variable is nested, meaning that for each instance of results, there is a vector or data frame of other variables represented. To account for the nested structure, you can explicitly unnest the variables that are nested.

### **1.2.26 Structured Data Files** {#1.2.26-structured-data-files}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/test2\_nested.json\]  
Consider the JSON structure found in test2\_nested.json (downloaded earlier in a zip file). 

It is different from the previous file only in one way. The *results* variable is now inside square brackets (\[ \]) as well as the curly brackets ({ }). Both instances occur but they need to be handled differently.  
\[END LINK\]  
Structured Data Files

Component Table38

| Type | Callout |
| :---- | :---- |
| Content | This code is provided in CHUNK 20\. |

Component Table39

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | In R the only change is to use **unnest** instead of **unpack.fromJSON(“test2\_nested.json”) %\>% unnest(results)** |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | In Python, the name of the nested file must be distinguished. Because variables like *name* and *id* are not part of the nested variable results, they need to be specifically listed as additional metadata to include in the resulting data set. **import jsonwith open(“test2\_nested.json”) as f:test \= json.load(f)results \= pd.json\_normalize(books,record\_path=\['results'\],meta=\["name","id"\])** |

Component Table40

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  **\[**  **{** **"name":"Steven","id":"07309198","results":\[{** **"q1\_points":"1","q2\_points":"1","q3\_points":"0"** **}\]** **},{** **"name":"Chalise","id":"12985540","results":\[{** **"q1\_points":"0","q2\_points":"1","q3\_points":"1"** **}\]** **}** **\]** |
| Footer | Panel Footer |

### **1.2.27 Structured Data Files** {#1.2.27-structured-data-files}

Component Table41

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  **{**  **"exam\_info":"test on first unit of material","date":"01/14/2021","students":"2 students taking the exam","test":\[{**  **"name":"Steven","id":"07309198","results":\[{** **"q1\_points":"1","q2\_points":"1","q3\_points":"0"** **}\]** **},{** **"name":"Chalise","id":"12985540","results":\[{** **"q1\_points":"0","q2\_points":"1","q3\_points":"1"** **}\]** **}\]** **}** |
| Footer | Panel Footer |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/test2\_nested.json\]  
Finally, it is possible to have unnecessary information, perhaps about the data itself. In this case, the data portion of the file will be labeled. The following is from test3\_nested.json (downloaded earlier in a zip file). The file has extra information and the data is nested inside the test variable.  
\[END LINK\]  
Structured Data Files

Component Table42

| Type | Callout |
| :---- | :---- |
| Content | This code is provided in CHUNK 21\. |

Component Table43

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | In R, a list is created when read in. The element of the list labeled "test" will hold the information, which can then be unnested.**fromJSON("test3\_nested.json")\[\["test"\]\] %\>% unnest(results)** |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | In Python, the syntax is the same as it was before, except each variable that is named needs to be associated with the variable test. This is done by placing each variable in brackets with "test" coming before the variable name. **with open("test3\_nested.json") as f:test \= json.load(f)pd.json\_normalize(test,record\_path=\['test','results'\],meta=\[\['test','name'\],\['test','id'\]\])** |

### **1.2.28 Exercise 2.2.3** {#1.2.28-exercise-2.2.3}

Exercise 2.2.3

Component Table44

| Type | Callout |
| :---- | :---- |
| Content | Space is provided to complete this assignment in CHUNK 22 and the solution is provided in CHUNK 23\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/colors.json\]  
Read in and create a data frame based on the file colors.json (downloaded earlier in a zip file).  
\[END LINK\]

### **1.2.29 Special File Types** {#1.2.29-special-file-types}

A few additional file type extensions are .xls and .xlsx, .sav, and .xpt, which come from Excel, SPSS, and SAS respectively. It is important to know how to work with these file types because if you specialize in a certain language and your colleagues specialize in one of these other popular languages, you can still communicate as long as you can transfer data. The languages are listed in the following table along with the library needed to install and load to read the files and the command used to read the data in.  
Special File Types

| Language | Extension | R Library | R Command | Python Command |
| ----- | ----- | ----- | ----- | ----- |
| Excel | .xls, .xlsx | readxl | **read\_excel(filename)** | **pd.read\_excel(filename)** |
| Excel, k-th sheet | .xls, .xlsx | readxl | **read\_excel(filename, sheet \= k)** | **pd.read\_excel(filename,sheet\_name \= k-1)** |
| SPSS | .sav | haven | **read\_sav(filename)** | **pd.read\_spss(filename)** |
| SAS | .xpt | haven | **read\_xpt(filename)** | **pd.read\_sas(filename)** |

### **1.2.30 Exercise 2.2.4** {#1.2.30-exercise-2.2.4}

Exercise 2.2.4

Component Table45

| Type | Callout |
| :---- | :---- |
| Content | Use the space in CHUNK 24 to do this. A solution is in CHUNK 25\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/menu.xls\]  
Read in the file [menu.xls](#bookmark=id.dowobr7gbp8a) into 3 different data frames: “Dinner”, “Sides”, and “Desserts”, one for each of the sheets within the file.  
\[END LINK\]

### **1.2.31 Tall vs Wide Data** {#1.2.31-tall-vs-wide-data}

Besides nested data structures, another way data can be messy is if there are multiple variables in one column. There may be a number of reasons this could happen. The way data is recorded could be such where each variable for each individual is stored as its own record. This means that each record only contains one variable for one individual. There may be algorithms or database operations that actually work better with data structured in this way.  
Tall vs Wide Data

Component Table46

| Type | Callout |
| :---- | :---- |
| Content | Consider the following data set which is created in CHUNK 26\. |

This data is not tidy because there are multiple variables in one column. This data structure is often called **tall data** or **stacked data**. This data may be useful in certain applications, but it is not ready for a predictive analytics model. 

Tall data is also called, narrow or long. 

| ID | Variable | Values |
| ----- | ----- | ----- |
| 01 | language | Java |
| 01 | edition | third |
| 01 | author | Herbert Schmidt |
| 07 | language | C++ |
| 07 | edition | second |
| 07 | author | E.Balagurusamy |

### **1.2.32 Tall vs Wide Data** {#1.2.32-tall-vs-wide-data}

The opposite of tall data is **wide data** or **unstacked data.** One step to creating tidy data may include converting from tall to wide data.  
Tall vs Wide Data

Component Table47

| Type | Callout |
| :---- | :---- |
| Content | The following code is in CHUNK 27 and converts the tall data frame to a wide data frame. |

Component Table48

| Type | Tabset |
| :---- | ----- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | wide\_books \<- pivot\_wider(tall\_books,names\_from=Variable, values\_from \= Values) wide\_books  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **The variable used to index the data values, in this case ID, is no longer included in the data frame and needs to be added back in.wide\_books \= tall\_books.pivot(index=”ID”,columns=”Variable”,values=”Values”)wide\_books\["ID"\] \= \["01","07"\]wide\_books** |
| Tab 3 Title | Output |
| Tab 3 Text | Output |
| Tab 3 Content |  **ID language edition author** 01 Java third Herbert Schmidt 07 C++ second E.Balagurusamy  |

### **1.2.33 Tall vs Wide Data** {#1.2.33-tall-vs-wide-data}

In many cases it will make sense to represent data in tall form, perhaps for figures or tables.  
Tall vs Wide Data

Component Table49

| Type | Callout |
| :---- | :---- |
| Content | To convert from wide to tall form, use the code in CHUNK 28\. |

Component Table50

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | In R, you need to specifically list which variables are included in the transition. **tall\_again \<- pivot\_longer(wide\_books,c("language","edition","author"),**  **names\_to="Variable",values\_to="Values")  tall\_again** |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | In Python, **tall\_again \= pd.melt(wide\_books,id\_vars=\["ID"\])tall\_again** |

### **1.2.34 Exercise 2.2.5** {#1.2.34-exercise-2.2.5}

Exercise 2.2.5

Component Table51

| Type | Callout |
| :---- | :---- |
| Content | Use CHUNK 29 to do your work, a solution is provided in CHUNK 30\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/menu.xls\]  
The following data set is found in the [tall\_measure.csv](#bookmark=id.yf38up3rtrt5) file. It represents a longitudinal study, where individuals are measured repeatedly over several months. 

**Name,Month,Measurement**  
**Steve,November,11.70**  
**Steve,December,12.5**  
**Steve,February,14.8**  
**Steve,March,14.1**  
**Tanya,November,4.9**  
**Tanya,December,4.9**  
**Tanya,January,5.1**  
**Tanya,February,5.6**  
**Tanya,March,5.9**

Convert this to a wide data set. Why is there a missing data point in the wide data set but not the tall data set?  
\[END LINK\]

### **1.2.35 Write to File** {#1.2.35-write-to-file}

Once you have prepared your data frame, you can save it in a file for later use or to share with others. There are a few decisions to make when you are writing a file: 

* File type and structure  
* Delimiter choice  
* Inclusion of header information  
* Appending to an existing data frame

Both R and Python have the capability to write to many different types of file formats. For example, different packages will allow you to write data as an Excel file. Also, R and Python can create JSON and XML file structures from data. However, if you have tidy data, a simple text file is a universal file type that can be effective in nearly all situations. For this reason, the only file type being considered in these modules for writing data to file is a text file.  
Write to File

### **1.2.36 Delimiters** {#1.2.36-delimiters}

Data frames stored in text files can have many different delimiters.  
Delimiters

Component Table52

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 31 contains code to create a simple data frame and CHUNK 32 writes it to a file with spaces and a file with commas as delimiters. |

As mentioned earlier, comma delimited files are typically labeled with “.csv” file extensions, though unlike software such as Office, the choice of extension is completely arbitrary. It is important to note that these functions do not provide a warning if you are about to overwrite an existing file. 

Any delimiter can be used to write to file. One important consideration is that the data itself should be free of the delimiter chosen. For example, if data values have spaces, avoid using spaces as a delimiter. If data values have commas, avoid using commas.

### **1.2.37 Headers** {#1.2.37-headers}

Files can be written without headers, but when data has meaningful variable names, these should be included. The default is to use the variable names in the data frame. To save with different column names, the easiest way is to change the names of the data frame objects before writing to file.  
Headers

### **1.2.38 Appending to Files** {#1.2.38-appending-to-files}

Typically, data will be written to a new file, but there are situations where, instead of creating a new file, the data will need to be appended to an existing file. For example, you may collect similar data frequently and want to store it in one file. When the amount of data is large it might not be feasible to read in all the past data to combine with the new data. Instead you can simply store the new data in the existing data file. 

When data is appended, it is placed at the very end of the document and column labels are not included. Appending will not automatically match the existing format or structure, so appending must be done intentionally and carefully. Note that if you intend to append but instead write as if a new document, it will completely overwrite the existing document.  
Appending to Files

Component Table53

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 33 shows an example of appending data to an existing file. |

## ***1.3 Data Transformation and Cleaning*** {#1.3-data-transformation-and-cleaning}

### **1.3.1 Section 2.3 Learning Objectives** {#1.3.1-section-2.3-learning-objectives}

Data Transformation and Cleaning

Component Table54

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.3 Learning Objectives**  Subset, aggregate, summarize, and otherwise modify data for specific exploratory or modeling purposes. Create data sets as a final product of extracting and transforming data that can be used in a predictive model.  |
| Footer | Panel Footer |

### **1.3.2 Introduction** {#1.3.2-introduction}

After you read data into your environment, you can perform interesting transformations of your data. Many data solutions can be found without ever having to build a statistical model. In this section, techniques are introduced for subsetting, aggregating, and ordering data. Perhaps these techniques will be enough to answer a specific business question, or maybe these methods are important for getting the data ready for a more robust modeling approach. While the last section focused on the Extract and Load steps of ETL operations, this section focuses on the Transform step. Also, while this section is important for cleaning and validating data, there will be dedicated sections for dealing with outliers and missing values and checking the data for internal consistency. 

There is a lot of material related to data manipulation. The following references provide additional information and examples that will help you to learn and understand the concepts.  
Introduction 

Component Table55

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R Users |
| Tab 1 Text | R Users |
| Tab 1 Content | *R for Data* Science Chapter 5 [https://r4ds.had.co.nz](#bookmark=id.ffh5gli9y4t9) Tidyverse Cheat Sheets \- “Data transformation with dplyr” [https://www.rstudio.com/resources/cheatsheets/](#bookmark=id.oct1ha24l4py) [https://www.listendata.com/2016/08/dplyr-tutorial.html](#bookmark=id.fmvqgstwdm22)  |
| Tab 2 Title | Python Users |
| Tab 2 Text | Python Users |
| Tab 2 Content | Pandas Cookbook2 Chapters 4, 5, and 7 Data Wrangling with Pandas cheat sheet [https://pandas.pydata.org/Pandas\_Cheat\_Sheet.pdf](#bookmark=id.2x4rjjx7cod7) [https://www.educative.io/blog/python-pandas-tutorial](#bookmark=id.7q1shby05yet) [https://www.educative.io/blog/pandas-cheat-sheet](#bookmark=id.ajckxxcbnh8m) Petrou, T. (2017). *Pandas Cookbook: Recipes for Scientific Computing, Time Series Analysis and Data Visualization using Python*. Packt Publishing Ltd.  |

### **1.3.3 Tidyverse and Pipes** {#1.3.3-tidyverse-and-pipes}

Even within the tidyverse there are multiple ways of accomplishing the same task. A pipe is an operator inside R, written as %\>%, and is part of the tidyverse. Much of the syntax presented will be using pipes because the resulting workflow is readable and easy to understand. For example, if I wanted to use a filter and a select function (to be defined later) on a data frame “df,” without pipes this would be 

**select(filter(df,...,...))**

With pipes this is 

**df %\>% filter(...) %\>% select(...)**

When there are multiple steps to a process, pipes help the reader understand the exact order and details of the workflow; however it is possible to do all these operations without pipes and without tidyverse altogether.  
Tidyverse and Pipes

### **1.3.4 Manipulating Data** {#1.3.4-manipulating-data}

The data manipulation techniques that are shown in this section will not automatically change the target data frame. In either R or Python, the changes must be assigned as a new data frame. This means that 

**df %\>% filter(...)**

will not permanently change the data frame but 

**df \<- df %\>% filter(...)**

will. Instead of overwriting the existing data frame, a new data frame can be created, such as   
**df\_modified \<- df %\>% filter(...)**  
In this case, the original data frame is unchanged, but a new data frame is created. Much of this section includes code snippets with tables and other types of output shown. These snippets will typically not overwrite the existing data frame or create new ones, as they are simply there to help teach the syntax. In the rmd files, these data manipulations are typically saved as new data frames, as that is more typical if a user wants the changes to permanently impact the data. 

Manipulating Data

### **1.3.5 Selecting Rows of Data** {#1.3.5-selecting-rows-of-data}

Frequently, a data set will contain rows of data you need for an analysis and others you don’t. For example, the focus of an analysis may be limited to a particular portion of the full sample. There may be records that are duplicated, no longer relevant, or are incorrect. In addition to this, it is often useful for some visualizations to limit the data to specific values. 

There are many ways to subset a data set to just the records that you need. These are some examples of ways you may want to filter your data: 

* One or more levels of a factor variable  
* Certain ranges of a continuous variable  
* Certain characters in a string variable  
* Non-missing values or non-zero values

Perhaps you may want to filter on more than one of these at once.  
Selecting Rows of Data

### **1.3.6 Practice Data** {#1.3.6-practice-data}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_3\_r.rmd\]  
At this time, download the Rmd file(s) for this section for R or Python ( [atpa\_2\_3\_r.rmd](#bookmark=id.y24bcptpbubn) or [atpa\_2\_3\_python.rmd](#bookmark=id.u70j3k4y5snq)).  
\[END LINK\]  
Practice Data

Component Table56

| Type | Callout |
| :---- | :---- |
| Content | Consider the simple data set, trials, which can be created by running CHUNK 1\. |

| Phase | Count | Successes | Location |
| ----- | ----- | ----- | ----- |
| A | 50 | 20 | Austin Texas |
| A | 40 | 17 | Nashville Tennessee |
| A | 65 | 31 | Nashville Tennessee |
| B | 70 | 40 | Dallas Texas |
| B | 70 | 33 | Seattle Washington |
| B | 90 | 41 | Houston Texas |
| C | 30 | 12 | Orlando Florida |
| C | 20 | 9 | Cincinnati Ohio |
| C | 25 | 9 | El Paso Texas |

Note that *Phase* is a factor variable with three levels while *Location* is a character variable.

### **1.3.7 Selecting Levels of a Factor Variable** {#1.3.7-selecting-levels-of-a-factor-variable}

Subset to all observations in Phase A by creating a condition that, when the condition is true, observations are kept in the data set and when the condition is not met, the observations are removed. This type of condition is called a logical or a boolean.  
Selecting Levels of a Factor Variable

Component Table57

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 2 and the expected output is: **Phase Count Successes Location** A 50 20 Austin Texas A 40 17 Nashville Tennessee A 65 31 Nashville Tennessee  |

Component Table58

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Phase \== "A") |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Phase \== ‘A’”) |

Note that there are both single and double quotation marks in the Python code. In both R and Python, double and single quotation marks are mostly interchangeable. Some special cases require one or the other, but none of these are covered in these modules. It is important, however, that when quotation marks are inside of other quotation marks, that the outer and inner quotation marks are not the same. So, for example, the query function in Python requires quotation marks, as does the identification of the factor level. It is thus necessary that the quotation marks are different, as seen in the example.

### **1.3.8 Subsetting Observations** {#1.3.8-subsetting-observations}

Subsetting on observations can also be accomplished with bracket subsetting.  
Subsetting Observations

Component Table59

| Type | Callout |
| :---- | :---- |
| Content | This alternative approach is illustrated in CHUNK 2A. |

Component Table60

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | df\[condition,\] is equivalent to df %\>% filter(condition)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | df.loc\[condition,:\] is equivalent to df.query(condition)  |

Component Table61

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **trials\[Phase== “A”,\]** will not work but **trials\[trials$Phase \== “A”,\]** will work. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **trials.loc\[Phase== “A”,:\]** will not work but **trials.loc\[trials.Phase \== “A”,:\]** will work. |

When referencing variable names inside of brackets, they must include the dataframe. For example,

### **1.3.9 Selecting Levels of a Factor Variable** {#1.3.9-selecting-levels-of-a-factor-variable}

To subset to all observations in Phase A or in Phase B, create a conditional that returns TRUE if either condition is met. Two approaches are provided. The first checks if the values belong to a set of possible values, returning TRUE if it matches any in the set. The second approach uses an OR operator, which checks two separate logical values and returns TRUE if either are met.  
Selecting Levels of a Factor Variable

Component Table62

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 3 and the expected output is:  **Phase Count Successes Location** A 50 20 Austin Texas A 40 17 Nashville Tennessee A 65 31 Nashville Tennessee B 70 40 Dallas Texas B 70 33 Seattle Washington B 90 41 Houston Texas  |

Component Table63

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Phase %in% c(“A”,”B”) trials %\>% filter(Phase \== “A” | Phase \== “B”) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Phase in \[‘A’,’B’\]”) trials.query(“Phase \== ‘A’ or Phase \== ‘B’”) |

### **1.3.10 Selecting Levels of a Factor Variable** {#1.3.10-selecting-levels-of-a-factor-variable}

In many cases it may be easier to subset by times when a condition is not met. The “not” operator in both R and Python is **\!**. In this case, the subset is where Phase is not equal to A.  
Selecting Levels of a Factor Variable

Component Table64

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Phase \!= “A”) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Phase \!= ‘A’”) |

Component Table65

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 4 and the expected output is: **Phase Count Successes Location** B 70 40 Dallas Texas B 70 33 Seattle Washington B 90 41 Houston Texas C 30 12 Orlando Florida C 20 9 Cincinnatti Ohio C 25 9 El PasoTexas You can also reverse any logical conditional to create the opposite effect of the original conditional. This code is also in CHUNK 4\.  Here has another component. See component table66  |

Component Table66

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(\!(Phase \== “A”)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“not Phase \== ‘A’”) |

### **1.3.11 Exercise 2.3.1** {#1.3.11-exercise-2.3.1}

Exercise 2.3.1

Component Table67

| Type | Callout |
| :---- | :---- |
| Content | There is space for code in CHUNK 5 with the solution in CHUNK 6\. |

Use three different ways to subset to all locations where *Phase* is equal to A or C. 

### **1.3.12 Subsetting on a Continuous Variable** {#1.3.12-subsetting-on-a-continuous-variable}

Perhaps you only want numeric data in a certain range. For example, maybe you only want observations in the trials data where there were 50 or more counts.  
Subsetting on a Continuous Variable

Component Table68

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Count \>= 50\) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Count \>= 50”) |

Component Table69

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 7 and the expected output is: **Phase Count Successes Location** A 50 20 Austin Texas A 65 31 Nashville Tennessee B 70 40 Dallas Texas B 70 33 Seattle Washington B 90 41 Houston Texas  |

### **1.3.13 Subsetting on a Continuous Variable** {#1.3.13-subsetting-on-a-continuous-variable}

Use logical “and” and “or” operators to subset on more customized ranges. 

Include only data where counts are either less than 40 or more than 70\.  
Subsetting on a Continuous Variable

Component Table70

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Count \< 40 | Count \> 70\) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Count \< 40 or Count \> 70”) |

Component Table71

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 8 and the expected output is: **Phase Count Successes Location** B 90 41 Houston Texas C 30 12 Orlando Florida C 20 9 Cincinnati Ohio C 25 9 El Paso Texas  |

### **1.3.14 Subsetting on a Continuous Variable** {#1.3.14-subsetting-on-a-continuous-variable}

Include only data where counts are between 45 and 80 excluding the endpoints.  
Subsetting on a Continuous Variable

Component Table72

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Count \> 45 & Count \< 80\) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Count \> 45 and Count \< 80”) |

Component Table73

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 9 and the expected output is: **Phase Count Successes Location** A 50 20 Austin Texas A 65 31 Nashville Tennessee B 70 40 Dallas Texas B 70 33 Seattle Washington  |

### **1.3.15 Subsetting on Values in a String** {#1.3.15-subsetting-on-values-in-a-string}

While variables that contain strings can be subset as if they were factor variables, you can also subset based on the content of the strings. For example, we could subset on all locations that include Texas.  
Subsetting on Values in a String

Component Table74

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(str\_detect(Location, “Texas”)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.loc\[trials.Location.str.contains(‘Texas’),:\] |

Component Table75

| Type | Callout |
| :---- | ----- |
| Content | This string function does not work with query in Python, so the bracket approach is used (see CHUNK 2A). The code is in CHUNK 10 and the expected output is: **Phase Count Successes Location** A 50 20 Austin Texas B 70 40 Dallas Texas B 90 41 Houston Texas C 25 9 El Paso Texas  |

### **1.3.16 Subsetting on Values in a String** {#1.3.16-subsetting-on-values-in-a-string}

In the last example, we looked for a partial match in the string. If “Texas” was anywhere in the string, it would have been detected and included in the resulting data frame. There may be a reason to be more specific. In the trials data set you can subset by the following:  
Subsetting on Values in a String

Component Table76

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(str\_detect(Location,”^Texas”))  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.loc\[trials.Location.str.startswith(‘Texas’),:\] |

Strings that begin with certain values  
Strings that end with certain values   
Strings that contain digits

Component Table77

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(str\_detect(Location,”\\\\d”))  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.loc\[trials.Location.str.isdigit,:\] |

Component Table78

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(str\_detect(Location,”Texas$”))  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.loc\[trials.Location.str.endswith(‘Texas’),:\] |

### **1.3.17 Exercise 2.3.2** {#1.3.17-exercise-2.3.2}

Exercise 2.3.2

Component Table79

| Type | Callout |
| :---- | :---- |
| Content | Use CHUNK 11 to subset to locations that  contain “n” end with “n” start with “n” A solution is in CHUNK 12\. |

Note that case is important in string detection, which is why we get the result we do in part C. When using string operations in R, brackets can be used to accept any from a list of characters. For example, 

**trials %\>% filter(str\_detect(Location,”^\[Nn\]”))**

will find locations that start with either N or n.

### **1.3.18 Subsetting on Multiple Conditions** {#1.3.18-subsetting-on-multiple-conditions}

You may need to subset your data based on conditions dealing with multiple variables. For example, let’s say we want *Phase* A trials with *Count* above 40\.  
Subsetting on Multiple Conditions

Component Table80

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% filter(Phase \== “A” & Count \> 40\) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.query(“Phase \== ‘A’ and Count \> 40”) |

Component Table81

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 13 and the expected output is: **Phase Count Successes Location** A 50 20 Austin Texas A 65 31 Nashville Tennessee  |

### **1.3.19 Exercise 2.3.3** {#1.3.19-exercise-2.3.3}

Exercise 2.3.3

Component Table82

| Type | Callout |
| :---- | :---- |
| Content | Use CHUNK 14 for your work. A solution is in CHUNK 15\. |

Subset to observations where *Count* is less than 50 AND *Successes* are more than 15\. Subset to observations where either *Count* is less than 50 OR *Successes* are more than 15\.

### **1.3.20 Exercise 2.3.4** {#1.3.20-exercise-2.3.4}

Exercise 2.3.4

Component Table83

| Type | Callout |
| :---- | :---- |
| Content | Use CHUNK 16 for your work. A solution is in CHUNK 17\. |

Subset to include only locations that include an “s” AND have more than 10 successes.

### **1.3.21 Subsetting Variables** {#1.3.21-subsetting-variables}

Instead of selecting or removing certain rows of a data frame, you may want to remove or select certain variables or columns.  
Subsetting Variables

Component Table84

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% select(Count)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.loc\[:,\[“Count”\]\] |

Component Table85

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 18 and the expected output is:  **Count** 50 40 65 70 70 90 30 20 25  |

### **1.3.22 Subsetting by Variables** {#1.3.22-subsetting-by-variables}

More than one variable can be used. Also, instead of variable names, column index numbers could be used.  
Subsetting by Variables

Component Table86

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% select(Count,Successes) \#or trials %\>% select(2:3) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **trials.loc\[:,\[“Count”,”Successes”\]\] \#ortrials.iloc\[:,1:3\]**When subsetting a pandas data frame by index numbers use **iloc** and when subsetting by variable name use **loc** . |

Component Table87

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 19 and the expected output is shown here. Python only subsets variables using bracket notation, but it can be done in R as well. **trials\[,c(“Count”, ”Successes”)\]** is equivalent to **trials %\>% select(Count, Successes)** **Count Successes** 50 20 40 17 65 31 70 40 70 33 90 41 30 12 20 9 25 9  |

### **1.3.23 Subsetting by Variables** {#1.3.23-subsetting-by-variables}

You can also subset by specifying the variables that you don’t want from the data set by using the minus operator in R or drop in Python.  
Subsetting by Variables

Component Table88

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% select(-Location)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.drop(columns \= \[“Location”\]) |

Component Table89

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 20 and the expected output is:  **Phase Count Successes** A 50 20 A 40 17 A 65 31 B 70 40 B 70 33 B 90 41 C 30 12 C 20 9 C 25 9  |

### **1.3.24 Subsetting by Both Observation and Variable** {#1.3.24-subsetting-by-both-observation-and-variable}

You can subset by observation and variable. Generic code for doing this is below.  
Subsetting by Both Observation and Variable

Component Table90

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | df %\>% filter(condition) %\>% select(variable) \# or df\[condition,variable\] |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | df.loc\[:,\[“variable”\]\].query(condition) \# or df.loc\[condition,variable\] |

### **1.3.25 Exercise 2.3.5** {#1.3.25-exercise-2.3.5}

Exercise 2.3.5

Component Table91

| Type | Callout |
| :---- | :---- |
| Content | There is space for this in CHUNK 21 and a solution in CHUNK 22\. |

Subset the data to include Count and Successes for those in Phase A.

### **1.3.26 Ordering Data Sets** {#1.3.26-ordering-data-sets}

You can reorder observations in an entire data set by the values of a single column. Perhaps you wish to observe the largest or smallest values of a certain variable. Reordering can help with some visualizations as well. 

We can order the trials data set by *Count*.   
Ordering Data Sets

Component Table92

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% arrange(Count) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.sort\_values(“Count”) |

Component Table93

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 23 and the expected output is: **Phase Count Successes Location** C 20 9 Cincinnati Ohio C 25 9 El Paso Texas C 30 12 Orlando Florida A 40 17 Nashville Tennessee A 50 20 Austin Texas A 65 31 Nashville Tennessee B 70 40 Dallas Texas B 70 33 Seattle Washington B 90 41 Houston Texas  |

### **1.3.27 Ordering Data Sets** {#1.3.27-ordering-data-sets}

By default, the ordering is from smallest to largest. This can be reversed.  
Ordering Data Sets

Component Table94

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% arrange(desc(Count))  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.sort\_values(“Count”,ascending=False) |

Component Table95

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 24 and the expected output is: **Phase Count Successes Location** B 90 41 Houston Texas B 70 40 Dallas Texas B 70 33 Seattle Washington A 65 31 Nashville Tennessee A 50 20 Austin Texas A 40 17 Nashville Tennessee C 30 12 Orlando Florida C 25 9 El Paso Texas C 20 9 Cincinnati Ohio  |

### **1.3.28 Ordering Data Sets** {#1.3.28-ordering-data-sets}

Ties in ordering will default to the original order of the data set. However, we can set additional variables to break ties if desired.  
Ordering Data Sets

Component Table96

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% arrange(Count,Successes) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.sort\_values(\[“Count”,”Successes”\]) |

Component Table97

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 25 and the expected output is: **Phase Count Successes Location** C 20 9 Cincinnati Ohio C 25 9 El Paso Texas C 30 12 Orlando Florida A 40 17 Nashville Tennessee A 50 20 Austin Texas A 65 31 Nashville Tennessee B 70 33 Seattle Washington B 70 40 Dallas Texas B 90 41 Houston Texas The values of the *Successes* variable broke the tie when the *Count* variable values were the same.  |

### **1.3.29 Creating New Variables** {#1.3.29-creating-new-variables}

Feature generation is the practice of using transformations of variables in a predictive model. Often, transformations of variables are useful in finding important relationships in a predictive model or even just to improve the performance. 

Additional variables are added to a data frame after the last column. (While there may be reasons for display purposes or ease of handling to have the variables in a particular order, most analytics procedures are indifferent to variable order.) You can add a new column of existing data or transform data that already exists. For example, in the trials data set, we can create a new variable, *Rate*, that is *Successes* divided by *Count*.  
Creating New Variables

Component Table98

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% mutate(Rate \= Successes/Count) \# or trials$Rate \<- trials$Successes/trials$Count  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.assign(Rate \= trials.Successes/trials.Count) \# or trials\[“Rate”\] \= trials.Successes/trials.Count |

Component Table99

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 26 and the expected output is: **Phase Count Successes Location Rate** A 50 20 Austin Texas 0.40 A 40 17 Nashville Tennessee 0.43 A 65 31 Nashville Tennessee 0.48 B 70 40 Dallas Texas 0.57 B 70 33 Seattle Washington 0.47 B 90 41 Houston Texas 0.46 C 30 12 Orlando Florida 0.40 C 20 9 Cincinnati Ohio 0.45 C 25 9 El Paso Texas 0.36  |

### **1.3.30 Creating New Variables** {#1.3.30-creating-new-variables}

You can create a new variable that is a logical value depending on some condition, such as *Count* being greater than 50 or Texas being part of the value for *Location*. Multiple variables could be created at once.  
Creating New Variables

Component Table100

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% mutate(Large\_Count \= Count \> 50, In\_Texas \= str\_detect(Location,”Texas”)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.assign(Large\_Count \= trials.Count \> 50, In\_Texas \= trials.Location.str.contains(“Texas”)) |

Component Table101

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 27 and the expected output is: **Phase Count Successes Location Large\_Count In\_Texas** A 50 20 Austin Texas FALSE TRUE A 40 17 Nashville Tennessee FALSE FALSE A 65 31 Nashville Tennessee TRUE FALSE B 70 40 Dallas Texas TRUE TRUE B 70 33 Seattle Washington TRUE FALSE B 90 41 Houston Texas TRUE TRUE C 30 12 Orlando Florida FALSE FALSE C 20 9 Cincinnati Ohio FALSE FALSE C 25 9 El Paso Texas FALSE TRUE  |

### **1.3.31 Creating New Variables** {#1.3.31-creating-new-variables}

Factors can be created from a continuous variable by binning into different groups. This may be used in a predictive model when relationships are non-linear or when there is a certain interpretation of model output that is facilitated by binning. We could group *Count* into High, Medium, and Low categories by splitting at 35 and 65\. Data that falls on a boundary will be binned by default into the lower group, thus the value at 65 was assigned to the Medium category.  
Creating New Variables

Component Table102

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% mutate(Count\_Level \= cut(Count,breaks \= c(0,35,65,100),labels \= c(“Low”,”Medium”,”High”))) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.assign(Count\_Level \= pd.cut(trials.Count,bins \= \[0,35,65,100\],labels \= \["Low","Medium","High"\])) |

Component Table103

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 28 and the expected output is: **Phase Count Successes Location Count\_Level** A 50 20 Austin Texas Medium A 40 17 Nashville Tennessee Medium A 65 31 Nashville Tennessee Medium B 70 40 Dallas Texas High B 70 33 Seattle Washington High B 90 41 Houston Texas High C 30 12 Orlando Florida Low C 20 9 Cincinnati Ohio Low C 25 9 El Paso Texas Low  |

If instead of manually creating bins you simply want a certain number of bins (n) of equal size, use **breaks \= n** in R and **bins \= n** in Python instead of providing a list of cutoffs.

### **1.3.32 Overwriting Existing Variables** {#1.3.32-overwriting-existing-variables}

If the name of a newly created variable matches the name of a variable already in the dataset, then the old values are overwritten by the new values.  
Overwriting Existing Variables

Component Table104

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% mutate(Location \= “Unknown”) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.assign(Location \= “Unknown”) |

Component Table105

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 29 and the expected output is: **Phase Count Successes Location** A 50 20 Unknown A 40 17 Unknown A 65 31 Unknown B 70 40 Unknown B 70 33 Unknown B 90 41 Unknown C 30 12 Unknown C 20 9 Unknown C 25 9 Unknown  |

### **1.3.33 Exercise 2.3.6** {#1.3.33-exercise-2.3.6}

Exercise 2.3.6

Component Table106

| Type | Callout |
| :---- | :---- |
| Content | Space for your work is in CHUNK 30 and the solution is in CHUNK 31\.  |

Create two new binned variables for *Successes*. One should use cutoffs at 15 and 30 while the other should make four bins of equal width. For the latter task, allow the software to make the bins rather than manually identifying the appropriate cutoffs.

### **1.3.34 Grouping and Aggregating** {#1.3.34-grouping-and-aggregating}

Many summary statistics are more deeply understood when you split the observations in a data set by certain criteria. For example, the average value for *Count* in the trials data set is 51.1, but this varies widely when averaging by *Phase*.  
Grouping and Aggregating

Component Table107

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **trials %\>% group\_by(Phase) %\>% summarize(AverageByPhase \= mean(Count))** Note that in R, NAs would need to be removed to find the mean if they existed, i.e. mean(Count, na.rm=TRUE). They are skipped automatically in Python. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.groupby(“Phase”).agg({“Count”:“mean”}) |

Component Table108

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 32 and the expected output from R is: **Phase AverageByPhase** A 51.66667 B 76.66667 C 25.00000 The output in Python is similar with different values shown due to rounding.  |

### **1.3.35 Grouping and Aggregating** {#1.3.35-grouping-and-aggregating}

You can use grouping to also count how many there are in each group.  
Grouping and Aggregating

Component Table109

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% group\_by(Phase) %\>% summarize(NumPhase \= n()) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.groupby(“Phase”).size() |

Component Table110

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 33 and the expected output is: **Phase NumPhase** A 3 B 3 C 3  |

### **1.3.36 Grouping and Aggregating** {#1.3.36-grouping-and-aggregating}

You can also see how many unique values there are of another variable within each group. Here we see that there are only 2 unique locations for *Phase* A because “Nashville Tennessee” shows up twice.  
Grouping and Aggregating

Component Table111

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | trials %\>% group\_by(Phase) %\>% summarize(NumLocs \= n\_distinct(Location)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | trials.groupby(“Phase”).agg({‘Location’: ’nunique’}) |

Component Table112

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 34 and the expected output is: **Phrase NumLocs** A 2 B 3 C 3  |

### **1.3.37 Exercise 2.3.7** {#1.3.37-exercise-2.3.7}

Exercise 2.3.7  
Count the number of distinct *Count* values there are in each *Phase*.

Component Table113

| Type | Callout |
| :---- | :---- |
| Content | Space for your work is in CHUNK 35 and the solution is in CHUNK 36\. |

### **1.3.38 Exercise 2.3.8: Check for Understanding** {#1.3.38-exercise-2.3.8:-check-for-understanding}

Exercise 2.3.8: Check for Understanding

Component Table114

| Type | Callout |
| :---- | :---- |
| Content | Space for your work is in CHUNK 37 and a solution is in CHUNK 38\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/flights.csv\]  
The flights data set in the nycflights13\* R package contains departure information for planes leaving New York City. If not using R, the file [flights.csv](#bookmark=id.bsi7ckg1rpla) can be downloaded. We can see each of the principles discussed in action in a series of tasks. Apply these tasks independently to the data. 

1. Filter observations to only values where *carrier* is equal to “UA”  
2. Filter observations to only where the *dest* variable is either “MIA” or “ORD”  
3. Filter observations to only where *air\_time* is between 60 and 120 minutes.  
4. Filter variables to only *sched\_dep\_time* and *dep\_delay*  
5. Order the data from longest *distance* to shortest *distance*  
6. Create a new variable called *delayed* that returns TRUE if *dep\_delay* is greater than 0 and FALSE otherwise.  
7. Create a new variable called *mph* that is equal to *distance* divided by *air\_time* times 60  
8. Determine mean *dep\_delay* values by carrier. Call it *mean\_delay*.  
9. Each plane has a unique value for *tailnum*. Determine how many distinct planes each *carrier* uses. Call it *num\_planes*.

\[END LINK\]  
\[BEGIN LINK \-https://cran.r-project.org/package=nycflights13\]  
\* [https://cran.r-project.org/package=nycflights13](#bookmark=id.vvrfsx3kce78)  
\[END LINK\]

### **1.3.39 Exercise 2.3.9: Advanced Exercise** {#1.3.39-exercise-2.3.9:-advanced-exercise}

Exercise 2.3.9: Advanced Exercise

Component Table115

| Type | Callout |
| :---- | :---- |
| Content | Space for your work is in CHUNK 39 and a solution is in CHUNK 40\. |

A lot of power in these methods lies in combining them together to answer certain questions. Determine the top 5 most common destinations from JFK airport.

### **1.3.40 Exercise 2.3.10: Advanced Exercise** {#1.3.40-exercise-2.3.10:-advanced-exercise}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/hotel\_bookings.csv\]  
Use the [hotel\_bookings.csv](#bookmark=id.4wt50r5f71jy) data set.\* Create a new variable that is the total number of nights booked by adding *stay\_in\_weekday\_nights* and *stay\_in\_weekend\_nights*. Keep only bookings where the *reserved\_room\_type* and the *assigned\_room\_type* are equal. Find the mean number of total nights stayed grouped by *assigned\_room\_type*.  
\[END LINK\]  
Exercise 2.3.10: Advanced Exercise

Component Table116

| Type | Callout |
| :---- | :---- |
| Content | Space for your work is in CHUNK 41 and a solution is in CHUNK 42\. |

\*Mostipak, J. (2020) Hotel booking demand. Used under license [CC BY 4.0](#bookmark=id.lboakfnle74o). [https://www.kaggle.com/jessemostipak/hotel-booking-demand](#bookmark=id.vg6u30vsq91r)

### **1.3.41 Data Types** {#1.3.41-data-types}

\[BEGIN LINK \-https://stackabuse.com/how-to-format-dates-in-python/\]  
One important data step in preparing data for analysis is making sure the data types are consistent with what is expected. This includes identifying missing values and working with strings, dates and factors. The rest of this section includes these topics and introduces a number of additional data manipulation techniques within these categories. The following references contain information and examples on these topics. 

**R Users** 

* *R For Data Science* Chapters 14, 15, and 6  
* *RStudio Cheatsheets* \- [https://www.rstudio.com/resources/cheatsheets/](#bookmark=id.cr6i4cij85tb)   
  * "String Manipulation with stringr"  
  * "Dates and times with lubridate"  
  * "Factors with forcats"

**Python Users** 

* *Pandas Cookbook* chapters 3 and 8  
* Data Wrangling with Pandas cheat sheet  
  [https://pandas.pydata.org/Pandas\_Cheat\_Sheet.pdf](#bookmark=id.2er64m7nxbci)  
* [https://stackabuse.com/how-to-format-dates-in-python/](#bookmark=id.1vbpuf7hg1ek)

\[END LINK\]  
Data Types

### **1.3.42 Renaming** {#1.3.42-renaming}

Variable names are important. Having variable names with spaces or special characters can make future data manipulation difficult. It may also be helpful to rename variable names that are long or incorrectly labeled. Run CHUNK 43 to set up the data. We prefer shorter names with no spaces, so want to rename *Total Hours Recorded* to *Hours\_Recorded*.  
Renaming

Component Table117

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | security \<- security %\>% rename(Hours\_Recorded \= "Total Hours Recorded") security  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | security \= security.rename(columns \= {"Total Hours Recorded":"Hours\_Recorded"}) security  |

Component Table118

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 44 and the expected output is below. Note that unlike in previous work, we want this change to be permanent and so are placing the results in the same object. **Camera Hours\_Recorded Incidents** Lobby 51 2 Main Floor 59 1 Back Door \-1 0 Front Door 22 0 Offices 27 NA  |

### **1.3.43 Identifying Missing Values** {#1.3.43-identifying-missing-values}

An important step in data cleaning is recognizing missing values. Missing values could show up in a data set in the following ways: 

* NA or NaN  
* 0  
* \-1 (or other negative numbers when positive numbers are expected)  
* 999 (or 9999 or 999999999.99, etc.)  
* blank character, ""

In many cases you must understand the context of the variable to understand when a 0, \-1, or a blank character is missing and when it might be a valid value. There could also be multiple missing value codes for a variable depending on the reason the value was missing. 

For example, the security dataset contains hours recorded from various cameras at a facility. Note that \-1 shows up in *Hours\_Recorded*, which does not make sense in the context of the problem. However, having 0 incidents makes sense. The missing values are highlighted  
Identifying Missing Values

Component Table119

| Type | Callout |
| :---- | ----- |
| Content |  **Camera Hours\_Recorded Incidents** Lobby 51 2 Main Floor 59 1 Back Door \-1 0 Front Door 22 0 Offices 27 NA  |

### **1.3.44 Removing Missing Values** {#1.3.44-removing-missing-values}

One way to handle missing data is to just remove all records with incidents of missing data. Alternatives to this and why they might be used are considered later. Subsetting can be used to remove rows that have missing values.  
Removing Missing Values

Component Table120

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | security %\>% filter(Hours\_Recorded \!= \-1, \!is.na(Incidents)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | security.dropna(subset=\["Incidents"\]).query("Hours\_Recorded \!= \-1") |

Component Table121

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 45 and the expected output is: **Camera Hours\_Recorded Incidents** Lobby 51 2 Main Floor 59 1 Front Door 22 0  |

### **1.3.45 Removing Missing Values** {#1.3.45-removing-missing-values}

If NA is the code for missing in all variables, which is quite common, then you can easily remove all records with any NAs without needing to filter by variable.  
Removing Missing Values

Component Table122

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | security %\>% na.omit() |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | security.dropna() |

Component Table123

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 46 and the expected output is below.  **Camera Hours\_Recorded Incidents** Lobby 51 2 Main Floor 59 1 Back Door \-1 0 Front Door 22 0 In this particular instance, filtering would have been helpful as there are multiple missing value codes.  |

### **1.3.46 Removing Missing Values** {#1.3.46-removing-missing-values}

In R, NA is the designated missing value while in Python, it is NaN. Some operations automatically recognize these as missing and account for them appropriately. If working with these recognized missing value codes is preferable, it is possible to replace all missing value codes in a data frame with NA directly. This can be dangerous as this replaces all values in all variables. Be sure this is what is desired.  
Removing Missing Values

Component Table124

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | security\[security \== \-1\] \<- NA |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | security.replace(-1,np.nan) |

Component Table125

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 47 and the expected output is below. **Camera Hours\_Recorded Incidents** Lobby 51 2 Main Floor 59 1 Back Door NA 0 Front Door 22 0 Offices 27 NA  |

### **1.3.47 Exercise 2.3.11** {#1.3.47-exercise-2.3.11}

Exercise 2.3.11  
You are told that an *Incidents* value of 0 should be considered missing. Remove all missing values with this information, treating \-1, 0, and NA as missing. Then rename the variable *Incidents* to *Occurrences*.

Component Table126

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 48 provides space for your work and a solution is in CHUNK 49\. |

### **1.3.48 Data Types** {#1.3.48-data-types}

Knowing what data type you are working with is very important. For example, you may add numeric values 3 \+ 4 and you will get 7\. But if you try to add strings "3" \+ "4" in R you will get an error and in Python you will get "34." In either language the result is not what you expect. 

Data types that are worth being familiar with are: 

* Numeric   
  * Integer  
  * Float  
  * Double  
* String  
* Date  
* Factor  
* Boolean (TRUE / FALSE)

There are others, but these are the most common.  
Data Types 

### **1.3.49 Data Types** {#1.3.49-data-types}

You can convert objects to different data types. For example, let x \= "3" and y \= "4" be strings. Then x+y \= "34" in Python and produces an error in R. But if we convert those to numeric values, we can add them properly.   
Data Types   
Note that in Python you must specify integer versus float. If it is a whole number you should use **int()**, if it is not, you should use **float()**.

Component Table127

| Type | Callout |
| :---- | :---- |
| Content | Run the following code in CHUNK 50 to confirm that the result is 7\.  Here has another component. See component table128  |

Component Table128

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | x \<- "3"; y \<- "4" as.numeric(x) \+ as.numeric(y)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | x \= "3"; y \= "4" int(x) \+ int(y) |

Component Table129

| Type | Callout |
| :---- | :---- |
| Content | Likewise, you can turn a numeric value into a string. Run the code in CHUNK 51 and confirm the result is a string.  Here has another component. See component table130  |

Component Table130

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | as.character(3) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | str(3) |

### **1.3.50 Strings** {#1.3.50-strings}

There is a field of study that looks at large bodies of text and analyzes the words for patterns and makes inferences. A host of text analysis tools are available to analyze strings. We only scratch the surface with a few key tools. 

We’ve already seen subsetting data frames by the presence of certain patterns in strings. However, strings might not be ready for us to parse in this way. Some cleaning may need to happen first. 

We can control and adjust if a string is lower or upper case. For a specific string it can be done using the following code in CHUNK 52\.  
Strings

Component Table131

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | str\_to\_lower("String") \# string str\_to\_upper("String") \# STRING  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | "String".lower() \# string "String".upper() \# STRING  |

For a vector of strings, R is the same, but Python requires a loop. Run the following code in CHUNK 53 and examine the results. 

Component Table132

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | X \<- c("String1","String2") str\_to\_lower(X) str\_to\_upper(X)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | X \= \["String1", "String2"\] \[str.lower() for str in X\] \[str.upper() for str in X\]  |

### **1.3.51 Strings** {#1.3.51-strings}

You can replace all instances of certain substrings in a string. Run the following code in CHUNK 54 and confirm that "my" is being replaced by "your."  
Strings

Component Table133

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | x \<- "my\_string" str\_replace\_all(x,"my","your") X \<- c("my\_string1","my\_string2") str\_replace\_all(X,"my","your")  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | x \= "my\_string" x.replace("my","your") X \= \["my\_string1","my\_string2"\] \[str.replace("my","your") for str in X\]  |

This can be helpful in a situation where you are given a data frame and the values are characters with special symbols, such as money: "$84,510". If you try to convert this to numeric form as is, it will produce an error because of the "$" and "," are non-numeric characters.  
In R, brackets are used **(\[$,\])** to show that it is searching for dollar signs and commas. 

Component Table134

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 55 to execute this code.  Here has another component. See component table135  |

Component Table135

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | x \<- "$84,510" as.numeric(str\_replace\_all(x,"\[$,\]","")) \# 84510  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | x \= "$84,510" float(x.replace("$","").replace(",","")) \# 84510  |

### **1.3.52 Strings** {#1.3.52-strings}

To subset a string you will need to determine the position in the string where you want to create a substring. For example, you may want the first 3 values in "apple", which would then return "app".  
Strings

Component Table136

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | x \<- "apple" str\_sub(x,1,3) X \<- c("apple","pear") str\_sub(X,1,3)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | x \= "apple" x\[0:3\] X \= \["apple","pear"\] \[str\[0:3\] for str in X\]  |

Component Table137

| Type | Callout |
| :---- | :---- |
| Content | Run the following to code in CHUNK 56 to see how the words are subset.  |

### **1.3.53 Strings** {#1.3.53-strings}

You can also combine strings together to create a new string, such as "apple" and "crisp" to become "apple crisp". Run CHUNK 57 to see the examples on this and the next page.  
Strings  
If the strings that need to be combined are elements of a vector, you can specify certain characters to separate the strings when combined. 

Component Table138

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | h \<- "honey" str\_c(c(h, a, c),collapse="") \# no space between the words str\_c(c(h, a, c),collapse="-") \# places a dash between the words str\_c(c(h, a, c),collapse=" ") \# places a space between the words  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | "".join(\["honey","apple","crisp"\]) \# no space between the words "-".join(\["honey","apple","crisp"\]) \# places a dash between the words \# honey-apple-crisp " ".join(\["honey","apple","crisp"\]) \# places a space between the words \# honey apple crisp |

Component Table139

| Type | Callout |
| :---- | :---- |
| Content | Here has another component. See component table140  |

Component Table140

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | a \<- "apple" c \<- "crisp" str\_c(a, " ", c) \# apple crisp  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | "apple" \+ "crisp" \# applecrisp |

If the strings that need to be combined are elements of a vector, you can specify certain characters to separate the strings when combined.

### **1.3.54 Strings** {#1.3.54-strings}

Strings

Component Table141

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | dessert \<- "honey apple crisp" str\_split(dessert," ", simplify \= TRUE) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | dessert \= "honey apple crisp" dessert.split(" ")  |

The opposite of combining strings is separating. This can be done by selecting a pattern (such as a space) and separating out all values before and after the pattern. It will turn “honey apple crisp” into a vector of “honey”, “apple”, and “crisp”. This can be helpful when splitting state values from a city and state combination or splitting first and last names when a value contains the full names.

### **1.3.55 Exercise 2.3.12** {#1.3.55-exercise-2.3.12}

Exercise 2.3.12

Component Table142

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 58 has space for your work and a solution is in CHUNK 59\. |

Create a vector called "my\_words" that contains the words "Actuarial", "Exam", and "Passed". Perform the following tasks independently on the vector (meaning don’t keep the results from task to task). 

1. Change all the letters to lower case.  
2. Replace each letter "a" with a dollar sign, "$".  
3. Combine all three words putting spaces between the words.

### **1.3.56 Dates** {#1.3.56-dates}

There are many date formats and packages to manipulate them. Dates are read in as characters in many situations. A predictive model, though, may use dates as a predictor. To do this, the ordering of the dates is important and so they must be distinguished as dates. It may also be useful to split the dates by month or year and knowing how to extract that information is important. We will be using the **lubridate** package in R and the **datetime** package in Python. There are other possible packages or functions, but the ones presented are flexible and useful. 

One way to create a Date object is through functions that take date components as arguments.  
Dates

Component Table143

| Type | Callout |
| :---- | :---- |
| Content | Run the following code in CHUNK 60 to see the Date objects.  Here has another component. See component table144  |

Component Table144

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | library(lubridate) make\_date(year \= 2022, month \= 1, day \= 1\) make\_datetime(year \= 2022, month \=1, day \= 1, hour \= 9, min \= 30, sec \= 55\) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | import datetime as dt dt.date(year \= 2022, month \= 1, day=1) dt.datetime(year \= 2022, month \=1, day \= 1, hour \= 9, minute \= 30, second \= 55\) |

### **1.3.57 Dates** {#1.3.57-dates}

Dates are often represented as strings in data sets, such as "10/01/2021" is October 1, 2021\. To turn this into a date object, we need to distinguish the order to make sure this is not read in as January 10, 2021\. You may also need to distinguish separating symbols, such as "/".  
Dates

Component Table145

| Type | Callout |
| :---- | :---- |
| Content | Run the code in CHUNK 61\. Here has another component. See component table146  |

Component Table146

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **Date1 \<- "10/01/2021"Date2 \<- "20211001"mdy(Date1)ymd(Date2)Date\_Time \<- "10-01-2021 5:30:41"mdy\_hms(Date\_Time)** R has several variations of this function. The order of the letters y, m, and d is the order of the year, month, and day in the string, where h, m, and s correspond to the positions of hour, minutes, and seconds. The separating symbols do not matter. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **Date1 \= "10/01/2021"Date2 \= "20211001"dt.datetime.strptime(Date1, "%m/%d/%Y")dt.datetime.strptime(Date2, "%Y%m%d")Date\_Time \= "10-01-2021 5:30:41"dt.datetime.strptime(Date\_Time, "%m-%d-%Y %H:%M:%S")** In Python you have to include the special symbols in the structure. %Y, %m, %d, %H, %M, %S correspond to 4-digit-year, month, day, hour, minute, and second respectively. %y would correspond to a 2-digit-year. |

### **1.3.58 Dates** {#1.3.58-dates}

You can sort a data set by date and time, for example, the same way you would by a number or a character. Another useful concept is a duration, or a difference between dates. The functions today() and now() are special date and time functions available in both R and Python.  
Dates

Component Table147

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 62 to see the examples below. Here has another component. See component table148  |

Component Table148

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | today() \- make\_date(2021, 1, 1\) now() \- make\_datetime(2021, 1, 1, 9, 30, 55\) Time1 \<- hms("12:30:09") Time2 \<- hms("12:35:30") Time2 \- Time1  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | dt.date.today() \- dt.date(2021, 1, 1\) dt.datetime.now() \- dt.datetime(2021, 1, 1, 9, 30, 55\) Time1 \= dt.datetime.strptime("12:30:09", "%H:%M:%S) Time2 \= dt.datetime.strptime("12:35:30", "%H:%M:%S) Time2 \- Time1  |

### **1.3.59 Dates** {#1.3.59-dates}

Suppose you have daily data but want to include the month variable in a data set, or you have two data sets you wish to combine, one is by month and the other is by day. Or perhaps you just want to visualize the data at a more coarse grid than daily. These are reasons to extract certain aspects of the date variable. There may be similar reasons to extract only the day of the week or the year. The following demonstrates how to do this for different aspects of a date variable.  
Dates

Component Table149

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 63 to extract the relevant parts of a date variable.  Here has another component. See component table150  |

Component Table150

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **my\_date \<- mdy("07102003")month(my\_date) \# Extracts the month as a numbermonth(my\_date,label=TRUE) \# Extracts the name of the monthyear(my\_date) \# Extracts the yearmday(my\_date) \# Extracts the day of the monthwday(my\_date) \# Extracts the day of the week as a number, Sunday is 1wday(my\_date,label=TRUE) \# Extracts the day of week as a name** In R, the function argument **abbr \= FALSE** can be used in **month** or **wday** to not abbreviate the output. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | my\_date \= dt.datetime.strptime("07102003", "%m%d%Y") my\_date.strftime("%m") \# Extracts the month as a number my\_date.strftime("%B") \# Extracts the name of the month my\_date.strftime("%Y") \# Extracts the year my\_date.strftime("%d") \# Extracts the day of the month my\_date.strftime("%w") \# Extracts the day of the week as a number, Sunday is 0 my\_date.strftime("%A") \# Extracts the day of week as a name  |

### **1.3.60 Exercise 2.3.13** {#1.3.60-exercise-2.3.13}

Exercise 2.3.13

Component Table151

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 64 is available for your work with a solution in CHUNK 65\. |

Using the **nycflights13** package and the "flights" data set, create a new variable in the data set called *Date* that is equal to a Date object created from the variables *year*, *month*, and *day*.

### **1.3.61 Factors** {#1.3.61-factors}

A factor is a variable of characters or numbers where data entries can only have values in a pre-specified list of factor levels. Some issues arise with factors in data sets, including: 

* Factor values that should match but don’t due to entry issues. For example, someone may enter in their Sex as Male or male or simply M. These should all be included in the same factor level, but they will not be interpreted as being exactly the same.  
* There may be some large factor levels and many more less important small factor levels. For example, budget expenses may be recorded in 100 categories, even though 95% of the budget goes to only three categories whereas only 5% goes to the other 97\. This may hinder inference on the factor variable when modeling. When appropriate, these unimportant factor levels may need to be combined.  
* The factor ordering affects outputs for plots and analytical models. Reordering the factors and setting a new base level could help.

Many situations that apply variables as factors work just as well when the variables are strings. However, to convert a string or numeric variable to a factor variable, use 

**as.factor(variable)** in R and 

**pd.Series(variable,dtype="categorical"**) in Python.  
Factors

Component Table152

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 66 to create factor variables that are ordered and designated as unordered. |

Certain algorithms may work better when the factor levels are ordered, meaning that the levels are given a hierarchy. For example, a factor may be how someone feels about the service they received, and the levels are “good”, “okay”, and “poor”. In this case there is an ordering because “good” is better than “okay” and “okay” is better than “poor”. On the other hand, some algorithms may in fact work better without ordering. 

Component Table153

| Type | Callout |
| :---- | :---- |
| Content | Also included in CHUNK 66 is the code to convert an ordered variable into an unordered variable. |

When the factor levels are ordered, the order they are listed in the function argument becomes the ordering of the level. 

### **1.3.62 Factor Recoding** {#1.3.62-factor-recoding}

In this case, both *Sex* and *Answer* are factor variables. In this data set only two levels should be present for each. But those levels are coded differently, even when they are intended to be the same. The output shows there are five levels for *Sex* and four for *Answer*. We will present some strategies to make sure these levels are as they were intended.  
Factor Recoding

Component Table154

| Type | Callout |
| :---- | ----- |
| Content | Consider the following data set, which can be created by running CHUNK 67, collected from a survey.  **Individual Sex Answer** 1 Male Y 2 male Y 3 fem. N 4 Female Yes 5 M n  |

### **1.3.63 Factor Recoding** {#1.3.63-factor-recoding}

Consider a simple and yet insufficient approach of making all letters lower or upper case.  
Factor Recoding

Component Table155

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 68 and the expected output is below.  **Individual Sex Answer** 1 MALE Y 2 MALE Y 3 FEM. N 4 FEMALE YES 5 M N  |

Component Table156

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | survey %\>% mutate(Sex \= factor(str\_to\_upper(Sex)), Answer \= factor(str\_to\_upper(Answer))) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | survey.assign(Sex \= survey.Sex.str.upper(),Answer \= survey.Answer.str.upper()) |

### **1.3.64 Factor Recoding** {#1.3.64-factor-recoding}

In some cases, including this one, the first letter will be enough to distinguish the factor levels.  
Factor Recoding

Component Table157

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 69 and the expected output is below. **Individual Sex Answer** 1 M Y 2 M Y 3 F N 4 F Y 5 M N  |

Component Table158

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | Survey %\>% mutate(Sex \= factor(str\_sub(str\_to\_upper(Sex),1,1)), Answer \= factor(str\_sub(str\_to\_upper(Answer),1,1))) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | survey.assign(Sex \= pd.Categorical(survey.Sex.str.upper().str\[0\]),Answer \= pd.Categorical(survey.Answer.str.upper().str\[0\])) |

By both converting to lower case and restricting to the first letter, we have created compatible factor levels.

### **1.3.65 Factor Recoding** {#1.3.65-factor-recoding}

When string values should be matched but are farther apart than can be fixed by simple functions, you can directly recode every instance of certain values. For example, we can recode stray values in the Survey data set directly.  
Factor Recoding

Component Table159

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 70 and the expected output is below. **Individual Sex Answer** 1 Male Y 2 Male Y 3 Female N 4 Female Yes 5 Male n  |

Component Table160

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | survey %\>% mutate(Sex \= fct\_recode(Male \= "M", Male \= "male", Female \= "fem.")) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | survey\["Sex"\] \= pd.Categorical(survey\["Sex"\].map({"M":"Male","male":"Male", "fem.":"Female","Male":"Male","Female":"Female"})) |

### **1.3.66 Factor Combining** {#1.3.66-factor-combining}

Even when all the factor levels are matched correctly, there still may be too many to properly visualize or model. For example, the NYC Flights data set has information on carriers for certain flights. When you plot the counts for each carrier you see that there are factors with a significant flight load and many that are insignificant in comparison. Building a model with small factor levels can lead to issues, especially if extreme values of the target variable occur within the small factor levels. One common strategy is to combine smaller factor levels into one large factor level.  
Factor Combining

### **1.3.67 Factor Combining** {#1.3.67-factor-combining}

R has a more general way to do this. The function fct\_lump\_min will combine all factor levels below a certain threshold. For example, **fct\_lump\_min(carrier,min=1000)** would lump all the carriers that have fewer than 1000 flights into an “Other” category.  
Factor Combining

Component Table161

| Type | Callout |
| :---- | :---- |
| Content | The code is in CHUNK 71 and a graph of the results is below.  |

Component Table162

| Type | Callout |
| :---- | ----- |
| Content | CHUNK **Individual Sex Answer** 1 2 3 4 5  |

Component Table163

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | small\_levels \<- c("AS","F9","HA","OO","YV") flights %\>% mutate(carrier \= factor(ifelse(carrier %in% small\_levels,"Other",carrier))) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | small\_levels \= {"AS","F9","HA","OO","YV"} mask \= flights.carrier.isin(small\_levels) flights.carrier\[mask\] \= "Other" flights.carrier \= pd.Categorical(flights.carrier) |

We can combine certain factors into an "other" category or lump them in with other factors as needed. This could be done in a loop where they could be lumped based on how low they are, their name, or however you choose.

### **1.3.68 Other Conversion Notes** {#1.3.68-other-conversion-notes}

For some analyses, it is often important to convert Boolean variables to numeric where FALSE is recoded as 0 and TRUE is recoded as 1\. In many instances, a vector of Booleans can be treated as if this were already the case and the conversion happens automatically.  
Other Conversion Notes

Component Table164

| Type | Callout |
| :---- | :---- |
| Content | Run the following commands in CHUNK 72 and see what happens when you multiply a vector TRUEs and FALSEs by 1\.  Here has another component. See component table165  |

Component Table165

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | security\[,2\] \> 30 (security\[,2\] \> 30\) \*1  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | security.iloc\[:,1\] \> 30 (security.iloc\[:,1\] \> 30\) \*1  |

### **1.3.69 Other Conversion Notes** {#1.3.69-other-conversion-notes}

This last note is specific to R users. If you wish to convert a factor variable to numeric, you must first convert to a character.  
Other Conversion Notes

Component Table166

| Type | Callout |
| :---- | :---- |
| Content | Run the following code in CHUNK 73 and see what happens to the factor variable when converted directly to numeric. |

Component Table167

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | **my\_factor \<- as.factor(c(15,5,10,15,15,15,10))my\_factoras.numeric(my\_factor)** If the vector is first converted to a character, it transfers without issue.  **my\_char \<- as.character(my\_factor)my\_num \<- as.numeric(my\_char)** This issue is specific to R, Python does not have the same issue. |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | **my\_factor \= pd.Series(\[15,5,10,15,15,15,10\], dtype="category")pd.Series(my\_factor,dtype="int")** |

### **1.3.70 Exercise 2.3.14: Check For Understanding** {#1.3.70-exercise-2.3.14:-check-for-understanding}

Exercise 2.3.14: Check For Understanding

Component Table168

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 74 has space for your work. A solution is provided in CHUNK 75\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/automobile.csv\]  
Consider the automobile data set found in [automobile.csv](#bookmark=id.juswxxbpeql) that you have previously downloaded. Notice that the missing values here are marked as "?". There are missing values for the variables *normalized\_losses*, *num\_doors*, *bore*, *stroke*, and *price*. Perform the following tasks successively (keep the results from one task to the next). 

1. Replace those "?" values with NAs  
2. Remove all records with missing values  
3. Rename the variable *drive\_wheels* to *drive\_type*  
4. Recode all the values in the new variable *drive\_type*. Make "rwd" into "rear", "fwd" into "front", and "4wd" into "four"  
5. Change the values in the variable *engine\_location* so that only the first two letters show and make those two letters all uppercase  
6. There are some numeric columns that had "?", and as a result, they were marked as strings or characters. Convert those variables to numeric  
7. Combine factors in the *body\_style* variable so that there are only three factors: "sedan", "hatchback", and "Other"

\[END LINK\]

## ***1.4 Relational Databases*** {#1.4-relational-databases}

### **1.4.1 Section 2.4 Learning Objective** {#1.4.1-section-2.4-learning-objective}

Relational Databases

Component Table169

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.4 Learning Objective**  Explain the terminology and structure of relational databases.  |
| Footer | Panel Footer |

### **1.4.2 Introduction** {#1.4.2-introduction}

Data that is useful for building predictive models is rarely found in one place. Suppose you are building a model to predict how weather affects sales for a particular business. While it is likely that both sales and weather data are being collected daily, it is unlikely that they are being collected by the same source. For example, the business collects the sales data and the government collects the weather data. 

When building a predictive model, you should be prepared to pull data from a variety of sources. If there is a covariate that would be useful, as long as it is possible to obtain and ethical to use, it should be added to the data set. However, data from different sources often does not have the exact same format and structure. It’s common that the values do not match up. For example, one source of data could have information for all individuals who initially enter a study, whereas another source only has information for the ones who completed the study. 

In this section we introduce the concept of a Relational Database Management System (RDBMS). We also introduce how to combine data from multiple sources into one. More information about this can be found in the following references. 

R Users 

* *R for Data Science*, Chapter 13  
* *R for Everyone*, Chapter 14

Python Users 

* *Pandas Cookbook*, Chapter 9

Introduction

### **1.4.3 Relational Database** {#1.4.3-relational-database}

Recall that a database is a collection of data that is organized in such a way that it is easy to use. A relational database is a database that is structured so that pieces of information are connected through the use of a **key**. For example, a business will keep track of its employees’ hours and wages and possibly other items. This data might all be attached to an Employee ID. As long as the data is connected to the ID, it can all be connected to each other, and regardless of what the source is, it can eventually be combined. 

It is possible that there are multiple keys. For example, health data could be connected to an individual’s name and birthday. This is common when one key might not be enough to distinguish observations from each other. 

A **primary key** is a key that is completely contained in a single table or data set. This will uniquely identify each record. Each value in a primary key will be unique. A **foreign key** is a key in a different table or data set. A foreign key to one data set might be a primary key to another, so to help distinguish, the main data set is called a **parent** table and the other data sets are called **child** tables. The parent table will have a primary key and the children will all have foreign keys. It is possible to have just one child table or many child tables. In certain situations, the designation of a parent table might depend on the context of the problem you are trying to solve.  
Relational Database

### **1.4.4 Relational Database** {#1.4.4-relational-database}

A **Relational Database Management System** (RDBMS) is a system that provides services for creating, maintaining, updating, and curating a relational database. The most common versions of an RDBMS are a Structured Query Language (SQL), Oracle, and Microsoft Access. A RDBMS belonging to an entity will often be maintained by a manager or department. 

An RDBMS will provide functions for accessing elements of the database according to the relational structure. Occasionally, they will offer visual representations of the data, such as spreadsheets or figures. They can also include a degree of security where the full data set is not available, but you can “query” the data, meaning you request small amounts of data or a summary from the larger data set. This can be useful where a specific record is too sensitive to make available, but general functions of the data or summaries of the variables will be general enough to mask the private data of specific individuals. These queries involve many of the data manipulation techniques that were covered in Section 3 of this module, such as filtering rows, grouping and summarizing, and creating new variables based on functions of existing variables. 

A relational database will often live in a data warehouse, as it is a cleaned and curated version of the data. However, data with keys can exist in data lakes as well. A skill that is useful for creating data for a predictive analysis is to know how to combine multiple data sets based on the key. The remainder of this section will give tools for how to use a primary and a foreign key to combine two data sets.  
Relational Database

### **1.4.5 Combining Datasets** {#1.4.5-combining-datasets}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_4\_r.rmd\]  
At this time, download the rmd files for this section for R or Python ( [atpa\_2\_4\_r.rmd](#bookmark=id.h7fohfx9npfe) or [atpa\_2\_4\_python.rmd](#bookmark=id.a4v4gm458y4z)). 

Examine the two data sets at the right. Notice that while the information is different in the two data sets, it is possible to match up the data because they have a common variable, *Ticker*. If the top table is designated as the parent table, then the bottom table will be a child table. The primary key is *Ticker* in the top table and the foreign key is *Ticker* in the bottom table. 

The foreign key for records available in the child tables do not necessarily need to match the primary key for the parent table. This can be seen here as the *Ticker* value F is in the foreign key but not in the primary key. Also, the *Ticker* value PCG is in the primary key but not in the foreign key. Besides this, the order in which the keys appear does not need to be equivalent. While TSLA is in both the primary key and the foreign key, it is first in the primary key and second in the foreign key. These are aspects that make an RDBMS important as they are able to match up these records in the right way and make sure the right data is available.  
\[END LINK\]  
Combining Datasets

Component Table170

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 1 to create these tables. |

| Ticker | Name |
| ----- | ----- |
| TSLA | Tesla, Inc. |
| AMZN | Amazon.com, Inc. |
| WFC | Wells Fargo & Company |
| PCG | PG\&E Corporation |

| Ticker | Price |
| ----- | ----- |
| WFC | 49 |
| TSLA | 840 |
| F | 16 |
| AMNZ | 3400 |

### **1.4.6 Left Joins** {#1.4.6-left-joins}

A **join** combines two data frames based on a key. There are several versions of joins. While we have discussed tables in terms of parent and child tables, the terminology describing joins refers to left and right data sets. In a **left join**, two data sets are combined in such a way that the parent key, or the key in the left data set, is maintained exactly as is. Where the key in the right data set matches the key in the left data set, the data is combined and extra variables are added. The following code joins Table\_1 and Table\_2 where Table\_1 is designated as the left data set and Table\_2 is the right data set.  
Left Joins

Component Table171

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | left\_join(Table\_1,Table\_2,by=”Ticker”) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Table\_1.merge(Table\_2,on=”Ticker”,how=”left”) |

Component Table172

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 2 and the expected output is:  **Ticker Name Price** TSLA Tesla, Inc. 840 AMZN Amazon.com, Inc. 3400 WFC Wells Fargo & Company 49 PCG PG\&E Corporation NA  |

There are some important aspects to understand. First of all, note that the key of the resulting data set matches the key from Table\_1, which is the left data set in this example. This means that, even though PCG is not in Table\_2, it shows up in the left join. As Table\_2 provides the *Price* variable, PCG does not have a value for *Price* in the join, and it shows up as missing. Also, because F is not in Table\_1, even though it is in Table\_2, it does not show up in the left join.

### **1.4.7 Right Joins** {#1.4.7-right-joins}

A right join will maintain all of the records from the right data set instead of the left. The order of the records and variables in the join will match the left data set.  
Right Joins

Component Table173

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | right\_join(Table\_1,Table\_2,by=”Ticker”)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Table\_1.merge(Table\_2,on=”Ticker”,how=”right”) |

Component Table174

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 3 and the expected output is:  **Ticker Name Price** TSLA Tesla, Inc. 840 AMZN Amazon.com, Inc. 3400 WFC Wells Fargo & Company 49 F NA 16  |

The key values that exist only in the left data do not show up in a right join so PCG is not found. Also, key values found only in the right data set will have missing values for new data, hence the ticker F has a missing value for *Name*. 

In practice, a left join and a right join provide essentially the same result when the data sets are switched, although the ordering of variables and records would not necessarily be the same.

### **1.4.8 Inner Joins** {#1.4.8-inner-joins}

An inner join only includes records where the key value is common to both the left and right data sets.  
Inner Joins

Component Table175

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | inner\_join(Table\_1,Table\_2,by=”Ticker”)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Table\_1.merge(Table\_2,on=”Ticker”,how=”inner”) |

Component Table176

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 4 and the expected output is:  **Ticker Name Price** TSLA Tesla, Inc. 840 AMZN Amazon.com, Inc. 3400 WFC Wells Fargo & Company 49  |

Because PCG appears only in the left data frame and F appears only in the right data set neither appears in the inner join. In an inner join, the result is exactly the same regardless of which data set is considered the left or right data set, although the ordering may be different.

### **1.4.9 Outer or Full Joins** {#1.4.9-outer-or-full-joins}

Finally, a full join or an outer join is a join where records are included if the key value shows up in either the left or right data set.  
Outer or Full Joins

Component Table177

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | full\_join(Table\_4,Table\_5,by=”Ticker”)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Table\_4.merge(Table\_5,on=”Ticker”,how=”outer”) |

Component Table178

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 5 and the expected output is:  **Ticker Name Price** TSLA Tesla, Inc. 840 AMZN Amazon.com, Inc. 3400 WFC Wells Fargo & Company 49 PCG PG\&E Corporation NA F NA 16  |

Notice how both PCG and F appear in the join and gain missing values for the unknown variables. In a full join, the result is exactly the same regardless of which data set is considered the left or right data set, although the ordering may be different.

### **1.4.10 Joins** {#1.4.10-joins}

\[BEGIN LINK \-https://thomasadventure.blog/posts/r-merging-datasets/\]  
To help visualize the process happening in all 4 kinds of joins, there are some interesting graphics at [https://thomasadventure.blog/posts/r-merging-datasets/](#bookmark=id.xze7iuodyhvw). You will note that the code that follows first uses the **merge()** function from base R, then uses the **x\_join()** functions from dplyr (within the tidyverse) that were used on the previous pages. 

To review the output each type of join produces, a left join will have the same number of records as the left data set. A right join will have the same number of records as the right data set. An inner join will have up to the number of records from the smaller data set (and maybe fewer). A full join will have at least as many records as the larger data set (and maybe more). 

These are some reasons why you may wish to use each type of join. 

* Use a left join when the records in the left data set are important and need to be maintained in the join and extra information about other records is not needed.  
* Use a right join when the right data set is important and other records are not needed.  
* Use an inner join when only records with complete information, i.e., data from both the parent and child data set, are needed in the join. This may be useful for predictive models where only complete data can be used.  
* Use a full join if you do not want to throw away any data, even if it is incomplete.

Missing data might already exist in the data and when the keys are identical all 4 types of joins can be done without creating new missing data values, but when the keys have differing values (not just out of order) a left, right, and full join may create missing data. Only an inner join is guaranteed to not create new missing data. There are ways to deal with missing data, as will be discussed in a later section, but this may be an important consideration when deciding which join to use.  
\[END LINK\]  
Joins

### **1.4.11 Keys Using Multiple Variables** {#1.4.11-keys-using-multiple-variables}

Note that for this example, the type of join does not matter.  
Keys Using Multiple Variables

Component Table179

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | inner\_join(Revenue,Employee,by=c(“Year”,”Month”)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Revenue.merge(Employee,on=\[“Year”, “Month”\],how=”outer”) |

Component Table180

| Type | Callout |
| :---- | ----- |
| Content | The code to create the tables and join them is in CHUNK 6 and the expected output is:  **Year  Month Revenue Employees** 2019 March 8400 55 2019 September 9600 56 2020 March 9100 56 2020 September 10300 60  |

Component Table181

| Type | Tabset |
| :---- | ----- |
| Tabs | 2 |
| Tab 1 Title | Revenue |
| Tab 1 Text | Revenue |
| Tab 1 Content |  **Year Month Revenue** 2019 March 8400 2019 September 9600 2020 March 9100 2020 September 10300  |
| Tab 2 Title | Employee |
| Tab 2 Text | Employee |
| Tab 2 Content |  **Year Month Employees** 2019 March 55 2019 September 56 2020 March 56 2020 September 60  |

A key might be a combination of two or more variables. For example, the key in the two data sets on the left is the combination of month and year. Just year or month alone is not enough to distinguish the records to match.

### **1.4.12 Keys With Duplicate Entries** {#1.4.12-keys-with-duplicate-entries}

A primary key is a unique value that completely identifies a record. However, there may be situations where a foreign key has duplicate values. Consider the data sets Patient\_Diet and Diet\_Cost. It may be tempting to consider the variable *Patient* as the key, and in some situations it likely would be. This is an important principle as the key used in a join may depend on the data being joined. If we wish to join the data from these two tables, the variable *Diet* is the key. The table *Diet\_Cost* would then be the parent table with the primary key, as *Diet* is uniquely identified.  
Keys With Duplicate Entries

Component Table182

| Type | Tabset |
| :---- | ----- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | Patient\_Diet |
| Tab 1 Content |  **Patient Diet** A Traditional B Custom C Custom D Traditional  |
| Tab 2 Title | Python |
| Tab 2 Text | Diet\_Cost |
| Tab 2 Content |  **Diet Cost** Traditional 40 Custom 65  |

### **1.4.13 Keys With Duplicate Values** {#1.4.13-keys-with-duplicate-values}

When doing a join with duplicate keys, all instances of the duplicate key are assigned the associated data from the other table. Note that the direction is intentional when using duplicate values to match on a given key. The data with the duplicate values will typically be the left data set in a left join and the information you are adding will be the right data set.  
Keys With Duplicate Values

Component Table183

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | inner\_join(Patient\_Diet, Diet\_Cost, by \=”Diet”)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | Patient\_Diet.merge(Diet\_Cost,on=”Diet”,how=”left”) |

Component Table184

| Type | Callout |
| :---- | ----- |
| Content | The code to create the two tables and join them is in CHUNK 7 and the expected output is: **Patient Diet Cost** A Traditional 40 B Custom 65 C Custom 65 D Traditional 40  |

### **1.4.14 Combining Columns** {#1.4.14-combining-columns}

There may be situations where data does not have a key to facilitate the join. This next example does not have a key but needs to be joined anyway. In some cases, it makes sense to combine data frames side by side. For this to be appropriate, the records in each table need to relate to the same real-world events.  
Combining Columns

Component Table185

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | bind\_cols(Table\_1,Table\_2) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | pd.concat(\[Table\_1,Table\_2\], axis=1) \# axis \= 1 specifies this direction for concatenation |

Component Table186

| Type | Callout |
| :---- | ----- |
| Content | For example, we can combine the two following datasets together, created by running CHUNK 8, to make one larger data set: **Table\_1 Week 1 Week 2** 2 2 3 3 6 7 **Table\_2 Week 3 Week 4** 3 5 3 2 6 5  |

Component Table187

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 8 and the expected output is:  **Week 1 Week 2 Week 3 Week 4** 2 2 3 5 3 3 3 2 6 7 6 5  |

### **1.4.15 Combining Rows** {#1.4.15-combining-rows}

Consider a situation where records come in multiple waves. For example, Table\_3 contains data for records with *ID* values of A through C, whereas Table\_4 contains records with ID values of D through F. In this situation, a join is not appropriate and neither is combining columns. Instead we combine the rows of the first data set with the rows of the second.  
Combining Rows

Component Table188

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | bind\_rows(Table\_3,Table\_4)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | pd.concat(\[Table\_3,Table\_4\], axis=0) \# axis \= 0 specifies this direction for concatenation |

| Table\_3 |  |  |
| :---: | :---: | :---: |
| **ID** | **Week 1** | **Week 2** |
| A | 2 | 2 |
| B | 3 | 3 |
| C | 6 | 7 |

Component Table189

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 9 and the expected output is:  **ID Week 1 Week 2** A 2 2 B 3 3 C 6 7 D 3 5 E 3 2 F 6 5  |

| Table\_4 |  |  |
| :---: | :---: | :---: |
| **ID** | **Week 1** | **Week 2** |
| D | 3 | 5 |
| E | 3 | 2 |
| F | 6 | 5 |

### **1.4.16 Exercise 2.4.1** {#1.4.16-exercise-2.4.1}

Exercise 2.4.1

Component Table190

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 10 to load the data sets. Examine each data set before performing a join to know what variables are present. There is space for code in CHUNK 10 with the solution in CHUNK 11\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/movie\_boxoffice.csv\]  
There are 5 data frames that will be used for this check for understanding. The data have been made up for this exercise. 

* [movie\_boxoffice.csv](#bookmark=id.9cka6582c96) contains box office results in billions of US dollars for popular movies  
* [economy.csv](#bookmark=id.9cpe9rmgb991) contains S\&P 500 information for several years  
* [movie\_details.csv](#bookmark=id.5snjkg9y17dk) provides certain details about selected movies  
* [rotten\_rutabagas.csv](#bookmark=id.ew9ezzsugwnh) provides the Rotten Rutabags score for selected movies  
* [movie\_economy.csv](#bookmark=id.s4apwothg564) contains total box office revenue by year

\[END LINK\]

Component Table191

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  Create a data frame using joins that would facilitate an investigation of the correlation between the U.S. economy and the movie industry economy by joining “economy” and “movie\_economy”. Only include years that have both data present as correlations are only useful when both are included. Create a data frame using joins to facilitate an investigation of the relationship between MPAA rating and Rotten Rutabagas score using “movie\_details” and “rotten\_rutabagas”. Again, this is only useful when both are present. Add the data in “movie\_details” to that in “movie\_boxoffice”. Include all the movies from the box office results but remove any extras from the movie details. Combine the data from “movie\_boxoffice”, “movie\_details”, and “rotten\_rutabagas” into one data frame called “all\_movies”. Include all the movies that show up in any of the original data frames. Add the data from “economy” and “movie\_economy” to each movie in the “all\_movies” data set by matching the year they were released.  |
| Footer | Panel Footer |

## ***1.5 Data Validation*** {#1.5-data-validation}

### **1.5.1 Section 2.5 Learning Objectives** {#1.5.1-section-2.5-learning-objectives}

Data Validation

Component Table192

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.5 Learning Objectives**  Describe how data collection practices and assumptions affect data quality. Evaluate the quality of appropriate data sources for a problem. Validate the data with regard to internal consistency.  |
| Footer | Panel Footer |

### **1.5.2 Introduction**  {#1.5.2-introduction}

Why do we care about data accuracy? Data can have many impacts to an organization, including informing decisions based on financials and results. However, in order to make such decisions, we need to ensure we are using accurate data. Further, we should aim to make ethical decisions based on the data, which is difficult to do if the underlying data is not accurate. Having inaccurate data may mean that we cannot be sure that our analysis, actions, and use are ethical or fair (Hall, Jones, Madigan, & Zheng, n.d.). 

There are several key questions you may ask yourself in using data. Is the data accurate? Can I make appropriate decisions on the basis of the data? Do I have safeguards in place to aid with data fairness, security, and privacy? Thinking through these questions can help determine if the data you have is appropriate for use and accurate in content. 

When data is of poor quality, decisions may not be reflective of risk, leading to undesirable outcomes. For instance, poor decisions could result in negative business outcomes including lower profitability, diminished revenue, less sales, or inappropriate allocation of available resources. Poor data quality can have cascading negative impacts on the ability of organizations to make properly informed decisions.  
Introduction

### **1.5.3 Components of Data Accuracy**  {#1.5.3-components-of-data-accuracy}

For data to be accurate, not only must the value be the correct one, but it must also be represented consistently and unambiguously. For example, let’s assume a person’s birthdate is August 7, 1977 and BIRTH\_DATE is used as an input for a personnel database. In this particular personnel system, the date is expected to be input in the format MM/DD/YYYY. So, if the birthdate is input as 08/07/1977, that would be accurate and understood by the system. An input of 08/08/1977 would be the correct format but is not the accurate date. Conversely, an input of 07/08/1977 would be inaccurate because it represents a different format, DD/MM/YYYY instead of MM/DD/YYYY as expected by the system. Therefore, it is important to eliminate ambiguities in the data. This birthdate example can be considered ambiguous because the reviewer would not know whether the date was invalid or just erroneously represented. In our example using the ISO (International Organization for Standardization) date format of YYYY-MM-DD or being clear about the expected format may reduce ambiguity. 

There are three elements of data accuracy: correct value, consistency, and unambiguity. These elements each impact one’s ability to use the data in further analysis, and if not present they can cause incorrect future conclusions.  
Components of Data Accuracy

### **1.5.4 Common Causes of Inaccuracies**  {#1.5.4-common-causes-of-inaccuracies}

The following are some common causes of data inaccuracy.  
Common Causes of Inaccuracies

Component Table193

| Type | Tabset |
| :---- | :---- |
| Tabs | 4 |
| Tab 1 Title | R |
| Tab 1 Text | Initial data entry |
| Tab 1 Content | Entering incorrect data at the beginning of a project or endeavor is a major source of data inaccuracy. The most common source of inaccuracy is if the person entering the data simply made a mistake or typo. For example, when intending to enter the name *Michael* they entered *Micheal*.  |
| Tab 2 Title | Python |
| Tab 2 Text | System changes |
| Tab 2 Content | Systems changes can cause an array of data problems, such as formatting issues or accidental changes in data meanings. For example, a system could change a “0” to a “-“ in formatting, which could completely change its meaning or interpretation.  |
| Tab 3 Title | Misaligned Data |
| Tab 3 Text | Misaligned Data |
| Tab 3 Content | Misaligned data refers to data used for a different purpose than it was collected.  |
| Tab 4 Title | Null problem |
| Tab 4 Text | Null problem |
| Tab 4 Content | The null problem arises when the information called for is not available. Some data entry forms require a value for all fields, while others allow some fields to be blank. A null problem arises where it is unknown why a field was left blank, and if it was done so intentionally. It could be that the true value is 0, that the field is unknown, that the field is not applicable, or even that the appropriate response for the field was not available to be selected.  |

### **1.5.5 Data Accuracy Example**  {#1.5.5-data-accuracy-example}

You are an actuary for XYZ Insurance and are about to begin work on a new predictive analytics project. As part of this project, you receive some initial information, including a file with policyholder data. You plan to use this data as input into your predictive analytics model, but some of the data looks questionable or inaccurate. An excerpt of the data is shown. 

What are some potential issues you see in the data? Before going to the next page, think about the potential issues you see in the data.  
Data Accuracy Example

| Record | Name | Phone Number | Zip Code | Age |
| ----- | ----- | ----- | ----- | ----- |
| 1 | Anish Singh | 555-266-3985 | 94756 | 35 |
| 2 | Amy Jones | 555-658-9004 | 02847 |  |
| 3 | James Smith | 555-209-8836 | 37543 | 23 |
| 4 | Evan Williams | (555) 936-7355 | 97548 | 172 |
| 5 | Ashley Johnson | 555-7645 | 336C8 | 71 |
| 6 | Jennifer Edwards | 55-630-0296 | 12846 | 43 |
| 8 | Maria Garcia | 555-445-1112 | 67453 | 38 |
| 9 | NULL |  | 88345 | 20 |
| 10 | Chen Lee | 555-221-2315 | 24563 | 62 |
| 11 | Chen Lee | 555-221-2315 | 24563 | 62 |

### **1.5.6 Data Accuracy Review** {#1.5.6-data-accuracy-review}

There are several potential data issues within this excerpt of the data: 

1. For some records, certain fields are missing. For example, there is no age listed for record 2 and no phone number listed for record 9\. We also see “NULL” listed as the name in record 9, indicating there may be an issue with the data input for that field as well.  
2. We notice that the record number jumps from 6 to 8, which indicates that record 7 may be missing entirely. This would need to be investigated further, to see if a complete record failed to be captured within the data.  
3. Records 10 and 11 appear to include identical information across all fields. Duplicate records are something we should be cognizant of, as we do not want to inadvertently double count some records or data.  
4. We see an integrity constraint violation within record 4\. In this instance, the policyholder’s age is clearly incorrect. This would need to be examined further, to see why an unrealistic value is shown for this record in the age field.  
5. Several domain format errors are also seen in this example. For instance, record 4 has the phone number shown using a different format than all other records and record 5 has a phone number with only 7 digits shown instead of 10\. Record 5 also includes a letter (C) within the zip code, which is not appropriate. It may be difficult to use the data with these formatting errors.

Data Accuracy Review

| Record | Name | Phone Number | Zip Code | Age |
| ----- | ----- | ----- | ----- | ----- |
| 1 | Anish Singh | 555-266-3985 | 94756 | 35 |
| 2 | Amy Jones | 555-658-9004 | 02847 |  |
| 3 | James Smith | 555-209-8836 | 37543 | 23 |
| 4 | Evan Williams | (555) 936-7355 | 97548 | 172 |
| 5 | Ashley Johnson | 555-7645 | 336C8 | 71 |
| 6 | Jennifer Edwards | 55-630-0296 | 12846 | 43 |
| 8 | Maria Garcia | 555-445-1112 | 67453 | 38 |
| 9 | NULL |  | 88345 | 20 |
| 10 | Chen Lee | 555-221-2315 | 24563 | 62 |
| 11 | Chen Lee | 555-221-2315 | 24563 | 62 |

### **1.5.7 Detecting Inaccurate Data**  {#1.5.7-detecting-inaccurate-data}

An assessment of data quality can be undertaken to assist in the detection of inaccurate data. This assessment can be completed via a few general activities that we summarize in this section.  
Detecting Inaccurate Data

Component Table194

| Type | Tabset |
| :---- | :---- |
| Tabs | 3 |
| Tab 1 Title | R |
| Tab 1 Text | Data reconciliation and balancing of data |
| Tab 1 Content | Data reconciliation and balancing should be done both prior to aggregation or combination of data tables and after aggregation or combination of data tables (final data). Data reconciliation and balancing may help pinpoint inaccuracies, in catching items such as duplicates or missing records and fields. Duplicate record data inaccuracies discovered after data combination may indicate an unintended joining of the underlying tables. If a balancing exercise does not reconcile, it can imply missing or duplicate data. To directly detect the nature of the issue, a more detailed exploration of the data may be required. |
| Tab 2 Title | Python |
| Tab 2 Text | Manual inspection of the data |
| Tab 2 Content | Manual inspection and high-level summaries may help determine if data inaccuracies are present. Manual inspection can take place through the review of data summaries and data visualizations. A manual inspection can include more than just a visual inspection, through automation, summaries, or functions such as minimums or maximums. A manual review can help identify domain formatting errors, missing values, and other data irregularities. This manual review can take the form of checking values for unreasonable inputs. For numerical fields there is a range of values that could be determined as unreasonable and might require further investigation. For example, a record detailing an insured’s age to be over 120 may indicate an incorrect birthdate entry. Categorical fields should also be manually inspected. Categorical fields can be checked against available data documentation and data dictionaries. Is the same breadth of categorical variable levels available in the dataset as shown in the documentation? If not, additional explorations may be necessary. |
| Tab 3 Title | Algorithmic methods |
| Tab 3 Text | Algorithmic methods |
| Tab 3 Content | Algorithmic methods can also be applied to help identify data inaccuracies. While duplicate records can be determined manually when records are exact duplicates, manual identification becomes more difficult if only certain attributes of the data have been duplicated. Models can be deployed or queries can be created to aid in the detection of duplicate records. For example, probability or scoring models can be used to determine the likelihood a record is a duplicate. |

### **1.5.8 Data Cleaning** {#1.5.8-data-cleaning}

Once data inaccuracies have been detected, it does not mean that the data is no longer useful. We have seen some tools for cleaning data in the data transformation section. For example, the discussion in that section on manipulating strings or converting data types can be useful in cleaning a data set so that specific variables can be used in a predictive model. Also previously discussed was how to remove missing values. Also consider the examples on recoding factor variables that should be consistent but were not. However, even when a data set is tidy and the variables are all as they should be, there could still be several lurking issues that require careful examination of the data. 

Here we provide some additional computational tools for identifying inaccuracies and cleaning a data set when it is found that certain values are inaccurate in the ways discussed. Specifically you will learn how to: 

* Remove duplicate records  
* Remove duplicate variables  
* Check for internal consistency  
* Detect target leakage  
* Identify values do not follow the proper domain of the variable  
* Identify values that do not make sense for the variable

Data Cleaning

### **1.5.9 Duplicate Records** {#1.5.9-duplicate-records}

text  
Duplicate Records

Component Table195

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | unique(directory)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | directory.drop\_duplicates() |

We want to include only the records that are unique and exclude all duplicates.

Component Table196

| Type | Callout |
| :---- | ----- |
| Content | Consider the data set [directory.csv](#bookmark=id.4ssewqcucm3g), which can be loaded using the code in CHUNK 1\. **Name Position Extension Office** Fred Jones Marketing 7110 B15 Dan Stevens Development 7189 B19 Fred Jones Marketing 7110 B15 Tasha Banks Management 7634 C22 Dan Stevens Development 7189 C12  |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_5\_r.rmd\]  
At this time, download the rmd and data files for this section for R or Python ( [atpa\_2\_5\_r.rmd](#bookmark=id.9mzmlwn6lwxn) or [atpa\_2\_5\_python.rmd](#bookmark=id.db565eowj9ra)). 

There may be many reasons duplicate records could exist in a data frame. Human error is an obvious reason. Also, when data is combined from multiple sources, it is very possible that some sources had data for the same individuals. You will want to identify where these observations are and remove the duplicates so that they are not overrepresented.  
\[END LINK\]

Component Table197

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 2 and the expected output is:  **Name Position Extension Office** Fred Jones Marketing 7110 B15 Dan Stevens Development 7189 B19 Tasha Banks Management 7634 C22 Dan Stevens Development 7189 C12  |

### **1.5.10 Duplicate Records** {#1.5.10-duplicate-records}

text  
Duplicate Records

Component Table198

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | directory %\>% filter(\!duplicated(Name)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | directory.drop\_duplicates("Name") |

Component Table199

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 3 and the expected output is:  **Name Position Extension Office** Fred Jones Marketing 7110 B15 Dan Stevens Development 7189 B19 Tasha Banks Management 7634 C22  |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_4\_r.rmd\]  
In this data set, Dan Stevens shows up twice, but the records are not entirely duplicated. Perhaps this is the same individual, and Dan moved offices. You can determine which records might be duplicates based on a specific variable and then subset the rows on that information.  
\[END LINK\]

### **1.5.11 Duplicate Records** {#1.5.11-duplicate-records}

text  
Duplicate Records

Component Table200

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | directory %\>% filter(\!duplicated(Name,fromLast \= TRUE)) |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | directory.drop\_duplicates("Name",keep="last") |

Component Table201

| Type | Callout |
| :---- | ----- |
| Content | The code is in CHUNK 4 and the expected output is: **Name Position Extension Office** Fred Jones Marketing 7110 B15 Tasha Banks Management 7634 C22 Dan Stevens Development 7189 C12  |

This default for the methods used keeps the first instance of the record in the data frame. You can add function arguments to keep the last one instead:  
This might be useful if the later records in the data set are the most recent and therefore will have the most updated information. In the case that the record to keep is not the first or the last, you may want to sort the data in particular ways to make sure the correct record is kept.

### **1.5.12 Duplicate Variables** {#1.5.12-duplicate-variables}

Duplicate Variables

Component Table202

| Type | Tabset |
| :---- | :---- |
| Tabs | 2 |
| Tab 1 Title | R |
| Tab 1 Text | R |
| Tab 1 Content | unique.matrix(var\_data,MARGIN \= 2\)  |
| Tab 2 Title | Python |
| Tab 2 Text | Python |
| Tab 2 Content | var\_data.T.drop\_duplicates().T |

| Var1 | Var2 | Var3 |
| ----- | ----- | ----- |
| 1 | 4 | 1 |
| 2 | 5 | 2 |
| 3 | 6 | 3 |

Component Table203

| Type | Callout |
| :---- | ----- |
| Content | The code to create the above table and exclude the duplicate variable is in CHUNK 5 and the expected output is: **Var1 Var2** 1 4 2 5 3 6  |

It is also possible to have repeated columns in a data frame. Duplicate variables do not need to have the same name, but could otherwise be identical. For example, when performing a join over two data sets where there is a common variable that is not used as the key, that variable will be duplicated. In many cases, duplicate variables can be noticed and dropped individually. You can, however, perform a single action that will exclude all duplicate variables, keeping only the first instance of each unique variable.

### **1.5.13 Internal Consistency** {#1.5.13-internal-consistency}

Internal Consistency  
Besides duplicate variables, it is possible to have variables that will share some of the same information. For example, consider a survey that asks about favorite foods. 

Question 1: Do you like Italian food? 

1. Yes  
2. No  
3. I have never had Italian food

Question 2: Which of the following is your favorite Italian food? 

1. Lasagna  
2. Fettuccine  
3. Spaghetti  
4. I don’t know

Question 3: If you had a choice between these following types of restaurants, which would you choose: 

1. Italian  
2. Mexican  
3. Chinese

### **1.5.14 Internal Consistency** {#1.5.14-internal-consistency}

Internal Consistency  
There is obviously some overlap in how someone would respond to these questions. A few logical results should follow: 

* Everyone who answered c in Question 1 would likely answer d in Question 2  
* Everyone who answered b in Question 1 would likely not answer a in Question 3

When logical rules like this are also seen in the data, this is called internal consistency. For example, suppose the results of the survey were as follows:   
Question 1 

1. 53%  
2. 26%  
3. 21%

We can check these results for internal consistency. We see 21% say they never have had Italian food, and yet 96% were able to pick their favorite. That is not consistent. We also see that 60% answered something other than Italian as their favorite in Question 3, so that would be consistent with the results in Question 1 where 47% either had not had or did not like Italian food.  
Question 2 

1. 22%  
2. 39%  
3. 35%  
4. 4%

Question 3 

1. 40%  
2. 29%  
3. 31%

### **1.5.15 Internal Consistency** {#1.5.15-internal-consistency}

Internal Consistency  
Any time you have variables that have common information you should check for internal consistency. One possible method for this is to use tables, summaries, figures, or correlations. 

* Tables: Just as in the example, you can examine counts or proportions of categorical variables and check if the numbers are consistent.  
* Conditional checks: For categorical variables, conditioning on a certain level and checking the output of a potentially related variable can be used to check consistency. In the example above, conditioning Question 1 on choice c and then viewing the results for Question 2 could be revealing.  
* Summaries: For continuous variables you can check the summary statistics. One example is you have two variables in a data set that measures distance travelled, but one value has a mean of 100 and a standard deviation of 10 and the other has a mean of 160 and a standard deviation of 16\. Upon further examination you determine that one variable is measured in miles while the other is measured in kilometers.  
* Figures: Counts and summaries can also be visualized to better spot discrepancies.  
* Dependence Measure: The measure of dependence between variables or factors that should be related will likely be high. Positive correlations close to 1 or \-1 are suggestive of internal consistency while low absolute correlations are problematic (if correlation was expected).

### **1.5.16 Internal Consistency** {#1.5.16-internal-consistency}

Internal Consistency  
When you conclude that your data does not have internal consistency, you have a few options. You can: 

* Remove all observations and/or variables that are not consistent.  
* Reconcile the values some way, such as in the miles and kilometers example. This could possibly be done using another variable in the data set. For example, perhaps there is a weighting variable that when multiplied by one of the inconsistent columns, the data becomes more internally consistent.  
* Ask for more information from the data source. Perhaps the two variables are not as connected as you might think or something in the sampling procedure happened to cause the lack of internal consistency. This could lead to you throwing out one variable and keeping the other.

### **1.5.17 Target Leakage** {#1.5.17-target-leakage}

Target Leakage  
When preparing data for a supervised model, there will be a specific variable, the **target variable**, that you will be using the other variables to predict. For these models to be useful, there must exist a way to measure the predictor variables and make a prediction prior to the target variable being knowable. In some cases, a predictor variable may be included in a data set that would be impossible to have been present when the target variable was measured. This is called **target leakage**. 

A classic example of this is airbag deployment predicting car crashes. An airbag being deployed nearly perfectly predicts a car crash occurring, but it is impossible to measure that prior to an accident. Variables such as lighting, road conditions, car velocity, and driver characteristics can all be predictive of a car crash because they occur prior to it happening, but airbag deployment being included in a model to predict a car crash would be target leakage. 

Another example is including departure date when trying to predict the length of hospital stay. There is no way to use the departure date to predict length of hospital stay before length of hospital stay is observed. In a model built to predict length of hospital stay, it may be important to designate when the predictive model would be used. For example, if the model is to be used upon check-in to a hospital, only that information available on check-in should be used. If the model is to be used after an initial inspection of a patient, then information available up to that point should be used. 

### **1.5.18 Target Leakage** {#1.5.18-target-leakage}

Target Leakage  
Beyond just data that is not available prior to the time that the target is being measured, target leakage can also happen algorithmically. For example, consider fitting a decision tree to data. On the combined data set, you find an optimal complexity parameter. Then you split the data into train-test-validate groups. Throughout the training and testing process you use the same complexity parameter you found on the whole data set. This is target leakage because you are using data to inform the process used in the training group prior to having access to that data. 

In other cases, it is possible that you test the training and testing group repeatedly and notice a trend in the testing group results and modify the training model based on that trend. This can lead to poor performance in future data and incorrect inference. 

Detecting target leakage requires understanding what each variable is and when it is measured. It can be numerically suspected when a model has extremely good predictive power. Using airbag deployment in a model predicting car crashes will likely be an extremely good model. When values that measure predictive performance, such as MSE, or model diagnostic values, such as R 2, suggest an unrealistic model fit, then it may be important to search the data for target leakage.

### **1.5.19 Value Checking** {#1.5.19-value-checking}

Value Checking  
The last logical check we discuss is value checking. This includes both checking if values match the domain inherent to a certain variable and if the values otherwise make sense. For example, consider this pregnancy data set.

| Days Pregnant | Birth Type | Location |
| ----- | ----- | ----- |
| 275 | Natural | Car |
| 290 | Cesarean | Hospital |
| 420 | Natural | Hospital |
| 282 | Male | Home |

In this data set we see an example of invalid data values of both kinds. A typical pregnancy will last 9 months, or about 280 days. There are frequent cases of pregnancies lasting more and less than this, but 420 is well out of the domain of reasonable pregnancy lengths. Also, *Birth Type* has a value of “Male.” This seems like a misplaced data value. While it may seem unreasonable that the *Location* would be “Car,” that’s not an obvious enough discrepancy to warrant extra suspicion. Having a birth type of “Male” is clearly an invalid value of the variable.

### **1.5.20 Exercise 2.5.1** {#1.5.20-exercise-2.5.1}

Exercise 2.5.1

Component Table204

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Show Answer |
| Content |  The *sched\_dep\_time* variable ranges from 106 to 2359\. This suggests that these are times in the format hhmm. This can be confirmed by observing that no values end with the digits 60-99. Thus, values in the range 500-559 may exist but values in the range 560-599 never will. While it is not coded as a time variable, the structure (and the variable name) suggest it is. (This can be confirmed using an internet search to learn more about the **nycflights13** package.) To remedy this, we can either convert to a time variable or convert to minutes from midnight. |
| Footer | Panel Footer |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/flights.csv\]  
In the [flights.csv](#bookmark=id.8m4y1tbkkmu5) data set from the **nycflights13** package, examine the variable *sched\_dep\_time*. It is read as a numeric variable. Examine the variable to determine exactly what type of variable it should be. What can be done to make that variable more useful in an analysis?   
\[END LINK\]

Component Table205

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 6 provides the data and a summary of the variable. No solution code is needed. However, additional examination of the data may be needed.  |

### **1.5.21 Exercise 2.5.2** {#1.5.21-exercise-2.5.2}

\[BEGIN LINK \-http://opendatacommons.org/licenses/odbl/1.0/\]  
\*This database is made available under the Open Database License: [http://opendatacommons.org/licenses/odbl/1.0/](#bookmark=id.c9f8d9b9aj24).   
It is available at [https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-youth-risk-behavior-surveillance-system](#bookmark=id.3yu8mh2pgtp6)  
\[END LINK\]  
Duplicate Records

Component Table206

| Type | Callout |
| :---- | :---- |
| Content | There is space for code in CHUNK 7 with the solution in CHUNK 8\. |

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/youth\_risk.csv\]  
The Youth Risk Behavior Survey data set\* ( [youth\_risk.csv](#bookmark=id.wab78y5a8t4b)) provides health statistics for youth groups around the U.S. The data is split by state and health category. Within each state and health category, the percentage of youth at risk is reported as data values for the total, but then also various stratifications, including grade, race, and gender (note that while the data set uses "gender" the documentation indicates that the question refers to "sex"). 

Validate the data set based on the criteria we have discussed. Specifically, perform the following tasks: 

1. Check for duplicate columns that repeat the same values or the same information.  
2. Check for duplicate rows.  
3. The percentage values are recorded as the variable *Data\_Value*. Check that all those values are in the proper domain.  
4. Check that the *Data\_Value* falls within the interval of *Low\_Confidence\_Interval* to *High\_Confidence\_Interval*.  
5. The *Data\_Value* for individual strata should be correlated with the *Data\_Value* for the total sample within each state. Find the correlation between the Total Data\_Value and the 11th Grade Strata by state. To do this, filter by *Stratification1* being equal to “Total” and then Grade equal to “11th”. Group by state and find the mean. Plot the relationship by state. Does it seem to be internally consistent?

\[END LINK\]

## ***1.6 Missing and Extreme Values*** {#1.6-missing-and-extreme-values}

### **1.6.1 Section 2.6 Learning Objectives** {#1.6.1-section-2.6-learning-objectives}

Missing and Extreme Values

Component Table207

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.6 Learning Objectives**  Handle missing data (including understanding the types of missing data) by selecting the appropriate action from deletion of the record, imputation, and adding a missing value flag. Check for outliers, both univariate and multivariate.  |
| Footer | Panel Footer |

### **1.6.2 Introduction** {#1.6.2-introduction}

Another step in the process of cleaning data is dealing with records with values that are either missing or extreme. Simply throwing away records with missing or extreme values is an approach that may work in certain situations. Understanding why values are the way they are is important in knowing when this would be appropriate. However, there are more sophisticated ways of dealing with these values. In this section we discuss missing and extreme values, reasons why they are missing or extreme, how that might influence your decision in dealing with them, and then provide tools for handling them.  
Introduction

### **1.6.3 Missing Data** {#1.6.3-missing-data}

While it is easiest to remove entire rows of data where any variables were missing, doing so can be damaging. Perhaps there is a reason why certain values are missing. If that is the case, then removing all the missing values can produce a model with significant bias. 

For example, suppose the target variable is readings from an instrument that measures the amount of a certain substance present in an environment. When the amount of the substance is below a certain threshold, though, the instrument returns an error. In this case, if you remove all instances where the instrument returns an error, you would be removing all data where the amount of the substance was low. When there is a systematic reason why data is missing, you may generate a model that is unable to make effective predictions when those conditions are repeated because it was not trained on those scenarios. 

Another example is an insurance application with a question about occupation. Possible responses might include “don’t know,” “prefer not to answer,” or no answer at all. Assuming everyone has an occupation, all three of these would be considered missing in that the actual occupation is unknown. But including all three of these as legitimate responses may be the right thing to do because future applicants might have these responses as well.  
Missing Data

### **1.6.4 Missing at Random** {#1.6.4-missing-at-random}

When there is no systematic reason that certain values are missing, this is called **missing completely at random (MCAR)**. When values are missing completely at random, it is more justified to remove those values from the data set without negatively affecting a predictive model based on that data. This might happen when a value is not recorded due to an error on the part of the data collection mechanism, such as a person not recording the data correctly. It could have happened to any observation regardless of anything inside the record with the missing data. 

When the reason data is missing has nothing to do with the value of the variable that is missing, but could be related to other aspects of a data set, the data is called **missing at random (MAR)**. In this case, throwing away observations with missing data may cause bias because there may be a reason certain individuals have missing data. Also, in this case there may be ways we can fill in those missing values with good guesses based on the rest of the data. Suppose there is data for Age and Previous Employer, where Previous Employer has some missing data. Someone who is young, may not have a Previous Employer to discuss, so they provide missing data. Then the age variable is somewhat indicative of whether or not Previous Employer is missing, and the data is missing at random. 

When data is missing because of what the values would have been if they were not missing, this is called **missing not at random (MNAR)**. The instrument detection is an example of this. Another example is drug testing. An individual might skip a drug test because they know they could fail, causing a missing data point specifically because of the value it would have been if it were not missing. Often this situation can be filled in as with MAR data, but perhaps there could be some other considerations, such as censoring or truncation. We will not be covering using censoring and truncation to deal with missing data in these modules, but these are a potential solution when data is MNAR.  
Missing at Random

### **1.6.5 Missing at Random** {#1.6.5-missing-at-random}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_6\_r.rmd\]  
If data is MCAR, then removing missing data will not introduce bias. Therefore, it is important to be sure it is MCAR before removal. To do this you can look at plots of other variables split by whether or not the data has missing values. At this time, download the rmd files for this section ( [atpa\_2\_6\_r.rmd](#bookmark=id.80shf0f8hu37) and [atpa\_2\_6\_python.rmd](#bookmark=id.ps20dfxwzivt)) and the flights data ( [flights.csv](#bookmark=id.usjt2oe1pil9)). (If using R the file is not needed, the data is available from the **nycflights13** package.) 

For example, the flights data set has several missing values for the variable *dep\_time*. We can look at the data for a different variable to see how it compares when *dep\_time* is missing or not. In this case we will look at *sched\_dep\_time*. There is no code provided that generates these graphs. 

Intuitively, we are looking at a flight's scheduled departure time when the actual departure time is missing and comparing it to when departure time is not missing. If the data is MCAR, the plots should look similar. In this example there is some difference between the two distributions. Missing data seems more likely to occur in the later hours. 

However, the plots do look somewhat similar. There is a way to more formally test the nature of the missingness.  
\[END LINK\]  
Missing at Random

### **1.6.6 Permutation Test** {#1.6.6-permutation-test}

A permutation test is useful in applications where we are testing ordering or correlations. The process randomly reorders a variable to generate some statistic. You then repeat that process many times to generate a distribution of possible statistics. When you compare this distribution to your actual data, you will be able to see if order does matter. 

Let Variable *A* be a variable with missing data and Variable *B* have no missing data. A permutation test is conducted according to the following steps. 

1. Set the null hypothesis to be the data is MCAR and the alternative is that the data is not MCAR.  
2. Create a test statistic for the observed data, *T* \= *BM* – *BNM* where *BM* is the mean of Variable *B* when Variable *A* is missing and *BNM* is the mean of Variable *B* when Variable *A* is not missing.  
3. Randomly reorder either Variable *A* or Variable *B*.  
4. Calculate *Ri* \= *BM* – *BNM* on the reordered data set, where *Ri* is similar to *T*, but is calculated on the *i*\-th sampled permutation.  
5. Repeat steps 3 and 4 a large number of times (perhaps 10,000).  
6. Obtain a 95% empirical confidence interval based on the 2.5th and 97.5th percentiles of the values.  
7. If *T* falls outside the confidence interval, reject the null hypothesis and conclude that the values are not MCAR. If *T* falls inside the interval, there is not sufficient evidence to conclude that the missing values are not MCAR.

Permutation Test

### **1.6.7 Permutation Test** {#1.6.7-permutation-test}

The statistic for this permutation is 4 – (2 \+ 10)/2 \= –2. 

For this simple example there are four other permutations. The *R* values for them are –5, –5, –2, and 7\.  
Permutation Test

| A | B |
| ----- | ----- |
| 1 | 2 |
| 2 | 4 |
| NA | 10 |

The baseline is *T* \= 10 – (2 \+ 4)/2 \= 7 where 10 is the average of the one value of *B* where *A* is missing and 3 is the average of the two values of *B* where *A* is not missing. 

Permutations will be done on *A* and one such permutation is given in the second table.

| A | B |
| ----- | ----- |
| 1 | 2 |
| NA | 4 |
| 2 | 10 |

The following very small example illustrates the process. Consider three observations of *A* and *B*:

### **1.6.8 Permutation Test** {#1.6.8-permutation-test}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_6\_r.rmd\]  
For the flights data set, the variable *dep\_time* represents the time as an integer. As discussed in the data validation section, this will not be helpful as is. For this illustration, *dep\_time* is converted to minutes from midnight.  
\[END LINK\]

Component Table208

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 1 to load and prepare the data. Then run CHUNK 2 to perform the permutation test. |

Permutation Test  
The test statistic is *T* \= 90.8, meaning the difference between the mean scheduled departure time when departure time is missing and mean scheduled departure time when departure time is not missing is 90.8. 

At the random seed provided, the distribution of the sampled values when reordering the variables has a 95% confidence interval near –6 to 6 (your results will depend on which program you are using). This means that if the ordering was really not important, the difference between the two groups would normally be between about –6 and 6\. Because *T* is not in the confidence interval, reject the null hypothesis and conclude that the missing values are not MCAR. 

In fact, the missing values are for cancelled flights, which are much more likely to happen at the end of the day than at the beginning of the day.

### **1.6.9 Permutation Test Shortcut** {#1.6.9-permutation-test-shortcut}

The permutation test as described previously may take a lot of time, particularly for large data sets. However, there is a shortcut available that gives an approximate answer that takes very little time or resources. The shortcut assumes that the permutations are done on the variable that has no missing observations (Variable *B*). Suppose we did every permutation (rather than a random sample of possible permutations). Then it can be shown that for the collection of *R* statistics, the mean is zero and the variance is given by the following formula, where *v* is the sample variance of the observations of Variable *B*, *n* is the total sample size, and *m* is the number of missing observations in Variable *A*.   
![][image2]   
Then, assuming the *R* values have an approximate normal distribution, the hypothesis of MCAR is rejected if the absolute value of the observed *T* statistic is greater than 1.96 times the square root of the variance as calculated here.  
Permutation Test Shortcut

Component Table209

| Type | Callout |
| :---- | :---- |
| Content | Run CHUNK 2A to use this approach on the example. |

### **1.6.10 Imputation** {#1.6.10-imputation}

When the data is not MCAR, it may be possible to fill in missing values with justifiable values. This is called **imputation**. While imputation may introduce additional sources of bias, it will often still be a better alternative than throwing out entire rows of data with any missing values. Imputation works best when there are many rows of data, as we will, in some cases, be using those other rows to help find the imputed values. 

We will look at the following imputation techniques: 

* Mean / Median  
* Regression  
* K Nearest Neighbors  
* Classification and Regression Trees

Imputation

### **1.6.11 Mean Imputation** {#1.6.11-mean-imputation}

The most basic form of imputation for numeric variables is to replace all missing values with the mean of the non-missing values of the same variable.  
Mean Imputation

Component Table210

| Type | Callout |
| :---- | :---- |
| Content | For example, consider the production data set, which is created by running CHUNK 3\.  |

| Produced | Employees | Available\_Machines | Hours\_Open |
| ----- | ----- | ----- | ----- |
| 145 | 6 | 19 | 10 |
| 212 | 8 | 24 | 8 |
| 137 | 6 | NA | 8 |
| 187 | 7 | 20 | 9 |
| 166 | 7 | 18 | 6 |

We have the total number of products produced in a work day, which will be explained by the number of employees, the number of available machines, and the number of hours open.

### **1.6.12 Mean Imputation** {#1.6.12-mean-imputation}

If we were to impute the mean for the missing value, we would simply find the mean of the values for *Available\_Machines* that are non-missing, which in this case is 20.25.  
Mean Imputation

Component Table211

| Type | Callout |
| :---- | :---- |
| Content | The code to perform this is in CHUNK 4 and the expected output is in the table. |

| Produced | Employees | Available\_Machines | Hours\_Open |
| ----- | ----- | ----- | ----- |
| 145 | 6 | 19 | 10 |
| 212 | 8 | 24 | 8 |
| 137 | 6 | **20.25** | 8 |
| 187 | 7 | 20 | 9 |
| 166 | 7 | 18 | 6 |

One issue with imputation is that imputed values for integer values are not guaranteed to return an integer. For consistency of interpretable data, you could round the values to the nearest integer. However, for a predictive model, using imputed values that are non-integer will be fine. This issue will be seen again in other imputation methods.  
While a mean imputation is the simplest and fastest way to impute data, it does not add any information for the value being imputed. In fact, mean imputation assumes the data is MCAR, which means it can essentially be ignored. However, it is still useful as an alternative to throwing away the record because of the other variables that now get to be included in the data set. 

In some cases, if the variable is highly skewed it makes more sense to impute the median instead of the mean.

### **1.6.13 Regression Imputation** {#1.6.13-regression-imputation}

When the data is missing at random, there may be a significant amount of information in the other variables of the model to help us determine what the missing values may be. A simple way to do this is using regression imputation. This builds a regression model for a feature with missing data using only the complete rows. Then the missing data will be predicted and the predicted value will be imputed. 

In the production example we would take the following steps: 

1. Use only rows 1, 2, 4, and 5 to build a regression model to predict *Available\_Machines* using *Employees* and *Hours\_Open*.  
2. Using the values for the predictors in row 3, use the model to predict Available\_Machines.  
3. Impute the predicted value into the data set.

Note that if the model is being built to predict a target variable in the data set, that target variable should not be used for the imputation algorithm.  
Regression Imputation

Component Table212

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 5 performs imputation using built in functions and the expected output is: |

| Produced | Employees | Available\_Machines | Hours\_Open |
| ----- | ----- | ----- | ----- |
| 145 | 6 | 19 | 10 |
| 212 | 8 | 24 | 8 |
| 137 | 6 | **16.80882** | 8 |
| 187 | 7 | 20 | 9 |
| 166 | 7 | 18 | 6 |

Regression imputation is more appropriate for MAR data than mean imputation because there is information in the other variables that relates to the missing data point. While not seen in this example, another advantage is that while mean imputation would impute the same value for all missing data points in a variable, regression imputation returns different values for each. This may be important for a predictive model such as a decision tree where many values fixed at a single point, as would be the case for mean imputation, could cause clusters in the nodes that will artificially affect the model.

### **1.6.14 Regression Imputation** {#1.6.14-regression-imputation}

Regression imputation as done in CHUNK 5 has one drawback. Using deterministic predictions can lead to overfitting with regard to the interrelationships among the predictor variables. These predictions assume the fitted linear model is the true relationship between the variables and that there is no error in that relationship. The mice package includes three alternative approaches: 

* Add a random adjustment to each imputation based on the standard error from the regression model. Use **method \= "norm.nob"** to do this.  
* Use Bayesian estimation to incorporate both sources of variability. Use **method \= "norm"** to do this.  
* Use the bootstrap to incorporate both sources of variability. Use **method \= "norm.boot"** to do this.

All of these methods employ random numbers and hence a seed should be set if results should be reproducible. For this course, if regression imputation is used, it will be sufficient to use the version without incorporating randomness.  
Regression Imputation

### **1.6.15 KNN Imputation** {#1.6.15-knn-imputation}

Another approach to using the data to help predict missing values is using K-Nearest-Neighbors (KNN). Essentially this approach defines a distance metric and determines the nearest K observations with non-missing data. Then the imputed value is the average of the values for those K observations. As with regression, this is better than imputing a mean or median. Compared to regression imputation, this may be easier to explain and a bit simpler for a non-technical audience but produces similar results. KNN imputation is typically slower for larger data sets.  
KNN Imputation

### **1.6.16 KNN Imputation** {#1.6.16-knn-imputation}

Again, there are functions and packages that help with the imputation.   
KNN Imputation

Component Table213

| Type | Callout |
| :---- | :---- |
| Content | The code is provided in CHUNK 6 and the expected output is shown on the right. |

| Produced | Employees | Available\_Machines | Hours\_Open |
| ----- | ----- | ----- | ----- |
| 145 | 6 | 19 | 10 |
| 212 | 8 | 24 | 8 |
| 137 | 6 | **19.5** | 8 |
| 187 | 7 | 20 | 9 |
| 166 | 7 | 18 | 6 |

In this example, we picked K \= 2 neighbors. The algorithm selected observations 1 and 4 as nearest to observation 3, and so it returned the average *Available\_Machines* value for those neighbors. Note that in practice, your data set will be larger than this, so 5 or 10 neighbors is more typical. 

Both regression imputation and KNN imputation can be used when there are multiple variables that have missing data. The approach is to use an iterative imputation, where one variable is imputed while the others are treated as known and then they swap, essentially always imputing one value while treating the other as known. This process goes back and forth as many steps as you want. This process is built into the functions in both R and Python.

### **1.6.17 Categorical Imputation** {#1.6.17-categorical-imputation}

The methods presented so far require numeric data. When they are categorical, the approach will be different. For example, instead of imputing a mean, the mode can be imputed for a quick and simple approach. 

If the variable with missing values is binary, a logistic regression function could be used instead of a linear regression function. When there are 3 or more categories, a categorical regression model can be built. These are outside the scope of this module. 

For KNN imputation of a categorical variable, the algorithm will determine which rows are considered to be neighbors, and then instead of taking an average of its neighbors, it will find the mode of the nearest neighbor variables. 

Consider the modified production data set. The *Manager* variable must be imputed using categorical imputation methods.  
Categorical Imputation

| Produced | Employees | Available\_ Machines | Hours\_Open | Manager |
| ----- | ----- | ----- | ----- | ----- |
| 145 | 6 | 19 | 10 | On |
| 212 | 8 | 24 | 8 | Off |
| 137 | 6 | *NA* | 8 | On |
| 187 | 7 | 20 | 9 | Off |
| 166 | 7 | 18 | 6 | *NA* |

### **1.6.18 Categorical Imputation R** {#1.6.18-categorical-imputation-r}

Categorical variables have different strategies in R and Python and so we will describe these approaches separately. 

The **mice** package in R has several useful imputation methods.  
Categorical Imputation R

Component Table214

| Type | Callout |
| :---- | :---- |
| Content | CHUNKs 4 and 5 show the mice package with mean and regression imputation. |

\[BEGIN LINK \-https://cran.r-project.org/web/packages/mice/mice.pdf\]  
It does not perform KNN imputation. To do categorical imputation with the **mice** package, use **method \= "cart"**, where cart stands for classification and regression trees. This method uses decision trees to impute data in the same way that regression does, separating rows of complete from rows of missing data, using complete rows to train a model for the missing variables, and then predicting the missing values. Again, this should be done without using the target variable that the data will eventually be predicting. As implemented in the **mice** package, the imputation is not the average value at the node but rather a random selection from the observations at the node. This adds variability and also ensures that the imputed value is one that could be observed. 

One useful thing about the cart method for imputation is that it works for both continuous and categorical variables. For this reason, using this method is useful to know and to be able to explain as it applies to all types of variables. For more information on the different options for the mice package, see pages 72 through 79 in [https://cran.r-project.org/web/packages/mice/mice.pdf](#bookmark=id.dzhixh83le6e). For the cart method in particular, see pages 93 and 94 of the same document.  
\[END LINK\]

Component Table215

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 7 provides code for extending the production data set to include a categorical variable with a missing value and then imputing the missing value using the **mice** package and the cart method. |

### **1.6.19 Categorical Imputation Python** {#1.6.19-categorical-imputation-python}

If the only missing values were categorical, then using **strategy \= "categorical"** imputes the missing data by randomly drawing from the complete data of that variable, meaning if 50% of complete values were “A”, 30% were “B”, and 20% were “C”, then that would create a distribution for the missing values. While this is not optimal as it does not use the other variables in the data set, it is the only option that is available when there are 3 or more categories in a variable. 

For binary variables, using **method \= "binary logistic"** will fit a logistic regression model for the missing values. The binary variables will need to be converted into 0s and 1s. Suppose there are multiple data types with missing values. Then the strategy argument should be a dictionary defining the method to use for each variable. For example, in the modified production data set, if you wanted to use regression for the *Available\_Machines* variable and logistic regression for the *Manager* variable, you would use **strategy={"Available\_Machines":"least squares","Manager\_On":"binary logistic"}**, where *Manager\_On* is a variable that is 1 when *Manager* \= “On” and 0 otherwise. In this way you can define exactly what method to use on each variable type. While you can use different methods that work best for the situation, when there are mixed data types with missing data, one suggestion would be to use regression for continuous variables, logistic regression for binary variables, and categorical for factors with 3 or more levels.   
Categorical Imputation \- Python

Component Table216

| Type | Callout |
| :---- | :---- |
| Content | The impute function used in CHUNKs 4 and 5 from the **autoimpute** package can also be used for categorical variables. |

Component Table217

| Type | Callout |
| :---- | :---- |
| Content | This approach is shown in CHUNK 7\. More information and several examples for the autoimpute function in Python can be found at [https://kearnz.github.io/autoimpute-tutorials](#bookmark=id.4kbtw2n67qsa) |

### **1.6.20 Missing Target Variable Observations** {#1.6.20-missing-target-variable-observations}

The goal of a predictive model is to use predictor variables to predict a target variable. When certain predictors are missing, we have seen several methods to impute the data. In many cases this is a superior alternative to throwing away an entire record, especially in cases where there are many variables. Suppose a record has 20 variables, only 1 of which is missing. There is a lot of information potentially being thrown out when the record is removed. Thus, imputation can be extremely useful in this case. 

Suppose that the target variable is missing for a record. Then imputation essentially becomes model prediction. Consider the regression imputation approach. In this approach, you use only complete records, build a model, and then predict the missing values. This is no different than just building the desired model on the complete records. Training a model should be done using only records with target variables.   
Missing Target Variable Observations

### **1.6.21 Missing Target Variable Observations** {#1.6.21-missing-target-variable-observations}

It is still concerning removing entire records, especially when the target variable is not missing completely at random. Since imputation is not an option, the only action you can take when you encounter a non-MCAR target variable would be to investigate the cause of its missingness. For example, suppose you are building a model to predict daily sales, and some days have missing values. Upon investigation you discover that the credit system was down on the days with missing values and sales were cash-only. This may have affected other variables in the data set, causing missingness of daily sales to be not missing completely at random. You have two options at that point. Perhaps you still throw out those data points because you only wish to use the model to predict sales on days with the credit system working. Or perhaps you still wish to include those days, in which case you may have other sources for the missing data. Imputation is not a valid option. 

Your decision path regarding a missing target variable is as follows: 

1. If the target is missing completely at random, you can throw out the data points, do not impute.  
2. If the target is not missing completely at random, investigate the cause of the missingness.   
   1. If the cause is determined to be an important case that needs to be accounted for in the predictive model, find the observation or a suitable substitute.  
   2. If the cause of the missingness is determined to be a case that does not need to be accounted for in the predictive model, the record can be thrown out.  
   3. If the missingness cause cannot be found, it is still better to throw out the records than to impute.

Missing Target Variable Observations

### **1.6.22 Exercise 2.6.1** {#1.6.22-exercise-2.6.1}

1. Examine the *normalized\_losses* variable for missingness at random. Create figures to investigate the relationship between missingness in *normalized\_losses* and the variables *curb\_weight* and *city\_mpg*.  
2. Perform a permutation test for the *normalized\_losses* variable using *curb\_weight* as the variable without missing data. What conclusion can you make about the missingness of *normalized\_losses*?

   Note that *normalized\_losses* is the target variable. When a target variable is not missing completely at random, you would not impute values for that variable, but it may be a signal to go back to the source of the data and determine why the missing values occurred.  
3. Notice the relationship between the missing data points in the *bore* variable with respect to the variable *engine\_type*. Insight may come from looking at the records where *bore* is missing. What implications might that have for imputation? Remove the records where *bore* is missing.  
4. Perform mean imputation for the missing values of *price*.  
5. Perform regression imputation for the missing values of *price*. Recall that *normalized\_losses* is the target and should not be included in the data set that generates this imputation.  
6. Perform multiple imputation for both the *num\_doors* and *price* variable. In R this could mean using cart to impute both. In Python this could mean using least squares for *price* and logistic regression for *num\_doors*.

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/automobile.csv\]  
Look at the [automobile.csv](#bookmark=id.h64pkixv3m6j) data set. In Section 3 we did some cleaning by recoding missing values and removing them. Now we will try and impute them. Specifically, perform the following tasks. Only certain variables in the data are used in this exercise.  
\[END LINK\]  
Exercise 2.6.1

Component Table218

| Type | Callout |
| :---- | :---- |
| Content | CHUNK 8 loads and prepares the data and provides space to perform these tasks. Solutions are shown in CHUNKs 9A-9F.  |

### **1.6.23 Identifying Outliers** {#1.6.23-identifying-outliers}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/hotel\_bookings.csv\]  
In addition to missing values, outliers, that is, extreme values, represent another issue that requires investigation and possible action. These outliers may be harmless and could possibly even be appropriate if they represent an important category of the population being modeled. However, these values could be even more dangerous than if they were missing, because fitting a model with records that have extreme values that are not representative of the population could lead to bias in the model fit and less accuracy in the predictions of all other records. 

Consider the hotel booking data set ( [hotel\_bookings.csv](#bookmark=id.25k952vnfavx)). There are several variables in this data set that have potential outliers. Consider the variable, *stay\_in\_week\_nights*. This variable measures the number of weeknights a customer has scheduled to stay in a hotel. We can plot this variable in a histogram or boxplot to see potential outliers.  
\[END LINK\]  
Identifying Outliers

Component Table219

| Type | Callout |
| :---- | :---- |
| Content | Run the code in CHUNK 10 to read in the data and produce the plots. |

### **1.6.24 Identifying Outliers** {#1.6.24-identifying-outliers}

Both plots are effective in showing that there are some potential outliers, in this case in the right tail. It is more difficult to tell exactly which observations should be considered outliers. There are several methods of determining if a value is far enough away from the bulk of the data to constitute an outlier. The simplest is to use a *z*\-score on the data calculated by subtracting the mean and dividing by the standard deviation of the data. If the population is truly normally distributed, absolute values greater than 3 should be rare. The formula is   
![][image3]  
where *x̄* is the sample mean and *s* x is the sample standard deviation. 

This can be tricky because data sets with outliers are hardly ever normal. However, *z*\-scores can still be useful for understanding how far an outlier is in the context of the data. 

While the formula here is written using all the data, it may be more appropriate to remove the observation being tested when calculating the mean and standard deviation for the z-score. This process requires removing a single observation, calculating the mean and standard deviation of the remaining observations, and finding the z-score of the removed value. This is also called a Leave One Out or LOO *z*\-score. In smaller data sets, this method may be more accurate for detecting outliers.  
Identifying Outliers

### **1.6.25 Identifying Outliers** {#1.6.25-identifying-outliers}

The *z*\-scores for the variable *stay\_in\_week\_night* range from \-1.3 to 24.9. Examine the code chunk that plots the histogram for the *stay\_in\_week\_night* variable with data points eliminated when *z*\-scores are greater than a specified value.

Component Table220

| Type | Callout |
| :---- | :---- |
| Content | Run the code in CHUNK 11 using cutoffs of 3, 5, and 10\. Note that this removes 1.40%, 0.25%, and 0.03% of the data, respectively. The figures are helpful to visualize the effect of these cutoffs. They may indicate visually when outliers are no longer present. |

Identifying Outliers

### **1.6.26 Outlier Handling** {#1.6.26-outlier-handling}

When there is an outlier in a specific variable, there are a few remedies. 

1. **Transform:** Taking the log or square root of a variable will often reduce the extremity of the outlier and minimize their impact while modeling. When zeroes are present, the log of (data \+ 1\) could be used.  
2. **Remove:** If an outlier is deemed to be too extreme, its observation could be removed. This can be most appropriate if it is suspected the outlier is due to a recording or other human error.  
3. **Censoring:** It is possible that all that is needed to know for that particular variable is that the value is large. Providing a censored value, perhaps at a z-score of 3 or \-3, could still give the same information without a single observation impacting the results as much.  
4. **Replace with percentiles:** Again, maybe specific values aren’t as important as just knowing which observations have a higher value than another. This method transforms the full variable to a quantile of the data. The data would then be spread evenly between 0 and 1\.  
5. Ignore the outliers and include their observations in the model.

Outlier Handling

Component Table221

| Type | Callout |
| :---- | :---- |
| Content | Methods 1 through 4 are shown in CHUNKS 12 through 15, respectively. |

### **1.6.27 Outlier Handling** {#1.6.27-outlier-handling}

Which of these is most helpful depends on the situation. An important consideration is whether the variable is the target variable or a predictor variable. It would be more appropriate to change a predictor variable into a percentile than the target variable. However, it is common to take the log of the target variable. In fact, methods 3 and 4, truncated and percentile transformations, are not appropriate for transforming the target variable and should only be used for predictor variables. 

How you handle outliers also depends on how extreme the outliers are. Mild outliers may not merit any action at all whereas extreme outliers might. There is a possibility that the value is extreme but not an outlier and removing it could also remove useful information. The goal is to build a predictive model. Ideally, the data used to fit the model is representative of the data being used to predict in the future, meaning if these extreme values are important to be able to predict, then they are important observations to keep in the model. In this case consider using a transformation to decrease the effect of the extremity of the values, as this may help the model fit better for non-outlier values. However, if the outliers are not representative of the type of data you would like to predict with the model, perhaps they could be removed. The number of points that are determined to be outliers is important. If there are many outliers, it is possible that they are representative of a group that is important not to exclude or change. A few widely separated outliers would be more appropriate to leave out.  
Outlier Handling

### **1.6.28 DBSCAN** {#1.6.28-dbscan}

\[BEGIN LINK \-https://www.analyticsvidhya.com/blog/2021/06/understand-the-dbscan-clustering-algorithm/\]  
While looking at *z*\-scores for a specific variable is useful, it also seems that, unless that variable is particularly important, throwing out or changing an entire record based on a value of a single variable may be extreme. A method called Density Based Spatial Clustering of Applications with Noise (DBSCAN) can determine outliers based on several variables. DBSCAN is a clustering algorithm that will discriminate between points that clearly fit within clusters of certain sizes and points that do not fit in any clusters. 

There are two main settings in a DBSCAN: 

* The distance at which two points are considered neighboring, called ε (eps when coding)  
* The minimum number of neighbors to be considered a cluster (minPts when coding)

The DBSCAN algorithm starts by identifying a core point randomly. If there are a minimum number of points within epsilon of the randomly chosen point, it forms a cluster. If not, it is considered “noise” which, when identifying outliers, can be interpreted as an outlier. All points within epsilon of the core point are included in that cluster. One way to interpret the results of this algorithm is that it will identify all points as outliers where you cannot find the minimum number of points within epsilon. More specific information and examples can be found at [https://www.analyticsvidhya.com/blog/2021/06/understand-the-dbscan-clustering-algorithm/](#bookmark=id.mk0ooi6871t4) 

This approach will only work on two or more continuous variables. A strategy may be to subset the data to only continuous predictor variables and use those in the DBSCAN algorithm to detect outliers as combinations of these continuous variables. 

\[END LINK\]  
DBSCAN

### **1.6.29 DBSCAN** {#1.6.29-dbscan}

Consider again the hotel booking data set. The results of using a DBSCAN on the three variables *stay\_in\_weekend\_night*s, *stay\_in\_week\_nights*, and *adults* depend on ε and the minimum number of points in a cluster. The number of outliers is highly dependent on these two values.  
DBSCAN

Component Table222

| Type | Callout |
| :---- | :---- |
| Content | Using the code in CHUNK 16, try several different values for ε ranging from 1 to 5 and minPts ranging from 4 to 50\. |

Notice that the number of outliers detected decreases as ε increases and will increase as minPts increases. With the values initially used in the CHUNK (3 and 10), 18 outliers were identified. It appears that five have a large number of week nights and weekend nights while 13 have a large number of adults. 

Broadly speaking, the minimum number of points in a cluster should be somewhere near twice the number of variables being used, although it can be larger for larger data sets. The parameter ε can then be chosen based on how strict you desire your outlier detection. For example, if you are very worried about how the outliers might affect the model, then perhaps choose epsilon to be small, which will detect more outliers. If you are not worried as much about outliers, choose epsilon to be large.

## ***1.7 Case Studies*** {#1.7-case-studies}

### **1.7.1 Section 2.7 Learning Objective** {#1.7.1-section-2.7-learning-objective}

Case Studies

Component Table223

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | **Module 4 Learning Objectives** |
| Content |  **Section 2.7 Learning Objective**  Apply the information from this module to realistic examples.  |
| Footer | Panel Footer |

### **1.7.2 Introduction** {#1.7.2-introduction}

\[BEGIN LINK \-https://www.analyticsvidhya.com/blog/2021/06/understand-the-dbscan-clustering-algorithm/\]  
This section contains two case studies that combine several of the elements of this module into a single problem. The goal of each case study is written in its problem definition, but generally the purpose is to create data sets that are ready to use in a predictive model. 

At this time, download a zip file that contains the data sets for both case studies ( [2.7\_case\_studies.zip](#bookmark=id.xwehzpwnktr0)).   
\[END LINK\]  
Introduction

### **1.7.3 Case Study 1.1: Website Visit Duration** {#1.7.3-case-study-1.1:-website-visit-duration}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_cs11.pdf\]  
ABC corporation has built a website that collects articles on predictive modeling topics. The site has been active for one year and now ABC is trying to determine how certain aspects of their website affect web traffic. Specifically, ABC would like to build a predictive model that predicts how long a first-time visitor will stay when they visit the website. 

At this time, download a PDF with details about the situation and questions for you to answer ( [atpa\_2\_7\_cs11.pdf](#bookmark=id.tas9bmo2xrmm)). After you have completed your work, go to the next page to see a possible solution.  
\[END LINK\]  
Case Study 1.1: Website Visit Duration

### **1.7.4 Case Study 1.1: Solution** {#1.7.4-case-study-1.1:-solution}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_r.rmd\]  
A possible solution to preparing the data set is given in the R and Python Rmd files for this case study ( [atpa\_2\_7\_1\_r.rmd](#bookmark=id.9lm19r4c08cp) or [atpa\_2\_7\_1\_python.rmd](#bookmark=id.hnplqnsyhk9z)). There are likely many ways to do the various tasks. Possible answers to the specific questions are: 

1. If we are determining how to handle records that have outlying variables, it is useful to know that those outliers are unlikely to be repeated. Outlying values that are likely to be repeated may be important to keep in the model. In this case, these values are likely to not be repeated and so it is okay to modify or remove them.  
2. If we are building a predictive model to determine how the website configuration affects visit duration, the data point of how many visitors the site had on a specific day would not be available for the model to use. This is an example of target leakage. Only variables that can feasibly be used to predict should be used in a predictive model.  
3. There are no decisions being made by this model that will benefit the individuals who visit the site in different ways. This is not affecting wages or program acceptance. This is to determine a marketing strategy via website design. Depending on what the website owner’s goal is, it actually may be helpful to build a model that will specifically target a specific demographic. For example, maybe they specifically want to encourage women in predictive modeling. Then trying to determine what increases site visit duration for women may be reasonable.

\[END LINK\]  
Case Study 1.1: Solution

### **1.7.5 Case Study 1.2** {#1.7.5-case-study-1.2}

Communication is an important part of ATPA. There is an entire section devoted to communication later in these modules. The communication section will discuss items such as when to explain more versus explain less. Part of this process is justifying decisions, both from a modeling perspective, but also from a data manipulation perspective. Give some thought to how you might communicate the work you did to prepare the data. 

A possible example of this report is available on the next page. This is not intended to be a full data exploration with summaries and figures of each variable.  
Case Study 1.2

### **1.7.6 Case Study 1.2: Report** {#1.7.6-case-study-1.2:-report}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_cs12.pdf\]  
A sample report is available for download ( [atpa\_2\_7\_cs12.pdf](#bookmark=id.i58fgeqd2e9q)).  
\[END LINK\]  
Case Study 1.2: Report

### **1.7.7 Case Study 2.1: Chiropractic Visits** {#1.7.7-case-study-2.1:-chiropractic-visits}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/questionnaire.csv\]  
New Start Chiropractic (NSC) is trying to build a predictive model to predict how many visits a patient will have in a given year, using data from the individual's past visits as well as a questionnaire given to every new patient. The new patient data is in questionnaire.csv and contains information such as an individual’s age, sex, reason for coming, and some other medical information. The data on past visits was entered into a web application and is currently available in the file visits.xml, both of which are in the zip file downloaded at the beginning of this section. The historical visits data is all visits from 2015 to 2018 and includes information about the type of visit, how the visit was paid for, and if the individual rescheduled. 

The goal is to use past data to predict future visits, so the data in visits.xml will need to be manipulated to find both the target variable and the predictors. The target variable NSC wants to use is the number of visits an individual had in 2018\. NSC wants to use the information from both the questionnaire and the historical visit data as the predictors. They specifically wonder if the number of all visits prior to 2018 could be used as a predictor variable. The purpose of the model is both to understand what factors might influence an individual to come more often in a given year as well as to build a model to predict the number of visits an individual might have in future years. 

Write down the issues you find when you consider creating data for a predictive model according to the data files and the information provided. A possible solution is provided on the next page. Do not do any coding other than to examine the two data sets.  
\[END LINK\]  
Case Study 2.1: Chiropractic Visits

### **1.7.8 Case Study 2.1: Solution** {#1.7.8-case-study-2.1:-solution}

Here are a few possible issues to consider: 

1. The data in visits.xml contains records for each visit from any individual, not the number of times they visit in a year, but each visit is coded with the patient’s ID, which is also found in the questionnaire data. The data needs to be aggregated to provide the target variable, which is the number of visits in 2018\.  
2. The other variables in visits.xml can be used as well, but not in their current form. Perhaps using values such as the percent of visits that were normal versus extended, or the percentage of times an individual rescheduled could be used.  
3. There is a variable *year* in both data sets. In visits.xml, *year* records the year of the visit. In questionnaire.csv *year* records when the questionnaire was filled out. These variables need to be validated to make sure they are internally consistent.  
4. NSC wants to use the total number of all visits prior to 2018 as a predictor. We need to figure out if that makes sense for a predictive model or if there is a better variable to create using the past data.  
5. The questionnaire data is not complete. There are certain individuals who did not answer whether or not they have had surgery.  
6. The variable *why\_visit* has 15 different categories, but they are all some combination of 4 specific causes. Is there a way to split this variable into something with fewer levels?  
7. The variable *how\_heard* contains information about how the individual heard about NSC. There are a few significant levels of this variable but then some levels that do not occur often in the data. Can the number of levels be reduced?

Case Study 2.1: Solution

### **1.7.9 Case Study 2.2** {#1.7.9-case-study-2.2}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_r.rmd\]  
Perform coding tasks to solve the issues listed above. You do not need to perform a full data exploration with descriptions and figures for each variable. Solutions in R and Python are available on the next page. 

\[END LINK\]  
Case Study 2.2

### **1.7.10 Case Study 2.2: Solution** {#1.7.10-case-study-2.2:-solution}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_2\_r.rmd\]  
The solution is found in the Rmd files for this section ( [atpa\_2\_7\_2\_r.rmd](#bookmark=id.hxa7rw3g5mbr) and [atpa\_2\_7\_2\_python.rmd](#bookmark=id.ac0wrlmhzo3f)). These are a few specific notes based on the information provided: 

* Variables were created for the percentage of visits that were extended as well as the percentage of visits that ended with rescheduling another appointment.  
* One issue with using the total number of visits prior to 2018 as a variable in a predictive model is that the further new data gets from 2018, the less likely this variable will be as valuable. For example, imagine using this model to predict 2022 numbers. Using data from prior to 2018 for prior visits could be very inaccurate as client bases change and shift. Instead, we created a variable for the number of visits in 2017 specifically. In this case, the model could be used as is where that variable is the number of visits in the prior year. Regardless of the year, the information from the prior year will always be relevant.  
* The *year* variable was validated by examining the first year that a patient visited and matching it with when the questionnaire was filled out. Only 5 individuals out of 340, or about 1.4% did not match. This is fairly strong evidence that the year variable from both sources is consistent.  
* The vast majority of the complete data indicates that the individual has not had surgery. For this reason, all the missing data values were imputed as having no surgery. It would also be okay to use other imputation methods, such as CART or logistic regression.  
* Individual variables were created for each of the causes, where 1 indicates that that cause was listed and 0 indicated it was not.  
* The smaller levels in the *how\_heard* variable were combined. The new categories are referral, radio ad, internet search, and other.

\[END LINK\]  
Case Study 2.2: Solution

### **1.7.11 Case Study 2.3: Report** {#1.7.11-case-study-2.3:-report}

Write a report describing and justifying the data modifications. A possible solution is on the next page.  
Case Study 2.3: Report

### **1.7.12 Case Study 2.3: Solution** {#1.7.12-case-study-2.3:-solution}

\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_2\_7\_cs23.pdf\]  
A sample report is available for download ( [atpa\_2\_7\_cs23.pdf](#bookmark=id.p2ixfrsbr1eh)).  
\[END LINK\]  
Case Study 2.3: Solution

### **1.7.13 Module 2 Bibliography** {#1.7.13-module-2-bibliography}

Module 2 Bibliography  
\[BEGIN LINK \-https://cdn-files.soa.org/e-learning/atpa/atpa\_m2\_bibliography.pdf\]  
A PDF copy of the bibliography is available as well ( [atpa\_m2\_bibliography.pdf](#bookmark=id.y20amucw9a2)).  
\[END LINK\]

Component Table224

| Type | Panel |
| :---- | :---- |
| Title | Panel |
| Header | Panel Header |
| Content |  Antonio, N., de Almeida, A., & Nunes, L. (2019). Hotel booking demand datasets. Data in brief, 22, 41-49. Barocas, S., & Selbst, A. (2016). Big Data's Disparate Impact. 104 California Law Review, 671-732. Bhalla, D. Dplyr tutorial: Data manipulation (50 examples). ListenData. https://www.listendata.com/2016/08/dplyr-tutorial.html. Accessed March 2, 2022\. Centers for Disease Control and Prevention. Nutrition, Physical Activity, and Obesity \- Youth Risk Behavior Surveillance System \- CKAN. https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-youth-risk-behavior-surveillance-system. Published April 25, 2021\. Accessed March 3, 2022\. Dastin, J. (2018). Amazon scraps secret AI recruiting tool that showed bias against women. Retrieved December 19, 2020, from Reuters: https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G Educative. Data Analysis Made Simple: Python pandas tutorial. https://www.educative.io/blog/python-pandas-tutorial. Accessed March 2, 2022\. Educative. Pandas cheat sheet: Top 35 commands and Operations. https://www.educative.io/blog/pandas-cheat-sheet. Accessed March 2, 2022\. Fiorina, C. (2004, December 6). Information: the currency of the digital age. Retrieved December 5, 2021 from http://www.hp.com/hpinfo/execteam/speeches/fiorina/04openworld.html Hall, G., Jones, M., Madigan, K., & Zheng, S. (n.d.). Data Quality Management in the P\&C Insurance Sector. Retrieved December 20, 2020, from Casualty Actuarial Society: https://www.casact.org/pubs/monographs/papers/09-Madigan.pdf Kahneman, D. (2011) Thinking, Fast and Slow. New York: Straus and Giroux Kearney J., Barkat S. Autoimpute tutorials. https://kearnz.github.io/autoimpute-tutorials. Accessed March 3, 2022\. Lander, J. P. (2017). R for everyone: Advanced analytics and graphics. Second edition. Addison-Wesley. Lerman, J. (2013). Big Data and Its Exclusions. Stanford Law Review Volume 66\. Lustig, I. Pandas cheat sheet. Data Wrangling with pandas. https://pandas.pydata.org/Pandas\_Cheat\_Sheet.pdf. Accessed March 3, 2022\. McCarthy, J. (2019, December). One in Five U.S. Adults Use Health Apps, Wearable Trackers. Retrieved from Gallup: https://news.gallup.com/poll/269096/one-five-adults-health-apps-wearable-trackers.aspx Neitmann, T. All you need to know about merging (joining) datasets in R. Thomas' adventuRe. https://thomasadventure.blog/posts/r-merging-datasets/. Published October 3, 2021\. Accessed March 3, 2022\. New York State Department of Financial Services. (2019, January 18). RE: Use of External Consumer Data and Information Sources in Underwriting for Life Insurance. Retrieved from New York State Department of Financial Services: https://www.dfs.ny.gov/industry\_guidance/circular\_letters/cl2019\_01 Petrou, T. (2017). Pandas Cookbook: Recipes for Scientific Computing, Time Series Analysis and Data Visualization using Python. Packt Publishing Ltd. Raden, N. (2019, September). Ethical Use of Artificial Intelligence for Actuaries. Retrieved from Society of Actuaries: https://www.soa.org/globalassets/assets/files/resources/research-report/2019/ethics-ai.pdf RStudio. Rstudio cheatsheets. https://www.rstudio.com/resources/cheatsheets/. Accessed March 2, 2022\. Samuel, N. How to format dates in Python. https://stackabuse.com/how-to-format-dates-in-python/. Published September 17, 2018\. Accessed March 3, 2022\. Schlimmer, J. (1987). Automobile Data Set, UCI Machine Learning Repository https://archive.ics.uci.edu/ml/datasets/Automobile. Irvine, CA: University of California, School of Information and Computer Science. Society of Actuaries. Mortality and Other Tables. https://mort.soa.org/. Accessed March 3, 2022\. Thailappan D. DBSCAN algorithm: Understand the DBSCAN clustering algorithm. https://www.analyticsvidhya.com/blog/2021/06/understand-the-dbscan-clustering-algorithm. Published June 8, 2021\. Accessed March 3, 2022\. Tidyverse. https://www.tidyverse.org/. Accessed March 2, 2022\. van Buuren, S., Groothuis-Oudshoorn, K. (2011). mice: Multivariate Imputation by Chained Equations in R. Journal of Statistical Software, 45(3), 1-67. DOI 10.18637/jss.v045.i03. Vullo, M. T. (2017, November 27). Second Amendment to 11 NYCRR 154 (Insurance Regulation 150). Retrieved December 20, 2020, from New York State Department of Financial Services: https://dfs.ny.gov/system/files/documents/2020/11/rf150a2txt.pdf Wickham, H. (2014). Tidy Data. Journal of Statistical Software, 59(10), 1–23. https://doi.org/10.18637/jss.v059.i10 Wickham, H. (2021). nycflights13: Flights that Departed NYC in 2013\. R package version 1.0.2. https://CRAN.R-project.org/package=nycflights13 Wickham, H. & Grolemund, G. R for data science. https://r4ds.had.co.nz/. Netlify. Accessed March 2, 2022\. Ziad Obermeyer, B. P. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. Science (366), 447–453.  |
| Footer | Panel Footer |

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARAAAAEQCAMAAABP1NsnAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAACc0lEQVR4Xu3cOU4EMQBFQRq4/41ZIluoLNTB9KLRvAqNA/Rw8IMW2/aWv949eHUFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQfDpwUNu+kcCPx48oBeCgqAgKAgKgoKgIDh2hwxHDoPV+CN+jYMj508vBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQE53xB9L8PD+ZnQMP+jVP1QlAQFAQFQUFQEBQEBcHVw2ysrDm/lh02XLvHpl4ICoKCoCAoCAqCguDqHTLMlbHskJv2x9ALQUFQEBQEBUFBUBAUBHcNs2WPTeMnNw20XggKgoKgICgICoKC4OodsuyPZW6MG/PmcuNUvRAUBAVBQVAQFAQFQUFw9TDbX1n7N07VC0FBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFQUFQEBQEBUFBUBAUBAVBQVAQFAQFwTlfED1x5if+1c9REBQEBUFBUBAUBMfukG8Pnk8vBAVBQVAQFAQFQUFQEGybJy+uF4KCoCAoCAqCgqAgKAgKgoKgICgICoKCoCAoCAqCgqAgKAgKgoKgICgICoKCoCAoCAqCgqAgKAgKgoKgICgICoKCoCAoCAqCgqAgKAgKgoKgICgICoKCoCAoCAqCgqAgKAgKgoKgICgICoKCoCAoCAqCgqAgKAgKgoKgICgICoKCoCD4BZeKETHVTGeKAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOQAAAA1CAYAAABRNUcHAAAJEklEQVR4Xu2dWascRRSAj3FXjLgbgxo3XBF3DKJxwQ0l7hgXVJQokYAbrnG5KBo1MRqjuESNC8QNjaIQJaBBlIhIEBERn+6Tb774B/R8Vp9M3Zru6Z7cOz3TnfPBIZnunqrq7jpr1SQijuM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4juM4jtNEdlKZlh6cJLRHu47jVGQrlctUrsr+PpXQHu3S/lS37TitZI7KXSrbpCemCNqlffppM4ervKjymcpclXskGKNXVK6MrnNq4AKV51T+Vtmo8r3KEpWT4osieGHfqfyrMq6ySuXg+IKamKnyqsq+6YmInVXmS7iO+2PMH6ncn8nTKh9KuP8jJd8T0j7fp7+2wjM6WWWlhOezT3b8OglKulv22amJHVReljBheQllnCHhRQ1rkm6t8qDK5emJAvZSWafyiwRvEEOueJHKnyr3Sr63pR/6o9+2sZ3KuRIMEsb4kuw4xulhlRUqO2bHnBp5RIJC3paeSNhe5Ukp9qB1cJDKapUZ6YkCjpWgcO+q7JKcA+5puco/Kuck54B+6I9+2wpK+aPKYdlnvOKnKrdsusKplRskKOSY5IduxnkScoxhegu8ONa71zhjrpbyezODhCdM4V4fl2rRQ1MhVyb9IMyHU1Q2SDBmGCk77tQEFpIJSb5UFKKQT+FJeuVtg4axMUbGWwWU6SkJ90b+mwdh2zIJ1zAx86A/wnrC+7ZB1ED0cF90DMO0VOUQlYUyXAO8RXKiyl8qX0p+Es8LwTPiIYfJfiprVI5ITxSwq8rHEkJWrH0etPmtyu8qRyfnDPqjX65tGxTlyB/Pio5RWcbwPSSdMNapEYodFD1+UDkwOQfkjOSO5FtVIMQhHyUUvFaCMh+THaPIEkNV71GVNySc31blbJXFKjepPKGye3YtSoVipG0UgSL9qrJWZc/kHBDCUmUkf2ScRSEt/dFvkVI7g4OIDO+NcaAyHofPJ0hYHVgQHWsFe6h8JWHypt5nusrzUt1SomAfSCgIWNWSnAQPnHoq87wUTKjecs1rEpYlUP55EpYsyAPhNAkeD89XBcJUQlFCUkLTGCqsrLf9JGG9rdduH/O09O/UB3PvMQlzypxGnHrwPsald6rVSNgmxjoUkzeedHiM6zMp8h4xWC9yrdezvxum8KmnwhtToLHyO/3zfb7LMbwy4dSh2fUUVqo+fCvd0yYG5cxMKFLcqfKJBKPBSy/DclczDAbeHMv99WYI6QFGyCmGJSl2S4EZ17h+wDu+W0KdoFV5blzYiKuJeEUmc5VJC3w3b/kAxSMcTj0VD9f6o6CCh8SbFtGPQlqxgjbJkQ289mwJVUTC4SoVRFPIQVdaiR5cgmDsFkmInmxpilw/zeNZJy5brmskVNbiSmO/a462dpX30Mz7sbwSg3IipjypB03pRyHxqj9L2BSQl3PyIhkTXrKMuhTyYpf/JTagYOFqnidkTrUy0mCyMUHtpqmo9rPmaJXaZdKdr5n3Sx+0YR4074HHzJXqCmlGIG88QGjO+SrtmULSf1NgOxwh3yhDDl80J2JsbsbhKjBX2GHF/GkdWBmboJTC+11ztAX4NHww71fkqcCUp8wDoURFSzMp5vHT8Rgc5/yYlOfHlgPTfxNgK9wDUr0qPixIF4jCehUMLZ3CYKeKRyTGfeYZ3MZD3E4VlJBzqfS/5mhWLA0fzPuZp2JSYxlj8KBpBTYPQheKMWlInFKUPxqWk1QxAkB/9Ev/MaNY1MGbs2TUa5KPEjxTxlu06QLjy7PK2/pIwSetV7QGy7mYpChkv9YVRaOgE3sRq9LSpuWPC2WikpjyVPF8lqfmKVmMGQGMS57y2nnGZWEQY2US5903/dFv2fhGAYpirP/2Cv1HCcbJ1sSid2oKmaYWe0uIgsrSjcZiYVm8ybgfeHD8fMeKJExwFviZyHgqPBHXEKLEE9sMQVn+CPbyyryahcBF291QUpSVa8yAzJJQQs/7xQf9VRnfsOGZL5LRzx1TyM1RrjzsnccFP4zm7RJC89aCpeFHqb12rJSxv4TfF86XMDH4vSXtkq9h4diRc+qmqwPHqfwhE7du9YIQhaWY1JMRPrL1DQXDC7O54I7sMwYmVibub47K+xLGRGXvZukOiYB+6K8JoRHjf0m6Q+tRh80o/Ei6aAmKnVrkiiskvCtSHOaaMwLgXd+R4n2nUw390F+d4So7U56RkLdiKNjIwG4ito4xGTEOGB3OseXQimX8yecZ2WfA+JCzM5m5jwslVCbnSTBItuliMmAAUCh+J8tyEsaQ31YylmtULlW5VYKBfFa6w0wiljclRGlOA+Fl89IHHULSvk2uOsELEO6PSdipZB7P8nSLYizNuCI7z3XvyUTjwbY/9oKyDLJROj/EtqWc+FcemwsREe2vlO5/dWBcOv8MCuNjq2K6+YP7WC1TYxycIUBog6Utq8pOFtqnn6JQalCgjCw9sX/WcnIg9P9COp7EJvjs6HOqkCxdnS4hT0O5Z2XHyccoluApjWkSKpcYoV6CEh+VfYfKOTk7+RztW2iPMSPvxjObR8SgbJDuGoUrZAvACi/J/hwEg26/DIzBb9JRNluPo8BhkQHh4VrpjJHq8VvSHV7nKQdeimLaVIX+KGVcELQN+WZQ8OgUzdJ9zoBCMu4DkuNOw2ACLpDuAs9koT280cz0RI3g0dZJJx8kz/pGOhVUxrhcQlEKb3q8dPLr1NP0Ug6eoYWUk4HcdpV0lA2DgsJTtAPGxhhuzM4xZgPP/nZ2jeOMHObRKOzYLhTCPX4eZx4NpVsvIXdjjZcQkmtZQ04r2eZtLXdj4n8uITc+X6pXuIuwtWQKTQb5Y2xQGNN6CR6UIlUceXBvi6WlO26c5oPCrJHgTQwmOJN+evYZT4TysVMIz2frp4SxsWIARZ84tOVackGWpvBsaQjZL3g78sdYsdmcwJqzKRl9U3WlX6qu8dIa1de6C2eOUwuE2YSyhKlNAOPzguTvqHKcVkDllPW/UQcvyRJOurfZcVoFISnFrlHfWkY+TPEsb7ui47QK1hRH/X/wYnyM03Ecx3Ecx3Ecx3Ecx3Ecx3Ecx3EcZ4vjPyY/o+vdhE/9AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAMAAABHPGVmAAADAFBMVEUAAAD///+AgIDAwMD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYRJjAAAAA3ElEQVR4Xu2YywrDIBREY9P//2P7IPYhFvSeYmYhcxbB3EWOMwQJSWk7n0s7OANLEJYgLEFYgrAEYQliHcm1HdSQL5l7O6iQJJFIunVt/RZePPeZ+9VKkliCsARhCWIdyeiA/LIf1/yzDiBJIpHE68pHS6WochtGkkQiide1vRsrC4IkiUSC6vq8WjtrTJJEIonX1ZxdpDFJEokkXlddTriogiSJJQhLEJYg1pGMDsgpm5jykBESSbeuWzv4E0kSiST1fiHNQpLEEoQlCEsQliAsQViCsARhCWIdyQNySA/ZGfANuQAAAABJRU5ErkJggg==>