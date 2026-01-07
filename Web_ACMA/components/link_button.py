import reflex as rx
from Web_ACMA.styles.components_style.navbar_style import HERO_BUTTON_STYLE

def link_button() -> rx.Component:
    return rx.link(
        rx.button(
            "Nuevo encargo",
            style=HERO_BUTTON_STYLE 
        ),
        href="/contact#formulario-encargo",
        text_decoration="none",
        padding_top="2rem",
    )