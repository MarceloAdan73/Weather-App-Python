# 🌤️ Weather App - Dev

Aplicación del clima desarrollada con FastAPI y Vue.js 3.

## 🚀 Desarrollo Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/MarceloAdan73/app-clima-python.git
cd app-clima-python
git checkout dev
```

### 2. Crear archivo .env
```bash
echo "OPENWEATHER_API_KEY=tu_api_key_aqui" > .env
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar servidor
```bash
uvicorn main:app --reload
```

La app estará disponible en: http://localhost:8000

## 🌐 Despliegue en Render

### Usando Blueprint (render.yaml)

1. Push a la rama `dev` en GitHub
2. Conectar el repositorio en [Render Dashboard](https://dashboard.render.com)
3. Render detectará automáticamente el `render.yaml`
4. Configurar `OPENWEATHER_API_KEY` en Environment Variables

### Usando Procfile

1. Push cambios
2. Crear nuevo Web Service en Render
3. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Añadir `OPENWEATHER_API_KEY` en Environment Variables

## 📁 Estructura del Proyecto

```
weather-app/
├── main.py           # Backend FastAPI
├── templates/
│   └── index.html    # Frontend Vue.js
├── static/           # Archivos estáticos
├── requirements.txt   # Dependencias Python
├── render.yaml       # Configuración Render
├── Procfile         # Proceso de inicio
└── .env             # Variables de entorno (local)
```

## 🔧 API Endpoints

| Endpoint | Descripción |
|----------|-------------|
| `GET /` | Página principal |
| `GET /healthz` | Health check |
| `GET /api/clima?ciudad={nombre}` | Clima por ciudad |
| `GET /api/clima?lat={lat}&lon={lon}` | Clima por coordenadas |

## 📝 Variables de Entorno

| Variable | Descripción | Requerido |
|----------|-------------|-----------|
| `OPENWEATHER_API_KEY` | API Key de OpenWeatherMap | Sí (en producción) |
| `PORT` | Puerto del servidor (automático en Render) | No |

## 🎨 Stack Tecnológico

- **Backend**: FastAPI + uvicorn
- **Frontend**: Vue.js 3 + Font Awesome
- **API**: OpenWeatherMap
- **Despliegue**: Render
