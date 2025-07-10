from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.goto(-220, 190)
        self.score = 0

        self.heart_count = 4
        self.hearts = Turtle()
        self.hearts.color('red')
        self.hearts.pu()
        self.hearts.ht()
        self.hearts.goto(220, 177)

        self.game_over = Turtle()
        self.game_over.color('white')
        self.game_over.pu()
        self.game_over.ht()
        self.game_over.goto(0, -40)
        self.is_game_over = False

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.hearts.clear()
        if self.score > 9999:
            self.score = 9999
            self.game_over.write('YOU WIN!', align="center", font=("Lucida Console", 50, "bold"))
            self.is_game_over = True
        elif self.heart_count == 0:
            self.game_over.write('YOU LOSE!', align='center', font=("Lucida Console", 50, "bold"))
            self.is_game_over = True
            self.score = -9999
        self.update_hearts()
        self.write(self.score, align="left", font=("Lucida Console", 35, "bold"))

    def increase_score(self, score):
        self.score += score
        self.update_scoreboard()

    def update_hearts(self):
        hearts = ''
        for h in ['❤' for _ in range(self.heart_count)]:
            hearts += h
        self.hearts.write(hearts, align='right', font=("Arial", 50, "normal"))

    def decrease_hearts(self):
        self.heart_count -= 1
        self.update_scoreboard()