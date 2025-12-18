import reflex as rx
from Web_ACMA.styles.views_style.body_style.contact_style.contact_cards_style import (
    CONTACT_CARD_STYLE, 
    ICON_CONTAINER_STYLE, 
    CARD_TITLE_STYLE
)

def caracteristics_card(tittle: str, text: str, icon: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(icon, size=24, color="rgb(59, 130, 246)"),
            **ICON_CONTAINER_STYLE
        ),
        rx.text(tittle, **CARD_TITLE_STYLE),
        rx.text(text, color="rgb(229, 231, 235)", font_size="0.9rem"),
        **CONTACT_CARD_STYLE
    )