from tkinter import *
from tkinter import ttk

# Initialize the root window
root = Tk()
root.title("XO's")

# Variables to store player names
player1_name = StringVar()
player2_name = StringVar()
current_player = StringVar(value="X")
array = [[" " for _ in range(3)] for _ in range(3)]
buttons = []


def show_game_page():
    global buttons, array
    array = [[" " for _ in range(3)] for _ in range(3)]
    buttons = []
    
    # Hide main page frame
    frm.grid_forget()
    
    # New frame for game page
    game_frm = ttk.Frame(root, padding=100)
    game_frm.grid()
    
    msg_text = Text(game_frm)
    
    # Add widgets for the game page
    ttk.Label(game_frm, text=f"{player1_name.get()} (X) vs {player2_name.get()} (O)").grid(row=0, columnspan=3)

    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = ttk.Button(game_frm, text=" ", width=5, command=lambda row=i, col=j: on_click(row, col))
            btn.grid(row=i+1, column=j, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    ttk.Button(game_frm, text="Quit", command=root.destroy).grid(row=4, columnspan=3)


def on_click(row, col):
    if array[row][col] == " ":
        array[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get())
        
        if checkwin(current_player.get()):
            print(f"{current_player.get()} wins!!!")
            msg_text.insert(END,f"{current_player.get()} wins.\n")
            
            for row_buttons in buttons:
                for btn in row_buttons:
                    btn.config(state="disabled")
        else:
            switch_player()
    else:
        print("This spot is already taken")


def switch_player():
    if current_player.get() == "X":
        current_player.set("O")
    else:
        current_player.set("X")


def checkwin(player):
    for row in array:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(array[0])):
        if array[0][col] == array[1][col] == array[2][col] and array[0][col] != ' ':
            return True

    if array[0][0] == array[1][1] == array[2][2] and array[0][0] != ' ':
        return True
    if array[0][2] == array[1][1] == array[2][0] and array[0][2] != ' ':
        return True

    return False


def show_main_page():
    # Hide the current frame
    frm.grid_forget()
    
    # Re-show the main frame
    frm.grid()
    
    # Add widgets for the main page
    ttk.Label(frm, text="Please enter a name player 1: ").grid(column=0, row=0)
    ttk.Entry(frm, textvariable=player1_name).grid(column=1, row=0)
    ttk.Label(frm, text="Please enter a name player 2: ").grid(column=0, row=1)
    ttk.Entry(frm, textvariable=player2_name).grid(column=1, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, sticky="sw")
    ttk.Button(frm, text="Let the games begin!", command=show_game_page).grid(column=1, row=2, sticky="se")


frm = ttk.Frame(root, padding=100)
frm.grid()

show_main_page()

root.mainloop()
