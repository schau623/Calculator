from tkinter import *
import tkinter as tk

class Application (Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        
        #entry/display box
        entryBox = Entry(self, width = 50, borderwidth = 5)
        entryBox.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        
                #define functions
        def click(number):
            curr = entryBox.get()
            entryBox.delete(0, END)
            entryBox.insert(0, str(curr) + str(number))
            
        def clear():
            entryBox.delete(0, END)
            
        def add():
            firstNumber = entryBox.get()
            global math
            math = "adding"
            global first_num #Global declaration of first num so we can use it outside this function.
            first_num = int(firstNumber)
            entryBox.delete(0, END)

        def subtract():
            firstNumber = entryBox.get()
            global math
            math = "subtracting"
            global first_num #Global declaration of first num so we can use it outside this function.
            first_num = int(firstNumber)
            entryBox.delete(0, END)

        def multiply():
            firstNumber = entryBox.get()
            global math
            math = "multiplying"
            global first_num #Global declaration of first num so we can use it outside this function.
            first_num = int(firstNumber)
            entryBox.delete(0, END)

        def divide():
            firstNumber = entryBox.get()
            global math
            math = "dividing"
            global first_num #Global declaration of first num so we can use it outside this function.
            first_num = int(firstNumber)
            entryBox.delete(0, END)
            
        def equal():
            secondNumber = entryBox.get()
            entryBox.delete(0, END)
            if math == "adding":
                entryBox.insert(0, first_num + int(secondNumber))
            if math == "subtracting":
                entryBox.insert(0, first_num - int(secondNumber))
            if math == "multiplying":
                entryBox.insert(0, first_num * int(secondNumber))
            if math == "dividing":
                entryBox.insert(0, first_num / int(secondNumber))
            
            
        #define number buttons (1, 2, 3...)
        self.button_0 = Button(self, text = "0", padx = 40, pady = 20, command = lambda: click(0))
        self.button_1 = Button(self, text = "1", padx = 40, pady = 20, command = lambda: click(1))
        self.button_2 = Button(self, text = "2", padx = 40, pady = 20, command = lambda: click(2))
        self.button_3 = Button(self, text = "3", padx = 40, pady = 20, command = lambda: click(3))
        self.button_4 = Button(self, text = "4", padx = 40, pady = 20, command = lambda: click(4))
        self.button_5 = Button(self, text = "5", padx = 40, pady = 20, command = lambda: click(5))
        self.button_6 = Button(self, text = "6", padx = 40, pady = 20, command = lambda: click(6))
        self.button_7 = Button(self, text = "7", padx = 40, pady = 20, command = lambda: click(7))
        self.button_8 = Button(self, text = "8", padx = 40, pady = 20, command = lambda: click(8))
        self.button_9 = Button(self, text = "9", padx = 40, pady = 20, command = lambda: click(9))
        self.button_add = Button(self, text = "+", padx = 39, pady = 20, command = add)
        self.button_subtract = Button(self, text = "-", padx = 41, pady = 20, command = subtract)
        self.button_multiply = Button(self, text = "x", padx = 40, pady = 20, command = multiply)
        self.button_divide = Button(self, text = "÷", padx = 41 , pady = 20, command = divide)
        self.button_equal = Button(self, text = "=", padx = 91, pady = 20, command = equal)
        self.button_clear = Button(self, text = "CLEAR", padx = 79, pady = 20, command = clear)
        #number button placements
        self.button_1.grid(row = 3, column = 0)
        self.button_2.grid(row = 3, column = 1)
        self.button_3.grid(row = 3, column = 2)

        self.button_4.grid(row = 2, column = 0)
        self.button_5.grid(row = 2, column = 1)
        self.button_6.grid(row = 2, column = 2)

        self.button_7.grid(row = 1, column = 0)
        self.button_8.grid(row = 1, column = 1)
        self.button_9.grid(row = 1, column = 2)

        self.button_0.grid(row = 4, column = 0)
        self.button_clear.grid(row = 4, column = 1, columnspan = 2)
        self.button_add.grid(row = 5, column = 0)
        self.button_equal.grid(row = 5, column = 1 ,columnspan = 2)
        self.button_subtract.grid(row = 6, column = 0)
        self.button_multiply.grid(row = 6, column = 1)
        self.button_divide.grid(row = 6, column = 2)
        self.pack()


#execute application
root = tk.Tk()
root.title("Calculator")
app = Application(root)
root.mainloop()
