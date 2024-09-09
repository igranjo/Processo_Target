word = str(input("Qual palavra deseja investigar? "))
counter = 0
for letter in word: # Itera por cada caracter da String 
    if letter.lower() == "a": # O uso do método lower simplifica a condicional para verificar se a letra A está presente e sua quantidade
        counter += 1
if counter == 0:
    print("A letra a não existe, seja maiúscula ou minúscula")
else:
    print(f"A letra a, seja minúscula ou maiúscula, apareceu {counter} vezes")
