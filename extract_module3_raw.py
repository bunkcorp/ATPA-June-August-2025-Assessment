#!/usr/bin/env python3
"""
Extract Module 3 using raw bytes approach
"""

import json
import re
from pathlib import Path
import subprocess

def extract_with_antiword_direct(doc_path):
    """Use antiword directly with error handling"""
    try:
        # Try antiword directly with different options
        result = subprocess.run(
            ['antiword', doc_path], 
            capture_output=True, 
            text=False  # Get bytes
        )
        
        if result.returncode == 0:
            # Try different encodings on the raw bytes
            encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1', 'utf-16']
            
            for encoding in encodings:
                try:
                    text = result.stdout.decode(encoding, errors='ignore')
                    if len(text) > 1000:  # Must be substantial content
                        print(f"✅ Success with antiword + {encoding}: {len(text)} characters")
                        return text, encoding
                except Exception as e:
                    continue
        
        print(f"❌ Antiword failed with return code: {result.returncode}")
        return None, None
        
    except Exception as e:
        print(f"❌ Antiword execution failed: {e}")
        return None, None

def extract_with_strings(doc_path):
    """Extract readable strings from the binary file"""
    try:
        result = subprocess.run(
            ['strings', doc_path], 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode == 0 and len(result.stdout) > 1000:
            print(f"✅ Strings extraction: {len(result.stdout)} characters")
            return result.stdout, 'strings'
        
        return None, None
        
    except Exception as e:
        print(f"❌ Strings extraction failed: {e}")
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
    
    print("Trying different extraction methods for Module 3...")
    
    # Try antiword directly
    print("\n1. Trying antiword directly...")
    text, method = extract_with_antiword_direct(doc_path)
    
    # If that fails, try strings
    if not text:
        print("\n2. Trying strings extraction...")
        text, method = extract_with_strings(doc_path)
    
    if not text:
        print("❌ All extraction methods failed")
        return
    
    print(f"✅ Successfully extracted with method: {method}")
    
    # Clean up the text a bit
    # Remove excessive whitespace and clean control characters
    text = re.sub(r'\x00+', ' ', text)  # Remove null bytes
    text = re.sub(r'[\x01-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', text)  # Remove control chars
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)  # Normalize line breaks
    
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
    print(f"   Method: {method}")

if __name__ == "__main__":
    main()