from tkinter import*
import pyautogui as pg
import time

def pegartexto():
    a=Entrada1.get()
    z=int(Entrada2.get())
    x=0

    time.sleep(5)
    while x<z:
        pg.write(f'{a}\n')
        time.sleep(0.2)
        x+=1

root=Tk()

root.geometry("350x150")
root.title("Spam Message App")
root.config(bg="lightblue")

def on_enter(e):
    Entrada1.delete(0, 'end')
    
def on_leave(e):
    e1=Entrada1.get()
    if e1=='':
        Entrada1.insert(0,'Your Message')

Entrada1=Entry(root)
Entrada1.insert(0,"Your Message")
Entrada1.place(x=25, y=20,width=290)
Entrada1.bind('<FocusIn>', on_enter)
Entrada1.bind('<FocusOut>', on_leave)

def on_enter(e):
    Entrada2.delete(0, 'end')
    
def on_leave(e):
    e2=Entrada2.get()
    if e2=='':
        Entrada2.insert(0,'How Many Times?')

Entrada2=Entry(root)
Entrada2.insert(0,"How Many Times?")
Entrada2.place(x=25, y=52,width=290)
Entrada2.bind('<FocusIn>', on_enter)
Entrada2.bind('<FocusOut>', on_leave)

btn=Button(root, text="Enviar", foreground="white", bg="darkgreen", command=pegartexto)
btn.place(x=25,y=85, width=290)

root.mainloop()