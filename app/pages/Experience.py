import streamlit as st

def projects_page():
    tab1, tab2 = st.tabs(["Professional Experience", "Personal Projects"])
    
    with tab1:
        st.header('Data Engineer at CNH Industrial')
        st.markdown("""
            **January 2023 - Current**
            - Drove the creation and management of batch and near real-time telemetry data pipelines, specializing in precision agriculture.
            - Collaborated on internal analytics initiatives to improve machinery performance through telemetry data analysis.
            """)

        st.header('Big Data Engineer at IBM')
        st.markdown("""
            **December 2021 - January 2023**
            - Key role in a machine learning project focused on reducing customer churn.
            - Acquired hands-on experience with a diverse range of technologies.
            """)
        
        st.header('Data Analyst at MG Info')
        st.markdown("""
            **August 2021 - December 2021**
            - Contributed to a global mining project, collaborating closely with teams in South Africa and India.
            """)

    with tab2:
        st.header('Healthcare Analysis Project')
        st.markdown("""
                - **Date:** November 2022
                - **Description:** Analyzed data from healthcare establishments in the state of São Paulo to identify trends and areas for improvement.
                - **More Information:** Click [Here](https://repositorio.unesp.br/items/e103fcd1-3a76-4495-9478-54cfde7ead99)
                """)
        
        st.header('Reinforcement Learning Project using C++')
        st.markdown("""
                - **Date:** November 2018
                - **Description:** Developed a Q-learning method for optimizing the decision-making process of a two-dimensional agent.
                - **More Information:** Click [Here](https://www.sorocaba.unesp.br/Home/Graduacao/EngenhariadeControleeAutomacao/mauricio/iv_mostra_robotica.pdf), page 288
                """)

if __name__ == '__main__':
    projects_page()
