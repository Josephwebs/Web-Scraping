from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista = ["hola", "como","yo","bien","hola", "como"]
lista_2 = ["adios", "ella","el","yo","elllll", "donde"]
nueva_lista= DataFrame(list(zip(lista,lista_2)), columns=("titulos", "mas titulos"))
print(nueva_lista)