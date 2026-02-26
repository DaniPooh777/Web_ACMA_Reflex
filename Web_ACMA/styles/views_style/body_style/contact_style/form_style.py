import reflex as rx
from Web_ACMA.styles.colors import *


FORM_CONTAINER_STYLE = {
    "width": "100%",
    "max_width": "824px",
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT, 
        dark=DARK_PAPER_SOFT
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark=f"1px solid {DARK_BORDER}"
    ),
    "padding": "2rem",
    "border_radius": "12px",
    "align_items": "stretch",
    "spacing": "3",
}

INPUT_STYLE = {
    "width": "100%",
    "height": "2.8rem",
    "background_color": rx.color_mode_cond(
        light=SOFT_INPUT,
        dark=DARK_INPUT
    ),
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN,
        dark=DARK_TEXT_MAIN
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark=f"1px solid {DARK_BORDER}"
    ),
    "border_radius": "8px", 
    "outline": "none !important",
    "transition": "all 0.2s ease-in-out",
    
    "& fieldset": { "border": "none" }, 
    "&:focus-within": {
        "border": f"0.5px solid {ACCENT_BLUE} !important",
        "box_shadow": f"0 0 0 1px {ACCENT_BLUE} !important",
    },
    
    "_autofill": {
        "transition": "background-color 5000s ease-in-out 0s",
        "text_fill_color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN),
    },
}

LABEL_STYLE = {
    "font_size": "0.9rem",
    "font_weight": "600",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN,
        dark=DARK_TEXT_MAIN
    ),
}

ATTACH_STYLE = {
    "position": "absolute",
    "bottom": "0.75rem",
    "right": "0.75rem",
    "color": rx.color_mode_cond(light=SOFT_TEXT_SECONDARY, dark=DARK_TEXT_SECONDARY),
    "z_index": "10",
    "_hover": {
        "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN), 
        "cursor": "pointer"
    },
}

SUBMIT_BUTTON_STYLE = {
    "width": "100%",
    "height": "3.2rem",
    "background_color": ACCENT_BLUE,
    "color": "white",
    "font_weight": "bold",
    "border_radius": "8px",
    "margin_top": "1rem",
    "_hover": {"background_color": "rgb(37, 99, 235)", "cursor": "pointer"},
}

UPLOAD_CLEAN_STYLE = {
    "border": "none",
    "padding": "0",
    "margin": "0",
}