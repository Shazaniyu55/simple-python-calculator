#i am importing the python tkinter gui libary
#for this project i am building a calculator app
from tkinter import *



#i created a function called frame for later use in my code
#this function has 2 parameter a root and side
def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w



#i also created a button function that will later be use a components it has 4 arguments
def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#i created a class calculator that will automate the entire application structure
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('simple calculator')
        self.master.iconname("calc")

        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)


        for key in ("123", "456", "789", "-0 ."):
            keyF = frame(self,  TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w = display,  s=' %s '%char: w.set(w.get()+s))

        opsF = frame(self, TOP)
        for char  in "+-*/=":
            if char == "=":
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>',lambda e, s=self, w=display: s.calc(w), '+')
            else:
                 btn = button(opsF, LEFT, char,lambda w=display, c=char: w.set(w.get()+' '+c+' '))




        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))


    def calc(self, display):
        try: 
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")







if __name__ == '__main__':
  Calculator().mainloop()
# window = Tk()
# window.geometry("300x300")
# window.title("calculator app")
# # label = Label(window, text="ADNET", fg="white", bg="blue", relief="solid", font=("arial"))
# # label.pack(fill=BOTH, pady=2, padx=2, expand=True)

# label = Label(window, text="ADNET", fg="white", bg="blue", relief="solid", font=("arial"), height=5)
# label.pack(fill=BOTH, pady=2, padx=2,)



# window.mainloop()