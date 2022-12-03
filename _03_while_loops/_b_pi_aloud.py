"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = "3.1415926535897932384"
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    for i in range(3):
        print(pi[i])
    # TODO) Use a while loop to keep asking for the next digit of pi
    correct = True
    counter = 3
    while correct:
        answer = simpledialog.askstring("Pi", "What is the next digit of pi?")
        if answer == pi[counter]:
            print("correct")
            counter += 1
        else:
            print("incorrect")
            correct = False
    messagebox.showinfo("Pi", "You recited " + str(counter) + " digits of pi in a row!")
        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop
    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
