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
    
    st.title("Gait and Motion Analysis Detection based on YOLOv8")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        The system is designed to analyze walking characteristics from video streams, focusing on movements such as head shaking, \
        head down posture, hand shaking, and waist bending angle. By combining advanced pose estimation techniques with detailed \
        gait analysis, the system extracts key metrics over time to identify unique walking patterns. These capabilities enable the \
        system to provide insights into movement behaviors, which can be useful in various applications such as security surveillance \
        or health monitoring. However, the current implementation has limitations, including a tendency for false detections. \
        To enhance reliability and stability, further refinements are needed, along with testing in diverse surveillance environments \
        to ensure consistent performance under different conditions.
        </p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv8, Temporal Data Analysis, Calculate Gait Metrics, Python")

    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        The system employs a multi-step process to analyze walking characteristics by combining pose estimation and gait analysis. \
        It begins by detecting the key points of relevant body parts in video frames, followed by the computation of various \
        gait metrics over time. These metrics are then analyzed to identify patterns in movement which provide insights into \
        walking behaviors. The detailed methodology is as follows:
        </p>
        
        <ol>
        <li>
            <strong>Pose Estimation</strong>: Use the YOLOv8 model to identify the 2D locations of key body parts from video frames.
        </li>
        <li>
            <strong>Gait Analysis</strong>: Compute metrics such as:
            <ul>
                <li><strong>Head Shake</strong>: Frequency and amplitude.</li>
                <li><strong>Arm Swing</strong>: Range and frequency for left and right arms.</li>
                <li><strong>Waist Bending</strong>: Trunk angle (hip-shoulder alignment relative to vertical).</li>
                <li><strong>Step Distance</strong>: Measurement of steps over time.</li>
            </ul>
        </li>
        <li>
            <strong>Pattern Detection</strong>: Analyze gait metrics to identify walking patterns like head shaking.
        </li>
        </ol>
    """
    
    st.write(method, unsafe_allow_html=True)
    st.image("assets/methods/11_gait detection.jpg", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/7EtSqIA_k4U")