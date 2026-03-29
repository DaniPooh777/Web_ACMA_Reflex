# Web ACMA

Sitio web institucional de ACMA, desarrollado 100% en **Python** con [Reflex](https://reflex.dev/).

---

## Sobre el Proyecto

Web ACMA es una aplicación web full-stack construida enteramente en Python.
Usa [Reflex](https://reflex.dev/) para generar automáticamente un frontend
React y un backend FastAPI a partir de código Python puro.

**¿Qué significa esto?** Un solo lenguaje para todo. Sin JavaScript escrito a mano,
sin contextos separados, con hot-reload en desarrollo y type-safety con Pydantic.

## Funcionalidades

| Feature | Descripción |
|---------|-------------|
| 🏠 Home | Página principal con showcase de proyectos |
| 👥 Quiénes Somos | Información sobre el equipo ACMA |
| 📂 Proyectos | Galería de proyectos y trabajos realizados |
| 📬 Contacto | Formulario con carga de archivos adjuntos |
| 🍪 Cookies | Página de política de cookies |
| 🔍 SEO | Metadatos Open Graph + Schema.org estructurado |
| 🗺️ Sitemap | Generación automática de sitemap.xml |
| 📱 Responsive | Diseño mobile-first con Tailwind CSS v4 |

## Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd Web_ACMA

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Linux/Mac: source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env         # Editar con tus valores

# 5. Ejecutar en modo desarrollo
reflex run
```

Abrir [http://localhost:3000](http://localhost:3000).

## Estructura del Proyecto

```
Web_ACMA/
├── Web_ACMA.py              # Entry point de la app
├── state.py                 # Estado global y event handlers (rx.State)
├── rxconfig.py              # Configuración de Reflex y plugins
├── assets/                  # Imágenes, favicon y archivos estáticos
├── components/              # Componentes UI reutilizables
│   ├── navbar.py            #   Barra de navegación
│   ├── footer.py            #   Pie de página
│   ├── project_card.py      #   Card de proyecto
│   ├── information_card.py  #   Card informativa
│   ├── seo_metadata.py      #   Metadatos SEO y Schema.org
│   └── ...
├── views/
│   ├── body/                # Contenido principal de cada página
│   │   ├── home/            #   Página principal
│   │   ├── contact/         #   Formulario de contacto
│   │   ├── projects/        #   Galería de proyectos
│   │   ├── who_are_we/      #   Quiénes somos
│   │   └── cookies/         #   Política de cookies
│   └── header/              # Encabezados de página
└── styles/
    ├── colors.py            # Paleta de colores del proyecto
    ├── components_style/    # Estilos por componente
    └── views_style/         # Estilos por vista
```

## Scripts Disponibles

```bash
reflex run          # Desarrollo con hot-reload
reflex export       # Build de producción
reflex db init      # Inicializar base de datos
reflex db migrate   # Ejecutar migraciones
```

## Stack Tecnológico

| Categoría | Tecnología |
|-----------|-----------|
| Framework | [Reflex](https://reflex.dev/) 0.8.27 |
| Lenguaje | Python 3.14 |
| Backend | FastAPI (auto-generado) |
| Frontend | React (auto-generado) |
| CSS | Tailwind CSS v4 (plugin) |
| ORM | SQLAlchemy 2.0 + SQLModel |
| Servidor | Granian 2.7 |
| Caché | Redis 7.2 |
| Validación | Pydantic v2 |

## Configuración

El proyecto usa un archivo `.env` para variables sensibles.
**Nunca commitear** este archivo al repositorio (está en `.gitignore`).

```bash
cp .env.example .env
# Editar .env con tus valores reales
```

## License

© 2026 ACMA. Todos los derechos reservados.
