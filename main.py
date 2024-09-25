import streamlit as st

from streamlit_option_menu import option_menu
import home, helmet, invasion, abandonment, fall, fight


st.set_page_config(
        page_title="Project Highlight",
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
                options=['Home','Helmet Detection','Property Invasion', 'Object Abandonemnt', 'Falling Detection', 'Fighting Detection'],
                menu_icon='chat-text-fill',
                default_index=1               
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
            
             
          
             
    run()            
         