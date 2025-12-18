import reflex as rx
from Web_ACMA.components.link_button import link_button
from Web_ACMA.styles.components_style.navbar_style import (
    NAVBAR_STYLE, 
    NAV_LINK_STYLE, 
    NAV_BUTTON_STYLE
)


def navbar() -> rx.Component:
    return rx.hstack(
        # Bloque Izquierdo: Logo y Nombre
        rx.hstack(
            rx.avatar(src="favicon.ico", size="3"),
            rx.text("ACMA", font_weight="bold", font_size="1.2rem", color="white"),
            align_items="center",
            spacing="3",
        ),
        
        # Bloque Central: Navegación (Solo se ve en desktop idealmente)
        rx.hstack(
            rx.link("Inicio", href="/", **NAV_LINK_STYLE),
            rx.link("Proyectos", href="/project", **NAV_LINK_STYLE),
            rx.link("Quiénes Somos", href="/quienes-somos", **NAV_LINK_STYLE),
            rx.link("Contacto", href="/contact", **NAV_LINK_STYLE),
            spacing="6",
            display=["none", "none", "flex", "flex"], # Responsive: oculto en móvil
        ),
        
        # Bloque Derecho: Botón de Acción
        rx.link(
            rx.button(
                "Solicite un nuevo encargo",
                **NAV_BUTTON_STYLE
            ),
            href="/contact#formulario-encargo",  # Apunta a tu formulario
            text_decoration="none",
        ),

        **NAVBAR_STYLE
    )