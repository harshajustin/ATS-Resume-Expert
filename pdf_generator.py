"""
Professional PDF Generation Utilities for ATS Resume Expert
Enhanced with professional typography, colors, and layout
"""
import io
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import re

class ProfessionalPDFStyles:
    """Professional color schemes and typography for PDF generation"""
    
    # Professional Color Palette
    COLORS = {
        'primary_dark': HexColor('#1a365d'),      # Professional navy blue
        'primary_medium': HexColor('#2d5a87'),    # Medium blue
        'primary_light': HexColor('#4a90b8'),     # Light blue
        'secondary': HexColor('#2c5aa0'),         # Secondary blue
        'accent': HexColor('#e53e3e'),            # Professional red accent
        'success': HexColor('#38a169'),           # Success green
        'warning': HexColor('#d69e2e'),           # Warning amber
        'text_primary': HexColor('#1a202c'),      # Primary text - dark gray
        'text_secondary': HexColor('#4a5568'),    # Secondary text - medium gray
        'text_muted': HexColor('#718096'),        # Muted text - light gray
        'background': HexColor('#f7fafc'),        # Background - very light gray
        'border': HexColor('#e2e8f0'),            # Border - light gray
        'white': HexColor('#ffffff'),             # Pure white
    }
    
    # Typography Settings
    FONTS = {
        'title_size': 24,
        'subtitle_size': 18,
        'heading1_size': 16,
        'heading2_size': 14,
        'body_size': 11,
        'caption_size': 9,
        'line_height_multiplier': 1.4,
    }

def create_professional_styles():
    """Create professional paragraph styles for PDF generation"""
    styles = getSampleStyleSheet()
    
    # Main Title Style
    title_style = ParagraphStyle(
        'ProfessionalTitle',
        parent=styles['Heading1'],
        fontSize=ProfessionalPDFStyles.FONTS['title_size'],
        textColor=ProfessionalPDFStyles.COLORS['primary_dark'],
        spaceAfter=30,
        spaceBefore=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['title_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Subtitle Style
    subtitle_style = ParagraphStyle(
        'ProfessionalSubtitle',
        parent=styles['Heading2'],
        fontSize=ProfessionalPDFStyles.FONTS['subtitle_size'],
        textColor=ProfessionalPDFStyles.COLORS['primary_medium'],
        spaceAfter=20,
        spaceBefore=15,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['subtitle_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Section Heading Style
    heading1_style = ParagraphStyle(
        'ProfessionalHeading1',
        parent=styles['Heading1'],
        fontSize=ProfessionalPDFStyles.FONTS['heading1_size'],
        textColor=ProfessionalPDFStyles.COLORS['primary_dark'],
        spaceAfter=15,
        spaceBefore=25,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['heading1_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier'],
        borderWidth=0,
        borderColor=ProfessionalPDFStyles.COLORS['border'],
        borderPadding=5
    )
    
    # Subsection Heading Style
    heading2_style = ParagraphStyle(
        'ProfessionalHeading2',
        parent=styles['Heading2'],
        fontSize=ProfessionalPDFStyles.FONTS['heading2_size'],
        textColor=ProfessionalPDFStyles.COLORS['secondary'],
        spaceAfter=12,
        spaceBefore=18,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['heading2_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Body Text Style
    body_style = ParagraphStyle(
        'ProfessionalBody',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['body_size'],
        textColor=ProfessionalPDFStyles.COLORS['text_primary'],
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=ProfessionalPDFStyles.FONTS['body_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier'],
        firstLineIndent=0
    )
    
    # Highlighted Content Style
    highlight_style = ParagraphStyle(
        'ProfessionalHighlight',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['body_size'],
        textColor=ProfessionalPDFStyles.COLORS['primary_medium'],
        spaceAfter=10,
        leftIndent=20,
        fontName='Helvetica',
        leading=ProfessionalPDFStyles.FONTS['body_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier'],
        bulletIndent=15
    )
    
    # Important/Success Style
    success_style = ParagraphStyle(
        'ProfessionalSuccess',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['body_size'],
        textColor=ProfessionalPDFStyles.COLORS['success'],
        spaceAfter=10,
        leftIndent=20,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['body_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Warning/Attention Style
    warning_style = ParagraphStyle(
        'ProfessionalWarning',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['body_size'],
        textColor=ProfessionalPDFStyles.COLORS['warning'],
        spaceAfter=10,
        leftIndent=20,
        fontName='Helvetica-Bold',
        leading=ProfessionalPDFStyles.FONTS['body_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Caption/Footer Style
    caption_style = ParagraphStyle(
        'ProfessionalCaption',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['caption_size'],
        textColor=ProfessionalPDFStyles.COLORS['text_muted'],
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica',
        leading=ProfessionalPDFStyles.FONTS['caption_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier']
    )
    
    # Quote Style
    quote_style = ParagraphStyle(
        'ProfessionalQuote',
        parent=styles['Normal'],
        fontSize=ProfessionalPDFStyles.FONTS['body_size'],
        textColor=ProfessionalPDFStyles.COLORS['text_secondary'],
        spaceAfter=15,
        spaceBefore=15,
        leftIndent=30,
        rightIndent=30,
        fontName='Helvetica-Oblique',
        leading=ProfessionalPDFStyles.FONTS['body_size'] * ProfessionalPDFStyles.FONTS['line_height_multiplier'],
        borderWidth=1,
        borderColor=ProfessionalPDFStyles.COLORS['border'],
        borderPadding=10
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'heading1': heading1_style,
        'heading2': heading2_style,
        'body': body_style,
        'highlight': highlight_style,
        'success': success_style,
        'warning': warning_style,
        'caption': caption_style,
        'quote': quote_style
    }
def create_pdf_response(title, response, filename_prefix="ATS_Analysis"):
    """
    Creates a professionally formatted PDF from the AI response with enhanced typography and colors.
    
    Args:
        title (str): The title of the analysis
        response (str): The AI-generated response content
        filename_prefix (str): Prefix for the filename
    
    Returns:
        tuple: (pdf_bytes, filename)
    """
    
    # Create a BytesIO buffer to hold the PDF
    buffer = io.BytesIO()
    
    # Create the PDF document with professional margins
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm,
        title=f"ATS Resume Expert - {title}",
        author="ATS Resume Expert",
        subject="Resume Analysis Report"
    )
    
    # Get professional styles
    pro_styles = create_professional_styles()
    
    # Build the PDF content
    story = []
    
    # Professional Header Section
    header_table_data = [
        ['🎯 ATS Resume Expert', datetime.now().strftime('%B %d, %Y')],
        [title, datetime.now().strftime('%H:%M')]
    ]
    
    header_table = Table(header_table_data, colWidths=[4*inch, 2*inch])
    header_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 16),
        ('FONTSIZE', (0, 1), (0, 1), 14),
        ('FONTSIZE', (1, 0), (1, 1), 10),
        ('TEXTCOLOR', (0, 0), (0, 1), ProfessionalPDFStyles.COLORS['primary_dark']),
        ('TEXTCOLOR', (1, 0), (1, 1), ProfessionalPDFStyles.COLORS['text_secondary']),
        ('ALIGN', (1, 0), (1, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 20))
    
    # Add a professional separator line
    separator_table = Table([['─' * 80]], colWidths=[6*inch])
    separator_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (0, 0), 8),
        ('TEXTCOLOR', (0, 0), (0, 0), ProfessionalPDFStyles.COLORS['border']),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
    ]))
    story.append(separator_table)
    story.append(Spacer(1, 20))
    
    # Process the response content with enhanced parsing
    content_parts = _parse_response_content_enhanced(response)
    
    for part in content_parts:
        try:
            if part['type'] == 'title':
                story.append(KeepTogether([
                    Paragraph(part['content'], pro_styles['title']),
                    Spacer(1, 10)
                ]))
            elif part['type'] == 'heading1':
                story.append(KeepTogether([
                    Paragraph(f"▸ {part['content']}", pro_styles['heading1']),
                    Spacer(1, 5)
                ]))
            elif part['type'] == 'heading2':
                story.append(KeepTogether([
                    Paragraph(f"• {part['content']}", pro_styles['heading2']),
                    Spacer(1, 3)
                ]))
            elif part['type'] == 'success':
                story.append(Paragraph(f"✓ {part['content']}", pro_styles['success']))
            elif part['type'] == 'warning':
                story.append(Paragraph(f"⚠ {part['content']}", pro_styles['warning']))
            elif part['type'] == 'highlight':
                story.append(Paragraph(f"→ {part['content']}", pro_styles['highlight']))
            elif part['type'] == 'quote':
                story.append(Paragraph(f'"{part["content"]}"', pro_styles['quote']))
            elif part['type'] == 'body':
                # Handle line breaks and formatting
                formatted_content = part['content'].replace('\n', '<br/>')
                # Add smart typography
                formatted_content = _enhance_typography(formatted_content)
                story.append(Paragraph(formatted_content, pro_styles['body']))
            elif part['type'] == 'spacer':
                story.append(Spacer(1, 15))
        except Exception as e:
            # Fallback for any parsing issues
            story.append(Paragraph(part['content'], pro_styles['body']))
    
    # Professional Footer Section
    story.append(Spacer(1, 40))
    
    footer_table = Table([
        ['Generated by ATS Resume Expert'],
        ['Your AI-Powered Career Assistant'],
        [f'Report ID: {filename_prefix}_{datetime.now().strftime("%Y%m%d_%H%M%S")}']
    ], colWidths=[6*inch])
    
    footer_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, 2), 'Helvetica'),
        ('FONTSIZE', (0, 0), (0, 0), 10),
        ('FONTSIZE', (0, 1), (0, 2), 8),
        ('TEXTCOLOR', (0, 0), (0, 0), ProfessionalPDFStyles.COLORS['primary_medium']),
        ('TEXTCOLOR', (0, 1), (0, 2), ProfessionalPDFStyles.COLORS['text_muted']),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(footer_table)
    
    # Build the PDF
    doc.build(story)
    
    # Get the PDF data
    pdf_data = buffer.getvalue()
    buffer.close()
    
    # Generate filename with better sanitization
    safe_title = re.sub(r'[^\w\s-]', '', title.strip())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)[:30]  # Limit length
    filename = f"{filename_prefix}_{safe_title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    return pdf_data, filename

def _enhance_typography(text):
    """
    Enhance text with professional typography improvements.
    
    Args:
        text (str): Input text to enhance
    
    Returns:
        str: Enhanced text with typography improvements
    """
    # Replace straight quotes with smart quotes
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace("'", ''').replace("'", ''')
    
    # Replace double hyphens with em dashes
    text = text.replace('--', '—')
    
    # Replace triple dots with ellipsis
    text = text.replace('...', '…')
    
    # Improve spacing around punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)  # Remove spaces before punctuation
    text = re.sub(r'([,.!?;:])\s*', r'\1 ', text)  # Ensure single space after punctuation
    
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def _parse_response_content_enhanced(response):
    """
    Enhanced parsing of AI response content into structured parts for professional PDF formatting.
    
    Args:
        response (str): The raw response content
    
    Returns:
        list: List of content parts with enhanced type classification and content
    """
    parts = []
    lines = response.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            parts.append({'type': 'spacer', 'content': ''})
            continue
        
        # Check for main headings (multiple # or ** formatting)
        if line.startswith('####') or (line.startswith('***') and line.endswith('***')):
            heading_text = line.replace('#', '').replace('*', '').strip()
            parts.append({'type': 'title', 'content': heading_text})
        
        # Check for section headings (### or ** formatting)
        elif line.startswith('###') or (line.startswith('**') and line.endswith('**')):
            heading_text = line.replace('#', '').replace('*', '').strip()
            parts.append({'type': 'heading1', 'content': heading_text})
        
        # Check for subsection headings (## or single *)
        elif line.startswith('##') or (line.startswith('*') and line.endswith('*') and not line.startswith('**')):
            heading_text = line.replace('#', '').replace('*', '').strip()
            parts.append({'type': 'heading2', 'content': heading_text})
        
        # Check for success indicators
        elif any(keyword in line.lower() for keyword in ['excellent', 'strong', 'good match', 'well-suited', 'perfect', 'outstanding']):
            parts.append({'type': 'success', 'content': line})
        
        # Check for warning indicators
        elif any(keyword in line.lower() for keyword in ['missing', 'lacks', 'needs improvement', 'consider adding', 'weak', 'insufficient']):
            parts.append({'type': 'warning', 'content': line})
        
        # Check for percentage matches (important metrics)
        elif re.search(r'\d+%', line):
            parts.append({'type': 'highlight', 'content': f"📊 {line}"})
        
        # Check for bullet points or numbered lists
        elif line.startswith(('•', '-', '*', '→', '▸')) or re.match(r'^\d+\.', line):
            parts.append({'type': 'highlight', 'content': line})
        
        # Check for quotes or recommendations
        elif line.startswith(('"', '"')) or 'recommend' in line.lower():
            parts.append({'type': 'quote', 'content': line})
        
        # Regular content
        else:
            parts.append({'type': 'body', 'content': line})
    
    return parts

def _parse_response_content(response):
    """
    Parses the AI response content into structured parts for PDF formatting.
    
    Args:
        response (str): The raw response content
    
    Returns:
        list: List of content parts with type and content
    """
    parts = []
    lines = response.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            parts.append({'type': 'spacer', 'content': ''})
            continue
        
        # Check for headings (lines with ### or ** formatting)
        if line.startswith('###') or (line.startswith('**') and line.endswith('**')):
            heading_text = line.replace('###', '').replace('**', '').strip()
            parts.append({'type': 'heading', 'content': heading_text})
        
        # Check for bullet points or numbered lists
        elif line.startswith(('•', '-', '*')) or re.match(r'^\d+\.', line):
            parts.append({'type': 'highlight', 'content': line})
        
        # Check for percentage matches
        elif re.search(r'\d+%', line):
            parts.append({'type': 'highlight', 'content': f"🎯 {line}"})
        
        # Regular content
        else:
            parts.append({'type': 'body', 'content': line})
    
    return parts

def create_multi_analysis_pdf(analyses, filename_prefix="ATS_Complete_Analysis"):
    """
    Creates a comprehensive PDF with multiple analysis results using professional styling.
    
    Args:
        analyses (dict): Dictionary of analysis titles and responses
        filename_prefix (str): Prefix for the filename
    
    Returns:
        tuple: (pdf_bytes, filename)
    """
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm,
        title="ATS Resume Expert - Complete Analysis",
        author="ATS Resume Expert",
        subject="Comprehensive Resume Analysis Report"
    )
    
    # Get professional styles
    pro_styles = create_professional_styles()
    
    story = []
    
    # Professional Cover Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("🎯 ATS Resume Expert", pro_styles['title']))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Complete Analysis Report", pro_styles['subtitle']))
    story.append(Spacer(1, 30))
    
    # Professional metadata table
    metadata_data = [
        ['Report Date:', datetime.now().strftime('%B %d, %Y')],
        ['Generated At:', datetime.now().strftime('%H:%M:%S')],
        ['Total Analyses:', str(len(analyses))],
        ['Report Type:', 'Comprehensive Assessment']
    ]
    
    metadata_table = Table(metadata_data, colWidths=[2*inch, 3*inch])
    metadata_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), ProfessionalPDFStyles.COLORS['text_secondary']),
        ('TEXTCOLOR', (1, 0), (1, -1), ProfessionalPDFStyles.COLORS['text_primary']),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    
    story.append(metadata_table)
    story.append(Spacer(1, 60))
    
    # Table of Contents with professional styling
    story.append(Paragraph("📋 Table of Contents", pro_styles['heading1']))
    story.append(Spacer(1, 20))
    
    toc_data = []
    for i, title in enumerate(analyses.keys(), 1):
        toc_data.append([f"{i}.", title, f"Page {i + 1}"])
    
    toc_table = Table(toc_data, colWidths=[0.5*inch, 4*inch, 1*inch])
    toc_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), ProfessionalPDFStyles.COLORS['text_primary']),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, ProfessionalPDFStyles.COLORS['border']),
        ('BACKGROUND', (0, 0), (-1, 0), ProfessionalPDFStyles.COLORS['background']),
    ]))
    
    story.append(toc_table)
    story.append(PageBreak())
    
    # Add each analysis with professional formatting
    for i, (title, response) in enumerate(analyses.items(), 1):
        if i > 1:
            story.append(PageBreak())
        
        # Section header
        story.append(Paragraph(f"Analysis {i}: {title}", pro_styles['title']))
        story.append(Spacer(1, 25))
        
        # Process content with enhanced parsing
        content_parts = _parse_response_content_enhanced(response)
        
        for part in content_parts:
            try:
                if part['type'] == 'title':
                    story.append(KeepTogether([
                        Paragraph(part['content'], pro_styles['subtitle']),
                        Spacer(1, 10)
                    ]))
                elif part['type'] == 'heading1':
                    story.append(KeepTogether([
                        Paragraph(f"▸ {part['content']}", pro_styles['heading1']),
                        Spacer(1, 5)
                    ]))
                elif part['type'] == 'heading2':
                    story.append(KeepTogether([
                        Paragraph(f"• {part['content']}", pro_styles['heading2']),
                        Spacer(1, 3)
                    ]))
                elif part['type'] == 'success':
                    story.append(Paragraph(f"✓ {part['content']}", pro_styles['success']))
                elif part['type'] == 'warning':
                    story.append(Paragraph(f"⚠ {part['content']}", pro_styles['warning']))
                elif part['type'] == 'highlight':
                    story.append(Paragraph(f"→ {part['content']}", pro_styles['highlight']))
                elif part['type'] == 'quote':
                    story.append(Paragraph(f'"{part["content"]}"', pro_styles['quote']))
                elif part['type'] == 'body':
                    formatted_content = part['content'].replace('\n', '<br/>')
                    formatted_content = _enhance_typography(formatted_content)
                    story.append(Paragraph(formatted_content, pro_styles['body']))
                elif part['type'] == 'spacer':
                    story.append(Spacer(1, 15))
            except Exception as e:
                # Fallback for any parsing issues
                story.append(Paragraph(part['content'], pro_styles['body']))
        
        # Add section separator (except for last section)
        if i < len(analyses):
            story.append(Spacer(1, 30))
    
    # Professional final footer
    story.append(Spacer(1, 40))
    final_footer_table = Table([
        ['📊 End of Report'],
        ['Generated by ATS Resume Expert'],
        ['For questions or support, contact our AI Career Assistant'],
        [f'Report ID: {filename_prefix}_{datetime.now().strftime("%Y%m%d_%H%M%S")}']
    ], colWidths=[6*inch])
    
    final_footer_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, 3), 'Helvetica'),
        ('FONTSIZE', (0, 0), (0, 0), 12),
        ('FONTSIZE', (0, 1), (0, 2), 10),
        ('FONTSIZE', (0, 3), (0, 3), 8),
        ('TEXTCOLOR', (0, 0), (0, 0), ProfessionalPDFStyles.COLORS['primary_dark']),
        ('TEXTCOLOR', (0, 1), (0, 2), ProfessionalPDFStyles.COLORS['primary_medium']),
        ('TEXTCOLOR', (0, 3), (0, 3), ProfessionalPDFStyles.COLORS['text_muted']),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(final_footer_table)
    
    # Build the PDF
    doc.build(story)
    
    pdf_data = buffer.getvalue()
    buffer.close()
    
    filename = f"{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    return pdf_data, filename
