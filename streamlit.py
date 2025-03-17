import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000"

# Title of the Streamlit app
st.title("To-Do Task Manager")

# Fetch all tasks from the FastAPI backend
def fetch_tasks():
    response = requests.get(f"{FASTAPI_URL}/tasks/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch tasks")
        return []

# Create a new task
def create_task(title, description, completed):
    task_data = {
        "title": title,
        "description": description,
        "completed": completed
    }
    response = requests.post(f"{FASTAPI_URL}/tasks/", json=task_data)
    if response.status_code == 200:
        st.success("Task created successfully!")
    else:
        st.error("Failed to create task")

# Update a task
def update_task(task_id, title, description, completed):
    task_data = {
        "title": title,
        "description": description,
        "completed": completed
    }
    response = requests.put(f"{FASTAPI_URL}/tasks/{task_id}", json=task_data)
    if response.status_code == 200:
        st.success("Task updated successfully!")
    else:
        st.error("Failed to update task")

# Delete a task
def delete_task(task_id):
    response = requests.delete(f"{FASTAPI_URL}/tasks/{task_id}")
    if response.status_code == 200:
        st.success("Task deleted successfully!")
    else:
        st.error("Failed to delete task")

# Sidebar for creating a new task
with st.sidebar:
    st.header("Create a New Task")
    title = st.text_input("Title")
    description = st.text_area("Description")
    completed = st.checkbox("Completed")
    if st.button("Create Task"):
        if title and description:
            create_task(title, description, completed)
        else:
            st.warning("Please fill in the title and description")

# Main section to display and manage tasks
st.header("Your Tasks")
tasks = fetch_tasks()

for task in tasks:
    with st.expander(f"Task #{task['id']}: {task['title']}"):
        st.write(f"**Description:** {task['description']}")
        st.write(f"**Completed:** {task['completed']}")

        # Update task form
        with st.form(key=f"update_form_{task['id']}"):
            new_title = st.text_input("Title", value=task["title"])
            new_description = st.text_area("Description", value=task["description"])
            new_completed = st.checkbox("Completed", value=task["completed"])
            if st.form_submit_button("Update Task"):
                update_task(task["id"], new_title, new_description, new_completed)
                st.rerun()  

        # Delete task button
        if st.button(f"Delete Task #{task['id']}"):
            delete_task(task["id"])
            st.rerun()  