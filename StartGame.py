import tkinter as tk
from random import randrange


class NumberGuesser:
    """Number Guessing Class Framework"""
    def __init__(self):
        global buttons, secretNumber, lblLogs
        secretNumber = randrange(10)
        print(secretNumber)

        # remove all logs on init
        for lblLog in lblLogs:
            lblLog.grid_forget()
        lblLogs = []

    def add_guess(self, g):
        global buttons
        # check if guess matches secret number
        if g == secretNumber:
            lbl = tk.Label(window, text="Your guess was right. You won! :) ", fg="green")
            lbl.grid(row=4, column=0, columnspan=5)
            lblLogs.append(lbl)
            for b in buttons:
                b["state"] = tk.DISABLED
        buttons[g]["state"] = tk.DISABLED


# _______________________________________________________________________________________________________________
game = NumberGuesser
window = tk.Tk()
window.title("Guessing Game")

lblInst = tk.Label(window, text="Guess a number from 0 to 9")
lblLine1 = tk.Label(window, text="*********************************************************************")
lblLogs = tk.Label(window, text="Game Logs")
lblLine2 = tk.Label(window, text="*********************************************************************")

# create the buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda g=index: game.add_guess(g), state=tk.DISABLED)
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
        i = (row * 5) + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

# Main game logic

guess = 0
secretNumber = randrange(10)
print(secretNumber)
lblLogs = []

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
        game.__init__()
    print("Game started")


window.mainloop()

