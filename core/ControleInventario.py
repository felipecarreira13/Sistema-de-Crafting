import json

class ControleInventario:
    def __init__(self):
        #Criacao do inventario a partir do arquivo
        with open('data/inventario.json', 'r', encoding='utf-8') as arq_inventario:
            self.inventario = json.load(arq_inventario)
            

    def listar_itens(self):
        print('Items no inventario: ')
        for item in self.inventario.values():
            # if item['qnt'] > 0:
            print(f'{item['nome']}: {item['qnt']}')

    def adicionar_item(self, _item, _qnt):
        self.inventario[_item]['qnt'] += _qnt
        print(f'{_qnt} {_item} adicionados ao inventario')
        self.atualizar_inventario()
        
    def remover_item(self, _item, _qnt):
        self.inventario[_item]['qnt'] -= _qnt
        print(f'{_qnt} {_item} removidos do inventario')
        self.atualizar_inventario()
        
    def craftar_item(self, _receita):
        
        #Tirando os itens do inventario
        for item in _receita:
            self.remover_item(item['nome'], item['qnt'])
            
            self.adicionar_item((item['nome']), item['qnt'])
            print(f'{item['qnt']} {item['nome']} adicionados ao inventario')
            
            
    def atualizar_inventario(self):
        with open('data/inventario.json', 'w', encoding='utf-8') as arq_inventario:
            json.dump(self.inventario, arq_inventario, indent=4, ensure_ascii=False)