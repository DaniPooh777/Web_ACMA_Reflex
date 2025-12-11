import reflex as rx


def footer() -> rx.Component:
    return rx.vstack(
        rx.divider(),
        rx.hstack(
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
        ),
        rx.divider(),
        rx.text("© 2025 ACMA. Agencia de Contenido Manyanet."),
        width = "100%",
    )