import streamlit as st

def app():
    st.markdown(""" <style> 
                .title {
                    font-size: 3rem;
                    color: #364F6B;
                    text-align: center;
                    font-weight: bold;
                    text-transform: uppercase;
                    font-family: "Poppins";
                    line-height: normal;
                }
                    
                .font {
                    font-family: "ui-sans-serif", "-apple-system", "system-ui", "Segoe UI";
                }
                
                .txtAlign {
                    text-align: justify;
                }
                
                .nav-container{
                    display: inline-grid;
                    grid-template-columns: repeat(auto-fit, 23.33%);
                    min-width: 100%;
                    grid-gap: 10px;
                    list-style: none;
                    position: relative;
                    justify-content: center;
                    background-color: #f1f2f6;
                    margin: 1rem 0;
                    padding: 8px 0px;
                    border-radius: 10px;
                }
                
                .nav-button {
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #f1f2f6;
                    color: black !important;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                    text-align: center;
                }
                
                .nav-button:hover {
                    background-color: #364F6B;
                    color: #FFF !important;
                    text-decoration: none;
                }
        </style> """, unsafe_allow_html=True)
    
    
    st.markdown("<p class='title font'>AI Convergence Lab</p> <hr style="">", unsafe_allow_html=True)
    
    # Navigation bar styled as buttons
    st.markdown(
        """
        <div class="nav-container">
            <a href="#introduction" class="nav-button">Introduction</a>
            <a href="#our-mission" class="nav-button">Mission</a>
            <a href="#collaborations" class="nav-button">Collaboration</a>
            <a href="#contact" class="nav-button">Contact</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.image("assets/ai-image.jpg")
    
    st.header("Introduction")
    st.write('<p class="font txtAlign"> We are a dedicated group of research enthusiast specializing in computer vision, machine learning, \
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
            Tel: (+82) 010-3090-7916<br>
            Address: Chungbuk National University, South Korea
        </p>
    """
    st.write(contact_info, unsafe_allow_html=True)