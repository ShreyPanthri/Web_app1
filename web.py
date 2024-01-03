import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


todos = functions.get_todos()

st.title('My ToDo App')
st.subheader('Personal ToDo app.')
st.write('Helps in increasing Productivity')

for index, tod in enumerate(todos):
    checkbox = st.checkbox(tod, key=tod)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[tod]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo....",
              on_change=add_todo, key="new_todo")

# st.session_state. This acts as a dictionary. It is a way to share variables btw reruns.
