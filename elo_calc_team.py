import create_dictionaries_of_players
import input_checker as ic


def main():
    players = create_dictionaries_of_players.import_json_players_group()
    players_dict = create_dictionaries_of_players.get_rank_dict(players)  # dictionary in format {name = ,rating = , rank = }
    players_panda = create_dictionaries_of_players.dict_to_pandas(players_dict)
    group_players_rating = create_dictionaries_of_players.elocalc_df(players_panda, ic.input_k_factor())
    print(group_players_rating)
    new_group_players = create_dictionaries_of_players.create_name_rank_df(group_players_rating)
    create_dictionaries_of_players.export_pd_json(new_group_players)


if __name__ == '__main__':
    main()
