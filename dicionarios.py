# Dicionários

# Criando dicionarios

dicionario = {}
dicionario = dict()
dicionario = {'nome': 'Daniele', 'idade': 26, 'altura': 1.64}
print(dicionario)
print(dicionario['altura'])

# Adicionando elementos a um dicionario

dicionario['programador'] = True
print(dicionario)
dicionario['altura'] = 2
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existencia de uma chave

print('peso' in dicionario)
print('nome' in dicionario)
