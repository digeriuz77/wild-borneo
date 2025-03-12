import streamlit as st

def show():
    st.title("🌴 Borneo Wildlife Explorer 🌴")
    
    st.markdown("### Choose an activity on the left. Why not start with identification?")
    
    # Simple image display
    try:
        col1, col2 = st.columns(2)
        with col1:
            st.image("images/Brahminy_kite.jpg", use_container_width=True)
        with col2:
            st.image("images/Proboscis_Monkey_in_Borneo.jpg", use_container_width=True)
    except Exception as e:
        st.warning("Images couldn't be loaded.")
    
    # Button to go straight to identification
    if st.button("Start Identification Activity", use_container_width=True):
        st.session_state.active_section = "identification"
        st.rerun()
