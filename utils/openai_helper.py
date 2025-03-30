import random
import re
from datetime import datetime
import string

class StoryGenerator:
    """
    Generador de historias de terror basado en plantillas y aleatoriedad.
    No requiere conexión a una API externa.
    """
    
    def __init__(self):
        # Inicialización de datos para la generación de historias
        # Títulos según el estilo
        self.title_templates = {
            "psicológico": [
                "La Sombra de {}", "El Susurro de {}", "Paranoia: {}", 
                "Delirio de {}", "Voces en {}", "La Obsesión de {}", 
                "Tras el Espejo de {}", "Locura en {}"
            ],
            "paranormal": [
                "El Espectro de {}", "La Maldición de {}", "Haunted: {}", 
                "Presencia Maligna en {}", "El Portal de {}", 
                "Posesión: {}", "Entidad de {}", "La Invocación de {}"
            ],
            "gore": [
                "Sangre en {}", "Destripado en {}", "Mutilación: {}", 
                "La Masacre de {}", "Carne Putrefacta de {}", 
                "Vísceras: {}", "Desmembrado en {}", "Carnaza en {}"
            ]
        }
        
        # Inicios según el estilo
        self.story_intros = {
            "psicológico": [
                "No podía estar seguro si lo que veía era real. {} se había convertido en una obsesión que me consumía día y noche.",
                "Las paredes parecían respirar. Desde que llegué a {}, mi mente no ha dejado de jugarme malas pasadas, distorsionando mi realidad.",
                "Las voces comenzaron como un susurro. Al principio creí que {} era producto de mi imaginación, pero ahora se han vuelto ensordecedoras.",
                "El insomnio me consumía lentamente. Cada noche en {} era peor que la anterior, los sonidos se intensificaban con la oscuridad.",
                "Mi terapeuta dice que {} es producto de mi imaginación, pero yo sé lo que vi. Nadie me cree cuando les cuento lo que ocurre."
            ],
            "paranormal": [
                "La casa de {} siempre tuvo esa reputación. Nadie quería acercarse después del anochecer, las historias sobre ella eran aterradoras.",
                "Todo comenzó con pequeños objetos que cambiaban de lugar. {} fue solo el principio de algo mucho peor, una presencia que crecía cada noche.",
                "El ritual parecía inofensivo. Nadie pensó que {} realmente funcionaría, pero despertamos algo antiguo y hambriento.",
                "Las apariciones siempre ocurrían a las 3:33 de la madrugada. {} se manifestaba con un frío intenso que helaba hasta los huesos.",
                "La ouija nos advirtió sobre {}. Deberíamos haberla escuchado, pero nuestra curiosidad fue más fuerte que el miedo."
            ],
            "gore": [
                "La sangre brotaba a borbotones, manchando todo {}. El olor metálico impregnaba la habitación mientras contemplaba mi obra.",
                "Su piel se desprendía en jirones mientras {} se retorcía de dolor. Sus gritos eran música para mis oídos enfermizos.",
                "Las vísceras se derramaron sobre {}. Nunca había visto tanta sangre en mi vida, pero me resultaba extrañamente hermosa.",
                "El cuchillo cortó limpiamente a través de {}. La carne cedió con una facilidad perturbadora, revelando los secretos bajo la piel.",
                "Los huesos crujieron mientras la sierra eléctrica atravesaba {}. La lluvia de sangre era hipnótica, casi poética en su brutalidad."
            ]
        }
        
        # Desarrollos según el estilo
        self.story_developments = {
            "psicológico": [
                "Con cada día que pasaba, la ansiedad crecía. {} se volvía más intenso, más real, dominando cada aspecto de mi vida.",
                "Las alucinaciones empeoraban con la oscuridad. {} aparecía en cada sombra, en cada rincón, susurrando promesas y amenazas.",
                "Mi percepción de la realidad se distorsionaba. Ya no podía confiar en mis sentidos cuando {} estaba cerca, alterando mi percepción.",
                "El miedo a {} me paralizaba. Comencé a evitar ciertas habitaciones, ciertos pensamientos que me llevaban a ese lugar oscuro.",
                "Las pesadillas se mezclaban con la realidad. A veces me despertaba gritando el nombre de {}, incapaz de distinguir el sueño de la vigilia."
            ],
            "paranormal": [
                "Los fenómenos aumentaron en intensidad. {} comenzó a manifestarse físicamente, dejando marcas inexplicables en las paredes y en mi piel.",
                "La temperatura bajaba drásticamente cuando {} se acercaba. Los cristales se empañaban con símbolos extraños que no pertenecían a ningún idioma conocido.",
                "Las fotografías capturaban siluetas que no deberían estar allí. {} siempre aparecía detrás de mí, más cerca en cada imagen nueva.",
                "Consulté a un médium que se negó a regresar después de sentir la presencia de {}. 'Hay algo antiguo y hambriento allí', me dijo temblando.",
                "Los niños de la casa fueron los primeros en ver a {}. Decían que les susurraba cosas por la noche, promesas oscuras y secretos prohibidos."
            ],
            "gore": [
                "La primera incisión fue solo el comienzo. {} se retorcía mientras la hoja se hundía más profundo, revelando capas de carne y secretos ocultos.",
                "Metódicamente separé cada articulación. {} era solo otro espécimen en mi colección, pero especialmente hermoso en su dolor.",
                "La piel se desprendía como si fuera papel. El verdadero arte comenzaba cuando {} revelaba su interior, la belleza escondida bajo la superficie.",
                "La sangre salpicaba las paredes con cada golpe. {} suplicaba, pero eso solo intensificaba el placer que sentía al continuar mi trabajo.",
                "El olor de {} en descomposición era embriagador. Cada día el hedor era más dulce, más seductor, como un perfume prohibido que solo yo apreciaba."
            ]
        }
        
        # Finales según el estilo
        self.story_endings = {
            "psicológico": [
                "Finalmente entendí la verdad: yo era {}. Siempre había sido yo, proyectando mis miedos más profundos hacia el exterior.",
                "El psiquiatra encontró mi diario. Ahora sé que {} nunca existió, excepto en mi mente fracturada que creó esta elaborada fantasía.",
                "Me internaron en el hospital psiquiátrico. Pero incluso aquí, {} sigue susurrándome en la oscuridad, prometiendo que nunca estaré solo.",
                "Decidí acabar con todo. Si {} era parte de mí, ambos moriríamos juntos, liberándome finalmente de este tormento eterno.",
                "Ahora tomo la medicación religiosamente. Pero a veces, cuando las pastillas no hacen efecto, {} regresa y me recuerda que nunca escaparé."
            ],
            "paranormal": [
                "El exorcismo falló. Ahora {} posee mi cuerpo, y yo soy el espectador atrapado en mi propia mente, viendo los horrores que comete con mis manos.",
                "Encontramos el cadáver emparedado exactamente donde {} nos indicó. El caso había quedado sin resolver durante décadas, pero ahora sabemos la verdad.",
                "El ritual de destierro funcionó, pero a un precio terrible. {} se ha ido, pero se llevó una parte de mi alma, dejándome incompleto para siempre.",
                "La casa fue demolida. Pero los vecinos dicen que por las noches aún se escuchan los lamentos de {}, buscando un nuevo hogar entre los escombros.",
                "Resultó que {} solo quería justicia. Ahora que encontramos sus restos, por fin puede descansar... o eso creíamos hasta que comenzaron los nuevos fenómenos."
            ],
            "gore": [
                "Cuando la policía llegó, el suelo estaba inundado de sangre. De {} solo quedaban pedazos irreconocibles, mi obra maestra final.",
                "Guardé partes de {} como recuerdo. A veces las acaricio en la oscuridad, recordando sus gritos y la belleza de su transformación.",
                "El forense vomitó al ver lo que quedaba de {}. Nunca había visto tal nivel de mutilación, lo que me llena de un orgullo perverso.",
                "Cosí partes de {} en mi propio cuerpo. Ahora somos uno, para siempre, una simbiosis perfecta de victimario y víctima.",
                "Nadie ha encontrado todos los trozos de {}. Algunos los conservo en el congelador para ocasiones especiales, reviviendo el placer de mi arte."
            ]
        }

        # Frases descriptivas según estilo
        self.atmospheric_descriptions = {
            "psicológico": [
                "La paranoia se intensificaba con cada sombra, cada movimiento en la periferia de mi visión.",
                "El tic-tac del reloj resonaba en mi cabeza como martillazos, marcando un tiempo que parecía distorsionarse.",
                "Las paredes parecían contraerse, asfixiándome lentamente en una prisión que se achicaba con cada respiración.",
                "Mi reflejo en el espejo parpadeó cuando yo no lo hice, mostrando una versión distorsionada de mi rostro.",
                "El silencio era ensordecedor, casi tangible, como una presencia física que presionaba contra mis tímpanos.",
                "Las sombras parecían moverse por el rabillo del ojo, danzando cuando no las miraba directamente.",
                "Cada crujido de la casa alimentaba mi ansiedad, como si el edificio mismo fuera un organismo vivo y hambriento."
            ],
            "paranormal": [
                "El aire se volvió frío y denso, como si algo lo estuviera consumiendo, robando su calor para alimentarse.",
                "Las luces parpadeaban sin razón aparente, código morse de un emisor del más allá.",
                "Un susurro ininteligible flotaba en la oscuridad, palabras en un idioma demasiado antiguo para ser comprendido.",
                "Sentí una presencia observándome desde la esquina vacía, ojos invisibles que perforaban mi alma.",
                "El perro se negaba a entrar en esa habitación, gruñendo al vacío como si pudiera ver lo que nosotros no.",
                "Las puertas se cerraban solas, como si alguien las empujara desde el otro lado, alguien ansioso por mantenernos dentro.",
                "El olor a azufre impregnó repentinamente el ambiente, señal inequívoca de una presencia maligna entre nosotros."
            ],
            "gore": [
                "La sangre formaba patrones hipnóticos en las baldosas blancas, como un macabro cuadro abstracto.",
                "El sonido húmedo de la carne al ser cortada era casi musical, una sinfonía de dolor y transformación.",
                "Sus gritos se transformaron en gorgoteos cuando la sangre llenó su garganta, ahogando sus últimas súplicas.",
                "Las vísceras brillaban con un tono rojizo bajo la luz tenue, joyas orgánicas expuestas al aire por primera vez.",
                "El crujido de los huesos al romperse reverberaba en la habitación, percusión macabra en mi orquesta de dolor.",
                "El olor metálico de la sangre fresca saturaba el aire, embriagador como el más fino de los perfumes.",
                "Cada corte revelaba nuevas capas, como un macabro regalo desenvolviéndose bajo mi cuchillo experto."
            ]
        }
        
        # Palabras de conexión temática según categorías comunes
        self.thematic_connections = {
            # Lugares
            "casa": ["habitación", "sótano", "ático", "pasillo", "escalera", "puerta", "ventana", "pared", "techo"],
            "mansión": ["salón", "biblioteca", "dormitorio", "sótano", "ático", "pasillo", "escalera", "candelabro"],
            "hospital": ["paciente", "doctor", "enfermera", "camilla", "bisturí", "medicamento", "tratamiento", "quirófano"],
            "bosque": ["árbol", "rama", "hoja", "sendero", "raíz", "niebla", "animal", "madera", "cabaña"],
            "cementerio": ["tumba", "lápida", "ataúd", "esqueleto", "muerte", "espíritu", "flores marchitas", "tierra"],
            "escuela": ["salón", "profesor", "estudiante", "pizarra", "libro", "pasillo", "casillero", "campana"],
            
            # Elementos sobrenaturales
            "fantasma": ["aparición", "espíritu", "presencia", "ectoplasma", "posesión", "médium", "más allá"],
            "demonio": ["posesión", "ritual", "pacto", "exorcismo", "pentagrama", "azufre", "infierno"],
            "bruja": ["hechizo", "poción", "aquelarre", "magia", "familiar", "grimorio", "caldero"],
            "vampiro": ["sangre", "colmillo", "noche", "ataúd", "estaca", "inmortal", "sed"],
            
            # Elementos psicológicos
            "miedo": ["terror", "pánico", "ansiedad", "fobia", "pesadilla", "trauma", "sobresalto"],
            "locura": ["alucinación", "delirio", "paranoia", "psicosis", "obsesión", "compulsión", "voces"],
            "pesadilla": ["sueño", "inconsciente", "terror nocturno", "parálisis del sueño", "insomnio"],
            
            # Elementos gore
            "sangre": ["hemorragia", "mancha", "charco", "gota", "vena", "arteria", "coagulación"],
            "cuchillo": ["filo", "hoja", "corte", "puñalada", "incisión", "herida", "desmembramiento"],
            "cuerpo": ["carne", "hueso", "órgano", "músculo", "piel", "entrañas", "vísceras"]
        }

    def _get_thematic_words(self, theme):
        """Obtiene palabras relacionadas con el tema para mejorar la coherencia."""
        theme_lower = theme.lower()
        
        # Buscar coincidencias directas en nuestro diccionario
        if theme_lower in self.thematic_connections:
            return self.thematic_connections[theme_lower]
        
        # Buscar coincidencias parciales
        for key, words in self.thematic_connections.items():
            if key in theme_lower or theme_lower in key:
                return words
        
        # Si no hay coincidencias, devolver un conjunto genérico
        return ["oscuridad", "miedo", "terror", "horror", "noche", "misterio", "pesadilla"]

    def _enhance_text_with_theme(self, text, theme, theme_words):
        """Mejora el texto incorporando más referencias al tema de manera coherente."""
        # Dividir el texto en oraciones para insertar referencias completas
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # No modificar textos muy cortos
        if len(sentences) < 3:
            return text
            
        # Número de inserciones basado en longitud
        insertions = min(1, len(sentences) // 5)
        
        for _ in range(insertions):
            # Seleccionar una posición aleatoria para insertar (evitando la primera y última oración)
            if len(sentences) > 2:
                pos = random.randint(1, len(sentences) - 2)
            else:
                continue
            
            # Crear una frase relacionada con el tema que se integre naturalmente
            theme_word = random.choice(theme_words)
            theme_phrases = [
                f"En mi mente, todo esto se conectaba con {theme}.",
                f"No podía dejar de pensar en cómo esto se relacionaba con {theme}.",
                f"Había algo en el {theme_word} que me hacía volver a {theme}.",
                f"Era imposible no relacionar lo que estaba pasando con {theme}.",
                f"El {theme_word} me recordaba constantemente a {theme}."
            ]
            
            # Insertar una oración completa
            sentences.insert(pos, random.choice(theme_phrases))
            
        return ' '.join(sentences)

    def _format_text_by_length(self, text, target_length):
        """Ajusta el texto para que se aproxime a la longitud objetivo."""
        words = text.split()
        
        if target_length == "corta" and len(words) > 300:
            # Para historias cortas, reducir contenido
            return ' '.join(words[:300])
        elif target_length == "larga" and len(words) < 800:
            # Para historias largas, expandir con descripciones adicionales
            expanded_text = text
            
            # Buscar puntos donde insertar descripciones adicionales
            sentences = re.split(r'(?<=[.!?])\s+', expanded_text)
            
            # Determinar cuántas descripciones necesitamos añadir
            descriptions_to_add = min(len(sentences) - 2, 8)
            
            # Añadir descripciones en ubicaciones aleatorias
            for _ in range(descriptions_to_add):
                idx = random.randint(1, len(sentences) - 1)
                style_key = random.choice(list(self.atmospheric_descriptions.keys()))
                description = random.choice(self.atmospheric_descriptions[style_key])
                sentences.insert(idx, description)
            
            expanded_text = ' '.join(sentences)
            return expanded_text
            
        return text

    def _ensure_coherence(self, story_parts, theme):
        """Asegura que todas las partes de la historia sean coherentes con el tema."""
        # Asegurarse de que el tema aparezca en cada sección principal
        for i, part in enumerate(story_parts):
            if theme.lower() not in part.lower() and i > 0 and i < len(story_parts) - 1:
                # Reemplazar la sección con una versión que incorpore el tema de manera natural
                sentences = re.split(r'(?<=[.!?])\s+', part)
                
                if len(sentences) > 1:
                    # Frases más naturales que incorporan el tema en contexto
                    coherent_references = [
                        f"Todo esto me recordaba a mi experiencia con {theme}.",
                        f"Mientras esto ocurría, no podía evitar relacionarlo con {theme}.",
                        f"Esta situación era similar a lo que había vivido con {theme} anteriormente.",
                        f"La sensación era muy parecida a cuando enfrenté a {theme} la primera vez.",
                        f"Mi mente no dejaba de volver a {theme} mientras procesaba lo que estaba ocurriendo."
                    ]
                    
                    # Insertar en un lugar donde tenga sentido - preferentemente al final de un párrafo
                    if len(sentences) > 3:
                        insert_pos = len(sentences) - 2
                    else:
                        insert_pos = len(sentences) - 1
                    
                    sentences.insert(insert_pos, random.choice(coherent_references))
                    story_parts[i] = ' '.join(sentences)
        
        return story_parts

    def generate_horror_story(self, theme, length, style):
        """
        Genera una historia de terror utilizando plantillas y aleatoriedad.
        
        Args:
            theme (str): Tema o palabra clave de la historia.
            length (str): Longitud de la historia (corta, mediana, larga).
            style (str): Estilo de terror (psicológico, paranormal, gore).
            
        Returns:
            str: Historia generada.
        """
        # Normalizar los valores de entrada para prevenir errores
        theme = theme.strip().lower()
        length = length.strip().lower()
        style = style.strip().lower()
        
        # Verificar que el estilo sea válido
        if style not in ["psicológico", "paranormal", "gore"]:
            style = random.choice(["psicológico", "paranormal", "gore"])
        
        # Obtener palabras temáticas relacionadas
        theme_words = self._get_thematic_words(theme)
        
        # Generar título asegurando que incluya el tema
        title_template = random.choice(self.title_templates[style])
        title = title_template.format(theme.capitalize() if '{}' in title_template else '')
        if theme.lower() not in title.lower():
            title = f"{title}: {theme.capitalize()}"
        
        # Seleccionar plantillas para cada parte de la historia que incluyan el tema
        intro_templates = [t for t in self.story_intros[style] if '{}' in t]
        if not intro_templates:
            intro_templates = self.story_intros[style]
            
        intro = random.choice(intro_templates).format(theme)
        intro = self._enhance_text_with_theme(intro, theme, theme_words)
        
        # Para historias medias y largas, añadir más desarrollo
        num_developments = 1 if length == "corta" else (2 if length == "mediana" else 4)
        developments = []
        
        # Seleccionar desarrollos que puedan incluir el tema
        dev_templates = [t for t in self.story_developments[style] if '{}' in t]
        if not dev_templates:
            dev_templates = self.story_developments[style]
            
        for _ in range(num_developments):
            dev = random.choice(dev_templates).format(theme)
            dev = self._enhance_text_with_theme(dev, theme, theme_words)
            developments.append(dev)
        
        # Añadir descripciones atmosféricas según la longitud
        num_descriptions = 1 if length == "corta" else (3 if length == "mediana" else 5)
        descriptions = []
        for _ in range(num_descriptions):
            desc = random.choice(self.atmospheric_descriptions[style])
            # Incorporar palabras temáticas en las descripciones de manera más natural
            if random.random() > 0.5:
                sentences = re.split(r'(?<=[.!?])\s+', desc)
                theme_word = random.choice(theme_words)
                
                # Frases más contextuales para las descripciones
                theme_sentences = [
                    f"Era como si {theme} estuviera presente en cada {theme_word}.",
                    f"El {theme_word} parecía una manifestación física de {theme}.",
                    f"Era increíble cómo {theme} parecía influir en cada {theme_word} a mi alrededor.",
                    f"Siempre asociaré el {theme_word} con {theme} después de esta experiencia.",
                    f"Hay una extraña conexión entre {theme} y este {theme_word} que no puedo explicar."
                ]
                
                # Elegir una frase aleatoria
                sentences.append(random.choice(theme_sentences))
                desc = ' '.join(sentences)
            descriptions.append(desc)
        
        # Seleccionar final que incluya el tema
        ending_templates = [t for t in self.story_endings[style] if '{}' in t]
        if not ending_templates:
            ending_templates = self.story_endings[style]
            
        ending = random.choice(ending_templates).format(theme)
        ending = self._enhance_text_with_theme(ending, theme, theme_words)
        
        # Construir la historia completa
        story_parts = [intro]
        
        # Intercalar desarrollos y descripciones
        for i in range(max(len(developments), len(descriptions))):
            if i < len(developments):
                story_parts.append(developments[i])
            if i < len(descriptions):
                story_parts.append(descriptions[i])
        
        story_parts.append(ending)
        
        # Asegurar coherencia con el tema
        story_parts = self._ensure_coherence(story_parts, theme)
        
        # Unir todas las partes
        story_body = "\n\n".join(story_parts)
        
        # Formato final con título
        full_story = f"{title}\n\n{story_body}"
        
        # Ajustar longitud final según lo solicitado
        full_story = self._format_text_by_length(full_story, length)
        
        return full_story

# Crear una instancia del generador
_story_generator = StoryGenerator()

def generate_horror_story(theme, length, style):
    """
    Función wrapper que utiliza el generador de historias.
    
    Args:
        theme (str): Tema o palabra clave de la historia.
        length (str): Longitud de la historia (corta, mediana, larga).
        style (str): Estilo de terror (psicológico, paranormal, gore).
        
    Returns:
        str: Historia generada.
    """
    return _story_generator.generate_horror_story(theme, length, style)
