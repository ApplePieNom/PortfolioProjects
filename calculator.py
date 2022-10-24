from tkinter import *

def button_press(num):

    global equation_text

    #convert number we receive into a string
    equation_text = equation_text + str(num)

    #display it in the space
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        #eval will calculate the expression 
        total = str(eval(equation_text))

        #after adding expression, it will remain there. 
        # and can continue calculation after the total
        equation_label.set(total)
        equation_text = total

    #this is to catch error, for instance you /*-= will give this error
    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    #this is to catch error, for instance you divide a num by 0
    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

#this function clear the space
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("500x600")

#this blank display the numbers that you enter in the cal
equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

#creating all these buttons and put them in a frame
frame = Frame(window)
frame.pack()

# Button 1 to 9, button_press(number to pass in)
btns = []
btns_nmbr = -1

for x in range(0, 3):
    for y in range(0, 3):
        btns_nmbr += 1

        btns.append(Button(frame, text=1 + btns_nmbr, height=4, width=9, font=35,
                           command=lambda btns_nmbr=btns_nmbr: button_press(1 + btns_nmbr)))
        btns[btns_nmbr].grid(row=x, column=y)
        btns[btns_nmbr].config(bg="#FFF0DB")


button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)
button0.config(bg="#FFF0DB")

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)
plus.config(bg="#FFF0DB")

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)
minus.config(bg="#FFF0DB")

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)
multiply.config(bg="#FFF0DB")

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)
divide.config(bg="#FFF0DB")

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)
equal.config(bg="#FFF0DB")

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)
decimal.config(bg="#FFF0DB")

#clear button to clear the numbers
clear = Button(window, text='clear', height=2, width=8, font=10,
                 command=clear)
clear.pack()
clear.config(bg="#FFF0DB")

window.mainloop()
