import PySimpleGUI as sg
# Theme
sg.theme('DarkTanBlue')    

# Very basic window.

layout = [
    [sg.Text('Adjective',key='adj-',size=(12,2)),sg.InputText()],
    [sg.Text('Verb1: ',key='verb1',size=(12,2)), sg.InputText()],
    [sg.Text('Verb2: ',key='verb2',size=(12,2)), sg.InputText()],
    [sg.Text('Person:',key='famous_person',size=(12,2)), sg.InputText()],
    [sg.Submit(), sg.Cancel(), sg.Button('Reset')],
]

window = sg.Window('Alien Madlibs', layout)
event, values = window.read()
window.close()
#output
print(event,  f"Computer programming is so", values[0], "It makes me so excited all the time",
    "I love to",values[1],"Stay hydrated and",values[2],"like you are",values[3])