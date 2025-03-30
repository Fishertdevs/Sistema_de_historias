// Elementos del DOM
const storyForm = document.getElementById('storyForm');
const themeInput = document.getElementById('theme');
const generateBtn = document.getElementById('generateBtn');
const loadingIndicator = document.getElementById('loadingIndicator');
const storyContent = document.getElementById('storyContent');
const storyText = document.getElementById('storyText');
const storyTitle = document.getElementById('storyTitle');
const emptyState = document.getElementById('emptyState');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');
const downloadBtns = document.querySelectorAll('.download-btn');
const newStoryBtn = document.getElementById('newStoryBtn');
const downloadToast = document.getElementById('downloadToast');
const downloadMessage = document.getElementById('downloadMessage');

// Inicializar toast
const toast = new bootstrap.Toast(downloadToast);

// Variable para almacenar la historia actual
let currentStory = '';

// Manejar envío del formulario
storyForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Obtener valores del formulario
    const theme = themeInput.value.trim();
    const length = document.querySelector('input[name="length"]:checked').value;
    const style = document.querySelector('input[name="style"]:checked').value;
    
    // Validar entrada
    if (!theme) {
        showError('Por favor ingresa un tema o palabra clave.');
        return;
    }
    
    // Mostrar cargando
    showLoading();
    
    try {
        // Llamar a la función de Python para generar la historia
        const result = await eel.generate_story(theme, length, style)();
        
        if (result.status === 'success') {
            // Mostrar la historia generada
            currentStory = result.story;
            showStory(currentStory);
        } else {
            showError(result.message || 'Error al generar la historia. Intenta nuevamente.');
        }
    } catch (error) {
        showError('Error de conexión. Asegúrate de que la aplicación esté funcionando correctamente.');
        console.error('Error:', error);
    } finally {
        hideLoading();
    }
});

// Manejar descarga de la historia
downloadBtns.forEach(btn => {
    btn.addEventListener('click', async function() {
        if (!currentStory) {
            showError('No hay una historia para descargar. Genera una primero.');
            return;
        }
        
        const format = this.getAttribute('data-format');
        
        try {
            // Determinar título de la historia
            const title = extractTitleFromStory(currentStory);
            
            // Llamar a la función de Python para descargar la historia
            const result = await eel.download_story(format, currentStory, title)();
            
            if (result.status === 'success') {
                // Mostrar notificación de éxito
                downloadMessage.textContent = `Tu historia ha sido guardada como: ${getFilenameFromPath(result.file_path)}`;
                toast.show();
            } else {
                showError(result.message || `Error al descargar la historia en formato ${format.toUpperCase()}.`);
            }
        } catch (error) {
            showError('Error de conexión al intentar descargar la historia.');
            console.error('Error:', error);
        }
    });
});

// Botón de nueva historia
newStoryBtn.addEventListener('click', function() {
    resetForm();
});

// Función para mostrar estado de carga
function showLoading() {
    generateBtn.disabled = true;
    loadingIndicator.classList.remove('d-none');
    storyContent.classList.add('d-none');
    emptyState.classList.add('d-none');
    errorMessage.classList.add('d-none');
}

// Función para ocultar estado de carga
function hideLoading() {
    generateBtn.disabled = false;
    loadingIndicator.classList.add('d-none');
}

// Función para mostrar la historia
function showStory(story) {
    // Extraer título y contenido
    const lines = story.trim().split('\n');
    let title = '';
    let content = story;
    
    // Buscar título en las primeras líneas
    if (lines.length > 0) {
        title = lines[0].trim();
        content = lines.slice(1).join('\n').trim();
    }
    
    // Mostrar título y contenido
    storyTitle.textContent = title;
    storyText.innerHTML = formatStoryText(content);
    
    // Mostrar contenedor de historia
    storyContent.classList.remove('d-none');
    storyContent.classList.add('slide-up');
    emptyState.classList.add('d-none');
    
    // Reiniciar animación después de completarse
    setTimeout(() => {
        storyContent.classList.remove('slide-up');
    }, 500);
}

// Función para dar formato al texto de la historia
function formatStoryText(text) {
    // Reemplazar saltos de línea con párrafos
    return text.split('\n\n').map(paragraph => {
        if (paragraph.trim() === '') return '';
        return `<p>${paragraph.trim()}</p>`;
    }).join('');
}

// Función para mostrar error
function showError(message) {
    errorText.textContent = message;
    errorMessage.classList.remove('d-none');
    loadingIndicator.classList.add('d-none');
    
    // Ocultar error después de 5 segundos
    setTimeout(() => {
        errorMessage.classList.add('d-none');
    }, 5000);
}

// Función para resetear el formulario
function resetForm() {
    storyContent.classList.add('d-none');
    emptyState.classList.remove('d-none');
    currentStory = '';
    
    // No limpiamos los campos del formulario para mantener las preferencias del usuario
}

// Función para extraer título de la historia
function extractTitleFromStory(story) {
    const lines = story.trim().split('\n');
    if (lines.length > 0) {
        return lines[0].trim();
    }
    return 'Historia de Terror';
}

// Función para obtener nombre de archivo de la ruta
function getFilenameFromPath(path) {
    const parts = path.split(/[\/\\]/);
    return parts[parts.length - 1];
}

// Añadir efectos de hover al título
document.querySelector('header h1').addEventListener('mouseover', function() {
    this.style.textShadow = '2px 2px 15px rgba(185, 28, 28, 0.7)';
});

document.querySelector('header h1').addEventListener('mouseout', function() {
    this.style.textShadow = '2px 2px 8px rgba(0, 0, 0, 0.7)';
});

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    // Asegurarse de que el estado vacío se muestre inicialmente
    emptyState.classList.remove('d-none');
    storyContent.classList.add('d-none');
    
    // Animación inicial
    document.querySelector('header').classList.add('fade-in');
});
