import reflex as rx
from Web_ACMA.styles.components_style.navbar_style import HERO_BUTTON_STYLE

"""Esta es la plantilla para crear el botón que funciona como link (no el de Zelda)"""


def link_button() -> rx.Component:
    return rx.link(
        rx.button("Nuevo encargo", style=HERO_BUTTON_STYLE),
        href="/contact#formulario-encargo",
        text_decoration="none",
        padding_top=["0.75rem", "1.25rem"],
    )
