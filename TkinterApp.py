from tkinter import *

root = Tk()
# Label(tk, text = 'Hello World').peak()
root.title('Event Test')
root.geometry('640x400+20+20')

def callback():
    print('Event 발생')

button = Button(root, text = 'Click', width = 20, command = callback)
button.pack(padx = 10, pady = 10)

root.mainloop()

