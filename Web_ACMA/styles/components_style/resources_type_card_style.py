import reflex as rx

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": "white",
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}

# El Grid de las 4 tarjetas principales
RESOURCES_GRID_STYLE = {
    "display": "flex",
    "flex_wrap": "wrap",
    "justify_content": "center", # Esto ya lo teníamos para centrar
    "gap": "1.5rem",
    "width": "100%",
    "max_width": "1200px", # <--- IGUAL QUE LAS TARJETAS DE ARRIBA
    "margin_bottom": "0.5rem",
}

# La tarjeta individual (La magia está acá)
RESOURCE_CARD_STYLE = {
    "width": ["100%", "265px"], # Responsive: full en mobile, fijo en desktop
    "height": "140px",
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