import PySimpleGUI as sg
import pyttsx3


'''
    Make a: Interface to a TTS script
    Input: An Phrase, word, or sentece
    Output: Some sort of voice from google speech what user's type
     
'''

layout = [
    [sg.Text('Escreva o que você quer que o computador falek', key='-TEXT-')],
    [sg.Text(' ')],
    [sg.Input(key='-INPUT-'), sg.Spin(['Slow', 'Medium', 'Fast6+'], key='-SPEED-'), sg.Button('Speech Button', key='-BUTTON-')]
]

window = sg.Window('Text to Speech', layout)

voice_speed = 150

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    match values['-SPEED-']:

        case 'Fast':
            voice_speed = 400

        case 'Medium':
            voice_speed = 150

        case 'Slow':
            voice_speed = 50

    if event == '-BUTTON-':
        engine = pyttsx3.init()
        engine.setProperty('rate', voice_speed)
        print(values['-INPUT-'])
        engine.say(values['-INPUT-'])
        engine.runAndWait()

window.close()
