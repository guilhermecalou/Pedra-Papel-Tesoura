import random
odds = ["Pedra", "Papel", "Tesoura"]
pickBot = random.choice(odds)
pick = input("Enter your value: ")
print(pickBot)
if pickBot == "Pedra":
    if pick == "Pedra":
        print("Empate! Jogue novamente.")
    elif pick == "Tesoura":
        print("Maquina ganhou!")
    elif pick == "Papel":
        print("Jogador venceu!")
elif pickBot == "Tesoura":
    if pick == "Pedra":
        print("Jogador ganhou!")
    elif pick == "Tesoura":
        print("Empate!")
    elif pick == "Papel":
        print("IA ganhou!")
elif pickBot == "Papel":
    if pick == "Pedra":
        print("Robozao ganhou")
    elif pick == "Papel":
        print("Empatou!")
    elif pick == "Tesoura":
        print("Jogador ganhou ihul!")
    
    