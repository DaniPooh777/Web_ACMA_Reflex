import reflex as rx
from Web_ACMA.components.caracteristics_card import caracteristics_card


def caracteristics() -> rx.Component:
    return rx.vstack(
        rx.heading("Tu Clase, Impulsada por la Calidad", size="8"),
        rx.hstack(
            caracteristics_card(
                "Calidad intachable de los trabajos", 
                "Garantizamos recursos de máxima calidad profesional para tus clases.",
                "shield" 
            ),
            caracteristics_card(
                "Más tiempo para planificar",
                "Dedica más tiempo a lo que importa: planificar tus clases.",
                "clock-4"
            ),
            caracteristics_card(
                "Recursos interactivos",
                "No te preocupes por crear recursos interactivos, nosotros lo hacemos.",
                "sparkles"
            )
        )
    )