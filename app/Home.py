import streamlit as st
from st_pages import Page,Section, show_pages, add_page_title

add_page_title()
print("Home.py rodando")
# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("Home.py", "About Me", "🙋‍♂️"),
        Page("pages/Experience.py", "Experience", "🛒"),
        Page("pages/Technical.py", "Tech Talk", "👨‍💻"),
    ]
)

# Texto destacando sua experiência e projetos
st.markdown("""
Hey there, data enthusiasts! I'm Caio Maximiano, a dedicated Data Engineer with a profound passion for turning complex data sets into actionable insights, innovative products, and strategic assets for businesses. Throughout my career, I've navigated the intricate realms of telemetry data in precision agriculture,ensured the availability of high-quality data for machine learning applications to mitigate customer churn in telecommunications, and contributed  to data-driven initiatives in the mining sector.

### My Expertise and Passion


**Data Products as Catalysts for Transformation:** My enthusiasm extends beyond traditional data engineering; I'm captivated by the potential of data products, from straightforward BI tools to sophisticated machine learning models. Each represents a unique opportunity for companies to elevate their decision-making, enhance operational efficiencies, and deliver unparalleled customer experiences.

### Core Technologies

My projects leverage a broad range of technologies across programming, cloud platforms, data processing, and more. Here's a quick look at my toolkit:

- **Programming:** Python, SQL
- **Cloud Platforms & Containerization:** Azure (Data Factory, Storage Accounts, Databricks), Informatica Cloud, Docker 
- **Data Management:** Cosmos DB, Oracle, SQL Server
- **DevOps & Collaboration:** Git, Azure DevOps
- **Visualization & BI:** Power BI, Streamlit
- **Architecture & Design:** Lakehouse Architecture, Data Modeling
- **Practices:** Object-Oriented Programming (OOP), Unit Testing

This concise toolkit enables me to address and solve complex data challenges effectively.

### Let's Connect and Make Data Work

I'm keen on connecting with like-minded individuals, innovators, and anyone passionate about the transformative power of data. Whether you're pondering over potential collaborations or simply wish to exchange ideas on the latest developments in data technology, don't hesitate to get in touch.

[🔗 LinkedIn Profile](https://www.linkedin.com/in/caio-maximiano/) | 📩 caiofcm97@gmail.com
            """)

# Adicionando uma imagem com uma legenda
st.image('images\\home_data_eng.jpg', 
         caption='Illustration by storyset on Freepik', 
         use_column_width=True)
