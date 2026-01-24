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
                    "p1", "La Fe en el Marco del Pensamiento.png",
                    "La Fe en el Marco del Pensamiento",
                    "Presentación interactiva en Genially sobre las principales religiones del mundo, con elementos multimedia y actividades."
                ),
                project_card(
                    "p2", "Tarjeta Horizontal Feliz Navidad.png",
                    "Tarjeta Horizontal Feliz Navidad",
                    "Tatjeta navideña diseñada para desear feliz Navidad a todos."
                ),
                project_card(
                    "p3", "Día de la Paz.png",
                    "Vídeo del Acto de la Virgen",
                    "Un montaje de las distintas fotos que se realizaron durante el evento escolar."
                ),

                # ---SEGUNDA FILA---
                project_card(
                    "p4", "Nomas de convivencia.png",
                    "Normas de Convivencia",
                    "Normas de convivencia para el buen uso del taller y para garantizar la seguridad de los alumnos."
                ),
                project_card(
                    "p5", "Horario Enfermería.png",
                    "Horario Enfermería",
                    "Un cartel innovador para informar de cuándo está abierto la enfermería. "
                ),
                project_card(
                    "p6", "Uno Morfología.png",
                    "Uno Morfología",
                    "Actividad lúdica sobre la morfología en el formato del famoso juego de mesa (UNO) para que los estudiantes repasen los contenido de una forma innovadora."
                ),

                # ---TERCERA FILA---
                project_card(
                    "p7", "Horario Secretaría.png",
                    "Horario Secretaría",
                    "Para que cualquiera sepa cuándo está abierto secretaría. Está hecho de tal forma que sea muy visual y bonita."
                ),
                project_card(
                    "p8", "Formulario Internet - Security and responsibility.png",
                    "Formulario Internet",
                    "Un breve formulario con preguntas para evaluar el conocimiento de los alumnos sobre la seguridad en internet."
                ),
                project_card(
                    "p9", "Mural.jpeg",
                    "El Mural de Manyanet",
                    "Póster motivacional y creativo sobre los distintos aspectos y valores que aprendemos en el Colegio Padre Manyanet Alcobendas."
                ),
                **CARDS_FLEX_STYLE
            ),
            **PROJECTS_CONTAINER_STYLE
        ),
        **PROJECTS_SECTION_STYLE
    )