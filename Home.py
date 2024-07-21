import streamlit as st
import pandas as pd
import os
import base64

# Load data and define image size
df = pd.read_csv("data.csv", sep=";")
IMAGE_WIDTH = 250

# Custom CSS styles
intro_style = """
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 20px;
"""

app_card_style = """
    border: 1px solid #e6e6e6;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
"""

# Header and introduction
st.title("Fahad Shaikh")
st.image("images/photo.png", width=IMAGE_WIDTH)
st.markdown(
    f"""<p style="{intro_style}">Hi, I am Fahad Shaikh, Centennial College Software Engineering (A.I) graduate, 
    focusing in Data Analytics Roles skilled in Python, SQl.Proficient in agile development, I've collaborated 
    effectively to solve projects in academic setting along with personal.
    Former marketing specialist with strong leadership and communication skills, leading 
    successful work trips. Passionate about F1, cars, and design, and with logo design 
    experience. Committed to personal and professional growth for a career in software 
    engineering and AI.</p>""",
    unsafe_allow_html=True,
)

# Define the width for the logos
logo_width = 40

# Define profile URLs
linkedin_url = "https://www.linkedin.com/in/fahad-shaikh-692332a5/"
twitter_url = "https://twitter.com/FahadFHS"
github_url = "https://github.com/fahadfhs"
tableau_url = "https://public.tableau.com/app/profile/fahad.shaikh3307/vizzes"
kaggle_url = "https://www.kaggle.com/fahadfhs"

# Adjust column widths
col1, col2, col3, col4, col5 = st.columns(5)

# Display the logos with links to profiles
with col1:
    st.image("images/linkedin-logo.png", width=logo_width, use_column_width=False)
    st.markdown(f"[LinkedIn]({linkedin_url})", unsafe_allow_html=True)

with col2:
    st.image("images/x-logo.png", width=logo_width, use_column_width=False)
    st.markdown(f"[Twitter]({twitter_url})", unsafe_allow_html=True)

with col3:
    st.image("images/github-logo.png", width=logo_width, use_column_width=False)
    st.markdown(f"[GitHub]({github_url})", unsafe_allow_html=True)

with col4:
    st.image("images/tableau-logo.png", width=logo_width, use_column_width=False)
    st.markdown(f"[Tableau]({tableau_url})", unsafe_allow_html=True)

with col5:
    st.image("images/kaggle-logo.png", width=logo_width, use_column_width=False)
    st.markdown(f"[Kaggle]({kaggle_url})", unsafe_allow_html=True)

# Intro
st.markdown("*Below you can find some of the apps I have built in Python. Feel free to contact me!*")

for index, row in df.iterrows():
    image_path = os.path.join("images", row["image"])

    # Display the app information with image embedded using HTML
    st.markdown(
        f'<div style="border: 1px solid #e6e6e6; border-radius: 10px; padding: 20px; margin-bottom: 20px;">'
        f'<h3>{row["title"]}</h3>'
        f'<p>{row["description"]}</p>'
        f'<img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" style="max'
        f'-width:300px;" alt="{row["title"]}"> '
        f'<p><a href="{row["url"]}">Github Repository</a></p>'
        f'</div>',
        unsafe_allow_html=True,
    )

# col1, col2 = st.columns(2)
#
# for index, row in df[:10].iterrows():
#     with col1:
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"], width=IMAGE_WIDTH)
#         st.write(f"[Source Code]({row['url']})")
#
# for index, row in df[10:].iterrows():
#     with col2:
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"], width=IMAGE_WIDTH)
#         st.write(f"[Source Code]({row['url']})")
