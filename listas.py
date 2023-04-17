# Listas

# Antes
nota1 = 7.9
nota22 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []  # vazia
lista = list()  # converte estrutura em lista vazia
lista = [26, 'Daniele', 1.71, False]
lista_de_lista = [10, [1, 2, 3]]

# Indexação
lista = [10, 'Daniele', 1.71, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices (fatiamento)
lista = [10, 50, 60, 40, 80, 90, 100]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

# Interações com FOR
# 1. Utilizando os proprios elementos da lista

for elemento in lista:  # para cada elemento dentro da lista percorra
    print(elemento)

    # 2. Utilizando os indices

    print('Comprimento da lista : ', len(lista))

for i in range(len(lista)):
    print(lista[i])
