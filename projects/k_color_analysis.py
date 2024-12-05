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
    
    st.title("Color Analysis and Clothing Identification using Background Subtraction and Dominant Grid Selection")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        This system combines object detection, background subtraction, and weighted grid analysis for accurate clothing detection \
        and classification. By using static and dynamic ROI comparisons and focusing on high-weighted regions, the system achieves \
        superior performance in detecting clothing features, even in complex environments. This concept is poised to revolutionize \
        applications in retail, surveillance, and fashion industries.</p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("YOLOv10, Background subtraction, Regions of Interest (ROIs) extraction, Python")

    st.header("Methodology")
    method_1 = """
        <p class="font txtAlign">
        The system employs advanced computer vision techniques to process video streams and extract clothing information. \
        Its workflow begins with frame extraction and preprocessing, where video frames are prepared for object detection and \
        background subtraction. The YOLOv10 deep learning model identifies clothing types such as short pants, long pants, short \
        sleeve shirts, and long sleeve shirts, generating bounding boxes for detected clothing parts. A static background model is \
        updated every five minutes, enabling background subtraction to distinguish between static and dynamic regions. Two types of \
        Regions of Interest (ROIs) are then extracted: dynamic ROIs from the original frames using object detection bounding boxes \
        and static ROIs from the background model.
        </p>
        
        <p class="font txtAlign">
        A weighted grid calculation process is applied to analyze changes between the dynamic and static ROIs. Both ROIs are resized \
        into 5×5 grids, and the differences between corresponding cells in these grids are computed. These differences are weighted, \
        emphasizing significant changes to identify the most meaningful areas for analysis. The grid cell with the highest weighted \
        difference, termed the "dominant grid," represents the region most indicative of clothing type or color. The dominant grid’s \
        RGB values are manually labeled into nine predefined color categories (e.g., red, blue, yellow). These labeled datasets are \
        used to train a Support Vector Machine (SVM) model, which learns to classify colors accurately. Once trained, the SVM model \
        classifies colors of new clothing items based on their dominant grid’s RGB values.
        </p>
    """
    
    method_2 = """
        <p class="font txtAlign">
        The system integrates results from the YOLO model and SVM classifier, outputting both the type and color of detected clothing. \
        This dual-output system is applicable in real-world scenarios such as safety and smart city applications, aiding in tasks like \
        identifying missing persons based on clothing type and color metadata. Key innovations include dual ROI comparison for improved \
        segmentation, a weighted grid approach to focus on significant clothing features, real-time background subtraction for \
        adaptability, and a modular framework combining object detection and machine learning for precise classification.
        </p>
    """
    
    st.write(method_1, unsafe_allow_html=True)
    st.image("assets/methods/10_color_classification_1.png", caption="Methodology Flowchart")
    
    st.write(method_2, unsafe_allow_html=True)
    st.image("assets/methods/10_color_classification.png", caption="Methodology Flowchart")

    st.header("Demo")
    st.video("https://youtu.be/6m1ZZtQfzbA")