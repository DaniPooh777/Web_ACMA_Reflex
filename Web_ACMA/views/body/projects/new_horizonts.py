import reflex as rx
from Web_ACMA.styles.views_style.body_style.projects_style.new_horizonts_style import HEADER_TITLE_STYLE
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import (
    FOUNDER_SECTION_CONTAINER,
    FOUNDER_IMAGE_STYLE,
    FOUNDER_TEXT_CARD_STYLE,
    INFO_TITLE_STYLE,
    INFO_TEXT_STYLE,
)

def new_horizonts() -> rx.Component:
    return rx.vstack(
        # Título de la sección
        rx.heading(
            "Nuevos Horizontes", 
            style={**HEADER_TITLE_STYLE, "font_size": ["2rem", "2.5rem"], "padding_x": "1rem"}
        ),
        
        rx.flex(
            # 1. Tarjeta de texto (Aparece PRIMERO en móvil)
            rx.vstack(
                rx.heading("Propuesta de Innovación", style=INFO_TITLE_STYLE),
                rx.text(
                    """A partir de este año, en ACMA, estamos abiertos a la idea de expandirnos en el área de la
                    programación. Nuestro objetivo es crear proyectos personalizados para tareas complejas, 
                    como esta misma página web, desarrollada por Daniel González para que ACMA sea accesible 
                    para todos los niveles educativos.""",
                    style=INFO_TEXT_STYLE,
                    text_align="justify"
                ),
                style={
                    **FOUNDER_TEXT_CARD_STYLE, 
                    "flex": "1", 
                    "width": "100%",
                },
                align_items="start",
                justify_content="center",
            ),
            
            # 2. Imagen (Aparece SEGUNDO en móvil, debajo del texto)
            rx.image(
                src="Código ACMA.png", 
                style={
                    **FOUNDER_IMAGE_STYLE, 
                    "width": ["100%", "450px"], 
                    "height": "auto", 
                    "border_radius": "15px",
                    "margin_top": ["1.5rem", "1.5rem", "0rem"],
                    "box_shadow": "0px 4px 20px rgba(0,0,0,0.2)" 
                } 
            ),
            
            # Layout: Columna simple en móvil, Fila en desktop
            style={
                **FOUNDER_SECTION_CONTAINER, 
                "max_width": "1150px", 
                "width": "100%",
                "padding_x": ["1.5rem", "2rem"],
                "gap": ["2rem", "4rem"], 
            },
            flex_direction=["column", "column", "row"],
            align_items="center",
        ),
        width="100%",
        align_items="center",
        padding_y=["3rem", "5rem"],
    )