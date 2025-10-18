from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="App del Clima")

# Configuración
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/")
async def read_root():
    return FileResponse("templates/index.html")

@app.get("/healthz")
async def health_check():
    return {"status": "healthy", "message": "Service is running"}

@app.get("/api/clima")
async def obtener_clima(ciudad: str = None, lat: float = None, lon: float = None):
    """
    Obtiene el clima por ciudad o por coordenadas GPS
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API Key no configurada")
    
    params = {
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    
    if ciudad:
        params["q"] = ciudad
    elif lat and lon:
        params["lat"] = lat
        params["lon"] = lon
    else:
        raise HTTPException(status_code=400, detail="Debe proporcionar ciudad o coordenadas")
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        datos = response.json()
        
        # Procesar y formatear los datos
        return {
            "ciudad": datos["name"],
            "pais": datos["sys"]["country"],
            "temperatura": round(datos["main"]["temp"]),
            "sensacion_termica": round(datos["main"]["feels_like"]),
            "humedad": datos["main"]["humidity"],
            "descripcion": datos["weather"][0]["description"].title(),
            "icono": datos["weather"][0]["icon"],
            "viento": datos["wind"]["speed"]
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error al conectar con la API del clima")

# Montar archivos estáticos solo si la carpeta existe
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
    print("✅ Static files mounted successfully")
except Exception as e:
    print(f"⚠️  Static files not mounted: {e}")