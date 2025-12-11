import reflex as rx
from Web_ACMA.components.link_button import link_button


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.avatar(
            src="favicon.ico",
            ),
            href = "/"
        ),
        rx.link(
            rx.text("ACMA", height = "40px"),
            href = "/"
        ),
        rx.link("Inicio", href="/"),
        rx.link("Proyecto", href="/project"),
        rx.link("Quiénes somos", href="/quienes-somos"), 
        rx.link("Contacto", href="/contact"),
        link_button(),
        position = "sticky",
        top = "0",
        bg = "blue",
        padding_x = "16px",
        padding_y = "10px",
        width = "100%",
        align_items="center",
        z_index="999"
    )