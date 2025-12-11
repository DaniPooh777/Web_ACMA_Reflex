import reflex as rx


def example_resources_type_card(url: str) -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.text("Visualización", size = "5"),
            rx.image(
                src = url,
                alt = "Póster: Tú Decides",
                width = "100px",
                height = "auto"
            )
        )
    )