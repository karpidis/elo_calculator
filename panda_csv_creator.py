import pandas as pd




table_pd = [[0, 0.5], [3, 0.5], [10, 0.51], [17, 0.52], [25, 0.53], [32, 0.54], [39, 0.55], [46, 0.56],
            [53, 0.57], [61, 0.58], [68, 0.59], [76, 0.6], [83, 0.61], [91, 0.62], [98, 0.63], [106, 0.64],
            [113, 0.65], [121, 0.66], [129, 0.67], [137, 0.68], [145, 0.69], [153, 0.7], [162, 0.71], [170, 0.72],
            [179, 0.73], [188, 0.74], [197, 0.75], [206, 0.76], [215, 0.77], [225, 0.78], [235, 0.79], [245, 0.8],
            [256, 0.81], [267, 0.82], [278, 0.83], [290, 0.84], [302, 0.85], [315, 0.86], [328, 0.87], [344, 0.88],
            [357, 0.89], [374, 0.9], [391, 0.91], [411, 0.92]]

elo_difference_table = pd.DataFrame(table_pd)
elo_difference_table.to_csv('elo_difference_table.csv', index=False)
