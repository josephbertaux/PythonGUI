import PySimpleGUI as sg
# import PySimpleGUIQt as sg

from my_funcs import try_func

sg.theme('DarkAmber')

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Button('Cancel')],
            [sg.Button('my_func_1'), sg.Button('my_func_2')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try_func(event)

window.close()
