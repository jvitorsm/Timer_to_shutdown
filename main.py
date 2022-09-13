import os
import time
from tkinter import *


def main():
    janela = Tk()
    janela.title('Shitdownd Timer')


    menu = Label(janela, text = 'Press 1 to turnoff     Press 2 to Cancel       Press 3 to exit')
    menu.grid(column=0, row = 0)

    bt_1 = Button(janela, text= 'Shutdown', command = shutdown)
    bt_1.grid(column=0, row=3)

    bt_2 = Button(janela, text= 'Cancel', command = cancel)
    bt_2.grid(column=0, row=4)

    janela.mainloop()


def cancel():
    exit()
def shutdown():
    t = int(input('how long do you want the computer to shut down in minutes '))
    T = t * 60
    for i in range(T,0,-1):
        print(i)
        time.sleep(1)
    os.system('shutdown /s /t 1')


main()

