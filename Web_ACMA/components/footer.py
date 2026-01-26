import reflex as rx
from Web_ACMA.styles.components_style.footer_style import (
    FOOTER_CONTAINER_STYLE,
    FOOTER_NAV_LINK_STYLE,
    FOOTER_COPYRIGHT_STYLE
)

def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # Bloque Izquierdo: Logo
            rx.hstack(
                rx.avatar(src="Acma Logo 2025-2026.png", size="3"),
                rx.text("ACMA", font_weight="bold", color="white", font_size="1.2rem"),
                align_items="center",
                spacing="3",
            ),
            
            rx.spacer(), 
            
            # Bloque Derecho: Navegación
            rx.hstack(
                rx.link("Inicio", href="/", **FOOTER_NAV_LINK_STYLE),
                rx.link("Proyectos", href="/project", **FOOTER_NAV_LINK_STYLE),
                rx.link("Quiénes somos", href="/quienes-somos", **FOOTER_NAV_LINK_STYLE),
                rx.link("Contacto", href="/contact", **FOOTER_NAV_LINK_STYLE),
                spacing="6",
            ),
            width="100%",
            max_width="1100px",
        ),
        
        rx.text(
            "© 2025 ACMA. Agencia de Contenido Manyanet Alcobendas.",
            **FOOTER_COPYRIGHT_STYLE
        ),
        
        style=FOOTER_CONTAINER_STYLE
    )