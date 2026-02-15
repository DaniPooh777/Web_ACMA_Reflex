import reflex as rx
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import (
    INFO_CARD_STYLE, 
    INFO_TITLE_STYLE, 
    INFO_TEXT_STYLE
)

"""Esta es la plantilla para crear la tarjeta de información"""
def information_card(tittle: str, text: str, width: str = "100%") -> rx.Component:
    return rx.vstack(
        rx.heading(tittle, style=INFO_TITLE_STYLE),
        rx.text(text, style=INFO_TEXT_STYLE),
        style={**INFO_CARD_STYLE, "width": width, "text_align":"justify"},
        align_items="center", 
        padding="2.5rem",     
    )