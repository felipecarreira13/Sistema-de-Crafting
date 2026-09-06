import json

from core.ConsoleUi import *

#Lendo as recipes
with open('data/recipes.json', 'r', encoding='utf-8') as arq_recipes:
    RECIPES = json.load(arq_recipes)

    
with open('data/inventario.json', 'r', encoding='utf-8') as arq_inventario:
    INVENTARIO = json.load(arq_inventario)
    print(INVENTARIO)

# menu = ConsoleUi(RECIPES, INVENTARIO)

# menu.menu_inicial()