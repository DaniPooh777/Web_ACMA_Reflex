import reflex as rx
from reflex.components.el.elements.scripts import Script


def get_seo_meta_list(
    title: str,
    description: str,
    canonical_url: str,
    og_image: str = "/og-image.png",
    og_type: str = "website",
) -> list[dict]:

    site_name = "ACMA | Agencia de Contenido Manyanet Alcobendas"

    return [
        # Basic meta
        {
            "name": "keywords",
            "content": "recursos educativos, contenido escolar, materiales didácticos, educación, ACMA, Manyanet, Alcobendas",
        },
        {"name": "author", "content": "ACMA"},
        {"name": "robots", "content": "index, follow"},
        {"name": "canonical", "content": canonical_url},
        # Open Graph
        {"property": "og:title", "content": f"{title} | {site_name}"},
        {"property": "og:description", "content": description},
        {"property": "og:type", "content": og_type},
        {"property": "og:url", "content": canonical_url},
        {"property": "og:image", "content": og_image},
        {"property": "og:image:width", "content": "1200"},
        {"property": "og:image:height", "content": "630"},
        {"property": "og:site_name", "content": site_name},
        {"property": "og:locale", "content": "es_ES"},
        # Twitter Cards
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": f"{title} | {site_name}"},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": og_image},
        # Theme color
        {"name": "theme-color", "content": "#3b82f6"},
    ]


def get_homepage_meta() -> list[dict]:
    """Metadatos para la página de inicio."""
    return get_seo_meta_list(
        title="Inicio",
        description="ACMA - Agencia de Contenido Manyanet Alcobendas. Creamos recursos educativos digitales de alta calidad.",
        canonical_url="https://web-acma-gray-orca.reflex.run/",
        og_image="https://web-acma-gray-orca.reflex.run/og-image.png",
    )


def get_projects_meta() -> list[dict]:
    """Metadatos para la página de proyectos."""
    return get_seo_meta_list(
        title="Proyectos",
        description="Descubre nuestros proyectos educativos más destacados. Pósters, presentaciones y cuestionarios.",
        canonical_url="https://web-acma-gray-orca.reflex.run/project",
        og_image="https://web-acma-gray-orca.reflex.run/og-image.png",
    )


def get_who_are_we_meta() -> list[dict]:
    """Metadatos para la página Quiénes Somos."""
    return get_seo_meta_list(
        title="Quiénes Somos",
        description="Conoce a ACMA, el equipo detrás de la Agencia de Contenido Manyanet Alcobendas.",
        canonical_url="https://web-acma-gray-orca.reflex.run/quienes-somos",
        og_image="https://web-acma-gray-orca.reflex.run/og-image.png",
    )


def get_contact_meta() -> list[dict]:
    """Metadatos para la página de contacto."""
    return get_seo_meta_list(
        title="Contacto",
        description="Contacta con ACMA para solicitar tus recursos educativos.",
        canonical_url="https://web-acma-gray-orca.reflex.run/contact",
        og_image="https://web-acma-gray-orca.reflex.run/og-image.png",
    )


def get_cookies_meta() -> list[dict]:
    """Metadatos para la página de cookies."""
    return get_seo_meta_list(
        title="Política de Cookies",
        description="Política de cookies de ACMA.",
        canonical_url="https://web-acma-gray-orca.reflex.run/cookies",
        og_image="https://web-acma-gray-orca.reflex.run/og-image.png",
    )


def get_schema_markup_component() -> rx.Component:
    """
    Genera el Schema.org JSON-LD para la organización.

    Ayuda a Google a entender la empresa y mostrar rich snippets.
    """
    schema_json = """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://web-acma-gray-orca.reflex.run/#organization","name":"ACMA - Agencia de Contenido Manyanet","url":"https://web-acma-gray-orca.reflex.run","logo":{"@type":"ImageObject","url":"https://web-acma-gray-orca.reflex.run/Acma Logo 2025-2026.png"},"description":"Agencia de contenido educativo que transforma visiones pedagógicas en recursos digitales.","contactPoint":{"@type":"ContactPoint","email":"acma@alcobendas.manyanet.org","contactType":"customer service"}},{"@type":"LocalBusiness","@id":"https://web-acma-gray-orca.reflex.run/#business","name":"ACMA","url":"https://web-acma-gray-orca.reflex.run","email":"acma@alcobendas.manyanet.org","address":{"@type":"PostalAddress","addressLocality":"Alcobendas","addressRegion":"Madrid","addressCountry":"ES"}},{"@type":"WebSite","@id":"https://web-acma-gray-orca.reflex.run/#website","url":"https://web-acma-gray-orca.reflex.run","name":"ACMA - Recursos Educativos","publisher":{"@id":"https://web-acma-gray-orca.reflex.run/#organization"}},{"@type":"EducationalOrganization","@id":"https://web-acma-gray-orca.reflex.run/#school","name":"ACMA","description":"Organización educativa especializada en creación de recursos educativos digitales.","url":"https://web-acma-gray-orca.reflex.run"}]}"""

    # Wrap in a proper script tag with type attribute
    script_tag = f'<script type="application/ld+json">{schema_json}</script>'
    return Script.create(script_tag)
