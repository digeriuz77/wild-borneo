# grammar.py
import streamlit as st
import random
from pages.data import GRAMMAR_EXERCISES

def show():
    st.title("📝 Grammar Practice: 'To Be' Verb Forms")
    
    # Initialize state variables
    if 'grammar_level' not in st.session_state:
        st.session_state.grammar_level = 'easy'
    if 'grammar_exercise_index' not in st.session_state:
        st.session_state.grammar_exercise_index = 0
    if 'grammar_answers' not in st.session_state:
        st.session_state.grammar_answers = []
    if 'grammar_submitted' not in st.session_state:
        st.session_state.grammar_submitted = False
    
    # Controls sidebar
    st.sidebar.markdown("### Grammar Controls")
    
    # Difficulty selector
    level = st.sidebar.radio(
        "Select difficulty:",
        options=['easy', 'medium', 'hard'],
        index=['easy', 'medium', 'hard'].index(st.session_state.grammar_level)
    )
    
    # Update level if changed
    if level != st.session_state.grammar_level:
        st.session_state.grammar_level = level
        st.session_state.grammar_answers = []
        st.session_state.grammar_submitted = False
        st.rerun()
    
    # New exercise button
    if st.sidebar.button("New Exercise"):
        st.session_state.grammar_exercise_index = (st.session_state.grammar_exercise_index + 1) % len(GRAMMAR_EXERCISES[st.session_state.grammar_level])
        st.session_state.grammar_answers = []
        st.session_state.grammar_submitted = False
        st.rerun()
    
    # Get current exercise
    exercises = GRAMMAR_EXERCISES[st.session_state.grammar_level]
    current_exercise = exercises[st.session_state.grammar_exercise_index % len(exercises)]
    
    st.markdown(f"### {current_exercise['title']}")
    st.markdown(current_exercise['instructions'])
    
    # Initialize answers if empty
    if not st.session_state.grammar_answers:
        st.session_state.grammar_answers = [[] for _ in range(len(current_exercise['exercises']))]
    
    # Display each sentence exercise
    correct_count = 0
    
    for i, exercise in enumerate(current_exercise['exercises']):
        st.markdown(f"**Sentence {i+1}**")
        
        # Initialize this sentence's word order if not done
        if not st.session_state.grammar_answers[i]:
            # Start with shuffled words
            shuffled = exercise['words'].copy()
            random.shuffle(shuffled)
            st.session_state.grammar_answers[i] = shuffled
        
        # Display current sentence arrangement
        current_sentence = " ".join(st.session_state.grammar_answers[i])
        st.text(f"Current sentence: {current_sentence}")
        
        # Display words with move buttons
        st.markdown("**Arrange the words:**")
        
        # Create a simple horizontal display of words with buttons
        for j, word in enumerate(st.session_state.grammar_answers[i]):
            # Use a container for each word
            word_container = st.container()
            word_container.markdown(f"**{word}**")
            
            # Simple left/right buttons side by side
            left_col, right_col = st.columns(2)
            
            # Left button (if not first word)
            if j > 0:
                if left_col.button("⬅️ Move Left", key=f"left_{i}_{j}"):
                    words = st.session_state.grammar_answers[i]
                    words[j], words[j-1] = words[j-1], words[j]
                    st.session_state.grammar_answers[i] = words
                    st.rerun()
            
            # Right button (if not last word)
            if j < len(st.session_state.grammar_answers[i]) - 1:
                if right_col.button("Move Right ➡️", key=f"right_{i}_{j}"):
                    words = st.session_state.grammar_answers[i]
                    words[j], words[j+1] = words[j+1], words[j]
                    st.session_state.grammar_answers[i] = words
                    st.rerun()
            
        # Check if the sentence is correct
        user_sentence = " ".join(st.session_state.grammar_answers[i])
        correct_sentence = exercise['correct']
        is_correct = user_sentence == correct_sentence
        
        # Display result if submitted
        if st.session_state.grammar_submitted:
            if is_correct:
                st.success("✅ Correct! Your sentence is in the right order.")
                correct_count += 1
            else:
                st.error("❌ Not quite right.")
                st.info(f"The correct sentence is: **{correct_sentence}**")
        
        st.markdown("---")
    
    # Submit button to check all sentences
    if not st.session_state.grammar_submitted:
        if st.button("Check My Sentences"):
            st.session_state.grammar_submitted = True
            st.rerun()
    else:
        # Display score
        total = len(current_exercise['exercises'])
        st.success(f"You got {correct_count} out of {total} sentences correct!")
        
        # Reset button after submission
        if st.button("Try Again"):
            st.session_state.grammar_answers = []
            st.session_state.grammar_submitted = False
            st.rerun()
