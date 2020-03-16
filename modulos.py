# modulos de python (Python Module Index)
import datetime 

print(datetime.date.today())


from datetime import timedelta

print(timedelta(minutes=70))

# modulos de terceros (pypi.org) pip install colorama
from colorama import Fore, Style, init
init(convert=True)
print(Fore.CYAN + "Hola Mundo")



# Modulos propios
from fsumar import sumar 
sumar(10,20)