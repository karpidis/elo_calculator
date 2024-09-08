from flask import Flask, render_template, request
from elocalculator import difr400  # Make sure the import points to your difr400 function

app = Flask(__name__)

# Define the Elo rating calculation route
@app.route('/')
def main():
    return render_template("app.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    try:
        # Get form inputs and convert to appropriate types
        my_elo = int(request.form['my_elo'])
        opponents_elo = int(request.form['opponents_elo'])
        result = float(request.form['result'])  # Win = 1, Draw = 0.5, Loss = 0
        k = int(request.form['k'])  # K-factor

        # Perform the Elo rating calculation
        new_elo = my_elo + difr400(my_elo, opponents_elo, result, k)

        # Return the result to the template
        return render_template('app.html', new_elo=new_elo)

    except ValueError:
        # If there's a problem with input conversion, return an error message
        return render_template('app.html', error="Invalid input")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
