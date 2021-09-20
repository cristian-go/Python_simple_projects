from random import randrange
n_vezes = input("Quantas vezes deseja rodar o dado? ")

for i in range(1,int(n_vezes)+1):
    sorteado = randrange(1,7)
    print(f"{i}ª Jogada saiu {sorteado}")
