import reflex as rx
from Web_ACMA.styles.project_style import (
    CARD_STYLE,
    IMAGE_CONTAINER_STYLE,
    IMAGE_STYLE,
    CONTENT_CONTAINER_STYLE,
    HEADER_STYLE,
    TITLE_STYLE,
    ICON_STYLE,
    EXPANDABLE_CONTAINER_STYLE,
    DESCRIPTION_CONTAINER_STYLE,
    DESCRIPTION_LABEL_STYLE,
    DESCRIPTION_TEXT_STYLE,
)


class ProjectCardState(rx.State):
    """Estado local para las tarjetas de proyecto."""
    expanded_cards: dict[str, bool] = {}
    
    def toggle_card(self, card_id: str):
        """Alterna el estado de expansión de una tarjeta específica."""
        current_state = self.expanded_cards.get(card_id, False)
        self.expanded_cards[card_id] = not current_state


def project_card(
    card_id: str,
    image_url: str,
    title: str,
    description: str,
) -> rx.Component:
    """
    Componente de tarjeta expandible para proyectos.
    
    Args:
        card_id: Identificador único de la tarjeta
        image_url: URL de la imagen de fondo
        title: Título del proyecto
        description: Descripción que se muestra al expandir
    """
    return rx.box(
        # Área clickable: Imagen de fondo
        rx.box(
            rx.image(
                src=image_url,
                **IMAGE_STYLE
            ),
            on_click=ProjectCardState.toggle_card(card_id),
            **IMAGE_CONTAINER_STYLE
        ),
        # Contenedor del contenido
        rx.box(
            # Área clickable: Header con título y botón de expansión
            rx.box(
                rx.heading(
                    title,
                    **TITLE_STYLE
                ),
                rx.icon(
                    tag=rx.cond(
                        ProjectCardState.expanded_cards.contains(card_id) & ProjectCardState.expanded_cards[card_id],
                        "chevron-up",
                        "chevron-down"
                    ),
                    **ICON_STYLE
                ),
                on_click=ProjectCardState.toggle_card(card_id),
                **HEADER_STYLE
            ),
            # Contenido expandible con altura máxima y scroll
            rx.box(
                rx.cond(
                    ProjectCardState.expanded_cards.contains(card_id) & ProjectCardState.expanded_cards[card_id],
                    rx.box(
                        rx.text(
                            "Descripción del trabajo: ",
                            **DESCRIPTION_LABEL_STYLE
                        ),
                        rx.text(
                            description,
                            **DESCRIPTION_TEXT_STYLE
                        ),
                        **DESCRIPTION_CONTAINER_STYLE
                    ),
                ),
                max_height=rx.cond(
                    ProjectCardState.expanded_cards.contains(card_id) & ProjectCardState.expanded_cards[card_id],
                    "200px",
                    "0px"
                ),
                **EXPANDABLE_CONTAINER_STYLE
            ),
            **CONTENT_CONTAINER_STYLE
        ),
        **CARD_STYLE
    )