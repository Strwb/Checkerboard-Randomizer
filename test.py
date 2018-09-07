import tkinter as tk
import random

root = tk.Tk()
root.geometry()
root.title("Dupa")

icon_white = tk.PhotoImage(file = "Magnus_W_icon.png")
icon_black = tk.PhotoImage(file = "Magnus_B_icon.png")


# def foo(event):
#    for i in range(5):
#     if i % 2 == 0:
#         im = fota
#     else:
#         im = fota2
#     tk.Label(checkerboard_frame, width = 70, height = 70, image = im).grid(row = 0, column = i) 


def show_squares(event):

    row_position = 0
    col_position = 0
    
    while row_position is not 10:

        colour_num = random.randint(0, 1)

        if colour_num == 0:
            colour_icon = icon_white
        else:
            colour_icon = icon_black

        tk.Label(checkerboard_frame, width = 70, height = 70, image = colour_icon).grid(row = row_position, column = col_position)

        col_position += 1
        if col_position == 10:
            col_position = 0
            row_position += 1





button_frame = tk.Frame(root, width = 50, height = 30)
button_frame.pack_propagate(0)
button_frame.grid(row = 0, column = 0, sticky = tk.E)

checkerboard_frame = tk.Frame(root, width = 700, height = 700)
checkerboard_frame.grid(row = 1, column = 0)

the_button = tk.Button(button_frame, text = "Losuj")
the_button.bind("<Button-1>", show_squares)
the_button.pack(expand = 1, fill = tk.BOTH)




root.mainloop()