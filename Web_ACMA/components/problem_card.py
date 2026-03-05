import reflex as rx
from Web_ACMA.styles.colors import *
from Web_ACMA.styles.views_style.body_style.home_style.problem_solutions_style import PROBLEM_CARD_STYLE

"""Esta es la plantilla para crear la tarjeta de problema-solución"""
def problem_card(tittle_1: str, text_1: str, tittle_2: str, text_2: str) -> rx.Component:
    return rx.vstack(
        # Sección Problema
        rx.text(tittle_1, color="rgb(239, 68, 68)", font_weight="bold", font_size="1.1rem", text_align="justify"),
        rx.text(
            text_1, 
            color=rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN), # Dinámico loco!
            font_size="0.95rem", 
            text_align=["left", "left", "justify"]
        ),
        
        # Línea divisoria sutil
        rx.divider(border_color=rx.color_mode_cond(light=SOFT_BORDER, dark=DARK_BORDER)),
        
        # Sección Solución
        rx.text(tittle_2, color="rgb(59, 130, 246)", font_weight="bold", font_size="1.1rem", text_align="justify"),
        rx.text(
            text_2, 
            color=rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN), # Dinámico!
            font_size="0.95rem", 
            text_align=["left", "left", "justify"]
        ),
        
        style=PROBLEM_CARD_STYLE
    )