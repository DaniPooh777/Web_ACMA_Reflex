import reflex as rx
from Web_ACMA.components.problem_card import problem_card


def problem_solutions() -> rx.Component:
    return rx.vstack(
        rx.heading("Transforma tu Tiempo de Planificación", size="8"),
        rx.hstack(
            problem_card(
                "Problema", 
                "Falta de creatividad a la hora de crear recursos como presentaciones, pósters, cuestionarios…", 
                "Solución", 
                "Podemos crear esos recursos con buena calidad y originalidad."
            ),
            problem_card(
                "Problema",
                "Falta de tiempo debido y no pueden crear los recursos antes mencionados.",
                "Solución",
                "Ahorramos tiempo a los profesores."
            )
        )
    )