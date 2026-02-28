import reflex as rx
from Web_ACMA.styles.colors import *

FAQ_CONTAINER_STYLE = {
    "width": "100%",
    "max_width": "824px",
    "padding_y": "4rem",
    "align_items": "center",
}

FAQ_CARD_STYLE = {
    "width": "100%",
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, 
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}", 
        dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "border_radius": "12px",
    "overflow": "hidden",
    "transition": "all 0.3s ease-in-out",
    "cursor": "pointer",
    "_hover": {
        "border_color": ACCENT_BLUE, 
        "background_color": rx.color_mode_cond(
            light="rgba(238, 234, 225, 0.7)", 
            dark="rgba(17, 24, 39, 0.7)"
        ),
    },
}

# Este es el contenedor que recibe el click y tiene el padding general
FAQ_ITEM_INNER_STYLE = {
    "width": "100%",
    "padding_x": "1.5rem",
    "padding_top": "2rem",
    "padding_bottom": "1.2rem",
}

FAQ_QUESTION_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN,
        dark="white"
    ),
    "font_weight": "600",
    "font_size": "1.1rem",
    "user_select": "none",
}

# La magia está acá: Animamos solo lo necesario
FAQ_ANSWER_ANIMATION_STYLE = {
    "transition": "max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease-in-out",
    "overflow": "hidden",
}

FAQ_ANSWER_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark="rgb(156, 163, 175)"
    ),
    "font_size": "1rem",
    "line_height": "1.6",
    "padding_top": "1rem", 
}

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark="white"), 
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}