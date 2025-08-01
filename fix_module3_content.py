#!/usr/bin/env python3
"""
Re-extract Module 3 with better content parsing
"""

import json
import re
from pathlib import Path

def extract_content_properly(text):
    """Extract actual content, not just titles"""
    
    # First, let's try to identify content blocks vs just navigation
    lines = text.split('\n')
    
    sections = {}
    current_section = None
    current_content = []
    
    # Look for actual content paragraphs, not just titles
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip pure navigation/contents lines
        if re.match(r'^Contents$|^ATPA Module \d+$', line):
            continue
            
        # Detect section headers (with substantial text, not just numbers)
        if re.match(r'^\d+\.\d+(\.\d+)?\s+[A-Za-z].*', line) and len(line.split()) >= 3:
            # This looks like a real section header
            
            # Save previous section
            if current_section and current_content:
                content_text = ' '.join(current_content)
                if len(content_text) > 50:  # Only save if substantial content
                    sections[current_section] = content_text
            
            current_section = line
            current_content = []
            
        elif current_section:
            # Look ahead to see if this is actual content
            next_lines = lines[i:i+5] if i < len(lines)-5 else lines[i:]
            
            # Skip if this line looks like just a page number or navigation
            if re.match(r'^\d+$', line) or len(line) < 10:
                continue
                
            # Check if we have substantial content in the next few lines
            substantial_content = any(len(next_line.strip()) > 20 for next_line in next_lines[1:])
            
            if substantial_content or len(line) > 20:
                current_content.append(line)
    
    # Save final section
    if current_section and current_content:
        content_text = ' '.join(current_content)
        if len(content_text) > 50:
            sections[current_section] = content_text
    
    return sections

def try_alternative_parsing(text):
    """Try parsing by looking for paragraph blocks"""
    
    # Split into potential paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    
    sections = {}
    current_section = "Introduction"
    
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 30:
            continue
            
        # Check if this starts with a section number
        if re.match(r'^\d+\.\d+(\.\d+)?\s+[A-Za-z]', para):
            lines = para.split('\n')
            if len(lines) > 1:
                # First line is section header, rest is content
                header = lines[0].strip()
                content = ' '.join(lines[1:]).strip()
                
                if len(content) > 50:
                    sections[header] = content
            else:
                # Just a header, wait for content
                current_section = para
        elif current_section and len(para) > 50:
            # This is content for the current section
            if current_section in sections:
                sections[current_section] += " " + para
            else:
                sections[current_section] = para
    
    return sections

def main():
    # Read the raw text
    raw_file = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/Module_3_Advanced_Models/ATPA_Module_3_Advanced_Models_raw_text.txt"
    
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"Re-processing Module 3 text ({len(text):,} characters)...")
    
    # Try the first approach
    sections1 = extract_content_properly(text)
    print(f"Method 1: Found {len(sections1)} sections with content")
    
    # Try alternative approach
    sections2 = try_alternative_parsing(text)
    print(f"Method 2: Found {len(sections2)} sections with content")
    
    # Use whichever found more substantial content
    if len(sections2) > len(sections1):
        sections = sections2
        method = "paragraph-based parsing"
    else:
        sections = sections1
        method = "line-based parsing"
    
    print(f"Using {method} with {len(sections)} sections")
    
    # Show sample of what we found
    print(f"\nSample content preview:")
    for i, (title, content) in enumerate(list(sections.items())[:3]):
        print(f"\nSection: {title}")
        print(f"Content ({len(content)} chars): {content[:200]}...")
        
        if i >= 2:
            break
    
    if len(sections) == 0 or all(len(content) < 100 for content in sections.values()):
        print("❌ Still not getting good content. Let me try raw text analysis...")
        
        # Show some samples of the raw text to understand structure
        print(f"\nRaw text sample (first 2000 chars):")
        print(text[:2000])
        
        print(f"\nLooking for content patterns...")
        # Look for common patterns that indicate actual content
        content_indicators = [
            "example", "model", "regression", "data", "analysis", 
            "equation", "formula", "algorithm", "method", "approach"
        ]
        
        for indicator in content_indicators:
            matches = re.findall(f'.{{0,100}}{indicator}.{{0,100}}', text, re.IGNORECASE)
            if matches:
                print(f"\nFound '{indicator}' context:")
                print(matches[0][:200] + "...")
                break
        
        return
    
    # Save the improved results
    base_path = Path(raw_file).parent
    
    # Update structured JSON
    json_file = base_path / "ATPA_Module_3_Advanced_Models_sections.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
    
    # Update markdown
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
    
    print(f"\n✅ Updated Module 3 files with actual content!")
    print(f"   Sections with content: {len(sections)}")
    print(f"   Average content length: {sum(len(c) for c in sections.values()) // len(sections):,} chars")
    
    # Copy updated files to organized folder
    organized_base = "/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA_Extracted_Content/Module_3_Advanced_Models"
    
    import shutil
    shutil.copy2(str(json_file), organized_base)
    shutil.copy2(str(md_file), organized_base)
    
    print(f"✅ Updated files copied to organized folder")

if __name__ == "__main__":
    main()