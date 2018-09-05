import tkinter as tk
import random

root = tk.Tk()
root.title("Program dla Wery")

def generate_checkerboard(event):


    row_position = 1
    col_position = 0

    while row_position != 11:

        colour = randomize_colour()
        if colour == "white":
            letter = "W"
        else:
            letter = "B"

        square = tk.Frame(main_frame, width = 50, height = 50, bg = colour)
        square.grid(row = row_position, column = col_position)

        col_position += 1

        if col_position == 10:
            col_position = 0
            row_position += 1


def randomize_colour():
    colour_num = random.randint(0, 1)
    if colour_num == 0:
        return "white"
    else:
        return "black"


button_frame = tk.Frame(root, width = 70, height = 50)
button_frame.grid(row = 0, sticky = tk.E)

randomize_button = tk.Button(button_frame, text = "Losuj")
randomize_button.pack(fill = tk.BOTH, expand = 1)
randomize_button.bind("<Button-1>", generate_checkerboard)

main_frame = tk.Frame(root, width = 500, height = 500)
main_frame.grid(row = 1)






root.mainloop()