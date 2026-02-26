import reflex as rx
from Web_ACMA.styles.views_style.header_style.header_style import *

# Es la plantilla para crear para crear los títulos de cada página.
def header(tittle: str, text: str) -> rx.Component:
    return rx.vstack(
        # Título
        rx.heading(tittle, style=HEADER_TITLE_STYLE),
        # Subtítulo
        rx.text(text, style=HEADER_TEXT_STYLE),
        style=HEADER_CONTAINER_STYLE,
    )