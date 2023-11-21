import os
import time
from tkinter import *


def main():
    janela = Tk()
    janela.title('Shutdownd Timer')


    bt_1 = Button(janela, text= 'Shutdown', command = shutdown)
    bt_1.grid(column=0, row=3)

    bt_2 = Button(janela, text= 'Cancel', command = cancel)
    bt_2.grid(column=0, row=4)

    janela.mainloop()


def cancel():
    exit()
def shutdown():
    t = int(input('Type in secconds, for how long you want for your computer to stay on?: '))
    T = t * 60
    for i in range(T,0,-1):
        print(i)
        time.sleep(1)
    os.system('shutdown /s /t 1')


main()

