import elocalculator
import input_checker


def get_opponents_elo_results():
    number_of_rounds = input_checker.input_rounds()
    elo_result_list = [[input_checker.input_opponent_elo(), input_checker.input_result()] for i in range(number_of_rounds)]
    return elo_result_list


def total_elo_calculator(elo1: int, elo_opponents_results: list, k):
    elo_list = [elocalculator.difr(elo1, elo_opponents_results[gyros][0], elo_opponents_results[gyros][1], k) for gyros in range(len(elo_opponents_results))]
    return sum(elo_list),(elo1+sum(elo_list))


def main():
    total_elo = total_elo_calculator(input_checker.input_my_elo(), get_opponents_elo_results(), input_checker.input_k_factor())
    print(total_elo)


if __name__ == '__main__':
    main()
