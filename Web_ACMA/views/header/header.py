import reflex as rx


def header(tittle: str, text: str) -> rx.Component:
    return rx.vstack(
        rx.heading(tittle, size="9"),
        rx.text(text),
    )