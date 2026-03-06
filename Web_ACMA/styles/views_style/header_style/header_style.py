import reflex as rx
from Web_ACMA.styles.colors import *


HEADER_CONTAINER_STYLE = {
    "width": "100%",
    "padding_top": ["2rem", "3rem", "4rem"],    
    "padding_bottom": "0rem", 
    "padding_x": ["1rem", "2rem"],
    "align_items": "center",
    "text_align": "center",
}

HEADER_TITLE_STYLE = {
    "font_size": ["1.8rem", "2.2rem", "2.5rem"], # Mobile, Tablet, Desktop
    "font_weight": "800",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark=DARK_TEXT_MAIN   
    ),
    "line_height": "1.2",
    "margin_bottom": "1rem",
    "text_align": "center",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}

HEADER_TEXT_STYLE = {
    "font_size": ["1rem", "1.2rem"],
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_SECONDARY, 
        dark=DARK_TEXT_SECONDARY   
    ), 
    "max_width": "750px",          
    "line_height": "1.6",
}