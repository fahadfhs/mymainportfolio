import streamlit as st
import pandas

st.set_page_config(layout="wide")

# adding list in columns func to specify the ratio in terms of area covered in the webpage
# since nothing is added in the empty col, no need to add another context manager.
col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Fahad Shaikh")
    content = """Hi, I am Fahad Shaikh, Centennial College software engineering graduate, specializing in AI, 
    skilled in Python, Java, and knowledgeable about Pyspark. Proficient in agile development, I've collaborated 
    effectively to solve complex problems. Former marketing specialist with strong leadership and communication 
    skills, leading successful work trips. Passionate about F1, cars, and design, and with logo design experience. 
    Committed to personal and professional growth for a career in software engineering and AI. 
    """
    st.info(content)
# I am using markdown for info part to make it bolder
content2 = """Below you can find some of the apps I have built in Python.
Feel free to contact me!"""
st.markdown(f"**{content2}**")

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        # We are joining the path below from two diff directories for the images to be
        # accessed and showed in the loop
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
