#Exercícios 1 e 2
def numeros():
    num = int(input("Informe um valor para n: " ))
    for num in range(1, num + 1):
        for a in range(1, num + 1):
            print(a, end="   ")
        print()

    num = str(num)
    print("-" * 40)
    print("A quantidade de dígitos do número informado é: ",len(num))

numeros()
#Exercício 3
def divisao():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

    except ZeroDivisionError:
        print("A divisão falhou, pois um dos números informados é 0")
    except ValueError:
        print("O cálculo falhou, pois um dos números informados não é válido")
    finally:
        print(num1/num2)
        
divisao()