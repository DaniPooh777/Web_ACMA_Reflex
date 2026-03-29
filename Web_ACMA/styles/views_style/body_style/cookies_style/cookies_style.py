import reflex as rx
from Web_ACMA.styles.colors import *

# Contenedor principal de la sección de cookies
COOKIES_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": "2rem",
    "padding_bottom": "4rem",
    "align_items": "center",
    "spacing": "0",
    "max_width": "900px",
    "margin": "0 auto",
    "padding_x": ["1rem", "2rem", "0rem"],
}

# Estilo para la fecha de última modificación
COOKIES_DATE_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY,
        dark=DARK_TEXT_SECONDARY,
    ),
    "font_size": "0.95rem",
    "font_style": "italic",
    "text_align": "left",
    "align_self": "flex-start",
    "margin_bottom": "1rem",
    "padding_left": "0.5rem",
}

# Estilo para las tarjetas de cookies
COOKIES_CARD_STYLE = {
    "width": "100%",
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, dark="rgba(17, 24, 39, 0.5)"
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}", dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "padding": "2rem 2.5rem",
    "border_radius": "12px",
    "margin_bottom": "1.5rem",
    "text_align": "left",
}

# Título de las tarjetas (preguntas)
COOKIES_CARD_TITLE_STYLE = {
    "font_weight": "600",
    "color": ACCENT_BLUE,
    "font_size": "1.35rem",
    "margin_bottom": "1rem",
    "text_align": "left",
    "width": "100%",
}

# Subtítulo dentro de las tarjetas
COOKIES_SUBTITLE_STYLE = {
    "font_weight": "600",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN,
        dark=DARK_TEXT_MAIN,
    ),
    "font_size": "1rem",
    "margin_top": "1.25rem",
    "margin_bottom": "0.5rem",
    "text_align": "left",
    "width": "100%",
}

# Texto de las tarjetas
COOKIES_TEXT_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY,
        dark=DARK_TEXT_SECONDARY,
    ),
    "font_size": "0.95rem",
    "line_height": "1.7",
    "text_align": "left",
    "width": "100%",
}

# Texto en negrita para subtítulos inline
COOKIES_BOLD_TEXT_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN,
        dark=DARK_TEXT_MAIN,
    ),
    "font_size": "0.95rem",
    "font_weight": "600",
    "line_height": "1.7",
    "text_align": "left",
}

# Estilo para listas
COOKIES_LIST_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY,
        dark=DARK_TEXT_SECONDARY,
    ),
    "font_size": "0.95rem",
    "line_height": "1.8",
    "text_align": "left",
    "padding_left": "1.5rem",
    "width": "100%",
}
