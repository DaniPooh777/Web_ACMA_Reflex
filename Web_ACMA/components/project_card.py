import reflex as rx
from Web_ACMA.state import ProjectCardState
from Web_ACMA.styles.views_style.body_style.projects_style.project_style import (
    CARD_STYLE,
    IMAGE_STYLE,
    CONTENT_CONTAINER_STYLE,
    HEADER_STYLE,
    TITLE_STYLE,
    ICON_STYLE,
    DESCRIPTION_CONTAINER_STYLE,
    DESCRIPTION_LABEL_STYLE,
    DESCRIPTION_TEXT_STYLE,
)

"""Esta es la plantilla para crear las tarjetas desplegables de los proyectos destacados de ACMA"""
def project_card(card_id: str, image_url: str, title: str, description: str) -> rx.Component:
    is_expanded = (ProjectCardState.opened_id == card_id) # La tarjeta está expandida si su ID coincide con el del estado
    
    return rx.box(
        # Tarjeta desplegable
        rx.vstack(
            # Imagen del trabajo
            rx.image(src=image_url, **IMAGE_STYLE), 

            # El resto de la tarjeta
            rx.box(
                # Sección de la tarjeta sin desplegar
                rx.hstack(
                    # Título del proyecto
                    rx.heading(title, **TITLE_STYLE),

                    # Icono flecha ^ que rota cuando la tarjeta de abre 
                    rx.icon(
                        tag="chevron-down",
                        **ICON_STYLE,
                        transform=rx.cond(is_expanded, "rotate(180deg)", "rotate(0deg)"),
                        transition="transform 0.4s ease-in-out",
                    ),
                    **HEADER_STYLE,
                    width="100%",
                ),

                # Sección de la tarjeta desplegada
                rx.box(
                    # Texto de la tarjeta desplegada
                    rx.text(
                        rx.text("Descripción: ", **DESCRIPTION_LABEL_STYLE),
                        rx.text(description, **DESCRIPTION_TEXT_STYLE),
                        **DESCRIPTION_CONTAINER_STYLE,
                    ),
                    max_height=rx.cond(is_expanded, "300px", "0px"),
                    opacity=rx.cond(is_expanded, "1", "0"),
                    transition="max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease-in-out",
                    overflow="hidden",
                    text_align="justify"
                ),
                **CONTENT_CONTAINER_STYLE,
                width="100%",
            ),
            spacing="0",
        ),
        # Hitbox total
        on_click=lambda: ProjectCardState.toggle_card(card_id),
        **CARD_STYLE,
        cursor="pointer",
    )