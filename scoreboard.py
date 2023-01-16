from turtle import Turtle
ALIGNMENT = "center"
MOVE = False
TEXT = ("Arial", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-20, 270)
        self.hideturtle()
        self.pencolor('white')
        self.score_text()

    def score_text(self):
        self.write(f"Score: {self.score} ", MOVE, ALIGNMENT, TEXT)

    def actual_score(self):
        self.clear()
        self.score += 1
        self.score_text()

    def game_over(self):
        self.goto(0, 0)
        self.color("yellow")
        self.write("GAME OVER", MOVE, ALIGNMENT, TEXT)


