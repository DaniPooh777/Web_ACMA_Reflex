import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.advantages_and_considerations_style import *

# =========
# COMPONENT
# =========

"""Esta es la plantila de la tabla"""
def table_row(icon: str, text: str, icon_color: str) -> rx.Component:
    return rx.hstack(
        rx.icon(tag=icon, color=icon_color, size=20),
        rx.text(text, color="#E2E8F0", font_size="0.95rem"),
        **ROW_STYLE
    )

# ===============
# VISTA PRINCIPAL
# ===============

"""Esta función se encarga de dar estructura a la sección de Beneficios y Consideraciones de trabajar con ACMA"""
def advantages_and_considerations() -> rx.Component:
    return rx.vstack(
        # Título de la sección
        rx.heading("Beneficios y Consideraciones de Trabajar con ACMA", style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}),

        # Tablas
        rx.flex(
            # Tabla de Beneficios
            rx.vstack(
                rx.text("Beneficios", color="#0ef56e", **TITLE_STYLE),
                table_row("check", "Hacemos cualquier tipo de contenido digital.", "#0ef56e"),
                table_row("check", "Trabajos de calidad.", "#0ef56e"),
                table_row("check", "Pedir todos los cambios necesarios para su satisfacción.", "#0ef56e"),
                table_row("check", "Respetamos las fechas límite.", "#0ef56e"),
                **TABLE_CONTAINER_STYLE
            ),
            # Tabla de Consideraciones
            rx.vstack(
                rx.text("Consideraciones", color="#f51b0b", **TITLE_STYLE),
                table_row("x", "No realizamos manualidades.", "#f51b0b"),
                table_row("x", "No imprimimos nada.", "#f51b0b"),
                table_row("x", "No realizamos trabajos para consumo propio, solo para el cole.", "#f51b0b"),
                **TABLE_CONTAINER_STYLE
            ),
            width="100%",
            justify="center",
            flex_wrap="wrap",
            gap="2rem",
            text_align="justify"
        ),
        **SECTION_CONTAINER_STYLE
    )