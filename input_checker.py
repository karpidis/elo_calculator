def check_elo(elo):
    try:
        valuate_elo = int(elo)
        if valuate_elo not in range(500, 4000):
            print("Not valid rating is not right")
            input_my_elo()
        else:
            return valuate_elo
    except ValueError:
        print('Not valid format of the rating')
        input_my_elo()


def check_rank(rank, list_of_players):
    try:
        valuate_rank = int(rank)
        while valuate_rank not in range(1, len(list_of_players) + 1):
            print("Not a valid rank")
            break
        else:
            return valuate_rank
    except ValueError:
        print("Not a valid format of rank")


def check_result(result):
    try:
        valuate_result = float(result)
        if valuate_result == 0 or valuate_result == 0.5 or valuate_result == 1:
            return valuate_result
        else:
            print("You didn't give a valid result")
            input_result()
    except ValueError:
        print("Not valid format of the result")
        input_result()


def check_rounds(rounds):
    try:
        valuate_rounds = int(rounds)
        if valuate_rounds >= 0:
            return valuate_rounds
        else:
            print("You didn't give a valid number of rounds")
            input_rounds()
    except ValueError:
        print("Not valid format of rounds")
        input_rounds()


def check_k(kappa):
    try:
        valuatek = int(kappa)
        if valuatek not in [10, 20, 40]:
            print("You didn't give a valid K-factor")
            input_k_factor()
        else:
            return valuatek
    except ValueError:
        print('Not valid format of K-factor')
        input_k_factor()


def input_my_elo():
    my_rating = input("What is your rating?\t", )
    my_rating = check_elo(my_rating)
    return my_rating


def input_opponent_elo():
    opponent_rating = input("What is your opponent's rating?\t", )
    opponent_rating = check_elo(opponent_rating)
    return opponent_rating


def input_k_factor():
    k_factor = input("Which is your K\t", )
    k_factor = check_k(k_factor)
    return k_factor


def input_rank(list_of_players: list):
    names_rank = {}
    for name in list_of_players:
        rank = None
        while rank is None:
            rank = input("What is the rank of " + name + "\t", )
            rank = check_rank(rank, list_of_players)
        else:
            names_rank[name] = rank
    print(names_rank)
    return names_rank


def input_result():
    result = input("what is the result", )
    result = check_result(result)
    return result


def input_rounds():
    rounds = input('How many rounds was the tournament')
    rounds = check_rounds(rounds)
    return rounds


def main():
    return input_my_elo(), input_opponent_elo(), input_result(), input_k_factor()


if __name__ == '__main__':
    main()
