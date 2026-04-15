# 🌤️ Weather App

> Aplicación del clima en tiempo real con un diseño moderno y responsivo.

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue.js">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

---

## ✨ Características

- 🌡️ **Clima en tiempo real** - Datos de OpenWeatherMap
- 📱 **Diseño responsivo** - Funciona en desktop, tablet y móvil
- 🔍 **Búsqueda intuitiva** - Busca por ciudad o usa tu ubicación
- 📅 **Pronóstico de 5 días** - Planea con anticipación
- 🌙 **Modo oscuro** - Interfaz elegante y moderna

---

## 🚀 Demo

🌐 **Live**: [weather-app.onrender.com](https://app-clima-python.onrender.com/)

---

## 🛠️ Instalación Local

### Prerrequisitos

- Python 3.11+
- API Key de [OpenWeatherMap](https://openweathermap.org/api)

### Pasos

```bash
# Clonar repositorio
git clone https://github.com/MarceloAdan73/Weather-App-Python.git
cd Weather-App-Python

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar API Key
echo "OPENWEATHER_API_KEY=tu_api_key" > .env

# Ejecutar servidor
uvicorn main:app --reload
```

🌐 **Abrir**: http://127.0.0.1:8000

---

## ☁️ Despliegue en Render

### Opción 1: Blueprint (Automático)

```bash
# Push a GitHub - Render detectará render.yaml automáticamente
git checkout -b dev
git add .
git commit -m "feat: improve responsive design"
git push origin dev
```

### Opción 2: Manual

1. Crear **New Web Service** en [Render Dashboard](https://dashboard.render.com)
2. Conectar repositorio GitHub
3. Configurar:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Agregar variable de entorno: `OPENWEATHER_API_KEY`

---

## 📂 Estructura

```
├── main.py              # API FastAPI
├── templates/
│   └── index.html      # Frontend Vue.js
├── requirements.txt    # Dependencias Python
├── render.yaml         # Configuración Render
└── Procfile            # Proceso de inicio
```

---

## 🔌 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Página principal |
| `GET` | `/healthz` | Health check |
| `GET` | `/api/clima?ciudad=Nombre` | Clima por ciudad |
| `GET` | `/api/clima?lat=X&lon=Y` | Clima por coordenadas |

---

## 📝 Variables de Entorno

| Variable | Descripción |
|----------|-------------|
| `OPENWEATHER_API_KEY` | API Key de OpenWeatherMap (requerido) |
| `PORT` | Puerto (automático en Render) |

---

## 📄 Licencia

MIT License - feel free to use this project.

---

## 👨‍💻 Autor

**Marcelo Adan** - [GitHub](https://github.com/MarceloAdan73)
