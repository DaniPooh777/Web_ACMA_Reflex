import reflex as rx
from Web_ACMA.styles.components_style.resources_type_card_style import RESOURCE_CARD_STYLE

def example_resources_type_card(url: str) -> rx.Component:
    # Creamos una copia para no romper el estilo original de las otras tarjetas
    custom_style = RESOURCE_CARD_STYLE.copy()
    custom_style.update({
        "width": ["100%", "550px"], # Ahora sí, pisamos el valor original
        "height": "auto",
        "padding": "1.5rem",
        "cursor": "default",    
        "_hover": {},
    })

    return rx.vstack(
        rx.text(
            "Visualización", 
            color="rgb(59, 130, 246)", 
            font_weight="bold", 
            font_size="1.1rem"
        ),
        rx.box(
            rx.image(
                src=url,
                alt="Vista previa del recurso",
                width="100%",
                height="400px",
                object_fit="contain",
                border_radius="8px",
            ),
            padding="1rem",
            background="rgba(255, 255, 255, 0.03)",
            border_radius="12px",
            width="100%",
        ),
        style=custom_style # Aplicamos el diccionario ya corregido
    )