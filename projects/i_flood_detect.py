import streamlit as st

def app():
    st.markdown(""" <style> 
                .font {
                    font-family: "ui-sans-serif", "-apple-system", "system-ui", "Segoe UI";
                }
                
                .txtAlign {
                    text-align: justify;
                }
        </style> """, unsafe_allow_html=True)
    
    st.title("Automated Flood Detection Using Vitual Height Basedline and Segmentation")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        Flood detection involves using a virtual height measurement as a baseline to assess the risk of rising water levels that could \
        impact areas of interest, such as urban cities, canals, and dams. The water surface is monitored, and as it reaches each level \
        of the virtual baseline, alerts are generated to help us take preventive action against potential flooding.</p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv8 Segmentation Model, OpenCV, Python, C++")

    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        This figure depicts a workflow for an automated flood detection and alerting system using computer vision and the YOLO \
        segmentation model. The process begins with CCTV cameras monitoring a designated detection area, such as a river, canal, \
        or other water body at risk of flooding. A virtual height baseline is established to measure water levels, serving as a \
        reference to assess risk as water levels approach critical points. Frames from the CCTV feed are then extracted in real-time, \
        capturing snapshots of the water surface. These frames are processed by the YOLO segmentation model to detect and segment \
        the water surface area, identifying the extent of water coverage within each frame.
        </p>
        
        <p class="font txtAlign">
        The segmented images are analyzed to assess the current water level relative to the virtual baseline. This allows for \
        continuous, real-time monitoring of the water level, enabling the system to identify any critical increases that may signal \
        a flood risk. If the water level reaches predetermined thresholds, an alerting system is activated, notifying relevant \
        personnel to take preventative action. This workflow provides a streamlined, automated solution for flood detection, helping \
        to manage and mitigate flood risks in urban areas and other vulnerable locations.
        </p>
    """
    st.write(method, unsafe_allow_html=True)
    st.image("assets/methods/9_flood_detection.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/h08FiHM5X4k?si=Oi8OBmuuzkReTJA4")