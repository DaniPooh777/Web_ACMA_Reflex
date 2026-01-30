import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.frecuent_questions_style import *

class FaqState(rx.State):
    opened_id: str = ""

    def toggle_faq(self, id: str):
        if self.opened_id == id:
            self.opened_id = ""
        else:
            self.opened_id = id

    def clean_state(self):
        """Resetea las FAQs al estado cerrado."""
        self.opened_id = ""

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
            "¿Cuánto tiempo tarda en completarse un encargo?",
            "El tiempo varía según la complejidad, pero generalmente entregamos en 5-10 días hábiles.",
            "q1"
        ),
        faq_item(
            "¿Puedo solicitar modificaciones después de recibir el recurso?",
            "Sí, ofrecemos una ronda de revisiones para asegurar que el contenido se ajuste perfectamente a tus necesidades.",
            "q2"
        ),
        faq_item(
            "¿Qué información necesito proporcionar para solicitar un recurso?",
            "Necesitamos conocer el tipo de recurso deseado, el tema específico, el nivel educativo y cualquier requisito especial de formato.",
            "q3"
        ),
        style=FAQ_CONTAINER_STYLE,
    )