import reflex as rx


def caracteristics_card(tittle: str, text: str, icon: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.card(
                rx.icon(icon),
                rx.text(tittle, size = "5"),
                rx.text(text)
            )
        )
    )