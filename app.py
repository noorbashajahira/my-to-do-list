import streamlit as st

# Page title
st.title("📝 To-Do List")

# Store tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
task = st.text_input("Enter a task:")

# Add task button
if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append({
            "task": task,
            "completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.subheader("My Tasks")

# Display tasks
for i, item in enumerate(st.session_state.tasks):

    col1, col2 = st.columns([4, 1])

    with col1:
        completed = st.checkbox(
            item["task"],
            value=item["completed"],
            key=f"task_{i}"
        )

        st.session_state.tasks[i]["completed"] = completed

    with col2:
        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# Task summary
total = len(st.session_state.tasks)
completed = sum(
    1 for item in st.session_state.tasks
    if item["completed"]
)

st.write(f"📌 Total Tasks: **{total}**")
st.write(f"✅ Completed: **{completed}**")
st.write(f"⏳ Pending: **{total - completed}**")