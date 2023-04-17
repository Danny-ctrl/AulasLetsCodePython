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


# Métodos de listas
lista = [1, 2, 3, 12, 8, 56]

# append (adiciona elemento no final)
print('Antes do append: ', lista)
lista.append(26)
print('Depois do append: ', lista)

# insert (adiciona o elemento escolhendo a posição)
lista.insert(2, 38)
print('Depois do insert: ', lista)

# extend (juntar duas listas)
lista2 = [6, 8, 7]
lista.extend(lista2)

print('Depois do extend: ', lista)

# pop (remover elemento especificando ou o ultimo elemento)
lista.pop()
print('lista após o pop: ', lista)

lista.pop(0)
print('lista após o pop0: ', lista)

# remove (informe o valor que quer retirar(o primeiro caso tenha equivalentes))

lista.remove(12)
print('lista após o remove: ', lista)

# count (contar o elemento da lista)
print('Quantidade de 3 na lista: ', lista.count(3))

# index (diz o indice de um determinado elemento na lista)
print('Indice do elemento 3 na lista: ', lista.index(3))

# sort(ordenar lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# Funções para listas

# len (quantos elementos a lista tem)
print(len(lista))
# sum(soma de todos os elementos de listas)
print(sum(lista))
# max (maior valor)
print('Maior elemento da lista', max(lista))
# min (menor valor)
print('Menor elemento da lista', min(lista))
