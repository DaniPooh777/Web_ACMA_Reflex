import reflex as rx

NAV_CENTER_HSTACK_STYLE = {
    "position": "absolute",
    "left": "50%",
    "transform": "translateX(-50%)",
    "display": ["none", "none", "flex", "flex"], # Responsive
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
    "background_color": rx.color_mode_cond(
        light="rgba(255, 255, 255, 0.8)", # Un blanco transparente para el modo claro
        dark="rgba(17, 24, 39, 0.8)"      # El color exacto que vos querés para el oscuro
    ),
    "border_bottom": f"1px solid {rx.color('mauve', 4)}",
    "backdrop_filter": "blur(10px)",
    "align_items": "center",
    "justify_content": "space-between", 
}

# Estilos para los links de navegación
NAV_LINK_STYLE = {
    "color": rx.color("mauve", 12),
    "text_decoration": "none",
    "font_size": "0.9rem",
    "font_weight": "500",
    "_hover": {
        "color": rx.color("accent", 9),  # Azul cuando pasás el mouse
        "transition": "0.3s",
    },
}

# Estilo para el botón de acción principal
NAV_BUTTON_STYLE = {
    "background_color": "rgb(59, 130, 246)",
    "color": "white",
    "border_radius": "8px",
    "padding_x": "1.5rem",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
        "transition": "all 0.2s ease-in-out",
    },
}

HERO_BUTTON_STYLE = {
    "background_color": "rgb(59, 130, 246)",
    "color": "white",
    "border_radius": "8px",
    "padding_x": "2.5rem", 
    "padding_y": "1.5rem", 
    "font_size": "1.1rem", 
    "font_weight": "600",
    "cursor": "pointer",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
        "transition": "all 0.2s ease-in-out",
    },
}