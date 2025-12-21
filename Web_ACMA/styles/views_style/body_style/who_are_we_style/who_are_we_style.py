import reflex as rx

# Contenedor principal de la sección
WHO_ARE_WE_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": "2rem",     
    "padding_bottom": "3rem",
    "align_items": "center",
    "spacing": "0",         
}

# Estilo de la tarjeta (Basado en el diseño de Contacto para consistencia)
INFO_CARD_STYLE = {
    "width": "100%",
    "background_color": "rgba(17, 24, 39, 0.5)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "padding": "3.5rem 2.5rem", # <--- Padding generoso para que el texto no asfixie
    "border_radius": "12px",
    "text_align": "center",
}

INFO_TITLE_STYLE = {
    "font_weight": "bold",
    "color": "rgb(59, 130, 246)", # El azul ACMA
    "margin_bottom": "1rem",
    "font_size": "1.5rem",
}

INFO_TEXT_STYLE = {
    "color": "rgb(156, 163, 175)", # Gris suave para lectura
    "font_size": "1rem",
    "line_height": "1.6",
}

# El contenedor que agrupa la imagen + la tarjeta
FOUNDER_SECTION_CONTAINER = {
    "width": "100%",
    "max_width": "1100px",
    "display": "flex",
    "flex_direction": ["column", "row"], # Columna en mobile, fila en desktop
    "align_items": "center",
    "justify_content": "center",
    "gap": "3rem", # El "aire" entre la imagen y la tarjeta
    "padding_y": "2rem",
}

FOUNDER_IMAGE_STYLE = {
    "width": ["250px", "350px"],
    "height": ["250px", "350px"],
    "border_radius": "20px",
    "object_fit": "cover",
    "box_shadow": "0px 10px 30px rgba(0, 0, 0, 0.5)",
    "border": "2px solid rgba(59, 130, 246, 0.5)",
}

# La tarjeta de texto (ahora sin la imagen adentro)
FOUNDER_TEXT_CARD_STYLE = {
    "flex": "1",
    "background_color": "rgba(17, 24, 39, 0.5)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "padding": "3rem",
    "border_radius": "15px",
    "text_align": "left",
}

FOUNDER_SECTION_TITLE_STYLE = {
    "font_weight": "bold",
    "color": "white", # O el azul ACMA rgb(59, 130, 246)
    "font_size": "2.7rem",
    "margin_top": "1rem",
    "text_align": "center",
    "width": "100%",
}