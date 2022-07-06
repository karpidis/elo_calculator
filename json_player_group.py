import json

player_group = [
    dict(name="Vangelis Prineas", rating=1634),
    dict(name="Pavlos Momtsos", rating=1606),
    dict(name="Martha Nikolakopoulou", rating=1582),
    dict(name="Andreas Kontokanis", rating=1578)
]

json_obj = json.dumps(player_group, indent=4)

file = open("player_group.json", "w")
file.write(json_obj)

file.close()

