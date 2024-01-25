from turtle import Turtle

ALINGMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.teleport(0, 270)
        self.increase_score()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALINGMENT, font=FONT)



