from tkinter import *
from tkinter import ttk

def show_game_page():
    # Hide main page frame
    frm.grid_forget()
    
    # New frame for game page
    game_frm = ttk.Frame(root, padding=100)
    game_frm.grid()
    
    # Add widgets for the game page
    ttk.Label(game_frm, text="Player 1").grid(row=0, columnspan=3)

    for i in range(3):
        for j in range(3):
            ttk.Button(game_frm, text=" ", width=5, command=lambda row=i, col=j: on_click(row, col)).grid(row=i+1, column=j, padx=5, pady=5)

    ttk.Button(game_frm, text="Quit?", command=root.destroy).grid(row=4, columnspan=3)


def on_click(row, col):
    print(f"Button clicked at row {row}, column {col}")


def show_main_page():
    # Hide the current frame
    frm.grid_forget()
    
    # Re-show the main frame
    frm.grid()
    
    # Add widgets for the main page
    ttk.Label(frm, text="Please enter a name player 1: ").grid(column=0, row=0)
    ttk.Label(frm, text="Please enter a name player 2: ").grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, sticky="sw")
    ttk.Button(frm, text="Let the games begin!", command=show_game_page).grid(column=1, row=2, sticky="se")

root = Tk()
root.title("XO's")
frm = ttk.Frame(root, padding=100)
frm.grid()

show_main_page()

root.mainloop()
