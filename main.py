import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
pre = soup.find_all("p", class_ = "price_color")
ti = soup.find_all("h3")
cov = soup.find_all("div", class_= "image_container")
links = list() # almacena los links de cada libro para obtener los demas datos
title = list() # almacena los titulos 
price = list() # almacena los precios
stock = list() # almacena si el titulo esta en stock y cuantos libros hay
category = list()
cover = list() #almacena las url de las portadas
product_description = list()
upc = list()
product_Type = list()
price_ex_tax = list()
price_in_tax = list()
tax= list()
availability = list()
number_of_reviews = list()

paginacion = 2
while paginacion != 52:
    print(url)
    for i in pre:
        price.append(i.text[1:])
    for titu in ti:
        sub = titu.find_all("a")
        title.append(sub[0].attrs.get("title"))
    for a in ti:
        link = a.find_all("a")
        links.append(link[0].attrs.get("href"))
    for src in cov:
        img = src.find_all("img")
        cover.append(img[0].attrs.get("src"))
    paginacion = str(paginacion) # se realiza un for para guardar los precios en una lista "price"
    url = "https://books.toscrape.com/catalogue/page-"+paginacion+".html"
    #Se cambia la url aumentando la paginacion hasta que llegue a la numero 50 que es hasta donde llega la cantidad de libros
    paginacion = int(paginacion) + 1
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pre = soup.find_all("p", class_ = "price_color")
    ti = soup.find_all("h3")
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
#     cat = soup.f
#     cat = soup.find_all()
#     pro_des = soup.find("p")
#     pre_ex_tax = soup.find_all("h3")
#     pre_in_tax = soup.find_all("h3")
#     t = soup.find_all("h3")
#     avail = soup.find_all("h3")
#     num_of_rev = soup.find_all("h3")


