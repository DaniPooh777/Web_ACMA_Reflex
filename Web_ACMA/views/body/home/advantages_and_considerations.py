import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.advantages_and_considerations_style import *

def table_row(icon: str, text: str, icon_color: str) -> rx.Component:
    return rx.hstack(
        rx.icon(tag=icon, color=icon_color, size=20),
        rx.text(text, color="gray.300", font_size="0.95rem"),
        **ROW_STYLE
    )

def advantages_and_considerations() -> rx.Component:
    return rx.vstack(
        rx.heading("Beneficios y Consideraciones de Trabajar con ACMA", style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}),
        rx.flex(
            # Tabla de Beneficios
            rx.vstack(
                rx.text("Beneficios", color="#0ef56e", **TITLE_STYLE),
                table_row("check", "Recursos educativos a medida.", "#0ef56e"),
                table_row("check", "Innovación pedagógica constante.", "#0ef56e"),
                table_row("check", "Ahorro de tiempo para el docente.", "#0ef56e"),
                table_row("check", "Soporte técnico especializado.", "#0ef56e"),
                **TABLE_CONTAINER_STYLE
            ),
            # Tabla de Consideraciones
            rx.vstack(
                rx.text("Consideraciones", color="#f51b0b", **TITLE_STYLE),
                table_row("x", "Requiere planificación previa.", "#f51b0b"),
                table_row("x", "Curva de aprendizaje en nuevas herramientas.", "#f51b0b"),
                table_row("x", "Dependencia de conectividad estable.", "#f51b0b"),
                table_row("x", "Proceso de feedback iterativo.", "#f51b0b"),
                **TABLE_CONTAINER_STYLE
            ),
            width="100%",
            justify="center",
            flex_wrap="wrap",
            gap="2rem",
        ),
        **SECTION_CONTAINER_STYLE
    )