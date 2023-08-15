import streamlit as st
from send_email import send_email

st.header("Contact Me")

# app_password = owwu fqgr gzkk kjkh
# form is a component which contains other components inside it,
# also the form needs to have an id which we can see below
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    # text_area allows to enter multiline text
    raw_message = st.text_area("Type your message below")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    # button is boolean, hence when pressed it'll do the work below
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

