def calcular_porcentagem(valor, percentual):
    if not validar_numero(valor) or not validar_numero(percentual):
        raise TypeError("Valores devem ser numericos")
    return (valor * percentual) / 100


def validar_numero(valor):
    return isinstance(valor, (int, float))

def somar(x, y):
    return x + y

# ... resto do arquivo continua igual
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Não é possível dividir"
    return x / y

print("--- Calculadora Simples ---")
print("Selecione a operação desejada:")
print("1. Somar (+)")
print("2. Subtrair (-)")
print("3. Multiplicar (*)")
print("4. Dividir (/)")

escolha = input("Digite sua escolha (1/2/3/4): ")

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
else:
    print("Opção inválida! Tente novamente")

def validar_numero(valor):
    return isinstance(valor, (int, float))


def calcular_porcentagem(valor, percentual):
    if not validar_numero(valor) or not validar_numero(percentual):
        raise TypeError("Valores devem ser numericos")
    return (valor * percentual) / 100
