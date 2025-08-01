# Module 2: Working with Data - Content Summary

## Overview
Module 2 covers comprehensive data manipulation, cleaning, and preparation techniques using Python. The module consists of 7 main sections plus case studies and preparation materials.

---

## Section 2.2: Reading and Writing Data (`atpa_2_2_python.rmd`)

### Key Topics Covered:

#### **Data Structure Creation**
- Creating pandas DataFrames from lists and dictionaries
- Adding variables to existing DataFrames
- Working with dictionaries and list extraction

#### **File Reading Operations**
- **Space-delimited files**: `pd.read_table()`
- **CSV files**: `pd.read_csv()`
- **Semicolon-delimited files**: `pd.read_table(sep=";")`
- **Files with headers to skip**: `pd.read_csv(skiprows=4)`
- **Files without headers**: `pd.read_csv(names=[...])` or `pd.read_csv(header=None)`

#### **XML Data Processing**
- Simple XML reading with `pd.read_xml()`
- Complex XML structures using xpath
- Multiple node extraction
- Attribute and element value extraction
- Working with nested XML structures

#### **JSON Data Processing**
- Simple JSON reading with `pd.read_json()`
- Nested JSON handling with `json.load()` and `pd.json_normalize()`
- Complex nested structures with record paths and metadata

#### **Excel File Processing**
- Reading multiple sheets from Excel files
- Using `pd.read_excel()` with `sheet_name` parameter

#### **Data Reshaping**
- **Tall to Wide**: Using `pivot()` method
- **Wide to Tall**: Using `melt()` method
- Understanding missing data implications during reshaping

#### **Data Writing**
- Writing to space-delimited files: `to_csv(sep=" ")`
- Writing to CSV files: `to_csv()`
- Appending to existing files
- Controlling index inclusion with `index=False`

---

## Section 2.3: Data Transformation and Cleaning (`atpa_2_3_python.rmd`)

### Key Topics Covered:

#### **Data Subsetting and Filtering**
- **Conditional filtering**: Using `query()` method
- **Multiple conditions**: AND/OR operations
- **String pattern matching**: `str.contains()`, `str.startswith()`, `str.endswith()`
- **Numeric filtering**: Range conditions, inequalities
- **Column selection**: Using `loc[]` and `iloc[]`
- **Row/column removal**: Using `drop()`

#### **Data Sorting**
- Single column sorting: `sort_values()`
- Multiple column sorting with tie-breakers
- Ascending/descending order control

#### **Variable Creation and Manipulation**
- **New variable creation**: Using `assign()` method
- **Multiple variables**: Creating several variables at once
- **Variable overwriting**: Replacing existing variables
- **Binning variables**: Using `pd.cut()` for categorical creation

#### **Aggregation and Grouping**
- **Groupby operations**: `groupby().agg()`
- **Multiple aggregations**: Mean, count, unique values
- **Column renaming**: After aggregation
- **Index handling**: Using `as_index=False`

#### **Missing Data Handling**
- **Missing value identification**: `isnull()`, `dropna()`
- **Specific value replacement**: `replace()`
- **Conditional filtering**: Removing specific values

#### **Data Type Conversions**
- **String operations**: Case changes, replacements, substrings
- **String to numeric**: `int()`, `float()`
- **Numeric to string**: `str()`
- **String manipulation**: `split()`, `join()`

#### **Date and Time Processing**
- **Date creation**: Using `datetime` module
- **String to date conversion**: `strptime()` with format strings
- **Date arithmetic**: Time differences
- **Date component extraction**: Day, month, year, weekday

#### **Categorical Variables**
- **Factor creation**: Using `pd.Categorical()`
- **Ordered vs unordered**: Controlling factor order
- **Factor recoding**: Direct mapping and string operations
- **Level combining**: Merging small categories
- **Boolean to numeric**: Converting logical to integer

#### **Practical Exercises**
- **Flights data analysis**: Comprehensive data manipulation exercise
- **Hotel bookings analysis**: Advanced filtering and aggregation
- **Automobile data cleaning**: Complete data preparation workflow

---

## Section 2.4: Relational Databases (`atpa_2_4_python.rmd`)

### Key Topics Covered:

#### **Join Operations**
- **Left Join**: `merge(how="left")`
- **Right Join**: `merge(how="right")`
- **Inner Join**: `merge(how="inner")`
- **Outer/Full Join**: `merge(how="outer")`

#### **Join Complexity**
- **Multiple key joins**: Joining on multiple columns
- **Duplicate key handling**: Managing repeated values
- **Key specification**: Using `on` parameter

#### **Data Combination**
- **Column concatenation**: Using `pd.concat(axis=1)`
- **Row concatenation**: Using `pd.concat(axis=0)`
- **Multiple table merging**: Chaining merge operations

#### **Practical Application**
- **Movie data analysis**: Complex multi-table joins
- **Economic data integration**: Time-series data combination
- **Rating system integration**: Combining different data sources

---

## Section 2.5: Data Validation (`atpa_2_5_python.rmd`)

### Key Topics Covered:

#### **Duplicate Detection and Removal**
- **Exact duplicate removal**: `drop_duplicates()`
- **Column-specific duplicates**: `drop_duplicates(subset=[...])`
- **Duplicate handling strategies**: `keep="first"`, `keep="last"`
- **Column duplicate detection**: Transposing and checking

#### **Data Quality Assessment**
- **Descriptive statistics**: Using `describe()`
- **Domain validation**: Checking value ranges
- **Logical consistency**: Validating relationships between variables
- **Confidence interval validation**: Ensuring values fall within expected ranges

#### **Correlation Analysis**
- **Internal consistency checks**: Correlating related variables
- **Stratified analysis**: Grouping by categories
- **Visual validation**: Plotting relationships

#### **Practical Validation Exercise**
- **Youth risk data**: Comprehensive data quality assessment
- **Multiple validation checks**: Duplicates, ranges, consistency
- **Correlation analysis**: Internal consistency verification

---

## Section 2.6: Missing and Extreme Values (`atpa_2_6_python.rmd`)

### Key Topics Covered:

#### **Missing Data Analysis**
- **Missingness patterns**: Identifying missing data structure
- **Permutation tests**: Testing for missing at random (MAR)
- **Visual assessment**: Box plots for missing vs non-missing groups
- **Statistical testing**: Confidence intervals for missingness

#### **Imputation Methods**
- **Mean imputation**: Using `SingleImputer` with 'mean' strategy
- **Regression imputation**: Using `MultipleImputer` with 'least squares'
- **K-Nearest Neighbors**: Using `KNNImputer`
- **Categorical imputation**: Binary logistic for categorical variables
- **Mixed data imputation**: Handling both numeric and categorical

#### **Outlier Detection and Treatment**
- **Visual identification**: Box plots and histograms
- **Statistical methods**: Z-scores, percentiles
- **Transformation methods**: Log transformation, percentile transformation
- **Capping and trimming**: Setting upper/lower bounds
- **Clustering-based**: Using DBSCAN for multivariate outliers

#### **Advanced Techniques**
- **Manual regression**: Implementing imputation manually
- **Multiple imputation**: Creating multiple versions
- **Domain-specific handling**: Special cases (e.g., rotor engines)

#### **Practical Applications**
- **Automobile data**: Comprehensive missing data analysis
- **Hotel bookings**: Outlier detection and treatment
- **Production data**: Various imputation strategies

---

## Section 2.7: Case Studies

### Case Study 1: Website Analytics (`atpa_2_7_1_python.rmd`)

#### **Data Integration**
- **Multiple data sources**: CSV and Excel files
- **Data combination**: Merging different data structures
- **Date handling**: Converting and matching date formats

#### **Data Cleaning**
- **Outlier removal**: Filtering extreme values
- **Missing data imputation**: Regression-based imputation
- **Variable standardization**: Fixing inconsistent values
- **Factor creation**: Converting to categorical variables

#### **Analysis Preparation**
- **Aggregation**: Daily statistics calculation
- **Variable creation**: Weekday identification
- **Data validation**: Ensuring data quality

### Case Study 2: Chiropractic Practice (`atpa_2_7_2_python.rmd`)

#### **Complex Data Integration**
- **XML data processing**: Extracting visit information
- **Questionnaire data**: Combining survey responses
- **Validation checks**: Ensuring data consistency

#### **Variable Engineering**
- **Text analysis**: Extracting keywords from text fields
- **Aggregation**: Creating summary statistics
- **Factor manipulation**: Combining small categories

#### **Data Quality**
- **Missing value handling**: Removing problematic variables
- **Data validation**: Cross-checking between sources
- **Final dataset creation**: Comprehensive data preparation

---

## Preparation Materials

### Flights Data Preparation (`FlightsPrep_python.Rmd`)

#### **Large Dataset Handling**
- **Multiple file processing**: Reading and combining 6 years of data
- **Memory management**: Efficient data processing
- **Data filtering**: Extracting specific airport data (BOI)

#### **Data Transformation**
- **Unitization**: Converting to per-departure metrics
- **Variable creation**: Calculating ground time
- **Data type management**: Converting to appropriate types

#### **Assessment Preparation**
- **Data summarization**: Comprehensive descriptive statistics
- **Quality checks**: Ensuring data integrity
- **Format standardization**: Preparing for analysis

---

## Key Skills Developed

### **Technical Skills**
- Pandas DataFrame manipulation
- File I/O operations (CSV, XML, JSON, Excel)
- Data cleaning and validation
- Missing data handling
- Outlier detection and treatment
- Data aggregation and grouping
- Join operations and data integration

### **Analytical Skills**
- Data quality assessment
- Statistical validation
- Pattern recognition in data
- Problem-solving with real datasets
- Critical thinking about data issues

### **Practical Applications**
- Real-world data scenarios
- Industry-specific examples (aviation, healthcare, web analytics)
- Assessment preparation
- Professional data science workflows

---

## Software and Packages Used

### **Core Python Libraries**
- `pandas`: Primary data manipulation
- `numpy`: Numerical operations
- `matplotlib`: Basic plotting
- `seaborn`: Statistical visualization

### **Specialized Packages**
- `autoimpute`: Missing data imputation
- `sklearn`: Machine learning algorithms (KNN, DBSCAN)
- `lxml`: XML parsing
- `openpyxl`: Excel file handling
- `datetime`: Date/time operations

### **R Integration**
- `reticulate`: Python-R integration in RStudio
- Seamless workflow between R and Python environments

---

## Assessment Relevance

This module provides essential skills for the ATPA assessment, covering:
- Data preparation and cleaning
- Quality assurance and validation
- Missing data handling
- Outlier detection and treatment
- Data integration and manipulation
- Real-world problem-solving scenarios

The case studies and exercises directly prepare students for the types of data challenges they will encounter in the actual assessment. 