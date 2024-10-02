import streamlit as st

def app():
    st.title("Property Invasion Detection Using CCTV Video")
    st.header("Overview")
    st.write("Automated systems for detecting crimes significantly reduce crime rates and facilitate crime monitoring. \
        One type of crime that can be detected using these systems is property invasion, which occurs when an individual enters \
        another person's property without permission. With advancements in technology, it has become easier to detect property \
        invasions and other common crimes using machine learning or deep learning techniques. We utilize deep learning technology \
        (specifically, YOLOv5) to detect property invasions in CCTV videos. The system has demonstrated high performance in \
        detecting invasions within a predefined property area. This research is significant because it showcases the potential \
        of deep learning for property invasion detection, and its results can be utilized to assist property owners in preventing \
        such invasions more easily."
    )

    st.header("Technology Stack")
    st.write("YOLOv5, PyTorch, OpenVino, Python, C++")
  
    st.header("Methodology")
    st.write(
        "The system first begins by defining the property boundaries in two specific shapes: a regular rectangle or a polygon. \
        Following this, the YOLOv5 model is employed to identify human figures. The system then verifies whether the detected \
        figure is situated within the predetermined property boundaries."
    )
    st.image("assets/methods/2_invasion.png", width=700, caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/vdz6jGvpIj0")
    st.video("https://youtu.be/t_84DQZY2P4")
    st.video("https://youtu.be/3Wd3Bhrna6Q")