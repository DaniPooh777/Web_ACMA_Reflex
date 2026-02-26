import reflex as rx
from Web_ACMA.styles.components_style.navbar_style import (
    NAVBAR_STYLE, 
    NAV_LINK_STYLE, 
    NAV_BUTTON_STYLE,
    NAV_CENTER_HSTACK_STYLE # 
)
from Web_ACMA.state import FormState

"""Esta es la plantilla para crear la navbar"""
def navbar() -> rx.Component:
    return rx.hstack(
        # Bloque Izquierdo: Logo
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.avatar(src="Acma Logo 2025-2026.png", size="3"),
                    rx.text("ACMA", font_weight="bold", color=rx.color("mauve", 12), font_size="1.2rem"),
                    align_items="center",
                ),                    
                href="/",
            ),
            align_items="center",
            spacing="3",
        ),
        
        # Bloque Central: Links 
        rx.hstack(
            rx.link("Inicio", href="/", **NAV_LINK_STYLE),
            rx.link("Proyectos", href="/project", **NAV_LINK_STYLE),
            rx.link("Quiénes Somos", href="/quienes-somos", **NAV_LINK_STYLE),
            rx.link("Contacto", href="/contact", **NAV_LINK_STYLE),
            spacing="6",
            style=NAV_CENTER_HSTACK_STYLE, 
        ),

        # Bloque Derecho: Botón
        rx.hstack(
            rx.color_mode.button(),
            # Bloque Derecho: Botón
            rx.link(
                rx.button(
                    "Nuevo encargo",
                    **NAV_BUTTON_STYLE
                ),
                href="/contact#formulario-encargo",
                text_decoration="none",
            )
        ),

        **NAVBAR_STYLE
    )