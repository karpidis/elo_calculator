# This program calculates elo rating on a tournament for a player if we know all of his rated opponents
# Fide table for the probability of win for a higher rated opponent

# Table of conversion of difference in rating, D, into scoring probability PD
table_pd = [[0, 0.5], [3, 0.5], [10, 0.51], [17, 0.52], [25, 0.53], [32, 0.54], [39, 0.55], [46, 0.56],
            [53, 0.57], [61, 0.58], [68, 0.59], [76, 0.6], [83, 0.61], [91, 0.62], [98, 0.63], [106, 0.64],
            [113, 0.65], [121, 0.66], [129, 0.67], [137, 0.68], [145, 0.69], [153, 0.7], [162, 0.71], [170, 0.72],
            [179, 0.73], [188, 0.74], [197, 0.75], [206, 0.76], [215, 0.77], [225, 0.78], [235, 0.79], [245, 0.8],
            [256, 0.81], [267, 0.82], [278, 0.83], [290, 0.84], [302, 0.85], [315, 0.86], [328, 0.87], [344, 0.88],
            [357, 0.89], [374, 0.9], [391, 0.91], [411, 0.92]]
rows = len(table_pd)


def main():
    starting_rating = int(input("What is your rating?\t", ))
    opponent_rating = int(input("What is your opponent's rating?\t", ))
    while True:
        resulta = int(input("what is the result", ))
        if resulta == 0 or resulta == 0.5 or resulta == 1:
            break
        else:
            print("Use 0 for loss, 0.5 for draw, 1 for win")

    development_coefficient = int(input("Which is your K\t", ))

    print(difr(starting_rating, opponent_rating, resulta, development_coefficient))


def difr(elo1, elo2, result, k):
    if elo2 == 0:
        return 0
    else:
        dif = elo1 - elo2
        if abs(dif) >= 400:
            dif = 400 * (abs(dif) / dif)
        if dif >= 0:
            for i in range(rows):
                if table_pd[i][0] <= dif <= table_pd[i + 1][0]:
                    dr = k * (result - table_pd[i + 1][1])
                    return dr
        elif dif < 0:
            for i in range(rows):
                if table_pd[i][0] <= abs(dif) <= table_pd[i + 1][0]:
                    dr = k * (result - 1 + table_pd[i + 1][1])
                    return dr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
