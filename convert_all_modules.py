#!/usr/bin/env python3
"""
Extract content from all ATPA module documents
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
        print(f"Error extracting {doc_path}: {e}")
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
        if (re.match(r'^\d+(\.\d+)*\s+', line) or  # 2.1 Section
            re.match(r'^Module\s+\d+', line, re.IGNORECASE) or  # Module 2
            re.match(r'^Section\s+\d+', line, re.IGNORECASE) or  # Section 2
            re.match(r'^\d+(\.\d+)*\.\d+\s+', line) or  # 2.1.1 Section
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

def process_module(doc_path, module_name):
    """Process a single module document"""
    print(f"\n{'='*60}")
    print(f"Processing {module_name}")
    print(f"{'='*60}")
    print(f"File: {doc_path}")
    
    # Extract text
    text = extract_text_with_textract(doc_path)
    if not text:
        print(f"❌ Failed to extract text from {module_name}")
        return
    
    print(f"✅ Extracted {len(text):,} characters")
    
    # Structure content
    sections = structure_content(text)
    print(f"✅ Found {len(sections)} sections")
    
    # Save results
    base_path = Path(doc_path).parent
    module_prefix = f"ATPA_{module_name.replace(' ', '_')}"
    
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
    
    print(f"📁 Files created:")
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
    
    return {
        'module': module_name,
        'characters': len(text),
        'sections': len(sections),
        'files': {
            'raw': str(raw_file),
            'json': str(json_file),
            'markdown': str(md_file)
        },
        'first_sections': list(sections.keys())[:10]
    }

def main():
    modules = [
        {
            'path': "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_2_Working_with_Data/ATPA_Module_2_document.doc",
            'name': "Module_2_Working_with_Data"
        },
        {
            'path': "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_3_Advanced_Models/ATPA_Module_3_document.doc", 
            'name': "Module_3_Advanced_Models"
        },
        {
            'path': "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_4_Model_Explainability/ATPA_Module_4_document.doc",
            'name': "Module_4_Model_Explainability"
        }
    ]
    
    results = []
    
    for module in modules:
        try:
            result = process_module(module['path'], module['name'])
            if result:
                results.append(result)
        except Exception as e:
            print(f"❌ Error processing {module['name']}: {e}")
    
    # Summary
    print(f"\n{'='*60}")
    print("EXTRACTION SUMMARY")
    print(f"{'='*60}")
    
    total_chars = 0
    total_sections = 0
    
    for result in results:
        total_chars += result['characters']
        total_sections += result['sections']
        print(f"\n📚 {result['module']}:")
        print(f"   Characters: {result['characters']:,}")
        print(f"   Sections: {result['sections']}")
        print(f"   Files: Raw, JSON, Markdown")
    
    print(f"\n🎯 TOTALS:")
    print(f"   Modules processed: {len(results)}")
    print(f"   Total characters: {total_chars:,}")
    print(f"   Total sections: {total_sections}")
    print(f"   Total files created: {len(results) * 3}")
    
    # Save summary
    summary_file = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/extraction_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump({
            'extraction_date': '2025-08-01',
            'modules_processed': len(results),
            'total_characters': total_chars,
            'total_sections': total_sections,
            'modules': results
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 Summary saved to: {summary_file}")

if __name__ == "__main__":
    main()