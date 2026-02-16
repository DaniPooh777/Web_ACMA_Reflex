import reflex as rx
from Web_ACMA.components.resources_types_card import resources_type_card
from Web_ACMA.components.problem_card import problem_card
from Web_ACMA.components.example_resource_type_card import example_resources_type_card
from Web_ACMA.styles.components_style.resources_type_card_style import RESOURCES_GRID_STYLE, HEADER_TITLE_STYLE 

# Esta función se encarga de dar estructura a la sección de ejemplos de recursos que ACMA puede realizar
def resources() -> rx.Component:
    from Web_ACMA.Web_ACMA import State # Importamos State dentro de la función para evitar importación circular 
    return rx.vstack(
        # Título de la sección
        rx.heading("Recursos a tu Alcance", 
                   style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}
                ),
        
        # Tarjetas clickeables
        rx.flex(
            resources_type_card("Pósters", "file", State.toggle_posters),
            resources_type_card("Presentaciones", "presentation", State.toggle_presentaciones),
            resources_type_card("Cuestionarios", "notepad-text", State.toggle_cuestionarios),
            resources_type_card("Documentos", "file-text", State.toggle_documentos),
            style=RESOURCES_GRID_STYLE #
        ),
        
        # Contenido que aparece para Pósters
        rx.cond(
            State.seccion_activa == "posters",
            rx.box(
                rx.heading("Ejemplo de Póster", 
                        size="7",
                        padding_bottom="1rem",
                        padding_top="1rem",
                        align="center",
                        color="#ffffff"
                    ),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Póster: Tú Decides",
                        "Descripción",
                        """Este póster es un recurso didáctico diseñado para explicar el fenómeno de la despoblación a alumnos de Primaria.

                        - Objetivo: Sensibilizar sobre la realidad rural mediante un enfoque empático y sencillo.

                        - Diseño: Combina imágenes orientativas con una disposición visual clara que facilita la retención de conceptos clave.

                        - Contenido: Utiliza un lenguaje adaptado, eliminando tecnicismos para que el mensaje sea accesible y fomente la reflexión crítica desde edades tempranas."""
                    ),
                    example_resources_type_card("TÚ DECIDES.png"),
                    spacing="6",
                    justify="center", 
                    flex_wrap="wrap",
                    white_space = "pre-line"
                ),
                padding_x="20px",
                margin_bottom="20px"
            ),
        ),
        
        # Contenido que aparece para Presentaciones
        rx.cond(
            State.seccion_activa == "presentaciones",
            rx.box(
                rx.heading("Ejemplo de Presentación", 
                        size="7",
                        padding_bottom="1rem",
                        padding_top="1rem",
                        align="center",
                        color="#ffffff"
                    ),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Presentación: Enlaces Químicos",
                        "Descripción",
                        """Este recurso es una presentación dinámica estructurada en un número determinado de diapositivas, diseñada específicamente para el nivel de 4º de E.S.O.

                        - Contenido temático: Explica de manera integral los distintos tipos de enlaces químicos, adaptando la complejidad técnica al nivel académico de los alumnos.

                        - Componentes Visuales: Se apoya en una múltiple variedad de elementos gráficos que facilitan la comprensión de los conceptos teóricos.

                        - Tono y estilo: Utiliza un texto claro, accesible y directo al grano, eliminando tecnicismos para que el mensaje sea accesible."""
                    ),
                    example_resources_type_card("Enlaces Químicos.png"),
                    spacing="6", 
                    justify="center", 
                    flex_wrap="wrap",
                    white_space = "pre-line"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        
        # Contenido que aparece para Cuestionarios
        rx.cond(
            State.seccion_activa == "cuestionarios",
            rx.box(
                rx.heading("Ejemplo de Cuestionario", 
                        size="7",
                        padding_bottom="1rem",
                        padding_top="1rem",
                        align="center",
                        color="#ffffff"
                    ),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Cuestionario: Cuestionario Tema 4 Historia de España",
                        "Descripción",
                        """Este cuestionario es una herramienta de repaso exhaustivo centrada en el tema 4 de la asignatura.

                        - Estructura: Consta de 50 preguntas de opción múltiple que cubren todo el temario del bloque.

                        - Objetivo: Facilitar la autoevaluación y el refuerzo de conceptos clave para alumnos que preparan la EBAU.

                        - Formato: Digital, diseñado para una resolución ágil y una corrección inmediata."""
                    ),
                    example_resources_type_card("Cuestionario Tema 4 Historia de España.png"),
                    spacing="6", 
                    justify="center", 
                    flex_wrap="wrap",
                    white_space = "pre-line"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        
        # Contenido que aparece para Documentos
        rx.cond(
            State.seccion_activa == "documentos",
            rx.box(
                rx.heading("Ejemplo de Documento", 
                        size="7",
                        padding_bottom="1rem",
                        padding_top="1rem",
                        align="center",
                        color="#ffffff"
                    ),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Documento: Guion Anuncio ACMA 2025-2026",
                        "Descripción",
                        """Este documento detalla una estrategia innovadora para el anuncio de la próxima temporada de ACMA.

                        - Diseño y forma: Destaca por una estructura clara y una buena maquetación, facilitando una lectura fluida y profesional de la propuesta.

                        - Factor innovador: El valor diferencial radica en una originalidad asombrosa, rompiendo con los formatos convencionales para buscar un impacto visual y creativo único.

                        - Objetivo: Modernizar la imagen del anuncio 25-26 mediante una narrativa visual y conceptual que busca la innovación total."""
                    ),
                    example_resources_type_card("Guión Anuncio Acma.png"),
                    spacing="6", 
                    justify="center", 
                    flex_wrap="wrap",
                    white_space = "pre-line"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        width="100%",
        align_items="center", 
        spacing="4",
    )