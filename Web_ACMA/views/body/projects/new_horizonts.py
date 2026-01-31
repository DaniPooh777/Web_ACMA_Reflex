import reflex as rx
from Web_ACMA.styles.views_style.body_style.projects_style.new_horizonts_style import (
    HEADER_TITLE_STYLE,
    ORDER_CARD_STYLE
)
from Web_ACMA.components.information_card import information_card

def new_horizonts() -> rx.Component:
    return rx.vstack(
        # Título usando el estilo de cabecera que ya tenías definido
        rx.heading(
            "Nuevos Horizontes", 
            style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}
        ),
        
        rx.flex(
            information_card(
                "¿Tenés una idea?",
                """En ACMA no nos quedamos quietos. Si sos docente y tenés una necesidad pedagógica 
                que requiere una solución digital innovadora, estamos listos para el desafío. 
                Desde simulaciones interactivas hasta nuevas plataformas de aprendizaje, 
                el límite es tu imaginación y nuestra capacidad de cómputo.""",
                width="100%"
            ),
            # Acá podrías meter otra tarjeta o un botón de contacto
            style=ORDER_CARD_STYLE
        ),
        width="100%",
        align_items="center",
    )