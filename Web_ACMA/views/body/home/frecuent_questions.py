import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.frecuent_questions_style import *
from Web_ACMA.state import FaqState


def faq_item(question: str, answer: str, id: str) -> rx.Component:
    is_open = (FaqState.opened_id == id)
    
    return rx.box(
        rx.vstack(
            # Header
            rx.hstack(
                rx.text(question, style=FAQ_QUESTION_STYLE),
                rx.icon(
                    tag="chevron-down",
                    size=20,
                    color="rgb(59, 130, 246)",
                    # Animación del icono también suave
                    transform=rx.cond(is_open, "rotate(180deg)", "rotate(0deg)"),
                    transition="transform 0.6s ease-in-out",
                ),
                justify_content="space-between",
                align_items="center",
                width="100%",
            ),
            
            # Contenedor de la Respuesta (El "túnel")
            rx.box(
                rx.text(answer, style=FAQ_ANSWER_STYLE),
                style=FAQ_ANSWER_ANIMATION_STYLE,
                # Usamos valores fijos para que el CSS pueda interpolar
                max_height=rx.cond(is_open, "300px", "0px"),
                opacity=rx.cond(is_open, "1", "0"),
            ),
            style=FAQ_ITEM_INNER_STYLE,
        ),
        # Hitbox total: el click está en la tarjeta
        on_click=lambda: FaqState.toggle_faq(id),
        style=FAQ_CARD_STYLE,
        margin_bottom="1rem",
    )

def frecuent_questions() -> rx.Component:
    return rx.vstack(
        rx.heading("Preguntas Frecuentes", style={**HEADER_TITLE_STYLE, "font_size": "2.5rem"}),
        faq_item(
            "¿Podéis imprimir trabajos como pósters o documentos?",
            "No. No está en nuestros servicios.",
            "q1"
        ),
        faq_item(
            "¿Podéis realizar algúna manualidad?",
            "No está dentro de nuestros servicios, solo trabajos digitales",
            "q2"
        ),
        faq_item(
            "¿Qué información necesito proporcionar para solicitar un trabajo?",
            """Necesitamos conocer el tipo de proyecto, qué quieres incluir, el estilo (opcional), 
            la fecha de entrega y algún ejemplo de trabajos similares que tengas para orientarnos.""",
            "q3"
        ),
        faq_item(
            "¿Qué tipos de trabajos digitales hacéis?",
            """Hacemos una gran variedad de trabajos: pósters, documentos, presentaciones, juegos,
            formularios, fotos, vídeos... Ahora estamos llevando a cabo una iniciativa para implementar
            la programación como uno de nuestros múltiples servicios. ¡Puedes pedirnos que programemos 
            algo para tu clase! Eso sí, llevará más tiempo que un encargo normal.""",
            "q4"
        ),
        style=FAQ_CONTAINER_STYLE,
    )