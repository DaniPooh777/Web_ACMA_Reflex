import reflex as rx
from Web_ACMA.state import FormState
from Web_ACMA.styles.views_style.body_style.contact_style.form_style import FORM_CONTAINER_STYLE

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

            # Aplicamos el estilo con el scroll_margin_top
            **FORM_CONTAINER_STYLE,
            id="formulario-encargo"
        ),
        on_submit=FormState.handle_submit,
    )