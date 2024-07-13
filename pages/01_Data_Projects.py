import streamlit as st


def display_data_analysis_projects():
    st.title("Data Analysis Projects")

    st.write("Here are some of my data analysis projects:")

    # Project 1
    with st.expander("Video Games Sales Analysis 📈", expanded=False):
        st.image("images/sales.png", use_column_width=True)
        st.write("This project aims to analyse sales data of video games from various genres and platforms, spanning"
                 " multiple years. By leveraging data analysis techniques and visualization tools, we uncover trends "
                 "and insights into the video game industry's performance.")

        button1 = st.button("View Project ")
        if button1:
            st.markdown("[Analyzing Sales Data](https://www.kaggle.com/code/fahadfhs/games-sales-analysis)")
            st.markdown("[Tableau Visualization](https://public.tableau.com/app/profile/fahad.shaikh3307/viz"
                        "/VideoGamessalesanalysis/Top25PublisherswiththeGlobalSales)")

    # Project 2
    with st.expander("Data Science Salary Analysis", expanded=False):
        st.image("images/salaries.png", use_column_width=True)
        st.write("This project examines salary trends across Data Science industries from 2020 to 2024. By analyzing "
                 "data on compensation, we identify key patterns and insights that can inform career planning and "
                 "industry benchmarking.")
        button3 = st.button("View Project 2")
        if button3:
            st.markdown("[Analyzing Salary Data](https://www.kaggle.com/code/fahadfhs/data-analysis-salaries-analysis"
                        "-2020-2024)")

    # Project 3


# Call the function to display the content
display_data_analysis_projects()
