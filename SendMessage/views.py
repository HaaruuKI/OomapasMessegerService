from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from twilio.rest import Client
from time import sleep
import webbrowser as web
import pywhatkit
import pyautogui as pg

import pandas as pd

def ReadExcel(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        namePage = request.POST["namePage"]
        letterColumn = request.POST["letterColumn"]
        
        if file:
            if not file.content_type.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
                return render(request, 'index.html', {'error': 'Tipo de formato invalido. Por favor de subir un archivo de Excel (.xlsx).'})

            try:
                # Attempt to read the Excel file with error handling
                data = pd.read_excel(file, sheet_name=namePage, usecols=letterColumn)
                numeros = []
                for row in data.itertuples():
                    valor_celda = row[1]
                    numeros.append(valor_celda)
                session = request.session
                session['numeros'] = numeros
                return redirect('viewExcel')

            except (FileNotFoundError, pd.errors.ClosedFileError, Exception) as e:
                # Handle errors for missing sheet or file
                error_message = 'Error: ' + str(e)
                return render(request, 'index.html', {'error': error_message})
        else:
            return render(request, 'index.html', {'error': 'No file uploaded.'})

    else:
        pass

    return render(request, 'index.html')

def FuctionSendMessage(numeros, messageTemplate):
    for num in numeros:
        try:
            web.get(using=None).open("https://web.whatsapp.com/send?phone=+52" + str(num) + "&text=" + messageTemplate )
            sleep(6)
            pg.click(1230, 1150)
            sleep(2)
            pg.press("enter")

            sleep(4)
            pg.hotkey('ctrl','w')
            sleep(1)
        except Exception as e:
            print(f"Error opening WhatsApp for number {num}: {e}")

        
        # try:
        #     with open("Reporte.txt", "a") as archivo:
        #         today = date.today()
        #         now = datetime.now()

        #         fecha = f"{today.day}/{today.month}/{today.year}"
        #         hora = f"{now.hour}:{now.minute}"

        #         archivo.write(f"Fecha: {fecha}\nHora: {hora}\nNumero de telefono: {num}\nMensaje: {messageTemplate}\n--------------------")
        # except Exception as error:
        #     # Maneja cualquier error que ocurra
        #     print(f"Error al crear el archivo: {error}")

def view_excel(request):
    session = request.session
    numeros = session.get('numeros')
    if request.method == "POST":
        messageTemplate = request.POST.get('message')
        FuctionSendMessage(numeros, messageTemplate)

    contexto = {'numeros':numeros}
    return render(request, 'view_excel.html', contexto)