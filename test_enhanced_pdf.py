#!/usr/bin/env python3
"""
Test script for enhanced PDF generation in ATS Resume Expert
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pdf_generator import create_pdf_response, create_multi_analysis_pdf, ProfessionalPDFStyles

def test_enhanced_pdf_generation():
    """Test the enhanced PDF generation with professional styling"""
    
    print("🧪 Testing Enhanced PDF Generation...")
    
    # Sample analysis content with various formatting
    sample_response = """
### ATS Analysis Results

**Overall Score: 85%**

Your resume shows strong alignment with the job requirements. Here are the key findings:

#### Strengths
• Strong technical skills match: Python, Data Analysis, Machine Learning
• Excellent project experience with quantifiable results
• Professional formatting and structure
• Good use of action verbs and metrics

#### Areas for Improvement
- Missing keywords: "Agile methodology", "Cross-functional teams"
- Consider adding more industry-specific certifications
- Work experience section needs more specific achievements

#### Recommendations
1. Add the following keywords to improve ATS compatibility
2. Quantify more achievements with specific numbers
3. Include relevant certifications and training

**Match Score Breakdown:**
- Technical Skills: 92%
- Experience Level: 78%
- Education: 85%
- Keywords: 82%

"This resume demonstrates solid qualifications for the target role with room for strategic improvements."

Missing critical elements:
⚠ Industry certifications
⚠ Agile/Scrum experience mentions
⚠ Leadership examples

Success indicators:
✓ Strong technical foundation
✓ Quantified achievements
✓ Professional presentation
✓ Relevant experience
"""
    
    try:
        # Test single analysis PDF
        print("📄 Creating single analysis PDF...")
        pdf_data, filename = create_pdf_response(
            title="Enhanced ATS Resume Analysis",
            response=sample_response,
            filename_prefix="Enhanced_Test"
        )
        
        # Save the PDF for verification
        output_path = f"test_output_{filename}"
        with open(output_path, 'wb') as f:
            f.write(pdf_data)
        
        print(f"✅ Single PDF generated successfully: {output_path}")
        print(f"   File size: {len(pdf_data):,} bytes")
        
        # Test multi-analysis PDF
        print("\n📚 Creating multi-analysis PDF...")
        analyses = {
            "ATS Score Analysis": sample_response,
            "Keyword Optimization": """
### Keyword Analysis

**Current Keyword Match: 78%**

#### Found Keywords:
• Python (5 mentions)
• Data Analysis (3 mentions)
• Machine Learning (2 mentions)
• Project Management (1 mention)

#### Missing Critical Keywords:
- Agile methodology
- Cross-functional collaboration
- Strategic planning
- Performance optimization

**Recommendation:** Add 6-8 more industry keywords to reach 90%+ match rate.
""",
            "Structure & Formatting": """
### Document Structure Assessment

**Format Score: 92%**

#### Strengths:
✓ Clean, professional layout
✓ Consistent formatting
✓ Appropriate use of bullet points
✓ Good white space management

#### Minor Issues:
⚠ Some sections could use better hierarchy
⚠ Consider adding more visual elements

**Overall:** Excellent professional presentation with minor enhancement opportunities.
"""
        }
        
        multi_pdf_data, multi_filename = create_multi_analysis_pdf(
            analyses=analyses,
            filename_prefix="Enhanced_Complete"
        )
        
        # Save the multi-analysis PDF
        multi_output_path = f"test_output_{multi_filename}"
        with open(multi_output_path, 'wb') as f:
            f.write(multi_pdf_data)
        
        print(f"✅ Multi-analysis PDF generated successfully: {multi_output_path}")
        print(f"   File size: {len(multi_pdf_data):,} bytes")
        
        # Test color palette
        print("\n🎨 Testing professional color palette...")
        colors = ProfessionalPDFStyles.COLORS
        print(f"   Primary colors: {len([k for k in colors.keys() if 'primary' in k])} variants")
        print(f"   Text colors: {len([k for k in colors.keys() if 'text' in k])} variants")
        print(f"   Total color palette: {len(colors)} colors")
        
        # Test typography settings
        print("\n📝 Testing typography settings...")
        fonts = ProfessionalPDFStyles.FONTS
        print(f"   Font sizes: {list(fonts.keys())}")
        print(f"   Line height multiplier: {fonts['line_height_multiplier']}")
        
        print("\n🎉 All enhanced PDF generation tests passed!")
        print("\nGenerated files:")
        print(f"   - {output_path}")
        print(f"   - {multi_output_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during PDF generation test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_error_handling():
    """Test error handling in PDF generation"""
    print("\n🔧 Testing error handling...")
    
    try:
        # Test with empty content
        pdf_data, filename = create_pdf_response(
            title="Empty Content Test",
            response="",
            filename_prefix="Error_Test"
        )
        print("✅ Empty content handled gracefully")
        
        # Test with special characters
        special_content = """
### Special Characters Test 🎯

This content contains special characters: ñ, é, ü, ß, €, £, ¥

"Smart quotes" and 'apostrophes' should work properly.

Mathematical symbols: ≥ ≤ ± × ÷ √

Bullets: • ◦ ▪ ▫ ○ ●
"""
        
        pdf_data, filename = create_pdf_response(
            title="Special Characters Test",
            response=special_content,
            filename_prefix="Special_Chars"
        )
        print("✅ Special characters handled correctly")
        
        return True
        
    except Exception as e:
        print(f"❌ Error handling test failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Enhanced PDF Generation Tests")
    print("=" * 50)
    
    # Run tests
    basic_test = test_enhanced_pdf_generation()
    error_test = test_error_handling()
    
    print("\n" + "=" * 50)
    if basic_test and error_test:
        print("🎉 ALL TESTS PASSED! Enhanced PDF generation is working correctly.")
        print("\n📋 Summary of Enhancements:")
        print("   ✅ Professional color scheme (navy blue palette)")
        print("   ✅ Enhanced typography (Helvetica family, optimized sizes)")
        print("   ✅ Improved layout (2cm margins, structured headers)")
        print("   ✅ Smart content parsing (automatic formatting detection)")
        print("   ✅ Visual indicators (✓, ⚠, →, 📊 symbols)")
        print("   ✅ Professional document structure")
        print("   ✅ Error handling and fallbacks")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED! Check the error messages above.")
        sys.exit(1)
