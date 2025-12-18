import reflex as rx

# NUEVO: Estilo para forzar el centro matemático
NAV_CENTER_HSTACK_STYLE = {
    "position": "absolute",
    "left": "50%",
    "transform": "translateX(-50%)",
    "display": ["none", "none", "flex", "flex"], # Responsive
    "align_items": "center",
    "justify_content": "center",
}

# Asegurate de que el NAVBAR_STYLE tenga position relative si no lo tiene
NAVBAR_STYLE = {
    "position": "sticky", # Ya lo tenés así
    "top": "0",
    "z_index": "999",
    "width": "100%",
    "padding_x": "2rem",
    "padding_y": "1rem",
    "background_color": "rgba(17, 24, 39, 0.8)",
    "backdrop_filter": "blur(10px)",
    "border_bottom": "1px solid rgba(255, 255, 255, 0.1)",
    "align_items": "center",
    "justify_content": "space-between", 
}

# Estilos para los links de navegación
NAV_LINK_STYLE = {
    "color": "rgb(156, 163, 175)",
    "text_decoration": "none",
    "font_size": "0.9rem",
    "font_weight": "500",
    "_hover": {
        "color": "rgb(59, 130, 246)",  # Azul cuando pasás el mouse
        "transition": "0.3s",
    },
}

# Estilo para el botón de acción principal
NAV_BUTTON_STYLE = {
    "background_color": "rgb(59, 130, 246)",
    "color": "white",
    "border_radius": "8px",
    "padding_x": "1.5rem",
    "_hover": {
        "background_color": "rgb(37, 99, 235)",
    },
}