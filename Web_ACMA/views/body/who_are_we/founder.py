import reflex as rx
import assets
from Web_ACMA.components.information_card import information_card

def founder() -> rx.Component:
    return rx.vstack(
        rx.heading("Nuestro Fundador", size="8"),
        rx.hstack(
            rx.image(
                src="favicon.ico",
                width="200px", 
                height="auto"
            ),
            information_card(
                "José Antonio Romero Paniagua",
                "Fundador y Director de ACMA",
                "Párrafo haciendo la pelota a José Antonio."
            )
        )
    )