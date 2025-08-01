#!/usr/bin/env python3
"""
Enhanced script to extract detailed course content including learning objectives.
"""

import json
import re
from html import unescape

def extract_learning_objectives(content):
    """Extract specific learning objectives from HTML content."""
    objectives = []
    
    # Look for list items with educational content
    patterns = [
        r'<li[^>]*>(Apply.*?)</li>',
        r'<li[^>]*>(Discuss.*?)</li>',
        r'<li[^>]*>(Reinforce.*?)</li>',
        r'<li[^>]*>(Identify.*?)</li>',
        r'<li[^>]*>(Understand.*?)</li>',
        r'<li[^>]*>(Explain.*?)</li>',
        r'<li[^>]*>(Demonstrate.*?)</li>',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        for match in matches:
            # Clean the HTML
            clean_text = re.sub(r'<[^>]+>', '', match)
            clean_text = re.sub(r'\s+', ' ', clean_text)
            clean_text = unescape(clean_text).strip()
            if len(clean_text) > 10 and 'webkit' not in clean_text.lower() and 'yui-gen' not in clean_text:
                objectives.append(clean_text)
    
    return list(set(objectives))  # Remove duplicates

def main():
    print("Reading original file to extract detailed learning content...")
    
    with open('/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA_course_structure.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Extracting learning objectives...")
    objectives = extract_learning_objectives(content)
    
    # Also look for other educational content
    case_studies = re.findall(r'case study[^<]*', content, re.IGNORECASE)
    examples = re.findall(r'Example[^<"]*', content, re.IGNORECASE)
    
    print("\n=== DETAILED LEARNING OBJECTIVES ===")
    for i, obj in enumerate(objectives, 1):
        print(f"{i}. {obj}")
    
    print(f"\n=== EXAMPLES FOUND ===")
    unique_examples = list(set([ex.strip() for ex in examples if len(ex.strip()) > 5]))
    for example in unique_examples[:10]:  # Limit output
        print(f"• {example}")
    
    print(f"\n=== CASE STUDIES ===")
    unique_cases = list(set([case.strip() for case in case_studies if len(case.strip()) > 5]))
    for case in unique_cases[:5]:  # Limit output
        print(f"• {case}")
    
    # Create a detailed summary file
    summary = {
        "course_title": "ATPA Module 1 - Data and Model Ethics",
        "learning_objectives": objectives,
        "examples": unique_examples[:10],
        "case_studies": unique_cases[:5],
        "module_structure": {
            "module_1": {
                "name": "Data and Model Ethics",
                "sections": [
                    "Ethical Framework",
                    "Regulations and Standards of Practice", 
                    "Case Study"
                ]
            }
        }
    }
    
    # Save detailed summary
    with open('/Users/kevinwoods/Desktop/ActuarialExams/ATPA/course_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\nDetailed summary saved to: course_summary.json")

if __name__ == "__main__":
    main()