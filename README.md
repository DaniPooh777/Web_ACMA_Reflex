# 🌐 Web ACMA

Sitio web institucional de ACMA, desarrollado 100% en **Python** con [Reflex](https://reflex.dev/).

---

## Sobre el Proyecto

Web ACMA es una aplicación web full-stack construida enteramente en Python. Usa Reflex para generar automáticamente un frontend React y un backend FastAPI a partir de código Python puro.

**¿Qué significa esto?** Un solo lenguaje para todo —> sin JavaScript escrito a mano, con hot-reload en desarrollo y type-safety con Pydantic.

---

## Funcionalidades

| Página | Descripción |
|--------|-------------|
| 🏠 Home | Página principal con showcase de proyectos |
| 👥 Quiénes Somos | Información sobre el equipo ACMA |
| 📂 Proyectos | Galería de proyectos y trabajos realizados |
| 📬 Contacto | Formulario con carga de archivos adjuntos |
| 🍪 Cookies | Página de política de cookies |

---

## Inicio Rápido

### 🪟 Windows

```powershell
# 1. Clonar el repositorio
git clone <repo-url>
cd Web_ACMA

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
copy .env.example .env

# 5. Ejecutar en modo desarrollo
reflex run
```

### 🍎 macOS / 🐧 Linux

```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd Web_ACMA

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env

# 5. Ejecutar en modo desarrollo
reflex run
```

👉 Abrir [http://localhost:3000](http://localhost:3000)

---

## Estructura del Proyecto

```
Web_ACMA/
├── Web_ACMA.py              # Entry point de la app
├── state.py                 # Estado global y event handlers
├── rxconfig.py              # Configuración de Reflex
├── assets/                  # Imágenes y archivos estáticos
├── components/              # Componentes UI reutilizables
│   ├── navbar.py            # Barra de navegación
│   ├── footer.py            # Pie de página
│   ├── project_card.py      # Card de proyecto
│   └── ...
├── views/                   # Páginas de la app
│   ├── body/                # Contenido de cada página
│   │   ├── home/
│   │   ├── contact/
│   │   ├── projects/
│   │   └── who_are_we/
│   └── header/              # Encabezados de página
└── styles/                  # Colores y estilos
```

---

## Licence

© 2026 ACMA. Todos los derechos reservados.
