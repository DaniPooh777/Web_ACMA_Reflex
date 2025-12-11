import reflex as rx


def information_card(tittle: str, subtittle: str, text: str) -> rx.Component:
    return rx.card(
                rx.text(tittle, size = "5"),
                rx.text(subtittle),
                rx.text(text)
            )