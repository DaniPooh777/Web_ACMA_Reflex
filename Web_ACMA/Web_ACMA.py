import reflex as rx
from rxconfig import config
from Web_ACMA.state import *
from Web_ACMA.styles.colors import *
from Web_ACMA.components.navbar import navbar
from Web_ACMA.views.header.header import header
from Web_ACMA.views.body.home.problems_solutions import problem_solutions
from Web_ACMA.views.body.home.resources import resources
from Web_ACMA.views.body.home.caracteristics import caracteristics
from Web_ACMA.components.footer import footer
from Web_ACMA.components.link_button import link_button
from Web_ACMA.views.body.who_are_we.information import information
from Web_ACMA.views.body.who_are_we.collaborators import collaborators 
from Web_ACMA.views.body.who_are_we.founder import founder
from Web_ACMA.views.body.projects.projects import projects
from Web_ACMA.views.body.contact.form import solicitud_form 
from Web_ACMA.views.body.contact.contact_cards import contact_cards
from Web_ACMA.views.body.home.frecuent_questions import frecuent_questions
from Web_ACMA.views.body.home.frecuent_questions import FaqState
from Web_ACMA.components.project_card import ProjectCardState
from Web_ACMA.views.body.home.advantages_and_considerations import advantages_and_considerations
from Web_ACMA.views.body.projects.new_horizonts import new_horizonts


# Página Inicio
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
            align_items="center",    
            spacing="4",
        ),
        problem_solutions(),
        resources(),
        caracteristics(),
        advantages_and_considerations(),
        frecuent_questions(),
        footer(),
        spacing="0",
        width="100%",
        align_items="center",       
        background_color=rx.color_mode_cond(
            light=SOFT_PAPER, 
            dark=DARK_PAPER   
        ),

        # Para resetear a sus valores iniciales
        on_mount=[
            ProjectCardState.clean_state, 
            FaqState.clean_state,
            FormState.limpiar_validacion          
        ]
    )

# Página Proyectos 
def project() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Proyectos Más Relevantes",
            "Descubre algunos de los proyectos más destacados que hemos realizado para el profesorado."
            ),
        projects(),
        new_horizonts(),  
        footer(),
        spacing="0",
        width="100%",
        background_color=rx.color_mode_cond(
            light=SOFT_PAPER, 
            dark=DARK_PAPER   
        ),
        on_mount=[
            ProjectCardState.clean_state, 
            FaqState.clean_state,
            FormState.limpiar_validacion          
        ]
    )

# Página Quiénes Somos
def who_are_we() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Profundizando en ACMA", 
            "Conoce a los que ensucian las manos."
        ),
        information(), 
        founder(),     
        collaborators(),
        footer(),
        width="100%",
        align_items="center",
        background_color=rx.color_mode_cond(
            light=SOFT_PAPER, 
            dark=DARK_PAPER   
        ),
        on_mount=[
            ProjectCardState.clean_state, 
            FaqState.clean_state,
            FormState.limpiar_validacion         
        ]
    )

# Página Contacto
def contact() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Contacta con ACMA",
            "Estamos aquí para ayudarte a crear los mejores recursos educativos."
        ),
        rx.vstack(
            contact_cards(),   
            solicitud_form(),  
            
            width="100%",
            align_items="center", 
            spacing="8",
            padding_y="4rem",
        ),
        footer(),
        spacing="0",
        width="100%",
        background_color=rx.color_mode_cond(
            light=SOFT_PAPER, 
            dark=DARK_PAPER   
        ), 
        on_mount=[
            ProjectCardState.clean_state, 
            FaqState.clean_state,
            FormState.limpiar_validacion         
        ]
    )

# Configuración de la app con estilos para animaciones
app = rx.App(
    head_components=[
        rx.el.link(rel="icon", href="/Acma Logo 2025-2026.png")
    ],
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
    },
    theme=rx.theme(
        appearance="inherit", 
        has_background=True,
        radius="large",
        accent_color="blue",
    ),
    
)

# Registrar páginas
app.add_page(index, route="/", title="ACMA | Inicio")
app.add_page(project, route="/project", title="ACMA | Proyecto")
app.add_page(who_are_we, route="/quienes-somos", title="ACMA | Quiénes Somos")
app.add_page(contact, route="/contact", title="ACMA | Contacto")
