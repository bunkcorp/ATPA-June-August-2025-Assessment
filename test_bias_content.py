#!/usr/bin/env python3
"""
Clean test script for bias types content
"""

from curriculum import ATPACurriculum

def test_bias_content():
    print("=== CLEAN BIAS CONTENT TEST ===")
    
    try:
        # Initialize curriculum
        c = ATPACurriculum()
        
        # Get data quality guidelines
        data_quality = c.get_data_quality_guidelines()
        
        print(f"Module: {data_quality['module']}")
        print(f"Available Guidelines: {list(data_quality['guidelines'].keys())}")
        
        # Get bias types content properly
        bias_types = data_quality['guidelines']['bias_types']
        
        print(f"\nBias Types Content Length: {len(str(bias_types))} characters")
        print("\nFirst 500 characters:")
        print(str(bias_types)[:500] + "...")
        
        # Test specific bias types
        print("\n=== SPECIFIC BIAS TYPES ===")
        if isinstance(bias_types, dict):
            for bias_type, content in bias_types.items():
                if isinstance(content, str):
                    print(f"✅ {bias_type}: {len(content)} characters")
                else:
                    print(f"✅ {bias_type}: {type(content).__name__}")
        
        print("\n🎉 Bias content test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_bias_content() 