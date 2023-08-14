import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")#width=400)
with col2:
    st.title("Fahad Shaikh")
    content = """Hi, I am Fahad Shaikh, Centennial College software engineering graduate, specializing in AI, 
    skilled in Python, Java, and knowledgeable about Pyspark. Proficient in agile development, I've collaborated 
    effectively to solve complex problems. Former marketing specialist with strong leadership and communication 
    skills, leading successful work trips. Passionate about F1, cars, and design, and with logo design experience. 
    Committed to personal and professional growth for a career in software engineering and AI. 
    """
    st.info(content)