import tkinter as tk

def gamestart():
    menu.destroy()
    game=tk.Tk()
    game.title('Game')
    game.resizable(width=False, height=False)
    canvas=tk.Canvas(game, width=720, height=800)
    canvas.pack()
    goToMenuBut=tk.Button(game, text='X', width=5, height=2, bg='white', fg='blue', command=game.destroy).place(x=0, y=0)
    chooseABut=tk.Button(game, text='Something A', width=50, height=2, bg='white', fg='black').place(x=0, y=765)
    chooseBBut=tk.Button(game, text='Something B', width=50, height=2, bg='white', fg='black').place(x=365, y=765)

menu=tk.Tk()
menu.title("Menu")
canvas=tk.Canvas(menu, width=720,height=800)
menu.resizable(width=False, height=False)
canvas.pack()

text = tk.Label(menu, text="Game", font="Arial 72").place(x=220, y=10)
startgameBut = tk.Button(menu, text="Начать игру", width=25,height=3, bg="white",fg="black", font='36', command=gamestart).place(x=260, y=400)
butexit = tk.Button(menu, text='Выход', width=25, height=3, bg='white', fg='black', font='28', command=menu.destroy).place(x=510, y=738)

