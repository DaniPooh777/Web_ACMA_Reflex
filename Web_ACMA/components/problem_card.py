import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.problem_solutions_style import PROBLEM_CARD_STYLE

def problem_card(tittle_1: str, text_1: str, tittle_2: str, text_2: str) -> rx.Component:
    return rx.vstack(
        # Sección Problema
        rx.text(tittle_1, color="rgb(239, 68, 68)", font_weight="bold", font_size="1.1rem"),
        rx.text(text_1, color="white", font_size="0.95rem"),
        
        # Línea divisoria sutil
        rx.divider(border_color="rgba(255, 255, 255, 0.05)"),
        
        # Sección Solución
        rx.text(tittle_2, color="rgb(59, 130, 246)", font_weight="bold", font_size="1.1rem"),
        rx.text(text_2, color="white", font_size="0.95rem"),
        
        style=PROBLEM_CARD_STYLE
    )