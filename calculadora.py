def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Não é possível dividir por zero!"
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
    print("Opção inválida! Tente novamente.")
