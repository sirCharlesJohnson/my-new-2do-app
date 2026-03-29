import streamlit as st
import My_Todo.tests.tests.functions as functions

todos = functions.get_todos()

def add_todo():
    new_todo = (st.session_state.get("new_todo") or "").strip()
    if not new_todo:
        return
    todos.append(new_todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

checked_indices = []
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checkbox:
        checked_indices.append(index)

if checked_indices:
    todos = [t for i, t in enumerate(todos) if i not in set(checked_indices)]
    functions.write_todos(todos)
    st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')