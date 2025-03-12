import streamlit as st
import random
from pages.data import SPECIES_DATA

def show():
    st.title(f"🔍 Identify the {st.session_state.pathway.rstrip('s')}!")
    
    # Initialize required session state variables
    if 'current_species_index' not in st.session_state:
        st.session_state.current_species_index = 0
    if 'answer_checked' not in st.session_state:
        st.session_state.answer_checked = False
    if 'correct_answers' not in st.session_state:
        st.session_state.correct_answers = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        pathway = st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 index=0 if st.session_state.pathway == 'birds' else 1)
        
        # Update pathway if changed
        if pathway != st.session_state.pathway:
            st.session_state.pathway = pathway
            st.session_state.current_species_index = 0
            st.session_state.answer_checked = False
            st.rerun()
    
    with col2:
        species_list = SPECIES_DATA[st.session_state.pathway]
        
        # Ensure index is valid
        if st.session_state.current_species_index >= len(species_list):
            st.session_state.current_species_index = 0
        
        species = species_list[st.session_state.current_species_index]
        
        # Display the species image
        try:
            st.image(species['image'], use_container_width=True)
        except Exception as e:
            st.error(f"Could not load image: {species['image']}")
            st.image("https://via.placeholder.com/400x300?text=Wildlife+Image", use_container_width=True)
        
        # Create a shuffled version of options if not already in session state
        option_key = f"shuffled_options_{st.session_state.pathway}_{st.session_state.current_species_index}"
        if option_key not in st.session_state:
            shuffled_options = species['options'].copy()
            random.shuffle(shuffled_options)
            st.session_state[option_key] = shuffled_options
        
        # Multiple choice question with shuffled options
        answer = st.radio("What species is this?", st.session_state[option_key])
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            # Check answer button
            if not st.session_state.answer_checked:
                if st.button("Check Answer"):
                    st.session_state.answer_checked = True
                    st.session_state.total_questions += 1
                    
                    if answer == species['name']:
                        st.session_state.correct_answers += 1
                        st.success("✅ Correct! Well done!")
                    else:
                        st.error(f"❌ Not quite. This is a {species['name']}.")
        
        with col_b:
            # Next button
            if st.button("Next Species"):
                st.session_state.answer_checked = False
                # Move to the next species
                st.session_state.current_species_index = (st.session_state.current_species_index + 1) % len(species_list)
                st.rerun()
        
        # Display fact box if answer has been checked
        if st.session_state.answer_checked:
            st.info(f"**Fact about the {species['name']}:** {species['fact']}")
        
        # Display score
        st.success(f"Your score: {st.session_state.correct_answers}/{st.session_state.total_questions}")
