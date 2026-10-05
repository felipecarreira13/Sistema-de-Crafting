from core.CraftingCalculator import CraftingCalculator
from core.ControleInventario import ControleInventario

# #Lendo as recipes
# with open('data/recipes.json', 'r', encoding='utf-8') as arq_recipes:
#     RECIPES = json.load(arq_recipes)

recipe_teste = {
    'input': [
        # {
        #     'nome': 'placa_de_ferro',
        #     'qnt': 40
        # },
        {
            'nome': 'minerio_de_ferro',
            'qnt': 40
        }
    ],
    'output': [
        {
            'nome': 'placa_de_ferro',
            'qnt': 40
        }
    ]
}
    
recipe_teste1 = {
    'input': [
        {
            'nome': 'placa_de_ferro',
            'qnt': 40
        }
    ],
    'output': [
        {
            'nome': 'minerio_de_ferro',
            'qnt': 40
        }
    ]
}
    

calculadora = CraftingCalculator()
teste = ControleInventario()


# teste.adicionar_item("fio_de_cobre", 100)
# teste.craftar_item(recipe_teste)
teste.adicionar_item('placa_de_ferro', 1000)
teste.adicionar_item('fio_de_cobre', 1000)
