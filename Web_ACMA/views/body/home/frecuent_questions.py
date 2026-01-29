import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.frecuent_questions_style import (
    FAQ_CONTAINER_STYLE, FAQ_CARD_STYLE, FAQ_QUESTION_STYLE, FAQ_ANSWER_STYLE, HEADER_TITLE_STYLE
)

class FaqState(rx.State):
    # Diccionario para trackear qué pregunta está abierta
    opened_items: dict[str, bool] = {}

    def toggle_faq(self, id: str):
        self.opened_items[id] = not self.opened_items.get(id, False)

def faq_item(question: str, answer: str, id: str) -> rx.Component:
    is_open = FaqState.opened_items.get(id, False)
    
    return rx.vstack(
        rx.hstack(
            rx.text(question, style=FAQ_QUESTION_STYLE),
            rx.icon(
                tag="chevron-down",
                size=20,
                color="rgb(59, 130, 246)",
                transform=rx.cond(is_open, "rotate(180deg)", "rotate(0deg)"),
                transition="transform 0.3s ease",
            ),
            on_click=lambda: FaqState.toggle_faq(id),
            justify_content="space-between",
            width="100%",
        ),
        rx.cond(
            is_open,
            rx.text(answer, style=FAQ_ANSWER_STYLE),
        ),
        style=FAQ_CARD_STYLE,
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
            "¿Qué información necesito proporcionar para solicitar un recurso?",
            "Necesitamos conocer el tipo de recurso, el tema, el nivel educativo y cualquier material de referencia.",
            "q2"
        ),
        # Agregá las que falten de la imagen acá...
        style=FAQ_CONTAINER_STYLE,
    )