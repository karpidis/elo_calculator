import input_checker


class Player:
    #creating a class for every chess player. It will has its name, rating, k_factor and later fide_id
    def __init__(self, name, rating, k_factor):
        self.name = name
        self.rating = rating
        self.kappa = k_factor


if __name__ == "__main__":

    player1 = Player("Andreas Kontokanis", input_checker.input_my_elo(), input_checker.input_k_factor())
    player2 = Player(input("Player name",), input_checker.input_my_elo(), input_checker.input_k_factor())
    print(player1.name)
    print(player1.rating)

    print(player2.name)
    print(player2.rating)
    print(player1)
