import turtle

ALLIGNEMNT = "center"
FONT = ("Courier", 30, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(10)
        self.penup()
        self.goto(-100, 280)
        self.color('white')

    def show_score(self, snake_lenght):
        self.clear()
        self.write(f'Score: {snake_lenght - 3}', False, align=ALLIGNEMNT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALLIGNEMNT, font=FONT)
