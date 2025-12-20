import reflex as rx


HEADER_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": "3rem",    # Un poco más de aire arriba
    "padding_bottom": "0rem", # Espacio sutil antes de lo que sigue
    "align_items": "center",
    "text_align": "center",
}

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": "white",
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}

HEADER_TEXT_STYLE = {
    "font_size": "1.2rem",
    "color": "rgb(156, 163, 175)", # El gris exacto de la imagen
    "max_width": "750px",          # Evitamos que el texto se estire como un chicle
    "line_height": "1.6",
}