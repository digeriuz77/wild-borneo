import streamlit as st

def show():
    st.title("Wildlife Poetry")
    
    # Display the image of the Brahminy kite
    st.image("images/Brahminy_kite.jpg", caption="Brahminy Kite", use_container_width=True)
    
    # Display Tennyson's "The Eagle" poem
    st.subheader("The Eagle by Alfred, Lord Tennyson")
    
    st.markdown("""
    *He clasps the crag with crooked hands;  
    Close to the sun in lonely lands,  
    Ring'd with the azure world, he stands.  
    The wrinkled sea beneath him crawls;  
    He watches from his mountain walls,  
    And like a thunderbolt he falls.*
    """)
    
    # Create a section for questions about the poem
    st.write("---")
    st.subheader("Understanding the Poem")
    
    # Question 1
    st.write("#### 1. Where does the eagle live near?")
    eagle_location = st.text_area("Type your answer here:", key="eagle_location", height=100)
    
    # Question 2
    st.write("#### 2. What does the eagle do?")
    eagle_action = st.text_area("Type your answer here:", key="eagle_action", height=100)
    
    # Check button for first two questions
    if st.button("Check My Answers", key="check_eagle_questions"):
        st.write("#### Answers:")
        
        st.markdown("""
        1. The eagle lives near a crag (a rocky cliff or mountain) close to the sun in lonely lands, with the sea beneath.
        
        2. The eagle:
           - Clasps the crag with his crooked hands (talons)
           - Stands watching from his mountain walls
           - Falls like a thunderbolt (to catch prey)
        
        **Some important words explained:**
        - **Crag**: A steep, rugged rock or cliff face
        - **Azure**: Blue, specifically the bright blue color of the sky
        - **Thunderbolt**: A flash of lightning with a simultaneous crash of thunder; suggesting something extremely fast and powerful
        """)
    
    st.write("---")
    
    # Multiple choice questions
    st.subheader("Multiple Choice Questions")
    
    # MCQ 1
    st.write("#### Why is the sea wrinkled?")
    mcq1 = st.radio(
        "Choose the best answer:",
        [
            "a) Because it is old",
            "b) Because the waves look like lines from high up",
            "c) Because it is messy",
            "d) Because it is big"
        ],
        key="mcq1"
    )
    
    # MCQ 2
    st.write("#### Why does the sea crawl?")
    mcq2 = st.radio(
        "Choose the best answer:",
        [
            "a) Because it is old",
            "b) Because it cannot walk",
            "c) Because it looks slow compared to the eagle",
            "d) Because it is a baby"
        ],
        key="mcq2"
    )
    
    # Check MCQ answers button
    if st.button("Check My Answers", key="check_mcqs"):
        score = 0
        feedback = ""
        
        # Check MCQ 1
        if mcq1 == "b) Because the waves look like lines from high up":
            score += 1
            feedback += "✅ Question 1: Correct! From high up, the waves on the sea surface appear as wrinkles.\n\n"
        else:
            feedback += "❌ Question 1: Incorrect. The correct answer is (b) because from the eagle's high perspective, the waves look like wrinkles or lines on the surface of the sea.\n\n"
        
        # Check MCQ 2
        if mcq2 == "c) Because it looks slow compared to the eagle":
            score += 1
            feedback += "✅ Question 2: Correct! From the eagle's perspective high up, the movement of the sea appears slow, like crawling.\n\n"
        else:
            feedback += "❌ Question 2: Incorrect. The correct answer is (c) because from the eagle's high vantage point, the sea's movement appears very slow compared to the eagle's swift movements.\n\n"
        
        st.markdown(f"**Your score: {score}/2**")
        st.markdown(feedback)
    
    st.write("---")
    
    # Thunderbolt explanation question
    st.subheader("Deeper Understanding")
    st.write("#### Why is the eagle compared to a thunderbolt when it falls?")
    thunderbolt_answer = st.text_area("Type your explanation here:", key="thunderbolt", height=150)
    
    if st.button("Submit My Explanation", key="submit_thunderbolt"):
        st.success("Well done! If you gave an answer about how it becomes fast and suddenly appears in the sky to strike its prey, you got it! The comparison to a thunderbolt emphasizes the eagle's speed, power, and the sudden, dramatic nature of its dive when hunting.")
    
    st.write("---")
    
    # Writing your own poem section
    st.subheader("Write Your Own Bird Poem")
    
    st.markdown("""
    Now it's your turn to create a poem about a bird! Consider including:
    - Colors of the bird
    - Sounds the bird makes
    - What the bird does
    - Where it flies near
    """)
    
    # Example poem
    with st.expander("Click here to see an example poem"):
        st.markdown("""
        **The Swallows**

        *The swallows swoop around my house  
        Their blue wings shine in flight  
        They build their nests from moss and sticks  
        and come to sleep at night.*

        *They tweet and chirp as they fly  
        their song is beautiful to hear  
        I miss them when they fly away  
        but they'll be back next year.*
        """)
    
    # Textarea for student's poem
    own_poem = st.text_area("Write your poem here:", height=200, key="own_poem")
    
    if st.button("Share My Poem", key="share_poem"):
        if len(own_poem.split()) < 10:
            st.warning("Please write a bit more for your poem.")
        else:
            st.balloons()
            st.success("Beautiful poem! Thank you for sharing your creativity. Why not write it in your exercise book to share with your teacher.")
            
            # Self-assessment checklist for the poem
            st.subheader("Self-Assessment")
            st.write("Check the elements you included in your poem:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                colors = st.checkbox("Colors of the bird")
                sounds = st.checkbox("Sounds the bird makes")
            
            with col2:
                actions = st.checkbox("What the bird does")
                location = st.checkbox("Where the bird flies")
            
            # Feedback based on checklist
            total_checked = sum([colors, sounds, actions, location])
            
            if total_checked >= 3:
                st.success("Excellent! Your poem includes most of the suggested elements.")
            elif total_checked >= 1:
                st.info("Good start! Consider adding more of the suggested elements to make your poem more vivid.")
            else:
                st.info("Try adding some specific details about the bird's colors, sounds, actions, or location to enhance your poem.")

if __name__ == "__main__":
    show()
