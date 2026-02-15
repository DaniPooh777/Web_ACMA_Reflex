import reflex as rx
from Web_ACMA.styles.views_style.body_style.contact_style.contact_cards_style import (
    SCHEDULE_CARD_STYLE, 
    ICON_CONTAINER_STYLE, 
    INNER_SCHEDULE_STYLE, 
    CARD_TITLE_STYLE
)

"""Esta es la plantilla para crear las tarjetas de contacto de ACMA"""
def caracteristics_card_card(tittle: str, text: str, text2: str, icon: str, num: str, num2: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=24, color="rgb(59, 130, 246)"),
                **ICON_CONTAINER_STYLE
            ),
            rx.text(tittle, **CARD_TITLE_STYLE),
            align_items="center",
            spacing="4",
            margin_bottom="1rem",
        ),
        rx.hstack(
            rx.vstack(
                rx.text(text, color="rgb(59, 130, 246)", font_size="0.8rem"),
                rx.text(num, size="6", color="white"),
                **INNER_SCHEDULE_STYLE
            ),
            rx.vstack(
                rx.text(text2, color="rgb(59, 130, 246)", font_size="0.8rem"),
                rx.text(num2, size="6", color="white"),
                **INNER_SCHEDULE_STYLE
            ),
            width="100%",
            spacing="4",
        ),
        **SCHEDULE_CARD_STYLE
    )