"""
Context Layer: Load and parse Data Dictionary to provide metadata for variables
"""
import pandas as pd
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class DataContext:
    def __init__(self, data_dict_path: str):
        """
        Initialize DataContext with path to Data Dictionary Excel file
        
        Args:
            data_dict_path: Path to Data_Dictionary.xlsx file
        """
        self.data_dict_path = data_dict_path
        self.field_metadata = {}
        self.incident_fields = []
        self.arrestee_fields = []
        self._load_data_dictionary()
    
    def _load_data_dictionary(self):
        """Load and parse the Data Dictionary Excel file"""
        try:
            # Read the Excel file
            df = pd.read_excel(self.data_dict_path)
            
            # Process each row to extract field metadata
            for _, row in df.iterrows():
                field_info = {
                    'variable_name': str(row.get('Variable Name', '')).strip(),
                    'data_type': str(row.get('Data Type', '')).strip(),
                    'description': str(row.get('Description', '')).strip(),
                    'source_file': str(row.get('Source File', '')).strip(),
                    'valid_values': str(row.get('Valid Values', '')).strip(),
                    'missing_values': str(row.get('Missing Values', '')).strip(),
                    'notes': str(row.get('Notes', '')).strip()
                }
                
                # Clean up the field name
                field_name = field_info['variable_name']
                if field_name and field_name != 'nan':
                    self.field_metadata[field_name] = field_info
                    
                    # Categorize by source file
                    source_file = field_info['source_file'].lower()
                    if 'incident' in source_file:
                        self.incident_fields.append(field_name)
                    elif 'arrestee' in source_file:
                        self.arrestee_fields.append(field_name)
            
            logger.info(f"Loaded {len(self.field_metadata)} fields from data dictionary")
            logger.info(f"Incident fields: {len(self.incident_fields)}")
            logger.info(f"Arrestee fields: {len(self.arrestee_fields)}")
            
        except Exception as e:
            logger.error(f"Error loading data dictionary: {e}")
            # Create fallback metadata based on CSV headers
            self._create_fallback_metadata()
    
    def _create_fallback_metadata(self):
        """Create fallback metadata if Excel file cannot be loaded"""
        logger.warning("Creating fallback metadata from CSV headers")
        
        # Common field patterns
        incident_patterns = [
            'incident_id', 'data_year', 'agency_id', 'offense_code', 
            'crime_against', 'offense_category_name', 'victim', 'offender'
        ]
        
        arrestee_patterns = [
            'arrestee_id', 'incident_id', 'arrest_date', 'arrest_type_name',
            'offense_code', 'age', 'sex', 'race', 'ethnicity'
        ]
        
        # This will be populated when actual data is loaded
        self.incident_fields = incident_patterns
        self.arrestee_fields = arrestee_patterns
    
    def get_field_metadata(self, field_name: str) -> Optional[Dict]:
        """Get metadata for a specific field"""
        return self.field_metadata.get(field_name)
    
    def get_all_fields(self) -> Dict[str, Dict]:
        """Get metadata for all fields"""
        return self.field_metadata
    
    def get_incident_fields(self) -> List[str]:
        """Get list of fields from incidents dataset"""
        return self.incident_fields
    
    def get_arrestee_fields(self) -> List[str]:
        """Get list of fields from arrestee dataset"""
        return self.arrestee_fields
    
    def get_fields_by_source(self, source: str) -> List[Dict]:
        """Get all fields from a specific source file"""
        source_lower = source.lower()
        if 'incident' in source_lower:
            return [self.field_metadata.get(field, {}) for field in self.incident_fields]
        elif 'arrestee' in source_lower:
            return [self.field_metadata.get(field, {}) for field in self.arrestee_fields]
        else:
            return []
    
    def get_field_summary(self) -> Dict:
        """Get summary statistics about fields"""
        return {
            'total_fields': len(self.field_metadata),
            'incident_fields': len(self.incident_fields),
            'arrestee_fields': len(self.arrestee_fields),
            'common_fields': list(set(self.incident_fields) & set(self.arrestee_fields)),
            'data_types': self._get_data_type_summary()
        }
    
    def _get_data_type_summary(self) -> Dict:
        """Get summary of data types"""
        type_counts = {}
        for field_info in self.field_metadata.values():
            data_type = field_info.get('data_type', 'Unknown')
            type_counts[data_type] = type_counts.get(data_type, 0) + 1
        return type_counts 