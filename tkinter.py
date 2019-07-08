import tkinter

window = tkinter.Tk() #initializes window manager
window.title("Blank Window Lol") #renames window title
label = tkinter.Label(window, text = "Blank window lolol").pack() #label is used to insert objects into window
#pack() attribute of widget displays size

#creates top and bottom frame
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

#creates buttons
btn1 = tkinter.Button(top_frame, text = "B1", fg = "pink").pack();
#fg is foreground
#side is to align the widget
btn2 = tkinter.Button(bottom_frame, text = "B2", fg = "blue").pack(side = "left")

#creates labels
tkinter.Label(window, text = "Taking up the whole of x width", fg = "white", bg = "blue").pack(fill = "x")
tkinter.Label(window, text = "Taking up the whole of y height", fg = "white", bg = "blue").pack(side = "left", fill = "y")


window.mainloop() # display window unttil manually closed - always needs be at bottom for code to execute in window
# code sourced from https://www.datacamp.com/community/tutorials/gui-tkinter-python#tkinter
