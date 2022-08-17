
## Utilizando pysimpleGUI para criação de interfaces graficas

import PySimpleGUI as sg

layout=[[sg.Text("Ola EStou Criando uma Mensagem")],[sg.Button('OK')]]

## Criar a janela 

window = sg.Window("Titulo do Programa",layout)

## Criar a ação ou loop do evento

while True:
    event,values = window.read()
    ## Finaliza o programa
    if event == "OK" or event ==sg.WIN_CLOSED:
        break

window.close()