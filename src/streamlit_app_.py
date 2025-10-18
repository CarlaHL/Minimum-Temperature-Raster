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

     st.subheader("Distribution of Mean Minimum Temperature by District")
     # Mostrar imagen PNG guardada
     st.image("data/histogram_tmin_mean_total.png", use_container_width=True,width=50)

     st.subheader("Top 15 districts with lowest mean Tmin (frost risk)")
     # Leer el DataFrame desde la carpeta data/
     summary_table1 = pd.read_csv("data/top15_lowest_tmin.csv")
     summary_table1 = summary_table1.rename(
          columns={"DISTRITO": "Distrito",
                   "tmin_mean_total": "Mean Minimum Temperature (°C)"
                  }
     )
     # Mostrar en tabla interactiva
     st.dataframe(summary_table1)

     st.subheader("Top 15 districts with highest mean Tmin")
     # Leer el DataFrame desde la carpeta data/
     summary_table2 = pd.read_csv("data/top15_highest_tmin.csv")
     summary_table2 = summary_table1.rename(
          columns={"DISTRITO": "Distrito",
                   "tmin_mean_total": "Mean Minimum Temperature (°C)"
                  }
     )
     # Mostrar en tabla interactiva
     st.dataframe(summary_table2)

     st.subheader("Choropleth map")
     # Mostrar imagen PNG guardada
     st.image("data/mapa_tmin_mean_total.png", use_container_width=True,width=50)

with tab3:
    st.markdown("# Public policy")
