import reflex as rx
from Web_ACMA.components.information_card import information_card
from Web_ACMA.styles.views_style.body_style.who_are_we_style.who_are_we_style import WHO_ARE_WE_CONTAINER_STYLE, ORDER_CARD_STYLE

def information() -> rx.Component:
    return rx.vstack(
        # Tarjeta superior (Quiénes Somos)
        information_card(
            "Quiénes Somos",
            """ACMA (Agencia de Contenido de Manyanet Alcobendas) es un equipo creativo de alumnos de 2º de Bachillerato 
            de Ciencias de la Computación, encargado de crear contenido digital para el centro. Su misión es conceptualizar, 
            diseñar y desarrollar aplicaciones, material didáctico y de divulgación, especializándose en presentaciones 
            interactivas y asegurando la calidad en la documentación (técnica y académica) y el diseño gráfico. ACMA 
            funciona como un laboratorio para aplicar conocimientos, fomentar el pensamiento crítico, el trabajo en 
            equipo y el dominio de herramientas de desarrollo.""",
            width="100%"
        ),
        # Contenedor inferior para Misión y Visión
        rx.flex(
            information_card(
                "Misión",
                """Nuestra misión es simplificar la vida de los educadores, permitiéndoles centrarse en la conexión con 
                los estudiantes y la preparación pedagógica, y no en la carga administrativa. Aligeramos drásticamente 
                el trabajo, proporcionando herramientas y contenido para crear material didáctico digital de forma rápida 
                y de calidad. Así, los docentes invierten su tiempo en lo verdaderamente importante: la planificación, la 
                personalización, la interacción y la mentoría.""",
                width=["100%", "48%"]
            ),
            information_card(
                "Visión",
                """ACMA (Agencia de Contenido Manyanet Alcobendas) es un referente interno en excelencia digital. Alumnos de 
                2º de Bachillerato de Ciencias de la Computación crean soluciones digitales (apps, material didáctico, documentación) 
                que simplifican la labor pedagógica y liberan a los profesores de carga técnica. Fomenta talento digital, pensamiento 
                crítico y colaboración, impulsando la innovación educativa.""",
                width=["100%", "48%"]
            ),
            style=ORDER_CARD_STYLE
        ),
        style=WHO_ARE_WE_CONTAINER_STYLE
    )