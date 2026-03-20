# Web_ACMA/components/navbar.py
import reflex as rx
from Web_ACMA.state import NavState # Asegurate de tener el NavState que creamos
from Web_ACMA.styles.components_style.navbar_style import (
    NAVBAR_STYLE, 
    NAV_LINK_STYLE, 
    NAV_BUTTON_STYLE,
    NAV_CENTER_HSTACK_STYLE,
    DRAWER_CONTENT_STYLE, # El que agregamos antes
    NAVBAR_LOGO_STYLE
)

def drawer_link(text: str, url: str) -> rx.Component:
    """Esta es la función que te faltaba definir."""
    return rx.link(
        text, 
        href=url, 
        style=NAV_LINK_STYLE, 
        on_click=NavState.close_drawer # <--- Esto hace que se cierre al pinchar
    )

def navbar() -> rx.Component:
    return rx.hstack(
        # LADO IZQUIERDO: Logo (Siempre visible)
        rx.link(
            rx.hstack(
                rx.avatar(src="Acma Logo 2025-2026.png", size="3"),
                rx.text("ACMA", style=NAVBAR_LOGO_STYLE),
                align_items="center",
            ),                    
            href="/",
        ),
        
        # CENTRO: Links (SOLO en Desktop: none en móvil, flex en PC)
        rx.hstack(
            rx.link("Inicio", href="/", **NAV_LINK_STYLE),
            rx.link("Proyectos", href="/project", **NAV_LINK_STYLE),
            rx.link("Quiénes Somos", href="/quienes-somos", **NAV_LINK_STYLE),
            rx.link("Contacto", href="/contact", **NAV_LINK_STYLE),
            spacing="3",
            style=NAV_CENTER_HSTACK_STYLE,
            display=["none", "none", "flex"], # <--- OCULTO EN MÓVIL
        ),

        # DERECHA: Acciones y Menú
        rx.hstack(
            rx.color_mode.button(),
            
            # Botón "Nuevo encargo" (SOLO en Desktop)
            rx.link(
                rx.button("Nuevo encargo", **NAV_BUTTON_STYLE),
                href="/contact#formulario-encargo",
                display=["none", "none", "flex"], # <--- OCULTO EN MÓVIL
            ),

            # DRAWER: Menú hamburguesa (SOLO en Móvil: flex en móvil, none en PC)
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon(
                        tag="menu", 
                        cursor="pointer", 
                        size=30, 
                        display=["flex", "flex", "none"] # <--- SOLO MÓVIL
                    )
                ),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.drawer.close(
                                rx.box(rx.icon(tag="x"), cursor="pointer", width="100%", text_align="right")
                            ),
                            drawer_link("Inicio", "/"),
                            drawer_link("Proyectos", "/project"),
                            drawer_link("Quiénes Somos", "/quienes-somos"),
                            drawer_link("Contacto", "/contact"),
                            rx.divider(width="100%"),
                            rx.link(
                                rx.button("Nuevo encargo", width="100%", color_scheme="blue", size="4"),
                                href="/contact#formulario-encargo",
                                on_click=NavState.close_drawer,
                            ),
                            spacing="5",
                            align_items="start",
                        ),
                        style=DRAWER_CONTENT_STYLE,
                    )
                ),
                direction="right",
                open=NavState.drawer_open,
                on_open_change=NavState.set_drawer_open,
            ),
            spacing="4",
        ),
        **NAVBAR_STYLE 
    )
    