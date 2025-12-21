import reflex as rx
from Web_ACMA.styles.views_style.header_style.header_style import (
    HEADER_CONTAINER_STYLE,
    HEADER_TITLE_STYLE,
    HEADER_TEXT_STYLE
)

def header(tittle: str, text: str) -> rx.Component:
    return rx.vstack(
        rx.heading(tittle, style=HEADER_TITLE_STYLE),
        rx.text(text, style=HEADER_TEXT_STYLE),
        style=HEADER_CONTAINER_STYLE,
    )