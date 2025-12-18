import reflex as rx


def caracteristics_card_card(tittle: str, text: str, text2: str, icon: str, num: str, num2: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.card(
                rx.hstack(
                    rx.icon(icon),
                    rx.text(tittle, size = "5")
                ),
                rx.hstack(
                    rx.card(
                    rx.text(text),
                    rx.text(num, size = "5")
                    ),
                    rx.card(
                        rx.text(text2),
                        rx.text(num2, size = "5")
                    )
                ) 
            )
        )
    )