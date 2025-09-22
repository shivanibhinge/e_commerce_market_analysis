import streamlit as st
import pandas as pd

# Define the data for team members
team_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Role': ['Project Manager', 'Data Scientist', 'Developer'],
    'Contribution': ['Managed project timelines', 'Developed analysis models', 'Built the website'],
    'Picture': [
        'https://via.placeholder.com/150/FF5733/FFFFFF?text=Alice',
        'https://via.placeholder.com/150/33FF57/FFFFFF?text=Bob',
        'https://via.placeholder.com/150/5733FF/FFFFFF?text=Charlie'
    ]
}

# Create a DataFrame
df_team = pd.DataFrame(team_data)

st.set_page_config(layout="wide")

st.title("Retail Stores Analysis")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Introduction", "Team", "Overview"])

with tab1:
    st.header("Introduction")
    st.write(
        """
        Welcome to the Retail Stores Analysis project. This initiative aims to provide
        in-depth insights into retail store performance across various countries.
        Our analysis covers key metrics such as sales trends, customer demographics,
        and market share to help businesses make data-driven decisions.
        """
    )
    st.write(
        """
        The project utilizes a comprehensive dataset that includes information from
        retail chains in the United States, United Kingdom, and Japan. By examining
        these different markets, we can identify regional trends and opportunities
        for growth.
        """
    )

with tab2:
    st.header("Team Members")
    st.write("Meet the talented individuals behind this project.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(df_team.loc[0, 'Name'])
        st.image(df_team.loc[0, 'Picture'], width=150)
        st.markdown(f"**Role:** {df_team.loc[0, 'Role']}")
        st.markdown(f"**Contribution:** {df_team.loc[0, 'Contribution']}")

    with col2:
        st.subheader(df_team.loc[1, 'Name'])
        st.image(df_team.loc[1, 'Picture'], width=150)
        st.markdown(f"**Role:** {df_team.loc[1, 'Role']}")
        st.markdown(f"**Contribution:** {df_team.loc[1, 'Contribution']}")

    with col3:
        st.subheader(df_team.loc[2, 'Name'])
        st.image(df_team.loc[2, 'Picture'], width=150)
        st.markdown(f"**Role:** {df_team.loc[2, 'Role']}")
        st.markdown(f"**Contribution:** {df_team.loc[2, 'Contribution']}")

with tab3:
    st.header("Project Overview")
    st.markdown(
        """
        The **Retail Stores Analysis** project is a comprehensive study of the retail
        sector, with a focus on multinational operations. Our primary goal is to
        provide a clear and concise summary of our findings.

        ### Key Project Highlights:
        * **Data Collection:** Sourced data from over 500 retail stores across three continents.
        * **Analytical Models:** Developed machine learning models to predict sales performance.
        * **Visualization:** Created interactive dashboards to visualize key performance indicators (KPIs).
        * **Geographic Focus:** Analyzed retail trends in the US, UK, and Japan to identify market-specific strategies.

        Our analysis shows a strong correlation between localized marketing efforts and sales growth in all three countries.
        """
    )

