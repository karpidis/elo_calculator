import elocalculator
import input_checker


def get_opponents_elo_results():
    number_of_rounds = input_checker.input_rounds()
    elo_result_list = [[input_checker.input_opponent_elo(), input_checker.input_result()] for i in range(number_of_rounds)]
    return elo_result_list


def total_elo_calculator(elo1: int, elo_opponents_results: list, k):
#   here is the list of elo points earned and lost
    elo_dif_list = [elocalculator.difr400(elo1, elo_opponents_results[gyros][0], elo_opponents_results[gyros][1], k) for gyros in range(len(elo_opponents_results))]
    total_elo_difference = sum(elo_dif_list)
    return total_elo_difference, (elo1+total_elo_difference)


def main():
    total_elo = total_elo_calculator(input_checker.input_my_elo(), get_opponents_elo_results(), input_checker.input_k_factor())
    print(total_elo)


if __name__ == '__main__':
    main()
