import streamlit as st

def display_data_analysis_projects():
    st.title("Data Analysis Projects")

    st.write("Here are some of my data analysis projects:")

    # Project 1
    with st.expander("Sales Analysis 📈", expanded=False):
        st.image("images/sales_analysis_image.jpg", use_column_width=True)
        st.write("This project analyzes sales data to identify trends and patterns.")
        button1 = st.button("View Project 1")
        if button1:
            st.markdown("[Analyzing Sales Data](https://github.com/username/project1)")

    # Project 2
    with st.expander("Housing Prices Analysis 🏠", expanded=False):
        st.image("images/housing_prices_image.jpg", use_column_width=True)
        st.write("This project explores housing prices data and performs exploratory data analysis.")
        button2 = st.button("View Project 2")
        if button2:
            st.markdown("[Exploratory Data Analysis of Housing Prices](https://github.com/username/project2)")

    # Project 3
    with st.expander("Twitter Sentiment Analysis 🐦", expanded=False):
        st.image("images/twitter_sentiment_image.jpg", use_column_width=True)
        st.write("This project analyzes sentiment in Twitter data using natural language processing techniques.")
        button3 = st.button("View Project 3")
        if button3:
            st.markdown("[Sentiment Analysis of Twitter Data](https://github.com/username/project3)")

# Call the function to display the content
display_data_analysis_projects()
