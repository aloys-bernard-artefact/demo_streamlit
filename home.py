import streamlit as st  

st.set_page_config(page_title="My first Streamlit app"
               , page_icon=":smiley:")   

# Title
st.markdown("# My first Streamlit app")
st.markdown(f'Hello {st.secrets["name"]}')

# Sidebar
st.sidebar.success("This is a sidebar")
st.sidebar.markdown("## Sidebar")

if st.button("Click me"):
    st.write("You clicked me!")
    st.balloons()
    st.snow()
    
st.write("This is a Streamlit app")

#st.write(df)
