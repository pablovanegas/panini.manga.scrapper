
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Configura las opciones del controlador de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')  # Desactiva extensiones del navegador (opcional)

# Inicializa el controlador de Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# URL de la página web a la que deseas hacer scraping
url = 'https://paninitienda.com/collections/mangas?grid_list=grid-view&sort_by=manual&page=4&filter.v.price.gte=&filter.v.price.lte='

# Abre la página en el navegador
driver.get(url)

# Espera unos segundos para que la página cargue completamente
time.sleep(3)

# Realiza un scroll para cargar más contenido (puedes ajustar la cantidad de scrolls)
for _ in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.8);")
    time.sleep(2)  # Espera un momento después de cada scroll

# Obtiene el contenido de la página después de cargar todo el contenido
page_source = driver.page_source

# Parsea el contenido de la página con BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Encuentra los nombres de los productos utilizando el selector adecuado
product_names = soup.find_all('h2', class_='productitem--title')

# Abre un archivo de texto para escribir los nombres de los productos
with open('nombres_productos_comics.txt', 'w', encoding='utf-8') as archivo:
    # Itera a través de los elementos encontrados y escribe los nombres de los productos en el archivo
    for product in product_names:
        archivo.write(product.text + '\n')

# Cierra el navegador
driver.quit()