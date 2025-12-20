import reflex as rx

# Contenedor principal de la sección
SOLUTIONS_CONTAINER_STYLE = {
    "width": "100%",
    "padding_y": "4rem",
    "align_items": "center",
    "spacing": "6",
}

# Contenedor que agrupa las tarjetas
PROBLEMS_GRID_STYLE = {
    "display": "flex",
    "flex_direction": "row",
    "flex_wrap": "wrap",
    "justify_content": "center",
    "align_items": "stretch",
    "gap": "2rem",
    "width": "100%",
    "max_width": "1200px",
}

# La tarjeta física: Fondo oscuro y borde sutil
PROBLEM_CARD_STYLE = {
    "background_color": "rgba(17, 24, 39, 0.5)", # El tono oscuro de la imagen
    "border": "1px solid rgba(255, 255, 255, 0.1)", # Borde casi invisible
    "padding": "2rem",
    "border_radius": "16px",
    "width": ["100%", "100%", "50%", "550px"],
    "align_items": "start",
    "spacing": "4",
}