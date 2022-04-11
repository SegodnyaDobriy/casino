from random import randint


def greetings(games):  # приветствие
    print("Добро пожаловать в Bogdan's Casino!")
    print('У нас вы можете поиграть в различные игры, вот полный список:')
    print(*games.keys(), sep='\n')  # вывод всех существующих игр


def get_games():  # список всех игр
    games = {'1': blackjack, '123': 1}
    return games


def get_croupier_name():  # выбор крупье
    croupiers = ('Пудж', 'Ильяс', 'Моргенштерн')  # список всех крупье
    return croupiers[randint(0, len(croupiers) - 1)]  # выбирается рандомный из всех


def choice_game():  # выбор игры
    print('Выберите игру, в которую хотите поиграть:')
    user_choice = input()  # ввод названия игры
    return user_choice


def start_game(games, user_choice):
    croupier = get_croupier_name()   # получаем нашего крупье
    print('Вы выбрали игру "Black Jack".\nВашим крупье назначен:', croupier + '.')
    return games[user_choice](get_croupier_name())   # вызываем выбранную игру


def blackjack(croupier):
    player_hand = []
    croupier_hand = []

    cards_pool = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7,
                  8,
                  9, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']

    for _ in range(2):
        player_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))
        croupier_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))

    cards_values = {'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}
    pass










def main():
    games = get_games()

    greetings(games)
    start_game(games, choice_game())


if __name__ == '__main__':
    main()
