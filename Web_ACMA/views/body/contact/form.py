import reflex as rx
from Web_ACMA.state import FormState
from Web_ACMA.styles.views_style.body_style.contact_style.form_style import (
    FORM_CONTAINER_STYLE, 
    INPUT_STYLE, 
    LABEL_STYLE, 
    COLOR_BORDER_INPUT,
    ATTACH_STYLE,
    SUBMIT_BUTTON_STYLE,
    UPLOAD_CLEAN_STYLE,
    COLOR_INPUT_BG,
    COLOR_BORDER_INPUT
)

def input_field(label: str, placeholder: str, name: str, type: str = "text") -> rx.Component:
    return rx.vstack(
        rx.text(label, **LABEL_STYLE),
        rx.input(
            name=name,
            placeholder=placeholder,
            type=type,
            style=INPUT_STYLE, # Este ya trae el border: 1px solid COLOR_BORDER
        ),
        width="100%",
        align_items="start",
        spacing="1",
    )

def solicitud_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Solicita un nuevo encargo", size="6", margin_bottom="0.5rem"),
            
            input_field("Nombre", "Tu nombre completo", "nombre"),
            input_field("Email", "tu@email.com", "email", type="email"),
            
            rx.vstack(
                rx.text("Nivel Educativo", **LABEL_STYLE),
                rx.select(
                    ["Guardería", "Infantil", "Primaria", "Secundaria", "Bachillerato"],
                    placeholder="Selecciona el nivel...",
                    name="nivel_educativo",
                    width="100%",
                    height="2.8rem",
                    style={
                        "border": f"1px solid {COLOR_BORDER_INPUT}", # Borde blanco unificado
                        "border_radius": "8px",
                        "background_color": COLOR_INPUT_BG,
                        "color": "white",
                    },
                ),
                width="100%", align_items="start", spacing="1",
            ),

            rx.vstack(
                rx.text("Descripción del Encargo", **LABEL_STYLE),
                rx.box(
                    rx.text_area(
                        name="descripcion",
                        placeholder="Describe detalladamente el encargo...",
                        width="100%",
                        min_height="160px",
                        background_color="transparent", 
                        style={"border": "none"}, # Fundamental para que no se pisen los bordes
                    ),                   
                    rx.upload(
                        rx.hstack(
                            rx.icon(tag="upload", size=16),
                            rx.text("Adjuntar", font_size="0.8rem"),
                            **ATTACH_STYLE
                        ),
                        id="upload_files",
                        **UPLOAD_CLEAN_STYLE
                    ),
                    # ACÁ ESTÁ EL PROBLEMA: Asegurate de usar COLOR_BORDER_INPUT
                    border=COLOR_BORDER_INPUT, 
                    background_color=COLOR_INPUT_BG,
                    border_radius="8px",
                    width="100%",
                ),
                width="100%", align_items="start", spacing="1",
            ),
            
            rx.button("Enviar Solicitud", type="submit", **SUBMIT_BUTTON_STYLE),
            **FORM_CONTAINER_STYLE,
        ),
        on_submit=FormState.handle_submit,
        width="100%",
        display="flex",
        justify_content="center",
        align_self="center", # Para que no se te escape al costado
    )