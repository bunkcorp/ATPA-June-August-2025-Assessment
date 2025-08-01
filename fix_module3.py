#!/usr/bin/env python3
"""
Fix Module 3 extraction with different encoding approaches
"""

import json
import re
from pathlib import Path
import textract

def extract_with_different_encodings(doc_path):
    """Try different encodings to extract text"""
    encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            print(f"Trying encoding: {encoding}")
            text = textract.process(doc_path).decode(encoding, errors='ignore')
            print(f"✅ Success with {encoding}: {len(text)} characters")
            return text, encoding
        except Exception as e:
            print(f"❌ Failed with {encoding}: {e}")
            continue
    
    return None, None

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
        if (re.match(r'^\d+(\.\d+)*\s+', line) or  # 3.1 Section
            re.match(r'^Module\s+\d+', line, re.IGNORECASE) or  # Module 3
            re.match(r'^Section\s+\d+', line, re.IGNORECASE) or  # Section 3
            re.match(r'^\d+(\.\d+)*\.\d+\s+', line) or  # 3.1.1 Section
            (line.isupper() and len(line) > 5 and len(line) < 100)):  # ALL CAPS headings
            
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
    doc_path = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_3_Advanced_Models/ATPA_Module_3_document.doc"
    
    print("Attempting to extract Module 3 with different encodings...")
    
    text, encoding = extract_with_different_encodings(doc_path)
    
    if not text:
        print("❌ All encoding attempts failed")
        return
    
    print(f"✅ Successfully extracted with {encoding}")
    
    # Structure content
    sections = structure_content(text)
    print(f"✅ Found {len(sections)} sections")
    
    # Save results
    base_path = Path(doc_path).parent
    module_prefix = "ATPA_Module_3_Advanced_Models"
    
    # Save raw text
    raw_file = base_path / f"{module_prefix}_raw_text.txt"
    with open(raw_file, "w", encoding="utf-8") as f:
        f.write(text)
    
    # Save structured JSON
    json_file = base_path / f"{module_prefix}_sections.json"
    with open(json_file, "w", encoding="utf-8") as f:
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
    
    md_file = base_path / f"{module_prefix}_content.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write('\n'.join(markdown_content))
    
    print(f"\n📁 Files created:")
    print(f"   Raw text: {raw_file}")
    print(f"   JSON: {json_file}")
    print(f"   Markdown: {md_file}")
    
    # Show preview
    print(f"\n📝 First 500 characters:")
    print(text[:500] + "..." if len(text) > 500 else text)
    
    print(f"\n📋 First 10 sections:")
    for i, section in enumerate(list(sections.keys())[:10]):
        print(f"   {i+1}. {section}")
        if i >= 9 and len(sections) > 10:
            print(f"   ... and {len(sections) - 10} more")
            break
    
    print(f"\n✅ Module 3 extraction completed!")
    print(f"   Characters: {len(text):,}")
    print(f"   Sections: {len(sections)}")
    print(f"   Encoding used: {encoding}")

if __name__ == "__main__":
    main()