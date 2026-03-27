import reflex as rx
from Web_ACMA.styles.colors import *

NAV_CENTER_HSTACK_STYLE = {
    "position": "absolute",
    "left": "50%",
    "transform": "translateX(-50%)",
    "display": ["none", "none", "flex", "flex"],  # Responsive
    "align_items": "center",
    "justify_content": "center",
}

NAVBAR_STYLE = {
    "position": "sticky",
    "top": "0",
    "z_index": "999",
    "width": "100%",
    "padding_x": "2rem",
    "padding_y": "1rem",
    "background_color": rx.color_mode_cond(light=SOFT_NAVBAR, dark=DARK_NAVBAR),
    "border_bottom": rx.color_mode_cond(
        light=f"1px solid {SOFT_BORDER}", dark=f"1px solid {DARK_BORDER}"
    ),
    "backdrop_filter": "blur(10px)",
    "align_items": "center",
    "justify_content": "space-between",
}

# Estilos para los links de navegación
NAV_LINK_STYLE = {
    "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN),
    "text_decoration": "none",
    "font_size": ["1.1rem", "1.1rem", "0.9rem"],
    "font_weight": "500",
    "width": "100%",
    "white_space": "nowrap",
    "_hover": {
        "color": ACCENT_BLUE,  # Azul cuando pasás el mouse
        "transition": "0.3s",
    },
}

# Estilo para el botón de acción principal
NAV_BUTTON_STYLE = {
    "background_color": ACCENT_BLUE,
    "color": "white",
    "border_radius": "8px",
    "font_size": ["1.1rem", "1.1rem", "0.9rem"],
    "font_weight": "600",
    "padding_x": "1.5rem",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
        "transition": "all 0.2s ease-in-out",
    },
}

NAVBAR_LOGO_STYLE = {
    "font_weight": "bold",
    "font_size": ["1.2rem", "1.2rem", "1.2rem"],
    "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark="white"),
}

HERO_BUTTON_STYLE = {
    "background_color": "rgb(59, 130, 246)",
    "color": "white",
    "border_radius": "8px",
    "padding_x": ["1.5rem", "2.5rem"],
    "padding_y": ["1rem", "1.5rem"],
    "font_size": ["0.9rem", "1.1rem"],
    "font_weight": "600",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
        "transition": "all 0.2s ease-in-out",
    },
}

DRAWER_CONTENT_STYLE = {
    "background_color": rx.color_mode_cond(light="white", dark="#111827"),
    "height": "100vh",
    "width": "100vw",
    "padding": "2rem",
    "padding_top": "4rem",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "justify_content": "start",
    "gap": "0.5rem",
    "position": "fixed",
    "top": "0",
    "left": "0",
    "right": "0",
    "bottom": "0",
    "z_index": "9999",
    "overflow": "hidden",
}

DRAWER_CLOSE_BUTTON_STYLE = {
    "position": "absolute",
    "top": "1.5rem",
    "right": "1.5rem",
    "cursor": "pointer",
    "transition": "all 0.2s ease",
    "_hover": {
        "transform": "rotate(90deg)",
        "color": ACCENT_BLUE,
    },
}

DRAWER_LINK_STYLE = {
    "font_size": "1.15rem",
    "font_weight": "500",
    "color": rx.color_mode_cond(light=SOFT_TEXT_MAIN, dark=DARK_TEXT_MAIN),
    "text_decoration": "none",
    "transition": "all 0.3s ease",
    "padding": "0.875rem 2rem",
    "border_radius": "8px",
    "width": "fit_content",
    "min_width": "180px",
    "text_align": "center",
    "_hover": {
        "color": ACCENT_BLUE,
        "background_color": rx.color_mode_cond(
            light="rgba(59, 130, 246, 0.1)",
            dark="rgba(59, 130, 246, 0.15)",
        ),
    },
}

DRAWER_BUTTON_STYLE = {
    "background_color": ACCENT_BLUE,
    "color": "white",
    "font_size": "1.05rem",
    "font_weight": "600",
    "padding_x": "2.5rem",
    "padding_y": "1.25rem",
    "border_radius": "8px",
    "width": "fit_content",
    "min_width": "180px",
    "transition": "all 0.3s ease",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
        "transform": "translateY(-2px)",
        "box_shadow": "0 4px 15px rgba(59, 130, 246, 0.3)",
    },
}

DRAWER_DIVIDER_STYLE = {
    "width": "60%",
    "max_width": "200px",
    "border": "none",
    "border_top": f"1px solid {rx.color_mode_cond(light=SOFT_BORDER, dark=DARK_BORDER)}",
    "margin": "1rem 0",
}

NAVBAR_CONTAINER_STYLE = {
    "width": "100%",
    "padding": "1rem 2rem",
    "background_color": rx.color_mode_cond(
        light="rgba(255,255,255,0.8)", dark="rgba(0,0,0,0.8)"
    ),
    "backdrop_filter": "blur(10px)",
    "border_bottom": f"1px solid {SOFT_BORDER}",
    "align_items": "center",
}
