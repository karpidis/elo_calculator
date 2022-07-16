import input_checker
import json
import pandas as pd
import elocalculator


def import_json_players_group():
    """This imports a players json file"""
    file = open("player_group.json", "r")

    content = file.read()

    player_group = json.loads(content)
    file.close()
    return player_group


def create_name_list(players_group):
    """creates a list of names from json list of dictionaries"""
    name_list = []
    for player in players_group:
        name_list.append(player['name'])
    return name_list


def get_rank(name_list, player_group):
    game_rank = input_checker.input_rank(name_list)
    player_ranking = [{game_rank.get(d["name"]): d} for d in player_group]
    return player_ranking


def get_rank_dict(players_group):
    game_rank_dict = input_checker.input_rank_dict(players_group)
    return game_rank_dict


def dict_to_pandas(python_dict):
    panda_df = pd.DataFrame(python_dict)
    panda_df = panda_df.sort_values('rank')
    return panda_df


def calculate_equivalent_result(rank, number_of_players):
    """
    rank: int
    number_of_players: int
    return:int
    It calculates based on the rank in a n-player game what is the euivalent number of wins/losses
    >>> calculate_equivalent_result(2, 4)
    1
    >>> calculate_equivalent_result(4, 4)
    -3
    >>> calculate_equivalent_result(4, 8)
    1
    >>> calculate_equivalent_result(4, 6)
    -1
    >>> calculate_equivalent_result(11,18)
    -3
    >>> calculate_equivalent_result(5, 9)
    0
    """
    return number_of_players-2*rank+1


def elocalc_df(players_dataframe, k):
    length = len(players_dataframe)
    elo_dif = []

    for rank in range(1, length+1):
        player1 = players_dataframe.loc[players_dataframe["rank"] == rank]
        other_players = players_dataframe.loc[players_dataframe["rank"] != rank]
        player1elo = player1['rating'].iloc[0]
        player1rank = player1['rank'].iloc[0]
        elo_difference = 0
        for i in range(len(other_players)):
            opponent_elo = other_players['rating'].iloc[i]
            opponent_elo_rank = other_players['rank'].iloc[i]
            if player1rank < opponent_elo_rank:
                elo_difference += elocalculator.difr(player1elo, opponent_elo, 1, k)
            elif player1rank == opponent_elo_rank:
                elo_difference += elocalculator.difr(player1elo, opponent_elo, 0.5, k)
            else:
                elo_difference += elocalculator.difr(player1elo, opponent_elo, 0, k)

        elo_dif.append(elo_difference)

    players_dataframe.insert(3, 'Elo Difference', elo_dif)
    players_dataframe['old rating'] = players_dataframe.rating
    players_dataframe["rating"] = players_dataframe.rating + round(players_dataframe['Elo Difference'])
    return players_dataframe


def create_name_rank_df(panda_dataframe):
    return panda_dataframe.iloc[:, [0, 1]]


def export_pd_json(panda_dataframe):
    panda_dataframe.to_json("player_group.json", indent = 4, orient =  'records')
    return


def main():
    players = import_json_players_group()
#   name_list = create_name_list(players)
#   rank_list_rating = get_rank(name_list, players)   dictionary in format {rank:{'name': , 'rating': }
    players_dict = get_rank_dict(players)  # dictionary in format {name = ,rating = , rank = }
    players_panda = dict_to_pandas(players_dict)
#    player_1 = players_panda.loc[players_panda["rank"] == 1]
#   other_players = players_panda.loc[players_panda["rank"] != 1]

    elocalc_df(players_panda)


if __name__ == '__main__':
    main()
