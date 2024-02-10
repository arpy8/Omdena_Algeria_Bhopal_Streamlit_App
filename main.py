import base64
import pandas as pd
import streamlit as st

from config import *
from model import main as model_page 
from streamlit_option_menu import option_menu

def set_page_background(png_file):
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    bin_str = get_base64_of_bin_file(png_file)
    custom_css = f'''
        <style>
            .stApp {{
                background-image: url("data:image/png;base64,{bin_str}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: scroll;
            }}
            
            #MainMenu {{visibility: hidden;}}

            footer {{visibility: hidden;}}
            icon {{color: white;}}
            nav-link {{--hover-color: grey; }}
            nav-link-selected {{background-color: #4ABF7E;}}
        </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)


def home_page():
    left, mid, right = st.columns([2, 3, 1])
    with left, right:
        st.empty()
    with mid:
        st.image(IMG_OMDENA, width=170)
        
    st.write("<center><h1 style='font-size: 2.7rem;'>Water Management and Forecasting Project in Algeria & Bhopal<br><br></h1></center>", unsafe_allow_html=True)

    with st.expander("📜 **PROJECT PROBLEM**", expanded=True):
        st.write(PROJECT_PROBLEM)
    with st.expander("🎯 **PROJECT GOALS**", expanded=True):
        st.write(PROJECT_GOALS)
    with st.expander("📖 **PROJECT BACKGROUND**", expanded=True):
        st.write(PROJECT_BACKGROUND, unsafe_allow_html=True)
    with st.expander("📆 **PROJECT TIMELINE**", expanded=True):
        st.write(PROJECT_TIMELINE)

def overview_page():
    st.write("<center><h1>Project Overview</h1></center>", unsafe_allow_html=True)
    
    algeria_dataframe = pd.read_csv(ALGERIA_DATASET)
    bhopal_dataframe = pd.read_csv(BHOPAL_DATASET)
    
    st.write(OVERVIEW_PHASE1)
    with st.expander("**A) Algeria Dataset**"):
        st.dataframe(algeria_dataframe, use_container_width=True)
    with st.expander("**B) Bhopal Dataset**"):
        st.dataframe(bhopal_dataframe, use_container_width=True)
    
    st.write(OVERVIEW_PHASE2)
    st.write(OVERVIEW_PHASE3)
    st.write(OVERVIEW_PHASE4)
    st.write(OVERVIEW_PHASE5)
    

def main():
    
    css_style = {
        "icon": {"color": "white"},
        "nav-link": {"--hover-color": "grey"},
        "nav-link-selected": {"background-color": "#232fac"},   
    }

    st.set_page_config(
        page_title=f"Omdena Algeria & Bhopal Chapter",
        page_icon="💦",
        initial_sidebar_state="expanded"
    )

    set_page_background(IMG_BACKGROUND)
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.image(IMG_BANNER2, width=280)
        st.write(SIDEBAR_TEXT_1, unsafe_allow_html=True)
        selected_task = option_menu(
            menu_title=None,    
            options=["Home Page", "Project Overview", "Developed Model", "Contributors"],
            icons=["house", "info-circle", "gear", "people"],
            styles=css_style
        )
        st.write(SIDEBAR_TEXT_2, unsafe_allow_html=True)
    
    
    if selected_task == "Home Page":
        home_page()
    elif selected_task == "Project Overview":
        overview_page()
    elif selected_task == "Developed Model":
        model_page()
    elif selected_task == "Contributors":
        st.balloons()
        st.write(CONTRIBUTORS, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()