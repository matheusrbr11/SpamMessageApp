from tkinter import*
import pyautogui as pg
import time

def pegartexto():
    a=Entrada1.get()
    z=int(Entrada2.get())
    x=0

    time.sleep(5)
    while x<z:
        pg.write(f'{a}, #{x}\n')
        x+=1

root=Tk()

root.geometry("300x150")
root.title("MyApp")
root.config(bg="lightblue")

Entrada1=Entry(root,)
Entrada1.place(x=25, y=20)
Entrada2=Entry(root,)
Entrada2.place(x=25, y=52)

btn=Button(root, text="Enviar", foreground="white", bg="darkgreen", command=pegartexto)
btn.place(x=25,y=85, width=164)

root.mainloop()