import streamlit as st

st.header("Contact Me")

# app_password = owwu fqgr gzkk kjkh
# form is a component which contains other components inside it,
# also the form needs to have an id which we can see below
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    # text_area allows to enter multiline text
    message = st.text_area("Type your message below")
    button = st.form_submit_button("Submit")
    # button is boolean, hence when pressed it'll do the work below
    if button:
        print("Pressed")

