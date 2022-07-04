import elocalculator


def main():
    elo_csv_creator()


def elo_csv_creator():
    elo_csv = open('elo.csv', 'w+', encoding="utf-8")
    for elo_opponent in range(1100, 1901):
        elo_points = [str(elo_opponent-1500), "|", str(format(elocalculator.difr(1500, elo_opponent, 0, 20), '2f')),
                      "|", str(format(elocalculator.difr(1500, elo_opponent, 0.5, 20), '2f')),
                      "|", str(format(elocalculator.difr(1500, elo_opponent, 1, 20), '2f')), "\n"]
        print(elo_points)
        elo_csv.writelines(elo_points)
    elo_csv.close()


if __name__ == '__main__':
    main()
