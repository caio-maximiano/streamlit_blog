import streamlit as st

def projects_page():
    tab1, tab2 = st.tabs(["Professional Experience", "Personal Projects"])
    
    with tab1:
        st.header('Data Engineer at CNH Industrial')
        st.markdown("""
            * **Company:** CNH Industrial
            * **Location:** Sorocaba, SP, BRA
            * **Dates:** January 2023 - Current
            * **Description:** Drove the creation and management of batch and near real-time telemetry data pipelines as a Data Engineer specializing in precision agriculture. Collaborated on internal analytics initiatives to improve machinery performance through the analysis of telemetry data.
            """)

        st.header('Big Data Engineer at IBM')
        st.markdown("""
            * **Company:** IBM
            * **Location:** São Paulo, SP, BRA
            * **Dates:** December 2021 - January 2023
            * **Description:** Played a key role in a machine learning project focused on reducing customer churn. Acquired hands-on experience with a diverse range of technologies.
            """)
        
        st.header('Data Analyst at MG Info')
        st.markdown("""
            * **Company:** MG Info
            * **Location:** Belo Horizonte, MG, BRA
            * **Dates:** August 2021 - December 2021
            * **Description:** Contributed as a Data Analyst to a global mining project, collaborating closely with teams in South Africa and India.
            """)

    with tab2:
        st.header('Reinforcement Learning Project')
        st.markdown("""
                * **Description:** Q-learning method for optimizing decision-making of a two-dimensional agent.
                * **Date:** November 2018
                """)

        st.header('Healthcare Analysis Project')
        st.markdown("""
                * **Description:** Analyzing data from healthcare establishments in the state of São Paulo.
                * **Date:** November 2021
                """)

if __name__ == '__main__':
    projects_page()
