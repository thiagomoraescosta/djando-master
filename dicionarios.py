meu_dicio = {'nome':'Thiago', 'idade': 39, 'profissao': 'Estudante'}
print(meu_dicio)

print(meu_dicio['nome'])

print(meu_dicio.get('nome'))

# mostrar as chaves do dicionario
print(meu_dicio.keys())

# mostrar os valores do dicionario
print(meu_dicio.values())

# remover item do dicionario
meu_dicio.pop('profissao')
print(meu_dicio)

# limpar dicionario
meu_dicio.clear()
print(meu_dicio)

# Exemplo
pessoa = {
    'nome': 'Thiago',
    'idade': 39,
    'profissao': 'Estudante',
    'interesses': ['Python', 'Programacao', 'Notebooks'],
    'pet': {
        'nome': 'Loki',
        'idade': 1,
        'peso': '2kg'
    }
}

print(pessoa.get('nome'))

print(pessoa.get('interesses'))
print(pessoa['interesses'])

print(pessoa.get('interesses')[0])
print(pessoa['interesses'][0])

print(pessoa.get('pet').get('nome'))
print(pessoa['pet']['nome'])

#adicionando valor ao dicionario
pessoa['ano_nascimento'] = 1985

pessoa['cores_favoritas'] = ['Amarelo', 'Azul', 'Verde']

pessoa['mae'] = {
    'nome': "Cleusa",
    'idade': 68,
}
print(pessoa)