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
    print(start_date, end_date)
    total_months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month

    years = total_months // 12
    months = total_months % 12
    return f"{years} years {months} months"

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
        st.image(osp.join('images', 'home', 'profile_picture2.png'), width=300)

with presentation_col:
    st.title("Edoardo Marchetti", anchor=False)
    st.write(
        "Graduated in **Data science and Engineering at the Polytechnic of Turin** 📊. Sports enthusiast 🏆. I love to realize projects that allows me to combine the sporting world with my academic background through data analysis and AI 🤖. Visit 'My projects' page to discover what I realized and feel free to contact me 😉"
    )
    st.write("📧 edoardomarchetti2@gmail.com")

    
    
    github_mention= mention(
            label='',
            url='https://github.com/EdoardoMarchetti',
            icon='github',
            write=False
        )



    # Define the image path and the URL
    image_path = osp.join('images', 'home', 'LI-In-Bug.png')
    linkedin_url = 'https://www.linkedin.com/in/edoardo-marchetti-907a2917a/'

    # Convert the image to base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Get the base64 string
    base64_image = get_base64_image(image_path)

    # Create the HTML for the clickable image
    html = f'{github_mention} <a href="{linkedin_url}" target="_blank"><img src="data:image/png;base64,{base64_image}" width="25"></a>'

    # Display the HTML in Streamlit
    st.write(html, unsafe_allow_html=True)

st.markdown('<br><br><br><br><br>', unsafe_allow_html=True)



st.markdown('## 🧑🏻‍💼 Working Experience')

work_experince = read_json(osp.join('working_experience.json'))

# Sort the list
work_experince = sort_by_dates(work_experince)

for we in work_experince:
    st.markdown('<br>', unsafe_allow_html=True)
    img_col, text_col = st.columns([0.1,0.9], gap='medium')

    with img_col:
        st.image(we['media']['path'])
    
    with text_col:
        start_transformed = transform_date(we['start'])
        end_transformed = transform_date(we['end'])
        we['display_period'] = f"{start_transformed} - {end_transformed}"

        duration = compute_duration(we['start'], we['end'])

        st.markdown(f"<span style='color:{LIGHT_GRAY}; font-weight:bold; white-space: pre;'>{we['company']}</span>  |   <span style='color:{LIGHT_GRAY};'>{we['display_period']} ({duration})</span>", unsafe_allow_html=True)
        st.markdown(f"### {we['name']}")
        st.markdown(f"{we['description']}")
        if we['hard_skills']:
            st.markdown(f"**Hard skills** : {', '.join(we['hard_skills'])}")
        if we['soft_skills']:
            st.markdown(f"**Soft skills** : {', '.join(we['soft_skills'])}")
        if we['related_projects']:
            st.markdown(f"**Related Projects** : {', '.join(we['related_projects'])}")
        
        st.markdown("<br>", unsafe_allow_html=True)


    


    
