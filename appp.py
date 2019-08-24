import PySimpleGUI as sg
import os.path, time
import os
from pprint import pprint
def dir(s):
    l = []
    dirlist =[]
    e=values['down']
    #searching the files and time
    for r, d, f in os.walk(s):
        for i in f:
            if values['at']== True:
                if e in i:
                    g = time.ctime(os.path.getctime(s))
                    dirlist = os.listdir(s)
                    return dirlist


            else:
                if e in i:
                    folder = values['in']
                    folder_size = 0
                    for (path, dirs, files) in os.walk(folder):
                        for file in files:
                            filename = os.path.join(path, file)
                            folder_size += os.path.getsize(filename)
                    o=("Folder = %0.1f MB" % (folder_size / (1024 * 1024.0)))
                    g = time.ctime(os.path.getctime(folder))
                    l.append(os.path.join(i, '    ', g,'   ',o))
                #g=time.ctime(os.path.getctime(s))
                #l.append(os.path.join(r,i,'     ',g))
    return l



layout = [[sg.Text('FILE EXPLORER')],
          [sg.Text('Enter a path'), sg.InputText('', key='in')],
          [sg.Text('Filter the files'),sg.InputText('',key='down')],#sg.Checkbox("Apply",key='top',default=False)],
          [sg.Button('FIND'), sg.Button('EXIT'),sg.Checkbox("DIRECTORIES",key='at',default = False)],#,sg.Checkbox("SIZE")],
          [sg.Multiline(disabled=True, size=(50, 10), key='tp')]
          ]

# Creating the Window
window = sg.Window('Window Title', layout)
while True:
    event, values = window.Read()
    if event in (None, 'EXIT'):
        break
    if event is 'FIND':
        l = dir(values['in'])
        window.FindElement('tp').Update("\n".join(l))
    print(event, values)

window.Close()