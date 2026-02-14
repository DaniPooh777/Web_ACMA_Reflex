import reflex as rx

# ==========================================
# CONFIGURACIÓN GLOBAL DE LA APLICACIÓN
# ==========================================
# Aquí definimos cómo se comporta el framework con nuestro proyecto.

config = rx.Config(
    app_name="Web_ACMA",
    plugins=[
        rx.plugins.SitemapPlugin(), # Para que Google no nos ignore
        rx.plugins.TailwindV4Plugin(), # Estilado moderno y rápido
    ]
)