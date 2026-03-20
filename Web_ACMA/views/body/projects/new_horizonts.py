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
                    """A partir de este año, en ACMA, estamos abiertos a la idea de de expandirnos en el área de la
                    programación. Nuesto objetivo detrás de ello es de crear la posibilidad de poder desarrollar
                    proyectos más personalizados para aquellas tareas más complejas que crear una presentación
                    interactiva en Genially. Un claro ejemplo de ello es esta página web. Fue creada por el 
                    colaborador principal de ACMA Daniel González, cuya visión es que ACMA sea más accesible y
                    entendible para todos los profesores independientemente de si es de Guardería o de Bachillerato.
                    Por esta razón, consideramos la importancia de intentar establecer en ACMA la programación como
                    uno de nuestros servicios fijos para así poder mejorar la enseñanza con proyectos personalizados
                    para las necesidades de cada profesor.""",
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
                    "height": ["100%", "450px"], 
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
                "padding_x": ["1rem", "1rem"],
                "gap": ["2rem", "4rem"], 
            },
            flex_direction=["column", "column", "row"],
            align_items="center",
        ),
        width="100%",
        align_items="center",
        padding_y=["3rem", "5rem"],
    )