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
     summary_table2 = summary_table2.rename(
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
     import streamlit as st

st.set_page_config(page_title="Peru Minimum Temperature (Tmin) Raster Analysis", layout="wide")

tab1, tab2, tab3 = st.tabs(["Description", "Analysis & Visualizations", "Public policy"])

with tab1:
    st.markdown(
"""
# Description
The purpose of this application is to present a geospatial analysis of minimum temperature (Tmin) data across Peru using satellite-derived GeoTIFF raster layers. By calculating zonal statistics (mean, min, max, standard deviation, percentiles, etc.) for each district, we aim to:
- Identify cold zones with increased risk of frost and heat stress.
- Support public decision-making by highlighting vulnerable areas.
- Propose evidence-based policies for risk management and climate adaptation.

The analysis is built using Python, GeoPandas, raster statistics, and climate data.  
Our code is hosted in the following GitHub repository: [Minimum-Temperature-Raster](https://github.com/CarlaHL/Minimum-Temperature-Raster)
"""
    )

with tab2:
    st.markdown("# Analysis & Visualizations")

    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import streamlit.components.v1 as components

    st.subheader("Distribution of Mean Minimum Temperature by District")
    st.image("data/histogram_tmin_mean_total.png", use_container_width=True)

    st.subheader("Top 15 districts with lowest mean Tmin (frost risk)")
    summary_table1 = pd.read_csv("data/top15_lowest_tmin.csv")
    summary_table1 = summary_table1.rename(
        columns={"DISTRITO": "District", "tmin_mean_total": "Mean Minimum Temperature (°C)"}
    )
    st.dataframe(summary_table1)

    st.subheader("Top 15 districts with highest mean Tmin")
    summary_table2 = pd.read_csv("data/top15_highest_tmin.csv")
    summary_table2 = summary_table2.rename(
        columns={"DISTRITO": "District", "tmin_mean_total": "Mean Minimum Temperature (°C)"}
    )
    st.dataframe(summary_table2)

    st.subheader("Choropleth map")
    st.image("data/mapa_tmin_mean_total.png", use_container_width=True)

with tab3:
    st.markdown("# Public Policy Proposals")
    st.markdown(
"""
## **Propuesta de intervención de hotspots de riesgo por climas extremos**

Peru’s territorial heterogeneity exposes its population to opposite climatic extremes: districts such as **Capazo (−5.19 °C)**, **Susapaya (−5.15 °C)**, and **Tarata (−4.99 °C)** in the southern Andes experience recurrent frost, while Amazonian districts like **Yaguas**, **Morona**, and **Ramón Castilla** report average minimum temperatures above **22 °C**. These conditions demand targeted adaptation strategies that account for social vulnerability, infrastructure gaps, and the territorial logic of risk. The following proposals integrate health, housing, and production resilience under region-specific conditions.

---

### 1️⃣ **Thermal Security for High-Andean Households**

In the high Andean districts of Tacna, Puno, and Arequipa, frost exposure is both chronic and structural. Many households rely on adobe dwellings with poor insulation, and fuel poverty forces residents to burn wood or waste for heating, intensifying respiratory risks and deforestation.

**Objective:** Strengthen household thermal resilience and reduce health risks associated with subzero temperatures.  
**Target population:** Rural families and schools located in districts with Tmin ≤ −4 °C.  
**Intervention:** The program would scale up *Andean Thermal Housing Units (ATHU)*, building upon existing models like *Mi Abrigo* (FONCODES, 2018) but integrating community-managed retrofitting. Upgrades would use double-layer adobe walls, ichu insulation, and metallic or reflective roofing to retain heat. Improved biomass stoves with controlled ventilation would reduce indoor pollution. Each community would form “thermal brigades” responsible for maintenance and replication of local prototypes.  
**Estimated cost:** S/ 2,800 per unit (materials, stove, and training).  
**KPI's:**  
- −20 % acute respiratory infections (ARI) in MINSA reports  
- −15 % household biomass use  
- +10 % thermal comfort rating among beneficiaries  

---

### 2️⃣ **Frost-Resilient Agroecosystems**

Agriculture in high-altitude districts—mainly Puno, Cusco, and Arequipa—faces yield losses of up to 30 % in frost years (MINAGRI, 2022). Traditional mitigation, such as burning or smoke screens, provides little protection and increases emissions.

**Objective:** Reduce agricultural and livestock losses caused by extreme cold.  
**Target population:** Smallholder farmers and herders in frost-prone valleys and plateaus.  
**Intervention:** Introduce *Agroclimatic Protection Packages* consisting of low-cost thermal blankets, microtunnels for seedlings, and humidity-based irrigation timers. Livestock protection would rely on modular *corralones térmicos* insulated with local materials and plastic membranes. Additionally, a network of local *Frost Response Committees* would coordinate alerts based on SENAMHI early-warning data and facilitate community drills before frost peaks.  
**Estimated cost:** S/ 1,500 per farm unit.  
**KPI's:**  
- −25 % alpaca mortality rate  
- −15 % crop loss index in target districts  
- +10 % participation in community alert protocols  

---

### 3️⃣ **Heat Adaptation in the Amazon Basin**

In contrast, Amazonian districts such as **Yaguas** and **Morona** endure chronic thermal stress, with nighttime temperatures exceeding 22 °C and rising humidity above 80 %. These conditions worsen living and learning environments, especially in poorly ventilated wooden or tin-roofed buildings.

**Objective:** Reduce chronic heat exposure and its impacts on health, education, and productivity.  
**Target population:** Schools, clinics, and households in Loreto’s warmest districts (Tmin ≥ 22 °C).  
**Intervention:** Develop *Cool Communities Amazonía* — a territorial program combining passive cooling architecture and urban greening. Schools and clinics would install ventilated roofs, reflective coatings, and shaded corridors using local timber. Community reforestation belts with native species (*capirona*, *shihuahuaco*) would reduce surface temperatures and improve air circulation. Water access points and hydration areas would be integrated into public spaces to prevent heat exhaustion.  
**Estimated cost:** S/ 9,000 per public facility; S/ 1,000 per household retrofit.  
**KPI's:**  
- −15 % heat-related illness consultations  
- average −1.5 °C indoor temperature reduction  
- +8 % school attendance during heat peaks  

---
""", unsafe_allow_html=True)

