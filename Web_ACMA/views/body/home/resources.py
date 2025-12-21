import reflex as rx
from Web_ACMA.components.resources_types_card import resources_type_card
from Web_ACMA.components.problem_card import problem_card
from Web_ACMA.components.example_resource_type_card import example_resources_type_card
from Web_ACMA.styles.components_style.resources_type_card_style import RESOURCES_GRID_STYLE, HEADER_TITLE_STYLE # Importá el estilo

def resources() -> rx.Component:
    # Importamos State dentro de la función para evitar importación circular (¿Qué es la importación circular?)
    from Web_ACMA.Web_ACMA import State
    
    return rx.vstack(
        rx.heading("Recursos a tu Alcance", 
                   style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}
                ),
        
        # Tarjetas clickeables
        rx.flex(
            resources_type_card("Pósters", "file", State.toggle_posters),
            resources_type_card("Presentaciones", "presentation", State.toggle_presentaciones),
            resources_type_card("Cuestionarios", "notepad-text", State.toggle_cuestionarios),
            resources_type_card("Documentos", "file-text", State.toggle_documentos),
            style=RESOURCES_GRID_STYLE # <--- USA ESTO PARA EL FLEX Y EL GAP
        ),
        
        # Contenido que aparece para Pósters
        rx.cond(
            State.seccion_activa == "posters",
            rx.box(
                rx.heading("Ejemplo de Póster", size="5"),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Póster: Tú Decides",
                        "Descripción",
                        """Póster educativo que ilustra los problemas de la España vaciada 
                        para los alumnos de Primaria. Incluye, elementos visuales, imágenes 
                        orientativas y un texto claro y accesible para los más pequeños."""
                    ),
                    example_resources_type_card("favicon.ico"),
                    spacing="4"
                ),
                padding_x="20px",
                margin_bottom="20px"
            ),
        ),
        
        # Contenido que aparece para Presentaciones
        rx.cond(
            State.seccion_activa == "presentaciones",
            rx.box(
                rx.heading("Ejemplo de Presentación", size="5"),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Presentación: Enlaces Químicos",
                        "Descripción",
                        """Presentación dinámica con nº diapositivas que habla sobre los distintos enlaces 
                        químicos adaptado para la comprensión de los alumnos de 4º E.S.O.. Incluye una múltiple 
                        variedad de elementos gráficos, dos juegos interactivos y un texto, claro, accesible 
                        y directo al grano."""
                    ),
                    example_resources_type_card("favicon.ico"),
                    spacing="4"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        
        # Contenido que aparece para Cuestionarios
        rx.cond(
            State.seccion_activa == "cuestionarios",
            rx.box(
                rx.heading("Ejemplo de Cuestionario", size="5"),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Cuestionario: Cuestionario Tema 4 Historia de España",
                        "Descripción",
                        """Cuestionario digital con 50 preguntas de opción múltiple sobre el tema 4 
                        de Historia de España para los alumnos de 2º de Bachillerato."""
                    ),
                    example_resources_type_card("favicon.ico"),
                    spacing="4"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        
        # Contenido que aparece para Documentos
        rx.cond(
            State.seccion_activa == "documentos",
            rx.box(
                rx.heading("Ejemplo de Documento", size="5"),
                rx.flex(
                    problem_card(
                        "Ejemplo",
                        "Documento: Guion Anuncio ACMA 2025-2026",
                        "Descripción",
                        """Una propuesta que hizo <nombre>, integrante de la promoción del 2025-2026, 
                        para el anuncio de ACMA. Cuanta con una estructura clara, buena maquetación y 
                        una originalidad asombrosa para innovar en el anuncio. """
                    ),
                    example_resources_type_card("favicon.ico"),
                    spacing="4"
                ),
                padding_x="20px",
                margin_bottom="20px"
            )
        ),
        
        width="100%",
        align_items="center", # Centra el heading y el grid
        spacing="4",
    )