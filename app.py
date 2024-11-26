import os
import io
import streamlit as st
import pdf2image
import google.generativeai as genai
import base64
from PIL import Image
from dotenv import load_dotenv
from time import sleep

# Load environment variables
load_dotenv()

# Configure generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate a response using generative AI
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDF and extract content
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Prompts for Generative AI
input_prompt1 = """
You are an experienced HR with Technical Experience in the field of any one job role from Data Science, Data Analyst, DevOPS, Machine Learning Engineer, Prompt Engineer, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst, Human Resource Manager, Software Developer your task is to review the provided resume against the job description for these profiles. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role from Data Science, Data Analyst, DevOPS, Machine Learning Engineer, Prompt Engineering, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst, Human Resource Manager, Software Developer and deep ATS functionality, 
your task is to evaluate the resume against the provided job description, give me only the Percentage of match if the resume matches
the job description. First the output should come as Percentage and then list of Keywords Missing and last final thoughts.
"""

# Set STREAMLIT page configuration
st.set_page_config(
    page_title="Application Tracking System",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS and animations
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        body {
            background: #000000;
            font-family: 'Poppins', sans-serif;
        }
        .main-title {
            font-size: 3rem; 
            font-family: 'Poppins', sans-serif; 
            color: #bdc3c7  ;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        .sub-title {
            font-size: 1.2rem; 
            color: #7f8c8d;
            text-align: center;
            margin-bottom: 30px;
        }
        .upload-section, .action-section, .footer-section {
            border-bottom: 2px solid #625d5c;  /* Adds a thin line at the bottom */
            margin-bottom: 10px;  /* Space between sections */
            padding: 5px 20px;  /* Reduce padding for a thinner look */
            display: flex;  /* Ensure elements align properly */
            justify-content: center;  /* Center the content */
        }

        .upload-section h3, .action-section h3, .footer-section p {
            font-size: 1rem;
            margin: 0;  /* Remove margin for compact look */
            padding: 0;  /* Remove any padding */
            color: #34495e;  /* Set text color */
        }

        .btn {
            font-size: 1.2rem; 
            color: #fff; 
            background-color: #3498db; 
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: 600;
            transition: all 0.3s ease-in-out;
        }
        .btn:hover {
            background-color: #2980b9;
        }
        .progress {
            height: 20px;
            border-radius: 10px;
            background-color: #dfe6e9;
            margin-top: 10px;
            overflow: hidden;
        }
        .progress-bar {
            height: 20px;
            width: 0;
            background-color: #3498db;
            animation: progressBar 2s linear forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes progressBar {
            from { width: 0; }
            to { width: 100%; }
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<h1 class='main-title'>AI Resume Analyzing System</h1>", unsafe_allow_html=True)
st.markdown("<div>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Analyze & Optimize your Resume for top job opportunities with AI insights</p>", unsafe_allow_html=True)
st.markdown("<div>", unsafe_allow_html=True)

# Upload Section
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
st.markdown("<h3>📁 Upload Your Resume & 📃Job Description</h3>", unsafe_allow_html=True)
st.markdown("<div class=''>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF only):", type=["PDF"])
with col2:
    input_text = st.text_area("Job Description:", placeholder="Enter job description here...")
if uploaded_file is not None:
    st.success("Resume Uploaded Successfully ✅")
else:
    st.warning("Please upload your resume to proceed.")

st.markdown("<div>", unsafe_allow_html=True)
st.markdown("<div>", unsafe_allow_html=True)

# Action Section
st.markdown("<div class='action-section'>", unsafe_allow_html=True)
st.markdown("<h3>👉🏻 Select Your Action</h3>", unsafe_allow_html=True)
st.markdown("<div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🔎 Analyze Resume", key="analyze", help="Get detailed evaluation of your resume"):
        if uploaded_file:
            with st.spinner("Processing..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_response(input_prompt1, pdf_content, input_text)
                st.success("Analysis Complete!")
                st.subheader("Evaluation Results:")
                st.write(response)
        else:
            st.error("Please upload a resume to proceed.")

with col2:
    if st.button("📈 PERCENTAGE Match", key="match", help="Find out how well your resume matches the job description"):
        if uploaded_file:
            with st.spinner("Calculating match..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_response(input_prompt2, pdf_content, input_text)
                st.success("Match Calculation Complete!")
                st.subheader("Match Results:")
                st.write(response)
        else:
            st.error("Please upload a resume to proceed.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# Footer Section
st.markdown("<div class='footer-section'>", unsafe_allow_html=True)
st.markdown("""
    <p style="text-align: center; color: #95a5a6;">Powered by <b>Streamlit</b> and <b>Gemini AI</b> | Developed by <b>Arbaaz</b></p>
    <p style="text-align: center; font-size: 0.9rem;">For support, contact <a href="mailto:arbaazt2002@gmail.com" style="color: #3498db;">arbaazt2002@gmail.com</a></p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
