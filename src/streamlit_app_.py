import streamlit as st

st.set_page_config(page_title="Peru Minimum Temperature (Tmin) Raster Analysis", layout="wide")

tab1, tab2, tab3 = st.tabs(["Desctription", "Analysis & Visualizations", "Public policy"])

with tab1:

     st.markdown(
"""
# Desctription
The purpose of this application is to present a geospatial analysis of minimum temperature (Tmin) data across Peru using satellite-derived GeoTIFF raster layers. By calculating zonal statistics (mean, min, max, standard deviation, percentiles, etc.) for each district, we aim to:
- Identify cold zones with increased risk of frost and cold surges.
- Support public decision-making by highlighting vulnerable areas.
- Propose evidence-based policies for risk management and climate adaptation.

The analysis is built using Python, GeoPandas, raster statistics, and climate data. 
Our code is hosted in the following GithHub repository: https://github.com/CarlaHL/Minimum-Temperature-Raster
"""
     )

with tab2:
     st.markdown("# Analysis & Visualizations")
    
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
    st.markdown("# Public policy")
