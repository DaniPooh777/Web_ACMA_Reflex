import reflex as rx
from Web_ACMA.components.information_card import information_card


def information() -> rx.Component:
    return rx.vstack(
        information_card(
            "Quiénes Somos",
            "",
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
        ),
        rx.hstack(
            information_card(
                "Misión",
                "",
                "Lorem Ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation."
            ),
            information_card(
                "Visión",
                "",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
            )
        )
    )