import reflex as rx


def link_button() -> rx.Component:
    return rx.link(
            rx.button(
            "Solicite un nuevo encargo", 
            ),
            href="https://reflex.dev/"
        )