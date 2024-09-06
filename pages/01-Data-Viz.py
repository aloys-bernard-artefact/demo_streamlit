import streamlit as st
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="DATA VIZ TITLE"
                   , page_icon=":bar_chart:")  


if not "df" in st.session_state:
    data = load_iris(as_frame=True)
    print(f" {datetime.now()} - Data loaded")
    st.session_state["df"] = data.frame
    
    


# Magic button
if st.button("Click me"):
    st.write("You clicked me!")
    st.snow()

# Plots
st.write("## Plots")
st.write("### Histogram Seaborn")
sns.histplot(st.session_state["df"]["sepal length (cm)"])
st.pyplot(plt)



st.write("### Scatter plot Matplotlib")
plt.scatter(st.session_state["df"]["sepal length (cm)"], st.session_state["df"]["sepal width (cm)"])
st.pyplot(plt)

st.write("### Pairplot Seaborn")
st.pyplot(sns.pairplot(st.session_state["df"], hue="target"))
