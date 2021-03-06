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


def pool_of_cards():  # 1 колода - 52 карты
    cards_pool = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3',
                  '4',
                  '5', '6',
                  '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q',
                  'Q',
                  'K', 'K',
                  'K', 'K', 'A', 'A', 'A', 'A']

    return cards_pool


def cards_coast():  # ценность карт
    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
             'A': (11, 1)}

    return cards


def get_cards_for_players(player_name_hand, cards_pool, num_of_cards=1):  # выдача N-го кол-ва карт одному игроку
    for _ in range(num_of_cards):
        player_name_hand.append(cards_pool.pop(randint(0, len(cards_pool) - 1)))

    return player_name_hand


def player_sum(player_cards, cards_values):  # сумма очков игрока после взятия доп. карты

    player_hand_value = 0

    for card in player_cards:  # если у игрока >= 21 очков, то туз даёт 1 очко, иначе 11

        if player_hand_value < 21 and card == 'A':
            player_hand_value += cards_values[card][0]
        elif player_hand_value >= 21 and card == 'A':
            player_hand_value += cards_values[card][1]
        else:
            player_hand_value += cards_values[card]

    return player_hand_value


def blackjack(croupier_name):  # геймплей блэкджека

    print('Вы выбрали игру "Black Jack".\nВашим крупье назначен:', croupier_name + '.')

    player_hand = []  # карты игрока
    croupier_hand = []  # карты крупье

    for _ in range(2):  # выдача первых 2-х карт каждому игроку
        get_cards_for_players(player_hand, pool_of_cards())
        get_cards_for_players(croupier_hand, pool_of_cards())

    start_winner = check_start_winner(player_hand, croupier_hand, croupier_name,
                                      cards_coast())  # проверка на блэкджек со старта

    if start_winner is True:  # если у игрока блекджек со старта и нет 10/11 у крупье - игрок выиграл
        return print('Black Jack, Вы выиграли х3 очков!')

    elif start_winner == '+':   # игрок рискнул на х3 выигрыш

        if player_sum(croupier_hand, cards_coast()) == 21:
            print('Black Jack у обоих игроков, ничья, ставки возвращаются.')
        else:
            print('Black Jack, Вы выиграли х3 очков!')

    elif start_winner == '-':   # игрок выбрал х1 выигрыш
        print('Black Jack, вы выбрали забрать х1 выигрыш.')

    while True:

        if card_question(player_hand, croupier_hand, croupier_name):  # если игрок согласен
            get_cards_for_players(player_hand, pool_of_cards())  # то ему выдаётся карта
        else:
            break

        pl_s = player_sum(player_hand, cards_coast())  # считается сумма очков игрока
        cr_s = player_sum(croupier_hand, cards_coast())  # считается сумма очков крупье

        if pl_s > 21:  # если сумма очков игрока больше 21, то он проигрывает
            print('В вашей руке:', *player_hand, '    Сумма очков:', pl_s)
            print('В руке', croupier_name + 'а:', *croupier_hand, '    Сумма очков:', cr_s)
            return print('У вас больше 21-го очка, Вы проиграли!')

    player_value = player_sum(player_hand, cards_coast())  # считается итоговая сумма очков игрока
    croupier_value = player_sum(croupier_hand, cards_coast())  # считается итоговая сумма очков крупье

    print('В вашей руке:', *player_hand, '    Сумма очков:', player_value)
    print('В руке', croupier_name + 'а:', *croupier_hand, '    Сумма очков:', croupier_value)

    return winner(player_value, croupier_value, croupier_name)


def check_start_winner(player_cards, croupier_cards, croupier_name,
                       cards_values):  # проверка на блекджек у игрока со старта

    player_hand_value = player_sum(player_cards, cards_values)

    if player_hand_value == 21 and cards_values[croupier_cards[0]] != 10 and cards_values[croupier_cards[0]] != 11:
        print('В вашей руке:', *player_cards, )
        print('В руке', croupier_name + 'а:', croupier_cards[0], '*')
        return True     # блэкджек у игрока, первая карта у крупье не 10/11

    elif player_hand_value == 21 and cards_values[croupier_cards[0]] == 10 or cards_values[
        croupier_cards[0]] == 11:  # если первая карт крупье 10/11 очков, то блэкджек может быть и у него
        print('В вашей руке:', *player_cards)
        print('В руке', croupier_name + 'а:', croupier_cards[0], '*')
        print('В руке у крупье лежит потенциальный Black Jack, рискнёте выиграть х3, или же остановитесь на х1?')

        player_choice = input()

        if player_choice == '+':    # выбор игрока - рискннуть на х3
            return '+'
        elif player_choice == '-':  # выбор игрока - забрать х1
            return '-'


def card_question(player_hand, croupier_hand, croupier_name):
    print('В вашей руке:', *player_hand, )
    print('В руке', croupier_name + 'а:', croupier_hand[0], '*')
    print('Ещё карту?')

    user_input = input()

    if user_input == '+':  # если соглашается, то игроку дают ещё одну карту
        return 1
    elif user_input == '-':
        return 0


def winner(player_score, croupier_score, croupier_name):  # определяем победителя

    if player_score == 21 and croupier_score != 21:  # блэкджек у игрока
        print('Black Jack, Вы выиграли!')
    elif player_score == 21 and croupier_score != 21:  # блэкджек у крупье
        print('Black Jack, ' + croupier_name + ' выиграл!')
    elif 21 - player_score < 21 - croupier_score:   # выигрыш игрока
        print('Вы выиграли!')
    elif player_score == croupier_score:    # ничья
        print('Ничья.')
    elif 21 - player_score > 21 - croupier_score:   # выигрыш крупье
        print(croupier_name, 'выиграл!')


def main():
    croupier_name = get_croupier_name()
    games = get_games()
    greetings(games)
    user_choice = choice_game(games)

    if user_choice == blackjack:
        blackjack(croupier_name)


if __name__ == '__main__':
    main()
