import reflex as rx
from rxconfig import config
from Web_ACMA.components.navbar import navbar
from Web_ACMA.views.header.header import header
from Web_ACMA.views.body.home.problems_solutions import problem_solutions
from Web_ACMA.views.body.home.resources import resources
from Web_ACMA.views.body.home.caracteristics import caracteristics
from Web_ACMA.components.footer import footer
from Web_ACMA.components.link_button import link_button
from Web_ACMA.views.body.who_are_we.information import information
from Web_ACMA.views.body.who_are_we.founder import founder
from Web_ACMA.views.body.projects.projects import projects
from Web_ACMA.state import State 
from Web_ACMA.views.body.contact.form import solicitud_form 
from Web_ACMA.views.body.contact.contact_cards import contact_cards


# Web_ACMA.py
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            header(
                "ACMA: Tu aliado confiable en la\nInnovación Educativa",
                "Transformamos tu visión pedagógica en recursos digitales de alta calidad"
            ),
            link_button(),
            width="100%",
            align_items="center",    # <--- ESTO ES LO QUE TE FALTA, LOCO
            spacing="4",
        ),
        problem_solutions(),
        resources(),
        caracteristics(),
        footer(),
        spacing="0",
        width="100%",
        align_items="center",        # <--- EL PADRE TAMBIÉN TIENE QUE CENTRAR
        background_color="rgb(10, 10, 15)"
    )


# Página Proyectos - ACTUALIZADA
def project() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
                "Proyectos Más Relevantes",
                "Descubre algunos de los proyectos más destacados que hemos realizado para el profesorado."
            ),
        projects(),  # Usando el nuevo componente
        footer(),
        spacing="0",
        width="100%",
        background_color="rgb(10, 10, 15)"
    )


# Página Quiénes Somos
def who_are_we() -> rx.Component:
    return rx.vstack(
        navbar(),
        header("Profundizando en ACMA", "Conocé a los que ensucian las manos."),
        information(), # El que arreglamos antes
        founder(),     # El que acabamos de pulir
        footer(),
        width="100%",
        align_items="center", # <--- ESTO ES NO NEGOCIABLE
        background_color="rgb(10, 10, 15)",
    )


# Página Contacto
def contact() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Contacta con ACMA",
            "Estamos aquí para ayudarte a crear los mejores recursos educativos."
        ),
        # Este es el contenedor clave que tiene que estar centrado
        rx.vstack(
            contact_cards(),   # Tiene max_width="824px"
            solicitud_form(),  # Ahora también tiene max_width="824px"
            
            width="100%",
            align_items="center", # <--- ESTO ES LO QUE LO CENTRA
            spacing="8",
            padding_y="4rem",
        ),
        footer(),
        spacing="0",
        width="100%",
        background_color="rgb(10, 10, 15)", 
    )


# Configurar la app con estilos para animaciones
app = rx.App(
    style={
        "html": {
            "scroll_behavior": "smooth",
        },
        "@keyframes fadeIn": {
            "from": {
                "opacity": "0",
                "transform": "translateY(-10px)",
            },
            "to": {
                "opacity": "1",
                "transform": "translateY(0)",
            },
        },
    }
)

# Registrar páginas
app.add_page(index, route="/")
app.add_page(project, route="/project", title="Proyecto")
app.add_page(who_are_we, route="/quienes-somos", title="Quiénes Somos")
app.add_page(contact, route="/contact", title="Contacto")
