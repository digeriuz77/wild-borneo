{
                    'question': 'Why do kingfishers need to adjust their trajectory when diving?',
                    'options': ['To avoid predators', 'To compensate for light refraction', 'To maintain body temperature'],
                    'answer': 'To compensate for light refraction'
                },
                {
                    'question': 'What term describes the process of seed dispersal through animal digestive systems?',
                    'options': ['Endozoochory', 'Anemochory', 'Epizoochory'],
                    'answer': 'Endozoochory'
                },
                {
                    'question': 'What ecological role do hornbills serve in Bornean forests?',
                    'options': ['Apex predators', 'Keystone dispersers', 'Pollinating agents'],
                    'answer': 'Keystone dispersers'
                },
                {
                    'question': 'What is the function of the pneumatized casque in hornbills?',
                    'options': ['Temperature regulation', 'Storage of fat reserves', 'Resonating chamber for vocalizations'],
                    'answer': 'Resonating chamber for vocalizations'
                }
            ]
        }
    },
    'monkeys': {
        'easy': {
            'text': """
            Monkeys in Borneo live in groups to stay safe. They have leaders who decide where the group goes and who gets food first. They make special sounds to tell each other about danger or where to find food.
            
            Most monkeys in Borneo stay in the trees all the time. They have strong arms and legs for climbing and jumping from branch to branch. Some can jump very far without falling.
            
            Different types of monkeys eat different foods. Some eat fruits and leaves, while others also eat insects and small animals. This helps them all find enough food in the same forest.
            """,
            'questions': [
                {
                    'question': 'Why do monkeys in Borneo live in groups?',
                    'options': ['To stay safe', 'To stay warm', 'To find water'],
                    'answer': 'To stay safe'
                },
                {
                    'question': 'Where do most Borneo monkeys spend their time?',
                    'options': ['In the water', 'On the ground', 'In the trees'],
                    'answer': 'In the trees'
                },
                {
                    'question': 'Why do different monkeys eat different foods?',
                    'options': ['They are picky eaters', 'So they can all find enough food', 'They have different colored fur'],
                    'answer': 'So they can all find enough food'
                }
            ]
        },
        'medium': {
            'text': """
            Monkeys in Borneo are **highly adaptive** creatures that rely on social groups for survival. Living in **hierarchical** communities, they develop complex social bonds that determine access to food, mates, and safe sleeping sites. Each group has a unique set of vocalizations to communicate danger or food location.
            
            Many species are **arboreal**, spending most of their lives in the trees, rarely coming down to the ground. Their strong limbs allow them to move with amazing **agility** through the forest canopy, leaping between branches that might be several meters apart.
            
            Borneo's monkeys have developed **specialized** diets that prevent competition for the same food sources. While some are **omnivorous**, eating both plants and small animals, others are strictly **herbivorous**, feeding only on leaves, fruits, and flowers from specific trees in their territory.
            """,
            'questions': [
                {
                    'question': 'What does "arboreal" mean?',
                    'options': ['Living in the water', 'Living on the ground', 'Living in trees'],
                    'answer': 'Living in trees'
                },
                {
                    'question': 'What kind of diet do all monkeys in Borneo have?',
                    'options': ['They all eat the same food', 'They have specialized diets', 'They only eat meat'],
                    'answer': 'They have specialized diets'
                },
                {
                    'question': 'What does "hierarchical" refer to?',
                    'options': ['Having ranks or levels', 'Being very tall', 'Having bright colors'],
                    'answer': 'Having ranks or levels'
                },
                {
                    'question': 'What helps monkeys move through the forest canopy?',
                    'options': ['Their agility', 'Their large size', 'Their bright colors'],
                    'answer': 'Their agility'
                }
            ]
        },
        'hard': {
            'text': """
            Primates of Borneo exhibit remarkable **behavioral plasticity** and **social cognition** within their **multi-level fission-fusion societies**. These **conspecific aggregations** establish **dominance hierarchies** governing resource allocation, mate selection, and territorial defense through complex **agonistic-affiliative interactions**. Their **paralinguistic communication** includes **species-specific vocalizations** and **gestural repertoires** that demonstrate **referential signaling** capabilities.
            
            The predominantly **arboreal locomotion** of these species has resulted in specialized **brachiation adaptations** and **anatomical preadaptations** for efficient **three-dimensional navigation** within the forest **stratification**. Their remarkable **proprioceptive acuity** enables precise trajectory calculation during **suspensory progression** and **quadrumanous climbing**, even across **discontinuous substrates** in the forest canopy.
            
            **Resource partitioning** among sympatric primate species in Borneo demonstrates classic **niche differentiation** strategies. Some exhibit **dietary specialization** as **folivores** with complex **foregut fermentation** systems, while others are **frugivore-insectivores** with **generalist dentition**. This **trophic differentiation** minimizes **interspecific competition** and promotes **ecological coexistence** within the same forest ecosystem.
            """,
            'questions': [
                {
                    'question': 'What term describes the ability of primates to adapt their behavior to different situations?',
                    'options': ['Social cognition', 'Behavioral plasticity', 'Paralinguistic communication'],
                    'answer': 'Behavioral plasticity'
                },
                {
                    'question': 'What type of society structure do many Bornean primates exhibit?',
                    'options': ['Solitary territories', 'Static hierarchies', 'Multi-level fission-fusion societies'],
                    'answer': 'Multi-level fission-fusion societies'
                },
                {
                    'question': 'What adaptation allows certain monkey species to swing from branch to branch?',
                    'options': ['Brachiation adaptations', 'Proprioceptive acuity', 'Quadrumanous climbing'],
                    'answer': 'Brachiation adaptations'
                },
                {
                    'question': 'What ecological concept explains how different monkey species can coexist in the same forest?',
                    'options': ['Competitive exclusion', 'Niche differentiation', 'Character displacement'],
                    'answer': 'Niche differentiation'
                },
                {
                    'question': 'What term describes leaf-eating monkeys?',
                    'options': ['Frugivores', 'Folivores', 'Omnivores'],
                    'answer': 'Folivores'
                }
            ]
        }
    }
}

# Helper function for download button
def download_button(object_to_download, download_filename, button_text):
    """
    Generates a download button for the text
    """
    if isinstance(object_to_download, str):
        b64 = base64.b64encode(object_to_download.encode()).decode()
    else:
        b64 = base64.b64encode(object_to_download).decode()

    button_uuid = str(random.randint(0, 10000))
    button_id = re.sub(r'\d+', '', button_uuid)

    custom_css = f""" 
        <style>
            #{button_id} {{
                background-color: #4CAF50;
                color: white;
                padding: 14px 20px;
                margin: 8px 0;
                border: none;
                cursor: pointer;
                width: 100%;
                border-radius: 10px;
                font-size: 16px;
            }}
            #{button_id}:hover {{
                background-color: #45a049;
            }}
        </style> """

    dl_link = custom_css + f'<a download="{download_filename}" id="{button_id}" href="data:text/plain;base64,{b64}">{button_text}</a><br>'
    return dl_link

# Theme toggle function
def add_theme_toggle():
    # Toggle function
    def toggle_theme():
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
    
    # Theme toggle in sidebar
    with st.sidebar:
        st.button("Toggle Dark/Light Mode", on_click=toggle_theme)
    
    # Apply the theme
    if st.session_state.theme == "dark":
        dark_theme_css = """
        <style>
            .main {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            .stButton button {
                background-color: #2E7D32;
                color: white;
            }
            .wildlife-card {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            .fact-box {
                background-color: #2D3A3A;
                color: #FFFFFF;
                border-left: 5px solid #2e7d32;
            }
            .word-bank {
                background-color: #2D3A3A;
                color: #FFFFFF;
            }
            .grammar-card {
                background-color: #2D3A3A;
                color: #FFFFFF;
            }
            .sentence-box {
                background-color: #333333;
                color: #FFFFFF;
                border: 1px solid #555555;
            }
            .sentence-box:hover {
                background-color: #444444;
            }
            .sentence-box-selected {
                background-color: #1E3A2F;
                border: 1px solid #2e7d32;
            }
            .timer-box {
                background-color: #2D3A3A;
                color: #FFFFFF;
            }
            .reading-line {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            .st-bq {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            .st-cc {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            .st-cd {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            .st-c0 {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            /* Override Streamlit's default text color */
            p, h1, h2, h3, h4, h5, h6, li, label {
                color: #FFFFFF !important;
            }
            /* Fix for radio buttons and checkboxes */
            .stRadio > div {
                color: #FFFFFF !important;
            }
            /* Fix for text inputs */
            .stTextInput input {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            /* Fix for text areas */
            .stTextArea textarea {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
        </style>
        """
        st.markdown(dark_theme_css, unsafe_allow_html=True)

# Home page
def show_home():
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

# Species identification activity
def show_identification():
    st.title(f"🔍 Identify the {st.session_state.pathway.rstrip('s')}!")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_radio",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_radio))
    
    with col2:
        species_list = SPECIES_DATA[st.session_state.pathway]
        
        # Ensure current_species_index is valid
        if st.session_state.current_species_index >= len(species_list):
            st.session_state.current_species_index = 0
        
        species = species_list[st.session_state.current_species_index]
        
        # Display the species image
        try:
            st.image(species['image'], use_container_width=True)
        except Exception as e:
            st.error(f"Could not load image: {species['image']}")
            st.info("Using placeholder image")
            st.image("https://via.placeholder.com/400x300?text=Wildlife+Image", use_container_width=True)
        
        # Store the correct answer
        correct_answer = species['name']
        
        # Create a shuffled version of options if not already in session state
        option_key = f"shuffled_options_{st.session_state.pathway}_{st.session_state.current_species_index}"
        if option_key not in st.session_state:
            shuffled_options = species['options'].copy()
            random.shuffle(shuffled_options)
            st.session_state[option_key] = shuffled_options
        
        # Multiple choice question with shuffled options
        answer = st.radio("What species is this?", st.session_state[option_key], key="species_radio")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            # Check answer button
            if not st.session_state.answer_checked:
                if st.button("Check Answer", key="check_button"):
                    st.session_state.answer_checked = True
                    st.session_state.total_questions += 1
                    
                    if answer == correct_answer:
                        st.session_state.correct_answers += 1
                        st.success("✅ Correct! Well done!")
                    else:
                        st.error(f"❌ Not quite. This is a {correct_answer}.")
        
        with col_b:
            # Next button (always visible)
            if st.button("Next Species", key="next_button"):
                st.session_state.answer_checked = False
                # Move to the next species
                st.session_state.current_species_index = (st.session_state.current_species_index + 1) % len(species_list)
                st.rerun()
        
        # Display fact box if answer has been checked
        if st.session_state.answer_checked:
            st.markdown(f"""
            <div class="fact-box">
                <h3>📚 Fact about the {species['name']}</h3>
                <p>{species['fact']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Display score
        st.info(f"Your score: {st.session_state.correct_answers}/{st.session_state.total_questions}")
        
        # Check if all species have been shown
        total_species = len(species_list)
        species_seen = min(st.session_state.total_questions, total_species)
        
        # Show completion message and button when all species have been seen
        if species_seen >= total_species:
            st.success(f"You've completed all {total_species} {st.session_state.pathway}! Great job!")
            
            # Button to move to the next activity
            if st.button("Continue to Reading & Comprehension", use_container_width=True):
                st.session_state.active_section = "comprehension"
                st.rerun()

# Description matching activity
def show_description_matching():
    st.title(f"🔍 Match Descriptions: {st.session_state.pathway.title()}")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_desc",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_desc))
    
    with col2:
        species_list = SPECIES_DATA[st.session_state.pathway]
        
        st.markdown("""
        ### Match each description to the correct animal
        
        Read each description carefully and select the animal you think it describes.
        """)
        
        # Initialize matches in session state if not exists
        if 'description_matches' not in st.session_state:
            st.session_state.description_matches = {}
        
        # Shuffled descriptions
        if 'shuffled_descriptions' not in st.session_state:
            descriptions = [(species['name'], species['description']) for species in species_list]
            random.shuffle(descriptions)
            st.session_state.shuffled_descriptions = descriptions
        
        # Display each description with a dropdown to select the animal
        correct_count = 0
        for i, (correct_name, description) in enumerate(st.session_state.shuffled_descriptions):
            st.markdown(f"**Description {i+1}:** {description}")
            
            # Extract all animal names for the dropdown
            all_names = [species['name'] for species in species_list]
            
            # Dropdown for selection
            selected = st.selectbox(
                f"Which animal does this describe?", 
                all_names,
                key=f"description_{i}"
            )
            
            # Record the selection
            st.session_state.description_matches[i] = selected
            
            # Check if correct
            if st.session_state.description_submitted:
                if selected == correct_name:
                    st.success("✅ Correct!")
                    correct_count += 1
                else:
                    st.error(f"❌ Incorrect. This description is for the {correct_name}.")
            
            st.markdown("---")
        
        # Submit button
        col_a, col_b = st.columns(2)
        
        with col_a:
            if not st.session_state.description_submitted:
                if st.button("Check Matches", key="check_description"):
                    st.session_state.description_submitted = True
                    st.rerun()
        
        with col_b:
            if st.button("Reset Activity", key="reset_description"):
                # Clear the matches and shuffle
                st.session_state.description_matches = {}
                del st.session_state.shuffled_descriptions
                st.session_state.description_submitted = False
                st.rerun()
        
        # Display score if submitted
        if st.session_state.description_submitted:
            total = len(st.session_state.shuffled_descriptions)
            st.success(f"You matched {correct_count} out of {total} descriptions correctly!")
            
            # Check if all correct
            if correct_count == total:
                st.balloons()
                st.markdown("### 🎉 Perfect score! You're an expert on Brunei wildlife!")

# Reading comprehension activity with scrollable container
def show_comprehension():
    st.title(f"📚 Reading & Comprehension: {st.session_state.pathway.title()}")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_comp",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_comp))
        
        # Difficulty selector
        st.session_state.comprehension_difficulty = st.radio(
            "Select difficulty:",
            options=['easy', 'medium', 'hard'],
            index=['easy', 'medium', 'hard'].index(st.session_state.comprehension_difficulty)
        )
    
    with col2:
        data = COMPREHENSION_DATA[st.session_state.pathway][st.session_state.comprehension_difficulty]
        
        # Display the reading passage with a scrollable container
        st.markdown("""
        <div class="wildlife-card" style="max-height: 300px; overflow-y: auto; padding-right: 10px;">
            <h3>Reading Passage</h3>
            {}
        </div>
        <style>
            /* Custom scrollbar styling */
            .wildlife-card::-webkit-scrollbar {
                width: 8px;
            }
            .wildlife-card::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 10px;
            }
            .wildlife-card::-webkit-scrollbar-thumb {
                background: #888;
                border-radius: 10px;
            }
            .wildlife-card::-webkit-scrollbar-thumb:hover {
                background: #555;
            }
            /* Adjust for dark mode if active */
            .dark-mode .wildlife-card::-webkit-scrollbar-track {
                background: #333;
            }
            .dark-mode .wildlife-card::-webkit-scrollbar-thumb {
                background: #666;
            }
            .dark-mode .wildlife-card::-webkit-scrollbar-thumb:hover {
                background: #888;
            }
        </style>
        """.format(data['text']), unsafe_allow_html=True)
        
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
                if st.button("Check Answers", key="check_comp"):
                    st.session_state.comprehension_submitted = True
                    st.rerun()
        
        with col_b:
            if st.button("Reset Questions", key="reset_comp"):
                st.session_state.comprehension_submitted = False
                st.rerun()
        
        # Display score if submitted
        if st.session_state.comprehension_submitted:
            score_percentage = (correct_answers / total_questions) * 100
            
            if score_percentage >= 80:
                st.success(f"**Great job! Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%)**")
                if st.session_state.comprehension_difficulty != 'hard':
                    st.info(f"Ready for a challenge? Try the {['medium', 'hard'][st.session_state.comprehension_difficulty == 'medium']} difficulty!")
            elif score_percentage >= 60:
                st.info(f"**Good effort! Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%)**")
            else:
                st.warning(f"**Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%). Keep practicing!**")
                if st.session_state.comprehension_difficulty != 'easy':
                    st.info(f"Try the {['easy', 'medium'][st.session_state.comprehension_difficulty == 'hard']} difficulty to build your skills.")

# Reading speed assessment activity
def show_reading_speed():
    st.title("⏱️ Reading Speed Assessment")
    
    # Instructions
    st.markdown("""
    ### Test your reading speed with this one-minute challenge!
    
    1. Press the "Start Reading" button to begin
    2. Use the ⬇️ DOWN ARROW key on your keyboard to reveal each new line of text
    3. Read as many lines as you can in one minute
    4. Your reading speed will be calculated automatically when time is up
    """)
    
    # Initialize or reset the activity
    if 'reading_timer_active' not in st.session_state or st.button("Reset", key="reset_reading"):
        st.session_state.reading_timer_active = False
        st.session_state.reading_timer_start = None
        st.session_state.reading_lines_revealed = 0
        st.session_state.reading_finished = False
    
    # Start button
    if not st.session_state.reading_timer_active and not st.session_state.reading_finished:
        if st.button("Start Reading", key="start_reading"):
            st.session_state.reading_timer_active = True
            st.session_state.reading_timer_start = datetime.now()
            st.session_state.reading_lines_revealed = 1
            st.rerun()
    
    # Display timer if active
    if st.session_state.reading_timer_active:
        elapsed_time = datetime.now() - st.session_state.reading_timer_start
        remaining_time = 60 - elapsed_time.total_seconds()
        
        if remaining_time <= 0:
            st.session_state.reading_timer_active = False
            st.session_state.reading_finished = True
            remaining_time = 0
            st.rerun()
        
        # Format time as MM:SS
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        
        # Display timer
        st.markdown(f"""
        <div class="timer-box">
            Time remaining: {minutes:02d}:{seconds:02d}
        </div>
        """, unsafe_allow_html=True)
    
    # Create a container for the reading text
    reading_container = st.container()
    
    # Display the revealed lines
    with reading_container:
        if st.session_state.reading_timer_active or st.session_state.reading_finished:
            for i in range(min(st.session_state.reading_lines_revealed, len(READING_SPEED_TEXT))):
                st.markdown(f"""
                <div class="reading-line">
                    {READING_SPEED_TEXT[i]}
                </div>
                """, unsafe_allow_html=True)
    
    # Handle key press for revealing next line
    if st.session_state.reading_timer_active:
        # This is a placeholder - in streamlit we can't actually capture keyboard events directly
        # We'll use a workaround with a button
        if st.button("⬇️ Next Line (Press Down Arrow)", key="reveal_next"):
            st.session_state.reading_lines_revealed += 1
            st.rerun()
        
        st.info("Press your keyboard's DOWN ARROW key to reveal the next line, or click the button above.")
    
    # Show results when finished
    if st.session_state.reading_finished:
        lines_read = st.session_state.reading_lines_revealed - 1  # Subtract first line that's shown automatically
        # Count words in the read lines
        words_read = sum(len(line.split()) for line in READING_SPEED_TEXT[:lines_read])
        
        st.success(f"Time's up! You read {lines_read} lines containing approximately {words_read} words.")
        
        # Calculate reading speed (words per minute)
        wpm = words_read
        
        # Provide feedback based on reading speed
        if wpm >= 250:
            st.markdown(f"### Your reading speed: {wpm} words per minute (Advanced)")
            st.info("Great job! You have above-average reading speed.")
        elif wpm >= 150:
            st.markdown(f"### Your reading speed: {wpm} words per minute (Average)")
            st.info("Good job! You have average reading speed.")
        else:
            st.markdown(f"### Your reading speed: {wpm} words per minute (Developing)")
            st.info("Keep practicing! Regular reading will help improve your speed.")

# Grammar practice with "to be" verb forms
def show_grammar_practice():
    st.title("📝 Grammar Practice: 'To Be' Verb Forms")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Difficulty selector
        st.session_state.grammar_level = st.radio(
            "Select difficulty:",
            options=['easy', 'medium', 'hard'],
            index=['easy', 'medium', 'hard'].index(st.session_state.grammar_level)
        )
        
        # Reset button
        if st.button("New Exercise", key="new_grammar"):
            st.session_state.grammar_exercise_index = (st.session_state.grammar_exercise_index + 1) % len(GRAMMAR_EXERCISES[st.session_state.grammar_level])
            st.session_state.grammar_answers = []
            st.session_state.grammar_submitted = False
            st.rerun()
    
    with col2:
        # Get current exercise based on level and index
        exercises = GRAMMAR_EXERCISES[st.session_state.grammar_level]
        current_exercise = exercises[st.session_state.grammar_exercise_index % len(exercises)]
        
        st.markdown(f"""
        <div class="grammar-card">
            <h3>{current_exercise['title']}</h3>
            <p>{current_exercise['instructions']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize grammar_answers if empty
        if not st.session_state.grammar_answers:
            st.session_state.grammar_answers = [[] for _ in range(len(current_exercise['exercises']))]
        
        # Display each sentence exercise
        correct_count = 0
        for i, exercise in enumerate(current_exercise['exercises']):
            st.markdown(f"**Sentence {i+1}**")
            
            # Create columns for the words
            col_words = st.columns(len(exercise['words']))
            
            # Get current order of words for this exercise
            if len(st.session_state.grammar_answers[i]) == 0:
                # Initialize with shuffled words if first time
                shuffled_words = exercise['words'].copy()
                random.shuffle(shuffled_words)
                st.session_state.grammar_answers[i] = shuffled_words
            
            # Display current order of words
            st.markdown("**Current sentence:**")
            current_sentence = " ".join(st.session_state.grammar_answers[i])
            st.markdown(f"<div class='sentence-box'>{current_sentence}</div>", unsafe_allow_html=True)
            
            # Display individual words that can be moved
            st.markdown("**Arrange these words:**")
            
            # Create multiple columns for word buttons
            cols = st.columns(min(6, len(exercise['words'])))
            
            # Function to move a word up in the sentence
            def move_word_left(word_index, sentence_index):
                if word_index > 0:
                    current_words = st.session_state.grammar_answers[sentence_index]
                    current_words[word_index], current_words[word_index-1] = current_words[word_index-1], current_words[word_index]
                    st.session_state.grammar_answers[sentence_index] = current_words
            
            # Function to move a word down in the sentence
            def move_word_right(word_index, sentence_index):
                current_words = st.session_state.grammar_answers[sentence_index]
                if word_index < len(current_words) - 1:
                    current_words[word_index], current_words[word_index+1] = current_words[word_index+1], current_words[word_index]
                    st.session_state.grammar_answers[sentence_index] = current_words
            
            # Display each word with movement buttons
            for j, word in enumerate(st.session_state.grammar_answers[i]):
                col_idx = j % len(cols)
                with cols[col_idx]:
                    st.markdown(f"**{word}**")
                    
                    # Left/right buttons
                    left_disabled = j == 0
                    right_disabled = j == len(st.session_state.grammar_answers[i]) - 1
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if not left_disabled:
                            if st.button("⬅️", key=f"left_{i}_{j}"):
                                move_word_left(j, i)
                                st.rerun()
                    with col2:
                        if not right_disabled:
                            if st.button("➡️", key=f"right_{i}_{j}"):
                                move_word_right(j, i)
                                st.rerun()
            
            # Check if this sentence is correct
            current_answer = " ".join(st.session_state.grammar_answers[i])
            is_correct = current_answer == exercise['correct']
            
            # Show feedback if submitted
            if st.session_state.grammar_submitted:
                if is_correct:
                    st.success("✅ Correct!")
                    correct_count += 1
                else:
                    st.error(f"❌ Not quite right. The correct sentence is: \"{exercise['correct']}\"")
            
            st.markdown("---")
        
        # Submit button
        if not st.session_state.grammar_submitted:
            if st.button("Check My Sentences", key="check_grammar"):
                st.session_state.grammar_submitted = True
                st.rerun()
        
        # Display score if submitted
        if st.session_state.grammar_submitted:
            total = len(current_exercise['exercises'])
            st.success(f"Score: {correct_count}/{total} correct sentences")
            
            # Check if all correct
            if correct_count == total:
                st.balloons()
                st.markdown("### 🎉 Perfect! You've mastered these 'to be' verb forms!")
                
                # Suggest next level if not on hard
                if st.session_state.grammar_level != 'hard':
                    next_level = 'medium' if st.session_state.grammar_level == 'easy' else 'hard'
                    st.info(f"Why not try the {next_level} level next?")

# Main app
def main():
    # Add theme toggle functionality
    add_theme_toggle()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    
    # Simple direct navigation buttons
    if st.sidebar.button("🏠 Home"):
        st.session_state.active_section = "home"
    
    if st.sidebar.button("🔍 Wildlife Identification"):
        st.session_state.active_section = "identification"
    
    if st.sidebar.button("🔤 Match Descriptions"):
        st.session_state.active_section = "description_matching"
    
    if st.sidebar.button("📚 Reading & Comprehension"):
        st.session_state.active_section = "comprehension"
    
    if st.sidebar.button("⏱️ Reading Speed Test"):
        st.session_state.active_section = "reading_speed"
    
    if st.sidebar.button("📝 Grammar Practice"):
        st.session_state.active_section = "grammar"
    
    # Score display in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current pathway:** {st.session_state.pathway.title()}")
    if st.session_state.active_section == "identification":
        st.sidebar.markdown(f"**Identification score:** {st.session_state.correct_answers}/{st.session_state.total_questions}")
    
    # Reset button
    st.sidebar.markdown("---")
    if st.sidebar.button("Reset All Progress"):
        for key in list(st.session_state.keys()):
            if key != 'theme':  # Preserve theme setting
                del st.session_state[key]
        
        # Reinitialize essential state
        st.session_state.pathway = 'birds'
        st.session_state.active_section = "home"
        st.session_state.current_species_index = 0
        st.session_state.answer_checked = False
        st.session_state.correct_answers = 0
        st.session_state.total_questions = 0
        st.session_state.comprehension_difficulty = 'easy'
        st.session_state.comprehension_submitted = False
        st.session_state.vocab_submitted = False
        st.session_state.vocabulary_answers = {}
        st.session_state.paragraph_level = 'easy'
        st.session_state.paragraph_version = 0
        st.session_state.shuffled_sentences = []
        st.session_state.reflection_text = ""
        st.session_state.reading_timer_active = False
        st.session_state.reading_timer_start = None
        st.session_state.reading_lines_revealed = 0
        st.session_state.reading_finished = False
        st.session_state.grammar_level = 'easy'
        st.session_state.grammar_exercise_index = 0
        st.session_state.grammar_answers = []
        st.session_state.grammar_submitted = False
        st.rerun()
    
    # Display the selected section
    if st.session_state.active_section == "home":
        show_home()
    elif st.session_state.active_section == "identification":
        show_identification()
    elif st.session_state.active_section == "description_matching":
        show_description_matching()
    elif st.session_state.active_section == "comprehension":
        show_comprehension()
    elif st.session_state.active_section == "reading_speed":
        show_reading_speed()
    elif st.session_state.active_section == "grammar":
        show_grammar_practice()

if __name__ == "__main__":
    main()import streamlit as st
import random
import base64
import re
import time
from datetime import datetime, timedelta
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Borneo Wildlife Explorer",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visual appeal
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    h1, h2, h3 {
        color: #2e7d32;
    }
    .stButton button {
        background-color: #43a047;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        margin: 0.5rem 0;
    }
    .stButton button:hover {
        background-color: #2e7d32;
    }
    .wildlife-card {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .correct-answer {
        color: #2e7d32;
        font-weight: bold;
    }
    .incorrect-answer {
        color: #c62828;
        font-weight: bold;
    }
    .fact-box {
        background-color: #e8f5e9;
        border-left: 5px solid #2e7d32;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 10px 10px 0;
        color: #333333;
    }
    .word-bank {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .timer-box {
        background-color: #fff3e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .reading-line {
        font-size: 1.2rem;
        margin: 0.5rem 0;
        padding: 0.5rem;
        background-color: #f5f5f5;
        border-radius: 5px;
        display: block;
    }
    .grammar-card {
        background-color: #e1f5fe;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sentence-box {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.5rem 0;
        cursor: pointer;
    }
    .sentence-box:hover {
        background-color: #f0f0f0;
    }
    .sentence-box-selected {
        background-color: #e8f5e9;
        border: 1px solid #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'pathway' not in st.session_state:
    st.session_state.pathway = 'birds'  # Default pathway
if 'current_species_index' not in st.session_state:
    st.session_state.current_species_index = 0
if 'answer_checked' not in st.session_state:
    st.session_state.answer_checked = False
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0
if 'comprehension_difficulty' not in st.session_state:
    st.session_state.comprehension_difficulty = 'easy'
if 'comprehension_submitted' not in st.session_state:
    st.session_state.comprehension_submitted = False
if 'vocab_submitted' not in st.session_state:
    st.session_state.vocab_submitted = False
if 'vocabulary_answers' not in st.session_state:
    st.session_state.vocabulary_answers = {}
if 'paragraph_level' not in st.session_state:
    st.session_state.paragraph_level = 'easy'
if 'paragraph_version' not in st.session_state:
    st.session_state.paragraph_version = 0
if 'shuffled_sentences' not in st.session_state:
    st.session_state.shuffled_sentences = []
if 'reflection_text' not in st.session_state:
    st.session_state.reflection_text = ""
if 'active_section' not in st.session_state:
    st.session_state.active_section = "home"
if 'reading_timer_active' not in st.session_state:
    st.session_state.reading_timer_active = False
if 'reading_timer_start' not in st.session_state:
    st.session_state.reading_timer_start = None
if 'reading_lines_revealed' not in st.session_state:
    st.session_state.reading_lines_revealed = 0
if 'reading_finished' not in st.session_state:
    st.session_state.reading_finished = False
if 'grammar_level' not in st.session_state:
    st.session_state.grammar_level = 'easy'
if 'grammar_exercise_index' not in st.session_state:
    st.session_state.grammar_exercise_index = 0
if 'grammar_answers' not in st.session_state:
    st.session_state.grammar_answers = []
if 'grammar_submitted' not in st.session_state:
    st.session_state.grammar_submitted = False
if 'description_matching_done' not in st.session_state:
    st.session_state.description_matching_done = False
if 'theme' not in st.session_state:
    st.session_state.theme = "light"  # Default theme

# Species data using local images
SPECIES_DATA = {
    'birds': [
        {
            'name': 'Brahminy Kite',
            'image': 'images/Brahminy_kite.jpg',
            'options': ['Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch', 'Collared Kingfisher'],
            'fact': 'The Brahminy Kite is a medium-sized bird of prey found in Borneo. With its distinctive reddish-brown plumage and white head, it\'s often seen soaring over coastal areas and wetlands, searching for fish and small animals.',
            'description': 'This bird has a striking white head and chest with reddish-brown wings and body. It often soars above coastal areas looking for fish and can be seen perched on tall trees near water.'
        },
        {
            'name': 'Cattle Egret',
            'image': 'images/Cattle_egret.jpg',
            'options': ['Cattle Egret', 'Brahminy Kite', 'Oriental Pied Hornbill', 'Collared Kingfisher'],
            'fact': 'The Cattle Egret is a white heron that often follows cattle and other large animals, feeding on insects disturbed by their movement. During breeding season, they develop orange-buff plumage on their head, back, and chest.',
            'description': 'A small white bird that is often seen following cattle or water buffalo in fields. During breeding season, it develops orange-colored patches on its head and chest.'
        },
        {
            'name': 'Chestnut Munia Finch',
            'image': 'images/Chestnut_munia_finch.jpg',
            'options': ['Chestnut Munia Finch', 'Cattle Egret', 'Brahminy Kite', 'Oriental Pied Hornbill'],
            'fact': 'The Chestnut Munia is a small finch with rich chestnut-brown upperparts and a black face and belly. They live in flocks and feed mainly on grass seeds. Their nests are round, woven structures usually built in tall grass or bushes.',
            'description': 'This small bird has a rich brown back and wings with a black face and belly. It moves in flocks and enjoys eating seeds from grasses and plants.'
        },
        {
            'name': 'Collared Kingfisher',
            'image': 'images/collared_kingfisher.jpg',
            'options': ['Collared Kingfisher', 'Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch'],
            'fact': 'The Collared Kingfisher has striking blue and white plumage with a distinctive white collar. Unlike many kingfishers, it doesn\'t only eat fish but feeds on a variety of prey including lizards, crabs, and insects.',
            'description': 'A bright blue bird with white areas on its neck and belly. It has a long, strong beak for catching prey and makes a distinctive loud call.'
        },
        {
            'name': 'Oriental Pied Hornbill',
            'image': 'images/Oriental_Pied_Hornbill.jpg',
            'options': ['Oriental Pied Hornbill', 'Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch'],
            'fact': 'The Oriental Pied Hornbill has a distinctive black and white plumage with a large yellow-white bill topped by a casque. During nesting, the female seals herself inside a tree cavity, leaving only a small slit through which the male feeds her.',
            'description': 'This large black and white bird has an enormous bill with a casque (horn-like structure) on top. It makes loud calls and can be seen flying between tall trees in the forest.'
        }
    ],
    'monkeys': [
        {
            'name': 'Proboscis Monkey',
            'image': 'images/Proboscis_Monkey_in_Borneo.jpg',
            'options': ['Proboscis Monkey', 'Macaque Monkey', 'Red Leaf Monkey', 'Silvered Leaf Monkey'],
            'fact': 'The Proboscis Monkey is endemic to Borneo and is known for its distinctive long nose. Males have huge noses that can grow up to 7 inches long, which they use to attract females and amplify their warning calls.',
            'description': 'This orange-colored monkey has a very long, drooping nose, especially in males. It lives near rivers and mangroves and is an excellent swimmer.'
        },
        {
            'name': 'Macaque Monkey',
            'image': 'images/macaque_monkey.jpg',
            'options': ['Macaque Monkey', 'Proboscis Monkey', 'Red Leaf Monkey', 'Silvered Leaf Monkey'],
            'fact': 'Macaques are highly adaptable monkeys found throughout Borneo. They live in large social groups with clear hierarchies and are known for their intelligence. They can use tools and solve complex problems to obtain food.',
            'description': 'A medium-sized brown monkey with a long tail, often found near human settlements. It lives in large social groups and is very intelligent and adaptable.'
        },
        {
            'name': 'Red Leaf Monkey',
            'image': 'images/Red_leaf_monkey.jpg',
            'options': ['Red Leaf Monkey', 'Proboscis Monkey', 'Macaque Monkey', 'Silvered Leaf Monkey'],
            'fact': 'The Red Leaf Monkey, also known as the Maroon Langur, has a distinctive dark maroon coat and a long tail. Babies are born with bright orange fur that gradually darkens as they age.',
            'description': 'This monkey has a dark reddish-brown coat and a very long tail. Its young babies have bright orange fur which darkens as they grow older.'
        },
        {
            'name': 'Silvered Leaf Monkey',
            'image': 'images/Silvered_Leaf_Monkey.jpg',
            'options': ['Silvered Leaf Monkey', 'Red Leaf Monkey', 'Proboscis Monkey', 'Macaque Monkey'],
            'fact': 'The Silvered Leaf Monkey has striking silver-tipped fur and a distinctive crest of hair on top of its head. They live in groups of 9-40 individuals and primarily eat leaves, making them true folivores.',
            'description': 'A dark monkey with silver-tipped fur that gives it a frosted appearance. It has a small crest of hair on its head and lives in large groups in the forest.'
        }
    ]
}

# Grammar exercises for "to be" verb forms
GRAMMAR_EXERCISES = {
    'easy': [
        {
            'title': 'Simple Present Tense with "to be"',
            'instructions': 'Arrange the words to make correct sentences using the present tense forms of "to be" (am/is/are).',
            'exercises': [
                {
                    'words': ['The', 'hornbill', 'is', 'a', 'large', 'bird'],
                    'correct': 'The hornbill is a large bird'
                },
                {
                    'words': ['Proboscis', 'monkeys', 'are', 'good', 'swimmers'],
                    'correct': 'Proboscis monkeys are good swimmers'
                },
                {
                    'words': ['I', 'am', 'learning', 'about', 'Brunei', 'wildlife'],
                    'correct': 'I am learning about Brunei wildlife'
                },
                {
                    'words': ['The', 'mangrove', 'forest', 'is', 'home', 'to', 'many', 'animals'],
                    'correct': 'The mangrove forest is home to many animals'
                },
                {
                    'words': ['We', 'are', 'visiting', 'the', 'nature', 'reserve', 'today'],
                    'correct': 'We are visiting the nature reserve today'
                }
            ]
        },
        {
            'title': 'Simple Past Tense with "to be"',
            'instructions': 'Arrange the words to make correct sentences using the past tense forms of "to be" (was/were).',
            'exercises': [
                {
                    'words': ['The', 'kingfisher', 'was', 'sitting', 'on', 'a', 'branch'],
                    'correct': 'The kingfisher was sitting on a branch'
                },
                {
                    'words': ['The', 'monkeys', 'were', 'eating', 'fruits', 'in', 'the', 'trees'],
                    'correct': 'The monkeys were eating fruits in the trees'
                },
                {
                    'words': ['I', 'was', 'watching', 'birds', 'yesterday'],
                    'correct': 'I was watching birds yesterday'
                },
                {
                    'words': ['We', 'were', 'hiking', 'in', 'the', 'rainforest'],
                    'correct': 'We were hiking in the rainforest'
                },
                {
                    'words': ['The', 'proboscis', 'monkey', 'was', 'swimming', 'across', 'the', 'river'],
                    'correct': 'The proboscis monkey was swimming across the river'
                }
            ]
        }
    ],
    'medium': [
        {
            'title': 'Present Continuous with "to be"',
            'instructions': 'Arrange the words to make correct sentences using present continuous tense (am/is/are + -ing verb).',
            'exercises': [
                {
                    'words': ['The', 'hornbill', 'is', 'building', 'a', 'nest', 'in', 'the', 'tree'],
                    'correct': 'The hornbill is building a nest in the tree'
                },
                {
                    'words': ['Scientists', 'are', 'studying', 'the', 'behavior', 'of', 'proboscis', 'monkeys'],
                    'correct': 'Scientists are studying the behavior of proboscis monkeys'
                },
                {
                    'words': ['The', 'leaf', 'monkeys', 'are', 'jumping', 'from', 'branch', 'to', 'branch'],
                    'correct': 'The leaf monkeys are jumping from branch to branch'
                },
                {
                    'words': ['I', 'am', 'taking', 'photos', 'of', 'wildlife', 'in', 'Brunei'],
                    'correct': 'I am taking photos of wildlife in Brunei'
                },
                {
                    'words': ['The', 'baby', 'macaques', 'are', 'playing', 'near', 'their', 'mothers'],
                    'correct': 'The baby macaques are playing near their mothers'
                }
            ]
        },
        {
            'title': 'Past Continuous with "to be"',
            'instructions': 'Arrange the words to make correct sentences using past continuous tense (was/were + -ing verb).',
            'exercises': [
                {
                    'words': ['The', 'kingfisher', 'was', 'hunting', 'for', 'fish', 'when', 'we', 'arrived'],
                    'correct': 'The kingfisher was hunting for fish when we arrived'
                },
                {
                    'words': ['The', 'monkeys', 'were', 'sleeping', 'in', 'the', 'trees', 'at', 'night'],
                    'correct': 'The monkeys were sleeping in the trees at night'
                },
                {
                    'words': ['We', 'were', 'watching', 'birds', 'when', 'it', 'started', 'to', 'rain'],
                    'correct': 'We were watching birds when it started to rain'
                },
                {
                    'words': ['The', 'guide', 'was', 'explaining', 'about', 'local', 'wildlife', 'yesterday'],
                    'correct': 'The guide was explaining about local wildlife yesterday'
                },
                {
                    'words': ['They', 'were', 'observing', 'a', 'family', 'of', 'proboscis', 'monkeys'],
                    'correct': 'They were observing a family of proboscis monkeys'
                }
            ]
        }
    ],
    'hard': [
        {
            'title': 'Mixed Tenses with "to be"',
            'instructions': 'Arrange the words to make correct sentences using appropriate forms of "to be" in different tenses.',
            'exercises': [
                {
                    'words': ['The', 'birds', 'are', 'migrating', 'now', 'but', 'some', 'species', 'were', 'here', 'all', 'year'],
                    'correct': 'The birds are migrating now but some species were here all year'
                },
                {
                    'words': ['If', 'I', 'am', 'lucky', 'I', 'will', 'see', 'the', 'rare', 'hornbill', 'that', 'was', 'spotted', 'yesterday'],
                    'correct': 'If I am lucky I will see the rare hornbill that was spotted yesterday'
                },
                {
                    'words': ['The', 'monkeys', 'were', 'eating', 'fruits', 'while', 'the', 'birds', 'were', 'singing', 'in', 'the', 'trees'],
                    'correct': 'The monkeys were eating fruits while the birds were singing in the trees'
                },
                {
                    'words': ['Although', 'it', 'is', 'rare', 'now', 'the', 'clouded', 'leopard', 'was', 'common', 'in', 'Brunei', 'forests'],
                    'correct': 'Although it is rare now the clouded leopard was common in Brunei forests'
                },
                {
                    'words': ['The', 'guide', 'said', 'we', 'are', 'fortunate', 'because', 'the', 'animals', 'were', 'very', 'active', 'today'],
                    'correct': 'The guide said we are fortunate because the animals were very active today'
                }
            ]
        },
        {
            'title': 'Complex Sentences with "to be"',
            'instructions': 'Arrange the words to form complex sentences using different forms of "to be" correctly.',
            'exercises': [
                {
                    'words': ['The', 'wildlife', 'sanctuary', 'which', 'is', 'located', 'near', 'the', 'coast', 'was', 'established', 'in', '1984'],
                    'correct': 'The wildlife sanctuary which is located near the coast was established in 1984'
                },
                {
                    'words': ['While', 'the', 'hornbill', 'is', 'feeding', 'its', 'young', 'the', 'female', 'is', 'sealed', 'inside', 'the', 'nest'],
                    'correct': 'While the hornbill is feeding its young the female is sealed inside the nest'
                },
                {
                    'words': ['If', 'they', 'are', 'disturbed', 'by', 'humans', 'the', 'proboscis', 'monkeys', 'will', 'dive', 'into', 'the', 'water'],
                    'correct': 'If they are disturbed by humans the proboscis monkeys will dive into the water'
                },
                {
                    'words': ['The', 'researchers', 'who', 'were', 'studying', 'monkey', 'behavior', 'are', 'publishing', 'their', 'findings', 'next', 'month'],
                    'correct': 'The researchers who were studying monkey behavior are publishing their findings next month'
                },
                {
                    'words': ['Although', 'they', 'are', 'endangered', 'now', 'efforts', 'are', 'being', 'made', 'to', 'ensure', 'their', 'survival'],
                    'correct': 'Although they are endangered now efforts are being made to ensure their survival'
                }
            ]
        }
    ]
}

# Reading speed assessment text
READING_SPEED_TEXT = """
Brunei's tropical rainforests are home to an astonishing variety of wildlife.
The country's commitment to forest preservation has made it a sanctuary for many species.
In the dense canopy, hornbills can be spotted flying between tall emergent trees.
These magnificent birds are known for their unique nesting habits and loud calls.
The proboscis monkey, with its distinctive long nose, is endemic to Borneo.
These endangered primates live in groups near rivers and mangroves.
They are excellent swimmers and can often be seen crossing rivers in search of food.
Brunei's mangrove forests support a rich ecosystem of birds, reptiles, and mammals.
The collared kingfisher hunts among the mangrove roots for small fish and crabs.
Its bright blue plumage contrasts beautifully with the muddy environment.
Clouded leopards are Brunei's largest wild cats, though they are rarely seen.
These secretive predators hunt at night, climbing trees with extraordinary agility.
The rainforest floor is home to many smaller creatures like the bearded pig.
These wild pigs play an important role in dispersing seeds throughout the forest.
Flying lizards can be spotted gliding between trees using their extended ribs.
These remarkable adaptations allow them to travel up to 30 meters in a single glide.
Brunei's rivers teem with life, including the fearsome saltwater crocodile.
These ancient reptiles can grow to enormous sizes in the undisturbed waterways.
Colorful butterflies like the Rajah Brooke's birdwing add splashes of color to the forest.
This protected species has distinctive black and green wings with a wingspan of up to 17 cm.
Orangutans, though rare in Brunei, occasionally appear in the remote forests.
These intelligent great apes build nests each night in different locations.
Conservation efforts in Brunei focus on preserving these diverse habitats.
Nearly 70% of the country remains covered in pristine primary forest.
This commitment to conservation ensures that Brunei's wildlife will continue to thrive.
Ecotourism provides opportunities to observe these animals in their natural settings.
Guided tours along rivers and through forests offer glimpses of this spectacular biodiversity.
Responsible tourism practices help protect these delicate ecosystems for future generations.
Research programs monitor wildlife populations and habitat health in Brunei.
Scientists use camera traps and field surveys to track elusive species.
Climate change poses new challenges for Brunei's wildlife conservation efforts.
Rising temperatures and changing rainfall patterns affect breeding cycles and food availability.
Community involvement is essential for successful wildlife protection.
Local knowledge and traditional practices often complement scientific approaches.
Education programs in schools raise awareness about Brunei's natural heritage.
Children learn about the importance of protecting wildlife and their habitats.
The government has established several protected areas and wildlife sanctuaries.
These protected zones restrict hunting and provide safe havens for many species.
International cooperation helps address cross-border conservation challenges.
Brunei works with Malaysia and Indonesia on initiatives to protect shared wildlife.
Sustainable forestry practices aim to balance economic needs with conservation.
Selective logging allows forests to regenerate while providing timber resources.
Brunei's wetlands are recognized internationally for their ecological importance.
They serve as critical stopover points for migratory birds along the East Asian-Australasian Flyway.
""".strip().split('\n')

# Vocabulary and comprehension data
COMPREHENSION_DATA = {
    'birds': {
        'easy': {
            'text': """
            Many birds in Borneo have **colorful** feathers that shine in the sunlight. These pretty colors help birds hide from danger or attract mates.
            
            Kingfishers have a special body shape that helps them dive into water very fast. They sit on branches above the water and wait for fish to swim by. Then they dive down quickly to catch them.
            
            Hornbills have very big beaks with a horn-like part on top. They eat fruits and help the forest by dropping seeds in different places. Their loud calls can be heard all through the forest.
            """,
            'questions': [
                {
                    'question': 'What do many birds in Borneo have?',
                    'options': ['Colorful feathers', 'Long tails', 'Sharp teeth'],
                    'answer': 'Colorful feathers'
                },
                {
                    'question': 'What do kingfishers do?',
                    'options': ['Build nests in the ground', 'Dive into water to catch fish', 'Sing beautiful songs'],
                    'answer': 'Dive into water to catch fish'
                },
                {
                    'question': 'How do hornbills help the forest?',
                    'options': ['By building nests', 'By dropping seeds in different places', 'By eating insects'],
                    'answer': 'By dropping seeds in different places'
                }
            ]
        },
        'medium': {
            'text': """
            Many birds in Borneo have **iridescent** feathers that shimmer in the sunlight. These colors aren't from pigments but come from the structure of the feathers that reflect light like tiny prisms. This helps birds with **camouflage** in the dense rainforest or attracts mates with brilliant displays.
            
            Kingfishers have a **streamlined** body, perfect for diving into the water at high speed. Their **aerodynamic** shape reduces water resistance, allowing them to catch fish with precision. Some species can dive from heights of 20 meters, adjusting their dive angle based on the position of their prey.
            
            Hornbills, known for their striking beaks, play an important role in **seed dispersal** by eating fruits and dropping seeds in different areas. Their **distinctive** casques (the horn-like structure above their bill) amplify their calls, which can be heard throughout the **canopy** of the rainforest.
            """,
            'questions': [
                {
                    'question': 'What does "iridescent" mean?',
                    'options': ['Shiny and colorful', 'Small and soft', 'Heavy and rough'],
                    'answer': 'Shiny and colorful'
                },
                {
                    'question': 'What helps kingfishers dive into the water?',
                    'options': ['Their large wings', 'Their streamlined body', 'Their long tail'],
                    'answer': 'Their streamlined body'
                },
                {
                    'question': 'What is a "casque" on a hornbill?',
                    'options': ['Their wing', 'The horn-like structure above their bill', 'Their tail feathers'],
                    'answer': 'The horn-like structure above their bill'
                },
                {
                    'question': 'How do hornbills help with seed dispersal?',
                    'options': ['By building nests', 'By eating fruits and dropping seeds', 'By breaking seeds open'],
                    'answer': 'By eating fruits and dropping seeds'
                }
            ]
        },
        'hard': {
            'text': """
            The avian species of Borneo exhibit remarkable **structural coloration** in their plumage, creating **iridescent** effects as light interacts with nanoscale features of their feathers. Unlike pigment-based colors, these **photonic structures** manipulate light waves through interference, diffraction, and scattering, producing the vibrant hues that serve dual purposes of **crypsis** in dense understory vegetation or **intersexual selection** displays.
            
            Alcedinidae species (kingfishers) possess extraordinarily **hydrodynamic** morphology optimized for high-velocity aquatic entry. Their **fusiform** body profile minimizes drag coefficient during the hunting dive, while specialized **cranial kinetics** allow precise trajectory adjustments in response to light refraction at the air-water interface, compensating for apparent displacement of prey items.
            
            Bucerotidae (hornbills) function as crucial **keystone dispersers** in forest ecosystems through **endozoochory** of large-seeded fruits. Their **pneumatized** casques serve as **resonating chambers** that amplify vocalizations across long distances in the forest **stratification**, facilitating both territorial defense and maintenance of pair bonds during nesting periods when females are sealed within tree cavities.
            """,
            'questions': [
                {
                    'question': 'What creates the iridescent effects in bird plumage?',
                    'options': ['Chemical pigments', 'Structural coloration', 'Ultraviolet radiation'],
                    'answer': 'Structural coloration'
                },
                {
                    'question': 'Why do kingfishers need to adjust their trajectory when diving?',
                    'options': ['To avoid predators', 'To compensate for light refraction', 'To maintain body temperature'],
                    'answer': 'To compensate for light refraction'
                },
