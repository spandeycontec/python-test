import PySimpleGUI as sg
import zip_extract as zp
label1 = sg.Text("Select archive.")
input1 = sg.Input()
choose_button1=sg.FilesBrowse("Choose",key="files")

label2= sg.Text("Select destination.")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key="folder")

submit = sg.Button("Extract")
cancle = sg.Cancel()
window=sg.Window("File Decompressor",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[submit]])

while True:
    event, values = window.read()
    match event:
        case 'Extract':

            event,values=window.read()
            #print(event,values)
            filepath=values["files"].split(";")
            folder= values["folder"]
           # print(filepath,folder)
            
            zp.extract_archive(filepath,folder)
            sg.popup('File decompressed successfully. Check output directory.')
            # window['files'].update(values=" ")
            # window['folder'].update(values=" ")
    if event == sg.WIN_CLOSED or event == 'Exit':
            break 
window.close()
      
        
