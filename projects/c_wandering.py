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
    
    st.title("Wandering Detection in Predefined Areas: A Temporal Tracking Solution")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        This project focuses on developing a wandering detection system that monitors individuals when entering predefined \
        areas and tracks the duration of their presence. While intrusion detection systems primarily detect unauthorized entries, \
        wandering detection systems add an important layer by maintaining the time spent within these areas. This capability is \
        critical for applications in healthcare, security, and other industries where prolonged presence in restricted or sensitive \
        zones could indicate potential concerns.</p>
        
        <p class="font txtAlign">
        The system is designed to provide real-time monitoring, ensuring accurate detection and tracking of individuals. \
        By integrating state-of-the-art object detection and tracking technologies, this solution aims to offer a reliable and \
        scalable method for identifying wandering behavior and providing actionable insights.</p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv5, ByteTrack, PyTorch, OpenVino, Python, C++")

    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        The wandering detection system employs a three-step approach. The system first uses YOLOv5, a high-performance object detection \
        model, to identify individuals in video frames. It processes real-time footage, detecting the location and class of \
        objects with high precision. Then, ByteTrack, a robust multi-object tracking algorithm, is integrated to track the movement \
        of detected individuals across frames. This ensures continuous monitoring and assigns unique IDs to each person, enabling \
        the system to follow their trajectories seamlessly. After tracking, the system evaluates the duration of each individual’s \
        presence within the predefined area. By maintaining time data, it differentiates wandering from regular movement and flags instances where the time exceeds \
        a set threshold.</p>
    """
    st.write(method, unsafe_allow_html=True)
    st.image("assets/methods/2_wandering.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/6iDX1L0_1Oo")