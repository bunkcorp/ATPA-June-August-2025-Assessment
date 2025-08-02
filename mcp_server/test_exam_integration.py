#!/usr/bin/env python3
"""
Test Exam Integration - Assess how well the MCP server uses exam documents
"""

from exam_analysis import ExamAnalysis
import json

def test_exam_integration():
    print("=" * 80)
    print("EXAM INTEGRATION ASSESSMENT - MCP SERVER EXAM DOCUMENT USAGE")
    print("=" * 80)
    
    # Initialize exam analysis
    try:
        exam_analysis = ExamAnalysis()
        print("✅ Exam Analysis initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize Exam Analysis: {e}")
        return
    
    print("\n📋 EXAM DOCUMENT LOADING ASSESSMENT")
    print("=" * 60)
    
    # Test document loading
    print("\n1. Testing Document Loading...")
    for doc_key, doc_info in exam_analysis.exam_documents.items():
        print(f"   📄 {doc_info['title']}:")
        if doc_key in exam_analysis.document_content:
            content = exam_analysis.document_content[doc_key]
            if 'Error loading document' in content['content']:
                print(f"      ❌ Failed to load: {content['content']}")
            else:
                print(f"      ✅ Loaded successfully ({len(content['content'])} characters)")
                print(f"      📊 Tasks extracted: {len(content['tasks'])}")
                print(f"      📊 Grading criteria: {len(content['grading_criteria'])}")
                print(f"      📊 Writing patterns: {len(content['writing_patterns'])}")
                print(f"      📊 Technical requirements: {len(content['technical_requirements'])}")
        else:
            print(f"      ❌ Not found in document_content")
    
    print("\n📋 EXAM ANALYSIS FUNCTIONALITY ASSESSMENT")
    print("=" * 60)
    
    # Test exam overview
    print("\n2. Testing Exam Overview...")
    try:
        overview = exam_analysis.get_exam_overview()
        print(f"   ✅ Exam overview generated: {len(overview)} sections")
        for key, value in overview.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Exam overview failed: {e}")
    
    # Test task analysis
    print("\n3. Testing Task Analysis...")
    try:
        task_analysis = exam_analysis.get_task_analysis()
        print(f"   ✅ Task analysis generated: {len(task_analysis)} sections")
        for key, value in task_analysis.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Task analysis failed: {e}")
    
    # Test writing guidelines
    print("\n4. Testing Writing Guidelines...")
    try:
        writing_guidelines = exam_analysis.get_writing_guidelines()
        print(f"   ✅ Writing guidelines generated: {len(writing_guidelines)} sections")
        for key, value in writing_guidelines.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Writing guidelines failed: {e}")
    
    # Test technical guidelines
    print("\n5. Testing Technical Guidelines...")
    try:
        technical_guidelines = exam_analysis.get_technical_guidelines()
        print(f"   ✅ Technical guidelines generated: {len(technical_guidelines)} sections")
        for key, value in technical_guidelines.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Technical guidelines failed: {e}")
    
    # Test grading insights
    print("\n6. Testing Grading Insights...")
    try:
        grading_insights = exam_analysis.get_grading_insights()
        print(f"   ✅ Grading insights generated: {len(grading_insights)} sections")
        for key, value in grading_insights.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Grading insights failed: {e}")
    
    # Test current assignment analysis
    print("\n7. Testing Current Assignment Analysis...")
    try:
        current_assignment = exam_analysis.get_current_assignment_analysis()
        print(f"   ✅ Current assignment analysis generated: {len(current_assignment)} sections")
        for key, value in current_assignment.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Current assignment analysis failed: {e}")
    
    # Test comparative analysis
    print("\n8. Testing Comparative Analysis...")
    try:
        comparative_analysis = exam_analysis.get_comparative_analysis()
        print(f"   ✅ Comparative analysis generated: {len(comparative_analysis)} sections")
        for key, value in comparative_analysis.items():
            if isinstance(value, list):
                print(f"      📊 {key}: {len(value)} items")
            else:
                print(f"      📊 {key}: {value}")
    except Exception as e:
        print(f"   ❌ Comparative analysis failed: {e}")
    
    # Test search functionality
    print("\n9. Testing Search Functionality...")
    test_queries = ["data preparation", "model validation", "executive summary", "grading criteria"]
    for query in test_queries:
        try:
            search_results = exam_analysis.search_exam_content(query)
            print(f"   🔍 Search '{query}': {len(search_results['results'])} results")
        except Exception as e:
            print(f"   ❌ Search '{query}' failed: {e}")
    
    print("\n📊 EXAM INTEGRATION ASSESSMENT SUMMARY")
    print("=" * 60)
    
    # Assess document loading success
    loaded_docs = 0
    total_docs = len(exam_analysis.exam_documents)
    for doc_key, doc_info in exam_analysis.exam_documents.items():
        if doc_key in exam_analysis.document_content:
            content = exam_analysis.document_content[doc_key]
            if 'Error loading document' not in content['content']:
                loaded_docs += 1
    
    print(f"📄 Document Loading: {loaded_docs}/{total_docs} documents loaded successfully")
    
    # Assess functionality success
    functions_tested = 8
    functions_working = 0
    
    test_functions = [
        exam_analysis.get_exam_overview,
        exam_analysis.get_task_analysis,
        exam_analysis.get_writing_guidelines,
        exam_analysis.get_technical_guidelines,
        exam_analysis.get_grading_insights,
        exam_analysis.get_current_assignment_analysis,
        exam_analysis.get_comparative_analysis,
        exam_analysis.search_exam_content
    ]
    
    for func in test_functions:
        try:
            if func == exam_analysis.search_exam_content:
                result = func("test")
            else:
                result = func()
            if result:
                functions_working += 1
        except:
            pass
    
    print(f"🔧 Functionality: {functions_working}/{functions_tested} functions working")
    
    # Overall assessment
    loading_score = (loaded_docs / total_docs) * 100
    functionality_score = (functions_working / functions_tested) * 100
    overall_score = (loading_score + functionality_score) / 2
    
    print(f"\n📊 OVERALL ASSESSMENT SCORES:")
    print(f"   📄 Document Loading: {loading_score:.1f}%")
    print(f"   🔧 Functionality: {functionality_score:.1f}%")
    print(f"   🎯 Overall Integration: {overall_score:.1f}%")
    
    if overall_score >= 90:
        print("\n🏆 EXCELLENT: MCP server makes excellent use of exam documents")
    elif overall_score >= 75:
        print("\n✅ GOOD: MCP server makes good use of exam documents")
    elif overall_score >= 50:
        print("\n⚠️  FAIR: MCP server makes fair use of exam documents")
    else:
        print("\n❌ POOR: MCP server makes poor use of exam documents")
    
    print("\n📋 RECOMMENDATIONS:")
    if loading_score < 100:
        print("   • Fix document loading issues for missing exam files")
    if functionality_score < 100:
        print("   • Debug and fix non-working analysis functions")
    if overall_score < 75:
        print("   • Enhance exam document parsing and analysis")
    if overall_score >= 75:
        print("   • Consider adding more advanced exam pattern analysis")
        print("   • Enhance search functionality with better query processing")

if __name__ == "__main__":
    test_exam_integration() 