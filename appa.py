import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Análisis de eficiencia logística")

uploaded_file = st.file_uploader("Sube tu archivo Excel con datos", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    st.write("Datos cargados:")
    st.dataframe(df.head())

    # Ejemplo: gráfica simple de entregas por zona
    if 'zona' in df.columns and 'n_entregas' in df.columns:
        fig, ax = plt.subplots()
        sns.barplot(data=df, x='zona', y='n_entregas', ax=ax)
        ax.set_title('Número de entregas por zona')
        st.pyplot(fig)
    else:
        st.warning("Tu archivo debe tener columnas 'zona' y 'n_entregas' para mostrar la gráfica.")