import requests
from bs4 import BeautifulSoup

def obtener_html(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.text
    except requests.RequestException as e:
        print(f"❌ Error al conectar con la página: {e}")
        return None

def obtener_soup(html):
    return BeautifulSoup(html, "html.parser") if html else None