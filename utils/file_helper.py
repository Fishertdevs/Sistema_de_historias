import os
import time
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_JUSTIFY

def create_download_dir():
    """Crea el directorio de descargas si no existe."""
    download_dir = os.path.join(os.path.expanduser("~"), "TerrorGeneratorDescargas")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

def sanitize_filename(title):
    """Sanitiza el título para usarlo como nombre de archivo."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    # Limita la longitud del título
    return title[:50]

def get_title_from_story(story):
    """Extrae el título de la historia."""
    lines = story.strip().split('\n')
    for line in lines[:3]:  # Busca el título en las primeras 3 líneas
        if line and not line.isspace():
            return line.strip()
    return "Historia de Terror"  # Título por defecto

def save_txt(story, custom_title=None):
    """
    Guarda la historia en formato TXT.
    
    Args:
        story (str): Texto de la historia.
        custom_title (str, optional): Título personalizado. Si es None, se extrae de la historia.
        
    Returns:
        str: Ruta al archivo guardado.
    """
    download_dir = create_download_dir()
    
    # Determinar el título
    title = custom_title if custom_title else get_title_from_story(story)
    sanitized_title = sanitize_filename(title)
    
    # Crear nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{sanitized_title}_{timestamp}.txt"
    file_path = os.path.join(download_dir, filename)
    
    # Guardar el archivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(story)
    
    return file_path

def save_pdf(story, custom_title=None):
    """
    Guarda la historia en formato PDF.
    
    Args:
        story (str): Texto de la historia.
        custom_title (str, optional): Título personalizado. Si es None, se extrae de la historia.
        
    Returns:
        str: Ruta al archivo guardado.
    """
    download_dir = create_download_dir()
    
    # Determinar el título
    title = custom_title if custom_title else get_title_from_story(story)
    sanitized_title = sanitize_filename(title)
    
    # Crear nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{sanitized_title}_{timestamp}.pdf"
    file_path = os.path.join(download_dir, filename)
    
    # Configurar el documento PDF
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='JustifyStyle',
        fontName='Helvetica',
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    ))
    
    # Procesar el texto para el PDF
    story_lines = story.split('\n')
    flowables = []
    
    # Título
    if story_lines and not story_lines[0].isspace():
        title_style = styles['Title']
        flowables.append(Paragraph(story_lines[0], title_style))
        story_lines = story_lines[1:]  # Quitar el título del texto
    
    # Contenido
    for line in story_lines:
        if line.strip():
            p = Paragraph(line, styles['JustifyStyle'])
            flowables.append(p)
        else:
            # Espacio en blanco para párrafos
            p = Paragraph("<br/>", styles['JustifyStyle'])
            flowables.append(p)
    
    # Construir el PDF
    doc.build(flowables)
    
    return file_path

def save_html(story, custom_title=None):
    """
    Guarda la historia en formato HTML.
    
    Args:
        story (str): Texto de la historia.
        custom_title (str, optional): Título personalizado. Si es None, se extrae de la historia.
        
    Returns:
        str: Ruta al archivo guardado.
    """
    download_dir = create_download_dir()
    
    # Determinar el título
    title = custom_title if custom_title else get_title_from_story(story)
    sanitized_title = sanitize_filename(title)
    
    # Crear nombre de archivo único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{sanitized_title}_{timestamp}.html"
    file_path = os.path.join(download_dir, filename)
    
    # Procesar el texto para HTML
    story_html = ""
    story_lines = story.split('\n')
    
    # Título
    if story_lines and not story_lines[0].isspace():
        html_title = story_lines[0]
        story_lines = story_lines[1:]  # Quitar el título del texto
    else:
        html_title = "Historia de Terror"
    
    # Formato de párrafos
    for line in story_lines:
        if line.strip():
            story_html += f"<p>{line}</p>\n"
    
    # Template HTML con estilo oscuro
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_title}</title>
    <style>
        body {{
            font-family: 'Times New Roman', Times, serif;
            background-color: #111111;
            color: #dddddd;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: #1a1a1a;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.8);
        }}
        h1 {{
            color: #b91c1c;
            text-align: center;
            font-size: 28px;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        p {{
            text-align: justify;
            margin-bottom: 20px;
            font-size: 16px;
        }}
        footer {{
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #777777;
        }}
        .blood-splatter {{
            position: absolute;
            top: 10px;
            right: 10px;
            width: 100px;
            height: 100px;
            opacity: 0.7;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{html_title}</h1>
        {story_html}
        <footer>
            Generado con Terror Generator - Desarrollado por Harry fishert - 
            <a href="https://github.com/Fishertdevs" style="color: #777777;">GitHub</a>
        </footer>
    </div>
</body>
</html>
"""
    
    # Guardar el archivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return file_path
