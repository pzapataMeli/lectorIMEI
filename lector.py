from queue import Empty
import os
import gspread, pandas as pd
import smtplib
import pygsheets
import datetime
from colorama import Fore, Back, init


if __name__ == "__main__":
    while True:
        init()
        print (Back.BLACK)
        print(Fore.GREEN+ """                                                               
db      d88888b  .o88b. d888888b  .d88b.  d8888b.   d8888b. d88888b   d888888b .88b  d88. d88888b d888888b .d8888. 
88      88'     d8P  Y8 `~~88~~' .8P  Y8. 88  `8D   88  `8D 88'         `88'   88'YbdP`88 88'       `88'   88'  YP 
88      88ooooo 8P         88    88    88 88oobY'   88   88 88ooooo      88    88  88  88 88ooooo    88    `8bo.   
88      88~~~~~ 8b         88    88    88 88`8b     88   88 88~~~~~      88    88  88  88 88~~~~~    88      `Y8b. 
88booo. 88.     Y8b  d8    88    `8b  d8' 88 `88.   88  .8D 88.         .88.   88  88  88 88.       .88.   db   8D 
Y88888P Y88888P  `Y88P'    YP     `Y88P'  88   YD   Y8888D' Y88888P   Y888888P YP  YP  YP Y88888P Y888888P `8888Y' 
                                                                                                                   
                                                                                                                   """+Fore.WHITE )
        codigo1 = input("MeliSKU: ")
        codigo2 = input("IMEI: ")
        #codigo3 = input("Tercer codigo: ")
        #codigo4 = input("Cuarto codigo: ")
        #codigo5 = input("Quinto codigo: ")
        #codigo6 = input("Sexto codigo: ")
        ahora = datetime.datetime.now()
        A1= len(codigo1)
        A2= len(codigo2)

        if A1 == 9:
            print(Fore.GREEN+"Meli SKU Correcto!")
        else:
            print(Fore.RED+"Meli SKU Invalido")
            continue
        if A2 == 15:
            print(Fore.GREEN+"IMEI Capturado con exito!")
        else:
            print (Fore.RED+"IMEI Invalido")
            continue    

        #print (len(codigo1))
        #print (len(codigo2))   

        service = gspread.service_account(filename="credentials.json")
        archivo = service.open("Scanner")
        ws = archivo.sheet1
        lista_listas = ws.get_all_values()
        df = pd.DataFrame(lista_listas)

        ws.append_row([codigo1, codigo2, ahora.strftime("%d/%m/%Y %H:%M:%S")])