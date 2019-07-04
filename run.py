from tkinter import *

state_of_play = [
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 0]
]

def __main__():
    intro()
    draw_window()

def renderStateOfPlay():
    """take the state_of_play array and draw it to the screen as ascii"""

def playerTurn(coord):
    """take players choice and update the state of play"""

def computerTurn():
    """TBC"""

def intro():
    print("welcome to Noughts and Crosses!")
    print("Please press enter to start the game!")
    input()

    print("Now we may begin. May the DoughNought be with you!")
    input()
    print("Let's begin with the rules, Enlightened One.")
    print("Your deadly Enemy, Computer, will be fighting you.")
    print("However, You may go First!")

def draw_window_grid():
    window=Tk()
    window.title('Noughts and Crosses')
    window.geometry("300x200+10+20")
    from PIL import ImageTk
    im = ImageTk.PhotoImage(file="test.png")
    canvas = Canvas(window, width=900, height=900)
    canvas.pack()
    canvasImage = canvas.create_image(0, 0, image=im, anchor="nw")
    window.mainloop()

if __name__ == "__main__":
    __main__()