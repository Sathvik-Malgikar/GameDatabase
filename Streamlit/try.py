import streamlit as st


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
 
</style>
"""

st.markdown(page_bg_img , unsafe_allow_html=True)