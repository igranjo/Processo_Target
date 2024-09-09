while True: #Bloco para prevenção de entradas incorretas por parte do usuário. Por opção, resolvi aceitar apenas números inteiros para verificar se faz parte da sequência
    try:
        number = int(input("Por favor, insira o número inteiro positivo que gostaria de verificar se faz parte da sequência de Fibonacci: "))
    except ValueError:
        print("Entrada inválida")
        continue
    if number >=0:
        break
    else:
        print("Entrada inválida")


previous_2 = 1 # Definição do segundo termo da série.
previous_1 = 0 # Definição do primeiro termo da série.
while True:
    if number == previous_1 or number == previous_2:
        print("O número faz parte da sequência de Fibonacci")
        break
    soma = previous_2 + previous_1 # Determinação do próximo elemento da sequência.
    previous_1 = previous_2
    previous_2 = soma #Nas duas linhas passadas, ocorre o deslocamento dos números para que a próxima iteração possa determinar o próximo elemento.
    if number == soma:
        print("O número faz parte da sequência de Fibonacci")
        break
    else:
        if soma > number: # Neste caso, é uma condição de parada para que o algoritmo não busque infinitamente por um número que já passou e é menor do que os próximos.
            print("O número não faz parte da sequência de Fibonacci")
            break