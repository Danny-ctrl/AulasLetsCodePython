
# para essa variavel dentro de uma determinada  faixa (de 10) valores(0-9) execute
"""for variavel in range(10):
    print(variavel)"""

"""for variavel2 in range(1, 10):
    print(variavel2)"""


"""for variavel3 in range(1, 12, 3):
    print(variavel3)"""

soma = 0
for i in range(1, 4):
    nota = float(input(f'Informe a sua nota{i}:'))

    soma = soma + nota

print(soma/3)
