from Tkinter import *

class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.result = StringVar()
        self.expression = StringVar()
        self.grid()
        # self.pack(side=LEFT)
        print "Result: " + str(self.result.get())
        print "Expression: " + str(self.expression.get())
        self.create_layout()
        self.create_display()
        self.create_buttons()

    def create_layout(self):
        self.displayexpressionrow = Frame(self, relief=GROOVE, bg='grey')
        self.displayexpressionrow.grid()
        # self.displayresultrow = Frame(self, relief=GROOVE, bg='grey')
        # self.displayresultrow.grid()
        self.buttonsrow = Frame(self)
        self.buttonsrow.grid()
        self.button_column1 = Frame(self.buttonsrow)
        self.button_column1.pack(side=LEFT)

        self.button_column2 = Frame(self.buttonsrow)
        self.button_column2.pack(side=LEFT)

        self.number_row1 = Frame(self.button_column1)
        self.number_row1.grid()
        self.number_row2 = Frame(self.button_column1)
        self.number_row2.grid()
        self.number_row3 = Frame(self.button_column1)
        self.number_row3.grid()
        self.number_row4 = Frame(self.button_column1)
        self.number_row4.grid()

        self.operator_row1 = Frame(self.button_column2)
        self.operator_row1.grid()
        self.operator_row2 = Frame(self.button_column2)
        self.operator_row2.grid()
        self.operator_row3 = Frame(self.button_column2)
        self.operator_row3.grid()
        self.operator_row4 = Frame(self.button_column2)
        self.operator_row4.grid()
        self.operator_row5 = Frame(self.button_column2)
        self.operator_row5.grid()

    def create_display(self):
        self.display_calculation = Label(self.displayexpressionrow, text='Calculation: ', textvariable=self.expression)
        self.display_calculation.grid()
        # self.display_result = Label(self.displayresultrow, text='Result: ', textvariable=self.result)
        # self.display_result.grid()

    def create_buttons(self):
        self.create_numbers()
        self.create_operators()

    def create_operators(self):
        self.add = Button(self.operator_row4, text='+', command=lambda: self.update_display('+'))
        self.add.pack(side=LEFT)
        self.subtract = Button(self.operator_row3, text='-', command=lambda: self.update_display('-'))
        self.subtract.pack(side=LEFT)
        self.multiply = Button(self.operator_row2, text='x', command=lambda: self.update_display('*'))
        self.multiply.pack(side=LEFT)
        self.divide = Button(self.operator_row1, text='/', command=lambda: self.update_display('/'))
        self.divide.pack(side=LEFT)
        self.equals = Button(self.operator_row5, text='=', command=self.calculate_result)
        self.equals.pack(side=LEFT)


    def create_numbers(self):
        self.one = Button(self.number_row3, text="1", fg="red", command=lambda: self.update_display(1)) #, command=self.update_display(1)
        self.one.pack(side=LEFT)
        self.two = Button(self.number_row3, text="2", fg="red", command=lambda: self.update_display(2)) #, command=lambda: self.update_display(2)
        self.two.pack(side=LEFT)

        self.three = Button(self.number_row3, text="3", fg="red", command=lambda: self.update_display(3)) #, command=lambda: self.update_display(3)
        self.three.pack(side=LEFT)

        self.four = Button(self.number_row2, text="4", fg="red", command=lambda: self.update_display(4)) #, command=lambda: self.update_display(4)
        self.four.pack(side=LEFT)

        self.five = Button(self.number_row2, text="5", fg="red", command=lambda: self.update_display(5)) #, command=lambda: self.update_display(5)
        self.five.pack(side=LEFT)

        self.six = Button(self.number_row2, text="6", fg="red", command=lambda: self.update_display(6)) #, command=lambda: self.update_display(6)
        self.six.pack(side=LEFT)

        self.seven = Button(self.number_row1, text="7", fg="red", command=lambda: self.update_display(7)) #, command=lambda: self.update_display(7)
        self.seven.pack(side=LEFT)

        self.eight = Button(self.number_row1, text="8", fg="red", command=lambda: self.update_display(8)) #, command=lambda: self.update_display(8)
        self.eight.pack(side=LEFT)

        self.nine = Button(self.number_row1, text="9", fg="red", command=lambda: self.update_display(9)) #, command=lambda: self.update_display(9)
        self.nine.pack(side=LEFT)

        self.clear_button = Button(self.number_row4, text="C", fg="red", command=self.clear_display)  # , command=lambda: self.update_display(0)
        self.clear_button.pack(side=LEFT)

        self.zero = Button(self.number_row4, text="0", fg="red", command=lambda: self.update_display(0)) #, command=self.update_display(0)
        self.zero.pack(side=LEFT)

        self.decimal_point = Button(self.number_row4, text=".", fg="red", command=lambda: self.update_display('.'))  # , command=self.update_display(0)
        self.decimal_point.pack(side=LEFT)

    def update_display(self, input):
        expression = self.expression.get()

        # if not expression:
        #     expression += str(input)
        # else:
        expression += str(input) if not self.do_not_update(expression, input) else ''
        self.expression.set(expression)

    def do_not_update(self, expression, input):
        result = ((str(input) in '/*+-0' and not expression) or len(expression) > 10)
        if not result:
            result = ((str(input) in '0-+/*' and expression[-1] in '/+*-') or expression == 'Error')


        return result

    def clear_display(self):
        # self.result.set('')
        self.expression.set('')

    def calculate_result(self):
        expression = self.expression.get()
        try:
            result = str(eval(expression))
        except:
            result = 'Error'
        if len(result) > 13:
            return
        else:
            self.expression.set(result) if expression else None

root = Tk()

app = App(root)

root.mainloop()
root.destroy()

