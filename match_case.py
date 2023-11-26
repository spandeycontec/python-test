todos=[]
while True:
    user_action= input("Type add,show,edit,remove or exit : ")
    user_action = user_action.strip() # strip function removes space from the string
    match user_action:
        case 'add':
            todo= input("Enter a to do : ") + "\n"
            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)

        case 'show':
            # print all element in todos
            # print(todos)  
            for index,item in enumerate(todos): # emumerate function prints data in key,value pair format
                item= item.title() # print each word capitalize
                row= f"{index}-{item}"
                #print(index,'-',item)
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number= number-1
            new_todo = input("Enter new todo number:")
            todos[number]=new_todo
        case 'remove':
            number = int(input("Number of the todo to remove: "))
           
            todos.pop(number)
            
        case _:
            print("Command not found")
print("Bye!")
    
    