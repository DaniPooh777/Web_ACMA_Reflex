import reflex as rx
from Web_ACMA.components.caracteristics_card import *

def caracteristics() -> rx.Component:
    return rx.vstack(
        rx.heading("Tu Clase, Impulsada por la Calidad", style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}),
        
        rx.flex(
            caracteristics_card(
                "Calidad intachable de los trabajos", 
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
            flex_wrap="nowrap", 
            justify_content="center",
            gap="1.5rem",
        ),
        width="100%",
        align_items="center",
        padding_top="4rem",
    )