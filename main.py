import streamlit as st
from PIL import Image

from streamlit_option_menu import option_menu
import home, helmet, invasion, abandonment, fall, fight, heirachy, reverse_driving, traffic_accident

icon = Image.open("assets/icon.png")
st.set_page_config(
    page_title="AI Convergence Lab",
    page_icon=icon,
    initial_sidebar_state="expanded",
    # layout="wide"
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
        st.markdown(
            """
            <style>
            .nav-link:hover {
                color: #00ADB5 !important;  /* Change hover text color */
                background-color: #393E46 !important;  /* Change hover background color */
            }
            </style>
            """, unsafe_allow_html=True
        )
        
        with st.sidebar:        
            app = option_menu(
                'Project Lists', ['Home','Helmet Detection','Property Invasion', 'Object Abandonemnt', 'Falling Detection', 
                         'Fighting Detection', 'Object Heirachy', 'Reverse Driving', 'Traffic Accident'],
                icons=['house-fill'],
                menu_icon="app-indicator",
                default_index=0,
                styles={
                    "menu-title": {"font-family": '"ui-sans-serif", "ui-sans-serif", "-apple-system", "system-ui", "Segoe UI"', "color": "#787878", "padding": "1rem", "text-align": "center", "font-weight": "bold"},
                    "icon": {"color": "#3FC1C9"},
                    "nav-link": {"color":"#252A34","font-size": "1rem", "text-align": "left", "margin":"0px", "--hover-color": "#F5F5F5", "padding": "0.7rem 1rem", "font-family": '"ui-sans-serif", "ui-sans-serif", "-apple-system", "system-ui", "Segoe UI"',},
                    "nav-link-selected": {"color":"white", "background-color": "#364F6B"},}
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
         