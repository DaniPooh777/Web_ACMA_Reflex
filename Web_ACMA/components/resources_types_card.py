import reflex as rx
from typing import Callable


def resources_type_card(text: str, icon: str, on_click: Callable) -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.icon(icon),
            rx.text(text),
            on_click=on_click,
            cursor="pointer",
            _hover={"background_color": "var(--gray-3)"}
        )
    )