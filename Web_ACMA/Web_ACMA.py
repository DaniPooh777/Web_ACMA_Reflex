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
from Web_ACMA.state import State  # Importar State desde el archivo separado


# Página Inicio
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            header(
                "Tu Aliado en la Innovación Educativa",
                "Transformamos tu visión pedagógica en recursos digitales de alta calidad, ahorrándote tiempo y garantizando la excelencia."
            ),
            link_button()
        ),
        problem_solutions(),
        resources(),
        caracteristics(),
        footer(),
        spacing="0",
        width="100%"
    )


# Página Proyectos - ACTUALIZADA
def project() -> rx.Component:
    return rx.vstack(
        navbar(),
        projects(),  # Usando el nuevo componente
        footer(),
        spacing="0",
        width="100%"
    )


# Página Quiénes Somos
def who_are_we() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Profundizando en ACMA",
            ""
        ),
        information(),
        founder(),
        footer(),
        spacing="0",
        width="100%"
    )


# Página Contacto
def contact() -> rx.Component:
    return rx.vstack(
        navbar(),
        problem_solutions(),
        footer(),
        spacing="0",
        width="100%"
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