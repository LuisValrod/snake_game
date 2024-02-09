from turtle import Turtle

ALINGMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.color('white')
        self.penup()
        self.teleport(0, 270)
        self.increase_score()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align=ALINGMENT, font=FONT)



