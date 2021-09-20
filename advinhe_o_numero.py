from random import randrange


#Declaração de variavel

numero = randrange(1,10)
print("Escolhi um numero de 1 a 10 tente advinhar")
tentativa = int(input("Qual numero você escolhe? "))
tentativas = 0

while numero != tentativa:
    if numero >= tentativa:

        print("O numero é maior")
        tentativa = int(input("Tente novamente: "))
    elif numero <= tentativa:
        tentativas = tentativas + 1
        print("O numero é menor")
        tentativa = int(input("Tente novamente: "))

print(f"Você acertou o numero era {numero}, Parabens!")
print(f"Tentativas = {tentativas + 1}")
