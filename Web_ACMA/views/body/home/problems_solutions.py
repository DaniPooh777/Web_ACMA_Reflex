import reflex as rx
from Web_ACMA.components.problem_card import problem_card
from Web_ACMA.styles.views_style.body_style.home_style.problem_solutions_style import SOLUTIONS_CONTAINER_STYLE, PROBLEMS_GRID_STYLE
from Web_ACMA.styles.views_style.header_style.header_style import HEADER_TITLE_STYLE

# Esta función se encarga de dar estructura a la sección de soluciones a problemas que tienen los profesores.
def problem_solutions() -> rx.Component:
    return rx.vstack(
        # Título de la sección
        rx.heading(
            "Transforma tu Tiempo de Planificación", 
            style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}
        ),

        # Tarjetas de problema-solución
        rx.flex(
            problem_card(
                "Problema", 
                "Falta de creatividad a la hora de crear recursos como presentaciones, pósters, cuestionarios…", 
                "Solución", 
                "Podemos crear esos recursos con buena calidad y originalidad."
            ),
            problem_card(
                "Problema",
                "Falta de tiempo y de ganas para crear los recursos que imagináis hacer.",
                "Solución",
                "Ahorramos tiempo y ganas a los profesores."
            ),
            style=PROBLEMS_GRID_STYLE 
        ),
        style=SOLUTIONS_CONTAINER_STYLE,
        width="100%",
        background_color="rgb(10, 10, 15)"
    )