import reflex as rx

COLOR_BG_DARK = "rgb(10, 10, 15)"
COLOR_CARD_BG = "rgba(17, 24, 39, 0.5)"
COLOR_BORDER_INPUT = "rgba(255, 255, 255, 0.2)"
COLOR_BORDER_CONTAINER = "rgba(255, 255, 255, 0.1)"
COLOR_ACCENT = "rgb(59, 130, 246)" 
COLOR_INPUT_BG = "rgb(20, 24, 33)" 
COLOR_TEXT_GRAY = "rgb(156, 163, 175)"

FORM_CONTAINER_STYLE = {
    "width": "100%",
    "max_width": "824px",
    "background_color": rx.color_mode_cond(
        light=rx.color("mauve", 3),
        dark=COLOR_CARD_BG
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {rx.color('mauve', 4)}",
        dark=f"1px solid {COLOR_BORDER_CONTAINER}"
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
        light="white",
        dark=COLOR_INPUT_BG
    ),
    "border": rx.color_mode_cond(
        light=f"1px solid {rx.color('mauve', 6)}",
        dark=f"1px solid {COLOR_BORDER_INPUT}"
    ),
    "color": rx.color_mode_cond(
        light="black",
        dark="white"
    ),
    "border_radius": "8px", 
    "outline": "none !important",
    "transition": "all 0.2s ease-in-out",
    
    "& fieldset": { "border": "none" }, 
    "&:focus-within": {
        "border": f"0.5px solid {COLOR_ACCENT} !important", # Forzamos el azul
        "box_shadow": f"0 0 0 1px {COLOR_ACCENT} !important",
    },
    
    "_autofill": {
        "transition": "background-color 5000s ease-in-out 0s",
        "text_fill_color": "white",
    }, #
}

LABEL_STYLE = {
    "font_size": "0.9rem",
    "font_weight": "600",
    "color": rx.color_mode_cond(
        light=rx.color("mauve", 12),
        dark="white"
    ),
}

ATTACH_STYLE = {
    "position": "absolute",
    "bottom": "0.75rem",
    "right": "0.75rem",
    "color": COLOR_TEXT_GRAY,
    "z_index": "10",
    "_hover": {"color": rx.color('mauve', 12), "cursor": "pointer"
    },
}

SUBMIT_BUTTON_STYLE = {
    "width": "100%",
    "height": "3.2rem",
    "background_color": COLOR_ACCENT,
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