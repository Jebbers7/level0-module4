"""
Use boolean variables to control program logic between two different code
paths.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    weekend = True
    if weekend == True:
        messagebox.showinfo("Day", "It's the weekend!")
    else:
        messagebox.showinfo("Day", "It's not a weekend")
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passed = False
    if passed:
        messagebox.showinfo("Score", "You passed!")
    else:
        messagebox.showinfo("Score", "You failed")
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    game = True
    if game:
        messagebox.showinfo("Game", "Game is over!")
    else:
        messagebox.showinfo("Game", "Game is not over!")
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    red = True
    square = True
    carlos = turtle.Turtle()
    if red and square:
        for i in range(4):
            carlos.forward(100)
            carlos.right(90)
    pass
