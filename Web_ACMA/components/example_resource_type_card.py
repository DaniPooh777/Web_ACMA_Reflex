import reflex as rx
from Web_ACMA.styles.colors import *
from Web_ACMA.styles.components_style.resources_type_card_style import RESOURCE_CARD_STYLE

"""Esta es la plantilla para crear la tarjeta de visualización de la sección de ejemplos de trabajos que ACMA puede realizar"""
def example_resources_type_card(url: str) -> rx.Component:    
    custom_style = RESOURCE_CARD_STYLE.copy() # Creamos una copia para no romper el estilo original de las otras tarjetas
    custom_style.update({
        "width": ["100%", "550px"],
        "height": "auto",
        "padding": "1.5rem",
        "cursor": "default",    
        "_hover": {},
    })

    # Tarjeta de visualización
    return rx.vstack(
        # Título
        rx.text(
            "Visualización", 
            color=ACCENT_BLUE,
            font_weight="bold", 
            font_size="1.1rem"
        ),

        # Sección imagen
        rx.box(
            rx.image(
                src=url,
                alt="Vista previa del recurso",
                width="100%",
                height="400px",
                object_fit="contain",
                border_radius="8px",
            ),
            padding="1rem",
            background=rx.color_mode_cond(
                light="rgba(0, 0, 0, 0.03)", 
                dark="rgba(255, 255, 255, 0.03)"
            ),
            border_radius="12px",
            width="100%",
        ),
        style=custom_style # Aplicamos el diccionario customizado
    )