import reflex as rx

config = rx.Config(
    app_name="Web_ACMA",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)