from turtle import Turtle

# create the Writer class that inherits from Turtle
class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def write_on_screen(self, state, xcor, ycor):
        """This function writes the names of the correctly guessed states
        on the map."""
        self.goto(xcor, ycor)
        self.write(state, align="center", font=("Courier", 10, "normal"))

    def game_over(self):
        """This function will write the winning message in the middle of the screen in red."""
        self.goto(0, 0)
        self.color("red")
        self.write("You win! The game is over.", align="center", font=("Courier", 30, "normal"))

    def finish_game(self):
        """This functions will write the exit message in the middle of the screen in red."""
        self.goto(0, 0)
        self.color("red")
        self.write("You exited the game. Learn the missed states now!", align="center", font=("Courier", 15, "normal"))



