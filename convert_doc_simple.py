#!/usr/bin/env python3
"""
Simple script to extract text from legacy .doc files using textract
"""

import json
import re
from pathlib import Path

try:
    import textract
except ImportError:
    print("textract not installed. Please run: pip install textract")
    exit(1)

def extract_text_with_textract(doc_path):
    """Extract text from .doc file using textract"""
    try:
        text = textract.process(doc_path).decode('utf-8')
        return text
    except Exception as e:
        print(f"Error extracting with textract: {e}")
        return None

def structure_content(text):
    """Structure the extracted text into sections"""
    lines = text.split('\n')
    sections = {}
    current_section = "Introduction"
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for section patterns
        if (re.match(r'^\d+(\.\d+)*\s+', line) or  # 1.1 Section
            re.match(r'^Module\s+\d+', line, re.IGNORECASE) or  # Module 1
            re.match(r'^Section\s+\d+', line, re.IGNORECASE) or  # Section 1
            line.isupper() and len(line) > 5):  # ALL CAPS headings
            
            # Save previous section
            if current_content:
                sections[current_section] = '\n'.join(current_content)
            
            # Start new section
            current_section = line
            current_content = []
        else:
            current_content.append(line)
    
    # Save final section
    if current_content:
        sections[current_section] = '\n'.join(current_content)
    
    return sections

def main():
    doc_path = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_1_Data_and_Model_Ethics/ATPA_Module_1_document.doc"
    
    print(f"Extracting text from: {doc_path}")
    
    # Extract text
    text = extract_text_with_textract(doc_path)
    if not text:
        print("Failed to extract text")
        return
    
    print(f"Extracted {len(text)} characters")
    
    # Structure content
    sections = structure_content(text)
    print(f"Found {len(sections)} sections")
    
    # Save results
    base_path = Path(doc_path).parent
    
    # Save raw text
    with open(base_path / "ATPA_Module_1_raw_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    # Save structured JSON
    with open(base_path / "ATPA_Module_1_sections.json", "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
    
    # Save markdown
    markdown_content = []
    for section, content in sections.items():
        # Determine heading level
        if re.match(r'^\d+\s+', section):
            level = 1
        elif re.match(r'^\d+\.\d+\s+', section):
            level = 2
        elif re.match(r'^\d+\.\d+\.\d+\s+', section):
            level = 3
        else:
            level = 1
        
        markdown_content.append(f"{'#' * level} {section}\n\n{content}\n\n")
    
    with open(base_path / "ATPA_Module_1_content.md", "w", encoding="utf-8") as f:
        f.write('\n'.join(markdown_content))
    
    print("✅ Files created:")
    print(f"   Raw text: {base_path}/ATPA_Module_1_raw_text.txt")
    print(f"   Structured JSON: {base_path}/ATPA_Module_1_sections.json")
    print(f"   Markdown: {base_path}/ATPA_Module_1_content.md")
    
    # Show preview
    print(f"\n📝 First 500 characters:")
    print(text[:500] + "..." if len(text) > 500 else text)
    
    print(f"\n📋 Sections found:")
    for i, section in enumerate(list(sections.keys())[:10]):
        print(f"   {i+1}. {section}")
        if i >= 9:
            print(f"   ... and {len(sections) - 10} more")
            break

if __name__ == "__main__":
    main()