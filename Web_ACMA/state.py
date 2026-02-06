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

    nivel_seleccionado: str = ""

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Esta función se dispara cuando el usuario suelta archivos"""
        for file in files:
            upload_data = await file.read()

            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            directorio_externo = os.path.join(base_dir, "archivos_externos_acma")

            # Creamos carpeta temporal si no existe
            if not os.path.exists(directorio_externo):
                os.makedirs(directorio_externo)
            
            nombre_limpio = file.filename.replace(" ", "_")
            ruta_final = os.path.join(directorio_externo, nombre_limpio)

            with open(ruta_final, "wb") as f:
                f.write(upload_data)
            
            # Guardamos para la UI y para el mail
            self.archivos_seleccionados.append(file.filename)
            self._rutas_temporales.append(ruta_final)

    def set_nivel_seleccionado(self, value: str):
        self.nivel_seleccionado = value

    def remove_file(self, file_name: str):
        """Para que el usuario pueda borrar un archivo de la lista"""
        if file_name in self.archivos_seleccionados:
            idx = self.archivos_seleccionados.index(file_name)
            self.archivos_seleccionados.pop(idx)
            # Borramos la ruta técnica también
            self._rutas_temporales.pop(idx)

    async def handle_submit(self, data: dict):
        """Caza los datos del form, limpia la UI al toque y manda el mail de fondo"""
        # CAPTURA DE DATOS
        nombre = data.get("nombre")
        email_cliente = data.get("email")
        nivel = data.get("nivel_educativo")
        asunto = data.get("asunto")
        fecha = data.get("fecha_entrega")
        descripcion = data.get("descripcion")        

        # El cuerpo que me pediste (respetando tu estructura)
        cuerpo_mail = f"""
        <html>
            <body style="margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif;">
                <div style="width: 100%; background-color: #f9f9f9; padding: 20px;">
                    <div style="max-width: 700px; margin: 0 auto; background-color: #ffffff; padding: 30px; border: 1px solid #eeeeee; border-radius: 8px;">
                        
                        <div style="font-family: Arial, Helvetica, sans-serif; color: #333333; line-height: 1.6;">
                            <div style="background-color: #f4f4f4; padding: 15px; border-left: 4px solid #333; margin-bottom: 25px;">
                                <p style="margin: 0 0 10px 0; font-size: 16px; text-transform: uppercase; letter-spacing: 1px;">
                                    <b>-------------------------------</b><br>
                                    <b>|   Datos Generales    |</b><br>
                                    <b>-------------------------------</b>
                                </p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Nombre:</b> {nombre}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Email:</b> {email_cliente}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Nivel Educativo:</b> {nivel}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Fecha de Entrega:</b> {fecha}</p>
                            </div>

                            <div style="margin-bottom: 20px;">
                                <p style="font-size: 16px;">Este es el encargo que nos han mandado, equipo de ACMA:</p>
                                <pre style="font-size: 16px; font-family: Arial, sans-serif; white-space: pre-wrap; word-wrap: break-word; margin: 0;">{descripcion}</pre>
                            </div>

                            <div style="background-color: #f4f4f4; padding: 15px; border-left: 4px solid #333; margin-bottom: 25px;">
                                <p style="margin: 0 0 10px 0; font-size: 16px; text-transform: uppercase; letter-spacing: 1px;">
                                    <b>----------------------------</b><br>
                                    <b>|   Instrucciones    |</b><br>
                                    <b>----------------------------</b>
                                </p>
                                <div style="margin-bottom: 20px;">
                                    <p style="font-size: 16px;"><b>1º</b> No se responde el email. Este email solo sirve de intermediario entre el formulario y ACMA. Para responder al profesor es necesario pinchar en su correo presente en la sección de Datos Generales.</p>
                                    <p style="font-size: 16px;"><b>2º</b> Es obligatorio usar un léxico formal pero a la vez cercano. Debemos dar una buena imagen hacia el profesorado pero con esa calidez que den ganas de estar con nosotros. Esto es con el objetivo de crear confianza y de nos confíen sus trabajos.</p>
                                    <p style="font-size: 16px;"><b>3º</b> Es preciso una estructura clara y uniforme sobre los correos de ACMA. Repasad la estructura del email vista en el cole (buscad en Google). Debemos demostrar la profesionalidad de la empresa.</p>
                                    <p style="font-size: 16px;"><b>Que la fuerza os acompañe.</b></p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </body>
        </html>
        """

        # Configuramos el mensaje
        msg = EmailMessage()
        msg.set_content(cuerpo_mail)
        msg['Subject'] = f"Solicitud encargo: {asunto}"
        msg['From'] = f"{nombre} <{os.getenv('EMAIL_USER')}>" # Ponemos el nombre del cliente pero el mail sigue siendo el de tu .env // Así Google no te rebota el mail y vos ves quién es.
        msg['To'] = "acma@alcobendas.manyanet.org"
        msg['Reply-To'] = email_cliente # Para que ACMA le responda directo al profe
        msg.add_alternative(cuerpo_mail, subtype='html')

        # Adjuntamos los archivos uno por uno
        for ruta in self._rutas_temporales:
            if os.path.exists(ruta):
                with open(ruta, 'rb') as f:
                    msg.add_attachment(
                        f.read(),
                        maintype='application',
                        subtype='octet-stream',
                        filename=os.path.basename(ruta)
                    )

        # El disparo final
        try:            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
                server.send_message(msg)
                
                # LIMPIAMOS LA CARPETA
                for ruta in self._rutas_temporales:
                    if os.path.exists(ruta):
                        os.remove(ruta)

                # LIMPIAMOS LOS ARCHIVOS          
                self.archivos_seleccionados = []
                self._rutas_temporales = []
                self.nivel_seleccionado = ""
        
        except Exception as e:
            return rx.window_alert(f"Error al enviar: {str(e)}") # Si explota, por lo menos le avisamos


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