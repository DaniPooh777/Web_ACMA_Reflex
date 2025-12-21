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
            rx.flex(
                # ---PRIMERA FILA---
                project_card(
                    "p1", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "La fe en el marco del pensamiento",
                    "Presentación interactiva en Genially sobre las principales religiones del mundo."
                ),
                project_card(
                    "p2", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "El Mural de Manyanet",
                    "Proyecto colaborativo de arte digital y físico para el colegio."
                ),
                project_card(
                    "p3", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Vídeo del Acto de la Virgen",
                    "Producción audiovisual completa del evento institucional de la paz."
                ),

                # ---SEGUNDA FILA---
                project_card(
                    "p4", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "La fe en el marco del pensamiento",
                    "Presentación interactiva en Genially sobre las principales religiones del mundo."
                ),
                project_card(
                    "p5", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "El Mural de Manyanet",
                    "Proyecto colaborativo de arte digital y físico para el colegio."
                ),
                project_card(
                    "p6", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
                    "Vídeo del Acto de la Virgen",
                    "Producción audiovisual completa del evento institucional de la paz."
                ),
                **CARDS_FLEX_STYLE
            ),
            **PROJECTS_CONTAINER_STYLE
        ),
        **PROJECTS_SECTION_STYLE
    )