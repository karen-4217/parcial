import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pyfirmata import Arduino, util
from tkinter import *
import time
placa = Arduino ('COM3')
it = util.Iterator(placa)
#inicio el iteratodr
it.start()

root=Tk()

variable=StringVar()

led1= placa.get_pin('d:8:o') 
led2= placa.get_pin('d:9:o') 
led3= placa.get_pin('d:10:o') 
led4= placa.get_pin('d:11:o') 
led5= placa.get_pin('d:12:o') 
led6= placa.get_pin('d:13:o') 

ventana = Tk()
ventana.geometry('850x850')
ventana.configure(bg = 'white')
ventana.title("punto 3")
texto = Label(ventana, text="entry", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=20, y=20)

def entrada(input):
    content = dato.get()
    dato.delete(0, END)
    if int(content)>= 8 and int(content)<= 13:
        
        else
        print("ingresar un nuevo numero")
    
    print(content)  

def update():
    i=0
    while 1:
        i=i+1
        variable.set(str(i))
        root.update()

label1=Label(root,textvariable=variable)
label1.pack()
boton=Button(marco1,text="ACTULIZAR",command=update)
boton.place(x=130, y=50)

    
Label(ventana, text="Input: ").place(x=20, y=60)
dato = Entry(ventana)
dato.place(x=90, y=60)
dato.bind('<Return>', entrada)


ventana.mainloop()

