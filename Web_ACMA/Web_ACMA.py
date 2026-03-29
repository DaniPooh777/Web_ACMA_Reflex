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
from Web_ACMA.views.body.home.advantages_and_considerations import (
    advantages_and_considerations,
)
from Web_ACMA.views.body.projects.new_horizonts import new_horizonts
from Web_ACMA.views.body.cookies.cookies import cookies_view
from Web_ACMA.components.seo_metadata import (
    get_homepage_meta,
    get_projects_meta,
    get_who_are_we_meta,
    get_contact_meta,
    get_cookies_meta,
    get_schema_markup_component,
)


# Página Inicio
@rx.page(
    route="/",
    title="ACMA | Inicio",
    description="ACMA - Agencia de Contenido Manyanet Alcobendas. Creamos recursos educativos digitales de alta calidad.",
    image="https://web-acma-gray-orca.reflex.run/og-image.png",
    meta=get_homepage_meta(),
)
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            header(
                "ACMA: Tu aliado confiable en la\nInnovación Educativa",
                "Transformamos tu visión pedagógica en recursos digitales de alta calidad",
            ),
            link_button(),
            width="100%",
            align_items="center",
            spacing={"initial": "2", "sm": "3", "md": "4"},
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
        background_color=rx.color_mode_cond(light=SOFT_PAPER, dark=DARK_PAPER),
        on_mount=[
            State.clean_state,
            ProjectCardState.clean_state,
            FaqState.clean_state,
            FormState.limpiar_validacion,
        ],
    )


# Página Proyectos
@rx.page(
    route="/project",
    title="ACMA | Proyectos",
    description="Descubre nuestros proyectos educativos más destacados.",
    image="https://web-acma-gray-orca.reflex.run/og-image.png",
    meta=get_projects_meta(),
)
def project() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Proyectos Más Relevantes",
            "Descubre algunos de los proyectos más destacados que hemos realizado para el profesorado.",
        ),
        projects(),
        new_horizonts(),
        footer(),
        spacing="0",
        width="100%",
        background_color=rx.color_mode_cond(light=SOFT_PAPER, dark=DARK_PAPER),
        on_mount=[
            ProjectCardState.clean_state,
            FaqState.clean_state,
            FormState.limpiar_validacion,
        ],
    )


# Página Quiénes Somos
@rx.page(
    route="/quienes-somos",
    title="ACMA | Quiénes Somos",
    description="Conoce a ACMA, el equipo detrás de la Agencia de Contenido Manyanet Alcobendas.",
    image="https://web-acma-gray-orca.reflex.run/og-image.png",
    meta=get_who_are_we_meta(),
)
def who_are_we() -> rx.Component:
    return rx.vstack(
        navbar(),
        header("Profundizando en ACMA", "Conoce a los que ensucian las manos."),
        information(),
        founder(),
        collaborators(),
        footer(),
        width="100%",
        align_items="center",
        background_color=rx.color_mode_cond(light=SOFT_PAPER, dark=DARK_PAPER),
        on_mount=[
            ProjectCardState.clean_state,
            FaqState.clean_state,
            FormState.limpiar_validacion,
        ],
    )


# Página Contacto
@rx.page(
    route="/contact",
    title="ACMA | Contacto",
    description="Contacta con ACMA para solicitar tus recursos educativos.",
    image="https://web-acma-gray-orca.reflex.run/og-image.png",
    meta=get_contact_meta(),
)
def contact() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Contacta con ACMA",
            "Estamos aquí para ayudarte a crear los mejores recursos educativos.",
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
        background_color=rx.color_mode_cond(light=SOFT_PAPER, dark=DARK_PAPER),
        on_mount=[
            ProjectCardState.clean_state,
            FaqState.clean_state,
            FormState.limpiar_validacion,
        ],
    )


# Página Cookies
@rx.page(
    route="/cookies",
    title="ACMA | Política de Cookies",
    description="Política de cookies de ACMA.",
    image="https://web-acma-gray-orca.reflex.run/og-image.png",
    meta=get_cookies_meta(),
)
def cookies() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(
            "Política de Cookies",
            "",
        ),
        cookies_view(),
        footer(),
        spacing="0",
        width="100%",
        background_color=rx.color_mode_cond(light=SOFT_PAPER, dark=DARK_PAPER),
        on_mount=[
            ProjectCardState.clean_state,
            FaqState.clean_state,
            FormState.limpiar_validacion,
        ],
    )


# Configuración de la app
app = rx.App(
    head_components=[
        rx.el.link(rel="icon", href="/Acma Logo 2025-2026.png"),
        get_schema_markup_component(),
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
        "@keyframes fadeInSlideUp": {
            "from": {
                "opacity": "0",
                "transform": "translateY(20px)",
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
