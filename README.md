Este es un proyecto personal para poder mejorar habilidades de Web Scraping usando librerias requests y bs4.
Fue sacado de una entrevista de trabajo que tuve hace un tiempo en donde me pedian realizar el ejercicio.

A continuacion indicare lo que se tiene que desarrollar en python3 para lograr el proyecto. 

recorrer paginacion de este sitio http://books.toscrape.com/

De cada libro se obtiene la siguiente información:
    * Title
    * Price
    * Stock
    * Category (Travel, Mystery, Historical Fiction, etc)
    * Cover (url de la carátula del libro)
    * Product Description
        * UPC
        * Product Type
        * Price (excl. tax)
        * Price (incl. tax)
        * Tax
        * Availability
        * Number of reviews

Los resultados se exportaron en un archivo CSV con las siguientes cabeceras:
    * Title
    * Price
    * Stock (Se almacena solamente si el libro esta en stock o no)
    * Category
    * Cover
    * UPC
    * Product Type
    * Price (excl. tax)
    * Price (incl. tax)
    * Tax
    * Availability (Se almacena la cantidad de libros disponibles)
    * Number of reviews
