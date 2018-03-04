from tkinter import *
import turtle
def agario():
	import turtle
	import mainMenu

widget = Button(text = 'Start', padx = 100 , pady = 20, command = agario)
widget.pack(padx = 20, pady = 300)
widget.config(bg= "dark blue", fg = 'white')
widget.config(font = ('helvetica', 15,'italic'))


widget.mainloop()

