
def formatar_nome_recipe(_nome):
    _excecoes = ["de", "da", "do", "das", "dos", "e"]

    _nome_formatado= " ".join([p if p in _excecoes else p.capitalize() for p in _nome.lower().split()])
    

    return _nome_formatado.replace("_", " ")
