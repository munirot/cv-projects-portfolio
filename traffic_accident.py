import streamlit as st

def app():
    st.title("Traffic Collisions Detection using YOLOv8 and LSTM to Enchance Road Safety")
    st.header("Overview")
    st.write(
        "This reserach project presents a deep learning-based method that utilizes YOLOv8 and advanced computer vision techniques to \
        detect vehicle collisions in real-time from CCTV traffic video feeds. The objective is to develop a highly responsive system \
        that can promptly identify potential collisions, thereby enhancing emergency response times and reducing the overall impact \
        of accidents. "
    )
    st.write(
        "Our approach enables the system to visualize detected collisions through OpenCV, offering an intuitive representation of \
        accident scenarios. By integrating spatial-temporal analysis with deep learning, the method provides robust and real-time \
        collision detection, which can significantly improve emergency response efficiency and contribute to minimizing casualties \
        and property damage. Furthermore, the system has the potential to provide valuable insights for accident prevention and traffic \
        safety management, making it a critical tool for urban safety initiatives."
    )

    st.header("Technology Stack")
    st.write("YOLOv8, OpenCV, LSTM, Python, C++")

    st.header("Methodology")
    st.write("The system processes real-time video footage obtained from CCTV cameras. Video frames are preprocessed using OpenCV, \
        and vehicles and pedestrians are detected in each frame using the YOLOv8 object detection model. Key features such as object \
        class, frame number, and coordinates are extracted and organized into sequences for further analysis. These sequences are then \
        fed into a Long Short-Term Memory (LSTM) model, which analyzes spatial and temporal patterns to accurately identify potential \
        collisions."
    )
    st.image("assets/methods/8_traffic.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/_jyfUuf2Urc?si=vWrQjSl2pVjcQS4v")
    st.video("https://youtu.be/Dv-30_JqMcM?si=GLrJPvKa_jNIwEcw")
    st.video("https://youtu.be/1Oackr2rRtM?si=E6d-sEYPINcP7hyt")
    st.video("https://youtu.be/As5NbrrO0zA?si=SZukIEt5Q-aIC0mc")