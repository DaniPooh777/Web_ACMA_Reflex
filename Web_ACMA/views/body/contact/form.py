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

# =========
# COMPONENT
# =========

"""Es la plantilla de la casilla para aquello que se necesita escribir en el formulario"""
def input_field(label: str, placeholder: str, name: str, valor: rx.Var, error_cond: rx.Var, on_blur_fn, on_change_fn, type: str = "text") -> rx.Component:
    return rx.vstack(
        # Título de la casilla
        rx.text(label, **LABEL_STYLE),

        # La casilla
        rx.input(
            name=name,
            placeholder=placeholder, # Es el textito clarito dentro de la casilla que desaparece cuando escribes en la casilla 
            value=valor,
            on_change=on_change_fn, # Detecta cambios en tiempo real
            on_blur=on_blur_fn, # Detecta cuando el usuario sale del componente
            type=type,

            # Da estilo al borde de la casilla cuando está normal y cuando falta el elemento en ella
            style={
                **INPUT_STYLE,
                "border": rx.cond(
                    error_cond,
                    "1px solid #ef4444 !important", # Color rojo advertencia
                    f"1px solid {COLOR_BORDER_INPUT}" # Color normal casilla
                ),
            },

            # Ignora la tecla ENTER para evitar que se envíe el formulario
            on_key_down=lambda e: rx.cond(
                e == "Enter",
                rx.event.prevent_default,
                rx.console_log("Tecla ignorada")
            ),
        ),

        # Condicional que activa el texto rojo debajo de la casilla cuando no la has completado y has salido de ella.
        rx.cond(
            error_cond,
            rx.text("Este campo es obligatorio", color="#ef4444", font_size="0.75rem"),
        ),
        width="100%",
        align_items="start",
        spacing="1",
    )

# =========
# COMPONENT
# =========

"""Es la plantilla del popup que sale cuando tratas de enviar el formulario sin haberlo completado por completo"""
def alerta_formulario_incompleto() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("⛔️ ¡Para el carro, fiera! ⛔️"),
            rx.alert_dialog.description(
                "¡No quieras pasarte de listo! Completa todo el formulario.",
            ),
            rx.flex(
                rx.alert_dialog.action(
                    rx.button("Lo reviso", on_click=FormState.cerrar_dialogo),
                ),
                justify="end",
                margin_top="1rem",
            ),
        ),
        open=FormState.dialogo_abierto, # Vinculado al estado
    )

# =========
# COMPONENT
# =========

"""Es la plantilla del popup que sale cuando el formulario se ha enviado exitosamente"""
def alerta_exito() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("🚀 ¡Encargo en camino! 🚀"),
            rx.alert_dialog.description(
                "Tu solicitud ha sido enviada correctamente. Revisa tu gmail (y el spam por si las dudas) porque te mandaremos una copia.",
            ),
            rx.flex(
                rx.alert_dialog.action(
                    rx.button(
                        "Perfecto", 
                        on_click=FormState.cerrar_dialogo_exito,
                        color_scheme="blue",
                    ),
                ),
                justify="end",
                margin_top="1rem",
            ),
        ),
        open=FormState.dialogo_exito_abierto,
    )

# ===============
# VISTA PRINCIPAL
# ===============

"""Esta función se encarga de dar estructura a la sección del formulario"""
def solicitud_form() -> rx.Component:
    return rx.fragment(
        # Los dos popups
        alerta_formulario_incompleto(),
        alerta_exito(),

        # El formulario en sí
        rx.form(
            rx.vstack(
                # Título de la sección
                rx.heading("Solicita un nuevo encargo", size="6", margin_bottom="0.5rem", color="#ffffff"),
                
                # Casilla del nombre
                input_field(
                    "Nombre", "Tu nombre completo", "nombre",
                    valor=FormState.nombre_valor,
                    error_cond=FormState.error_nombre,
                    on_blur_fn=FormState.marcar_nombre_tocado,
                    on_change_fn=FormState.set_nombre_valor
                ),
                
                # Casilla del email
                rx.vstack(
                    rx.text("Email", **LABEL_STYLE),
                    rx.input(
                        name="email",
                        placeholder="Tu email del centro",
                        type="email",
                        value=FormState.email_valor,
                        on_change=FormState.set_email_valor,
                        on_blur=FormState.marcar_email_tocado, 
                        on_key_down=lambda e: rx.cond(e == "Enter", rx.event.prevent_default, rx.console_log("")),
                        style={
                            **INPUT_STYLE,
                            "border": rx.cond(
                                FormState.mostrar_error_email,
                                "1px solid #ef4444 !important",
                                f"1px solid {COLOR_BORDER_INPUT}"
                            ),
                        },
                    ),
                    rx.cond(
                        FormState.mostrar_error_email,
                        rx.text("Usa tu correo del centro", color="#ef4444", font_size="0.75rem"),
                    ),
                    width="100%",
                    align_items="start",
                    spacing="1",
                ),
                
                # Casilla del nivel eduacativo
                rx.vstack(
                    rx.text("Nivel Educativo", **LABEL_STYLE),
                    rx.box(
                        rx.select(
                            ["Guardería", "Infantil", "Primaria", "Secundaria", "Bachillerato"],
                            placeholder="Selecciona el nivel...",
                            name="nivel_educativo",
                            value=FormState.nivel_seleccionado, 
                            on_change=lambda v: FormState.set_nivel_seleccionado(v),
                            on_open_change=FormState.manejar_cierre_menu,
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
                        border=rx.cond(
                            FormState.error_nivel,
                            "1px solid #ef4444 !important",
                            f"2px solid {COLOR_BORDER_INPUT}"
                        ),
                        border_radius="8px",
                        width="100%",
                        height="2.8rem",
                        padding_x="1rem",
                        display="flex",
                        align_items="center",
                        overflow="hidden",
                    ),
                    rx.cond(
                        FormState.error_nivel,
                        rx.text("Este campo es obligatorio", color="#ef4444", font_size="0.75rem"),
                    ),
                    width="100%", 
                    align_items="stretch",
                    spacing="1",
                ),
                
                # Casilla del asunto del encargo
                input_field(
                    "Asunto", "Dale un nombre al encargo", "asunto",
                    valor=FormState.asunto_valor,
                    error_cond=FormState.error_asunto,
                    on_blur_fn=FormState.marcar_asunto_tocado,
                    on_change_fn=FormState.set_asunto_valor
                ),

                # Casilla de la fecha de entrega
                rx.vstack(
                    rx.text("Fecha de Entrega Deseada", **LABEL_STYLE),
                    rx.input(
                        type="date", # Esto activa el calendario nativo del navegador que es muy intuitivo
                        name="fecha_entrega",
                        min=FormState.fecha_minima,
                        color="#ffffff",
                        on_change=FormState.set_fecha_valor,
                        on_blur=FormState.marcar_fecha_tocado,
                        style={
                            **INPUT_STYLE,
                            "width": "100%",
                            "border": rx.cond(
                                FormState.error_fecha,
                                "1px solid #ef4444 !important",
                                f"1px solid {COLOR_BORDER_INPUT}"
                            ),
                        },
                    ),
                    rx.cond(
                        FormState.error_fecha,
                        rx.text("Este campo es obligatorio", color="#ef4444", font_size="0.75rem"),
                    ),
                    width="100%",
                    align_items="start",
                    spacing="1",
                ),
                
                # Casilla de la descripción del encargo
                rx.vstack(
                    rx.text("Descripción del Encargo", **LABEL_STYLE),
                    # RECUADRO DE TEXTO (Solo el área de escritura y el botón)
                    rx.box(
                        rx.text_area(
                            name="descripcion",
                            placeholder="Describe detalladamente el encargo...",
                            color="#ffffff",
                            width="100%",
                            min_height="160px",
                            background_color="transparent", 
                            value=FormState.descripcion_valor,
                            on_change=FormState.set_descripcion_valor,
                            on_blur=FormState.marcar_descripcion_tocado, 
                            style={
                                "border": "none",
                                "padding_bottom": "3rem",
                                "padding_right": "1rem"
                            },
                        ),

                        # Botón de adjuntar archivos
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
                        border=rx.cond(
                            FormState.error_descripcion,
                            "1px solid #ef4444 !important",
                            f"1px solid {COLOR_BORDER_INPUT}"
                        ),
                        background_color=COLOR_INPUT_BG,
                        border_radius="8px",
                        width="100%",
                    ),

                    rx.cond(
                        FormState.error_descripcion,
                        rx.text("La descripción es obligatoria", color="#ef4444", font_size="0.75rem"),
                    ),
                    
                    # Lista de archivos adjuntados
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
                                    on_click=FormState.remove_file(file) 
                                ),
                                width="100%",
                                padding_y="0.5rem",
                                border_bottom=f"1px solid {COLOR_BORDER_CONTAINER}",
                            )
                        ),
                        align_items="start",
                        width="100%",
                        padding_top="0.5rem", 
                    ),
                    width="100%", 
                    align_items="start", 
                    spacing="1",
                ),
                
                # Botón de enviar formulario
                rx.button(
                    rx.cond(
                        FormState.cargando,
                        rx.spinner(size="2"), # Para que el usuario sepa que se está enviando el formulario
                        "Enviar Solicitud"
                    ),
                    type="submit",
                    disabled=FormState.cargando, # No permitir clicks extra
                    **SUBMIT_BUTTON_STYLE
                ),
                **FORM_CONTAINER_STYLE,
            ),
            id="formulario-encargo", 
            on_submit=FormState.handle_submit,
            reset_on_submit=True, # Limpia el texto de los inputs tras enviar
            width="100%",
            scroll_margin_top="100px",
            display="flex",
            justify_content="center",
            align_self="center", 
        )
    ) 