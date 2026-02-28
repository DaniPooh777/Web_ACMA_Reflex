import reflex as rx
from Web_ACMA.styles.colors import *

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": rx.color_mode_cond(
        light=SOFT_TEXT_MAIN, 
        dark=DARK_TEXT_MAIN   
    ),
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}

ORDER_CARD_STYLE = {
    "width": "100%",
    "justify_content": "space-between", 
    "flex_wrap": "wrap",
    "max_width": "1150px"
}