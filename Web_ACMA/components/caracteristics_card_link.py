import reflex as rx
from Web_ACMA.styles.views_style.body_style.contact_style.contact_cards_style import (
    CONTACT_CARD_STYLE, 
    ICON_CONTAINER_STYLE, 
    CARD_TITLE_STYLE, 
    CARD_LINK_STYLE
)

def caracteristics_card_link(tittle: str, text: str, icon: str, link: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(icon, size=24, color="rgb(59, 130, 246)"),
            **ICON_CONTAINER_STYLE
        ),
        rx.text(tittle, **CARD_TITLE_STYLE),
        rx.link(text, href=link, **CARD_LINK_STYLE),
        **CONTACT_CARD_STYLE
    )