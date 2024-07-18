from datetime import datetime
from threading import Thread
import requests

from sanic import Sanic, response, HTTPResponse, json, redirect, html, file
from sanic.response import text, html

from jinja2 import Environment, FileSystemLoader, select_autoescape

from sanic_session import Session

from database import Database

dadata_token = "37246a81de5e3317c98fb92126a5e5bf19aae2b2"
dadata_secret = "3f9e0cfb14948539950d4543f816fe1deeff0f51"

app = Sanic("WeatherForecastServer")
env = Environment( #Инициализировали Jinja2
    loader=FileSystemLoader('static/html'),  # Указали путь к шаблонам для Jinja2
    autoescape=select_autoescape(['html', 'xml']) # Указали типы файлов
)

local_link = "localhost:3000"

DEBUG_MODE = False

app.static("/static/", "./static/") # Маршрут на папку со статичными файлами

Session(app)

def getSuggestions(text):
    suggestions = requests.get("https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", 
                            params={"query": text, 
                                    "count": 5, 
                                    "from_bound": { "value": "region" },
                                    "to_bound": { "value": "city" }  
                                    }, 
                            headers={"Authorization": f"Token {dadata_token}"}).json()['suggestions']
    return suggestions

def getCoords(text):
    coords = requests.post("https://cleaner.dadata.ru/api/v1/clean/address",headers={
                            "Authorization": f"Token {dadata_token}",
                            "X-Secret": dadata_secret
                            },
                            json=[text]).json()[0]
    return coords['geo_lat'], coords['geo_lon']

@app.get("/")
async def index(request):
    data = {'last_request':request.ctx.session.get('last_request')}
    template = env.get_template('index.html')
    return html(template.render(data=data))

def getForecast(lat, lon):
    return requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": lat, "longitude": lon, "current_weather": True}).json()

@app.post("/weather")
async def get_weather(request):
    request.ctx.session['last_request'] = request.form.get("city")
    geo_lat, geo_lon = getCoords(request.form.get("city"))
    success = True
    if not geo_lat is None:
        try:
            forecast = getForecast(geo_lat, geo_lon)
        except:
            forecast = None
            success = False
    else:
        forecast = None
        success = False
    Database.addRequest(request.form.get("city"), success)
    
    template = env.get_template('weather.html')
    data = {'latitude':geo_lat,
            'longitude':geo_lon,
            'is_success':not geo_lat is None,
            'city': request.form.get("city")}
    
    if forecast: data['forecast'] = forecast
    return html(template.render(data=data))

@app.get("/stats")
async def get_stats(request):
    return json(Database.getRequests())

@app.post("/suggestion")
async def suggestion(request):
    return json(getSuggestions(request.json.get("text")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=DEBUG_MODE)