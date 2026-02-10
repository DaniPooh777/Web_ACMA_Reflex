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

    nivel_seleccionado: str = ""
    nivel_tocado: bool = False

    dialogo_abierto: bool = False
    dialogo_exito_abierto: bool = False

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
        # Si seleccionó algo, ya no hay error, así que lo marcamos como tocado
        self.nivel_tocado = True

    def manejar_cierre_menu(self, abierto: bool):
        # 'abierto' es un booleano que manda Reflex. 
        # Si es False, es porque el menú se cerró (el usuario eligió o hizo clic afuera)
        if not abierto:
            self.nivel_tocado = True

    def tocar_nivel(self, _=None):
        self.nivel_tocado = True

    def abrir_dialogo(self):
        self.dialogo_abierto = True

    def cerrar_dialogo(self):
        self.dialogo_abierto = False

    def abrir_dialogo_exito(self):
        self.dialogo_exito_abierto = True

    def cerrar_dialogo_exito(self):
        self.dialogo_exito_abierto = False

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
    
    @rx.var
    def error_nivel(self) -> bool:
        # Si fue tocado y no seleccionó nada (está el placeholder)
        return self.nivel_tocado and (not self.nivel_seleccionado or self.nivel_seleccionado == "")
    
    @rx.var
    def formulario_invalido(self) -> bool:
        # Verificamos que todos los campos tengan contenido y que NO haya errores activos
        # Usamos strip() para que no nos engañen con puros espacios en blanco, ¡ponete las pilas!
        campos_vacios = (
            len(self.nombre_valor.strip()) == 0 or
            len(self.email_valor.strip()) == 0 or
            len(self.asunto_valor.strip()) == 0 or
            len(self.fecha_valor.strip()) == 0 or
            len(self.descripcion_valor.strip()) == 0 or
            self.nivel_seleccionado == ""
        )
        
        # También chequeamos que no existan errores de validación (como el dominio del email)
        hay_errores = (
            self.mostrar_error_email or 
            self.error_nombre or 
            self.error_asunto or 
            self.error_fecha or 
            self.error_descripcion or 
            self.error_nivel
        )

        return campos_vacios or hay_errores
    
    @rx.var
    def formulario_completo(self) -> bool:
        # Verificamos que todo esté lleno y sin errores
        return (
            len(self.nombre_valor.strip()) > 0 and
            len(self.email_valor.strip()) > 0 and
            not self.mostrar_error_email and
            len(self.asunto_valor.strip()) > 0 and
            len(self.fecha_valor.strip()) > 0 and
            len(self.descripcion_valor.strip()) > 0 and
            self.nivel_seleccionado != ""
        )

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
        # Limpiamos los valores de los campos
        self.nombre_valor = ""
        self.email_valor = ""
        self.asunto_valor = ""
        self.fecha_valor = ""
        self.descripcion_valor = ""
        self.nivel_seleccionado = ""
        
        # Reseteamos los estados de "tocado" para que no salten errores
        self.nombre_tocado = False
        self.email_tocado = False
        self.asunto_tocado = False
        self.fecha_tocado = False
        self.descripcion_tocado = False
        self.nivel_tocado = False
        
        # Limpiamos archivos si corresponde
        self.archivos_seleccionados = []
        self._rutas_temporales = []
    
    # --- ENVÍO DE FORMULARIO ---
    async def handle_submit(self, data: dict):        
        email_cliente = data.get("email")
        nombre = data.get("nombre")
        nivel = data.get("nivel_educativo")
        asunto = data.get("asunto")
        fecha = data.get("fecha_entrega")
        descripcion = data.get("descripcion")       
        
        if not self.formulario_completo:
            self.abrir_dialogo()
            return

        # --- 2. MAIL PARA EL ACMA ---
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
                                <p style="font-size: 16px;"><b>Este es el encargo que nos han mandado, equipo de ACMA:</b></p>
                                <pre style="font-size: 16px; font-family: Arial, sans-serif; white-space: pre-wrap; word-wrap: break-word; margin: 0;">{descripcion}</pre>
                            </div>

                            <div style="background-color: #f4f4f4; padding: 15px; border-left: 4px solid #333; margin-bottom: 25px;">
                                <p style="margin: 0 0 10px 0; font-size: 16px; text-transform: uppercase; letter-spacing: 1px;">
                                    <b>----------------------------</b><br>
                                    <b>|   Instrucciones    |</b><br>
                                    <b>----------------------------</b>
                                </p>
                                <div style="margin-bottom: 20px;">
                                    <p style="font-size: 16px;"><b>1º</b> Es obligatorio usar un léxico formal pero a la vez cercano. Debemos dar una buena imagen hacia el profesorado pero con esa calidez que den ganas de estar con nosotros. Esto es con el objetivo de crear confianza y de nos confíen sus trabajos.</p>
                                    <p style="font-size: 16px;"><b>2º</b> Es preciso una estructura clara y uniforme sobre los correos de ACMA. Repasad la estructura del email vista en el cole (buscad en Google). Debemos demostrar la profesionalidad de la empresa.</p>
                                    <p style="font-size: 16px;"><b>Que la fuerza os acompañe.</b></p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </body>
        </html>
        """

        # Configuramos el mensaje para ACMA
        msg_acma = EmailMessage()
        msg_acma.set_content(cuerpo_mail)
        msg_acma['Subject'] = f"Solicitud encargo: {asunto}"
        msg_acma['From'] = f"{nombre} <{os.getenv('EMAIL_USER')}>"
        msg_acma['To'] = "acma@alcobendas.manyanet.org"
        msg_acma['Reply-To'] = email_cliente
        msg_acma.add_alternative(cuerpo_mail, subtype='html')

        # --- 2. MAIL PARA EL CLIENTE (Copia amigable) ---
        cuerpo_cliente = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
                    <h2 style="color: #3b82f6;">¡Hola {nombre}!</h2>
                    <p>Hemos recibido correctamente tu solicitud para el proyecto: <strong>{asunto}</strong></p>
                    <p>Nuestro equipo de ACMA lo revisará y se pondrá en contacto contigo pronto.</p>
                    <hr>
                    <p><strong>Resumen de tu pedido:</strong></p>
                    <ul>
                        <li><strong>Nivel educativo:</strong> {nivel}</li>
                        <li><strong>Fecha de entrega:</strong> {fecha}</li>
                        <li><strong>Descripción:</strong> <blockquote style="background: #f4f4f4; padding: 10px; border-left: 5px solid #3b82f6; white-space: pre-wrap; word-wrap: break-word;">{descripcion}</blockquote></li>
                    </ul>
                    
                    <p style="font-size: 12px; color: #777;">Este es un mensaje automático, no es necesario que lo respondas. Que la fuerza te acompañe :)</p>
                </div>
            </body>
        </html>
        """

        # Configuramos el mensaje para el cliente
        msg_cliente = EmailMessage()
        msg_cliente['Subject'] = f"Confirmación de pedido: {asunto}"
        msg_cliente['From'] = f"ACMA Manyanet <{os.getenv('EMAIL_USER')}>"
        msg_cliente['To'] = email_cliente # El destinatario es el cliente
        msg_cliente['Reply-To'] = "acma@alcobendas.manyanet.org"
        msg_cliente.add_alternative(cuerpo_cliente, subtype='html')


        # Adjuntamos los archivos a AMBOS mensajes
        for ruta in self._rutas_temporales:
            if os.path.exists(ruta):
                with open(ruta, 'rb') as f:
                    contenido_adjunto = f.read()
                    nombre_archivo = os.path.basename(ruta)
                    
                    # Adjunto para ACMA
                    msg_acma.add_attachment(contenido_adjunto, maintype='application', subtype='octet-stream', filename=nombre_archivo)
                    # Adjunto para el Cliente
                    msg_cliente.add_attachment(contenido_adjunto, maintype='application', subtype='octet-stream', filename=nombre_archivo)

        try:            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))

                # Mandamos los dos
                server.send_message(msg_acma)
                server.send_message(msg_cliente)
                
                # Limpiamos la carpeta
                for ruta in self._rutas_temporales:
                    if os.path.exists(ruta):
                        os.remove(ruta)

                self.limpiar_validacion()
                self.abrir_dialogo_exito()

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