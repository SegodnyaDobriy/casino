from random import randint


def greetings(games):  # приветствие
    print("Добро пожаловать в Bogdan's Casino!")
    print('У нас вы можете поиграть в различные игры, вот полный список:')
    print(*games.keys(), sep='\n')  # вывод всех существующих игр


def get_games():  # список всех игр
    games = {'1': blackjack, '123': 1}
    return games


def choice_game(games):  # выбор игры
    print('Выберите игру, в которую хотите поиграть:')
    user_choice = input()  # ввод названия игры
    return games[user_choice]  # возвращаю выбранную игру


def get_croupier_name():  # выбор крупье
    croupiers = ('Пудж', 'Моргенштерн')  # список всех крупье
    return croupiers[randint(0, len(croupiers) - 1)]  # выбирается рандомный из всех


def blackjack(croupier):  # геймплей блэкджека
    print('Вы выбрали игру "Black Jack".\nВашим крупье назначен:', croupier + '.')

    hands = starting_set_of_cards()  # стартовые руки из 2-х карт
    result_hands = get_other_cards(croupier, hands)  # руки после добора игрока

    player_hand, croupier_hand, cards_pool = result_hands

    score = sum_cards_values(player_hand, croupier_hand, croupier)  # ценность рук

    winner(score, croupier)     # определение победителя


def starting_set_of_cards():  # стартовая рука у игроков(по 2 карты каждому из колоды, в которой 52 карты)

    player_hand = []
    croupier_hand = []

    cards_pool = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3',
                  '4',
                  '5', '6',
                  '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q',
                  'Q',
                  'K', 'K',
                  'K', 'K', 'A', 'A', 'A', 'A']

    for _ in range(2):  # выдача карт
        player_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))
        croupier_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))

    return player_hand, croupier_hand, cards_pool


def get_other_cards(croupier, hands):  # добор карт для игрока(в будущем и для крупье)
    player_hand, croupier_hand, cards_pool = hands

    while True:     # выдаём карты игроку

        print('В вашей руке:', *player_hand, )
        print('В руке', croupier + 'а:', croupier_hand[0], '*')

        print('Ещё карту?')

        user_input = input()

        if user_input == '+':  # если соглашается, то игроку дают ещё одну карту и идёт пересчёт суммы очков
            player_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))
        elif user_input == '-':
            break

    return player_hand, croupier_hand, cards_pool


def sum_cards_values(player_cards, croupier_cards, croupier_name):  # подсчёт ценности карт

    cards_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A': (11, 1)}  # ценность карт

    player_hand_value = 0
    croupier_hand_value = 0

    for card in player_cards:  # если у игрока >= 21 очков, то туз даёт 1 очко, иначе 11

        if player_hand_value < 21 and card == 'A':
            player_hand_value += cards_values[card][0]
        elif player_hand_value >= 21 and card == 'A':
            player_hand_value += cards_values[card][1]
        else:
            player_hand_value += cards_values[card]

    for card in croupier_cards:
        if card == 'A':  # сумма 2-х карт в руке у крупье не может превышать 21 очко, поэтому туз даёт всегда 11 очков
            croupier_hand_value += cards_values[card][0]
        else:
            croupier_hand_value += cards_values[card]

    print('Всркываемся...')
    print('В вашей руке:', *player_cards, '    Сумма очков:', player_hand_value )
    print('В руке', croupier_name + 'а:', *croupier_cards, '    Сумма очков:', croupier_hand_value)

    return player_hand_value, croupier_hand_value


def winner(players_score, croupier):    # определяем победителя

    player_score, croupier_score = players_score

    if player_score == 21 and croupier_score != 21:     # блэкджек у игрока
        print('Black Jack, Вы выиграли!')
    elif player_score == 21 and croupier_score != 21:     # блэкджек у крупье
        print('Black Jack, ' + croupier + ' выиграл!')
    elif 21 - player_score < 21 - croupier_score:
        print('Вы выиграли!')
    elif player_score == croupier_score:
        print('Ничья.')
    elif 21 - player_score > 21 - croupier_score:
        print(croupier, 'выиграл!')


def main():
    croupier = get_croupier_name()
    games = get_games()

    greetings(games)
    user_choice = choice_game(games)

    if user_choice == blackjack:
        blackjack(croupier)


if __name__ == '__main__':
    main()
