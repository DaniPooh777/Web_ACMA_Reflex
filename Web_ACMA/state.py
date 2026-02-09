import reflex as rx
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class FormState(rx.State):
    # 1. Variables para la UI y archivos
    archivos_seleccionados: list[str] = []
    _rutas_temporales: list[str] = []
    nivel_seleccionado: str = ""

    # 2. Variables para validación reactiva
    email_valor: str = ""
    email_tocado: bool = False
    
    nombre_valor: str = ""
    nombre_tocado: bool = False
    
    asunto_valor: str = ""
    asunto_tocado: bool = False
    
    fecha_valor: str = ""
    fecha_tocado: bool = False

    descripcion_valor: str = ""
    descripcion_tocado: bool = False

    # --- SETTERS Y MARCADORES ---
    def set_email_valor(self, valor: str):
        self.email_valor = valor

    def marcar_email_tocado(self, _=None):
        self.email_tocado = True

    def set_nombre_valor(self, valor: str):
        self.nombre_valor = valor

    def marcar_nombre_tocado(self, _=None):
        self.nombre_tocado = True

    def set_asunto_valor(self, valor: str):
        self.asunto_valor = valor

    def marcar_asunto_tocado(self, _=None):
        self.asunto_tocado = True

    def set_fecha_valor(self, valor: str):
        self.fecha_valor = valor

    def marcar_fecha_tocado(self, _=None):
        self.fecha_tocado = True

    def set_descripcion_valor(self, valor: str):
        self.descripcion_valor = valor

    def marcar_descripcion_tocado(self, _=None):
        self.descripcion_tocado = True

    def set_nivel_seleccionado(self, value: str):
        self.nivel_seleccionado = value

    # --- COMPUTED VARS ---
    @rx.var
    def mostrar_error_email(self) -> bool:
        if not self.email_tocado:
            return False
        return not self.email_valor.lower().endswith("@alcobendas.manyanet.org")

    @rx.var
    def error_nombre(self) -> bool:
        return self.nombre_tocado and len(self.nombre_valor.strip()) == 0

    @rx.var
    def error_asunto(self) -> bool:
        return self.asunto_tocado and len(self.asunto_valor.strip()) == 0

    @rx.var
    def error_fecha(self) -> bool:
        return self.fecha_tocado and len(self.fecha_valor.strip()) == 0
    
    @rx.var
    def error_descripcion(self) -> bool:
        return self.descripcion_tocado and len(self.descripcion_valor.strip()) == 0

    # --- LÓGICA DE ARCHIVOS ---
    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            directorio_externo = rx.get_upload_dir()
            if not os.path.exists(directorio_externo):
                os.makedirs(directorio_externo)
            
            nombre_limpio = file.filename.replace(" ", "_")
            ruta_final = os.path.join(directorio_externo, nombre_limpio)

            with open(ruta_final, "wb") as f:
                f.write(upload_data)
            
            self.archivos_seleccionados.append(file.filename)
            self._rutas_temporales.append(ruta_final)

    def remove_file(self, file_name: str):
        if file_name in self.archivos_seleccionados:
            idx = self.archivos_seleccionados.index(file_name)
            ruta_a_borrar = self._rutas_temporales[idx]
            try:
                if os.path.exists(ruta_a_borrar):
                    os.remove(ruta_a_borrar)
            except Exception as e:
                print(f"Error al borrar archivo físico: {e}")
            self.archivos_seleccionados.pop(idx)
            self._rutas_temporales.pop(idx)

    def limpiar_validacion(self):
        # Reset de booleanos
        self.email_tocado = False
        self.nombre_tocado = False
        self.asunto_tocado = False
        self.fecha_tocado = False
        self.descripcion_tocado = False
        # Reset de valores (opcional, si querés que el texto también desaparezca)
        self.email_valor = ""
        self.nombre_valor = ""
        self.asunto_valor = ""
        self.fecha_valor = ""
        self.descripcion_valor = ""
        self.nivel_seleccionado = ""
    
    # --- ENVÍO DE FORMULARIO ---
    async def handle_submit(self, data: dict):
        email_cliente = data.get("email")
        nombre = data.get("nombre")
        nivel = data.get("nivel_educativo")
        asunto = data.get("asunto")
        fecha = data.get("fecha_entrega")
        descripcion = data.get("descripcion")       

        dominio_permitido = "@alcobendas.manyanet.org"
        if not email_cliente.lower().endswith(dominio_permitido):
            return rx.window_alert(f"Acceso denegado. Usá tu mail de {dominio_permitido}") 

        cuerpo_mail = f"""
        <html>
            <body style="margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif;">
                <div style="width: 100%; background-color: #f9f9f9; padding: 20px;">
                    <div style="max-width: 700px; margin: 0 auto; background-color: #ffffff; padding: 30px; border: 1px solid #eeeeee; border-radius: 8px;">
                        <div style="font-family: Arial, Helvetica, sans-serif; color: #333333; line-height: 1.6;">
                            <div style="background-color: #f4f4f4; padding: 15px; border-left: 4px solid #333; margin-bottom: 25px;">
                                <p style="margin: 5px 0; font-size: 16px;"><b>Nombre:</b> {nombre}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Email:</b> {email_cliente}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Nivel Educativo:</b> {nivel}</p>
                                <p style="margin: 5px 0; font-size: 16px;"><b>Fecha de Entrega:</b> {fecha}</p>
                            </div>
                            <div style="margin-bottom: 20px;">
                                <pre style="font-size: 16px; font-family: Arial, sans-serif; white-space: pre-wrap; word-wrap: break-word; margin: 0;">{descripcion}</pre>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
        msg_acma = EmailMessage()
        msg_acma.set_content(cuerpo_mail)
        msg_acma['Subject'] = f"Solicitud encargo: {asunto}"
        msg_acma['From'] = f"{nombre} <{os.getenv('EMAIL_USER')}>"
        msg_acma['To'] = "acma@alcobendas.manyanet.org"
        msg_acma['Reply-To'] = email_cliente
        msg_acma.add_alternative(cuerpo_mail, subtype='html')

        msg_cliente = EmailMessage()
        msg_cliente['Subject'] = f"Confirmación de pedido: {asunto}"
        msg_cliente['From'] = f"ACMA Manyanet <{os.getenv('EMAIL_USER')}>"
        msg_cliente['To'] = email_cliente
        msg_cliente.add_alternative("Tu pedido ha sido recibido.", subtype='html')

        for ruta in self._rutas_temporales:
            if os.path.exists(ruta):
                with open(ruta, 'rb') as f:
                    contenido_adjunto = f.read()
                    nombre_archivo = os.path.basename(ruta)
                    msg_acma.add_attachment(contenido_adjunto, maintype='application', subtype='octet-stream', filename=nombre_archivo)
                    msg_cliente.add_attachment(contenido_adjunto, maintype='application', subtype='octet-stream', filename=nombre_archivo)

        try:            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
                server.send_message(msg_acma)
                server.send_message(msg_cliente)
                for ruta in self._rutas_temporales:
                    if os.path.exists(ruta): os.remove(ruta)
                self.archivos_seleccionados = []
                self._rutas_temporales = []
                self.nivel_seleccionado = ""
        except Exception as e:
            return rx.window_alert(f"Error al enviar: {str(e)}")

class State(rx.State):
    seccion_activa: str = ""
    def toggle_posters(self): self.seccion_activa = "" if self.seccion_activa == "posters" else "posters"
    def toggle_presentaciones(self): self.seccion_activa = "" if self.seccion_activa == "presentaciones" else "presentaciones"
    def toggle_cuestionarios(self): self.seccion_activa = "" if self.seccion_activa == "cuestionarios" else "cuestionarios"
    def toggle_documentos(self): self.seccion_activa = "" if self.seccion_activa == "documentos" else "documentos"

class FaqState(rx.State):
    opened_id: str = ""
    def toggle_faq(self, id: str): self.opened_id = "" if self.opened_id == id else id
    def clean_state(self): self.opened_id = ""

class ProjectCardState(rx.State):
    opened_id: str = ""
    def toggle_card(self, card_id: str): self.opened_id = "" if self.opened_id == card_id else card_id
    def clean_state(self): self.opened_id = ""