from random import randint
import PySimpleGUI as sg


class TelaSimulador:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        self.layout = [
            [sg.Text('-' * 100)],
            [sg.Text('SEJA BEM VINDO AO SIMULADOR DE DADOS')],
            [sg.Text('-' * 100)],
            [sg.Button('RODAR O DADO', size=(50, 3))],
            [sg.Text('NÚMERO ALEATÓRIO ABAIXO')],
            [sg.Output(size=(60, 20))]
        ]

        self.janela = sg.Window('Simulador de Dados').layout(self.layout)

    def simula_dado(self):
        while True:
            self.button = self.janela.Read()
            print(randint(1, 6))

tela = TelaSimulador()
tela.simula_dado()
