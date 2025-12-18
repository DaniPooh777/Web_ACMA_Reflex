import reflex as rx


def caracteristics_card_link(tittle: str, text: str, icon: str, link: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.card(
                rx.icon(icon),
                rx.text(tittle, size = "5"),
                rx.link(text, href = link)
            )
        )
    )