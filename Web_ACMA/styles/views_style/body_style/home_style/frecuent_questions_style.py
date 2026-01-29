import reflex as rx

FAQ_CONTAINER_STYLE = {
    "width": "100%",
    "max_width": "824px",  # Alineado con tus otros formularios
    "padding_y": "4rem",
    "align_items": "center",
}

FAQ_CARD_STYLE = {
    "width": "100%",
    "background_color": "rgba(17, 24, 39, 0.5)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "12px",
    "overflow": "hidden", # Importante para que el click no se escape por los bordes
    "transition": "all 0.3s ease",
    "_hover": {
        "border_color": "rgba(59, 130, 246, 0.5)",
    },
}

FAQ_ITEM_INNER_STYLE = {
    "width": "100%",
    "padding": "1.5rem", # El padding se lo damos al contenido, no a la tarjeta
    "cursor": "pointer",
}

FAQ_QUESTION_STYLE = {
    "color": "white",
    "font_weight": "600",
    "font_size": "1.1rem",
    "user_select": "none",
}

FAQ_ANSWER_STYLE = {
    "color": "rgb(156, 163, 175)",
    "font_size": "1rem",
    "padding_top": "1rem",
    "line_height": "1.6",
}

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": "white",
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}