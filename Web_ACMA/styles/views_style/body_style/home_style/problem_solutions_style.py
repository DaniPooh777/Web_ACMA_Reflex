import reflex as rx
from Web_ACMA.styles.colors import *

# Contenedor principal de la sección
SOLUTIONS_CONTAINER_STYLE = {
    "width": "100%",
    "padding_y": ["2rem", "4rem"], 
    "padding_x": ["1rem", "2rem"],
    "align_items": "center",
    "spacing": "6",
}

# Contenedor que agrupa las tarjetas
PROBLEMS_GRID_STYLE = {
    "display": "flex",
    "flex_direction": ["column", "row"], # Columna en mobile, fila en desktop
    "flex_wrap": "wrap",
    "justify_content": "center",
    "align_items": "stretch",
    "gap": ["1.5rem", "2rem"],
    "width": "100%",
    "max_width": "1200px",
}

# La tarjeta física: Fondo oscuro y borde sutil
PROBLEM_CARD_STYLE = {
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT,  
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark=f"1px solid {DARK_BORDER}"
    ),
    "padding": ["1.5rem", "2rem"],
    "border_radius": "16px",
    "width": "100%",
    "max_width": ["100%", "550px"],
    "align_items": "start",
    "spacing": "4",
}