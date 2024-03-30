import streamlit as st

def projects_page():
    tab1, tab2 = st.tabs(["Professional Experience", "Personal Projects"])
    
    with tab1:
        st.header('Data Engineer at CNH Industrial')
        st.markdown("""
            **January 2023 - Current**
            - Drove the creation and management of batch and near real-time telemetry data pipelines as a Data Engineer specializing in precision agriculture at CNH Industrial. These pipelines catered to end-users and involved intricate transformations and aggregations across different layers within the lakehouse architecture.
            - Collaborated on internal analytics initiatives to improve machinery performance through the analysis of telemetry data. Leveraged data science principles to derive valuable insights and contribute to ongoing enhancements.
            """)

        st.header('Big Data Engineer at IBM')
        st.markdown("""
            **December 2021 - January 2023**
            - Played a key role in a machine learning project focused on reducing customer churn as a Data Engineer in the telecommunications industry at IBM. Responsibilities included creating tables that fueled the recommendation engine maintained by the data science team, ultimately optimizing customer recommendations.
            - Acquired hands-on experience with a diverse range of technologies, including Cloudera Data Platform, Azure Data Factory, Azure Data Lake Storage, Databricks, HDFS, Informatica Cloud, and Oracle Database, demonstrating versatility in managing data infrastructure.
            """)
        
        st.header('Data Analyst at MG Info')
        st.markdown("""
            **August 2021 - December 2021**
            - Contributed as a Data Analyst to a global mining project at MG Info, collaborating closely with teams in South Africa and India. Played a key role in testing the data pipeline developed by the Indian team, ensuring its seamless integration and validation for systems destined for Azure Data Lake Storage.
            - Utilized Azure Databricks to meticulously verify data flow, model relationships, and maintain the accuracy of dashboards in alignment with the source system data. This involved active participation in cross-functional efforts to uphold data quality and consistency.
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
