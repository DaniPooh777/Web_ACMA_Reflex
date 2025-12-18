import reflex as rx


def link_button() -> rx.Component:
    return rx.link(
        rx.button(
            "Solicite un nuevo encargo", 
        ),
        href="/contact#formulario-encargo",  # Redirige a la página de contacto
    )