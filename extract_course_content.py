#!/usr/bin/env python3
"""
Script to extract essential course content from ATPA_course_structure.js
Removes UI/styling data and focuses on educational content.
"""

import json
import re
from html import unescape

def clean_html_content(html_str):
    """Extract readable text from HTML, removing styling and formatting tags."""
    if not html_str:
        return ""
    
    # Handle specific content patterns
    if '<ul' in html_str or '<li' in html_str:
        # Extract list items
        items = re.findall(r'<li[^>]*>(.*?)</li>', html_str, re.DOTALL)
        clean_items = []
        for item in items:
            clean_item = re.sub(r'<[^>]+>', '', item)
            clean_item = re.sub(r'\s+', ' ', clean_item)
            clean_item = unescape(clean_item).strip()
            if clean_item and len(clean_item) > 3 and 'webkit' not in clean_item.lower():
                clean_items.append(clean_item)
        if clean_items:
            return clean_items
    
    # Remove HTML tags but preserve content
    text = re.sub(r'<[^>]+>', '', html_str)
    # Remove extra whitespace and HTML entities
    text = re.sub(r'\s+', ' ', text)
    text = unescape(text)
    text = text.strip()
    
    # Filter out very short or meaningless content
    if len(text) < 3 or text in ['', ' ', 'Panel Footer', 'Rich Text', 'Box']:
        return ""
    
    return text

def extract_essential_content(obj, path=""):
    """Recursively extract essential educational content."""
    essential = {}
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            current_path = f"{path}.{key}" if path else key
            
            # Key educational content fields
            if key in ['loname', 'eodesc', 'summary', 'title']:
                if value and isinstance(value, str):
                    essential[key] = value
            
            # Extract meaningful content from meta fields
            elif key == 'meta' and isinstance(value, str):
                cleaned = clean_html_content(value)
                if cleaned:
                    essential['content'] = cleaned
            
            # Also check for text content in other fields
            elif key in ['txt', 'content', 'asset_transcript', 'description'] and isinstance(value, str):
                cleaned = clean_html_content(value)
                if cleaned:
                    if key == 'asset_transcript':
                        essential['transcript'] = cleaned
                    else:
                        essential[key] = cleaned
            
            # Keep structural information
            elif key in ['modules', 'objects', 'subeos', 'elements']:
                if isinstance(value, list) and value:
                    essential[key] = [extract_essential_content(item, current_path) for item in value]
                    # Remove empty items
                    essential[key] = [item for item in essential[key] if item]
                    if not essential[key]:
                        del essential[key]
            
            # Extract specific useful fields
            elif key in ['eoorder', 'subeoorder', 'subeotype', 'elementno', 'page_title']:
                if value:
                    essential[key] = value
            
            # Recursively process nested objects
            elif isinstance(value, dict):
                nested = extract_essential_content(value, current_path)
                if nested:
                    essential[key] = nested
    
    elif isinstance(obj, list):
        return [extract_essential_content(item, path) for item in obj if item]
    
    return essential if essential else None

def main():
    # Read the original file
    print("Reading ATPA_course_structure.js...")
    with open('/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA_course_structure.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the JSON part (remove 'var courseStructure = ' prefix)
    json_start = content.find('{')
    if json_start == -1:
        print("Error: Could not find JSON data in file")
        return
    
    json_content = content[json_start:]
    
    # Parse JSON
    print("Parsing JSON structure...")
    try:
        data = json.loads(json_content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return
    
    print(f"Original file size: {len(content):,} characters")
    
    # Extract essential content
    print("Extracting essential educational content...")
    cleaned_data = extract_essential_content(data)
    
    # Create cleaned version
    cleaned_json = json.dumps(cleaned_data, indent=2, ensure_ascii=False)
    
    print(f"Cleaned content size: {len(cleaned_json):,} characters")
    print(f"Size reduction: {(1 - len(cleaned_json)/len(content))*100:.1f}%")
    
    # Write cleaned version
    output_file = '/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA_course_structure_cleaned.js'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('var courseStructure = ')
        f.write(cleaned_json)
        f.write(';')
    
    print(f"Cleaned course structure saved to: {output_file}")
    
    # Print summary
    print("\n=== COURSE STRUCTURE SUMMARY ===")
    if 'modules' in cleaned_data:
        print(f"Number of modules: {len(cleaned_data['modules'])}")
        for i, module in enumerate(cleaned_data['modules']):
            print(f"\nModule {i+1}: {module.get('loname', 'Unnamed')}")
            if 'objects' in module:
                print(f"  Learning objectives: {len(module['objects'])}")
                for j, obj in enumerate(module['objects']):
                    print(f"    {j+1}. {obj.get('eodesc', 'Unnamed objective')}")
                    if 'subeos' in obj:
                        print(f"       Sub-elements: {len(obj['subeos'])}")

if __name__ == "__main__":
    main()