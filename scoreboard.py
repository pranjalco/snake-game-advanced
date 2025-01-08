from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = None
        self.fetch_high_score_data()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """It resets score to 0 and update the high score in file."""
        self.update_high_score_data()
        self.score = 0
        self.fetch_high_score_data()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """It increases the score by 1."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def fetch_high_score_data(self):
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
            # print(self.high_score)

    def update_high_score_data(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(f"{self.score}")
