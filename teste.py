
from core.ControleInventario import ControleInventario

# #Lendo as recipes
# with open('data/recipes.json', 'r', encoding='utf-8') as arq_recipes:
#     RECIPES = json.load(arq_recipes)

    


teste = ControleInventario()


# teste.adicionar_item("fio_de_cobre", 100)
teste.remover_item("fio_de_cobre", 200)
