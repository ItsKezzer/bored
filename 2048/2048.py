## Dependencies
import os, art, pick, random, getch


## Initialisation
title = art.text2art("2048", font="rnd-medium")

## Functions
def menu():
    _, index = pick.pick(["Play", "Help", "Exit"], title + art.text2art("Menu", font="small"), indicator="->", default_index=0)
    if index == 0:
        game = Game()
        game.play()
    elif index == 1:
        helper()

def helper():
    print("Use the arrow keys to move the tiles. When two tiles with the same number touch, they merge into one!")
    print("Press any key to continue...")
    input()
    menu()

## Class

class Game:
    def __init__(self):
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1024], [0, 0, 0, 1024]]
        self.score = 0
        self.game_over = False
        self.infinite = False

    def play(self):
        while not self.game_over:
            self.add()
            self.display()
            self.process(self.move())
            self.check()
        exit(0)

    def display(self):
        os.system("clear")
        print(title)
        print(art.text2art(str(self.score), font="medium"))
        print("+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "+")
        for row in self.board:
            print("|", end="")
            for col in row:
                print(f" {col:7d} |", end="")
            print()
            print("+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "+")

    def add(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while self.board[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.board[row][col] = 2

    def move(self):
        direction = getch.getch()
        if ord(direction) == 27:
            getch.getch()
            direction = getch.getch()
            if ord(direction) == 65:                                           # [[0, 0, 0, 0],
                return "up"                                                     # [0, 0, 0, 0],
            elif ord(direction) == 66:                                          # [0, 0, 0, 0],
                return "down"                                                   # [0, 0, 0, 0]]
            elif ord(direction) == 67:
                return "right"
            elif ord(direction) == 68:
                return "left"
            else:
                exit(0)
        return self.move()

    def process(self, direction):
        if direction == "down":
            for row in range(3):
                for col in range(4):
                    if self.board[row][col] != 0 and self.board[row + 1][col] == 0:
                        self.board[row + 1][col] = self.board[row][col]
                        self.board[row][col] = 0
                    elif self.board[row][col] != 0 and self.board[row + 1][col] == self.board[row][col]:
                        self.board[row + 1][col] *= 2
                        self.board[row][col] = 0
                        self.score += self.board[row + 1][col]
        elif direction == "up":
            for row in range(3, 0, -1):
                for col in range(4):
                    if self.board[row][col] != 0 and self.board[row - 1][col] == 0:
                        self.board[row - 1][col] = self.board[row][col]
                        self.board[row][col] = 0
                    elif self.board[row][col] != 0 and self.board[row - 1][col] == self.board[row][col]:
                        self.board[row - 1][col] *= 2
                        self.board[row][col] = 0
                        self.score += self.board[row - 1][col]
        elif direction == "right":
            for row in range(4):
                for col in range(3):
                    if self.board[row][col] != 0 and self.board[row][col + 1] == 0:
                        self.board[row][col + 1] = self.board[row][col]
                        self.board[row][col] = 0
                    elif self.board[row][col] != 0 and self.board[row][col + 1] == self.board[row][col]:
                        self.board[row][col + 1] *= 2
                        self.board[row][col] = 0
                        self.score += self.board[row][col + 1]
        elif direction == "left":
            for row in range(4):
                for col in range(3, 0, -1):
                    if self.board[row][col] != 0 and self.board[row][col - 1] == 0:
                        self.board[row][col - 1] = self.board[row][col]
                        self.board[row][col] = 0
                    elif self.board[row][col] != 0 and self.board[row][col - 1] == self.board[row][col]:
                        self.board[row][col - 1] *= 2
                        self.board[row][col] = 0
                        self.score += self.board[row][col - 1]

    def check(self):
        # Win
        if not self.infinite:
            for row in self.board:
                for col in row:
                    if col == 2048:
                        self.over(win=True)
        # Game over
        for row in self.board:
            for col in row:
                if col == 0:
                    return
        self.over(win=False)

    def over(self, win=False):
        if win:
            _, index = pick.pick(["Keep Playing", "Restart", "Exit"], title + art.text2art("Well Played !", font="medium"), indicator="->", default_index=0)
            if index == 0:
                self.infinite = True
                return
        else:
            _, index = pick.pick(["Restart", "Exit"], title + art.text2art("Game Over", font="small"), indicator="->", default_index=0)
            index += 1
        if index == 1:
            self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            self.score = 0
        else:
            self.game_over = True
        

## Main
menu()