from tkinter import * 
import random

def next_turn(row, column):
    global player #to have access to player in this function

    # check if the text of the button we click on is empty and when checkwinner is false,
    # we will then fill in that button with our player, aka X or O 
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # index 0 is the first player 
        # if current player equal to first player, 
        # put the text of the button as that player (x or 0)
        if player == players[0]:
            buttons[row][column]['text'] = player

            #check to see if there is winner after filling in this button
            # if no winner yet, switch to the other player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            #if there is a winnerz
            elif check_winner() is True:
                label.config(text=(players[0]+" wins!"))

            #if it ties
            elif check_winner() == "Tie":
                label.config(text="Its a Tie!")

        #else refers to if player is [1]
        else: 
            
            buttons[row][column]['text'] = player

            # if no winner yet, switch to the other player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            #if there is a winner
            elif check_winner() is True:
                label.config(text=(players[1]+" wins!"))

            #if it ties
            elif check_winner() == "Tie":
                label.config(text="Its a Tie!")

#[0,0],[0,1],[0,2]
#[1,0],[1,1],[1,2]
#[2,0],[2,1],[2,2]

def check_winner():

    #horizontal win conditions etc. [0,0],[0,1],[0,2]
    for row in range(3):
        #if all these buttons are the same and no empty space, means there is a winner
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#C1E1C1")
            buttons[row][1].config(bg="#C1E1C1")
            buttons[row][2].config(bg="#C1E1C1")
            return True

    #vertical win conditions etc. [0,0],[1,0],[2,0]
    for column in range(3):
        #if all these buttons are the same and no empty space, means there is a winner
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#C1E1C1")
            buttons[1][column].config(bg="#C1E1C1")
            buttons[2][column].config(bg="#C1E1C1")
            return True

    #diagonal winning conditions
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="#C1E1C1")
        buttons[1][1].config(bg="#C1E1C1")
        buttons[2][2].config(bg="#C1E1C1")
        return True  

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="#C1E1C1")
        buttons[1][1].config(bg="#C1E1C1")
        buttons[2][0].config(bg="#C1E1C1")
        return True   

    #check if there is any spaces remaining, if no more empty spaces and no winner means its a tie
    elif empty_spaces() is False:
        
        #if there is a tie, colors should change to yellow
        for row in range(3):
            for column in range(3):
                buttons[row][column].config (bg="#FDFD96")

        return "Tie"

    #no winner, no tie. Means the game continues until all are filled
    else:
        return False

def empty_spaces():
    spaces = 9 

    #check the text of each button to see if it is filled 
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1 #same as spaces = spaces - 1 

    #if there are no more spaces, return false
    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    #change the label
    label.config(text = player+" turn")

    #reset the display to original 
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["X","O"]
#select random player to begin 
player = random.choice(players)
# add 9 buttons and put them in a list 
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',20))
label.pack(side="top")


# commands call this new_game function after pressing this button
reset_button = Button(text="restart", font=('consolas',16), command=new_game)
reset_button.config(bg="#C3EEFA")

reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

#creates the 3 by 3 grid 
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',30), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

#this must be below
window.mainloop()



