import reflex as rx

FOOTER_CONTAINER_STYLE = {
    "width": "100%",
    "padding_x": "2rem",
    "padding_y": "2rem",
    "background_color": "rgb(10, 10, 15)", # El oscuro de la captura
    "border_top": "2px solid rgba(255, 255, 255, 0.05)",
    "align_items": "center",
}

FOOTER_NAV_LINK_STYLE = {
    "color": "rgb(156, 163, 175)",
    "text_decoration": "none",
    "font_size": "0.9rem",
    "_hover": {
        "color": "rgb(59, 130, 246)",
        "transition": "0.3s",
    },
}

FOOTER_COPYRIGHT_STYLE = {
    "color": "rgb(156, 163, 175)",
    "font_size": "0.8rem",
    "margin_top": "3rem",
}