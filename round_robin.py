from input_checker import input_number_of_players


def pairing_every_round(number_of_round, players_list):
    """This makes the pairing of colours in a list of players. It needs a moved list to make different pairing """
    number_of_players = len(players_list)
    pairing_list = ""
    if number_of_round % 2 == 1:
        for table in range(int(number_of_players / 2)):
            board_table = str(table + 1) + ". " + players_list[table] + " - " + players_list[
                number_of_players - 1 - table] + "\t"
            pairing_list += board_table
    else:
        board_table = "1. " + players_list[number_of_players - 1] + " - " + players_list[0] + "\t"
        pairing_list += board_table
        for table in range(1, int(number_of_players / 2)):
            board_table = str(table + 1) + ". " + players_list[table] + " - " + players_list[
                number_of_players - 1 - table] + "\t"
            pairing_list += board_table

    return pairing_list


def create_anonymous_list():
    number_of_players = input_number_of_players()
    if number_of_players % 2 == 1:
        number_of_players += 1
        print("Max number is the bye of the round")
    return [str(x) for x in range(1, number_of_players + 1)]


def create_moved_list(list_of_players):
    number_of_players = len(list_of_players)
    half_list_len = int(number_of_players/2)

    first_player = list_of_players.pop(len(list_of_players)-1)

    list_of_players.extend(x for x in list_of_players[0:half_list_len])
    list_of_players[0:half_list_len-1] = list_of_players[half_list_len:number_of_players-1]

    del list_of_players[half_list_len-1:number_of_players-1]

    list_of_players.append(first_player)

    return list_of_players


def create_all_pairings(player_list):
    pairings = ""
    round1_pairing = "Rd 1: " + pairing_every_round(1, player_list) + "\n"
    pairings += round1_pairing
    for gyros in range(2, len(player_list)):
        player_list = create_moved_list(player_list)
        round_pairing = "Rd " + str(gyros) + ": " + pairing_every_round(gyros, player_list) + "\n"
        pairings += round_pairing
    return pairings


def main():
    players_list = create_anonymous_list()
    print(create_all_pairings(players_list))


main()
