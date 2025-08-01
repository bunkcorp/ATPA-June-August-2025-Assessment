#!/usr/bin/env python3
"""
Final fix for Module 3 - parse the continuous stream properly
"""

import json
import re
from pathlib import Path

def parse_continuous_stream(text):
    """Parse the continuous stream text properly"""
    
    sections = {}
    
    # The text appears to be: "title page_num title page_num ... actual_content"
    # Let's split into the table of contents and actual content
    
    # Find where actual content starts (after the learning objectives table)
    content_start = text.find("Module 3 [pic]")
    if content_start == -1:
        content_start = text.find("1.1.2 Section 3.1")
    
    if content_start == -1:
        print("Could not find content start")
        return {}
    
    actual_content = text[content_start:]
    
    # Split by section numbers followed by text
    pattern = r'(\d+\.\d+\.\d+\s+[^0-9][^\d]+?)(?=\d+\.\d+\.\d+\s+[^0-9]|$)'
    matches = re.findall(pattern, actual_content, re.DOTALL)
    
    if not matches:
        # Try simpler pattern
        pattern = r'(\d+\.\d+\s+[^0-9][^\d]+?)(?=\d+\.\d+\s+[^0-9]|$)'
        matches = re.findall(pattern, actual_content, re.DOTALL)
    
    for match in matches:
        lines = match.strip().split('\n')
        
        # First line should be the section header
        if lines:
            header_line = lines[0].strip()
            
            # Extract just the section number and title (not page numbers)
            header_match = re.match(r'(\d+\.\d+(\.\d+)?\s+[^0-9][^|]*)', header_line)
            if header_match:
                section_title = header_match.group(1).strip()
                
                # Get the content (everything after the header)
                content_lines = []
                for line in lines[1:]:
                    line = line.strip()
                    if line and not re.match(r'^\d+$', line):  # Skip standalone page numbers
                        content_lines.append(line)
                
                content = ' '.join(content_lines).strip()
                
                if len(content) > 30:  # Only include if substantial content
                    sections[section_title] = content
    
    # If that didn't work well, try manual extraction for key sections
    if len(sections) < 10:
        print("Automatic parsing didn't work well, trying manual extraction...")
        
        # Look for key content patterns
        key_sections = {
            "1.1.3 Software for Module 3": r"Python currently has great functionality.*?Software for Module 3",
            "1.1.4 Introduction": r"As part of Exams SRM and PA.*?Introduction",
            "1.1.5 Purposes of a Model": r"A perfectly fit and perfectly tuned model.*?Purposes of a Model",
            "1.1.6 Model Workflow": r"There are many steps to build a model.*?Model Workflow",
            "1.1.7 Safety in the Context of Analytics": r"In the context of analytics, safety relates.*?Safety in the Context of Analytics",
            "1.2.2 Introduction": r"Generalized additive models are an extension.*?Introduction",
            "1.2.3 Motivating Example": r"We begin our discussion of additive models.*?Motivating Example",
        }
        
        for section_title, pattern in key_sections.items():
            match = re.search(pattern, text, re.DOTALL)
            if match:
                content = match.group(0).replace(section_title.split()[-1], "").strip()
                if len(content) > 50:
                    sections[section_title] = content
    
    return sections

def main():
    # Read the raw text
    raw_file = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_3_Advanced_Models/ATPA_Module_3_Advanced_Models_raw_text.txt"
    
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"Processing Module 3 text ({len(text):,} characters)...")
    
    sections = parse_continuous_stream(text)
    
    print(f"Extracted {len(sections)} sections with content")
    
    # Show what we found
    if sections:
        print(f"\nSections extracted:")
        for i, (title, content) in enumerate(list(sections.items())[:10]):
            print(f"{i+1}. {title} ({len(content)} chars)")
            if len(content) > 100:
                print(f"   Preview: {content[:100]}...")
            else:
                print(f"   Content: {content}")
            print()
    else:
        print("❌ No content extracted successfully")
        return
    
    # Save results
    base_path = Path(raw_file).parent
    
    # Save JSON
    json_file = base_path / "ATPA_Module_3_Advanced_Models_sections.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
    
    # Save Markdown
    markdown_content = []
    for section, content in sections.items():
        if re.match(r'^\d+\s+', section):
            level = 1
        elif re.match(r'^\d+\.\d+\s+', section):
            level = 2
        elif re.match(r'^\d+\.\d+\.\d+\s+', section):
            level = 3
        else:
            level = 1
        
        markdown_content.append(f"{'#' * level} {section}\n\n{content}\n\n")
    
    md_file = base_path / "ATPA_Module_3_Advanced_Models_content.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write('\n'.join(markdown_content))
    
    # Copy to organized folder
    organized_base = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA_Extracted_Content/Module_3_Advanced_Models"
    
    import shutil
    shutil.copy2(str(json_file), organized_base)
    shutil.copy2(str(md_file), organized_base)
    
    print(f"✅ Fixed Module 3 extraction!")
    print(f"   Sections: {len(sections)}")
    print(f"   Total character count: {sum(len(content) for content in sections.values()):,}")
    print(f"   Files updated in organized folder")

if __name__ == "__main__":
    main()