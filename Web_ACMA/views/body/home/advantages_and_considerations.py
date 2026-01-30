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
                table_row("check-circle", "Recursos educativos a medida.", "#3b82f6"),
                table_row("check-circle", "Innovación pedagógica constante.", "#3b82f6"),
                table_row("check-circle", "Ahorro de tiempo para el docente.", "#3b82f6"),
                table_row("check-circle", "Soporte técnico especializado.", "#3b82f6"),
                **TABLE_CONTAINER_STYLE
            ),
            # Tabla de Consideraciones
            rx.vstack(
                rx.text("Consideraciones", color="#f51b0b", **TITLE_STYLE),
                table_row("info", "Requiere planificación previa.", "#f59e0b"),
                table_row("info", "Curva de aprendizaje en nuevas herramientas.", "#f59e0b"),
                table_row("info", "Dependencia de conectividad estable.", "#f59e0b"),
                table_row("info", "Proceso de feedback iterativo.", "#f59e0b"),
                **TABLE_CONTAINER_STYLE
            ),
            width="100%",
            justify="center",
            flex_wrap="wrap",
            gap="2rem",
        ),
        **SECTION_CONTAINER_STYLE
    )