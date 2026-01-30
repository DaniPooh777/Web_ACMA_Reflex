import reflex as rx
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


class ProjectCardState(rx.State):
    """Estado local para las tarjetas de proyecto."""
    expanded_cards: dict[str, bool] = {}
    
    def toggle_card(self, card_id: str):
        """Alterna el estado de expansión de una tarjeta específica."""
        current_state = self.expanded_cards.get(card_id, False)
        self.expanded_cards[card_id] = not current_state


def project_card(card_id: str, image_url: str, title: str, description: str) -> rx.Component:
    is_expanded = ProjectCardState.expanded_cards.contains(card_id) & ProjectCardState.expanded_cards[card_id]
    
    return rx.box(
        rx.vstack(
            rx.image(src=image_url, **IMAGE_STYLE),
            rx.box(
                rx.hstack(
                    rx.heading(title, **TITLE_STYLE),
                    rx.icon(
                        tag="chevron-down",
                        **ICON_STYLE,
                        transform=rx.cond(is_expanded, "rotate(180deg)", "rotate(0deg)"),
                        transition="transform 0.4s ease-in-out",
                    ),
                    **HEADER_STYLE,
                    width="100%",
                ),
                rx.box(
                    # USAMOS UN SOLO TEXT CON SPANS ADENTRO PARA EVITAR SALTOS DE LÍNEA
                    rx.text(
                        rx.text("Descripción: ", **DESCRIPTION_LABEL_STYLE),
                        rx.text(description, **DESCRIPTION_TEXT_STYLE),
                        **DESCRIPTION_CONTAINER_STYLE,
                    ),
                    max_height=rx.cond(is_expanded, "300px", "0px"),
                    opacity=rx.cond(is_expanded, "1", "0"),
                    transition="max-height 0.6s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease-in-out",
                    overflow="hidden",
                ),
                **CONTENT_CONTAINER_STYLE,
                width="100%", 
            ),
            spacing="0",
        ),
        on_click=ProjectCardState.toggle_card(card_id),
        **CARD_STYLE,
        cursor="pointer",
    )