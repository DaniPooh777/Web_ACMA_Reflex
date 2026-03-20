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

# ==========
# COMPONENTE
# ==========

# Es la plantilla para crear tarjetas de colaborador (imagen + tarjeta con texto)
def collaborator_item(name: str, role: str, description: str, img_src: str) -> rx.Component:
    return rx.vstack(
        # Imagen arriba
        rx.image(src=img_src, style=COLLABORATOR_IMAGE_STYLE),

        # Tarjetas abajo
        rx.vstack(
            rx.heading(name, style=INFO_TITLE_STYLE),
            rx.text(role, style=INFO_SUBTITTLE_STYLE),
            rx.text(description, style=INFO_TEXT_STYLE, text_align="justify"),
            style=FOUNDER_TEXT_CARD_STYLE,
            align_items="start",
            width="100%",
        ),
        spacing="4",
        align_items="center",
        width="100%",
    )

# =========================================
# VISTA PRINCIPAL: SECCIÓN DE COLABORADORES
# =========================================

# Esta sección se encarga de organizar el layout de los colaboradores.
def collaborators() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título principal
            rx.heading("Nuestros Colaboradores Principales", 
                style={
                    **FOUNDER_SECTION_TITLE_STYLE,
                    "font_size": ["2rem", "2.7rem"], 
                    "padding_x": "1rem"
                }
            ),

            # Tarjetas + imágenes
            rx.flex(
                collaborator_item(
                    "Marcos Asenjo González", 
                    "Co-formador en ACMA", 
                    """La informática ha evolucionado mucho en los últimos años y décadas, y en este mundo cada vez más digital 
                    aparece la necesidad de contar con equipos que ayuden a los docentes en esta tarea. Mi papel como co-formador 
                    en ACMA consiste en proveer a los trabajadores de ACMA de la formación en programación, redes y sistemas para 
                    que las soluciones proporcionadas por nuestro equipo ya no consistan únicamente en soluciones de diseño, sino 
                    también soluciones técnicas a los problemas de la docencia.""",
                    "Foto Marcos.jpg" 
                ),
                collaborator_item(
                    "Daniel González Rodríguez", 
                    "Integrante y creador de la página web de ACMA", 
                    """Pieza clave en ACMA, no solo es el fundador de esta web, sino un integrante excepcional que ha elevado 
                    la calidad de nuestros trabajos. Su visión técnica nos llevó a GitHub, creando el espacio donde compartimos 
                    nuestros códigos creados en los múltiples proyectos que trabajamos, destacando el videojuego ROGUETHON que creó. 
                    Además, su labor publicitaria (¡especialmente en Primaria!) ha sido vital para generar esa confianza 
                    y cercanía que hoy nos une con los profesores.""",
                    "Foto Daniel.jpeg"
                ),
                style=COLLABORATOR_SECTION_CONTAINER,
            ),
            padding_x=["1.5rem", "2rem", "0rem"],
            width="100%",
            max_width="1100px",
            align_items="center",
        ),
        width="100%",
    )