from typing import Text
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
titl = soup.find_all("h3")
cost = soup.find_all("p", class_ = "price_color")
cov = soup.find_all("div", class_= "image_container")

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
product_description = list()
upc = list()
product_Type = list()
price_ex_tax = list()
price_in_tax = list()
tax= list()
availability = list()
number_of_reviews = list()
paginacion = 2 #Esta es una variable auxiliar que se usara para marcar las paginas de la 1 a la 50,
               #de esta manera obtendremos datos que se encuentran en cada ariculo de las paginas
               #como el titulo, el precio, el cover, el stock y tambien el link de cada libro que 
               #nos sera de mucha ayuda para obtener datos individuales de cada uno. 
while paginacion != 52:
    print(url)
    for i in cost:          # se realiza un for para guardar los precios en una lista "price"
        price.append(i.text[1:])
    for titu in titl:       # se realiza un for para guardar los titulos en la lista "title"
        sub = titu.find_all("a")
        title.append(sub[0].attrs.get("title")) 
    for a in titl:          # se realiza un for para guardar los link de cada libro en una lista "links"
        link = a.find_all("a") 
        links.append(link[0].attrs.get("href"))
    for src in cov:         # se realiza un for para guardar las portadas en una lista "cover"
        img = src.find_all("img")
        cover.append(img[0].attrs.get("src"))
    paginacion = str(paginacion) 
    url = "https://books.toscrape.com/catalogue/page-"+paginacion+".html"
    #Se cambia la url aumentando la paginacion hasta que llegue a la numero 50 que es hasta donde llega los link para presentar los libros
    paginacion = int(paginacion) + 1
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    titl = soup.find_all("h3")
    cost = soup.find_all("p", class_ = "price_color")
    cov = soup.find_all("div", class_= "image_container")
# el siguiente for es para recorrer cada pagina de cada libro para extraer sus datos individuales, stock, descripcion, precio con impuesto, etc.

for i in links:
    url = i
    if "catalogue" not in(i):
        page = requests.get(f"https://books.toscrape.com/catalogue/{url}")
    else:
        page = requests.get(f"https://books.toscrape.com/{url}")
    soup = BeautifulSoup(page.content, "html.parser")
    sto = soup.find("p", attrs=["instock availability"]).get_text().strip()
    stock.append(sto)
    des = soup.find("h2").find_next("p").get_text()
    product_description.append(des)
    category = soup.find("ul", attrs=["breadcrumb"]).find_next("li").find_next("li").find_next("li").get_text().strip()
    category_book.append(category)
#Para terminar de obtener los datos se obtiene el product information y como todo esta
#en la misma tabla, solamente se prosigue a obtener el dato siguiente y asi se termina
#el proceso de extraccion de datos.
    u = soup.find("td").get_text()
    u_ = soup.find("td").find_next("td").get_text()
    u__ = soup.find("td").find_next("td").find_next("td").get_text()
    u___ = soup.find("td").find_next("td").find_next("td").find_next("td").get_text()
    u____ = soup.find("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
    u_____ = soup.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
    u______ = soup.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
    upc.append(u)
    product_Type.append(u_)
    price_ex_tax.append(u__)
    price_in_tax.append(u___)
    tax.append(u____)
    availability.append(u_____)
    number_of_reviews.append(u______)