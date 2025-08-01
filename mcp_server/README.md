# ATPA MCP Server

## Overview

The ATPA MCP (Model-Context-Protocol) Server is a comprehensive FastAPI application designed for interactive exploration and analysis of criminal incident and arrest data. Built specifically for the ATPA June-August 2025 assessment, this server incorporates the business context provided by NMInsights to understand:

1. **What characteristics of criminal incidents are associated with arrests?**
2. **Which types of crimes are more or less likely to lead to arrests?**

## Architecture

The server follows a layered MCP architecture:

### 1. Context Layer (`context.py`)
- **Purpose**: Load and parse the Data Dictionary Excel file
- **Functionality**: 
  - Extract variable names, types, descriptions
  - Categorize variables by source file (incidents vs arrestee)
  - Provide metadata for each variable
- **Endpoints**: `/fields`, `/fields/{field_name}`, `/fields/source/{source}`

### 2. Model Layer (`loader.py`)
- **Purpose**: Load and clean incidents.csv and arrestee.csv
- **Functionality**:
  - Standardize column names
  - Parse data types (dates, numbers, categories)
  - Handle missing values
  - Provide paginated data access with filtering
- **Endpoints**: `/data/incidents`, `/data/arrestee`, `/data/summary`

### 3. Protocol Layer (`protocol.py`)
- **Purpose**: Merge datasets and create ARREST target variable
- **Functionality**:
  - Merge incidents and arrestee datasets using INCIDENT_ID
  - Handle imperfect matching (not every incident has an arrest)
  - Create binary target: ARREST = 1 if matched to arrestee data, 0 otherwise
  - Add derived features (time-based, categorical, etc.)
- **Endpoints**: `/merged/create`, `/merged/data`, `/merged/summary`, `/merged/arrest-analysis`

### 4. Insights Layer (`insights.py`)
- **Purpose**: Exploratory Data Analysis and visualization
- **Functionality**:
  - Summary statistics
  - Arrest rate analysis by crime type
  - Temporal patterns (hourly, daily, monthly)
  - Correlation analysis
  - Feature importance for arrest prediction
  - Data quality and reasonability checks
- **Endpoints**: `/eda/summary`, `/eda/arrest-rate-viz`, `/eda/temporal-analysis`, etc.

### 5. Ethics Layer (`ethics.py`)
- **Purpose**: ATPA Module 1 Data and Model Ethics framework integration
- **Functionality**:
  - Protected class identification and monitoring
  - Bias assessment (selection, measurement, representation)
  - Fairness metrics calculation (demographic parity)
  - Ethical recommendations generation
  - Compliance checklist (ASOPs, regulations)
  - Risk assessment for criminal justice context
- **Endpoints**: `/ethics/framework`, `/ethics/bias-assessment`, `/ethics/fairness-metrics`, etc.

## Installation

1. **Navigate to the MCP server directory**:
   ```bash
   cd mcp_server
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify data files exist**:
   - `../Task1_DataPrep/Data_Dictionary.xlsx`
   - `../Task1_DataPrep/incidents.csv`
   - `../Task1_DataPrep/arrestee.csv`

## Usage

### Starting the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

### API Endpoints

#### Context Layer
- `GET /fields` - Get metadata for all fields
- `GET /fields/{field_name}` - Get metadata for specific field
- `GET /fields/source/{source}` - Get fields by source file

#### Model Layer
- `GET /data/incidents` - Get incidents data (paginated)
- `GET /data/arrestee` - Get arrestee data (paginated)
- `GET /data/summary` - Get data summary statistics

#### Protocol Layer
- `POST /merged/create` - Create merged dataset with ARREST target
- `GET /merged/data` - Get merged data (paginated)
- `GET /merged/summary` - Get merged dataset summary
- `GET /merged/arrest-analysis` - Get detailed arrest pattern analysis

#### Insights Layer
- `GET /eda/summary` - Get comprehensive EDA summary
- `GET /eda/arrest-rate-viz` - Get arrest rate visualization
- `GET /eda/temporal-analysis` - Get temporal analysis
- `GET /eda/correlation-analysis` - Get correlation analysis
- `GET /eda/feature-importance` - Get feature importance analysis
- `GET /eda/reasonability-checks` - Get data quality checks

#### Ethics Layer
- `GET /ethics/framework` - Get ATPA Module 1 ethics framework
- `GET /ethics/protected-variables` - Identify protected variables
- `GET /ethics/bias-assessment` - Get comprehensive bias assessment
- `GET /ethics/fairness-metrics` - Get fairness metrics for ARREST target
- `GET /ethics/recommendations` - Get ethical recommendations
- `GET /ethics/summary` - Get comprehensive ethical summary
- `GET /ethics/compliance-checklist` - Get ATPA compliance checklist

#### Utility
- `GET /` - Server information
- `GET /health` - Health check
- `GET /docs` - API documentation
- `GET /dashboard` - Interactive web dashboard
- `GET /api/status` - Server status

### Web Dashboard

Access the interactive dashboard at `http://localhost:8000/dashboard` to:

- View server status and data availability
- Create merged datasets
- Explore summary statistics
- View interactive visualizations
- Perform data quality checks
- Browse API documentation

## Data Processing Pipeline

### 1. Data Loading
- **Large File Handling**: Uses chunked reading for large CSV files
- **Sampling**: Optional sampling for development/testing
- **Error Handling**: Graceful fallbacks for missing files

### 2. Data Cleaning
- **Column Standardization**: Convert to snake_case
- **Type Conversion**: 
  - Dates: Parse incident_date, arrest_date, etc.
  - Numbers: Convert numeric columns
  - Categories: Handle categorical variables
  - Booleans: Standardize flag columns
- **Missing Values**: Identify and document missing data patterns

### 3. Data Merging
- **Primary Key**: Use INCIDENT_ID for merging
- **Join Strategy**: Left join to preserve all incidents
- **Target Creation**: ARREST = 1 if incident appears in arrestee data
- **Multiple Arrests**: Handle cases with multiple arrests per incident

### 4. Feature Engineering
- **Time Features**: Days between incident and arrest
- **Categorical Features**: Age categories, agency size, crime severity
- **Temporal Categories**: Hour categories, day of week
- **Geographic Features**: Agency size based on population

## Business Context Integration

The server is designed around NMInsights' research questions:

### Research Question 1: Incident Characteristics Associated with Arrests
- **Analysis**: Feature importance analysis
- **Visualization**: Correlation with arrest target
- **Insights**: Which variables most strongly predict arrest outcomes

### Research Question 2: Crime Types and Arrest Likelihood
- **Analysis**: Arrest rate by offense category
- **Visualization**: Bar charts of arrest rates by crime type
- **Insights**: Which crimes have higher/lower arrest rates

## Data Quality Features

### Reasonability Checks
- **Data Volume**: Verify reasonable arrest rates (1-50%)
- **Date Ranges**: Check for logical date sequences
- **Outliers**: Identify statistical outliers
- **Missing Data**: Document missing data patterns
- **Logical Consistency**: Check for impossible values

### Data Completeness
- **Missing Value Analysis**: Percentage missing by column
- **Duplicate Detection**: Identify duplicate incidents
- **Data Type Validation**: Ensure proper data types

## Performance Considerations

### Memory Management
- **Chunked Reading**: Handle large files without loading entire dataset
- **Sampling**: Optional sampling for development
- **Lazy Loading**: Load data only when needed

### Scalability
- **Pagination**: All data endpoints support pagination
- **Filtering**: Support for column-based filtering
- **Caching**: Consider adding Redis for production

## Development Workflow

### 1. Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start server
python main.py
```

### 2. Data Exploration
```bash
# Check server status
curl http://localhost:8000/api/status

# Create merged dataset
curl -X POST "http://localhost:8000/merged/create?sample_size=10000"

# Get summary statistics
curl http://localhost:8000/eda/summary
```

### 3. Interactive Analysis
- Open `http://localhost:8000/dashboard`
- Use the web interface for exploration
- View interactive visualizations

## API Examples

### Create Merged Dataset
```bash
curl -X POST "http://localhost:8000/merged/create?sample_size=10000"
```

### Get Arrest Analysis
```bash
curl http://localhost:8000/merged/arrest-analysis
```

### Get Paginated Data
```bash
curl "http://localhost:8000/merged/data?page=1&page_size=100"
```

### Get Field Metadata
```bash
curl http://localhost:8000/fields/incident_id
```

## File Structure

```
mcp_server/
├── main.py              # FastAPI application entry point
├── context.py           # Context layer - data dictionary handling
├── loader.py            # Model layer - data loading and cleaning
├── protocol.py          # Protocol layer - data merging and target creation
├── insights.py          # Insights layer - EDA and visualization
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── templates/
│   └── dashboard.html   # Web dashboard template
└── static/             # Static files (CSS, JS)
```

## Troubleshooting

### Common Issues

1. **Data Files Not Found**
   - Verify paths in `main.py` match your file structure
   - Check file permissions

2. **Memory Issues with Large Files**
   - Use sampling: `?sample_size=10000`
   - Increase system memory or use chunked processing

3. **Missing Dependencies**
   - Run `pip install -r requirements.txt`
   - Check Python version compatibility

4. **Port Already in Use**
   - Change port in `main.py` or kill existing process
   - Use `lsof -i :8000` to find process using port

### Logging

The server uses Python's logging module. Check console output for:
- Data loading progress
- Error messages
- Performance metrics

## Future Enhancements

### Potential Improvements
1. **Authentication**: Add user authentication for production
2. **Database Integration**: Use PostgreSQL for persistent storage
3. **Real-time Updates**: WebSocket support for live data updates
4. **Advanced Analytics**: Machine learning model integration
5. **Export Features**: CSV/Excel export capabilities
6. **Advanced Filtering**: Complex query builder interface

### Production Deployment
1. **Docker**: Containerize the application
2. **Load Balancing**: Use nginx for multiple instances
3. **Monitoring**: Add health checks and metrics
4. **Security**: Implement proper authentication and authorization

## Contributing

1. Follow the existing code structure
2. Add appropriate error handling
3. Include docstrings for new functions
4. Test with sample data before committing
5. Update documentation for new features

## License

This project is developed for educational purposes as part of the ATPA assessment. 