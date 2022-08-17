import PySimpleGUI as sg

## Criar os itens da janela

layout = [[sg.Text("Qual Seu Nome ?")],
        [sg.Input(key='-INPUT-')],
        [sg.Text(size=(40,1),key='-OUTPUT-')],
        [sg.Button('OK'),sg.Button("Sair")]]

# Criar a janela com os itens acima

window = sg.Window("Titulo do Programa",layout)

# Criar a acções do programa e botoes

while True:
    event,values=window.read() 
    # Validacao usuario sair e fechar a janela
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    # Criar a saida do input em console
    window["-OUTPUT-"].update("Olá "+values['-INPUT-']+' Gravando Saida em Console')

window.close()



