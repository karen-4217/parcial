import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pyfirmata import Arduino, util
from tkinter import *

import time


placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
#arduino con analog_0 quemado

a0 = placa.get_pin('a:1:i')
a1 = placa.get_pin('a:2:i')
a2 = placa.get_pin('a:3:i')
led1 = placa.get_pin('d:3:p')
led2 = placa.get_pin('d:5:p')
led3 = placa.get_pin('d:6:p')

time.sleep(0.5)

ventana = Tk()
ventana.geometry('700x700')
ventana.title("PUNTO 1")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-f3a02.firebaseio.com/'
})



marco1 = Frame(ventana, bg="pink", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)

frame1 = Frame(marco1, bg="pink", highlightthickness=1, width=500, height=500, bd= 5)
frame1.place(x = 15,y = 15)
texto = Label(ventana, text="SENSORES", bg='cadet blue1', font=("Arial", 12), fg="white")
texto.place(x=110, y=20)



label1= Label(frame1, bg='yellow', font=("times new roman", 14), fg="gray", width=5)
info1=StringVar()
label1.configure(textvariable=info1)
label1.place(x=20,y=30)

label2= Label(frame1, bg='yellow', font=("times new roman", 14), fg="gray", width=5)
label2.place(x=20,y=70)
info2=StringVar()
label2.configure(textvariable=info2)

label3= Label(frame1, bg='yellow', font=("times new roman", 14), fg="gray", width=5)
label3.place(x=20,y=110)
info3=StringVar()
label3.configure(textvariable=info3)
   

def adc_read1():  

    ref = db.reference('sensor')
    x=ref.get()
    
    i=x.get('sensor 1')
    print(i)
    led1.write(i)

 
        
def adc_read2():
   

    ref = db.reference('sensor')
    x=ref.get()
    
    i=x.get('sensor 2')
    print(i)
    led2.write(i)
   
def adc_read3():
    

    ref = db.reference('sensor 3')
    x=ref.get()
    i=x.get('sensor 3')
    print(i)
    led3.write(i)
    
       


save_button=Button(marco1,text="ADC1_UPDATE1",command=adc_read1)
save_button.place(x=130, y=50)

save_button2=Button(marco1,text="ADC1_UPDATE2",command=adc_read2)
save_button2.place(x=130, y=90)

save_button3=Button(marco1,text="ADC1_UPDATE3",command=adc_read3)
save_button3.place(x=130, y=130)    
    
ventana.mainloop()

