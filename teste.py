from core.CraftingCalculator import CraftingCalculator
from core.ControleInventario import ControleInventario

# #Lendo as recipes
# with open('data/recipes.json', 'r', encoding='utf-8') as arq_recipes:
#     RECIPES = json.load(arq_recipes)

recipe_teste = {
    'input': [
        {
            'nome': 'minerio_de_ferro',
            'qnt': 40
        }
    ],
    'output': [
        {
            'nome': 'placa_de_ferro',
            'qnt': 20
        }
    ]
}
    

calculadora = CraftingCalculator()
teste = ControleInventario()


# teste.adicionar_item("fio_de_cobre", 100)
teste.craftar_item(recipe_teste)
