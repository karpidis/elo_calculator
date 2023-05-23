from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QInputDialog,
                             QSpinBox, QComboBox, QMessageBox)
import sys
# import your Elo calculator and input checker modules
import elocalculator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Elo Calculator by Andreas Kontokanis')
        layout = QVBoxLayout()

        self.start_button = QPushButton('Tournament Elo Calculation')
        self.start_button.clicked.connect(self.start_calculation)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_calculation(self):
        self.elo_calculator = EloCalculatorApp()
        self.elo_calculator.show()


class EloCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tournament Elo Calculator')
        layout = QVBoxLayout()

        self.my_elo_edit = QSpinBox()
        self.my_elo_edit.setRange(800, 3500)  # Setting range
        self.my_elo_edit.setValue(1600)
        self.k_factor_edit = QComboBox()
        self.k_factor_edit.addItems(['10', '15', '20', '30', '40'])
        self.k_factor_edit.setCurrentText("20")

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_elo)

        layout.addWidget(QLabel('My Elo:'))
        layout.addWidget(self.my_elo_edit)

        layout.addWidget(QLabel('K Factor:'))
        layout.addWidget(self.k_factor_edit)

        self.rounds_button = QPushButton('Set Rounds')
        self.rounds_button.clicked.connect(self.set_rounds)
        layout.addWidget(self.rounds_button)

        self.setLayout(layout)

    def set_rounds(self):
        num_rounds, ok = QInputDialog.getInt(self, 'Number of Rounds', 'Enter number of rounds:')
        if ok:
            self.rounds = num_rounds
            self.opponent_elo_edits = []
            self.result_edits = []
            for i in range(self.rounds):
                opponent_elo_edit = QSpinBox()
                opponent_elo_edit.setRange(800, 3500)  # Setting range
                opponent_elo_edit.setValue(1600)  # Setting default value
                result_edit = QComboBox()
                result_edit.addItems(['0', '0.5', '1'])  # Adding options

                self.layout().addWidget(QLabel(f'Opponent Elo {i + 1}:'))
                self.layout().addWidget(opponent_elo_edit)

                self.layout().addWidget(QLabel(f'Result {i + 1}:'))
                self.layout().addWidget(result_edit)

                self.opponent_elo_edits.append(opponent_elo_edit)
                self.result_edits.append(result_edit)

            self.layout().addWidget(self.calculate_button)

    def total_elo_calculator(self, elo1: int, elo_opponents_results: list, k):
        elo_opponents_results.sort()
        beneficial_opponent = elo_opponents_results.pop(0)
        beneficial_elo = elocalculator.difr400(elo1, beneficial_opponent[0], beneficial_opponent[1], k)
        elo_list = [elocalculator.difr(elo1, elo_opponents_results[i][0], elo_opponents_results[i][1], k) for i in range(len(elo_opponents_results))]
        total_elo_difference = beneficial_elo + sum(elo_list)
        return total_elo_difference, (elo1+total_elo_difference)

    def calculate_elo(self):
        try:
            my_elo = self.my_elo_edit.value()
            k_factor = int(self.k_factor_edit.currentText())

            opponents_elo_results = []
            for i in range(self.rounds):
                opponent_elo = self.opponent_elo_edits[i].value()
                result = float(self.result_edits[i].currentText())
                opponents_elo_results.append([opponent_elo, result])

            total_elo, new_elo = self.total_elo_calculator(my_elo, opponents_elo_results, k_factor)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f"Total Elo: {total_elo}\nNew Elo: {new_elo}")
            msg.setWindowTitle("Elo calculation")
            msg.exec()
        except Exception as e:
            print(f"Exception occurred: {e}")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
