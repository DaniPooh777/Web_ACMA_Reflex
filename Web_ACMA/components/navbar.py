# Web_ACMA/components/navbar.py
import reflex as rx
from Web_ACMA.state import NavState
from Web_ACMA.styles.colors import ACCENT_BLUE
from Web_ACMA.styles.components_style.navbar_style import (
    NAVBAR_STYLE,
    NAV_LINK_STYLE,
    NAV_BUTTON_STYLE,
    NAV_CENTER_HSTACK_STYLE,
    DRAWER_CONTENT_STYLE,
    DRAWER_CLOSE_BUTTON_STYLE,
    DRAWER_LINK_STYLE,
    DRAWER_BUTTON_STYLE,
    DRAWER_DIVIDER_STYLE,
    NAVBAR_LOGO_STYLE,
)


def drawer_link(text: str, url: str) -> rx.Component:
    """Link del drawer con estilo animado."""
    return rx.link(
        text,
        href=url,
        style=DRAWER_LINK_STYLE,
        on_click=NavState.close_drawer,
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
            spacing="6",
            style=NAV_CENTER_HSTACK_STYLE,
            display=["none", "none", "flex"],  # <--- OCULTO EN MÓVIL
        ),
        # DERECHA: Acciones y Menú
        rx.hstack(
            rx.color_mode.button(),
            # Botón "Nuevo encargo" (SOLO en Desktop)
            rx.link(
                rx.button("Nuevo encargo", **NAV_BUTTON_STYLE),
                href="/contact#formulario-encargo",
                display=["none", "none", "flex"],  # <--- OCULTO EN MÓVIL
            ),
            # DRAWER: Menú móvil fullscreen con animaciones
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon_button(
                        rx.icon(tag="menu", size=24),
                        variant="ghost",
                        size="3",
                        cursor="pointer",
                        display=["flex", "flex", "none"],
                        _hover={"color": ACCENT_BLUE},
                    )
                ),
                rx.drawer.portal(
                    rx.drawer.overlay(
                        rx.drawer.content(
                            # Botón cerrar - arriba a la derecha
                            rx.drawer.close(
                                rx.icon_button(
                                    rx.icon(tag="x", size=24),
                                    variant="ghost",
                                    size="3",
                                    style=DRAWER_CLOSE_BUTTON_STYLE,
                                )
                            ),
                            # Links centrados
                            rx.vstack(
                                drawer_link("Inicio", "/"),
                                drawer_link("Proyectos", "/project"),
                                drawer_link("Quiénes Somos", "/quienes-somos"),
                                drawer_link("Contacto", "/contact"),
                                rx.box(style=DRAWER_DIVIDER_STYLE),
                                rx.link(
                                    rx.button(
                                        "Nuevo encargo",
                                        style=DRAWER_BUTTON_STYLE,
                                    ),
                                    href="/contact#formulario-encargo",
                                    on_click=NavState.close_drawer,
                                ),
                                spacing="0",
                                align_items="center",
                                justify_content="start",
                                width="100%",
                            ),
                            style=DRAWER_CONTENT_STYLE,
                        ),
                        style={
                            "background_color": rx.color_mode_cond(
                                light="rgba(0, 0, 0, 0.5)",
                                dark="rgba(0, 0, 0, 0.7)",
                            ),
                            "position": "fixed",
                            "top": "0",
                            "left": "0",
                            "right": "0",
                            "bottom": "0",
                            "z_index": "9998",
                        },
                    )
                ),
                direction="right",
                open=NavState.drawer_open,
                on_open_change=NavState.set_drawer_open,
            ),
            spacing="4",
        ),
        **NAVBAR_STYLE,
    )
