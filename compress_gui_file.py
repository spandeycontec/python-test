import PySimpleGUI as sg
import zip_createro as zp
label1 = sg.Text("Enter file to compress.")
input1 = sg.Input()
choose_button1=sg.FilesBrowse("Choose",key="files")

label2= sg.Text("Enter destination folder.")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key="folder")

submit = sg.Button("Compress")
cancle = sg.Cancel()
window=sg.Window("File Compressor",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[submit,cancle]])

while True:
    event, values = window.read()
    match event:
        case 'Compress':

            event,values=window.read()
            #print(event,values)
            filepath=values["files"].split(";")
            folder= values["folder"]
            
            zp.make_archive(filepath,folder)
            sg.popup('File compressed successfully. Check output directory.')
            # window['files'].update(values=" ")
            # window['folder'].update(values=" ")
    if event == sg.WIN_CLOSED or event == 'Exit':
            break 
window.close()
      
        
"""
how to create exe file in python 
1. install pyinstaller plugin
2. pyinstaller --onefile --windowed --clean compress_gui_file.py
"""