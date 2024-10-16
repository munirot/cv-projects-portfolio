import streamlit as st

def app():
    st.markdown(""" <style> 
                .title {
                    font-size: 3rem;
                    color: #507687;
                    text-align: center;
                    font-weight: bold;
                    text-transform: uppercase;
                    font-family: "Poppins";
                    margin-bottom: 3rem;
                    line-height: normal;
                }
                    
                .font {
                    font-family: "ui-sans-serif", "-apple-system", "system-ui", "Segoe UI";
                }
                
                .txtAlign {
                    text-align: justify;
                }
        </style> """, unsafe_allow_html=True)
    
    st.markdown("<p class='title font'>Project Highlights / <br> Lab's Name</p> <hr>", unsafe_allow_html=True)
    
    st.header("Introduction")
    st.write('<p class="font txtAlign"> We are a dedicated group of professor and research students specializing in computer vision, machine learning, \
        and artificial intelligence. Our team is committed to solving complex real-world challenges by applying advanced technology \
        and developing innovative solutions across a wide range of industries. With a strong foundation in deep learning, image \
        processing, and sensor integration, we strive to leverage our expertise to create impactful applications that can transform \
        the way problems are approached and solved. Our work spans multiple domains, including traffic safety, automation, and \
        intelligent systems, where we focus on applying theoretical knowledge to practical use cases.</p>', unsafe_allow_html=True)

    st.header("Our Mission")
    st.write('<p class="font txtAlign"> Our mission is to use the power of computer vision and machine learning to develop scalable solutions that improve \
        efficiency, enhance safety, and drive innovation. We aim to bridge the gap between cutting-edge research and real-world \
        applications by creating systems that address critical issues such as traffic management, anomaly detection, and \
        environmental monitoring. Through our research, we strive to contribute to societal advancement by delivering technologies \
        that make environments safer and smarter. We believe in creating a lasting impact by transforming complex research concepts \
        into user-friendly, accessible solutions that cater to diverse industries and communities.</p>', unsafe_allow_html=True)
    
    st.header("Collaborations")
    st.write('<p class="font txtAlign"> Our research has been enriched through collaborations with leading institutions, industry professionals, and fellow \
        researchers. We are always seeking opportunities to collaborate with companies and investors who share our vision for \
        advancing computer vision technologies.</p>', unsafe_allow_html=True)

    st.header("Contact")
    contact_info = """
        <p class="font">
            For inquiries, please reach out to us at:<br>
            <strong>Professor Kim Tae-Kyung</strong><br>
            Email: <a href="mailto:misoh049@gmail.com">misoh049@gmail.com</a><br>
            Tel: (Add phone number here)
        </p>
    """
    st.write(contact_info, unsafe_allow_html=True)