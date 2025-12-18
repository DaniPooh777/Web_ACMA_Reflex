import reflex as rx
from Web_ACMA.state import FormState # Ajustá el path según tu estructura

def solicitud_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            # Título
            rx.heading("Solicita un nuevo encargo", size="7"),
            
            # Campos secuenciales
            rx.text("Nombre"),
            rx.input(name="nombre"),
            
            rx.text("Email"),
            rx.input(name="email", type="email"),
            
            rx.text("Nivel Educativo"),
            rx.select(
                ["Primaria", "Secundaria", "Grado", "Posgrado"],
                name="nivel_educativo",
            ),
            
            rx.text("Departamento"),
            rx.input(name="departamento"),
            
            rx.text("Descripción del Encargo"),
            rx.text_area(name="descripcion"),
            
            # El upload como un bloque separado, sin posicionamiento
            rx.upload(
                rx.button("Adjuntar Archivo"),
                id="upload_files",
            ),
            
            # Envío
            rx.button("Enviar Solicitud", type="submit"),
            
            align_items="start",
            width="100%",
        ),
        on_submit=FormState.handle_submit,
    )