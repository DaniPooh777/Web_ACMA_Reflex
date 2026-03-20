import reflex as rx
from Web_ACMA.styles.colors import *

# Estilos para la tarjeta de proyecto
CARD_STYLE = {
    "width": ["100%", "360px"], 
    "max_width": "100%", 
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, 
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "border_radius": "12px",
    "overflow": "hidden",
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "transition": "all 0.3s ease",
    "_hover": {
        "transform": "translateY(-5px)",
        "border": "1.5px solid rgb(59, 130, 246)", 
    }
}

# Estilos para la imagen de la tarjeta
IMAGE_CONTAINER_STYLE = {
    "cursor": "pointer",
    "_hover": {
        "opacity": "0.9",
    },
    "transition": "opacity 0.2s ease",
}

IMAGE_STYLE = {
    "width": "100%",
    "height": "200px",
    "object_fit": "cover",
    "transition": "opacity 0.2s ease",
}

# Estilos para el contenedor de contenido
CONTENT_CONTAINER_STYLE = {
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, 
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "display": "flex",
    "flex_direction": "column",
}

# Estilos para el header
HEADER_STYLE = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "center",
    "padding": "1.5rem",
    "cursor": "pointer",
    "flex_shrink": "0",
}

# Estilos para el título
TITLE_STYLE = {
    "size": "6",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark="white"
    ),
    "weight": "medium",
}

# Estilos para el ícono
ICON_STYLE = {
    "size": 24,
    "color": "rgb(59, 130, 246)",
}

# Estilos para el contenedor expandible
EXPANDABLE_CONTAINER_STYLE = {
    "overflow_y": "auto",
    "transition": "max-height 0.3s ease-out",
}

# Estilos para el contenido de descripción
DESCRIPTION_CONTAINER_STYLE = {
    "padding": "0 1.5rem 1.5rem 1.5rem",
    "opacity": "1", 
    "animation": "fadeIn 0.3s ease-out forwards",
}

# Estilos para el label de descripción
DESCRIPTION_LABEL_STYLE = {
    "as_": "span",
    "color": "rgb(59, 130, 246)",
    "font_weight": "600",
}

# Estilos para el texto de descripción
DESCRIPTION_TEXT_STYLE = {
    "as_": "span",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark=DARK_TEXT_SECONDARY
    ),
}

# Estilos para la sección de proyectos
PROJECTS_SECTION_STYLE = {
    "width": "100%",
}

PROJECTS_CONTAINER_STYLE = {
    "padding_top": "4rem",
    "align_items": "center",
    "width": "100%",
}

# Estilos para el flex container de tarjetas
CARDS_FLEX_STYLE = {
    "flex_wrap": "wrap",
    "spacing": "6",
    "justify_content": "center",
    "align_items": "stretch", 
    "width": "100%",
    "max_width": "1200px",
    "padding_x": ["1rem", "2rem"], 
}