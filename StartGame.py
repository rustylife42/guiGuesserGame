import tkinter as tk
from random import randrange


class NumberGuesser:
    """Number Guessing Class Framework"""
    def __init__(self):
        self.guessed_list = []

    def add_guess(self, guess):
        self.guessed_list.append(guess)


MAX = 10


# _______________________________________________________________________________________________________________

window = tk.Tk()
window.title("Guessing Game")

lblInst = tk.Label(window, text="Guess a number from 0 to 9")
lblLine1 = tk.Label(window, text="*********************************************************************")
lblLogs = tk.Label(window, text="Game Logs")
lblLine2 = tk.Label(window, text="*********************************************************************")

# create the buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index: process(index), state=tk.DISABLED)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Game", command=lambda: start_game(index))
    btnStartGameList.append(btnStartGame)

# append elements to grid
lblInst.grid(row=0, column=0, columnspan=5)
lblLine1.grid(row=1, column=0, columnspan=5)
lblLogs.grid(row=2, column=0, columnspan=5)  # row 2 - 6 is reserved for showing logs

lblLine2.grid(row=7, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

# Main game logic

guess = 0
secretNumber = randrange(10)
print(secretNumber)
lblLogs = []
guess_row = 4

# reset all variables
def init():
    global buttons, guess, secretNumber, lblLogs, guess_row
    guess = 0
    secretNumber = randrange(10)
    print(secretNumber)
    guess_row = 4

    # remove all logs on init
    for lblLog in lblLogs:
        lblLog.grid_forget()
    lblLogs = []


def process(g):
    global buttons, guess_row
    # check if guess matches secret number
    if g == secretNumber:
        lbl = tk.Label(window, text="Your guess was right. You won! :) ", fg="green")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1
        for b in buttons:
            b["state"] = tk.DISABLED
    buttons[i]["state"] = tk.DISABLED


status = "none"


def start_game(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Restart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


window.mainloop()

