import streamlit as st

def page1():
  """Content and logic for page 1"""
  name = st.text_input("Enter your name:")
  submit_button = st.button("Submit")

  if submit_button:
    st.session_state["user_name"] = name  # Store user input
    st.success("Information submitted!")
    st.experimental_rerun()  # Trigger page refresh

# page2.py

import streamlit as st

def page2():
  """Content and logic for page 2"""
  if "user_name" in st.session_state:
    name = st.session_state["user_name"]
    st.write(f"Welcome, {name}!")
  else:
    st.write("Please enter your information on the previous page.")

# Main Script (logic for displaying pages)
if "user_name" in st.session_state:
  page2()
else:
  page1()
