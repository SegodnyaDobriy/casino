from random import randint


def greetings(games):  # приветствие
    print("Добро пожаловать в Bogdan's Casino!")
    print('У нас вы можете поиграть в различные игры, вот полный список:')
    print(*games.keys(), sep='\n')  # вывод всех существующих игр


def get_games():  # список всех игр
    games = {'1': blackjack, '123': 1}
    return games


def get_croupier_name():  # выбор крупье
    croupiers = ('Пудж', 'Моргенштерн')  # список всех крупье
    return croupiers[randint(0, len(croupiers) - 1)]  # выбирается рандомный из всех


def choice_game():  # выбор игры
    print('Выберите игру, в которую хотите поиграть:')
    user_choice = input()  # ввод названия игры
    return user_choice


def start_game(games, user_choice):
    croupier = get_croupier_name()  # получаем нашего крупье
    print('Вы выбрали игру "Black Jack".\nВашим крупье назначен:', croupier + '.')
    return games[user_choice]()  # вызываем выбранную игру


def sum_cards_values(croupier, hands):
    player_hand, croupier_hand, cards_pool = hands

    cards_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A': (11, 1)}  # ценность карт

    while True:
        player_hand_value = 0
        croupier_hand_value = 0

        for card in player_hand:  # если у игрока >= 21 очков, то туз даёт 1 очко, иначе 11

            if player_hand_value < 21 and card == 'A':
                player_hand_value += cards_values[card][0]
            elif player_hand_value >= 21 and card == 'A':
                player_hand_value += cards_values[card][1]
            else:
                player_hand_value += cards_values[card]

        if croupier_hand[0] == 'A':  # у крупье видна только одна карта, поэтому туз даёт всегда 11 очков
            croupier_hand_value += 11
        else:
            croupier_hand_value += cards_values[croupier_hand[0]]

        print('В вашей руке:', *player_hand, '    Сумма очков:', player_hand_value)
        print('В руке у', croupier + 'а:', croupier_hand[0], '*', '    Сумма очков:', croupier_hand[0])

        print('Ещё карту?')

        user_input = input()

        if user_input == '+':  # если соглашается, то игроку дают ещё одну карту и идёт пересчёт суммы
            player_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))
        elif user_input == '-':
            break


def players_hands():  # игроку и крупье выдаются по 2 карты из колоды, в которой 52 карты

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


def blackjack():
    pass


def main():
    croupier = get_croupier_name()
    games = get_games()

    greetings(games)
    start_game(games, choice_game())
    sum_cards_values(croupier, players_hands())


if __name__ == '__main__':
    main()
