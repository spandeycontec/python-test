#todos=[]
while True:
    user_action= input("Type add,show,edit,remove or exit : ")
    user_action = user_action.strip() # strip function removes space from the string
    match user_action:
        case 'add':
            todo= input("Enter a to do : ") + "\n"
            
            with open('todos.txt','r') as file:
                todos=file.readlines()
            #print(todo)
            #print(todos)
            todos.append(todo)
            
            #todos.append(todo)
            with open('todos.txt','w') as file:
                file.writelines(todos)
            

        case 'show':
            # print all element in todos
            # print(todos)  
            file=open('todos.txt','r')
            with open('todos.txt','r') as file:
                 todos=file.readlines()
            
            for index,item in enumerate(todos): # emumerate function prints data in key,value pair format
                item = item.strip('\n')
                item= item.title() # print each word capitalize
                row= f"{index + 1}-{item}"
                #print(index,'-',item)
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number= number-1
            with open('todos.txt','r') as file:
                todos=file.readlines()
            new_todo = input("Enter value:") + "\n"
            todos[number]=new_todo
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'remove':
            number = int(input("Number of the todo to remove: "))
            with open('todos.txt','r') as file:
                todos=file.readlines()
           
            todos.pop(number-1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
            
        case _:
            print("Command not found")
print("Bye!")
    
    