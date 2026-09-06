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

    #Core das mudanças ----------------------------
    def adicionar_item(self, _item, _qnt):
        self.inventario[_item]['qnt'] += _qnt
        print(f'{_qnt} {_item} adicionados ao inventario')
        self.atualizar_inventario()
        
    def remover_item(self, _item, _qnt):
        self.inventario[_item]['qnt'] -= _qnt
        print(f'{_qnt} {_item} removidos do inventario')
        self.atualizar_inventario()
    # ---------------------------------------------
    
    def craftar_item(self, _receita):
        
        #NAO PRECISA INFORMAR QUANTIDADE PORQUE JA VOU RECEBER ELA FORMATADA
        for _input_item in _receita['input']:
            self.remover_item(_input_item['nome'], _input_item['qnt'])
            
        for _output_item in _receita['output']:
            self.adicionar_item((_output_item['nome']), _output_item['qnt'])
            
            
    def atualizar_inventario(self):
        with open('data/inventario.json', 'w', encoding='utf-8') as arq_inventario:
            json.dump(self.inventario, arq_inventario, indent=4, ensure_ascii=False)