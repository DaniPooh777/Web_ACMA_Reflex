import reflex as rx
from Web_ACMA.styles.colors import *

CONTACT_CARD_STYLE = {
    "width": ["100%", "100%", "50%", "550px"], 
    "max_width": "830px", 
    "background_color": rx.color_mode_cond(
        light=SOFT_PAPER_SOFT,  
        dark="rgba(17, 24, 39, 0.5)"
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}", 
        dark="1px solid rgba(255, 255, 255, 0.1)"
    ),
    "padding": "2rem",
    "border_radius": "12px",
    "transition": "all 0.3s ease",
}

ICON_CONTAINER_STYLE = {
    "background_color": "rgba(59, 130, 246, 0.1)",
    "padding": "0.75rem",
    "border_radius": "8px",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "margin_bottom": "1rem",
}

CARD_TITLE_STYLE = {
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark="white"
    ),
    "size": "6",
}

CARD_LINK_STYLE = {
    "color": "rgb(59, 130, 246)",
    "text_decoration": "none",
    "font_size": "0.9rem",
}

SCHEDULE_CARD_STYLE = {
    "width": "100%", 
    "max_width": "824px", 
    "background_color": "rgba(17, 24, 39, 0.5)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "padding": "2rem",
    "border_radius": "12px",
    "margin_top": "0rem",
}

INNER_SCHEDULE_STYLE = {
    "background_color": "rgba(255, 255, 255, 0.03)",
    "padding": "1.5rem",
    "border_radius": "8px",
    "width": "100%",
    "align_items": "start",
}

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark="white"
    ),
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}