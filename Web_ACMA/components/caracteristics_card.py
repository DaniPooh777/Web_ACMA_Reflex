import reflex as rx
from Web_ACMA.styles.colors import *
from Web_ACMA.styles.views_style.body_style.contact_style.contact_cards_style import *

"""Esta es la plantilla para crear las tarjetas de características"""
def caracteristics_card(tittle: str, text: str, icon: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(icon, size=24, color=ACCENT_BLUE),
            **ICON_CONTAINER_STYLE
        ),
        rx.text(tittle, **CARD_TITLE_STYLE),
        rx.text(
            text, 
            color=rx.color_mode_cond(light=SOFT_TEXT_SECONDARY, dark=DARK_TEXT_SECONDARY),
            font_size="0.9rem"),
        **CONTACT_CARD_STYLE
    )