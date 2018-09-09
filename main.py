import tkinter as tk
import random
import tkinter.messagebox

squares_showed = False
max_scroll_v = 0

def show_squares(event):
    """    Prints squares and manages window size """
    global squares_showed
    global max_scroll_v
    row_position = 0
    col_position = 0
   
    try:
        row_limit = int(y_variable.get())
        col_limit = int(x_variable.get())
    except ValueError:
        tkinter.messagebox.showerror("Złe dane", "Proszę wprowadzić rozmiary jako liczby całkowite")
        return None

    if row_limit == 0 or col_limit == 0:
        return None

    square_list = checkerboard_frame.grid_slaves()
    for square in square_list:
        square.destroy()

    while row_position is not row_limit:
        colour_num = random.randint(0, 1)

        if colour_num == 0:
            colour_icon = icon_white
        else:
            colour_icon = icon_black

        tk.Label(checkerboard_frame, width = 70, height = 70, image = colour_icon).grid(row = row_position, column = col_position)

        col_position += 1
        if col_position == col_limit:
            col_position = 0
            row_position += 1


    if col_limit <= 10:
        canvas_width = col_limit * 74
    else:
        canvas_width = 740

    if row_limit <= 10:
        canvas_height = row_limit * 74 + 30
    else:
        canvas_height = 770
    
    squares_showed = True
    max_scroll_v = row_limit * 74 + 30



    # if canvas_height

    top_canvas.configure(width = canvas_width, height = canvas_height)

def on_frame_configure(canvas):
    top_canvas.configure(scrollregion = top_canvas.bbox("all"))

def roll_wheel(event):

    if squares_showed == True and max_scroll_v >= top_canvas.winfo_height():
        top_canvas.yview_scroll(-1 * (event.delta // 120), "units")
    else:
        return None


root = tk.Tk()
root.title("Program dla Werci")
root.bind("<Return>", show_squares)
root.bind_all("<MouseWheel>", roll_wheel)

icon_white = tk.PhotoImage(file = "Magnus_W_icon.png") # imports white image
icon_black = tk.PhotoImage(file = "Magnus_B_icon.png") # imorts black image
x_variable = tk.StringVar()
y_variable = tk.StringVar() # Text variables for both entries

top_canvas = tk.Canvas(root, borderwidth = 0, bg = "#ffffff")
top_frame = tk.Frame(top_canvas, bg = "#ffffff")
vsb = tk.Scrollbar(root, orient = "vertical", command = top_canvas.yview) # vertical scroll bar
hsb = tk.Scrollbar(root, orient = "horizontal", command = top_canvas.xview) # horizontal scroll bar
top_canvas.configure(yscrollcommand = vsb.set) 
top_canvas.configure(xscrollcommand = hsb.set) # <- and ^ sets up both scroll bars

vsb.pack(side = tk.RIGHT, fill = tk.Y)
hsb.pack(side = tk.BOTTOM, fill = tk.X)
top_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand= True)
top_canvas.create_window((4, 4), window = top_frame, anchor = "nw")
# ^ Sets up scroll bars and canvases

top_frame.bind("<Configure>", lambda event, canvas = top_canvas: on_frame_configure(top_canvas)) # don't know what it does yet


buttons_frame = tk.Frame(top_frame, bg = "#ffffff")
buttons_frame.grid(row = 0, column = 0, sticky = tk.W)

x_label = tk.Label(buttons_frame, text = "X:")
x_label.grid(row = 0, column = 0, sticky = tk.W)

y_label = tk.Label(buttons_frame, text = "Y:")
y_label.grid(row = 0, column = 2, sticky = tk.W)

x_entry = tk.Entry(buttons_frame, textvariable = x_variable)
x_entry.grid(row = 0, column = 1, sticky = tk.W)

y_entry = tk.Entry(buttons_frame, textvariable = y_variable)
y_entry.grid(row = 0, column = 3, sticky = tk.W)

button_frame = tk.Frame(buttons_frame, width = 50, height = 30)
button_frame.pack_propagate(0)
button_frame.grid(row = 0, column = 4, sticky = tk.E)

the_button = tk.Button(button_frame, text = "Losuj")
the_button.bind("<Button-1>", show_squares)
the_button.pack(expand = 1, fill = tk.BOTH)

checkerboard_frame = tk.Frame(top_frame)
checkerboard_frame.grid(row = 1, column = 0, sticky = tk.W)



x_entry.focus()

root.mainloop()
