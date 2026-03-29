import reflex as rx
from datetime import datetime
from Web_ACMA.styles.colors import *
from Web_ACMA.styles.components_style.footer_style import (
    FOOTER_CONTAINER_STYLE,
    FOOTER_NAV_LINK_STYLE,
    FOOTER_COPYRIGHT_STYLE,
)

"""Esta es la plantilla para crear el footer"""


def footer() -> rx.Component:
    year = datetime.now().year

    return rx.vstack(
        rx.flex(
            # Bloque de Navegación (Ahora arriba en mobile)
            rx.hstack(
                rx.link("Inicio", href="/", **FOOTER_NAV_LINK_STYLE),
                rx.link("Proyectos", href="/project", **FOOTER_NAV_LINK_STYLE),
                rx.link(
                    "Quiénes somos", href="/quienes-somos", **FOOTER_NAV_LINK_STYLE
                ),
                rx.link("Contacto", href="/contact", **FOOTER_NAV_LINK_STYLE),
                rx.link("Política de Cookies", href="/cookies", **FOOTER_NAV_LINK_STYLE),
                spacing="6",
                justify_content="center",
                flex_wrap="wrap",
                width=["100%", "auto"],
                order=["1", "2"],  # <--- PRIMERO en mobile, SEGUNDO en desktop
            ),
            # Bloque del Logo (Al medio en mobile)
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.avatar(src="Acma Logo 2025-2026.png", size="3"),
                        rx.text(
                            "ACMA",
                            font_weight="bold",
                            color=rx.color_mode_cond(
                                light=SOFT_TEXT_MAIN, dark="white"
                            ),
                            font_size=["1rem", "1.2rem"],
                        ),
                        align_items="center",
                    ),
                    href="/",
                ),
                align_items="center",
                justify_content="center",
                width=["100%", "auto"],
                order=["2", "1"],  # <--- SEGUNDO en mobile, PRIMERO en desktop
            ),
            flex_direction=["column", "row"],  # Columna en mobile
            justify_content="space-between",
            align_items="center",
            spacing="6",
            width="100%",
            max_width="1100px",
        ),
        # Bloque inferior: Copyright (Siempre al final)
        rx.text(
            f"© {year} ACMA. Agencia de Contenido Manyanet Alcobendas.",
            **FOOTER_COPYRIGHT_STYLE,
            text_align="center",
            width="100%",
            order="3",  # <--- SIEMPRE ÚLTIMO
        ),
        style=FOOTER_CONTAINER_STYLE,
        width="100%",
        align_items="center",
    )
