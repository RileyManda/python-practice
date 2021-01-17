import PySimpleGUI as sg
# Theme
sg.theme('DarkTanBlue')    

# Very basic window.

layout = [
    [sg.Text('Adjective',key='adj-')],
    [sg.Text('Verb',key='verb1'), sg.InputText()],
    [sg.Text('Verb',key='verb2'), sg.InputText()],
    [sg.Text('Famous Person:',key='person'), sg.InputText()],
    [sg.Submit(), sg.Cancel(), sg.Button('Reset')],
]

window = sg.Window('Alien Madlibs', layout)
event, values = window.read()
window.close()
#output
print(event,  f"Computer programming is so", values[0], "It makes me so excited all the time \
    I love to",values[1],"Stay hydrated and","like you are ",values[2])