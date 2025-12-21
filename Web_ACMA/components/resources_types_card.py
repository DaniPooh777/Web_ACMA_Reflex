import reflex as rx
from typing import Callable
from Web_ACMA.styles.components_style.resources_type_card_style import (
    RESOURCE_CARD_STYLE,
    RESOURCE_ICON_STYLE,
    RESOURCE_TEXT_STYLE # Importá esto también
)

def resources_type_card(text: str, icon: str, on_click: Callable) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(tag=icon, **RESOURCE_ICON_STYLE), # Usamos el estilo para el tamaño y color
            rx.text(text, **RESOURCE_TEXT_STYLE),
            on_click=on_click,
            **RESOURCE_CARD_STYLE, # El estilo de la tarjeta va al contenedor
        ),
    )