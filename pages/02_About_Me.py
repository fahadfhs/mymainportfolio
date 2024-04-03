import streamlit as st


def display_about_me():
    st.title("About Me")

    st.write("""
    Below you can find some of my skills and tools I have worked with.
    """)

    # Skills & Expertise
    st.header("Skills & Expertise")
    with st.container():
        skills_expertise = [
            "Data Analysis",
            "Machine Learning",
            "Python Programming",
            "Data Visualization",
        ]
        for skill in skills_expertise:
            st.success(f"- {skill}")

    # Technologies & Tools
    st.header("Technologies & Tools")
    with st.container():
        technologies_tools = [
            "Python, R, SQL",
            "Pandas, Numpy, Matplotlib, Seaborn, Plotly, ggplot",
            "Git, VS Code, Pycharm"
        ]
        for tech_tool in technologies_tools:
            st.info(f"- {tech_tool}")

    # Additional Tools & Platforms
    st.header("Additional Tools & Platforms")
    with st.container():
        additional_tools = [
            "Tableau",
            "RStudio",
            "Jupyter Notebook",
            "R Notebook",
            "R Markdown",
            "Kaggle"
        ]
        for tool in additional_tools:
            st.warning(f"- {tool}")

    # Education & Certifications
    st.header("Education & Certifications")
    with st.container():
        education_certifications = [
            "Software Engineering (A.I) Advanced Diploma, Centennial College, 2023",
            "Python Mega Course- Udemy, 2023",
            "Google Data Analytics Certificate, 2024"
        ]
        for certification in education_certifications:
            st.info(f"- {certification}")

    # Experience
    st.header("Experience")
    with st.container():
        st.markdown(
            """
            - **Team Leader, Sales Representative** | Aedos Marketing, Halifax, NS | Jan 2018 - Mar. 2020
              - *Sales and Marketing Expertise:* Consistently achieved sales goals, generated high revenue, and developed effective techniques.
              - *Leadership:* Led team of over 10, and managed sales strategies for territories across Nova Scotia and PEI.
              - *Communication and Negotiation:* Utilized exceptional skills to sell home internet, television, and security systems, while maintaining positive customer relationships.
              - *Strategic Thinking:* Piloted campaigns to develop effective marketing strategies.
              - *Results-Oriented:* Expanded customer base in targeted territories by implementing effective sales strategies.
            """,
            unsafe_allow_html=True,
        )


# Call the function to display the content
display_about_me()