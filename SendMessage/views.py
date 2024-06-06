from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from twilio.rest import Client
from time import sleep
import pywhatkit
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
    # for num in numeros:
    #     pywhatkit.sendwhatmsg_instantly("+52"+str(num), messageTemplate)

    print(list(map(str, numeros)))
   
def view_excel(request):
    session = request.session
    numeros = session.get('numeros')
    if request.method == "POST":
        messageTemplate = request.POST.get('message')
        FuctionSendMessage(numeros, messageTemplate)

    contexto = {'numeros':numeros}
    return render(request, 'view_excel.html', contexto)