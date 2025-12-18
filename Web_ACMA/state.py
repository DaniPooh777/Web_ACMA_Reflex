import reflex as rx


class State(rx.State):
    """Estado global de la aplicación."""
    seccion_activa: str = ""
    
    def toggle_posters(self):
        self.seccion_activa = "" if self.seccion_activa == "posters" else "posters"
    
    def toggle_presentaciones(self):
        self.seccion_activa = "" if self.seccion_activa == "presentaciones" else "presentaciones"
    
    def toggle_cuestionarios(self):
        self.seccion_activa = "" if self.seccion_activa == "cuestionarios" else "cuestionarios"
    
    def toggle_documentos(self):
        self.seccion_activa = "" if self.seccion_activa == "documentos" else "documentos"


class FormState(rx.State):
    """Lógica específica para el formulario de encargos."""
    
    def handle_submit(self, form_data: dict):
        # El diccionario form_data trae los 'name' de los inputs como keys
        print(f"Datos recibidos: {form_data}")
        # Acá iría la lógica de persistencia o envío
        return rx.window_alert("¡Solicitud enviada con éxito!")

    def handle_upload(self, files: list[rx.UploadFile]):
        """Manejo de archivos. No se mandan solos, ¡ponete las pilas!"""
        for file in files:
            # Aquí procesarías el guardado en el servidor
            pass