import reflex as rx
from Web_ACMA.styles.views_style.body_style.home_style.frecuent_questions_style import (
    FAQ_CONTAINER_STYLE, FAQ_CARD_STYLE, FAQ_QUESTION_STYLE, FAQ_ANSWER_STYLE, FAQ_ITEM_INNER_STYLE, HEADER_TITLE_STYLE
)

class FaqState(rx.State):
    # Guardamos solo el ID de la que está abierta. Si es "", todas están cerradas.
    opened_id: str = ""

    def toggle_faq(self, id: str):
        # Si clickeás la que ya está abierta, la cerramos. Si no, abrimos la nueva.
        if self.opened_id == id:
            self.opened_id = ""
        else:
            self.opened_id = id

def faq_item(question: str, answer: str, id: str) -> rx.Component:
    # La condición ahora es: "¿Es mi ID el que está guardado en el estado?"
    is_open = (FaqState.opened_id == id)
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(question, style=FAQ_QUESTION_STYLE),
                rx.icon(
                    tag="chevron-down",
                    size=20,
                    color="rgb(59, 130, 246)",
                    transform=rx.cond(is_open, "rotate(180deg)", "rotate(0deg)"),
                    transition="transform 0.3s ease",
                ),
                justify_content="space-between",
                align_items="center",
                width="100%",
            ),
            rx.cond(
                is_open,
                rx.text(answer, style=FAQ_ANSWER_STYLE),
            ),
            style=FAQ_ITEM_INNER_STYLE,
            on_click=lambda: FaqState.toggle_faq(id),
        ),
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