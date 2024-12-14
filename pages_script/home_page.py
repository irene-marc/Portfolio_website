import base64
from datetime import datetime
import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc
from streamlit_extras.tags import tagger_component
from utils.utils import read_json
import os 
import os.path as osp
from streamlit_extras.mention import mention
from utils.colors import *



st.set_page_config(
    page_title='Home',
    initial_sidebar_state="expanded"
)

def transform_date(date_str):
    if date_str == '-':
        return 'Present'
    else:
        date_obj = datetime.strptime(date_str, "%m/%y")
        return date_obj.strftime("%B  %y")
    
# Function to convert date strings to datetime objects for sorting
def parse_date(date_str):
    if date_str == '-' or date_str.lower() == 'present':
        return datetime.today()  # Treat 'Present' as the most recent date
    return datetime.strptime(date_str, "%m/%y")

# Function to sort the list of dictionaries
def sort_by_dates(dicts):
    return sorted(dicts, key=lambda x: (parse_date(x['end']), parse_date(x['start'])), reverse=True)

# Function to compute the difference in years and months
def compute_duration(start_str, end_str):
    start_date = parse_date(start_str)
    end_date = parse_date(end_str)
    total_months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month

    years = total_months // 12
    months = total_months % 12
    return f"{years} years {months} months"

# Convert the image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#MARK: Hero

image_hero_col, presentation_col = st.columns(2, gap='large', vertical_alignment='center')

with image_hero_col:
    with sc(key='profile', css_styles=["""img{
                                            border: 1px solid #335384;
                                            border-radius: 50%;
                                            margin-left:auto;
                                            margin-right:auto;
                                        }""",
                                        """
                                        div[data-testid="stImage"]{
                                            margin:auto;
                                            border: 1px solid #335384;
                                            border-radius: 50%;
                                            margin-left:auto;
                                            margin-right:auto;
                                            box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
                                        }
                                        """]):
        st.image(osp.join('images', 'home', 'fotocv.jpg'), width=300)

with presentation_col:
    st.title("Irene Marchetti", anchor=False)
    st.write("Ho 20 anni e sono una studentessa di Digital Marketing. Il mio obiettivo è continuare a lavorare nel settore del marketing digitale, con un particolare interesse per l'analisi dei dati. Sono entusiasta di applicare le mie conoscenze e competenze universitarie in un ambito professionale. Credo sia un ambito dove posso combinare la mia passione per il marketing con il mio interesse per questi settori dinamici e in continua evoluzione.   ")

    
    
    github_mention= mention(
            label='',
            url='https://github.com/EdoardoMarchetti',
            icon='github',
            write=False
        )
    
    external_pages = read_json(osp.join('external_links.json'))
    ep_cols = st.columns(8)

    for (i,ep) in enumerate(external_pages):
        with ep_cols[i]:
            # Get the base64 string
            base64_image = get_base64_image(ep['icon'])

            # Create the HTML for the clickable image
            html = f'<a href="{ep["url"]}" target="_blank"><img src="data:image/png;base64,{base64_image}" width="100"></a>'

            # Display the HTML in Streamlit
            st.write(html, unsafe_allow_html=True)                                                                      



    



##MARK: WORK
st.markdown('<br><br><br><br><br>', unsafe_allow_html=True)
st.markdown('## 👩🏻‍💼 Working Experience')

work_experince = read_json(osp.join('working_experience.json'))

# Sort the list
work_experince = sort_by_dates(work_experince)

for i, we in enumerate(work_experince):
    #st.markdown('<br>', unsafe_allow_html=True)
    with sc(key=f'exp_{i}', css_styles=["""div[data-testid="stHorizontalBlock"]:first-of-type {
                                        border: 1px solid #335384;
                                        border-radius: 20px;
                                        padding:15px;
                                        padding-top:30px;
                                        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    }
    """]):
        with st.container():
            img_col, text_col = st.columns([0.1,0.9], gap='medium', vertical_alignment='top')

            with img_col:
                with sc(key=f'exp_img_{i}', css_styles=["""img{
                                        margin-top:15px;                                        
                }
                """]):
                    st.image(we['media']['path'])
            
            with text_col:
                start_transformed = transform_date(we['start'])
                end_transformed = transform_date(we['end'])
                we['display_period'] = f"{start_transformed} - {end_transformed}"

                duration = compute_duration(we['start'], we['end'])

                st.markdown(f"<span style='color:{LIGHT_GRAY}; font-weight:bold; white-space: pre;'>{we['company']}</span>  |   <span style='color:{LIGHT_GRAY};'>{we['display_period']} ({duration})</span>", unsafe_allow_html=True)
                st.markdown(f"### {we['name']}")
                st.markdown(f"{we['description']}", unsafe_allow_html=True)
                if len(we['hard_skills']) > 0:
                    st.markdown(f"**Hard skills** : {', '.join(we['hard_skills'])}", unsafe_allow_html=True)
                if len(we['soft_skills']) > 0:
                    st.markdown(f"**Soft skills** : {', '.join(we['soft_skills'])}", unsafe_allow_html=True)
                if len(we['related_projects']) > 0:
                    st.markdown(f"**Related Projects** : {', '.join(we['related_projects'])}", unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)


st.markdown('<br><br><br><br><br>', unsafe_allow_html=True)
st.markdown('## 🧑‍🎓 Education')

education = read_json(osp.join('education.json'))

# Sort the list
education = sort_by_dates(education)

for i, e in enumerate(education):
    #st.markdown('<br>', unsafe_allow_html=True)
    with sc(key=f'e_{i}', css_styles=["""div[data-testid="stHorizontalBlock"]:first-of-type {
                                        border: 1px solid #335384;
                                        border-radius: 20px;
                                        padding:15px;
                                        padding-top:30px;
                                        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    }
    """]):
        with st.container():
            img_col, text_col = st.columns([0.1,0.9], gap='medium', vertical_alignment='top')

            with img_col:
                with sc(key=f'exp_img_{i}', css_styles=["""img{
                                        margin-top:15px;                                        
                }
                """]):
                    st.image(e['media']['path'])
            
            with text_col:
                start_transformed = transform_date(e['start'])
                end_transformed = transform_date(e['end'])
                e['display_period'] = f"{start_transformed} - {end_transformed}"

                duration = compute_duration(e['start'], e['end'])

                string_to_show = []
                institution_string = f"<span style='color:{LIGHT_GRAY}; font-weight:bold; white-space: pre;'>{e['institution']}</span>"
                string_to_show.append(institution_string)
                grade = e.get('grade', '')
                if grade in e:
                    grade_string =  f"<span style='color:{LIGHT_GRAY};'>Grade: {grade}"
                    string_to_show.append(grade_string)
                display_period_string = f" </span>  <span style='color:{LIGHT_GRAY};'>{e['display_period']} </span>"
                string_to_show.append(display_period_string)

                st.markdown(' | '.join(string_to_show), unsafe_allow_html=True)
                st.markdown(f"### {e['name']}")
                st.markdown(f"{e['description']}")
                thesis_title = e.get('thesis', '')
                if thesis_title in e:
                    st.markdown(f"**Thesis title** {thesis_title}")
                
                
                st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<br><br><br><br><br>', unsafe_allow_html=True)
st.markdown('## Extra Learning')

extra_learning = read_json(osp.join('extra_learning.json'))

# Sort the list
extra_learning = sort_by_dates(extra_learning)


for i, e in enumerate(extra_learning):
    #st.markdown('<br>', unsafe_allow_html=True)
    with sc(key=f'el_{i}', css_styles=["""div[data-testid="stHorizontalBlock"]:first-of-type {
                                        border: 1px solid #335384;
                                        border-radius: 20px;
                                        padding:15px;
                                        padding-top:30px;
                                        box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    }
    """]):
        with st.container():
            img_col, text_col = st.columns([0.1,0.9], gap='medium', vertical_alignment='top')

            with img_col:
                with sc(key=f'exp_img_{i}', css_styles=["""img{
                                        margin-top:15px;                                        
                }
                """]):
                    st.image(e['media']['path'])
            
            with text_col:
                start_transformed = transform_date(e['start'])
                end_transformed = transform_date(e['end'])
                e['display_period'] = f"{start_transformed} - {end_transformed}"

                st.markdown(f"<span style='color:{LIGHT_GRAY}; font-weight:bold; white-space: pre;'>{e['institution']}</span> | <span style='color:{LIGHT_GRAY};'>{e['display_period']} </span> ", unsafe_allow_html=True)
                st.markdown(f"### {e['name']}")
                st.markdown(f"{e['description']}")
                if e['project']:
                    st.markdown(f"**Project** {e['project']}")
                if e.get('url', ''):
                    st.link_button('Certification', url=e['url'])
                
                
                st.markdown("<br>", unsafe_allow_html=True)


    


    

