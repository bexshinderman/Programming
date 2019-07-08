import tkinter

window = tkinter.Tk() #initializes window manager
window.title("Blank Window Lol") #renames window title
label = tkinter.Label(window, text = "Blank window lolol").pack(2) #label is used to insert objects into window the pack() attribute of widget displays size
window.mainloop() # display window unttil manually closed

# code sourced from https://www.datacamp.com/community/tutorials/gui-tkinter-python#tkinter
