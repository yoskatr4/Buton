
# gerekli kütüphaneler 
from tkinter import *
from tkinter import messagebox
import random
# tikla fonksiyonu
def tikla():
    messagebox.showinfo('', 'Hayırlı Olsun')
    quit()
# rastgele konuma kaçan buton
def motionMouse(event):
    btni.place(x=random.randint(0, 500), y=random.randint(0,500))

# pencere özelliklerini bu kısımdan değiştirebilirsin
root = Tk()
root.geometry('600x600')
root.title('AL BAKALIM Bİ TELEFON')
root.resizable(width=False, height=False)
root['bg'] = 'white'

# butonların özelliklerini bu kısımdan değiştirebilirsin
Label = Label(root, text='Öğrenciler Vergisiz Telefon Alabilir', font='Arial 20 bold', bg='white').pack()
btni = Button(root, text='iPhone 14 Pro Max', font='Arial 12 bold')
btni.place(x=170, y=100)
btni.bind('<Enter>', motionMouse)
btnV = Button(root, text='Vestel Venüs', font='Arial 12 bold', command=tikla).place(x=350,y=100)

root.mainloop()