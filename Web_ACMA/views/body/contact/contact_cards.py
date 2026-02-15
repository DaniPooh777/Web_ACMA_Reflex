import reflex as rx
from Web_ACMA.components.caracteristics_card import caracteristics_card 
from Web_ACMA.components.caracteristics_card_link import caracteristics_card_link 
from Web_ACMA.components.caracteristics_card_card import caracteristics_card_card

# Esta función se encarga de dar estructura a la sección de las distintas tarjetas para contactar a ACMA
def contact_cards() -> rx.Component:
    return rx.vstack(
        # Tarjetas superiores
        rx.hstack(
            # Tarjeta izquierda: Correo Electrónico
            caracteristics_card_link(
                "Correo Electrónico",
                "acma@alcobendas.manyanet.org", 
                "mail",
                "mailto:acma@alcobendas.manyanet.org"
            ),

            # Tarjeta derecha: Ubicación en el colegio
            caracteristics_card(
                "Ubicación",
                "Sala de ordenadores secundaria Colegio P. M.",
                "map_pin",
            ),
            width="100%",
            justify="center",
            spacing="6",
        ),

        # Tarjeta inferior: Horario Presencial
        caracteristics_card_card(
            "Horario Presencial",
            "Martes y Jueves",
            "Miércoles y Viernes",
            "clock-4",
            "10:05 - 11:00",
            "12:25 - 13:20"
        ),
        width="100%",
        max_width="824px", 
        align_items="center",
        spacing="8",
    )