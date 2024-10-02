import streamlit as st

from streamlit_option_menu import option_menu
import home, helmet, invasion, abandonment, fall, fight, heirachy, reverse_driving, traffic_accident

st.set_page_config(
    page_title="Computer Vision Project Portfolio",
    page_icon="📊",
    initial_sidebar_state="expanded",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Project Highlights',
                options=['Home','Helmet Detection','Property Invasion', 'Object Abandonemnt', 'Falling Detection', 
                         'Fighting Detection', 'Object Heirachy', 'Reverse Driving', 'Traffic Accident'],
                default_index=0,
                styles={
        "nav-link": {"color":"#3C3D37","font-size": "1rem", "text-align": "left", "margin":"0px", "--hover-color": "#FCFAEE"},
        "nav-link-selected": {"color":"white", "background-color": "#507687"},}
                )

        if app == "Home":
            home.app()
        if app == "Helmet Detection":
            helmet.app()    
        if app == "Property Invasion":
            invasion.app()
        if app == "Object Abandonemnt":
            abandonment.app()
        if app == "Falling Detection":
            fall.app()
        if app == "Fighting Detection":
            fight.app()
        if app == "Object Heirachy":
            heirachy.app()
        if app == "Reverse Driving":
            reverse_driving.app()
        if app == "Traffic Accident":
            traffic_accident.app()
             
    run()            
         