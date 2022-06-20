import elocalculator


def main():
    elo_csv = open('elo.csv', 'w+', encoding="utf-8")
    for result in [0, 0.5, 1]:
        for elo_opponent in range(1100, 1901):
            elo_points = [str(elo_opponent-1500), "|", str(format(elocalculator.difr(1500, elo_opponent, result, 20), '2f')), "\n"]
            print(elo_points)
            elo_csv.writelines(elo_points)
    elo_csv.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
