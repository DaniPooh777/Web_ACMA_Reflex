import reflex as rx
from Web_ACMA.components.caracteristics_card import *

# Esta función se encarga de dar estructura a la sección de características importantes de ACMA
def caracteristics() -> rx.Component:
    return rx.vstack(
        # Título de la sección 
        rx.heading("Tu Clase, Impulsada por la Calidad", style={**HEADER_TITLE_STYLE}),
        
        # Tarjetas
        rx.flex(
            caracteristics_card(
                "Calidad intachable", 
                "Garantizamos recursos de máxima calidad profesional para tus clases.",
                "shield" 
            ),
            caracteristics_card(
                "Más tiempo para planificar",
                "Dedica más tiempo a lo que importa: planificar tus clases.",
                "clock-4"
            ),
            caracteristics_card(
                "Recursos interactivos",
                "No te preocupes por crear recursos interactivos, nosotros lo hacemos.",
                "sparkles"
            ),
            width="100%",
            max_width="1130px",
            display="flex", 
            flex_direction= ["column", "column", "row"],
            justify_content="center",
            gap=["1.5rem", "2rem"],
            padding_x=["1rem", "2rem"],
        ),
        width="100%",
        align_items="center",
        padding_top="4rem",
    )