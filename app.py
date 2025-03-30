import eel
import os
import sys
import json
from utils.openai_helper import generate_horror_story
from utils.file_helper import save_txt, save_pdf, save_html

# Configuración inicial de Eel
eel.init('web')

@eel.expose
def generate_story(theme, length, style):
    """
    Genera una historia de terror basada en los parámetros proporcionados.
    
    Args:
        theme (str): Tema o palabra clave de la historia.
        length (str): Longitud de la historia (corta, mediana, larga).
        style (str): Estilo de terror (psicológico, paranormal, gore).
        
    Returns:
        str: Historia generada.
    """
    try:
        story = generate_horror_story(theme, length, style)
        return {"status": "success", "story": story}
    except Exception as e:
        print(f"Error generando historia: {str(e)}")
        return {"status": "error", "message": f"Error al generar la historia: {str(e)}"}

@eel.expose
def download_story(format_type, story_text, title):
    """
    Descarga la historia en el formato especificado.
    
    Args:
        format_type (str): Tipo de formato (txt, pdf, html).
        story_text (str): Texto de la historia.
        title (str): Título de la historia.
        
    Returns:
        dict: Estado de la operación y ruta del archivo.
    """
    try:
        if format_type == "txt":
            file_path = save_txt(story_text, title)
        elif format_type == "pdf":
            file_path = save_pdf(story_text, title)
        elif format_type == "html":
            file_path = save_html(story_text, title)
        else:
            return {"status": "error", "message": "Formato no soportado"}
        
        return {"status": "success", "file_path": file_path}
    except Exception as e:
        print(f"Error descargando historia: {str(e)}")
        return {"status": "error", "message": f"Error al descargar la historia: {str(e)}"}

# Iniciar la aplicación
if __name__ == "__main__":
    try:
        # Iniciamos la aplicación en el puerto 5000 y host 127.0.0.1 para acceso local
        # Usamos mode='default' para evitar problemas con Chrome
        eel.start('index.html', mode='default', host='127.0.0.1', port=8080, 
                  size=(900, 700), block=True)
    except (SystemExit, MemoryError, KeyboardInterrupt):
        print("Cerrando aplicación...")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
