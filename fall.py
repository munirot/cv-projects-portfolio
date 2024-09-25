import streamlit as st

def app():
    st.title("Fall Detection Using Pose Angle Analysis with Machine Learning Classifiers")
    st.header("Overview")
    st.write(
        "Fall detection is an important area of focus in healthcare and assisted living technologies, especially as the global \
        population ages, resulting in an increased incidence of falls among older adults. Traditional fall detection methods, \
        such as manual observation or wearable sensors, have limitations in terms of scalability and accuracy. To address these issues, \
        this study proposes a novel machine-learning framework for improving fall detection from CCTV camera footage. The framework \
        uses YOLOv8, a deep learning model, to detect and track people's movements and poses in real time. After preprocessing the data, \
        various machine learning classifiers were used to differentiate between standing and lying positions. By leveraging geometric \
        data analysis, the proposed system offers a comprehensive approach to fall detection, facilitating early intervention and \
        improved patient outcomes."
    )

    st.header("Technology Stack")
    st.write("YOLOv8, Machine Learning Classifier, PyTorch, OpenVino, Python, C++")
    
    st.header("Dataset and Labeling Guideline")
    st.write("We collected data from the internet and combined it with the KISA video dataset to have a comprehensive dataset for \
        training and testing. As for the pose estimation dataset, we combined the COCO pose data with our manual labeling to \
        create a more robust and accurate model.")
    st.markdown("[Labeling Guide](https://docs.google.com/presentation/d/1fBfKtVBGKDe9Kt3m24RtUgz8qmAbZNc92txGm5dG0ug/edit?usp=sharing)")

    st.header("Methodology")
    st.write(
        "The process starts with the video being segmented into frames, which are then analyzed by YOLOv8, an object detection \
        algorithm that detects, tracks, and estimates the pose of people within the frames. The system processes this information \
        to extract geometric data on each person's position and pose. Before determining a fall, this preprocessed data is inputted \
        into machine learning classifiers such as random forests, support vector machines, decision trees, gradient boosting, \
        and deep learning models, to initially determine whether the person is standing or lying. The critical step of \
        falling detection then uses criteria checking across multiple frames to ascertain whether a fall has occurred. \
        If the set criteria are met, a fall is detected; otherwise, the system proceeds to the next frame without indicating a fall."
    )
    st.image("assets/methods/4_fall.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/61W3Hjj0vfI")
    st.video("https://youtu.be/-iw6W231Zmc")