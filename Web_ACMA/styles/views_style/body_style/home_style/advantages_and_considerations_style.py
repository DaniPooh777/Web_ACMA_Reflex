import reflex as rx

# Contenedor principal de la sección
SECTION_CONTAINER_STYLE = dict(
    width="100%",
    max_width="1225px", # Ajustalo al max_width que usen tus tarjetas de arriba
    padding_top="4rem",
    align_items="center",
    margin_x="auto",
)

# Estilo de cada tabla/columna
TABLE_CONTAINER_STYLE = dict(
    width=["95%", "90%", "45%"], # Responsive: full en mobile, mitad en desktop
    border_radius="15px",
    padding="1.5rem",
    border="1px solid rgba(255, 255, 255, 0.1)",
    background="rgba(17, 24, 39, 0.5)",
)

# Títulos de las tablas
TITLE_STYLE = dict(
    font_size="1.5rem",
    font_weight="bold",
    margin_bottom="1rem",
)

# Filas de la tabla
ROW_STYLE = dict(
    width="100%",
    padding_y="0.75rem",
    border_bottom="1px solid rgba(255, 255, 255, 0.05)",
    align_items="center",
    spacing="3"
)

HEADER_TITLE_STYLE = {
    "font_size": "4rem",
    "font_weight": "800",
    "color": "white",
    "line_height": "1.1",
    "margin_bottom": "1rem",
    "white_space": "pre-line", # <--- ESTO permite que el \n funcione 
}