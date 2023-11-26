from functions import get_todos,write_todos
import time
now = time.strftime("%b %d, %Y:%H:%S")
print("it is ", now)

""" 
other way to import functions.py syntax is

import functions

calling a function from the function.py file inside another file

functions.get_todos()
"""
while True:
    user_action = input("Type add,show,edit,remove or exit : ")
    user_action = user_action.strip()  # strip function removes space from the string
    # match user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")
        todos.append(todo + "\n")

        write_todos("todos.txt",todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for index, item in enumerate(
            todos
        ):  # emumerate function prints data in key,value pair format
            item = item.strip("\n")
            item = item.title()  # print each word capitalize
            row = f"{index + 1}-{item}"

            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")
            new_todo = input("Enter value:") + "\n"
            todos[number] = new_todo

            write_todos("todos.txt",todos)
        except ValueError:
            print("Invalid Command.")
            continue
    elif user_action.startswith("remove"):
        try:
            number = int(user_action[7:])

            todos = get_todos("todos.txt")

            todos.pop(number - 1)

            write_todos("todos.txt",todos)
        except (ValueError, IndexError):
            print("invalid number.")
            continue

    elif user_action.startswith("exit"):
        break
print("Bye!")
