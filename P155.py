from tkinter import *
import random
root = Tk()
root.title('P155')
root.geometry('600x600')


dictionary = {'Colors':'Pink,Blue,Green,Red,Brown,Orange,Yellow,Purple,Black,White'}

def stuff():
    randomNum = random.randint(len(dictionary))
    dictionary['Colors'][randomNum]
    print(colorIndex)
    root.configure(background = colorIndex)
    
btn = Button(root,title='click me',command=stuff)
btn.place(relx = 0.5,rely = 0.5,anchor=CENTER)


root.mainloop()
