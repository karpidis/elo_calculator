# Import necessary components from PyQt6.QtWidgets
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QSpinBox, QComboBox, QMessageBox, QInputDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
import sys

# Import your Elo calculator module
import elocalculator


# Main application window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('Elo Calculator by Andreas Kontokanis')

        # Create a QVBoxLayout which is a type of layout in Qt that arranges widgets vertically
        layout = QVBoxLayout()

        # Create a button to start the tournament Elo calculation
        self.start_button = QPushButton('Tournament Elo Calculation')

        # Connect the button click to the start_calculation function
        self.start_button.clicked.connect(self.start_calculation)

        # Add button to the layout
        layout.addWidget(self.start_button)

        # Set the layout to the main window
        self.setLayout(layout)

    # Function to show the EloCalculatorApp when button is clicked
    def start_calculation(self):
        self.elo_calculator = EloCalculatorApp()
        self.elo_calculator.show()


# Window for Elo calculation
class EloCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set window title
        self.setWindowTitle('Tournament Elo Calculator')

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a spinbox for user to input their Elo rating
        self.my_elo_edit = QSpinBox()
        self.my_elo_edit.setRange(800, 3500)  # Set range of the spinbox
        self.my_elo_edit.setValue(1600)  # Set default value

        # Create a combobox for user to select the K factor
        self.k_factor_edit = QComboBox()
        self.k_factor_edit.addItems(['10', '15', '20', '30', '40'])  # Add options
        self.k_factor_edit.setCurrentText("20")  # Set default value

        # Create a calculate button
        self.calculate_button = QPushButton('Calculate')

        # Connect the button click to the calculate_elo function
        self.calculate_button.clicked.connect(self.calculate_elo)

        # Add widgets to the layout
        layout.addWidget(QLabel('My Elo:'))
        layout.addWidget(self.my_elo_edit)
        layout.addWidget(QLabel('K Factor:'))
        layout.addWidget(self.k_factor_edit)

        # Create a button for setting the number of rounds
        self.rounds_button = QPushButton('Set Rounds')

        # Connect the button click to the set_rounds function
        self.rounds_button.clicked.connect(self.set_rounds)
        layout.addWidget(self.rounds_button)

        # Set the layout to the window
        self.setLayout(layout)

    # Function to set the number of rounds and add corresponding widgets for opponent Elo and result
    def set_rounds(self):
        num_rounds, ok = QInputDialog.getInt(self, 'Number of Rounds', 'Enter number of rounds:')
        if ok:
            self.rounds = num_rounds
            self.opponent_elo_edits = []
            self.result_edits = []

            # For each round, add spinbox for opponent Elo and combobox for result
            for i in range(self.rounds):
                opponent_elo_edit = QSpinBox()
                opponent_elo_edit.setRange(800, 3500)  # Set range of the spinbox
                opponent_elo_edit.setValue(1600)  # Set default value
                result_edit = QComboBox()
                result_edit.addItems(['0', '0.5', '1'])  # Add options

                self.layout().addWidget(QLabel(f'Opponent Elo {i + 1}:'))
                self.layout().addWidget(opponent_elo_edit)
                self.layout().addWidget(QLabel(f'Result {i + 1}:'))
                self.layout().addWidget(result_edit)

                # Append the widgets to their respective lists for later retrieval
                self.opponent_elo_edits.append(opponent_elo_edit)
                self.result_edits.append(result_edit)

            # Add the calculate button to the layout
            self.layout().addWidget(self.calculate_button)

    # Function to calculate the total Elo and new Elo
    def total_elo_calculator(self, elo1: int, elo_opponents_results: list, k):
        # Sort the list of opponent Elo and result pairs
        elo_opponents_results.sort()

        # Pop the first element in the list which is the opponent Elo and result pair that gives the maximum Elo gain
        beneficial_opponent = elo_opponents_results.pop(0)

        # Calculate the Elo gain from the most beneficial opponent
        beneficial_elo = elocalculator.difr400(elo1, beneficial_opponent[0], beneficial_opponent[1], k)

        # Calculate the Elo gain from the rest of the opponents
        elo_list = [elocalculator.difr(elo1, elo_opponents_results[i][0], elo_opponents_results[i][1], k) for i in
                    range(len(elo_opponents_results))]

        # Calculate the total Elo gain and new Elo
        total_elo_difference = beneficial_elo + sum(elo_list)
        return total_elo_difference, (elo1 + total_elo_difference)

    # Function to calculate Elo when calculate button is clicked
    def calculate_elo(self):
        try:
            # Get user's Elo and K factor
            my_elo = self.my_elo_edit.value()
            k_factor = int(self.k_factor_edit.currentText())

            # Initialize list to store opponent Elo and result pairs
            opponents_elo_results = []

            # For each round, get opponent Elo and result and add to the list
            for i in range(self.rounds):
                opponent_elo = self.opponent_elo_edits[i].value()
                result = float(self.result_edits[i].currentText())
                opponents_elo_results.append([opponent_elo, result])

            # Calculate total Elo and new Elo
            total_elo, new_elo = self.total_elo_calculator(my_elo, opponents_elo_results, k_factor)

            # Show a message box with the calculated total Elo and new Elo
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f"Total Elo: {total_elo}\nNew Elo: {new_elo}")
            msg.setWindowTitle("Elo calculation")
            msg.exec()
        except Exception as e:
            # Print any exceptions that occur
            print(f"Exception occurred: {e}")


# Function to run the application
def main():
    # Create a QApplication
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Execute the application and exit
    sys.exit(app.exec())


# Entry point of the script
if __name__ == "__main__":
    main()
