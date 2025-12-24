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
    COLOR_BORDER_INPUT,
    COLOR_BORDER_CONTAINER
)

def input_field(label: str, placeholder: str, name: str, type: str = "text") -> rx.Component:
    return rx.vstack(
        rx.text(label, **LABEL_STYLE),
        rx.input(
            name=name,
            placeholder=placeholder,
            type=type,
            style=INPUT_STYLE, #

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
                rx.box(
                    rx.select(
                        ["Guardería", "Infantil", "Primaria", "Secundaria", "Bachillerato"],
                        placeholder="Selecciona el nivel...",
                        name="nivel_educativo",
                        width="100%",
                        height="100%",
                        variant="ghost",
                        style={
                            "color": "white",
                            "width": "100%",
                            "& .rt-SelectTrigger": {
                                "background_color": "transparent !important",
                                "border": "none !important",
                                "box_shadow": "none !important",
                                "width": "100% !important",
                                "height": "2.8rem !important",
                                "padding": "0 1rem",
                                "cursor": "pointer",
                            },
                            # Mantenemos el bloqueo de color para que no se ponga azul/gris
                            "& .rt-SelectTrigger:hover": {
                                "background_color": "transparent !important",
                            },
                            "& .rt-SelectTrigger:focus": {
                                "background_color": "transparent !important",
                                "box_shadow": "none !important",
                            },
                        },
                    ),
                    background_color=COLOR_INPUT_BG,
                    border=f"2px solid {COLOR_BORDER_INPUT}",
                    border_radius="8px",
                    width="100%",
                    height="2.8rem",
                    padding_x="1rem",
                    display="flex",
                    align_items="center",
                    overflow="hidden",
                ),
                width="100%", 
                align_items="stretch",
                spacing="1",
            ),
            rx.vstack(
                rx.text("Descripción del Encargo", **LABEL_STYLE),
                # RECUADRO DE TEXTO (Solo el área de escritura y el botón)
                rx.box(
                    rx.text_area(
                        name="descripcion",
                        placeholder="Describe detalladamente el encargo...",
                        width="100%",
                        min_height="160px",
                        background_color="transparent", 
                        style={"border": "none"},
                    ),
                    rx.upload(
                        rx.hstack(
                            rx.icon(tag="upload", size=16),
                            rx.text("Adjuntar", font_size="0.8rem"),
                            **ATTACH_STYLE 
                        ),
                        id="upload_files",
                        on_drop=FormState.handle_upload(rx.upload_files(upload_id="upload_files")), 
                        **UPLOAD_CLEAN_STYLE
                    ),
                    position="relative",
                    border=f"1px solid {COLOR_BORDER_INPUT}", 
                    background_color=COLOR_INPUT_BG,
                    border_radius="8px",
                    width="100%",
                ),
                
                # LISTA DE ARCHIVOS (Fuera del recuadro, tal cual la imagen)
                rx.vstack(
                    rx.foreach(
                        FormState.archivos_seleccionados,
                        lambda file: rx.hstack(
                            rx.text(file, font_size="0.85rem", color="white"),
                            rx.spacer(),
                            rx.icon(
                                tag="x", 
                                size=14, 
                                color="gray", 
                                cursor="pointer",
                                on_click=FormState.remove_file(file) # <--- Necesitamos esta lógica
                            ),
                            width="100%",
                            padding_y="0.5rem",
                            border_bottom=f"1px solid {COLOR_BORDER_CONTAINER}",
                        )
                    ),
                    align_items="start",
                    width="100%",
                    padding_top="0.5rem", # Espacio entre el recuadro y la lista
                ),
                width="100%", 
                align_items="start", 
                spacing="1",
            ),
            
            rx.button("Enviar Solicitud", type="submit", **SUBMIT_BUTTON_STYLE),
            **FORM_CONTAINER_STYLE,
        ),
        id="formulario-encargo", # <--- AGREGÁ ESTO ACÁ, LOCO
        on_submit=FormState.handle_submit,
        width="100%",
        scroll_margin_top="100px",
        display="flex",
        justify_content="center",
        align_self="center", # Para que no se te escape al costado
    )