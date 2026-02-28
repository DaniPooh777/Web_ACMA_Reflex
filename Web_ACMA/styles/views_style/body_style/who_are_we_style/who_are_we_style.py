import reflex as rx
from Web_ACMA.styles.colors import *

# Contenedor principal de la sección
WHO_ARE_WE_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": "2rem",     
    "padding_bottom": "3rem",
    "align_items": "center",
    "spacing": "0",  
    "max_width": "1100px",   
    "align_items": "center",
    "margin": "0 auto", 
}

ORDER_CARD_STYLE = {
    "width": "100%",
    "justify_content": "space-between", 
    "flex_wrap": "wrap",
    "margin_top": "1.5rem",
}
 
INFO_CARD_STYLE = {
    "width": "100%",
    "background_color": rx.color_mode_cond(
                light=SOFT_PAPER_SOFT, 
                dark="rgba(17, 24, 39, 0.5)"
            ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "padding": "3.5rem 2.5rem",
    "border_radius": "12px",
    "text_align": "center",
}

INFO_TITLE_STYLE = {
    "font_weight": "bold",
     "color": "rgb(59, 130, 246)", # El azul ACMA
    "margin_bottom": "0.5rem",
    "font_size": "1.5rem",
}

INFO_SUBTITTLE_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark=DARK_TEXT_MAIN,
    ), 
    "font_size": "1.2rem",
    "line_height": "2",
    "margin_bottom": "0.5rem",
}

INFO_TEXT_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark=DARK_TEXT_SECONDARY,
    ),
    "font_size": "1rem",
    "line_height": "1.6",
}

# El contenedor que agrupa la imagen + la tarjeta
FOUNDER_SECTION_CONTAINER = {
    "width": "100%",
    "max_width": "1100px",
    "display": "flex",
    "flex_direction": ["column", "row"], 
    "align_items": "center",
    "justify_content": "center",
    "gap": "3rem", 
    "padding_y": "2rem",
}

FOUNDER_IMAGE_STYLE = {
    "width": ["250px", "350px"],
    "height": ["250px", "350px"],
    "border_radius": "65px",
    "object_fit": "cover",
}

FOUNDER_TEXT_CARD_STYLE = {
    "flex": "1",
    "background_color": rx.color_mode_cond(
                light=SOFT_PAPER_SOFT, 
                dark="rgba(17, 24, 39, 0.5)"
            ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "padding": "3rem",
    "border_radius": "15px",
    "text_align": "left",
}

FOUNDER_SECTION_TITLE_STYLE = {
    "font_weight": "bold",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark=DARK_TEXT_MAIN,
    ),
    "font_size": "2.7rem",
    "margin_top": "1rem",
    "text_align": "center",
    "width": "100%",
}

COLLABORATOR_SECTION_CONTAINER = {
    "width": "100%",
    "max_width": "1100px",
    "display": "flex",
    "flex_direction": ["column", "row"], # Columna en mobile, fila en desktop
    "align_items": "center",
    "text_align": "center",
    "justify_content": "center",
    "gap": "2rem",
    "padding_y": "2rem",
}

COLLABORATOR_IMAGE_STYLE = {
    "width": "100%",
    "height": "350px",
    "border_radius": "12px",
    "object_fit": "cover",
    "margin_bottom": "1rem"
}