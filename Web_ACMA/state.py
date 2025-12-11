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
