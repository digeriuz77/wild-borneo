import streamlit as st
import importlib

# Page configuration
st.set_page_config(page_title="Borneo Wildlife Explorer", page_icon="🌴", layout="wide")

# Initialize session state
if 'pathway' not in st.session_state:
    st.session_state.pathway = 'birds'
if 'active_section' not in st.session_state:
    st.session_state.active_section = "home"
if 'theme' not in st.session_state:
    st.session_state.theme = "light"

# Apply theme
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    .main {background-color: #1E1E1E; color: white;}
    .stButton button {background-color: #2E7D32; color: white;}
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Borneo Wildlife Explorer")

# Toggle theme function
if st.sidebar.button("Toggle Dark/Light Mode"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
    st.rerun()

# Navigation buttons
if st.sidebar.button("🏠 Home"):
    st.session_state.active_section = "home"
if st.sidebar.button("🔍 Wildlife Identification"):
    st.session_state.active_section = "identification"
if st.sidebar.button("📚 Reading & Comprehension"):
    st.session_state.active_section = "reading"
if st.sidebar.button("📝 Grammar Practice"):
    st.session_state.active_section = "grammar"
if st.sidebar.button("✏️ Reflective Writing"):
    st.session_state.active_section = "reflection"    

# Display current section
if st.session_state.active_section == "home":
    import pages.home as module
elif st.session_state.active_section == "identification":
    import pages.identification as module
elif st.session_state.active_section == "reading":
    import pages.reading as module
elif st.session_state.active_section == "grammar":
    import pages.grammar as module
elif st.session_state.active_section == "reflection":
    import pages.reflection as module

# Add this to app.py

# Hide default Streamlit menu items
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Show the current module
module.show()
