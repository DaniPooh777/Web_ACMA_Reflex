import reflex as rx
import assets
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import (
    FOUNDER_SECTION_CONTAINER,
    FOUNDER_IMAGE_STYLE,
    FOUNDER_TEXT_CARD_STYLE,
    FOUNDER_SECTION_TITLE_STYLE, 
    INFO_TITLE_STYLE,
    INFO_TEXT_STYLE,
    INFO_SUBTITTLE_STYLE
)


def founder() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título de arriba
            rx.heading("Nuestro Fundador", style=FOUNDER_SECTION_TITLE_STYLE),
            
            # Contenedor de imagen + tarjeta
            rx.flex(
                # Imagen a la izquierda
                rx.image(
                    src="favicon.ico",
                    style=FOUNDER_IMAGE_STYLE
                ),
                # Tarjeta a la derecha
                rx.vstack(
                    rx.heading("José Antonio Romero Paniagua", style=INFO_TITLE_STYLE),
                    rx.text(
                        "Profesor y Director de ACMA",
                        style=INFO_SUBTITTLE_STYLE
                    ),
                    rx.text(
                        "Acá va toda la historia del fundador. Al estar fuera de la tarjeta, la imagen tiene su propio peso visual y la tarjeta de la derecha contiene solo el mensaje, tal cual pediste.",
                        style=INFO_TEXT_STYLE
                    ),
                    style=FOUNDER_TEXT_CARD_STYLE,
                    align_items="start",
                    justify_content="center",
                ),
                style=FOUNDER_SECTION_CONTAINER,
            ),
            width="100%",
            max_width="1100px",
            align_items="center",
        ),
        width="100%",
    )