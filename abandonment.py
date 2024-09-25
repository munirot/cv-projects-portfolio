import streamlit as st

def app():
    st.title("Object Abandonment Detection in a Public Space Using Surveillance Video")
    st.header("Overview")
    st.write("Object abandonment detection in real-world CCTV footage has been challenging due to diverse and complex conditions, \
        limiting the effectiveness of existing technologies. This research proposes a new approach combining YOLOv8 for object detection \
        and ByteTrack to track the objects across multiple frames to enhance accuracy in public spaces. The method tracks the movement \
        of detected objects and associates them with their owners enabling precise identification of abandoned objects. This approach \
        effectively addresses various forms of object abandonment issues that may occur in real-world scenarios. The proposed method \
        achieved 95% precision and over 98% accuracy when testing with the test set. These findings have potential applications in \
        public safety and surveillance systems across diverse environments, contributing to advancements in the field of security."
    )

    st.header("Technology Stack")
    st.write("YOLOv8, ByteTrack, OpenVino, Python, C++")
    
    st.header("Labeling Guideline")
    st.write("Find the labeling guideline to the project through the slides below")
    st.markdown("[Labeling Guide](https://docs.google.com/presentation/d/14GOl0Dp8gUuK8tfF2L4YQWwVL4VfKEqABT9iUjJCi9k/edit?usp=sharing)")
  
    st.header("Methodology")
    st.write(
        "Our methodology for detecting abandoned objects in video frames involves two primary stages: object detection and tracking, \
        and distance estimation. In the first stage, we used the custom YOLOv8 object detection model to identify and localize objects,\
        such as boxes and bags, within video frames. Once detected, we employ the ByteTrack algorithm to track and assign unique IDs \
        to these objects across consecutive frames, handling occlusions and maintaining real-time performance. In the second stage, \
        a distance estimation function determines if an object is abandoned by calculating the Euclidean distance between the \
        tracked object and the last person who interacted with it. If the distance exceeds a threshold of two times a person's width, \
        the object is flagged as abandoned."
    )
    st.image("assets/methods/3_abandonment.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/iZQs-JqEOZ8")
    st.video("https://youtu.be/ih946UYGsSY")