"""API -> https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json"""

"""
Resultados para la búsqueda “chromecast”, pero deberás elegir otros términos para el experimento que permitan
enriquecer el análisis en un hipotético dashboard 
(ejemplo Google Home, Apple TV, Amazon Fire TV, o afines para poder comparar dispositivos portátiles, o bien elegir
otros 3 que te interesen para comparar)
"""

"""
Por cada resultado, realizar el correspondiente GET por Item_Id al recurso público:
https://api.mercadolibre.com/items/{Item_Id}
"""

"""
Escribir los resultados en un archivo plano delimitado por comas, desnormalizando
el JSON obtenido en el paso anterior, en tantos campos como sea necesario para
guardar las variables que te interesen modelar.
"""