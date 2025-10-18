import streamlit as st

st.set_page_config(page_title="Geospatial Analysis of Hospitals in Peru", layout="wide")

tab1, tab2, tab3 = st.tabs(["Data Desctription", "Static Maps & Department Analysis", "Dynamic Maps"])

with tab1:

     st.markdown(
"""
# Data Desctription
The purpose of this application is to present a geospatial analysis of hospitals in Peru, both at the departmental level and at the population center level. Through this visualization, we aim to identify patterns in their geographic distribution as well as potential gaps in access to healthcare services.


Our code is hosted in the following GithHub repository: https://github.com/CarlaHL/Hospitals-Access-Peru
"""
     )

with tab2:
     st.markdown("# Static Maps & Department Analysis")
    
     import streamlit as st
     import matplotlib.pyplot as plt
     import seaborn as sns
     import pandas as pd
     import streamlit.components.v1 as components   

     st.subheader("Distribution of hospitals across departments")
     # Leer el DataFrame desde la carpeta data/
     summary_table = pd.read_csv("data/summary_table.csv")
     summary_table = summary_table.rename(
          columns={"Departamento": "Department",
                   "n_hospitals_dept": "Number of Hospitals"
                  }
     )
     # Mostrar en tabla interactiva
     st.dataframe(summary_table)

     # Mostrar imagen PNG guardada
     st.image("assets/hospitals_dept_bars.png", use_container_width=True,width=50)

     st.subheader("Geospatial distribution of hospitals by departments")
     st.image("assets/hospitals_dept_map.png", use_container_width=True)

with tab3:
    st.markdown("# Dynamic Maps")
    st.subheader("Lima")
    with open("assets/mapa_lima.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600)

    st.subheader("Loreto")
    with open("assets/mapa_loreto.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600)

