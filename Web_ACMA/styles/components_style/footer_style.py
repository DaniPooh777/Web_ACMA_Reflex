import reflex as rx
from Web_ACMA.styles.colors import *

FOOTER_CONTAINER_STYLE = {
    "width": "100%",
    "padding_x": "2rem",
    "padding_y": "2rem",
    "border_top": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}",
        dark="2px solid rgba(255, 255, 255, 0.05)"
    ),
    "align_items": "center",
}

FOOTER_NAV_LINK_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark="rgb(156, 163, 175)"
    ),
    "text_decoration": "none",
    "font_size": "0.9rem",
    "_hover": {
        "color": ACCENT_BLUE,
        "transition": "0.3s",
    },
}

FOOTER_COPYRIGHT_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark="rgb(156, 163, 175)"
    ),
    "font_size": "0.8rem",
    "margin_top": "3rem",
}