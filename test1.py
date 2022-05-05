from tkinter import *
from tkinter import messagebox

from click import command
 
 
root = Tk()
root.geometry("300x600")
root.title("Lector de IMEIs")

def take_input1():
    IMEI = inputtxt1.get("1.0", "end-1c")
    print(IMEI)
    if len(IMEI) == 15:
        output1.configure(bg="green")
        l.configure(text="Correcto")
    else:
        output1.configure(bg="red")
    return IMEI

def take_input2():

    SKU= inputtxt2.get("1.0", "end-1c")
    print(SKU)
    if len(SKU) == 9:
        output2.configure(bg="green")
    else:
        output2.configure(bg="red")
    return SKU

#Acá defino los objetos que van en la función
l = Label(text = "Ingrese el IMEI:")


inputtxt1 = Text(root, height=10, width=25, bg = "light yellow")
l2 = Label(text = "Ingrese el SKU:")
inputtxt2 = Text(root, height=10, width=25, bg = "green")

output1 = Text(root, height=10, width=25, bg = "white")
output2 = Text(root, height=10, width=25, bg = "white")

#display = Button(root, height = 2, width=20, text="Show", command= lambda:take_input1(),take_input2())
root.bind('<Return>', take_input1())
root.bind('<Return>', take_input2())


    

l.pack()
l2.pack()
inputtxt1.pack()
inputtxt2.pack()
#display.pack()
output1.pack()
output2.pack()


#Siempre al final
root.mainloop()