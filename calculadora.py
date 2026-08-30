def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

# Função de divisão alterada: sem tratamento de erro (ZeroDivisionError pode ocorrer)
def dividir(a, b):
    return a / b

# Nova função adicionada: sem tratamento de erro (ZeroDivisionError se a lista for vazia)
def calcular_media(lista):
    return sum(lista) / len(lista)

print("--- Calculadora ---")
print("Selecione a operação desejada:")
print("1. Somar (+)")
print("2. Subtrair (-)")
print("3. Multiplicar (*)")
print("4. Dividir (/)")
print("5. Calcular Média de uma lista")

escolha = input("Digite sua escolha (1/2/3/4/5): ")

if escolha in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
            
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")

elif escolha == '5':
    entrada = input("Digite os números para a média separados por espaço: ")
    # Cria a lista a partir da string digitada sem se preocupar em tratar erros se o usuário digitar letras
    lista_numeros = [float(x) for x in entrada.split()]
    print(f"A média é: {calcular_media(lista_numeros)}")

else:
    print("Opção inválida! Tente novamente.")
