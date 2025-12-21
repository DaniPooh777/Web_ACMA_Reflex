import reflex as rx
from Web_ACMA.components.information_card import information_card
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import WHO_ARE_WE_CONTAINER_STYLE

def information() -> rx.Component:
    return rx.vstack(
        # Tarjeta superior (Quiénes Somos)
        information_card(
            "Quiénes Somos",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            width="100%"
        ),
        # Contenedor para Misión y Visión
        rx.flex(
            information_card(
                "Misión",
                "Lorem Ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation.",
                width=["100%", "49%"] # Casi la mitad para que el gap no las rompa
            ),
            information_card(
                "Visión",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                width=["100%", "49%"]
            ),
            width="100%",
            justify_content="space-between", # Las pega a los bordes de la de arriba
            flex_wrap="wrap",
            gap="1rem",
        ),
        style=WHO_ARE_WE_CONTAINER_STYLE,
        width="100%",
        max_width="1000px", # <--- ESTO define el límite de la de arriba
        align_items="center", # <--- ESTO centra todo el bloque
        margin="0 auto", # Margen automático para centrar el bloque en la pantalla
    )