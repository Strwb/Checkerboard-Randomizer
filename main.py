import tkinter as tk
import random
import tkinter.messagebox

squares_showed = False
max_scroll_v = 0
colour_list = []
colour_square_list = []

class Colour_button:

    def __init__(self, colour):
        self.is_pressed = False
        self.square_colour = colour

    def press(self, event):
        global colour_list
        if self.is_pressed == True:
            self.is_pressed = False
            colour_list = self.delete_from_colour_list(colour_list, self.square_colour)
            self.a_square.config(relief = "raised")
        else:
            self.is_pressed = True
            colour_list.append(self.square_colour)
            self.a_square.config(relief = "sunken")

    def define_widget(self, container, r, c):
        global colour_square_list
        self.a_square = tk.Frame(container, width = 13, height = 13, bg = self.square_colour, borderwidth = 2, relief = "raised", padx = 1, pady = 1)
        self.a_square.grid(row = r, column = c)
        self.a_square.bind("<Button-1>", self.press)
        colour_square_list.append(self)

    def delete_from_colour_list(self, the_list, element):
        return_list = []
        for thing in the_list:
            if thing == element:
               continue
            else:
                return_list.append(thing)
        return return_list

    def reset(self):
        self.a_square.config(relief = "raised")

def show_squares(event):
    """    Prints squares and manages window size """
    global squares_showed
    global max_scroll_v
    global colour_list
    global colour_square_list
    row_position = 0
    col_position = 0

    the_button.config(relief = "raised") 

    try:
        row_limit = int(y_variable.get())
        col_limit = int(x_variable.get())
    except ValueError:
        
        tkinter.messagebox.showerror("Złe dane", "Proszę wprowadzić rozmiary jako liczby całkowite")
        return None

    if row_limit == 0 or col_limit == 0 or len(colour_list) == 0:
        reset_colour_squares(colour_square_list)
        tkinter.messagebox.showerror("Brak danych", "Proszę wprowadzić rozmiary płótna i wybrać kolory")
        return None

    square_list = checkerboard_frame.grid_slaves()
    for square in square_list:
        square.destroy()

    while row_position is not row_limit:

        tk.Frame(checkerboard_frame, width = 68, height = 68, borderwidth = 1, relief = "groove", bg = randomize_colours(colour_list)).grid(row = row_position, column = col_position)

        col_position += 1
        if col_position == col_limit:
            col_position = 0
            row_position += 1

    canvas_size = canvas_size_configure(col_limit, row_limit)
    squares_showed = True
    max_scroll_v = row_limit * 74 + 30
    checkerboard_frame.config(width = canvas_size[0], height = canvas_size[1])


def randomize_colours(a_list):
    return a_list[random.randint(0, len(a_list) - 1)]
    
def on_frame_configure(canvas):
    top_canvas.configure(scrollregion = top_canvas.bbox("all"))

def roll_wheel(event):

    if squares_showed == True and max_scroll_v >= top_canvas.winfo_height():
        top_canvas.yview_scroll(-1 * (event.delta // 120), "units")
    else:
        return None

def canvas_size_configure(col_limit, row_limit):
    canvas_width = 0
    canvas_height = 0

    if col_limit < 6:
        canvas_width = 402
    elif col_limit <= 10:
        canvas_width = col_limit * 70
    else:
        canvas_width = 2000
    
    if row_limit <= 10:
        canvas_height = row_limit * 70 + 30
    else:
        canvas_height = 748
    return (canvas_width, canvas_height)

def reset_colour_squares(square_list):
    
    for element in square_list:
        element.reset()
 
root = tk.Tk()
root.title("Program dla Werci")
root.bind("<Return>", show_squares)
root.bind_all("<MouseWheel>", roll_wheel)

# icon_white = tk.PhotoImage(file = "Magnus_W_icon.png") # imports white image
# icon_black = tk.PhotoImage(file = "Magnus_B_icon.png") # imorts black image
x_variable = tk.StringVar()
y_variable = tk.StringVar() # Text variables for both entries

top_canvas = tk.Canvas(root, borderwidth = 0, bg = "#ffffff", width = 402, height = 300)
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

checkerboard_frame = tk.Frame(top_frame)
checkerboard_frame.grid(row = 1, column = 0, sticky = tk.W)

top_buttons_frame = tk.Frame(top_frame, bg = "#ffffff")
top_buttons_frame.grid(row = 0, column = 0, sticky = tk.W)

x_label = tk.Label(top_buttons_frame, text = "X:")
x_label.grid(row = 0, column = 0, sticky = tk.W)

y_label = tk.Label(top_buttons_frame, text = "Y:")
y_label.grid(row = 0, column = 2, sticky = tk.W)

x_entry = tk.Entry(top_buttons_frame, textvariable = x_variable)
x_entry.grid(row = 0, column = 1, sticky = tk.W)

y_entry = tk.Entry(top_buttons_frame, textvariable = y_variable)
y_entry.grid(row = 0, column = 3, sticky = tk.W)

the_button_frame = tk.Frame(top_buttons_frame, width = 50, height = 34)
the_button_frame.pack_propagate(0)
the_button_frame.grid(row = 0, column = 4, sticky = tk.E)

colours_frame = tk.Frame(top_buttons_frame, bg = "#ffffff", width = 68, height = 34, padx = 10)
colours_frame.pack_propagate(0)
colours_frame.grid(row = 0, column = 5)

colour_white = Colour_button("white")
colour_red = Colour_button("red")
colour_yellow = Colour_button("yellow")
colour_purple = Colour_button("purple")
colour_black = Colour_button("black")
colour_green = Colour_button("green")
colour_blue = Colour_button("blue")
colour_orange = Colour_button("orange")

colour_white.define_widget(colours_frame, 0, 0)
colour_red.define_widget(colours_frame, 0, 1)
colour_yellow.define_widget(colours_frame, 0, 2)
colour_purple.define_widget(colours_frame, 0, 3)
colour_black.define_widget(colours_frame, 1, 0)
colour_green.define_widget(colours_frame, 1, 1)
colour_blue.define_widget(colours_frame, 1, 2)
colour_orange.define_widget(colours_frame, 1, 3)

the_button = tk.Button(the_button_frame, text = "Losuj")
the_button.bind("<Button-1>", show_squares)
the_button.pack(expand = 1, fill = tk.BOTH)

x_entry.focus()


root.mainloop()