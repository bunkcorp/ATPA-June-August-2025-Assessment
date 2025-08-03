# ATPA MCP Server - Project Summary

## Project Overview

This project implements a comprehensive **Model-Context-Protocol (MCP) Server** for the ATPA June-August 2025 assessment, specifically designed to address NMInsights' research questions about criminal incident and arrest data in New Mexico.

## Business Context Addressed

### NMInsights Research Questions:
1. **What characteristics of criminal incidents are associated with arrests?**
2. **Which types of crimes are more or less likely to lead to arrests?**

### Business Value:
- **Data-Driven Insights**: Enables systematic analysis of arrest patterns
- **Resource Allocation**: Helps law enforcement understand factors affecting arrest success
- **Policy Development**: Supports evidence-based policy decisions
- **Transparency**: Provides accessible data exploration tools

## Technical Architecture

### MCP Layer Design

#### 1. **Context Layer** (`context.py`)
- **Purpose**: Metadata management and data dictionary parsing
- **Key Features**:
  - Loads and parses `Data_Dictionary.xlsx`
  - Categorizes variables by source (incidents vs arrestee)
  - Provides field metadata and descriptions
  - Supports fallback metadata creation

#### 2. **Model Layer** (`loader.py`)
- **Purpose**: Data loading, cleaning, and standardization
- **Key Features**:
  - Handles large CSV files with chunked reading
  - Standardizes column names to snake_case
  - Converts data types (dates, numbers, categories)
  - Provides paginated data access with filtering
  - Handles missing values and data quality issues

#### 3. **Protocol Layer** (`protocol.py`)
- **Purpose**: Data merging and target variable creation
- **Key Features**:
  - Merges incidents and arrestee datasets using `INCIDENT_ID`
  - Creates binary target variable: `ARREST = 1` if incident has arrest, `0` otherwise
  - Handles imperfect matching (not every incident has an arrest)
  - Adds derived features (time-based, categorical, geographic)
  - Manages multiple arrests per incident

#### 4. **Insights Layer** (`insights.py`)
- **Purpose**: Exploratory Data Analysis and visualization
- **Key Features**:
  - Comprehensive summary statistics
  - Arrest rate analysis by crime type
  - Temporal pattern analysis (hourly, daily, monthly)
  - Correlation analysis for numerical variables
  - Feature importance for arrest prediction
  - Data quality and reasonability checks

#### 5. **Ethics Layer** (`ethics.py`)
- **Purpose**: ATPA Module 1 Data and Model Ethics framework integration
- **Key Features**:
  - Protected class identification and monitoring
  - Bias assessment (selection, measurement, representation)
  - Fairness metrics calculation (demographic parity)
  - Ethical recommendations generation
  - Compliance checklist (ASOPs, regulations)
  - Risk assessment for criminal justice context

## Key Features Implemented

### 1. **Interactive Web Dashboard**
- **URL**: `http://localhost:8000/dashboard`
- **Features**:
  - Real-time server status monitoring
  - Interactive data exploration
  - Plotly-based visualizations
  - Data quality assessment tools
  - API documentation browser

### 2. **Comprehensive API Endpoints**
- **Context**: Field metadata and data dictionary access
- **Model**: Raw data access with pagination and filtering
- **Protocol**: Merged dataset creation and analysis
- **Insights**: EDA tools and visualizations
- **Utility**: Health checks and documentation

### 3. **Data Processing Pipeline**
- **Large File Handling**: Chunked reading for 30MB+ CSV files
- **Data Cleaning**: Standardization and type conversion
- **Feature Engineering**: Time-based and categorical features
- **Quality Assurance**: Missing value analysis and reasonability checks

### 4. **Business Intelligence Features**
- **Arrest Rate Analysis**: By crime type, agency, geography
- **Temporal Patterns**: Hourly, daily, monthly arrest patterns
- **Feature Importance**: Which variables predict arrest outcomes
- **Data Quality**: Comprehensive reasonability checks

## Data Sources Integrated

### 1. **Data Dictionary** (`Data_Dictionary.xlsx`)
- Variable names, types, and descriptions
- Source file categorization
- Valid values and missing value codes

### 2. **Incidents Data** (`incidents.csv`)
- ~30MB file with criminal incident records
- Key fields: incident_id, offense_category, crime_against, victim/offender demographics
- Temporal and geographic information

### 3. **Arrestee Data** (`arrestee.csv`)
- ~4MB file with arrest records
- Key fields: arrestee_id, incident_id, arrest_date, demographics
- Links arrests to incidents via incident_id

## Target Variable Creation

### ARREST Target Variable
- **Definition**: Binary variable indicating whether an incident resulted in an arrest
- **Logic**: `ARREST = 1` if incident_id appears in arrestee dataset, `0` otherwise
- **Business Meaning**: Success/failure of law enforcement response
- **Use Cases**: Predictive modeling, resource allocation, policy analysis

### Derived Features
- **Time Features**: Days between incident and arrest
- **Categorical Features**: Age categories, agency size, crime severity
- **Temporal Features**: Hour categories, day of week
- **Geographic Features**: Agency size based on population

## Performance Optimizations

### 1. **Memory Management**
- Chunked reading for large files
- Optional sampling for development
- Lazy loading of data

### 2. **Scalability Features**
- Pagination for all data endpoints
- Column-based filtering
- Efficient data structures

### 3. **Error Handling**
- Graceful fallbacks for missing files
- Comprehensive logging
- User-friendly error messages

## Business Insights Enabled

### 1. **Arrest Pattern Analysis**
- Which crime types have highest/lowest arrest rates
- Temporal patterns in arrest success
- Geographic variations in arrest rates

### 2. **Predictive Modeling Foundation**
- Feature importance for arrest prediction
- Correlation analysis with arrest target
- Data quality assessment for modeling

### 3. **Resource Allocation Insights**
- Agency performance analysis
- Temporal resource needs
- Geographic resource distribution

## Technical Stack

### Backend
- **FastAPI**: Modern, fast web framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Plotly**: Interactive visualizations

### Frontend
- **HTML/CSS/JavaScript**: Dashboard interface
- **Plotly.js**: Client-side visualizations
- **HTMX**: Dynamic content loading

### Data Processing
- **OpenPyXL**: Excel file parsing
- **Scikit-learn**: Feature importance analysis
- **Matplotlib/Seaborn**: Statistical visualizations

## Usage Instructions

### Quick Start
```bash
cd mcp_server
python3 start_server.py
```

### Access Points
- **Dashboard**: http://localhost:8000/dashboard
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Key Workflows
1. **Data Exploration**: Use dashboard to browse data
2. **Analysis**: Create merged dataset and run EDA
3. **Visualization**: Generate interactive charts
4. **Quality Assessment**: Run reasonability checks

## Business Impact

### For NMInsights
- **Systematic Analysis**: Structured approach to data exploration
- **Reproducible Results**: Consistent methodology across analyses
- **Scalable Platform**: Can handle additional data sources
- **Interactive Tools**: Accessible to non-technical stakeholders

### For Law Enforcement
- **Performance Insights**: Understanding arrest success factors
- **Resource Optimization**: Data-driven resource allocation
- **Policy Development**: Evidence-based policy recommendations
- **Transparency**: Public access to analysis tools

### For Researchers
- **Data Access**: Clean, standardized data access
- **Analysis Tools**: Built-in EDA and visualization capabilities
- **Modeling Foundation**: Ready for predictive modeling
- **Documentation**: Comprehensive metadata and documentation

## Future Enhancements

### Short-term
1. **Authentication**: User access controls
2. **Export Features**: CSV/Excel data export
3. **Advanced Filtering**: Complex query builder
4. **Real-time Updates**: Live data refresh capabilities

### Long-term
1. **Machine Learning Integration**: Predictive model deployment
2. **Database Backend**: Persistent data storage
3. **API Rate Limiting**: Production-ready access controls
4. **Mobile Interface**: Responsive design for mobile devices

## Conclusion

The ATPA MCP Server successfully addresses NMInsights' research questions by providing:

1. **Comprehensive Data Integration**: Seamlessly combines incidents and arrestee data
2. **Target Variable Creation**: Establishes ARREST as the primary outcome variable
3. **Interactive Analysis Tools**: Enables exploration of arrest patterns
4. **Business Intelligence**: Supports data-driven decision making
5. **Scalable Architecture**: Ready for production deployment

The server serves as both a research tool for NMInsights and a foundation for future predictive modeling tasks in the ATPA assessment, enabling systematic analysis of the factors that influence arrest outcomes in New Mexico's criminal justice system. 