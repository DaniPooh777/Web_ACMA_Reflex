import reflex as rx
from Web_ACMA.styles.components_style.navbar_style import HERO_BUTTON_STYLE

def link_button() -> rx.Component:
    return rx.link(
        rx.button(
            "Solicite un nuevo encargo",
            style=HERO_BUTTON_STYLE # <--- PONETE LAS PILAS ACÁ
        ),
        href="/contact#formulario-encargo",
        text_decoration="none",
        padding_top="2rem",
    )