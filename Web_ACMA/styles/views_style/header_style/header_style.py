import reflex as rx

HEADER_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": "5rem",    # Espacio generoso arriba para que no lo tape la navbar
    "padding_bottom": "0rem", # Espacio abajo antes de las tarjetas
    "align_items": "center",  # Centra el contenido horizontalmente
    "text_align": "center",   # Centra el texto
}

HEADER_TITLE_STYLE = {
    "font_size": "4rem",      # Tamaño masivo como en la imagen
    "font_weight": "800",     # Extra negrita
    "color": "white",
    "line_height": "1.2",
    "margin_bottom": "1rem",
}

HEADER_TEXT_STYLE = {
    "font_size": "1.2rem",
    "color": "rgb(156, 163, 175)", # Gris suave para el subtítulo
    "max_width": "600px",          # Para que el texto no se estire infinito a los costados
}