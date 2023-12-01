import streamlit as st
import functions as fs
def add_todo():
    new_todo=st.session_state.todo
    todos.append(new_todo + "\n") 
    fs.write_todos("todos.txt",todos)


    

todos=fs.get_todos("todos.txt")
st.title("My todo app")
st.subheader("this is my todo app.")
st.write("This app is to increase your productivity.")
unique_value = 0
for index,todo in enumerate(todos):
    #unique_value += 1
    chkbox=st.checkbox(todo, key=todo)
    if chkbox:
        todos.pop(index)
        fs.write_todos("todos.txt",todos)
        del st.session_state[todo]
        st.experimental_rerun()
        

    

st.text_input(label="write your todo here.",placeholder='add new todo',key="todo",on_change=add_todo)


"""
how to run web app in local sever
streamlit run .\todo_web.py
how to deploy web app
1. press ctrl+shift+p
2. create enviorment
3. create requirement.txt
4. pip freeze > requirements.txt
"""
