import reflex as rx
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import (
    COLLABORATOR_IMAGE_STYLE,
    COLLABORATOR_SECTION_CONTAINER,
    FOUNDER_TEXT_CARD_STYLE,
    FOUNDER_SECTION_TITLE_STYLE,
    INFO_TITLE_STYLE,
    INFO_TEXT_STYLE,
    INFO_SUBTITTLE_STYLE
)

def collaborator_item(name: str, role: str, description: str, img_src: str) -> rx.Component:
    return rx.vstack(
        # Imagen arriba
        rx.image(src=img_src, style=COLLABORATOR_IMAGE_STYLE),

        # Tarjetas abajo
        rx.vstack(
            rx.heading(name, style=INFO_TITLE_STYLE),
            rx.text(role, style=INFO_SUBTITTLE_STYLE),
            rx.text(description, style=INFO_TEXT_STYLE),
            style=FOUNDER_TEXT_CARD_STYLE,
            align_items="start",
            width="100%",
        ),
        spacing="4",
        align_items="center",
        width="100%",
    )

def collaborators() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título principal
            rx.heading("Nuestros Colaboradores Principales", style=FOUNDER_SECTION_TITLE_STYLE),

            # Tarjetas + imágenes
            rx.flex(
                collaborator_item(
                    "Marcos Asenjo González", 
                    "Rol en ACMA", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
                    "favicon.ico" 
                ),
                collaborator_item(
                    "Daniel González Rodríguez", 
                    "Integrante y creador de la página web de ACMA", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
                    "favicon.ico"
                ),
                style=COLLABORATOR_SECTION_CONTAINER,
            ),
            width="100%",
            max_width="1100px",
            align_items="center",
        ),
        width="100%",
    )