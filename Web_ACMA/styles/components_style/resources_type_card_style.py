import reflex as rx
from Web_ACMA.styles.colors import *

HEADER_TITLE_STYLE = {
    "font_size": ["1.8rem", "2.2rem", "2.5rem"],
    "font_weight": "800",
    "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark="white"),
    "line_height": "1.2",
    "margin_bottom": "1.5rem",
    "white_space": "pre-line",
    "text_align": "center",
    "width": "100%",
}

# El Grid de las 4 tarjetas principales
RESOURCES_GRID_STYLE = {
    "display": "flex",
    "flex_wrap": "wrap",
    "justify_content": "center", 
    "gap": ["1rem", "1.5rem"],
    "width": "100%",
    "max_width": "1200px", 
    "padding_x": ["1rem", "2rem", "0rem"],
    "margin_bottom": "0.5rem",
    "white_space": "pre-line"
}

# La tarjeta individual
RESOURCE_CARD_STYLE = {
    "width": ["100%", "265px"], # Responsive: full en mobile, fijo en desktop
    "height": "140px",
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, # El gris/crema suave de tus tokens
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark=f"1px solid {DARK_BORDER}"
    ),
    "border_radius": "12px",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "justify_content": "center",
    "padding": "1.5rem",
    "transition": "all 0.3s ease-in-out",
    "cursor": "pointer",
    "_hover": {
        "transform": "translateY(-5px)",
        "background_color": rx.color_mode_cond(
            light=SOFT_PAPER_SOFT, 
            dark="rgba(30, 41, 59, 0.8)"
        ),
        "border_color": ACCENT_BLUE,
    },
}

# Estilo para el icono dentro de la tarjeta
RESOURCE_ICON_STYLE = {
    "size": 40,
    "color": "rgb(59, 130, 246)",
    "margin_bottom": "1rem",
    "background_color": "rgba(59, 130, 246, 0.1)",
    "padding": "0.5rem",
    "border_radius": "8px",
}

# Estilo para el texto de la tarjeta
RESOURCE_TEXT_STYLE = {
    "font_size": ["1rem", "1.1rem"],
    "font_weight": "600",
    "text_align": "center",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark="white"
    ),
}