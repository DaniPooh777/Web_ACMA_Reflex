import reflex as rx
from Web_ACMA.styles.views_style.body_style.cookies_style.cookies_style import (
    COOKIES_CONTAINER_STYLE,
    COOKIES_DATE_STYLE,
    COOKIES_CARD_STYLE,
    COOKIES_CARD_TITLE_STYLE,
    COOKIES_SUBTITLE_STYLE,
    COOKIES_TEXT_STYLE,
    COOKIES_LIST_STYLE,
    COOKIES_BOLD_TEXT_STYLE,
)


def cookies_view() -> rx.Component:
    """Vista principal de la página de Cookies."""
    return rx.vstack(
        # Fecha de última modificación
        rx.text(
            "Última modificación: 28 de marzo de 2026",
            style=COOKIES_DATE_STYLE,
        ),
        # Tarjeta 1: Uso de Cookies Técnicas
        _cookies_card(
            title="Uso de Cookies Técnicas",
            content="""Este sitio web utiliza únicamente cookies técnicas que son estrictamente necesarias para su correcto 
            funcionamiento. Al ser esenciales para que puedas navegar y utilizar las opciones o servicios solicitados, 
            no requieren de tu consentimiento según el artículo 22.2 de la LSSI-CE.""",
        ),
        # Tarjeta 2: ¿Qué cookies utilizamos?
        _cookies_card(
            title="¿Qué cookies utilizamos?",
            content="Dado que este sitio web tiene como únicos fines mostrar información sobre ACMA y permitir el contacto mediante formulario, únicamente utilizamos cookies técnicas esenciales:",
            list_items=[
                "Preferencia de tema: Recordar si has seleccionado modo claro u oscuro para que no tengas que cambiarlo cada vez que visitas la web.",
                "Funcionamiento del formulario: Garantizar que el formulario de contacto funcione correctamente durante tu sesión de navegación.",
                "Seguridad básica: Proteger contra ataques y mantener la integridad de la sesión.",
            ],
        ),
        # Tarjeta 3: Identidad del Responsable
        _cookies_card(
            title="Identidad del Responsable de la Infraestructura",
            content="""Para garantizar la trazabilidad de la responsabilidad legal y cumplir con las obligaciones del marco 
            jurisdiccional vigente (LSSI-CE y RGPD), se establecen los datos identificativos del titular del control 
            operativo y de los datos:""",
            subtitles=[
                ("Titular:", "Agencia de Contenido Manyanet Alcobendas (ACMA)"),
                ("NIF:", "R2800965B"),
                ("Domicilio:", "Alcobendas, Carretera El Goloso, Km 3,780"),
                ("Contacto:", "acma@alcobendas.manyanet.org"),
            ],
        ),
        # Tarjeta 4: Alcance y Base Operativa
        _cookies_card(
            title="Alcance y Base Operativa",
            content="""El modelo operativo de esta plataforma se rige por el principio de minimización. Solo se captura y 
            procesa la información estrictamente indispensable para: (1) mostrar el contenido publicitario de los servicios 
            de ACMA, y (2) procesar las consultas recibidas a través del formulario de contacto. No existen mecanismos de 
            rastreo, analítica o monetización de datos.""",
        ),
        # Tarjeta 5: Política de Cookies
        _cookies_card(
            title="Política de Cookies",
            content="Esta infraestructura despliega de manera exclusiva cookies de carácter técnico.",
            list_items=[
                "Sin rastreo: Nula integración de scripts analíticos, píxeles de seguimiento o herramientas de terceros.",
                "Sin perfilado: No se genera ningún perfil de comportamiento ni se utiliza publicidad personalizada.",
                "Sin consentimiento: Al carecer de fines analíticos o publicitarios, estas cookies operan bajo la exención de consentimiento estipulada en el artículo 22.2 de la LSSI-CE.",
            ],
        ),
        # Tarjeta 6: Tratamiento de Datos del Formulario
        _cookies_card(
            title="Tratamiento de Datos del Formulario de Contacto",
            content="Los datos que nos facilitas voluntariamente a través del formulario de contacto se utilizan exclusivamente para:",
            list_items=[
                "Responder a tu consulta o solicitud de información sobre los servicios de ACMA.",
                "Gestionar la comunicación necesaria para dar seguimiento a tu petición.",
                "No se incorporan a bases de datos de marketing ni se comparten con terceros.",
            ],
        ),
        style=COOKIES_CONTAINER_STYLE,
        spacing="0",
    )


def _cookies_card(
    title: str,
    content: str = "",
    subtitles: list[tuple[str, str]] = None,
    list_items: list[str] = None,
) -> rx.Component:
    """Componente reutilizable para las tarjetas de cookies."""
    children = []

    # Título de la tarjeta
    children.append(rx.heading(title, style=COOKIES_CARD_TITLE_STYLE))

    # Contenido principal (si existe)
    if content:
        children.append(rx.text(content, style=COOKIES_TEXT_STYLE))

    # Subtítulos con contenido (si existen)
    if subtitles:
        for subtitle_title, subtitle_content in subtitles:
            children.append(
                rx.box(
                    rx.text(subtitle_title, style=COOKIES_BOLD_TEXT_STYLE),
                    rx.text(" " + subtitle_content, style=COOKIES_TEXT_STYLE),
                    display="flex",
                    flex_direction="row",
                    flex_wrap="wrap",
                    gap="0.25rem",
                    width="100%",
                )
            )

    # Lista de elementos (si existen)
    if list_items:
        children.append(
            rx.unordered_list(
                *[rx.list_item(item) for item in list_items],
                style=COOKIES_LIST_STYLE,
            )
        )

    return rx.box(
        rx.vstack(*children, spacing="3"),
        style=COOKIES_CARD_STYLE,
    )
