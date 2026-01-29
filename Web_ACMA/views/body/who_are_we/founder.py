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
                    src="WebMaster.jpg",
                    style=FOUNDER_IMAGE_STYLE
                ),
                # Tarjeta a la derecha
                rx.vstack(
                    rx.heading("José Antonio Romero Paniagua", style=INFO_TITLE_STYLE),
                    rx.text(
                        "Fundador y Director de ACMA",
                        style=INFO_SUBTITTLE_STYLE
                    ),
                    rx.text(
                        """ACMA nació bajo el respaldo de Jefatura de Estudios como un proyecto innovador dentro de la optativa Ciencias de la Computación. 
                        Nuestra misión es doble: facilitar la labor docente con materiales de alta calidad y ofrecer al alumno una experiencia laboral real 
                        sin añadir carga lectiva a la PAU. Aquí entrenamos el rigor profesional ayudando a nuestros profesores.""",
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