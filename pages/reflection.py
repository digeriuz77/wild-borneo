import streamlit as st
from annotated_text import annotated_text

def show():
    st.title("Wildlife Reflective Writing")
    
    # Allow students to choose between birds or monkeys
    animal_choice = st.radio(
        "Choose your topic for today's reflection:",
        ["Birds", "Monkeys"],
        horizontal=True
    )
    
    st.write("---")
    
    # Different phrase matching and reflection prompt based on choice
    if animal_choice == "Birds":
        show_bird_activities()
    else:
        show_monkey_activities()

def show_bird_activities():
    st.subheader("Bird Idioms and Expressions")
    
    st.markdown("""
    First, let's explore some common expressions about birds. Match each phrase with its meaning.
    """)
    
    # Dictionary of bird idioms with their meanings
    bird_idioms = {
        "jailbird": "A person who is or has been in prison",
        "songbird": "A person with a beautiful singing voice",
        "birdbrain": "Someone who is not very intelligent",
        "birdstrike": "When a bird collides with an aircraft",
        "early-bird": "Someone who arrives early or does something before others"
    }
    
    # Create columns for each phrase to match
    cols = st.columns(len(bird_idioms))
    user_matches = {}
    
    # Create a dropdown for each idiom
    for i, (phrase, meaning) in enumerate(bird_idioms.items()):
        with cols[i]:
            st.markdown(f"**{phrase}**")
            meanings_list = list(bird_idioms.values())
            selected_meaning = st.selectbox(
                f"Meaning of '{phrase}'",
                meanings_list,
                key=f"bird_{i}"
            )
            user_matches[phrase] = selected_meaning
    
    # Check button to verify matches
    if st.button("Check My Answers", key="check_birds"):
        correct_count = sum(1 for phrase, meaning in bird_idioms.items() if user_matches[phrase] == meaning)
        
        if correct_count == len(bird_idioms):
            st.success(f"Perfect! You matched all {len(bird_idioms)} phrases correctly!")
        else:
            st.warning(f"You matched {correct_count} out of {len(bird_idioms)} phrases correctly. Try again!")
        
        # Show the correct answers with annotation
        st.subheader("Correct Matches:")
        for phrase, correct_meaning in bird_idioms.items():
            user_meaning = user_matches[phrase]
            is_correct = user_meaning == correct_meaning
            
            annotated_text(
                (phrase, "", "#8ef" if is_correct else "#faa"),
                " → ",
                (correct_meaning, "", "#afa" if is_correct else "#faa")
            )
            st.write("")
    
    st.write("---")
    
    # Reflective writing section
    show_reflective_writing("birds")

def show_monkey_activities():
    st.subheader("Monkey Idioms and Expressions")
    
    st.markdown("""
    First, let's explore some common expressions about monkeys. Match each phrase with its meaning.
    """)
    
    # Dictionary of monkey idioms with their meanings
    monkey_idioms = {
        "monkey around": "To waste time playing or doing something unproductive",
        "monkey bars": "A playground structure with horizontal bars for climbing",
        "go ape": "To become very angry or excited",
        "cheeky monkey": "A playfully mischievous person",
        "ape someone": "To copy or imitate someone's behavior"
    }
    
    # Create columns for each phrase to match
    cols = st.columns(len(monkey_idioms))
    user_matches = {}
    
    # Create a dropdown for each idiom
    for i, (phrase, meaning) in enumerate(monkey_idioms.items()):
        with cols[i]:
            st.markdown(f"**{phrase}**")
            meanings_list = list(monkey_idioms.values())
            selected_meaning = st.selectbox(
                f"Meaning of '{phrase}'",
                meanings_list,
                key=f"monkey_{i}"
            )
            user_matches[phrase] = selected_meaning
    
    # Check button to verify matches
    if st.button("Check My Answers", key="check_monkeys"):
        correct_count = sum(1 for phrase, meaning in monkey_idioms.items() if user_matches[phrase] == meaning)
        
        if correct_count == len(monkey_idioms):
            st.success(f"Perfect! You matched all {len(monkey_idioms)} phrases correctly!")
        else:
            st.warning(f"You matched {correct_count} out of {len(monkey_idioms)} phrases correctly. Try again!")
        
        # Show the correct answers with annotation
        st.subheader("Correct Matches:")
        for phrase, correct_meaning in monkey_idioms.items():
            user_meaning = user_matches[phrase]
            is_correct = user_meaning == correct_meaning
            
            annotated_text(
                (phrase, "", "#8ef" if is_correct else "#faa"),
                " → ",
                (correct_meaning, "", "#afa" if is_correct else "#faa")
            )
            st.write("")
    
    st.write("---")
    
    # Reflective writing section
    show_reflective_writing("monkeys")

def show_reflective_writing(animal_type):
    st.subheader(f"Reflective Writing: My Experience with {animal_type.capitalize()}")
    
    st.markdown(f"""
    Now, write about a personal encounter you've had with {animal_type}. This could be:
    - A time you saw {animal_type} in nature or at a zoo
    - An interesting documentary you watched about {animal_type}
    - A memorable story you heard about {animal_type}
    
    Try to include details about their appearance, behavior, and how you felt during this experience.
    """)
    
    # Text area for reflection
    reflection = st.text_area(
        "Write your reflection here (aim for at least 100 words):",
        height=200,
        key=f"reflection_{animal_type}"
    )
    
    # Submit button for reflection
    if st.button("Submit Reflection", key=f"submit_{animal_type}"):
        if len(reflection.split()) < 30:
            st.error("Please write a bit more to complete this reflection (at least 30 words).")
        else:
            st.success("Thank you for sharing your reflection!")
            
            # Show self-assessment checklist
            st.subheader("Self-Assessment Checklist")
            st.write("Check the elements you included in your reflection:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                described = st.checkbox(f"I described the {animal_type} I encountered")
                appearance = st.checkbox(f"I described the appearance of the {animal_type}")
            
            with col2:
                behavior = st.checkbox(f"I described the behavior of the {animal_type}")
                feelings = st.checkbox(f"I wrote about how I felt during this experience")
            
            # Feedback based on checklist
            total_checked = sum([described, appearance, behavior, feelings])
            
            if total_checked == 4:
                st.balloons()
                st.success("Excellent! You included all the important elements in your reflection.")
            elif total_checked >= 2:
                st.success("Good job! You've included several important elements in your reflection.")
            else:
                st.info("Consider adding more details about the appearance, behavior, and your feelings to make your reflection more vivid.")
            
            # Option to save or download reflection (placeholder)
            st.info("Copy your writing into your exercise book, so you can show your teacher at school. Well done!")

if __name__ == "__main__":
    show()
