#!/usr/bin/env python3
"""
Fix Module 3 section parsing
"""

import json
import re
from pathlib import Path

def better_structure_content(text):
    """Better structure parsing for Module 3 format"""
    # Split by potential section markers
    sections = {}
    
    # Look for patterns like "1.1.1 Module 3 Learning Objectives"
    pattern = r'(\d+\.\d+\.\d+\s+[^\d][^\.]*?)(?=\d+\.\d+\.\d+\s|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    
    if not matches:
        # Try simpler pattern
        pattern = r'(\d+\.\d+\s+[^\d][^\.]*?)(?=\d+\.\d+\s|$)'
        matches = re.findall(pattern, text, re.DOTALL)
    
    if not matches:
        # Try even simpler - split on numbers followed by titles
        lines = text.split('\n')
        current_section = "Introduction"
        current_content = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Look for section patterns
            if re.match(r'^\d+\.\d+(\.\d+)?\s+[A-Za-z]', line):
                # Save previous section
                if current_content:
                    sections[current_section] = ' '.join(current_content)
                
                # Extract section title (first reasonable part)
                parts = line.split()
                if len(parts) > 1:
                    current_section = ' '.join(parts[:6])  # Take first few words
                    current_content = [' '.join(parts[6:])] if len(parts) > 6 else []
                else:
                    current_section = line
                    current_content = []
            else:
                current_content.append(line)
        
        # Save final section
        if current_content:
            sections[current_section] = ' '.join(current_content)
    
    else:
        for i, match in enumerate(matches):
            # Extract section number and title
            lines = match.strip().split('\n')
            first_line = lines[0].strip()
            
            # Get section title
            title_match = re.match(r'(\d+\.\d+(\.\d+)?\s+[^0-9]+)', first_line)
            if title_match:
                section_title = title_match.group(1).strip()
                content = match.strip()
            else:
                section_title = f"Section {i+1}"
                content = match.strip()
            
            sections[section_title] = content
    
    return sections

def main():
    # Read the existing raw text
    raw_file = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_3_Advanced_Models/ATPA_Module_3_Advanced_Models_raw_text.txt"
    
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"Re-parsing Module 3 text ({len(text):,} characters)...")
    
    # Better structure content
    sections = better_structure_content(text)
    print(f"✅ Found {len(sections)} sections")
    
    # Save updated structured JSON
    base_path = Path(raw_file).parent
    json_file = base_path / "ATPA_Module_3_Advanced_Models_sections.json"
    
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
    
    # Save updated markdown
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
    
    md_file = base_path / "ATPA_Module_3_Advanced_Models_content.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write('\n'.join(markdown_content))
    
    print(f"\n📁 Updated files:")
    print(f"   JSON: {json_file}")
    print(f"   Markdown: {md_file}")
    
    print(f"\n📋 Sections found:")
    for i, section in enumerate(list(sections.keys())[:15]):
        print(f"   {i+1}. {section}")
        if i >= 14 and len(sections) > 15:
            print(f"   ... and {len(sections) - 15} more")
            break
    
    print(f"\n✅ Module 3 section parsing completed!")
    print(f"   Total sections: {len(sections)}")

if __name__ == "__main__":
    main()