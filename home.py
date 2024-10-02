import streamlit as st

def app():
    st.markdown("""
        <style>
        body {
            font-family: ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica,Apple Color Emoji,Arial,sans-serif,Segoe UI Emoji,Segoe UI Symbol;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("Computer Vision Project Portfolio")
    st.header("Introduction")
    st.write("We are a dedicated group of professor and research students specializing in computer vision, machine learning, \
        and artificial intelligence. Our team is committed to solving complex real-world challenges by applying advanced technology \
        and developing innovative solutions across a wide range of industries. With a strong foundation in deep learning, image \
        processing, and sensor integration, we strive to leverage our expertise to create impactful applications that can transform \
        the way problems are approached and solved. Our work spans multiple domains, including traffic safety, automation, and \
        intelligent systems, where we focus on applying theoretical knowledge to practical use cases.")

    st.header("Mission")
    st.write("Our mission is to use the power of computer vision and machine learning to develop scalable solutions that improve \
        efficiency, enhance safety, and drive innovation. We aim to bridge the gap between cutting-edge research and real-world \
        applications by creating systems that address critical issues such as traffic management, anomaly detection, and \
        environmental monitoring. Through our research, we strive to contribute to societal advancement by delivering technologies \
        that make environments safer and smarter. We believe in creating a lasting impact by transforming complex research concepts \
        into user-friendly, accessible solutions that cater to diverse industries and communities.")
    
    st.header("Collaborations")
    st.write("Our research has been enriched through collaborations with leading institutions, industry professionals, and fellow \
        researchers. We are always seeking opportunities to collaborate with companies and investors who share our vision for \
        advancing computer vision technologies.")

    st.header("Contact")
    st.write("For inquiries, please reach out to us at: [contact info].")