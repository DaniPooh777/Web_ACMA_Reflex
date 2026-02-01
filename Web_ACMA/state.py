import reflex as rx
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class FormState(rx.State):
    # 1. Variables para la UI (lo que ve el usuario)
    archivos_seleccionados: list[str] = []
    
    # 2. Variables internas (rutas de los archivos en el servidor)
    _rutas_temporales: list[str] = []

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Esta función se dispara cuando el usuario suelta archivos"""
        for file in files:
            upload_data = await file.read()
            # Creamos carpeta temporal si no existe
            if not os.path.exists("uploads"):
                os.makedirs("uploads")
            
            ruta_final = os.path.join("uploads", file.filename)
            with open(ruta_final, "wb") as f:
                f.write(upload_data)
            
            # Actualizamos la lista que ve el usuario
            self.archivos_seleccionados.append(file.filename)
            # Guardamos la ruta para el mail
            self._rutas_temporales.append(ruta_final)

    def remove_file(self, file_name: str):
        """Para que el usuario pueda borrar un archivo de la lista"""
        if file_name in self.archivos_seleccionados:
            idx = self.archivos_seleccionados.index(file_name)
            self.archivos_seleccionados.pop(idx)
            # Borramos la ruta técnica también
            self._rutas_temporales.pop(idx)

    async def handle_submit(self, data: dict):
        """Caza los datos del form y manda el mail"""
        nombre = data.get("nombre")
        email_cliente = data.get("email")
        nivel = data.get("nivel_educativo")
        asunto = data.get("asunto")
        fecha = data.get("fecha_entrega")
        descripcion = data.get("descripcion")

        # El cuerpo que me pediste (respetando tu estructura)
        cuerpo_mail = (
            f"------------------------\n"
            f"|Datos Generales|\n"
            f"------------------------\n"
            f"Nombre: {nombre}\n"
            f"Email: {email_cliente}\n"
            f"Nivel Educativo: {nivel}\n\n"
            f"-------------\n"
            f"|Encargo|\n"
            f"-------------\n"
            f"Buenas equipo de ACMA,\n\n"
            f"{descripcion}.\n\n"
            f"Quiero que esté para el {fecha}.\n\n"
            f"Muchas gracias por vuestro tiempo.\n\n"
            f"{nombre}"
        )

        # Configuramos el mensaje
        msg = EmailMessage()
        msg.set_content(cuerpo_mail)
        msg['Subject'] = f"Solicitud encargo: {asunto}"
        # Ponemos el nombre del cliente pero el mail sigue siendo el de tu .env
        # Así Google no te rebota el mail y vos ves quién es.
        msg['From'] = f"{nombre} <{os.getenv('EMAIL_USER')}>" 
        msg['To'] = "acma@alcobendas.manyanet.org"
        # Esto hace que cuando ACMA le dé a "Responder", le escriba al profe
        msg['Reply-To'] = email_cliente # Para que ACMA le responda directo al profe

        # Adjuntamos los archivos uno por uno
        for ruta in self._rutas_temporales:
            if os.path.exists(ruta):
                with open(ruta, 'rb') as f:
                    archivo_binario = f.read()
                    nombre_archivo = os.path.basename(ruta)
                    msg.add_attachment(
                        archivo_binario,
                        maintype='application',
                        subtype='octet-stream',
                        filename=nombre_archivo
                    )

        # El disparo final
        try:
            user = os.getenv("EMAIL_USER")
            password = os.getenv("EMAIL_PASS")
            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(user, password)
                server.send_message(msg)
            
            # Limpiamos todo
            self.archivos_seleccionados = []
            self._rutas_temporales = []
            return rx.window_alert("¡Enviado con éxito!")
        
        except Exception as e:
            return rx.window_alert(f"Error técnico: {str(e)}")


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