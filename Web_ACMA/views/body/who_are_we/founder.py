import reflex as rx
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import (
    FOUNDER_SECTION_CONTAINER,
    FOUNDER_IMAGE_STYLE,
    FOUNDER_TEXT_CARD_STYLE,
    FOUNDER_SECTION_TITLE_STYLE, 
    INFO_TITLE_STYLE,
    INFO_TEXT_STYLE,
    INFO_SUBTITTLE_STYLE
)

# Esta función se encarga de dar estructura a la sección del fundador de ACMA
def founder() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título de arriba
            rx.heading("Nuestro Fundador", 
                style={
                    **FOUNDER_SECTION_TITLE_STYLE,
                    "font_size": ["2rem", "2.7rem"], 
                    "padding_x": "1rem"
                    }
                ),
            
            # Contenedor de imagen + tarjeta
            rx.flex(
                # Imagen a la izquierda
                rx.image(
                    src="WebMaster.jpg",
                    alt="Imagen del fundador",
                    style={
                        **FOUNDER_IMAGE_STYLE,
                        "width": ["200px", "350px"], 
                        "height": ["200px", "350px"],
                    }
                ),
                # Tarjeta a la derecha
                rx.vstack(
                    rx.heading("José Antonio Romero Paniagua", style=INFO_TITLE_STYLE),
                    rx.text("Fundador y Director de ACMA", style=INFO_SUBTITTLE_STYLE),
                    rx.text(
                        """ACMA nació bajo el respaldo de Jefatura de Estudios como un proyecto innovador dentro de la optativa Ciencias de la Computación. 
                        Nuestra misión es doble: facilitar la labor docente con materiales de alta calidad y ofrecer al alumno una experiencia laboral real 
                        sin añadir carga lectiva a la PAU. Aquí entrenamos el rigor profesional ayudando a nuestros profesores.""",
                        style=INFO_TEXT_STYLE,
                        text_align="justify"
                    ),
                    style={
                        **FOUNDER_TEXT_CARD_STYLE,
                        "width": "100%", 
                        "padding": ["1.5rem", "3rem"], 
                    },
                    align_items="start",
                    justify_content="center",
                ),
                style={
                    **FOUNDER_SECTION_CONTAINER,
                    "gap": ["1.5rem", "3rem"], 
                    "padding_x": ["1rem", "2rem"],
                },
                flex_direction=["column", "row"], 
                align_items="center",
            ),
            width="100%",
            max_width="1100px",
            align_items="center",
        ),
        width="100%",
    )