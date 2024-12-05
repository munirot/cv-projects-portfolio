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
    
    st.title("Dynamic Detection Of Reverse Driving And Lane Collapse Using Yolov8")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        This work presents an application that uses the YOLOv8 object detection model and a dynamic polygon-based zone management \
        system to accurately identify reverse driving and lane collapse incidents, regardless of camera setup or road orientation. \
        The proposed algorithm outperforms other approaches with its raw detection approach and support for dynamic roads, lanes, \
        and varied CCTV angles. The findings contribute to enhanced road safety, intelligent transportation systems, and autonomous \
        vehicle development.</p>
        </p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv8, ByteTrack, Python, C++")

    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        The method leverages customizable 'In Zone' and 'Out Zone' polygons for each lane to monitor vehicle movements. \
        Reverse driving is detected when a vehicle crosses these zones in a direction opposite to the intended traffic flow, \
        while lane collapse is identified when a vehicle transitions between the zones of adjacent lanes. Each reverse driving \
        detection is evaluated based on a predefined judgment table, where a value of 0 indicates correct driving, and a value of \
        1 signifies the detection of reverse driving. This flexible approach allows adaptation to various road configurations, \
        complex intersections, and camera angles, providing robust monitoring capabilities. Additionally, we integrate ByTrack \
        for precise tracking of each vehicle as it passes through the designated zones, ensuring reliable detection and monitoring \
        even in challenging scenarios.
        </p>
    """
    st.write(method, unsafe_allow_html=True)
    st.image("assets/7_reverse_table.png", caption="Case of Reverse Driving Judgment Table")
    st.image("assets/methods/7_reverse.png", caption="Methodology and Judgement Critiria")

    st.header("Demo")
    st.video("https://youtu.be/1Qbh03eaQBA?si=WfJAfRRhsTcjln5h")
    st.video("https://youtu.be/IUWnYBE7z7g?si=ou0yV0W8XdGNnGsa")
    st.video("https://youtu.be/N0tneAS61jA?si=9FSX194-MqGhb5LR")
    st.video("https://youtu.be/yuesXMikig8?si=qbwdAvdAxkfi50gH")