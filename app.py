from flask import Flask, render_template, request
import random

app = Flask(__name__)

# A simple Sudoku generator (it doesn't generate fully random but fixed puzzles for simplicity)
def generate_sudoku():
    # A fixed Sudoku puzzle to display (9x9 grid)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    return board

@app.route('/')
def index():
    board = generate_sudoku()
    return render_template('index.html', board=board)

@app.route('/solve', methods=['POST'])
def solve():
    board = generate_sudoku()
    # Here, you could implement a Sudoku-solving algorithm, but for simplicity, we'll just send the same board back.
    # This is just a mock-up for simplicity.
    solved_board = board  # In a real app, you'd implement Sudoku-solving logic here
    return render_template('index.html', board=solved_board)

if __name__ == '__main__':
    app.run(debug=True)
