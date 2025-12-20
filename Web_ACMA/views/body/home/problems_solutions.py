import reflex as rx
from Web_ACMA.components.problem_card import problem_card
from Web_ACMA.styles.views_style.body_style.home_style.problem_solutions_style import (
    SOLUTIONS_CONTAINER_STYLE,
    PROBLEMS_GRID_STYLE
)
from Web_ACMA.styles.views_style.header_style.header_style import HEADER_TITLE_STYLE


def problem_solutions() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Transforma tu Tiempo de Planificación", 
            style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}
        ),
        # EL FLEX ES EL PADRE DIRECTO DE LAS TARJETAS
        rx.flex(
            problem_card(
                "Problema", 
                "Falta de creatividad a la hora de crear recursos como presentaciones,\n pósters, cuestionarios…", 
                "Solución", 
                "Podemos crear esos recursos con buena calidad y originalidad."
            ),
            problem_card(
                "Problema",
                "Falta de tiempo y de ganas y no pueden crear los recursos que quieras.",
                "Solución",
                "Ahorramos tiempo y ganas a los profesores."
            ),
            style=PROBLEMS_GRID_STYLE # <--- ACÁ VA LA MAGIA
        ),
        style=SOLUTIONS_CONTAINER_STYLE,
        width="100%",
    )