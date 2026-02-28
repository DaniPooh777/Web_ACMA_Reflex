import reflex as rx
from datetime import datetime
from Web_ACMA.styles.colors import *
from Web_ACMA.styles.components_style.footer_style import (
    FOOTER_CONTAINER_STYLE,
    FOOTER_NAV_LINK_STYLE,
    FOOTER_COPYRIGHT_STYLE
)

"""Esta es la plantilla para crear el footer"""
def footer() -> rx.Component:
    year = datetime.now().year

    return rx.vstack(
        rx.hstack(
            # Bloque Izquierdo: Logo
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.avatar(src="Acma Logo 2025-2026.png", size="3"),
                        rx.text(
                            "ACMA", 
                            font_weight="bold", 
                            color=rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark="white"),
                            font_size="1.2rem"),
                        align_items="center",
                    ),                    
                    href="/",
                ),
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
        
        # Bloque inferior: Copyright
        rx.text(
            f"© {year} ACMA. Agencia de Contenido Manyanet Alcobendas.",
            **FOOTER_COPYRIGHT_STYLE
        ),
        
        style=FOOTER_CONTAINER_STYLE
    )