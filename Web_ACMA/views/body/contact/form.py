import reflex as rx
from Web_ACMA.state import FormState # Ajustá el path según tu estructura

def solicitud_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            # Le clavamos un ID al heading para que sirva de ancla
            rx.heading("Solicita un nuevo encargo", size="7", id="formulario-encargo"),
            
            rx.text("Nombre"),
            # El auto_focus hace que el cursor aparezca solo al llegar
            rx.input(name="nombre", auto_focus=True),
            
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