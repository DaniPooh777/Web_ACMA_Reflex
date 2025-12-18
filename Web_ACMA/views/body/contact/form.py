import reflex as rx
from Web_ACMA.state import FormState # Ajustá el path según tu estructura

def solicitud_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.heading("Solicita un nuevo encargo", size="7"),
            
            rx.text("Nombre", size="2", weight="bold"),
            rx.input(placeholder="Tu nombre completo", name="nombre", width="100%"),
            
            rx.text("Email", size="2", weight="bold"),
            rx.input(placeholder="tu@email.com", name="email", type="email", width="100%"),
            
            rx.text("Nivel Educativo", size="2", weight="bold"),
            rx.select(
                ["Guardería", "Infantil", "Primaria", "Secundaria", "Bachillerato"],
                placeholder="Selecciona el nivel educativo",
                name="nivel_educativo",
                width="100%"
            ),
            
            rx.text("Departamento", size="2", weight="bold"),
            rx.input(placeholder="Di de qué departamento eres...", name="departamento", width="100%"),
            
            rx.text("Descripción del Encargo", size="2", weight="bold"),
            # Contenedor relativo para posicionar el adjuntar
            rx.box(
                rx.text_area(
                    placeholder="Describe detalladamente el encargo que necesitas...",
                    name="descripcion",
                    width="100%",
                    min_height="200px",
                ),
                # El componente de Upload ahora es solo un botón posicionado
                rx.upload(
                    rx.button(
                        rx.icon(tag="upload", size=16),
                        "Adjuntar",
                        variant="ghost",
                        size="1",
                        color_scheme="gray",
                        cursor="pointer",
                    ),
                    id="upload_files",
                    # Lo movemos abajo a la derecha del cuadro de texto
                    border="none", 
                    padding="0",   
                    position="absolute",
                    bottom="10px",
                    right="10px",
                ),
                position="relative",
                width="100%",
            ),
            
            rx.button(
                "Enviar Solicitud", 
                type="submit", 
                width="100%", 
                size="3",
                color_scheme="blue"
            ),
            
            spacing="4",
            align_items="stretch",
            width="100%",
        ),
        on_submit=FormState.handle_submit,
        reset_on_submit=True,
    )