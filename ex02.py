'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def fibonacci(num):
    lista = [0,1]
    while num >= lista[-1]:
        lista.append(lista[-1] + lista[-2])
    return lista

entrada = 34  #Insira aqui o número que deseja verificar
sequencia = fibonacci(entrada)

print("############")
if entrada in sequencia:
    print(f"O número {entrada} faz parte da Sequência de Fibonacci.")
else:
    print(f"O número {entrada} não faz parte da Sequência de Fibonacci.")
print("############")
