#todos=[]
while True:
    user_action= input("Type add,show,edit,remove or exit : ")
    user_action = user_action.strip() # strip function removes space from the string
    #match user_action:
    if user_action.startswith("add"):
        todo=user_action[4:]
        #case 'add':
        #todo= input("Enter a to do : ") + "\n"
            
        with open('todos.txt','r') as file:
            todos=file.readlines()
            #print(todo)
            #print(todos)
            todos.append(todo + '\n')
            
            #todos.append(todo)
        with open('todos.txt','w') as file:
            file.writelines(todos)
            

    elif user_action.startswith("show"):
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
    elif user_action.startswith("edit"):
                try:
                     
                #break
                    number = int(user_action[5:])
                    number= number-1
                    #number = int(input("Number of the todo to edit: "))
                    
                    with open('todos.txt','r') as file:
                        todos=file.readlines()
                    new_todo = input("Enter value:") + "\n"
                    todos[number]=new_todo
                    with open('todos.txt','w') as file:
                        file.writelines(todos)
                except ValueError:
                    print("Invalid Command.")
                    continue 
    elif user_action.startswith("remove"):
            try:
                 
                number = int(user_action[7:])
            
                #number = int(input("Number of the todo to remove: "))
                with open('todos.txt','r') as file:
                    todos=file.readlines()
            
                todos.pop(number-1)
                with open('todos.txt','w') as file:
                    file.writelines(todos)
            except(ValueError, IndexError):
                 print("invalid number.")
                 continue
            
    elif user_action.startswith("exit"):

        #print("press ctrl + c to exit")
        break
print("Bye!")
    
    