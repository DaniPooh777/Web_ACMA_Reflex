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
    # Verificamos si la tarjeta está expandida
    is_expanded = ProjectCardState.expanded_cards.contains(card_id) & ProjectCardState.expanded_cards[card_id]
    
    return rx.box(
        rx.box(
            rx.image(src=image_url, **IMAGE_STYLE),
            on_click=ProjectCardState.toggle_card(card_id),
            cursor="pointer",
        ),
        rx.box(
            rx.hstack(
                rx.heading(title, **TITLE_STYLE),
                rx.icon(
                    tag=rx.cond(is_expanded, "chevron-up", "chevron-down"),
                    **ICON_STYLE
                ),
                on_click=ProjectCardState.toggle_card(card_id),
                **HEADER_STYLE
            ),
            rx.box(
                rx.cond(
                    is_expanded,
                    rx.box(
                        rx.text("Descripción: ", **DESCRIPTION_LABEL_STYLE),
                        rx.text(description, **DESCRIPTION_TEXT_STYLE),
                        **DESCRIPTION_CONTAINER_STYLE
                    ),
                ),
                # Animación de altura
                max_height=rx.cond(is_expanded, "300px", "0px"),
                transition="max-height 0.4s ease-in-out",
                overflow="hidden",
            ),
            **CONTENT_CONTAINER_STYLE
        ),
        **CARD_STYLE
    )