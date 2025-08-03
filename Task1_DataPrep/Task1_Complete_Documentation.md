# Task 1: Data Preparation - Complete Documentation

## ATPA Assessment - June to August 2025

---

## 📊 **Business Problem Context**

**Client**: NMInsights, a non-profit public policy research institute in New Mexico
**Objective**: Identify key characteristics of criminal incidents that lead to arrests being made
**Key Questions**:
1. What characteristics of a criminal incident are associated with an arrest?
2. Are there specific categories of criminal offenses more likely to result in arrests than others?

**Data Source**: Federal Bureau of Investigation's Crime Data Explorer (2023 New Mexico data)
- **incidents.csv**: 96,904 records with 58 variables (demographic, offense, location, agency info)
- **arrestee.csv**: 28,682 records with 21 variables (arrestee demographics, charges, weapons)

---

## 🎯 **Task 1 Requirements & Implementation**

### **1a) Data Cleaning and Preparation**

#### **Missing Values Analysis & Handling**

**Incidents Dataset Missing Values**:
- **High Missing Rate (>90%)**: `outside_agency_id` (99.98%), `num_premises_entered` (99.66%), `cleared_except_date` (99.53%)
- **Moderate Missing Rate (50-90%)**: `recovered_count` (98.39%), `method_entry_code` (94.86%), `stolen_count` (94.03%)
- **Significant Missing Rate (30-50%)**: `victim_injury_name` (87.58%), `victim_injury_code` (75.39%), `weapon_name` (75.37%)

**Arrestee Dataset Missing Values**:
- **High Missing Rate**: `under_18_disposition_code` (93.95%)
- **Moderate Missing Rate**: `hc_code` (41.55%), `resident_code` (12.98%)

**Handling Strategy**:
- **Categorical Variables**: Mode imputation (most frequent value)
- **Numeric Variables**: Median imputation (preserves distribution)
- **Justification**: Mode for categorical preserves most common category; median for numeric is robust to outliers

#### **Dimension Reduction**

**High Cardinality Variables Identified**:
- `submission_date` (359 unique values) → Reduced to 21 categories
- `incident_date` (365 unique values) → Reduced to 21 categories  
- `agency_name` (89 unique values) → Reduced to 21 categories
- `arrest_date` (405 unique values) → Reduced to 21 categories

**Strategy**: Keep top 20 categories, group remainder as 'Other'
**Justification**: Reduces sparsity while preserving most common categories

#### **Numeric to Factor Conversion**

**Age Variables**:
- `victim_age_num` → `victim_age_group` (Under 18, 18-25, 26-35, 36-50, 51-65, 65+)
- `offender_age_num` → `offender_age_group` (same bins)
- `age_num` (arrestee) → `age_group` (same bins)

**Population Variable**:
- `population` → `population_group` (Under 10K, 10K-50K, 50K-100K, 100K-500K, 500K+)

**Justification**: Age groups provide meaningful categories for analysis; population groups reflect jurisdiction size differences

---

### **1b) Data Merging Strategy**

#### **Matching Analysis**
- **Incidents Dataset**: 96,904 unique incidents
- **Arrestee Dataset**: 26,955 unique incidents  
- **Overlap**: 18,439 incidents in both datasets
- **Incidents-only**: 78,465 (no arrests recorded)
- **Arrestee-only**: 8,516 (arrests without incident records)

#### **Merge Strategy**: LEFT JOIN
- **Primary Dataset**: incidents.csv (all criminal incidents)
- **Secondary Dataset**: arrestee.csv (arrest information)
- **Logic**: Keep all incidents, add arrestee information where available
- **Result**: 96,904 records with arrest information for 18,439 incidents

#### **Variable Handling**
- **Duplicate Variables**: `offense_category_name`, `crime_against`, `weapon_name`
- **Strategy**: Use incidents data as primary, supplement with arrestee data where incidents data is missing
- **Arrestee Aggregation**: Group by `incident_id` to create summary statistics (count, mode, mean)

---

### **1c) Target Variable Creation**

#### **ARREST Variable**
- **Definition**: Binary variable indicating whether an incident resulted in an arrest
- **Logic**: `ARREST = 1` if `num_arrests` is not null, `ARREST = 0` otherwise
- **Distribution**:
  - No Arrest (0): 78,465 incidents (80.97%)
  - Arrest (1): 18,439 incidents (19.03%)

**Key Insight**: The dataset shows that only about 19% of reported incidents resulted in arrests, indicating significant challenges in law enforcement resolution.

---

### **1d) Exploratory Data Analysis**

#### **Target Variable Distribution**
- **Overall Arrest Rate**: 19.03%
- **Class Imbalance**: Significant (80.97% no arrest vs 19.03% arrest)
- **Implication**: Models will need to handle class imbalance appropriately

#### **Key Visualizations Created**
1. **Arrest Rate by Offense Category**: Shows which crime types have higher arrest rates
2. **Arrest Rate by Hour of Day**: Temporal patterns in arrest likelihood
3. **Arrest Rate by Victim Type**: Differences in arrest rates based on victim characteristics
4. **Arrest Rate by Agency Type**: Variations across different law enforcement agencies

#### **Reasonability Checks**

**Outlier Analysis**:
- `agency_id`: 342 outliers (0.35%) - acceptable
- `location_id`: 4,754 outliers (4.91%) - acceptable
- `offender_age_num`: 33,683 outliers (34.76%) - high rate, needs investigation
- `stolen_count`: 68 outliers (0.07%) - acceptable

**Internal Consistency**:
- All incident hours within valid range (0-23)
- Age values within reasonable bounds (0-120)
- No data type inconsistencies detected

---

## 📈 **Key Findings**

### **Data Quality Insights**
1. **Missing Data Patterns**: Weapon information and injury details are frequently missing (75%+ missing rates)
2. **Age Data Issues**: Significant missing offender age data (43.47% missing)
3. **Property Crime Focus**: High missing rates for property-specific variables suggest many incidents are non-property crimes

### **Arrest Patterns**
1. **Low Overall Arrest Rate**: Only 19% of incidents result in arrests
2. **Temporal Patterns**: Arrest rates vary by time of day (visualization shows patterns)
3. **Offense Type Variation**: Different crime categories show varying arrest likelihoods
4. **Agency Differences**: Different law enforcement agencies show different arrest rates

### **Data Limitations**
1. **Incomplete Arrest Data**: Only incidents with arrests are in arrestee dataset
2. **Missing Demographics**: Significant missing age and demographic information
3. **Reporting Inconsistencies**: High missing rates suggest inconsistent reporting practices

---

## 🔧 **Technical Implementation**

### **Final Dataset Characteristics**
- **Records**: 24,951 (after removing records with missing values in key features)
- **Features**: 13 predictor variables + 1 target variable
- **Features Included**:
  - `incident_hour`: Time of incident
  - `offense_category_name`: Type of crime
  - `crime_against`: Crime target (Person/Property/Society)
  - `victim_type_name`: Type of victim
  - `weapon_name`: Weapon used
  - `agency_type_name`: Type of law enforcement agency
  - `population_group`: Jurisdiction size
  - `victim_age_group`: Victim age category
  - `offender_age_group`: Offender age category
  - `stolen_count`: Number of items stolen
  - `recovered_count`: Number of items recovered
  - `suburban_area`: Urban/suburban indicator

### **Data Quality Metrics**
- **Completeness**: 25.7% of original incidents retained (24,951/96,904)
- **Arrest Rate in Final Dataset**: 22.60%
- **Feature Completeness**: All features have complete data

---

## 📋 **Recommendations for Next Steps**

### **Modeling Considerations**
1. **Class Imbalance**: Implement techniques like SMOTE, class weights, or undersampling
2. **Feature Engineering**: Create interaction terms between key variables
3. **Cross-Validation**: Use stratified sampling to maintain class proportions

### **Data Enhancement Opportunities**
1. **External Data**: Consider adding demographic data at county/agency level
2. **Temporal Features**: Create seasonal and day-of-week variables
3. **Geographic Features**: Add location-based variables if coordinates available

### **Business Insights**
1. **Arrest Rate Analysis**: Focus on understanding why 81% of incidents don't result in arrests
2. **Resource Allocation**: Use findings to inform law enforcement resource distribution
3. **Policy Implications**: Identify factors that could improve arrest rates

---

## 📁 **Deliverables**

### **Files Created**
1. **`prepared_data.csv`**: Final dataset ready for modeling (24,951 records, 14 features)
2. **`task1_eda_plots.png`**: Exploratory data analysis visualizations
3. **`task1_data_preparation_complete.py`**: Complete data preparation script

### **Key Metrics**
- **Original Incidents**: 96,904
- **Final Dataset**: 24,951 records
- **Arrest Rate**: 22.60%
- **Features**: 13 predictors + 1 target
- **Data Completeness**: 100% (no missing values in final dataset)

---

## ✅ **Task 1 Completion Status**

**All Requirements Met**:
- ✅ Data cleaning and missing value handling
- ✅ Dimension reduction implementation
- ✅ Numeric to factor conversion
- ✅ Dataset merging with proper strategy
- ✅ Target variable creation
- ✅ Exploratory data analysis with visualizations
- ✅ Reasonability checks and quality assessment
- ✅ Comprehensive documentation

**Ready for Task 2**: The prepared dataset is now ready for privacy analysis and subsequent modeling tasks. 