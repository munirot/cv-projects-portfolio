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
    
    st.title("A Simple Approach for Extracting Object Hierarchy Based on Object Detection")
    st.header("Overview")
    overview = """
        <p class="font txtAlign">
        This project addresses the challenge of efficiently generating an object hierarchy from images or videos, a process that \
        is often complex and resource-intensive without the application of advanced techniques such as machine learning or deep learning. \
        The core objective of this research is to introduce a novel method for extracting object hierarchies by analyzing the \
        overlapping bounding boxes obtained from object detection results.</p>
        
        <p class="font txtAlign"> The proposed approach simplifies the understanding of object relationships by establishing parent-child associations \
        between detected objects based on the spatial overlap of their bounding boxes. This hierarchical structure provides a clearer \
        representation of the scene, facilitating better comprehension of object interactions within digital content. The developed \
        method is implemented as a standalone package that is compatible with both Python and C++ programming languages, making it \
        versatile and easy to integrate into a wide range of applications.
        </p>
    """
    st.write(overview, unsafe_allow_html=True)

    st.header("Technology Stack")
    st.write("Python, C++, YOLO")
    
    st.header("Publication")
    st.markdown('[A Simple and Efficient Approach for Extracting Object Hierarchy in Image Data]\
        https://thesai.org/Publications/ViewPaper?Volume=15&Issue=8&Code=IJACSA&SerialNo=120')
    
  
    st.header("Methodology")
    method = """
        <p class="font txtAlign">
        The proposed methodology in this research efficiently constructs a hierarchy of detected objects in images or videos. \
        By utilizing the spatial overlap of bounding boxes generated from object detection results, the method establishes parent-child \
        relationships between objects, making it easier to comprehend the hierarchical structure of objects within a scene. The \
        implementation is available as a standalone package that supports both Python and C++, enabling seamless integration into \
        diverse applications.
        </p>
    """
    st.write(method, unsafe_allow_html=True)
    st.image("assets/methods/new_6_hierachy-1.png", caption="Flowchart of the Process of Object Detection and Hierarchy Establishment")

    st.header("Use Cases")
    st.image("assets/methods/new_6_hierachy-2.png", caption="An experimental result on single base object")
    st.image("assets/methods/new_6_hierachy-3.png", caption="An experimental result on multiple common base objects")