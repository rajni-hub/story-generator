import streamlit as st
import requests
import json
import os
import random
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Page Configuration ---
st.set_page_config(
    page_title="✨ AI Story Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- Custom CSS Styling ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    

    
    /* Header styling */
    .main-header {
        background: #ffffff;
        padding: 2.5rem 0;
        border-bottom: 1px solid #e5e7eb;
        text-align: center;
    }
    
    .main-title {
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        color: #00c896;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #6b7280;
        font-size: 1.2rem;
        font-weight: 400;
    }

    .story-output {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        line-height: 1.7;
        font-size: 1rem;
    }
    
            
    
    /* Card styling with better spacing */
    .card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }
    
    /* Compact card for API test */
    .compact-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0 0 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.3rem;
        color: #1F2937;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .section-header::before {
        content: '';
        width: 4px;
        height: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* Compact section header */
    .compact-header {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        color: #1F2937;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .compact-header::before {
        content: '';
        width: 3px;
        height: 16px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* Improved text readability */
    p, div, span, label {
        color: #374151 !important;
        line-height: 1.6;
    }
    
    /* Form labels with better contrast */
    .stSelectbox > label, .stTextArea > label {
        color: #1F2937 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    /* Help text styling */
    .stSelectbox > div > div[data-testid="stMarkdownContainer"] small,
    .stTextArea > div > div[data-testid="stMarkdownContainer"] small {
        color: #6B7280 !important;
        font-size: 0.85rem !important;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        text-transform: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
        background: linear-gradient(135deg, #5a67d8, #6b46c1) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Compact button for API test */
    .compact-button > button {
        padding: 0.4rem 1rem !important;
        font-size: 0.9rem !important;
        border-radius: 8px !important;
    }
    
    /* Primary button variant */
    .primary-button > button {
        background: linear-gradient(135deg, #10B981, #059669) !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
    }
    
    .primary-button > button:hover {
        background: linear-gradient(135deg, #059669, #047857) !important;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4) !important;
    }
    
    /* Secondary button variant */
    .secondary-button > button {
        background: linear-gradient(135deg, #F59E0B, #D97706) !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3) !important;
    }
    
    .secondary-button > button:hover {
        background: linear-gradient(135deg, #D97706, #B45309) !important;
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4) !important;
    }
    
    /* Form elements */
    .stTextArea > div > div > textarea {
        border-radius: 12px !important;
        border: 2px solid #E5E7EB !important;
        font-family: 'Inter', sans-serif !important;
        padding: 1rem !important;
        transition: all 0.3s ease !important;
        background: #FFFFFF !important;
        color: #1F2937 !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
        font-weight: 400 !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        background: #FFFFFF !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #6B7280 !important;
        opacity: 1 !important;
        font-style: italic !important;
        font-weight: 400 !important;
    }
    
    /* Additional textarea styling to ensure visibility */
    .stTextArea textarea {
        color: #1F2937 !important;
        background-color: #FFFFFF !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #6B7280 !important;
        opacity: 1 !important;
    }
    
    /* COMPREHENSIVE SELECTBOX STYLING - All possible selectors */
    
    /* Basic selectbox container */
    .stSelectbox {
        color: #1F2937 !important;
    }
    
    .stSelectbox > div {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
    }
    
    .stSelectbox > div > div {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 12px !important;
    }
    
    .stSelectbox > div > div > div {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        border-radius: 12px !important;
    }
    
    /* Target the actual select element */
    .stSelectbox select {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 12px !important;
        padding: 0.5rem 1rem !important;
    }
    
    /* Target select options */
    .stSelectbox select option {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        padding: 0.5rem !important;
    }
    
    /* Modern Streamlit versions - BaseWeb components */
    [data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        border: 2px solid #E5E7EB !important;
        border-radius: 12px !important;
    }
    
    [data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
    }
    
    /* Dropdown popover */
    [data-baseweb="popover"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 8px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Menu container */
    [data-baseweb="menu"] {
        background-color: #FFFFFF !important;
        border: none !important;
        max-height: 200px !important;
        overflow-y: auto !important;
    }
    
    /* Menu options */
    [data-baseweb="menu-item"] {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
        border: none !important;
        cursor: pointer !important;
    }
    
    /* Hover state for menu items */
    [data-baseweb="menu-item"]:hover {
        background-color: #F3F4F6 !important;
        color: #1F2937 !important;
    }
    
    /* Active/selected state */
    [data-baseweb="menu-item"][aria-selected="true"] {
        background-color: #EBF4FF !important;
        color: #1E40AF !important;
        font-weight: 600 !important;
    }
    
    /* Alternative targeting for menu items */
    li[role="option"] {
        background-color: #FFFFFF !important;
        color: #1F2937 !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        list-style: none !important;
    }
    
    li[role="option"]:hover {
        background-color: #F3F4F6 !important;
        color: #1F2937 !important;
    }
    
    /* Generic targeting for all dropdown elements */
    [data-testid="stSelectbox"] {
        color: #1F2937 !important;
    }
    
    [data-testid="stSelectbox"] * {
        color: #1F2937 !important;
    }
    
    [data-testid="stSelectbox"] div {
        background-color: #FFFFFF !important;
    }
    
    /* Force override any inherited styles */
    .stSelectbox *, 
    [data-baseweb="select"] *, 
    [data-baseweb="menu"] *,
    [data-baseweb="popover"] * {
        color: #1F2937 !important;
        background-color: inherit !important;
    }
    
    /* Specific override for dropdown text */
    .stSelectbox div[role="combobox"],
    .stSelectbox div[role="button"] {
        color: #1F2937 !important;
        background-color: #FFFFFF !important;
    }
    
    /* Last resort - use !important on everything */
    .stSelectbox, 
    .stSelectbox div, 
    .stSelectbox span,
    [data-testid="stSelectbox"],
    [data-testid="stSelectbox"] div,
    [data-testid="stSelectbox"] span {
        color: #1F2937 !important;
        background-color: #FFFFFF !important;
    }
    
    /* Story output styling */
    .story-output {
        background: linear-gradient(135deg, #F8FAFC, #F1F5F9);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        font-family: 'Inter', sans-serif;
        line-height: 1.8;
        color: #1F2937 !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        font-size: 1rem;
    }
    
    /* Success/Error messages with better text */
    .stSuccess {
        background: linear-gradient(135deg, #ECFDF5, #D1FAE5) !important;
        border: 1px solid #10B981 !important;
        border-radius: 12px !important;
    }
    
    .stSuccess > div {
        color: #047857 !important;
        font-weight: 600 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #FEF2F2, #FECACA) !important;
        border: 1px solid #EF4444 !important;
        border-radius: 12px !important;
    }
    
    .stError > div {
        color: #B91C1C !important;
        font-weight: 600 !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #EFF6FF, #DBEAFE) !important;
        border: 1px solid #3B82F6 !important;
        border-radius: 12px !important;
    }
    
    .stInfo > div {
        color: #1D4ED8 !important;
        font-weight: 500 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #FFFBEB, #FEF3C7) !important;
        border: 1px solid #F59E0B !important;
        border-radius: 12px !important;
    }
    
    .stWarning > div {
        color: #92400E !important;
        font-weight: 600 !important;
    }
    
    /* Spinner customization */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Expandable section */
    .streamlit-expanderHeader {
        background: rgba(102, 126, 234, 0.1) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        color: #1F2937 !important;
        font-weight: 600 !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 0 0 12px 12px !important;
        color: #374151 !important;
    }
    
    /* Columns spacing */
    .row-widget.stHorizontal > div {
        padding: 0 0.25rem;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3));
        border-radius: 1px;
        margin: 1.5rem 0;
    }
    
    /* Animation for loading states */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .card, .compact-card {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Better column info styling */
    .column-info {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 8px;
        padding: 0.75rem;
        text-align: center;
        color: #1E40AF !important;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .card, .compact-card {
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        .row-widget.stHorizontal > div {
            padding: 0;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a67d8, #6b46c1);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript solution to force dropdown styling
st.markdown("""
<script>
// Function to fix dropdown styling
function fixDropdownStyling() {
    // Wait for elements to load
    setTimeout(function() {
        // Target all selectbox elements
        const selectboxes = document.querySelectorAll('[data-testid="stSelectbox"]');
        
        selectboxes.forEach(function(selectbox) {
            // Style the main container
            selectbox.style.color = '#1F2937';
            selectbox.style.backgroundColor = '#FFFFFF';
            
            // Style all child elements
            const allChildren = selectbox.querySelectorAll('*');
            allChildren.forEach(function(child) {
                child.style.color = '#1F2937';
                child.style.backgroundColor = '#FFFFFF';
            });
            
            // Style select elements specifically
            const selects = selectbox.querySelectorAll('select');
            selects.forEach(function(select) {
                select.style.color = '#1F2937';
                select.style.backgroundColor = '#FFFFFF';
                select.style.border = '2px solid #E5E7EB';
                select.style.borderRadius = '12px';
                select.style.padding = '0.5rem 1rem';
                
                // Style options
                const options = select.querySelectorAll('option');
                options.forEach(function(option) {
                    option.style.color = '#1F2937';
                    option.style.backgroundColor = '#FFFFFF';
                });
            });
        });
        
        // Target BaseWeb components
        const baseweb_selects = document.querySelectorAll('[data-baseweb="select"]');
        baseweb_selects.forEach(function(element) {
            element.style.color = '#1F2937';
            element.style.backgroundColor = '#FFFFFF';
            element.style.border = '2px solid #E5E7EB';
            element.style.borderRadius = '12px';
        });
        
        // Target menu items
        const menuItems = document.querySelectorAll('[data-baseweb="menu-item"], li[role="option"]');
        menuItems.forEach(function(item) {
            item.style.color = '#1F2937';
            item.style.backgroundColor = '#FFFFFF';
            item.style.padding = '0.75rem 1rem';
            
            // Add hover effect
            item.addEventListener('mouseenter', function() {
                this.style.backgroundColor = '#F3F4F6';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.backgroundColor = '#FFFFFF';
            });
        });
        
        // Target menus and popovers
        const menus = document.querySelectorAll('[data-baseweb="menu"], [data-baseweb="popover"]');
        menus.forEach(function(menu) {
            menu.style.backgroundColor = '#FFFFFF';
            menu.style.border = '1px solid #E5E7EB';
            menu.style.borderRadius = '8px';
            menu.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.1)';
        });
        
    }, 100);
}

// Run the function when page loads
document.addEventListener('DOMContentLoaded', fixDropdownStyling);

// Also run when Streamlit reruns
window.addEventListener('load', fixDropdownStyling);

// Run periodically to catch dynamically created elements
setInterval(fixDropdownStyling, 1000);

// Run immediately
fixDropdownStyling();
</script>
""", unsafe_allow_html=True)

# --- Page Configuration ---
st.set_page_config(
    page_title="Gemini AI Story Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Header Section ---
st.markdown("""
<div class="main-header">
    <h1 class="main-title">AI Story Generator</h1>
    <p class="subtitle">Powered by Google Gemini - Create magical stories with AI</p>
</div>
""", unsafe_allow_html=True)

# --- API Key Check ---
if not api_key:
    st.markdown("""
    <div class="card">
        <h3 class="section-header">API Key Required</h3>
        <p>API key not found in environment variables.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("How to set up your API key"):
        st.markdown("""
        **Quick Setup Guide:**
        
        1. Visit [aistudio.google.com](https://aistudio.google.com) and sign in  
        2. Click "Get API Key" and create a new one  
        3. Copy the key (starts with `AIza...`)  
        4. Create a `.env` file in your project directory  
        5. Add this line: `GEMINI_API_KEY=your_api_key_here`
        
        **That's it! Restart the app and start creating stories.**
        """)
    st.stop()

# --- Helper Functions ---
def test_gemini_api(api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": "Hello! Please respond with 'API test successful'"}]
        }]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code, response.text
    except Exception as e:
        return "Error", str(e)

def generate_story_gemini(prompt, api_key, creativity="balanced"):
    creativity_settings = {
        "creative": {"temperature": 0.9, "top_p": 0.8},
        "balanced": {"temperature": 0.7, "top_p": 0.8},
        "focused": {"temperature": 0.3, "top_p": 0.8}
    }
    settings = creativity_settings.get(creativity, creativity_settings["balanced"])
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    story_prompt = f"""Write a creative, engaging short story based on this prompt: "{prompt}"

Guidelines:
- Length: 150-250 words
- Include vivid descriptions and engaging characters
- Create a compelling narrative arc with a satisfying conclusion
- Use creative and imaginative elements
- Make it interesting and entertaining to read

Story:"""

    payload = {
        "contents": [{"parts": [{"text": story_prompt}]}],
        "generationConfig": {
            "temperature": settings["temperature"],
            "topP": settings["top_p"],
            "maxOutputTokens": 300
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    return candidate['content']['parts'][0]['text'].strip()
            return "No story generated or response format unexpected."
        elif response.status_code == 401:
            return "Invalid API key (401)."
        elif response.status_code == 403:
            return "Access forbidden (403)."
        elif response.status_code == 404:
            return "Model not found (404). Try gemini-2.0-flash."
        elif response.status_code == 429:
            return "Rate limit exceeded (429). Please wait and retry."
        else:
            return f"API Error {response.status_code}: {response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out."
    except Exception as e:
        return f"Unexpected error: {str(e)}"



# --- Story Generation Section ---
st.markdown("""
<div class="card">
    <h3 class="section-header">Create Your Story</h3>
</div>
""", unsafe_allow_html=True)

prompt = st.text_area(
    "What's your story idea?",
    placeholder="e.g., A detective discovers that all the clocks in the city have stopped at the same time...",
    height=120,
    help="Describe your story concept, characters, or scenario. Be as creative as you want!"
)

# Settings in columns
col1, col2 = st.columns(2)
with col1:
    creativity = st.selectbox(
        "Creativity Level:",
        ["balanced", "creative", "focused"],
        help="Creative = More unexpected twists, Focused = More structured narrative, Balanced = Best of both"
    )
with col2:
    genre_hint = st.selectbox(
        "Genre (Optional):",
        ["Any", "Science Fiction", "Fantasy", "Mystery", "Romance", "Horror", "Adventure", "Comedy"],
        help="Choose a genre to guide the story's tone and style"
    )

final_prompt = f"{prompt} (Write this as a {genre_hint.lower()} story)" if genre_hint != "Any" else prompt

# Generate button
if st.button("Generate My Story", key="generate_story", type="primary"):
    if prompt:
        with st.spinner("Crafting your masterpiece..."):
            story = generate_story_gemini(final_prompt, api_key, creativity)
        
        if not story.startswith("No story") and not story.startswith("Invalid") and not story.startswith("Access") and not story.startswith("Model") and not story.startswith("Rate") and not story.startswith("API") and not story.startswith("Request") and not story.startswith("Unexpected"):
            st.success("Your story is ready!")
            
            # Story metadata
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f'<div class="column-info"><strong>Genre:</strong> {genre_hint}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="column-info"><strong>Style:</strong> {creativity.title()}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="column-info"><strong>Words:</strong> ~{len(story.split())}</div>', unsafe_allow_html=True)
            
            # Story display
            st.markdown(f'<div class="story-output">{story}</div>', unsafe_allow_html=True)
            
            # Alternative version button
            if st.button("Generate Alternative Version", key="alt_version"):
                with st.spinner("Creating another version..."):
                    alt_story = generate_story_gemini(final_prompt, api_key, creativity)
                st.markdown("### Alternative Version")
                st.markdown(f'<div class="story-output">{alt_story}</div>', unsafe_allow_html=True)
        else:
            st.error(story)
    else:
        st.warning("Please enter a story prompt first!")

# --- Sample Prompts Section ---
st.markdown("""
<div class="card">
    <h3 class="section-header">Need Inspiration? Try These Prompts</h3>
</div>
""", unsafe_allow_html=True)

sample_prompts = {
    "Sci-Fi": "A space station receives a distress signal from Earth... but Earth was destroyed 50 years ago.",
    "Fantasy": "A librarian discovers that the books in the restricted section are actually portals to other worlds.",
    "Mystery": "Every morning, the same stranger leaves a different colored rose on your doorstep.",
    "Adventure": "You inherit a map from your grandmother, but it shows places that don't exist on Earth.",
    "Horror": "Your smart home starts making decisions you never programmed it to make.",
    "Romance": "Two rival food truck owners keep parking next to each other by 'coincidence'.",
    "Comedy": "A superhero whose only power is making people slightly more optimistic."
}

selected_sample = st.selectbox("Choose a sample prompt:", list(sample_prompts.keys()))

col1, col2 = st.columns(2)
with col1:
    if st.button("Use This Prompt", key="use_prompt"):
        st.success("Prompt selected!")
        st.info(f"**{selected_sample}:** {sample_prompts[selected_sample]}")
        st.markdown("Copy this prompt and paste it in the story generator above!")

with col2:
    if st.button("Show Random Sample Story", key="random_story"):
        sample_stories = [
            "Maya thought her grandmother's recipe book was ordinary until the ingredients started glowing. Each page revealed not just recipes, but memories - the warm aroma of cardamom from her great-grandmother's kitchen in Mumbai, echoing with decades of family laughter. When she cooked the luminous recipes, something magical happened: each dish became a time portal, transporting her to precious moments with relatives she'd never met but somehow recognized in her heart.",
            
            "The city's clocks stopped at 3:47 AM, but Detective Chen was the only one who noticed. While everyone continued their routines - watches ticking, phones updating - Chen witnessed the truth: frozen raindrops suspended mid-fall, birds motionless against the dawn sky. As she delved deeper into this temporal mystery, she discovered she wasn't alone in this frozen moment, and someone had been planning this impossible pause in time for years.",
            
            "Captain Torres received an impossible transmission: 'This is Earth Control, requesting immediate assistance.' The message chilled her because Earth had been consumed by solar flares fifty years ago, forcing humanity to flee to the stars. Yet here was the signal, clear and desperate, originating from coordinates that should show only cosmic dust. As her ship altered course toward the ghost of home, Torres wondered whether Earth had somehow survived the apocalypse, or if something else was using humanity's voice to lure them back."
        ]
        
        st.markdown("### Sample Story")
        selected_story = random.choice(sample_stories)
        st.markdown(f'<div class="story-output">{selected_story}</div>', unsafe_allow_html=True)
        st.info("This is just a sample! Use the Gemini API above to create custom stories from your own prompts.")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; color: rgba(255, 255, 255, 0.9);">
    <p style="font-size: 0.9rem; margin: 0; font-weight: 500;">
        Made with Streamlit & Google Gemini AI | 
        Create unlimited stories with your imagination
    </p>
</div>
""", unsafe_allow_html=True)