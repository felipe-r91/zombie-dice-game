# Estudante: Felipe Silva Rapachi
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas

# Importa módulo
import random


# Inicialização de variáveis

def intialize_dices(dice):
    """

    :param dice: inicialização da variável, deve ser 0
    :return: quantidade de dados no copo
    """
    green_dices = []
    yellow_dices = []
    red_dices = []
    for i in range(13):
        if 0 <= dice <= 2:
            red_dices.append(dice)
        elif 3 <= dice <= 6:
            yellow_dices.append(dice)
        elif 7 <= dice <= 12:
            green_dices.append(dice)
        dice += 1

    dices_cup = red_dices + yellow_dices + green_dices

    return dices_cup


# Coloca todos os dados no copo
dicesCup = intialize_dices(0)


# Define o número de jogadores
def new_player(num_players):
    """

    :param num_players: inicialização da variável, deve ser 0
    :return: número de jogadores no jogo
    """
    print("Bem vindo ao jogo Zombie Dice!!")
    print('=' * 50)
    while num_players < 2:
        try:
            num_players = int(input("Quantos jogadores vão jogar? "))
        except:
            print("Formato inválido, digite apenas números inteiros!")

        if num_players < 2:
            print("Esse jogo é para 2 ou mais jogadores")
            continue
        return num_players


# Inicialização da variável
numPlayers = new_player(0)


# Define os nomes dos jogadores
def players_name(number_of_players):
    """

    :param number_of_players: número de jogadores no jogo
    :return: lista com o nome dos jogadores
    """
    list_of_players_name = []
    unique_names = []
    while True:
        for i in range(number_of_players):
            name = str(input("Qual é o nome do " + str(i + 1) + "º jogador? "))
            list_of_players_name.append(name)
            unique_names = set(list_of_players_name)
        if len(list_of_players_name) != len(unique_names):
            print("Os jogadores não podem ter nomes iguais, defina nomes diferentes entre si!")
            list_of_players_name.clear()
            continue
        else:
            break

    return list_of_players_name


# Inicializa o nome dos jogadores
playersName = players_name(numPlayers)

gameRound = 0
playerNameIndex = 0
playerPoints = {}


# Sorteia 3 dados do copo e remove os mesmos do copo
def sort_dices(dices_cup, dice_to_replay):
    dices_drawn = []
    for i in range(3 - (len(dice_to_replay))):
        random_dice = random.choice(dices_cup)
        dices_drawn.append(random_dice)
        dices_cup.remove(random_dice)
    dices_to_be_played = dices_drawn + dice_to_replay

    return dices_to_be_played


# Passa os dados que foram sorteados
dicesTobePlayed = sort_dices(dicesCup, dice_to_replay=[])


# Sorteia a face de cada dado
def trow_dices(players_name_list, dices_to_trow, player_index, game_round):
    faces_drawn = []
    # Define os tipos de dados no jogo
    green_dice = tuple("CPCTPC")
    ylw_dice = tuple("TPCTPC")
    red_dice = tuple("TPTCPT")

    while True:
        print('=' * 50)
        if game_round == 0:
            print(players_name_list[player_index] + ", vamos começar!")
        if game_round != 0:
            print(players_name_list[player_index] + ", rodada nº: " + str(game_round + 1))
        for dice in range(len(dices_to_trow)):
            if 0 <= dices_to_trow[dice] <= 2:
                print("Você sorteou um dado Vermelho")
                random_face = random.choice(red_dice)
                faces_drawn.append(random_face)
            if 3 <= dices_to_trow[dice] <= 6:
                print("Você sorteou um dado Amarelo")
                random_face = random.choice(ylw_dice)
                faces_drawn.append(random_face)
            if 7 <= dices_to_trow[dice] <= 12:
                print("Você sorteou um dado Verde")
                random_face = random.choice(green_dice)
                faces_drawn.append(random_face)
        return faces_drawn


# Passa os parâmetros para sortear os dados
diceFace = trow_dices(playersName, dicesTobePlayed, playerNameIndex, gameRound)


# Mostra a quantidade de cada tipo de dado no copo
def show_dices_in_cup(dices_in_cup):
    red_dices_count = 0
    ylw_dices_count = 0
    grn_dices_count = 0
    for i in range(len(dices_in_cup)):
        dice = dices_in_cup[i]
        if 0 <= dice <= 2:
            red_dices_count += 1
        if 3 <= dice <= 6:
            ylw_dices_count += 1
        if 7 <= dice <= 12:
            grn_dices_count += 1
    dices_list = red_dices_count, ylw_dices_count, grn_dices_count
    print('=' * 50)
    print("Estão no copo:\n" + str(dices_list[0]) + " dados vermelhos\n"
          + str(dices_list[1]) + " dados amarelos\n" + str(dices_list[2]) + " dados verdes")


show_dices_in_cup(dicesCup)


# Analisa as faces sorteadas, soma os pontos e tiros e salva os dados a serem re-jogados.
def players_points(dice_face, dices_played, game_round):
    print('=' * 50)
    global points, bang
    dice_to_be_replayed = []
    i = 0
    if game_round == 0:
        points = 0
        bang = 0
    for dice in range(len(dice_face)):
        if dice_face[dice] == 'C':
            points += 1
            print("CÉREBRO!\nVocê comeu um Cérebro!")
        if dice_face[dice] == 'T':
            bang += 1
            print("TIRO!\nVocê levou um tiro!")
        if dice_face[dice] == 'P':
            dice_to_be_replayed.append(dices_played[i])
            print("PASSOS!\nSua vítima fugiu, rejogue o dado!")
        i += 1

    return points, bang, dice_to_be_replayed


brains, shoots, replayDice = players_points(diceFace, dicesTobePlayed, gameRound)


# Define as condições de vitória ou derrota
def victory_loose(brains_, shoots_, player_index):
    victory = False
    loose_ = False
    print('=' * 50)
    print(playersName[player_index] + f", seu nº de pontos: {brains}\n Seu nº de tiros: {shoots}")

    if 13 <= brains_:
        print(playersName[player_index] + ", Parabéns, você venceu o jogo!!!\nFim de Jogo.")
        victory = True
    if 3 <= shoots_:
        print(playersName[player_index] + ", você levou 3 tiros e perdeu!")
        loose_ = True

    return victory, loose_


win, loose = victory_loose(brains, shoots, playerNameIndex)


# Define um vencedor usando o dicionário com nomes e pontos
def define_winner(player_index):
    print(playerPoints)
    winner_ = False
    print(len(playersName))
    if player_index == len(playersName):
        print('=' * 50)
        max_score = [key for key, value in playerPoints.items() if value == max(playerPoints.values())]
        if len(max_score) == 1:
            print("Parabéns " + str(max_score) + " você foi o VENCEDOR!")
            winner_ = True
        if len(max_score) > 1 and max(playerPoints.values()) != 0:
            print("Os jogadores " + str(max_score) + " empataram!")
            winner_ = True
        if max(playerPoints.values()) == 0:
            print("Ninguém marcou pontos!")
            winner_ = True
        # Após satisfazer uma das condições acima finaliza o jogo
        print("Fim do jogo!")
    return winner_


winner = define_winner(playerNameIndex)


def keep_playing():
    play_again = str(input("Você deseja continuar jogando? s/n "))
    return play_again


while True:
    if winner:
        break
    proceed = keep_playing()
    if proceed == 's':
        if len(dicesCup) < 3:
            dicesCup = intialize_dices(0)
        gameRound += 1
        dicesTobePlayed = sort_dices(dicesCup, replayDice)
        diceFace = trow_dices(playersName, dicesTobePlayed, playerNameIndex, gameRound)
        show_dices_in_cup(dicesCup)
        brains, shoots, replayDice = players_points(diceFace, dicesTobePlayed, gameRound)
        win, loose = victory_loose(brains, shoots, playerNameIndex)
        winner = define_winner(playerNameIndex)
    if proceed == 'n':
        playerPoints[playersName[playerNameIndex]] = brains
        playerNameIndex += 1
        winner = define_winner(playerNameIndex)
        if winner:
            break
        dicesCup = intialize_dices(0)
        gameRound = 0
        dicesTobePlayed = sort_dices(dicesCup, replayDice)
        diceFace = trow_dices(playersName, dicesTobePlayed, playerNameIndex, gameRound)
        show_dices_in_cup(dicesCup)
        brains, shoots, replayDice = players_points(diceFace, dicesTobePlayed, gameRound)
        win, loose = victory_loose(brains, shoots, playerNameIndex)
        winner = define_winner(playerNameIndex)
    if loose:
        brains = 0
        playerPoints[playersName[playerNameIndex]] = brains
        playerNameIndex += 1
        winner = define_winner(playerNameIndex)
        if winner:
            break
        dicesCup = intialize_dices(0)
        gameRound = 0
        dicesTobePlayed = sort_dices(dicesCup, replayDice)
        diceFace = trow_dices(playersName, dicesTobePlayed, playerNameIndex, gameRound)
        show_dices_in_cup(dicesCup)
        brains, shoots, replayDice = players_points(diceFace, dicesTobePlayed, gameRound)
        win, loose = victory_loose(brains, shoots, playerNameIndex)
        winner = define_winner(playerNameIndex)
        continue
