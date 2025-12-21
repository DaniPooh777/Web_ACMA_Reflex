import reflex as rx

# El contenedor padre que sostiene todo el quilombo
RESOURCES_SECTION_STYLE = {
    "width": "100%",
    "padding_y": "4rem",
    "background_color": "rgb(10, 10, 15)", # Fondo bien oscuro
    "align_items": "center",
}

# El Grid de las 4 tarjetas principales
RESOURCES_GRID_STYLE = {
    "display": "flex",
    "flex_wrap": "wrap",
    "justify_content": "center",
    "gap": "1.5rem",
    "width": "100%",
    "max_width": "1100px",
    "padding": "2rem",
}

# La tarjeta individual (La magia está acá)
RESOURCE_CARD_STYLE = {
    "width": ["100%", "240px"], # Responsive: full en mobile, fijo en desktop
    "height": "160px",
    "background_color": "rgba(17, 24, 39, 0.5)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "12px",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "justify_content": "center",
    "transition": "all 0.3s ease-in-out",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgba(30, 41, 59, 0.8)",
        "border_color": "rgb(59, 130, 246)", # El azul de ACMA
        "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1)",
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
    "font_size": "1.1rem",
    "font_weight": "600",
    "color": "white",
}