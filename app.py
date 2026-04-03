import streamlit as st 
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config( 
 page_title="SA Career Coach",
 page_icon="🇿🇦",
 layout="centered"
 ) 
# Custom styling
st.markdown("""
 <style>
 .main { 
    background-color: #f8F8F6;
 }
 .stButton>button { 
    background-color: #9C8B7A; 
    color: white;
    border-radius: 8px; 
    padding: 10px 24px; 
    font-size: 16px;
    width: 100%; 
} 
.stButton>button:hover { 
    background-color: #005c3a; 
    color: white;
 }
 .response-box { 
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #007A4D;
    margin-top: 20px;
 }
 </style> 
""", unsafe_allow_html=True) 

# Header
st.markdown("## Galz the Career Coach")
st.markdown("*Your personal career advisor for the South African job market*")
st.divider() 

# Sidebar 
with st.sidebar: 
  st.markdown("### How to use") 
  st.markdown("""
    1. Describe your skills and experience 
    2. Mention the type of job you want 
    3. Click **Get Career Advice**
    4. Get personalised guidance
 """) 
st.divider()
st.markdown("### Example prompts")
st.markdown("""
- I am a matric graduate looking for admin work in Johannesburg 
- I have 3 years in retail and want to move into data 
- Help me write a CV summary for a call centre job """) 

# Main input
user_input = st.text_area(
 "Tell me about yourself:",
 placeholder="E.g. I have 2 years experience in debt collection and I want to move into data analytics...",
 height=150 
)
if st.button("Get Career Advice"):
 if user_input: 
    with st.spinner("Generating your personalised advice..."):
        response = requests.post(
    "https://api.mistral.ai/v1/chat/completions", 
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={ 
        "model": "mistral-small-latest",
         "messages": [
            {
                "role": "system",
                "content": "You are a career coach specializing in the South African job market. Help users with CV advice, job suggestions, interview tips, and career guidance. Be encouraging, practical, and relevant to South Africa. Do not use emojis in your responses." 
            },
            {
                "role": "user", 
                "content": user_input
        }
     ]
 } 
)
    result = response.json() 
    advice = result["choices"][0]["message"]["content"]

    st.markdown(f"""
             <div class="response-box"> 
            {advice} 
            </div> 
            """, unsafe_allow_html=True)
else: 
 st.warning("Please tell me a bit about yourself first!") 
# Footer
st.divider() 
st.markdown("<center>Built for South Africa | Powered by AI</center>", unsafe_allow_html=True)




