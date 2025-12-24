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
    
    # Lista para llevar registro de los nombres de archivos subidos
    archivos_seleccionados: list[str] = []
    
    def handle_submit(self, form_data: dict):
        # El diccionario form_data trae los 'name' de los inputs como keys
        print(f"Datos recibidos: {form_data}")
        # Acá podrías incluir self.archivos_seleccionados en el envío final
        return rx.window_alert(f"¡Solicitud enviada con éxito! Archivos: {', '.join(self.archivos_seleccionados)}")

    async def handle_upload(self, files: list[rx.UploadFile]):
        """
        Manejo de archivos. 
        Leemos los archivos seleccionados y los guardamos en el servidor.
        """
        for file in files:
            upload_data = await file.read()
            # Definimos la ruta de salida (asegurate de que la carpeta exista)
            outfile = f".web/public/{file.filename}"
            
            with open(outfile, "wb") as f:
                f.write(upload_data)
            
            # Actualizamos la lista para dar feedback al usuario
            self.archivos_seleccionados.append(file.filename)
    
    def remove_file(self, file_name: str):
        """Elimina un archivo de la lista de seleccionados."""
        self.archivos_seleccionados = [
            f for f in self.archivos_seleccionados if f != file_name
        ]