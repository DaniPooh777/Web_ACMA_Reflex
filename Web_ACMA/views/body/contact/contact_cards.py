import reflex as rx
from Web_ACMA.components.caracteristics_card import caracteristics_card 
from Web_ACMA.components.caracteristics_card_link import caracteristics_card_link 
from Web_ACMA.components.caracteristics_card_card import caracteristics_card_card 


def contact_cards() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            caracteristics_card_link(
                "Correo Electrónico",
                "acma@ejemplo.com", 
                "mail",
                "https://reflex.dev/"
            ),
            caracteristics_card(
                "Ubicación",
                "Sala de ordenadores secundaria Colegio Padre Manyanet.",
                "map_pin"
            )
        ),
        caracteristics_card_card(
                "Horario Presencial",
                "Martes y Jueves",
                "Miércoles y Viernes",
                "clock-4",
                "10:05 - 11:00",
                "12:25 - 13:20"
            )
    )