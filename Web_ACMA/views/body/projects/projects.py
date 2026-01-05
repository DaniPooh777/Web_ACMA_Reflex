import reflex as rx
from Web_ACMA.components.project_card import project_card
from Web_ACMA.views.header.header import header
from Web_ACMA.styles.views_style.body_style.projects_style.project_style import (
    PROJECTS_CONTAINER_STYLE,
    CARDS_FLEX_STYLE,
    PROJECTS_SECTION_STYLE
)


def projects() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Tarjetas proyecto
            rx.flex(
                # ---PRIMERA FILA---
                project_card(
                    "p1", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "La Fe en el Marco del Pensamiento",
                    "Presentación interactiva en Genially sobre las principales religiones del mundo, con elementos multimedia y actividades."
                ),
                project_card(
                    "p2", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "El Mural de Manyanet",
                    "Póster motivacional y creativo sobre los distintos aspectos y valores que aprendemos en el Colegio Padre Manyanet Alcobendas."
                ),
                project_card(
                    "p3", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Vídeo del Acto de la Virgen",
                    "Un montaje de las distintas fotos que se realizaron durante el evento escolar."
                ),

                # ---SEGUNDA FILA---
                project_card(
                    "p4", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Inserte Título",
                    "Inserte descripción."
                ),
                project_card(
                    "p5", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Inserte Título",
                    "Inserte descripción."
                ),
                project_card(
                    "p6", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Inserte Título",
                    "Inserte descripción."
                ),
                **CARDS_FLEX_STYLE
            ),
            **PROJECTS_CONTAINER_STYLE
        ),
        **PROJECTS_SECTION_STYLE
    )