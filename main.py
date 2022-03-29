# Estudante: Felipe Silva Rapachi
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas

# Importa módulo
import random

# Define os tipos de dados no jogo
greenDice = tuple("CPCTPC")
ylwDice = tuple("TPCTPC")
redDice = tuple("TPTCPT")

# Inicialização de variáveis
numPlayers, brains, shoots, runners, playerIndex, nameError = 0, 0, 0, 0, 0, 0
proceed, nextPlayer = "n", "n"
playersName = []
redDices = [0, 1, 2]
yellowDices = [3, 4, 5, 6]
greenDices = [7, 8, 9, 10, 11, 12]
dicesCup = [*greenDices, *yellowDices, *redDices]
diceDrawn = []
playerPoints = {}

print("Bem vindo ao jogo Zombie Dice!")

# Inicia o jogo e compara se o número de jogadores é válido
while numPlayers < 2 or nameError == 1:
    try:
        numPlayers = int(input("Quantos jogadores vão jogar? "))
    except:
        print("Valor inválido, digite apenas números inteiros")
    if numPlayers < 2:
        print("Esse jogo é para 2 ou mais jogadores")

# Cria uma lista perguntando o nome dos jogadores e verifica os nomes
while True:
    if nameError == 1:
        playersName.clear()
    for i in range(numPlayers):
        name = str(input("Qual é o nome do " + str(i + 1) + "° jogador? "))
        playersName.append(name)
    if len(playersName) == numPlayers:
        if len(set(playersName)) == len(playersName):
            nameError = 0
        else:
            nameError = 1
    if nameError == 1:
        print("Os jogadores não podem ter nomes iguais, defina nomes diferentes entre si!")
    if nameError == 1:
        continue
    else:
        break

while proceed == "n" and playerIndex == 0:
    proceed = str(input(playersName[playerIndex] + " , vamos começar?  s/n "))

# Loop infinito das rodadas do jogo, sorteia os dados, e armazena as variáveis
while True:
    nextPlayer = "n"
    for _ in range(3):
        randomDice = random.choice(dicesCup)
        dicesCup.remove(randomDice)
        diceDrawn.append(randomDice)

        if 0 <= randomDice <= 2:
            print(playersName[playerIndex] + " Você sorteou um dado Vermelho")
            randomDiceFace = random.choice(redDice)
        elif 3 <= randomDice <= 6:
            print(playersName[playerIndex] + " Você sorteou um dado Amarelo")
            randomDiceFace = random.choice(ylwDice)
        else:
            print(playersName[playerIndex] + " Você sorteou um dado Verde")
            randomDiceFace = random.choice(greenDice)
        if randomDiceFace == "T":
            print("Tiro!!")
            print("Você levou um tiro")
            shoots += 1
        elif randomDiceFace == "C":
            print("Cerébro!!")
            print("Você comeu um cérebro")
            brains += 1
        elif randomDiceFace == "P":
            print("Passos")
            print("Sua vítima escapou")
            runners += 1

    # Exibe a pontuação e os tiros contabilizados, se o jogador levar mais de 3 tiros ele perde a vez
    print(playersName[playerIndex] + f", seu número de pontos: {brains} \nNúmero de tiros: {shoots} nessa rodada")
    print("Os dados no copo são:" + str(dicesCup))
    if brains == 13:
        print("Parabéns " + playersName[playerIndex] + " você fez 13 pontos e venceu o jogo!")
    if shoots >= 3:
        print(playersName[playerIndex] + ", você levou 3 tiros e perdeu!")
        brains = 0
    else:
        # Pergunta ao jogador se quer continuar o jogo
        proceed = str(input(playersName[playerIndex] + ", você deseja continuar jogando? s/n "))
        if proceed == "s":
            if len(dicesCup) < 3:
                dicesCup = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            continue
    # Redefine as variáveis para o próximo jogador
    if proceed == "n" or shoots >= 3:
        playerPoints[playersName[playerIndex]] = brains
        playerIndex += 1
        dicesCup = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        diceDrawn.clear()
        shoots, brains, runners = 0, 0, 0
        # Após todos terem jogado verifica se há um vencedor, empate ou se ninguém marcou pontos
        if playerIndex == len(playersName):
            maxScore = [key for key, value in playerPoints.items() if value == max(playerPoints.values())]
            if len(maxScore) == 1:
                print("Parabéns " + str(maxScore) + " você foi o VENCEDOR!")
            if len(maxScore) > 1 and max(playerPoints.values()) != 0:
                print("Os jogadores " + str(maxScore) + " empataram!")
            if max(playerPoints.values()) == 0:
                print("Ninguém marcou pontos!")
            # Após satisfazer uma das condições acima finaliza o jogo
            print("Fim do jogo!")
            break
        # SENÃO Chama o próximo jogador
        else:
            while nextPlayer == "n":
                nextPlayer = input(playersName[playerIndex] + ", é sua vez. Vamos lá? s/n ")
        if nextPlayer == "s":
            continue
