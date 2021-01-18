import PySimpleGUI as sg
# Theme
sg.theme('DarkBlue14') 

# Define the window's contents
layout = [
    [sg.Text('Adjective',key='adj-',size=(12,2)),sg.InputText(key='-ADJ-')],
    [sg.Text('Verb1: ',key='verb1',size=(12,2)), sg.InputText(key='-V1-')],
    [sg.Text('Verb2: ',key='verb2',size=(12,2)), sg.InputText(key='-V2-')],
    [sg.Text('Person:',key='famous_person',size=(12,2)), sg.InputText(key='-P-')],
    [sg.Text(size=(8,1), key='-OUTPUT-')],
    [sg.Button('Submit'), sg.Button('Quit')],
    
    ]

#window

window = sg.Window('Alien Madlibs', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    # window['-OUTPUT-'].update('Computer programming is so ' + values['-ADJ-'] + 'It makes me so excited all the time and '
    # 'I love to' + values['-V1-'] + 'Stay hydrated and' + values['-V2-'] +  'like you are'  + values['-P-'])

    window['-OUTPUT-'].update(f"Computer programming is so {values['-ADJ-'][0]}" + f"It makes me so excited all the time and I love to {values['-V1-'][1]}" 
     f" Stay hydrated and {values['-V2-'][2]}" + f" like you are {values['-P-'][3]}")

# Finish up by removing from the screen
window.close()