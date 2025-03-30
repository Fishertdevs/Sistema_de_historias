/**
 * Animaciones para la aplicación de Generador de Historias de Terror
 */

document.addEventListener('DOMContentLoaded', function() {
    // Elementos para animar
    const header = document.querySelector('header');
    const controlPanel = document.querySelector('.control-panel');
    const storyContainer = document.querySelector('.story-container');
    const generateBtn = document.querySelector('.generate-btn');
    const bloodSplatters = document.querySelectorAll('.blood-splatter');
    
    // Animación de entrada
    setTimeout(() => {
        header.style.opacity = '1';
        header.style.transform = 'translateY(0)';
    }, 100);
    
    setTimeout(() => {
        controlPanel.style.opacity = '1';
        controlPanel.style.transform = 'translateY(0)';
    }, 300);
    
    setTimeout(() => {
        storyContainer.style.opacity = '1';
        storyContainer.style.transform = 'translateY(0)';
    }, 500);
    
    // Añadir clases de animación a elementos
    header.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    header.style.opacity = '0';
    header.style.transform = 'translateY(-20px)';
    
    controlPanel.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    controlPanel.style.opacity = '0';
    controlPanel.style.transform = 'translateY(20px)';
    
    storyContainer.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    storyContainer.style.opacity = '0';
    storyContainer.style.transform = 'translateY(20px)';
    
    // Animación del botón de generar
    generateBtn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-3px)';
        this.style.boxShadow = '0 6px 15px rgba(0, 0, 0, 0.4)';
    });
    
    generateBtn.addEventListener('mouseleave', function() {
        this.style.transform = '';
        this.style.boxShadow = '';
    });
    
    // Animación para los efectos de sangre
    bloodSplatters.forEach(splatter => {
        // Posición aleatoria
        const randomRotate = Math.random() * 90 - 45;
        splatter.style.transform = `rotate(${randomRotate}deg)`;
        
        // Animación periódica
        setInterval(() => {
            const randomScale = 0.8 + Math.random() * 0.4;
            splatter.style.transform = `rotate(${randomRotate}deg) scale(${randomScale})`;
            
            setTimeout(() => {
                splatter.style.transform = `rotate(${randomRotate}deg) scale(1)`;
            }, 2000);
        }, 8000);
    });
    
    // Efecto hover para elementos interactivos
    const interactiveElements = document.querySelectorAll('.option-btn, .download-btn, .form-control');
    
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
            this.style.transform = 'translateY(-2px)';
        });
        
        element.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // Animación del texto cuando se genera una historia
    document.addEventListener('storyGenerated', function() {
        const storyText = document.querySelector('.story-text p');
        if (storyText) {
            storyText.style.animation = 'fadeIn 1s ease-in-out';
        }
    });
    
    // Efecto de parpadeo para el título
    const mainTitle = document.querySelector('header h1');
    
    setInterval(() => {
        mainTitle.style.textShadow = '2px 2px 15px rgba(185, 28, 28, 0.7)';
        
        setTimeout(() => {
            mainTitle.style.textShadow = '2px 2px 8px rgba(0, 0, 0, 0.7)';
        }, 200);
    }, 5000);
    
    // Animación para los elementos del formulario
    const formLabels = document.querySelectorAll('.form-label');
    
    formLabels.forEach((label, index) => {
        setTimeout(() => {
            label.style.opacity = '1';
            label.style.transform = 'translateX(0)';
        }, 600 + (index * 100));
        
        label.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        label.style.opacity = '0';
        label.style.transform = 'translateX(-10px)';
    });
    
    // Efecto para botones de descarga
    const downloadButtons = document.querySelectorAll('.download-btn');
    
    downloadButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            // Añadir efecto de pulso al hacer clic
            this.classList.add('btn-pulse');
            
            setTimeout(() => {
                this.classList.remove('btn-pulse');
            }, 500);
        });
    });
    
    // Añadir estilo CSS para animación de pulso
    const style = document.createElement('style');
    style.textContent = `
        @keyframes btn-pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .btn-pulse {
            animation: btn-pulse 0.5s ease;
        }
    `;
    document.head.appendChild(style);
});

// Función para animar la aparición del texto de la historia
function animateStoryText() {
    const storyParagraphs = document.querySelectorAll('#storyText p');
    
    storyParagraphs.forEach((paragraph, index) => {
        paragraph.style.opacity = '0';
        paragraph.style.transform = 'translateY(10px)';
        paragraph.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        
        setTimeout(() => {
            paragraph.style.opacity = '1';
            paragraph.style.transform = 'translateY(0)';
        }, 100 * index);
    });
}

// Exponer la función de animación
window.animateStoryText = animateStoryText;
