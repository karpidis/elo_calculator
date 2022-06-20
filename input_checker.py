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


def input_result():
    result = input("what is the result", )
    result = check_result(result)
    return result


def main():
    return input_my_elo(), input_opponent_elo(), input_result(), input_k_factor()


if __name__ == '__main__':
    main()
