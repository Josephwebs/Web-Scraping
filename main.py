import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/index.html"
def start(url): # Esta funcion nos permitira abrir la url y almacenar los datos que se encuentan en cada articulo de libro como el titulo, el precio y el cover
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    titl = soup.find_all("h3")
    cost = soup.find_all("p", class_ = "price_color")
    cov = soup.find_all("div", class_= "image_container")
    return (titl,cost,cov)
starts = start(url)
"""
Se almacenara cada dato de los libros dentro de las siguientes listas, 
luego se juntaran todas las listas y se identificara cada libro
y sus datos por su indice
"""
links = list() # almacena los links de cada libro para obtener los demas datos
title = list() # almacena los titulos 
price = list() # almacena los precios
stock = list() # almacena si el titulo esta en stock y cuantos libros hay
category_book = list()
cover = list() #almacena las url de las portadas
upc = list() #almacena el upc de cada libro
product_Type = list() # almacena el tipo de producto
price_ex_tax = list() #almacena el precio sin el impuesto
price_in_tax = list()# almacena el precio con el impuesto 
tax= list() #almacena el impuesto 
availability = list() #almacena la cantidad de cada libro disponibles
number_of_reviews = list() #almaneca el numero de reviews

paginacion = 2 #Esta es una variable auxiliar que se usara para marcar las paginas de la 1 a la 50,
               #de esta manera obtendremos datos que se encuentran en cada ariculo de las paginas
               #como el titulo, el precio, el cover, el stock y tambien el link de cada libro que 
               #nos sera de mucha ayuda para obtener datos individuales de cada uno. 
while paginacion != 52:
    for i in starts[1]:          # se realiza un for para guardar los precios en una lista "price"
        price.append(i.text[1:])
    for titu in starts[0]:       # se realiza un for para guardar los titulos en la lista "title"
        sub = titu.find_all("a")
        title.append(sub[0].attrs.get("title")) 
    for a in starts[0]:          # se realiza un for para guardar los link de cada libro en una lista "links"
        link = a.find_all("a") 
        links.append(link[0].attrs.get("href"))
    for src in starts[2]:         # se realiza un for para guardar las portadas en una lista "cover"
        img = src.find_all("img")
        cover.append(img[0].attrs.get("src"))
    paginacion = str(paginacion) 
    url = "https://books.toscrape.com/catalogue/page-"+paginacion+".html"
    #Se cambia la url aumentando la paginacion hasta que llegue a la numero 50 que es hasta donde llega los link para presentar los libros
    paginacion = int(paginacion) + 1
    starts = start(url)
# el siguiente for es para recorrer cada pagina de cada libro para extraer sus datos individuales, stock, descripcion, precio con impuesto, etc.
for i in links:
    url = i
    if "catalogue" not in(i):
        page = requests.get(f"https://books.toscrape.com/catalogue/{url}")
    else:
        page = requests.get(f"https://books.toscrape.com/{url}")
    soup = BeautifulSoup(page.content, "html.parser")
    sto = soup.find("p", attrs=["instock availability"]).get_text().strip() #esto busca el stock
    category = soup.find("ul", attrs=["breadcrumb"]).find_next("li").find_next("li").find_next("li").get_text().strip() #esto busca la categoria del libro
    
    #ya que todos los datos de "UPC" hasta "number of reviews" se encuentran en tablas sin class se procede a buscar los datos uno por uno
    u = soup.find("td").get_text()
    pt = soup.find("td").find_next("td").get_text()
    excl_tax = soup.find("td").find_next("td").find_next("td").get_text()
    incl_tax = soup.find("td").find_next("td").find_next("td").find_next("td").get_text()
    t = soup.find("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
    rev = soup.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
    
    # Se realizan los appends para rellenar cada lista     
    stock.append(sto[:8])
    category_book.append(category)    
    upc.append(u)
    product_Type.append(pt)
    price_ex_tax.append(excl_tax)
    price_in_tax.append(incl_tax)
    tax.append(t)
    availability.append(sto[-14:])
    number_of_reviews.append(rev)
"""
Las siguientes lineas son para convertir las listas a DataFrame para luego pasarlas a un archivo CSV
"""
headers = {'Title': title, 'Price': price, 'Stock': stock, 'Category' : category_book, 'Cover': cover, 'UPC': upc, 'Product Type': product_Type,'Price (excl. tax)': price_ex_tax, 'Price (incl. tax)': price_in_tax, 'Tax': tax , 'Availability': availability, 'Number of reviews': number_of_reviews} 
data = pd.DataFrame(headers)
data.to_csv('books_To_Scrape.csv')
