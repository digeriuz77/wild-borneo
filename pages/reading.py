import streamlit as st
from datetime import datetime
from pages.data import COMPREHENSION_DATA, READING_SPEED_TEXT

def show():
    st.title("📚 Reading Activities")
    
    # Initialize state variables
    if 'comprehension_difficulty' not in st.session_state:
        st.session_state.comprehension_difficulty = 'easy'
    if 'comprehension_submitted' not in st.session_state:
        st.session_state.comprehension_submitted = False
    if 'reading_timer_active' not in st.session_state:
        st.session_state.reading_timer_active = False
    if 'reading_timer_start' not in st.session_state:
        st.session_state.reading_timer_start = None
    if 'reading_lines_revealed' not in st.session_state:
        st.session_state.reading_lines_revealed = 0
    if 'reading_finished' not in st.session_state:
        st.session_state.reading_finished = False
    if 'reading_mode' not in st.session_state:
        st.session_state.reading_mode = 'comprehension'
    
    # Choose reading mode
    reading_mode = st.radio("Select reading activity:", 
                 ["Comprehension", "Speed Reading"],
                 index=0 if st.session_state.reading_mode == 'comprehension' else 1,
                 horizontal=True)
    
    # Set mode based on selection
    current_mode = reading_mode.lower().replace(" ", "_")
    if current_mode != st.session_state.reading_mode:
        st.session_state.reading_mode = current_mode
        st.rerun()
    
    # Show selected reading activity
    if st.session_state.reading_mode == 'comprehension':
        show_comprehension()
    else:
        show_reading_speed()

def show_comprehension():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        pathway = st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 index=0 if st.session_state.pathway == 'birds' else 1)
        
        # Update pathway if changed
        if pathway != st.session_state.pathway:
            st.session_state.pathway = pathway
            st.session_state.comprehension_submitted = False
            st.rerun()
        
        # Difficulty selector
        difficulty = st.radio(
            "Select difficulty:",
            options=['easy', 'medium', 'hard']
        )
        
        # Update difficulty if changed
        if difficulty != st.session_state.comprehension_difficulty:
            st.session_state.comprehension_difficulty = difficulty
            st.session_state.comprehension_submitted = False
            st.rerun()
    
    with col2:
        data = COMPREHENSION_DATA[st.session_state.pathway][st.session_state.comprehension_difficulty]
        
        # Display the reading passage with a scrollable container
        st.markdown(f"""
        <div style="max-height: 300px; overflow-y: auto; padding: 15px; border-radius: 10px; background-color: #f5f5f5;">
            <h3>Reading Passage</h3>
            {data['text']}
        </div>
        """, unsafe_allow_html=True)
        
        # Comprehension questions
        st.subheader("Comprehension Check")
        
        correct_answers = 0
        total_questions = len(data['questions'])
        
        for i, q in enumerate(data['questions']):
            answer = st.radio(q['question'], q['options'], key=f"comp_q_{i}")
            
            if st.session_state.comprehension_submitted:
                if answer == q['answer']:
                    st.success("✅ Correct!")
                    correct_answers += 1
                else:
                    st.error(f"❌ The correct answer is: {q['answer']}")
        
        # Submit button
        col_a, col_b = st.columns(2)
        
        with col_a:
            if not st.session_state.comprehension_submitted:
                if st.button("Check Answers"):
                    st.session_state.comprehension_submitted = True
                    st.rerun()
        
        with col_b:
            if st.button("Reset Questions"):
                st.session_state.comprehension_submitted = False
                st.rerun()
        
        # Display score if submitted
        if st.session_state.comprehension_submitted:
            score_percentage = (correct_answers / total_questions) * 100
            st.success(f"**Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%)**")

def show_reading_speed():
    st.subheader("⏱️ Reading Speed Test")
    
    # Instructions
    st.info("""
    **Test your reading speed with this two-minute challenge!**
    1. Press "Start Reading" to begin
    2. Click "Next Line" to reveal each new line of text
    3. Read as many lines as you can in two minutes
    4. Your reading speed will be calculated automatically
    """)
    
    # Reset button
    if st.button("Reset Test"):
        st.session_state.reading_timer_active = False
        st.session_state.reading_timer_start = None
        st.session_state.reading_lines_revealed = 0
        st.session_state.reading_finished = False
        st.rerun()
    
    # Start button
    if not st.session_state.reading_timer_active and not st.session_state.reading_finished:
        if st.button("Start Reading"):
            st.session_state.reading_timer_active = True
            st.session_state.reading_timer_start = datetime.now()
            st.session_state.reading_lines_revealed = 1
            st.rerun()
    
    # Display timer if active
    if st.session_state.reading_timer_active:
        elapsed_time = datetime.now() - st.session_state.reading_timer_start
        remaining_time = 120 - elapsed_time.total_seconds()  # 2 minutes = 120 seconds
        
        if remaining_time <= 0:
            st.session_state.reading_timer_active = False
            st.session_state.reading_finished = True
            remaining_time = 0
            st.rerun()
        
        # Format time as MM:SS
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        
        # Display timer
        st.warning(f"Time remaining: {minutes:02d}:{seconds:02d}")
    
    # Display the revealed lines
    if st.session_state.reading_timer_active or st.session_state.reading_finished:
        for i in range(min(st.session_state.reading_lines_revealed, len(READING_SPEED_TEXT))):
            st.text(READING_SPEED_TEXT[i])
    
    # Next line button
    if st.session_state.reading_timer_active:
        if st.button("Next Line"):
            st.session_state.reading_lines_revealed += 1
            st.rerun()
    
    # Show results when finished
    if st.session_state.reading_finished:
        lines_read = st.session_state.reading_lines_revealed - 1
        words_read = sum(len(line.split()) for line in READING_SPEED_TEXT[:lines_read])
        
        st.success(f"Time's up! You read {lines_read} lines containing approximately {words_read} words.")
        
        # Calculate reading speed (words per minute)
        # For a 2-minute test, divide by 2 to get the average WPM
        wpm = words_read // 2
        
        if wpm >= 250:
            st.success(f"Your reading speed: {wpm} words per minute (Advanced)")
        elif wpm >= 150:
            st.success(f"Your reading speed: {wpm} words per minute (Average)")
        else:
            st.success(f"Your reading speed: {wpm} words per minute (Developing)")

