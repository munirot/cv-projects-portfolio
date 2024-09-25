import streamlit as st

def app():
    st.title("Detection of Motorcycle Riders without Helmets using Surveillance Camera")
    st.header("Overview")
    st.write(
        "Riding without a helmet is one of the leading causes of injuries and deaths in motorcycle accidents. "
        "In a country like Vietnam, the number of motorcycles on the roads is very high, making it difficult to monitor "
        "and preserve the safety of the riders. This research proposes a method for detecting motorcycle riders who are "
        "not wearing helmets using videos from the surveillance cameras along the roads, which can help enhance law "
        "enforcement and manage the safety of riders."
    )
    st.write(
        "The proposed method utilizes the state-of-the-art object detection algorithm YOLOv5 to detect helmets, non-helmets, "
        "and riders. Next, it determines whether or not riders are wearing helmets in the post-processing step. "
        "Finally, the results showed that the detection model has an mAP (mean Average Precision) of around 98% "
        "and the proposed approach can identify the motorcycle riders who are not wearing helmets precisely."
    )

    st.header("Technology Stack")
    st.write("YOLOv5, PyTorch, OpenVino, Python, C++")
    
    st.header("Dataset and Labeling Guideline")
    st.write("The dataset was collected from CCTV placed across various locations in Vietnam.")
    st.markdown("[Labeling Guide](https://docs.google.com/presentation/d/1mUDAjoQD9aZarOnBN9z2Srahx9vgDk6H9kp6FmCyZhY/edit#slide=id.g13c488e432b_2_1)")

    st.header("Methodology")
    st.write(
        "The input images are extracted from the surveillance video and then loaded into the YOLOv5 custom model to detect "
        "plain objects such as helmets, non-helmets, and riders. The results from detection are then processed to check "
        "whether or not the riders are wearing helmets."
    )
    st.image("assets/methods/1_helmet.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://www.youtube.com/watch?v=963DPLj5mJc&ab_channel=SaravitSoeng")