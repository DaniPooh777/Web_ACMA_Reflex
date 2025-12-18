import reflex as rx
from Web_ACMA.components.project_card import project_card
from Web_ACMA.views.header.header import header
from Web_ACMA.styles.views_style.body_style.projects_style.project_style import (
    PROJECTS_SECTION_STYLE,
    PROJECTS_CONTAINER_STYLE,
    CARDS_FLEX_STYLE,
)


def projects() -> rx.Component:
    """Vista con grid de proyectos expandibles."""
    return rx.box(
        rx.vstack(
            # Título de la sección
            header(
                "Nuestros Proyectos Más Relevantes",
                "Descubre algunos de los proyectos más destacados que hemos realizado para el profesorado."
            ),
            # Grid de tarjetas
            rx.flex(
                # Proyecto 1
                project_card(
                    card_id="proyecto_fe",
                    image_url="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    title="La fe en el marco del pensamiento",
                    description="Presentación interactiva en Genially sobre las principales religiones del mundo, con elementos multimedia y actividades.",
                ),
            ),
            **PROJECTS_CONTAINER_STYLE
        ),
        **PROJECTS_SECTION_STYLE
    )