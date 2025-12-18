import reflex as rx

# Estilo para el contenedor del formulario
FORM_CONTAINER_STYLE = {
    "width": "100%",
    "padding": "2rem",
    "align_items": "start",
    # El truco de magia: 100px suele ser suficiente para saltar la navbar
    "scroll_margin_top": "100px", 
}

# Estilo para los inputs para que no se vean tan pegados
INPUT_STYLE = {
    "width": "100%",
    "margin_bottom": "1rem",
}