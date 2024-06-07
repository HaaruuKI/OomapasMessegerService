# import pandas as pd
# import webbrowser as web
# import pyautogui as pg
# import time   

# lista = [6311860453,6311661632]

# for num in lista:
#     edge_path = 'C:/Users\vicen\AppData\Local\Programs\Opera GX\launcher.exe %s'

#     # web.get(chrome_path).open("https://www.google.com/search?client=opera-gx&q=hola&sourceid=opera&ie=UTF-8&oe=UTF-8")
#     web.get(edge_path).open("https://web.whatsapp.com/send?phone=+52" + str(num) + "&text=Mensaje de prueba." )

#     time.sleep(10)
#     pg.click(1230, 1150)
#     time.sleep(5)
#     pg.press("enter")

#     time.sleep(5)
#     pg.hotkey('ctrl','w')
#     time.sleep(2)


# web.get(using=None).open("https://docs.python.org/es/3/library/webbrowser.html")


# from datetime import date
# from datetime import datetime


# phone_numbers = [
#     "+526311860453","+526311661632","+526311860453"
# ]

# message = "Este es un mensaje masivo enviado con Python."

# for phone_number in phone_numbers:
#     now = datetime.now()
#     minutos = now.minute + 1
#     hora = now.hour
#     print(minutos)
        
#     pw.sendwhatmsg(phone_no=phone_number,message=message,time_hour=hora,time_min=minutos)

import pywhatkit as pw
from datetime import date
from datetime import datetime

def crear_archivo_txt():
  try:
    # Abre el archivo en modo de escritura
    with open("Reporte.txt", "w") as archivo:
      today = date.today()
      now = datetime.now()
      
      fecha = f"{today.day}/{today.month}/{today.year}"
      hora = f"{now.hour}:{now.minute}"
      numero = "+526311860453"
      mensaje = "Mensaje de prueba"

      archivo.write(f"Fecha: {fecha}\nHora: {hora}\nNumero de telefono: {numero}\nMensaje: {mensaje}\n--------------------")
  except Exception as error:
    # Maneja cualquier error que ocurra
    print(f"Error al crear el archivo: {error}")

# Llama a la función para crear el archivo
crear_archivo_txt()
