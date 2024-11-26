# AI Resume Analyzing System

**Application Tracking System (ATS)** is an advanced, AI-powered platform developed to optimize resumes for job seekers. By leveraging the capabilities of **Google Gemini AI**, this system evaluates resumes, compares them with job descriptions, and provides actionable insights into the alignment, match percentage, and suggestions for resume improvement. The goal is to enhance the chances of candidates successfully passing through Applicant Tracking Systems (ATS) used by companies in their hiring processes.

### Analyze your RESUME: [HERE](https://huggingface.co/spaces/arbaazt21/AI-Resume-Analyzing-System)

---

## 🚀 **Key Features**
- **Resume Upload & Job Description Input**: Seamlessly upload a resume in PDF format and input the job description to receive a thorough evaluation.
- **AI-Powered Resume Analysis**: Using **Google Gemini AI**, the system offers an in-depth analysis of how well your resume aligns with the job description.
- **Match Percentage**: Instantly calculate the alignment percentage between your resume and the job description.
- **Resume Optimization**: Receive AI-driven suggestions on improving your resume, including optimizing for relevant keywords and improving format.
- **User-Friendly Interface**: Built with **Streamlit**, providing a clean and intuitive interface for a seamless user experience.

---

## 📋 **Prerequisites**
- Python 3.7 or higher
- Streamlit (for the web interface)
- Google Generative AI (Gemini AI) for natural language processing
- Poppler-utils (required for PDF conversion)

---

## 🛠️ **Installation**

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/ats-resume-analyzer.git
cd ats-resume-analyzer
```

### 2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
```

### 3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:
- Create a `.env` file in the root directory of the project.
- Add your **Google API Key** to the `.env` file:
```
GOOGLE_API_KEY=your_google_api_key
```

---

## 🧑‍💻 **Usage**
### 1. Run the application locally:
```bash
streamlit run app.py
```

### 2. Open the app in your browser: [AI Resume Analyzing System](https://huggingface.co/spaces/arbaazt21/AI-Resume-Analyzing-System)


### 3. How to Use:
- Upload your resume in **PDF** format.
- Enter the job description in the provided text area.
- Click **"🔎 Analyze Resume"** to receive a detailed evaluation or **"📈 Match Percentage"** to see the alignment score.

---

## 🧠 **How It Works**
1. **Resume Upload**: The user uploads a resume in PDF format. The first page of the resume is extracted and processed as an image using **pdf2image**.
2. **Job Description**: The user inputs the job description into the designated text field.
3. **Analysis**: The resume is analyzed against the job description using **Google Gemini AI**, which evaluates the content and provides insights on areas for improvement.
4. **Match Percentage**: The system calculates and displays the match percentage, indicating the alignment between the resume and the job description.

---

## ⚙️ **Technologies Used**
- **Python** - Backend programming language.
- **Streamlit** - A powerful web framework for creating interactive web applications.
- **Google Gemini AI** - This cutting-edge generative AI model is used for natural language processing, offering insights and suggestions for resume optimization based on the provided job description. The specific model used is **Google Gemini 1.5 Flash**.
- **pdf2image** - Converts PDF files to images for easier processing.
- **Poppler-utils** - Required for PDF conversion in the server environment.
- **Pillow** - Used for image processing and manipulation.

---

## 🤖 **AI Model Used**

The core of this application is powered by **Google Gemini 1.5 Flash**, a generative AI model developed by Google. Gemini 1.5 Flash is specifically designed for advanced natural language processing tasks, enabling the application to provide detailed and actionable feedback on resume-job description alignment. The model utilizes semantic analysis to identify key terms, skills, and formatting issues within both the resume and the job description, offering optimization recommendations. Here's how the model is integrated:

```python
model = genai.GenerativeModel("gemini-1.5-flash")
```

This model excels in understanding the nuances of job descriptions and resumes, ensuring that the feedback provided is not only accurate but also tailored to the specific needs of job seekers.

---

## 🔧 **Deployment on Hugging Face or Other Platforms**

To deploy this project on platforms like Hugging Face Spaces or similar, follow these steps:

1. **Ensure `requirements.txt` is complete**:
   Include all required dependencies:
   ```txt
   streamlit
   pdf2image
   pillow
   google-generativeai
   python-dotenv
   ```

2. **Add `apt.txt` for Poppler**:
   If your deployment platform doesn't include **Poppler-utils** by default, create an `apt.txt` file containing:
   ```txt
   poppler-utils
   ```

3. **Deploy**:
   Follow the platform's instructions to deploy the app, such as linking your GitHub repository to Hugging Face Spaces or another platform that supports Streamlit applications.

---

## 🌍 **Contributing**

We welcome contributions from the open-source community! If you would like to improve the app, please fork the repository, create a branch, and submit a pull request.

---

## 📧 **Contact**

For inquiries or support, feel free to reach out via email:
- Email: [support@example.com](mailto:arbaazt2002@gmail.com).
---

**Optimize your resume with the ATS and take the next step toward your dream job!** 🚀

