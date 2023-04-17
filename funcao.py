# Criação de funções

# Função inicial

def saudacao():
    print('Seja Bem Vindo(a)!')
    print('É um prazer ter você conosco.')


saudacao()

# Funçao com parametros


def saudacao(nome, curso):
    print(f'Seja Bem Vindo(a),{nome}!')
    print(f'É um prazer ter você conosco no curso de {curso}.')


saudacao('Daniele', 'python')
saudacao('Maria', 'JavaScript')


# Função com parametros Default
def saudacao(nome, curso='Python'):
    print(f'Seja Bem Vindo(a),{nome}!')
    print(f'É um prazer ter você conosco no curso de {curso}.')


saudacao('Daniele')
saudacao('Maria', 'JavaScript')

# Funções com retorno


def soma(num1, num2):
    return num1 + num2


resultado = soma(5, 7)

print('O resultado da soma é', resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1+num2
    elif operacao == '-':
        return num1 - num2


resultado = calculadora(10, 20, '-')
print(resultado)
