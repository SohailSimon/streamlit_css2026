import streamlit as st
import pandas as pd
import numpy as np



# ---- Page Config ----
st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🎓",
    layout="wide"  # Makes the page stretch full width
)

# ---- Custom CSS ----
st.markdown(
    """
    <style>
    /* Background gradient for the whole app */
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        background-attachment: fixed;
        color: #fff; /* default text color white */
    }

    /* White card style for sections */
    .card {
        background-color: rgba(255, 255, 255, 0.95); /* semi-transparent white */
        color: #000; /* text color inside card */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }

    /* Column spacing adjustment */
    .stColumns > div {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Basic Info ----
name = "Sohail Simon"
field = "Bioinformatics"
institution = "University of the Western Cape"

col1, col2 = st.columns([1, 3])  # image smaller, info wider

with col1:
    st.image("https://cdn.pixabay.com/photo/2014/12/21/23/37/science-575704_1280.png", width=200)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Summary ----
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("Summary")
st.write("""I am an organized and dependable candidate, capable of managing multiple tasks 
with a positive attitude without skipping attention to detail. I have the willingness to take on 
added responsibilities and acquire needed skills to fulfill tasks at hand. I am goal-oriented, and 
with proper planning and time management, I strive to reach my goals within a realistic timeframe.""")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Education and Skills ----
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ## Education

    **Master of Science (MSc) in Biotechnology**  
    University of the Western Cape  
    2021–2023  
    *Awarded summa cum laude*

    **Bachelor of Science (Honours) in Biotechnology**  
    University of the Western Cape  
    2020–2021  

    **Bachelor of Science (BSc) in Biotechnology**  
    University of the Western Cape  
    2016–2020  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ## Skills

    **Data & Analysis**
    - Data verification and maintenance
    - Predictive modeling
    - Data munging
    - Strong analytical skills

    **Technical**
    - Database development

    **Professional**
    - Excellent communication skills
    - Leadership skills
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Contact Information ----
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("Contact Information")
email = "3646335@myuwc.ac.za"
st.write(f"You can reach {name} at {email}.")
st.markdown('</div>', unsafe_allow_html=True)
