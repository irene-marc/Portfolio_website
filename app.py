import streamlit as st


pages = [
    st.Page("pages_script/home_page.py", title="About Me", icon="🏠"),
    st.Page("pages_script/projects.py", title="My Projects", icon="🧪"),
]
    
pg = st.navigation(pages)

pg.run()