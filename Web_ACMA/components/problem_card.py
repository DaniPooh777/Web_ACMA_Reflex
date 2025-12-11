import reflex as rx


def problem_card(tittle_1: str, text_1: str, tittle_2: str, text_2: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.card(
                rx.text(tittle_1, size = "5"),
                rx.text(text_1),
                rx.divider(),
                rx.text(tittle_2, size = "5"),
                rx.text(text_2)
            )
        )
    )