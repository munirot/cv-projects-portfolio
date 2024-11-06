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
    
    st.title("Fighting Detection Using Keypoint Pose Estimation with Machine Learning Classifiers")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        With the rapid growth of smart surveillance systems, behavior recognition has become a hotspot in research in the field \
        of computer vision. This project explores the use of deep learning, a YOLOv8 model for automated fighting detection in CCTV \
        footage by identifying fighting and non-fighting activities in video. The key to the system is the extraction of \
        geometric angles from pose estimation, which feeds into classifiers to categorize actions into binary classification.</p>
        
        <p class="font txtAlign"> The post-classification is also employed to check against predefined criteria to validate fight activities, \
        enhancing accuracy and reducing false positives. This project aims to improve public safety in various environments by \
        leveraging advanced computer vision and machine learning for efficient real-time monitoring and detection of fighting incidents.
        </p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv8, Machine Learning Classifier, PyTorch, OpenVino, Python, C++")
    
    st.header("Dataset and Labeling Guideline")
    st.write("We collected data from the internet and combined it with the KISA video dataset to have a comprehensive dataset for \
        training and testing. As for the pose estimation dataset, we combined the COCO pose data with our manual labeling to \
        create a more robust and accurate model.")
    st.markdown("[Labeling Guide](https://docs.google.com/presentation/d/1fBfKtVBGKDe9Kt3m24RtUgz8qmAbZNc92txGm5dG0ug/edit?usp=sharing)")

    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        Similar to fall detection, the process starts with the video being segmented into frames to be fed to the YOLOv8 to \
        perform detection, tracking, and estimate the pose of people within the frames. The model outputs 17 key points of \
        information that were then used to convert to angle data, to analyze the relationships and movements of the people in the scene. \
        This angle data serves as input to a machine learning classifier trained to classify between fight and non-fight scenarios. \
        The classifier's output is further checked through a set of criteria, checking the overlap of wrists and ankles of the people \
        in the frame to enhance detection accuracy. If the overlap criteria are met, the system conclusively identifies the occurrence \
        of a fight. This methodology aims to improve real-time fight detection accuracy by combining advanced detection models with \
        specific post-classification criteria checks.
        </p>
    """
    st.write(method, unsafe_allow_html=True)
    st.image("assets/methods/new_5_fight.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/M3kLdogW4As")
    st.video("https://youtu.be/_4x46AjSc2A")
    st.video("https://youtu.be/wJRCseXsQzc")
    st.video("https://youtu.be/qh2L586V3-A")