import PySimpleGUI as sg   
import functions as fs   
import os
if not os.path.exists("todos.txt"):
     with open("todos.txt", 'w') as file:
          pass
sg.theme('DarkGreen3')
user_input=sg.InputText(tooltip="Enter todo.",key="todo")
layout = [[sg.Text('Type in todo.')],      
                 [user_input],      
                 [sg.Button("Add"),sg.Button("Show"), sg.Cancel("Exit")],
                 [sg.Listbox(values=fs.get_todos("todos.txt"),key="todos",enable_events=True,size=[45,10]),
                  sg.Button("Edit"),sg.Button("Remove")]]

window = sg.Window('Simple todo Example', layout,
                 font=('Helvetica',20))  
while True:
        event, values = window.read() 
        # print(event)
        #print(values['todos'])
                    
        match event:
             
            case 'Add':
                todos=fs.get_todos("todos.txt")
                #print(todos)
                new_todo= values['todo'] + "\n"
                todos.append(new_todo) 
                fs.write_todos("todos.txt",todos)
                window['todos'].update(values=todos)
            case 'Edit':
                  try:
                        todo_to_edit = values['todos'][0]
                        new_todo = values['todo']
                        todos=fs.get_todos("todos.txt")
                        index=todos.index(todo_to_edit)
                        todos[index]= new_todo
                        fs.write_todos("todos.txt",todos)
                        window['todos'].update(values=todos)
                  except IndexError:
                       sg.popup('Please select the item first.',font=('Helvetica',20))
                       
                       
                  #user_input=todo
                  #print(todo)
            case 'Remove':
                  todo_to_remove = values['todos'][0]
                  todos = fs.get_todos("todos.txt")
                  index=todos.index(todo_to_remove)
                  
                  todos.pop(index)
                  fs.write_todos("todos.txt",todos)
                  window['todos'].update(values=todos)
                  
            case 'Show':
                todos=fs.get_todos("todos.txt")
                for todo in todos:
                     
                    sg.popup('You entered', todo)
            case 'Exit':
                  sg.WIN_CLOSED 
                  
        if event == sg.WIN_CLOSED or event == 'Exit':
            break 
window.close()

             
        # sg.popup('You entered', text_input,
        #          font=('Helvetica',20))     


