import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc
from streamlit_extras.tags import tagger_component
from utils.utils import read_json

st.set_page_config(
    page_title='My Projects',
    layout='wide',
    initial_sidebar_state="expanded"
)

projects = read_json('projects.json')


for idx, p in enumerate(projects):
    #st.markdown('<br>', unsafe_allow_html=True)
    with sc(key=f'pro_{idx}', css_styles=["""div[data-testid="stHorizontalBlock"]:first-of-type {
                                        border: 1px solid #737373;
                                        border-radius: 20px;
                                        padding:15px;
                                        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    }
    """]):
        with st.container():
            
            text_col, image_col = st.columns(2, gap='large', vertical_alignment='center')

            with text_col:
                st.markdown(f"# {p['name']}")
                tagger_component(
                    content='',
                    tags=p['tags']
                )
                st.markdown(p['description'])
                st.link_button(p['button_label'], url=p['url'])

            with image_col:
                media = p['media']
                if media['type'] == 'image':
                    st.image(media['path'])
                else:
                    st.video(media['path'], loop=True, autoplay=True)

        