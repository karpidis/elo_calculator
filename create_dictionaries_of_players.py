import input_checker
import json

file = open("player_group.json", "r")

content = file.read()

player_group = json.loads(content)
name_list = []

for player in player_group:
    name_list.append(player['name'])

game_rank = input_checker.input_rank(name_list)
print(game_rank.get("Vangelis Prineas"))
print(player_group)
player_ranking = [{d["name"]:[d["rating"], game_rank.get(d["name"])]} for d in player_group]
print(player_ranking)
file.close()
