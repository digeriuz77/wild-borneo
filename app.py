import streamlit as st
import random
from PIL import Image
from io import BytesIO
import base64

# Set page configuration
st.set_page_config(
    page_title="Borneo Wildlife Explorer",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better mobile experience and visual appeal
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 2rem;
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
        width: 100%;
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
    }
    .word-bank {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stRadio > label {
        font-weight: bold;
    }
    .progress-tracker {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    .annotated {
        display: inline;
        border-radius: 0.25rem;
        padding: 0.125rem 0.25rem;
        margin: 0 0.125rem;
        background-color: #bbdefb;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'pathway' not in st.session_state:
    st.session_state.pathway = None
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0
if 'species_done' not in st.session_state:
    st.session_state.species_done = []
if 'vocab_done' not in st.session_state:
    st.session_state.vocab_done = False
if 'comprehension_done' not in st.session_state:
    st.session_state.comprehension_done = False
if 'comprehension_difficulty' not in st.session_state:
    st.session_state.comprehension_difficulty = 'easy'
if 'paragraph_level' not in st.session_state:
    st.session_state.paragraph_level = 'easy'
if 'paragraph_attempts' not in st.session_state:
    st.session_state.paragraph_attempts = 0
if 'paragraph_version' not in st.session_state:
    st.session_state.paragraph_version = 0
if 'reflection' not in st.session_state:
    st.session_state.reflection = ""

# Navigation functions
def go_to_page(page):
    st.session_state.page = page
    
def choose_pathway(pathway):
    st.session_state.pathway = pathway
    st.session_state.page = 'identification'
    st.session_state.species_done = []
    st.session_state.correct_answers = 0
    st.session_state.total_questions = 0

def next_species():
    if len(st.session_state.species_done) >= len(SPECIES_DATA[st.session_state.pathway]):
        go_to_page('comprehension')
    else:
        st.session_state.page = 'identification'

def check_progress():
    total_steps = 5
    completed_steps = 0
    
    if st.session_state.pathway:
        completed_steps += 1
    
    if len(st.session_state.species_done) == len(SPECIES_DATA[st.session_state.pathway or 'birds']):
        completed_steps += 1
        
    if st.session_state.comprehension_done:
        completed_steps += 1
        
    if st.session_state.vocab_done:
        completed_steps += 1
        
    if st.session_state.page == 'reflection' or st.session_state.page == 'completion':
        completed_steps += 1
        
    return completed_steps, total_steps

# Placeholder for species data - this would ideally come from a database
SPECIES_DATA = {
    'birds': [
        {
            'name': 'Rhinoceros Hornbill',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Rhinoceros_Hornbill_%28Buceros_rhinoceros%29_male_-_20090813.jpg/800px-Rhinoceros_Hornbill_%28Buceros_rhinoceros%29_male_-_20090813.jpg',
            'options': ['Rhinoceros Hornbill', 'Oriental Pied Hornbill', 'Great Hornbill', 'Wreathed Hornbill'],
            'fact': 'The Rhinoceros Hornbill is one of the largest hornbill species, known for its huge orange and red casque on top of its bill. It plays an important role in seed dispersal in the rainforests of Borneo.'
        },
        {
            'name': 'Blue-crowned Hanging Parrot',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Blue-crowned_hanging_parrot_%28Loriculus_galgulus%29_male.jpg/800px-Blue-crowned_hanging_parrot_%28Loriculus_galgulus%29_male.jpg',
            'options': ['Blue-crowned Hanging Parrot', 'Red-breasted Parakeet', 'Long-tailed Parakeet', 'Blue-naped Parrot'],
            'fact': 'The tiny Blue-crowned Hanging Parrot gets its name from its habit of sleeping upside-down, hanging from branches. It has bright green plumage with a blue spot on its crown.'
        },
        {
            'name': 'Bornean Bristlehead',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Bristlehead.jpg/800px-Bristlehead.jpg',
            'options': ['Bornean Bristlehead', 'Black-and-crimson Pitta', 'Malaysian Rail-babbler', 'Black-headed Bulbul'],
            'fact': 'The Bornean Bristlehead is an enigmatic and rare bird found only in Borneo. It has distinctive stiff bristle-like feathers on its head and is the only member of its family.'
        },
        {
            'name': 'Oriental Dwarf Kingfisher',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Oriental_Dwarf_Kingfisher.jpg/800px-Oriental_Dwarf_Kingfisher.jpg',
            'options': ['Oriental Dwarf Kingfisher', 'Common Kingfisher', 'Stork-billed Kingfisher', 'Collared Kingfisher'],
            'fact': 'The Oriental Dwarf Kingfisher, also known as the Three-toed Kingfisher, is one of the smallest kingfishers with incredibly vibrant plumage of orange, purple, blue, and white.'
        },
        {
            'name': 'Crested Fireback',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Lophura_ignita_-Kuala_Lumpur_Bird_Park-8a.jpg/800px-Lophura_ignita_-Kuala_Lumpur_Bird_Park-8a.jpg',
            'options': ['Crested Fireback', 'Great Argus', 'Bulwer\'s Pheasant', 'Bornean Peacock-Pheasant'],
            'fact': 'The Crested Fireback is a pheasant species with a beautiful blue-black plumage, red legs and facial skin, and, as the name suggests, a "fire-colored" back. Males have a tall crest on their heads.'
        }
    ],
    'monkeys': [
        {
            'name': 'Proboscis Monkey',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Proboscis_Monkey_in_Borneo.jpg/800px-Proboscis_Monkey_in_Borneo.jpg',
            'options': ['Proboscis Monkey', 'Silvered Leaf Monkey', 'Long-tailed Macaque', 'Maroon Leaf Monkey'],
            'fact': 'The Proboscis Monkey is endemic to Borneo and is known for its distinctive long nose. Males have huge noses that can grow up to 7 inches long, which they use to attract females and amplify their warning calls.'
        },
        {
            'name': 'Silvered Leaf Monkey',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Trachypithecus_cristatus_%28Silvery_Lutung%29.jpg/800px-Trachypithecus_cristatus_%28Silvery_Lutung%29.jpg',
            'options': ['Silvered Leaf Monkey', 'Maroon Leaf Monkey', 'Proboscis Monkey', 'Red Leaf Monkey'],
            'fact': 'The Silvered Leaf Monkey, also known as the Silvery Lutung, has striking silver-tipped fur and a distinctive crest of hair on top of its head. They live in groups of 9-40 individuals and primarily eat leaves, making them true folivores.'
        },
        {
            'name': 'Maroon Leaf Monkey',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/PB090103b_maroon_sureli_PA.jpg/800px-PB090103b_maroon_sureli_PA.jpg',
            'options': ['Maroon Leaf Monkey', 'Silvered Leaf Monkey', 'Red Leaf Monkey', 'Banded Leaf Monkey'],
            'fact': 'The Maroon Leaf Monkey, also known as the Red Leaf Monkey, has a distinctive dark maroon coat and a long tail. Babies are born with bright orange fur that gradually darkens as they age.'
        },
        {
            'name': 'Long-tailed Macaque',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Macaca_fascicularis-01.jpg/800px-Macaca_fascicularis-01.jpg',
            'options': ['Long-tailed Macaque', 'Pig-tailed Macaque', 'Crab-eating Macaque', 'Stump-tailed Macaque'],
            'fact': 'The Long-tailed Macaque is one of the most widespread primates in Southeast Asia. It is highly adaptable and can swim well, often diving into water to find crabs and other aquatic food.'
        },
        {
            'name': 'Bornean Gibbon',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Hylobates_muelleri_-_Tulsa_Zoo.jpg/800px-Hylobates_muelleri_-_Tulsa_Zoo.jpg',
            'options': ['Bornean Gibbon', 'Agile Gibbon', 'Siamang', 'Lar Gibbon'],
            'fact': 'The Bornean Gibbon has the impressive ability to swing through the forest canopy at speeds up to 35 mph using its extremely long arms. It is known for its distinctive morning songs that can be heard throughout the forest.'
        }
    ]
}

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
            
            Many species are **arboreal**, spending most of their lives in the trees, rarely coming down to the ground. Their **prehensile** tails and strong limbs allow them to move with amazing **agility** through the forest canopy, leaping between branches that might be several meters apart.
            
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
                    'question': 'What does "prehensile" refer to?',
                    'options': ['Ability to grab things', 'Ability to run fast', 'Ability to swim'],
                    'answer': 'Ability to grab things'
                },
                {
                    'question': 'What type of communities do Bornean monkeys live in?',
                    'options': ['Random groups', 'Hierarchical communities', 'Solitary territories'],
                    'answer': 'Hierarchical communities'
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
                    'question': 'Which digestive adaptation is found in leaf-eating monkeys?',
                    'options': ['Generalist dentition', 'Foregut fermentation', 'Proteolytic enzymes'],
                    'answer': 'Foregut fermentation'
                }
            ]
        }
    }
}

# Vocabulary activity data
VOCABULARY_DATA = {
    'birds': [
        {
            'sentence': 'The kingfisher has a ________ body that helps it dive into water.',
            'answer': 'streamlined',
            'explanation': 'Streamlined means having a shape that reduces resistance from air or water.'
        },
        {
            'sentence': 'Many birds use ________ feathers to attract mates.',
            'answer': 'iridescent',
            'explanation': 'Iridescent means showing luminous colors that seem to change when seen from different angles.'
        },
        {
            'sentence': 'The hornbill has a  ________ casque makes it easy to identify.',
            'answer': 'distinctive',
            'explanation': 'Distinctive means having a quality that makes something recognizably different from others.'
        },
        {
            'sentence': 'Birds help with ________ by carrying seeds to new areas.',
            'answer': 'seed dispersal',
            'explanation': 'Seed dispersal is the movement of seeds away from the parent plant.'
        },
        {
            'sentence': 'The bird has an ________ shape allows it to fly with minimal resistance.',
            'answer': 'aerodynamic',
            'explanation': 'Aerodynamic means having a shape that reduces the drag from air moving past.'
        },
        {
            'sentence': 'Some birds use ________ to hide from predators in the forest.',
            'answer': 'camouflage',
            'explanation': 'Camouflage is the use of color or pattern to blend into surroundings.'
        }
    ],
    'monkeys': [
        {
            'sentence': 'Monkeys are ________ creatures that rely on social groups for survival.',
            'answer': 'highly adaptive',
            'explanation': 'Highly adaptive means able to adjust well to different conditions.'
        },
        {
            'sentence': 'Many monkey species are ________, spending most of their lives in trees.',
            'answer': 'arboreal',
            'explanation': 'Arboreal means living in trees.'
        },
        {
            'sentence': 'Some monkeys have ________ tails that can grab onto branches.',
            'answer': 'prehensile',
            'explanation': 'Prehensile means adapted for seizing or grasping, especially by wrapping around.'
        },
        {
            'sentence': 'Monkeys move with amazing ________ through the forest canopy.',
            'answer': 'agility',
            'explanation': 'Agility is the ability to move quickly and easily.'
        },
        {
            'sentence': 'Monkeys live in ________ communities with clear social rankings.',
            'answer': 'hierarchical',
            'explanation': 'Hierarchical means arranged in order of rank or importance.'
        },
        {
            'sentence': 'Some monkeys are ________, eating both plants and small animals.',
            'answer': 'omnivorous',
            'explanation': 'Omnivorous means eating both plant and animal foods.'
        }
    ]
}

# Paragraph organization challenge data
PARAGRAPH_DATA = {
    'birds': {
        'easy': [
            {
                'sentences': [
                    "Hornbills are large birds with colorful beaks.",
                    "They make nests in hollow trees.",
                    "The female stays inside the nest to lay eggs.",
                    "The male brings food to the female and chicks.",
                    "After the chicks grow, they break out of the nest."
                ]
            },
            {
                'sentences': [
                    "Kingfishers are beautiful birds that live near water.",
                    "They have bright blue and orange feathers.",
                    "Kingfishers sit on branches above the water.",
                    "They dive quickly to catch fish.",
                    "Then they return to their perch to eat."
                ]
            },
            {
                'sentences': [
                    "The Bornean Bristlehead is a rare bird.",
                    "It lives only in the forests of Borneo.",
                    "It has black feathers with red and yellow parts.",
                    "It eats insects from tree bark.",
                    "Scientists still don't know much about this bird."
                ]
            }
        ],
        'medium': [
            {
                'sentences': [
                    "Hornbills are important birds in Borneo's ecosystem.",
                    "First, they eat fruits from many different trees.",
                    "Then, they fly to other areas of the forest.",
                    "Next, they drop seeds in their droppings.",
                    "Finally, these seeds grow into new trees.",
                    "This process helps maintain the diversity of the forest."
                ]
            },
            {
                'sentences': [
                    "Birdwatching in Borneo requires careful preparation.",
                    "Initially, you should research which birds you want to see.",
                    "Subsequently, you need to find the right locations.",
                    "Additionally, bringing good binoculars is essential.",
                    "Furthermore, a field guide will help with identification.",
                    "Ultimately, patience is the most important quality for birdwatchers."
                ]
            },
            {
                'sentences': [
                    "The Oriental Dwarf Kingfisher has a remarkable hunting technique.",
                    "At first, it perches motionless above the water.",
                    "When it spots a fish, it calculates the exact position.",
                    "Then, it dives at high speed into the water.",
                    "Surprisingly, it can adjust its dive path during the descent.",
                    "Most impressively, it rarely misses its target."
                ]
            }
        ],
        'hard': [
            {
                'sentences': [
                    "The Rhinoceros Hornbill faces several threats in Borneo.",
                    "Deforestation is reducing their habitat rapidly; however, conservation efforts are increasing.",
                    "Hunting was once a major problem; nevertheless, new protection laws have helped.",
                    "Climate change is also affecting their food sources; consequently, their breeding success has declined.",
                    "Tourism brings money for conservation; on the other hand, it can disturb nesting birds.",
                    "These magnificent birds are cultural symbols; therefore, their survival is important for both ecological and cultural reasons."
                ]
            },
            {
                'sentences': [
                    "Bird migration patterns in Borneo are complex and fascinating.",
                    "Some birds remain on the island year-round; in contrast, others arrive only for specific seasons.",
                    "Rainfall patterns influence food availability; as a result, birds time their breeding accordingly.",
                    "The island's mountains create diverse habitats; thus, different species can be found at various elevations.",
                    "Research on migration is still limited; nonetheless, satellite tracking is providing new insights.",
                    "Understanding these patterns is essential; in fact, it may be crucial for effective conservation plans."
                ]
            },
            {
                'sentences': [
                    "The evolution of Borneo's bird species is a tale of adaptation and isolation.",
                    "The island separated from mainland Asia millions of years ago; consequently, many unique species developed.",
                    "Forest birds evolved specialized beaks for different foods; for instance, hornbills developed large bills for fruits.",
                    "Mountain species adapted to cooler climates; meanwhile, lowland birds became heat-tolerant.",
                    "Some birds developed bright colors for attracting mates; conversely, others became camouflaged to hide from predators.",
                    "These evolutionary adaptations took thousands of generations; indeed, they represent nature's incredible ingenuity."
                ]
            }
        ]
    },
    'monkeys': {
        'easy': [
            {
                'sentences': [
                    "Proboscis monkeys have big noses.",
                    "They live in groups near rivers.",
                    "They eat leaves and fruits.",
                    "They are good swimmers.",
                    "They sleep in trees at night."
                ]
            },
            {
                'sentences': [
                    "Silvered Leaf Monkeys have silver-tipped fur.",
                    "They live in groups near forests.",
                    "They mainly eat leaves and some fruits.",
                    "Baby monkeys are born with orange fur.",
                    "Their fur turns silver as they grow."
                ]
            },
            {
                'sentences': [
                    "Macaques live in large groups.",
                    "They have long tails for balance.",
                    "They communicate with sounds and faces.",
                    "They find food on the ground and in trees.",
                    "They teach their young how to find food."
                ]
            }
        ],
        'medium': [
            {
                'sentences': [
                    "Proboscis monkeys have a unique social structure.",
                    "Initially, they form groups with one male and several females.",
                    "Additionally, there are bachelor groups of males without mates.",
                    "Sometimes, a stronger male will take over a family group.",
                    "Interestingly, groups come together at night for safety.",
                    "This complex arrangement helps their survival in the wild."
                ]
            },
            {
                'sentences': [
                    "Pig-tailed Macaques have distinctive short tails that look like a pig's tail.",
                    "First, they live in large groups of 15-40 individuals.",
                    "Then, they establish clear dominance hierarchies within the group.",
                    "Subsequently, young macaques learn foraging skills from their mothers.",
                    "Meanwhile, males compete for dominance and mating opportunities.",
                    "Ultimately, their social structure helps them survive in the forest."
                ]
            },
            {
                'sentences': [
                    "Bornean gibbons have fascinating communication methods.",
                    "Each morning, they sing loud songs that echo through the forest.",
                    "These songs mark their territory for other gibbons.",
                    "Furthermore, mated pairs sing duets together.",
                    "Remarkably, their calls can be heard from over a mile away.",
                    "Scientists study these songs to monitor gibbon populations."
                ]
            }
        ],
        'hard': [
            {
                'sentences': [
                    "The Proboscis Monkey's future in Borneo remains uncertain.",
                    "Mangrove forests are their primary habitat; unfortunately, these areas are being cleared for development.",
                    "Conservation areas have been established; however, they cover only a fraction of their range.",
                    "Ecotourism provides economic incentives for protection; nevertheless, it must be carefully managed to avoid stress to the animals.",
                    "Local communities are increasingly involved in conservation; as a result, some populations are now stable.",
                    "These unique monkeys are found nowhere else on Earth; therefore, their loss would be irreplaceable."
                ]
            },
            {
                'sentences': [
                    "Proboscis monkey communication involves multiple sophisticated signals.",
                    "Males use their large noses to amplify vocalizations; moreover, this feature attracts females.",
                    "Different groups have unique alarm calls; in fact, these vary based on specific threats.",
                    "They coordinate group movements with visual signals; for example, dominant males lead river crossings.",
                    "During territorial displays, they perform branch-shaking behaviors; remarkably, the intensity indicates their level of aggression.",
                    "Their vocal repertoire is extensive; indeed, researchers have identified over 20 distinct call types."
                ]
            },
            {
                'sentences': [
                    "The relationships between different monkey species in Borneo create a complex ecological web.",
                    "Larger species feed on fruits high in the canopy; meanwhile, smaller ones gather fallen pieces below.",
                    "Some species are active during the day; conversely, others come out at night to avoid competition.",
                    "Leaf-eating monkeys can digest toxic plants; consequently, they access food sources unavailable to others.",
                    "During fruit shortages, territories may overlap; however, direct confrontations are surprisingly rare.",
                    "This resource partitioning developed over millennia; in other words, it represents a finely tuned balance in the ecosystem."
                ]
            }
        ]
    }
}

# Word bank for reflective writing
WORD_BANK = {
    'birds': {
        'emotion': ['excited', 'amazed', 'peaceful', 'curious', 'surprised', 'delighted'],
        'descriptive': ['colorful', 'graceful', 'swift', 'tiny', 'majestic', 'noisy', 'quiet']
    },
    'monkeys': {
        'emotion': ['fascinated', 'entertained', 'surprised', 'amused', 'curious', 'impressed'],
        'descriptive': ['playful', 'intelligent', 'agile', 'social', 'mischievous', 'gentle', 'clever']
    }
}

# Welcome Page
def show_welcome():
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Mount_Kinabalu_from_Kampung_Kiau.jpg/1920px-Mount_Kinabalu_from_Kampung_Kiau.jpg", use_container_width=True)
    
    st.title("🌴 Borneo Wildlife Explorer 🌴")
    st.markdown("### Welcome to your wildlife learning adventure!")
    
    st.markdown("""
    During this activity, you'll learn about the fascinating wildlife of Borneo through:
    1. 🔍 **Wildlife Identification**
    2. 📚 **Reading & Comprehension**
    3. 📝 **Vocabulary Building**
    4. 🧩 **Paragraph Organization**
    5. ✏️ **Creative Reflection**
    """)
    
    st.markdown("### Choose your learning pathway:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🦜 Learn about Birds", use_container_width=True):
            choose_pathway('birds')
    with col2:
        if st.button("🐵 Learn about Monkeys", use_container_width=True):
            choose_pathway('monkeys')
    
    # Display progress if returning
    if st.session_state.pathway:
        completed, total = check_progress()
        st.markdown(f"""
        <div class="progress-tracker">
            <h3>Welcome back! Continue your {st.session_state.pathway.title()} adventure</h3>
            <p>You've completed {completed} out of {total} activities.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Resume button
        if st.button("Resume My Learning Journey", use_container_width=True):
            if len(st.session_state.species_done) < len(SPECIES_DATA[st.session_state.pathway]):
                st.session_state.page = 'identification'
            elif not st.session_state.comprehension_done:
                st.session_state.page = 'comprehension'
            elif not st.session_state.vocab_done:
                st.session_state.page = 'vocabulary'
            else:
                st.session_state.page = 'paragraph'

# Species Identification
def show_identification():
    # Get all species that haven't been shown yet
    available_species = [s for i, s in enumerate(SPECIES_DATA[st.session_state.pathway]) 
                        if i not in st.session_state.species_done]
    
    if not available_species:
        go_to_page('comprehension')
        return
    
    # Pick a random species
    species = random.choice(available_species)
    species_index = SPECIES_DATA[st.session_state.pathway].index(species)
    
    st.title(f"🔍 Identify the {st.session_state.pathway.rstrip('s')}!")
    st.image(species['image'], use_container_width=True)
    
    # Multiple choice options
    answer = st.radio("What species is this?", species['options'], key="species_selection")
    
    # Check answer button
    if st.button("Check my answer"):
        st.session_state.total_questions += 1
        
        if answer == species['name']:
            st.session_state.correct_answers += 1
            st.success("✅ Correct! Well done!")
        else:
            st.error(f"❌ Not quite. This is a {species['name']}.")
        
        # Display fact box
        st.markdown(f"""
        <div class="fact-box">
            <h3>📚 Fact about the {species['name']}</h3>
            <p>{species['fact']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add to completed species
        if species_index not in st.session_state.species_done:
            st.session_state.species_done.append(species_index)
        
        # Next button
        if st.button("Next"):
            next_species()
    
    # Display progress
    completed, total = check_progress()
    st.progress(completed/total)
    st.text(f"Progress: {completed}/{total} activities completed")

# Comprehension Check
def show_comprehension():
    st.title(f"📝 Reading About {st.session_state.pathway.title()}")
    
    # Initialize comprehension difficulty if not set
    if 'comprehension_difficulty' not in st.session_state:
        st.session_state.comprehension_difficulty = 'easy'
    
    # Difficulty selector
    difficulty = st.select_slider(
        "Select difficulty level:",
        options=['easy', 'medium', 'hard'],
        value=st.session_state.comprehension_difficulty
    )
    
    # Update difficulty if changed
    if difficulty != st.session_state.comprehension_difficulty:
        st.session_state.comprehension_difficulty = difficulty
        if 'submitted' in st.session_state:
            st.session_state.submitted = False
        st.rerun()
    
    data = COMPREHENSION_DATA[st.session_state.pathway][st.session_state.comprehension_difficulty]
    
    # Display the reading passage with highlighted vocabulary
    st.markdown("""
    <div class="wildlife-card">
        <h3>Reading Passage</h3>
        {}
    </div>
    """.format(data['text']), unsafe_allow_html=True)
    
    # Comprehension questions
    st.subheader("Comprehension Check")
    correct_answers = 0
    total_questions = len(data['questions'])
    
    for i, q in enumerate(data['questions']):
        answer = st.radio(q['question'], q['options'], key=f"comprehension_{i}")
        
        if 'submitted' in st.session_state and st.session_state.submitted:
            if answer == q['answer']:
                st.success("✅ Correct!")
                correct_answers += 1
            else:
                st.error(f"❌ The correct answer is: {q['answer']}")
    
    # Submit button
    if not ('submitted' in st.session_state and st.session_state.submitted):
        if st.button("Check my answers"):
            st.session_state.submitted = True
            st.rerun()
    else:
        # Display score with appropriate feedback
        score_percentage = (correct_answers / total_questions) * 100
        
        if score_percentage >= 80:
            st.success(f"**Great job! Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%)**")
            if difficulty != 'hard':
                st.info(f"Ready for a challenge? Try the {['medium', 'hard'][difficulty == 'medium']} difficulty!")
        elif score_percentage >= 60:
            st.info(f"**Good effort! Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%)**")
        else:
            st.warning(f"**Score: {correct_answers}/{total_questions} ({score_percentage:.0f}%). Keep practicing!**")
            if difficulty != 'easy':
                st.info(f"Try the {['easy', 'medium'][difficulty == 'hard']} difficulty to build your skills.")
        
        if st.button("Continue to Vocabulary Activity"):
            st.session_state.comprehension_done = True
            st.session_state.submitted = False
            go_to_page('vocabulary')
    
    # Display progress
    completed, total = check_progress()
    st.progress(completed/total)
    st.text(f"Progress: {completed}/{total} activities completed")

# Vocabulary Activity
def show_vocabulary():
    st.title(f"📝 Vocabulary Challenge: {st.session_state.pathway.title()}")
    
    data = VOCABULARY_DATA[st.session_state.pathway]
    
    st.markdown("""
    Fill in the blanks with the correct vocabulary word.
    Type the exact word or phrase that fits in each sentence.
    """)
    
    # Create text inputs for each sentence
    answers = []
    for i, item in enumerate(data):
        st.markdown(f"**{i+1}. {item['sentence']}**")
        answer = st.text_input("", key=f"vocab_{i}")
        answers.append(answer.strip().lower())
    
    # Check answers button
    if 'vocab_submitted' not in st.session_state:
        st.session_state.vocab_submitted = False
    
    if not st.session_state.vocab_submitted:
        if st.button("Check my answers"):
            st.session_state.vocab_submitted = True
            st.rerun()
    else:
        # Display results
        correct_count = 0
        for i, (answer, item) in enumerate(zip(answers, data)):
            correct = answer == item['answer'].lower()
            if correct:
                correct_count += 1
                st.markdown(f"**{i+1}.** ✅ Correct!")
            else:
                st.markdown(f"**{i+1}.** ❌ The correct answer is: **{item['answer']}**")
            
            st.markdown(f"<div class='fact-box'><p><strong>Explanation:</strong> {item['explanation']}</p></div>", unsafe_allow_html=True)
        
        st.markdown(f"**Your score: {correct_count}/{len(data)}**")
        
        if st.button("Continue to Paragraph Challenge"):
            st.session_state.vocab_done = True
            st.session_state.vocab_submitted = False
            go_to_page('paragraph')
    
    # Display progress
    completed, total = check_progress()
    st.progress(completed/total)
    st.text(f"Progress: {completed}/{total} activities completed")

# Paragraph Organization Challenge
def show_paragraph():
    st.title("🧩 Paragraph Organization Challenge")
    
    # Choose difficulty level
    if 'paragraph_level_changed' not in st.session_state:
        st.session_state.paragraph_level_changed = False
    
    level = st.selectbox("Select difficulty:", 
                        ["easy", "medium", "hard"], 
                        index=["easy", "medium", "hard"].index(st.session_state.paragraph_level))
    
    if level != st.session_state.paragraph_level:
        st.session_state.paragraph_level = level
        st.session_state.paragraph_level_changed = True
        st.session_state.paragraph_version = random.randint(0, len(PARAGRAPH_DATA[st.session_state.pathway][level])-1)
        st.rerun()
    
    # Get paragraph data
    paragraph_set = PARAGRAPH_DATA[st.session_state.pathway][level]
    if st.session_state.paragraph_version >= len(paragraph_set):
        st.session_state.paragraph_version = 0
    
    paragraph = paragraph_set[st.session_state.paragraph_version]
    
    st.markdown("""
    Arrange these sentences to form a logical paragraph. Drag and drop them in the correct order.
    """)
    
    # For this challenge, we'll use shuffled sentences and let users reorder them
    if 'shuffled_sentences' not in st.session_state or st.session_state.paragraph_level_changed:
        st.session_state.shuffled_sentences = paragraph['sentences'].copy()
        random.shuffle(st.session_state.shuffled_sentences)
        st.session_state.paragraph_level_changed = False
    
    # Let users reorder sentences
    ordered_sentences = st.session_state.shuffled_sentences.copy()
    for i, sentence in enumerate(ordered_sentences):
        st.text_input(f"Sentence {i+1}", sentence, key=f"sentence_{i}")
    
    # In a real app, would use drag and drop, but Streamlit doesn't have native support
    # So we'll use a simple up/down system
    col1, col2 = st.columns(2)
    
    with col1:
        sentence_to_move = st.number_input("Select sentence number to move:", 1, len(ordered_sentences), step=1) - 1
    
    with col2:
        direction = st.radio("Move direction:", ["Up", "Down"], horizontal=True)
    
    if st.button("Move Sentence"):
        if direction == "Up" and sentence_to_move > 0:
            ordered_sentences[sentence_to_move], ordered_sentences[sentence_to_move-1] = ordered_sentences[sentence_to_move-1], ordered_sentences[sentence_to_move]
        elif direction == "Down" and sentence_to_move < len(ordered_sentences) - 1:
            ordered_sentences[sentence_to_move], ordered_sentences[sentence_to_move+1] = ordered_sentences[sentence_to_move+1], ordered_sentences[sentence_to_move]
        
        st.session_state.shuffled_sentences = ordered_sentences
        st.rerun()
    
    # Check answer
    if st.button("Check my paragraph"):
        correct = ordered_sentences == paragraph['sentences']
        if correct:
            st.success("✅ Perfect! Your paragraph is in the correct order.")
            
            if st.button("Continue to Reflection"):
                go_to_page('reflection')
        else:
            st.error("❌ Not quite right. The sentences aren't in the correct order yet.")
            st.session_state.paragraph_attempts += 1
            
            # Give hint after multiple attempts
            if st.session_state.paragraph_attempts >= 2:
                st.info("Hint: Look for transition words that show sequence or logical connections.")
            
            # Option to see answer after multiple attempts
            if st.session_state.paragraph_attempts >= 3:
                if st.button("Show me the correct order"):
                    st.markdown("**Correct paragraph order:**")
                    for i, sentence in enumerate(paragraph['sentences']):
                        st.markdown(f"{i+1}. {sentence}")
                    
                    if st.button("Try another paragraph"):
                        st.session_state.paragraph_version = (st.session_state.paragraph_version + 1) % len(paragraph_set)
                        st.session_state.paragraph_attempts = 0
                        del st.session_state.shuffled_sentences
                        st.rerun()
    
    # Option to try a different paragraph
    if st.button("Try a different paragraph"):
        st.session_state.paragraph_version = (st.session_state.paragraph_version + 1) % len(paragraph_set)
        st.session_state.paragraph_attempts = 0
        del st.session_state.shuffled_sentences
        st.rerun()
    
    # Display progress
    completed, total = check_progress()
    st.progress(completed/total)
    st.text(f"Progress: {completed}/{total} activities completed")

# Reflective Writing
def show_reflection():
    st.title("✏️ Reflective Writing")
    
    st.markdown(f"""
    ### Remembering {st.session_state.pathway.title()} I've Seen
    
    Write a short reflection about your experiences with {st.session_state.pathway} in Borneo.
    You can use the word bank below for inspiration.
    """)
    
    # Word bank
    word_bank = WORD_BANK[st.session_state.pathway]
    
    st.markdown("""
    <div class="word-bank">
        <h4>Word Bank</h4>
        <p><strong>Emotion words:</strong> {}</p>
        <p><strong>Descriptive words:</strong> {}</p>
    </div>
    """.format(", ".join(word_bank['emotion']), ", ".join(word_bank['descriptive'])), unsafe_allow_html=True)
    
    # Sentence starters
    st.markdown("""
    <div class="word-bank">
        <h4>Sentence Starters</h4>
        <ul>
            <li>I saw a...</li>
            <li>I felt... when...</li>
            <li>The most interesting thing was...</li>
            <li>I learned that...</li>
            <li>I wonder why...</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Text area for writing
    reflection = st.text_area("Your reflection (150 words max):", height=200, key="reflection_text", 
                             value=st.session_state.reflection)
    
    # Word count
    word_count = len(reflection.split())
    st.text(f"Word count: {word_count}/150")
    
    # Save button
    if st.button("Save my reflection"):
        st.session_state.reflection = reflection
        st.success("Your reflection has been saved!")
    
    # Download button
    if reflection:
        download_text = f"""My Reflection on Borneo {st.session_state.pathway.title()}\n\n{reflection}"""
        
        download_button_str = download_button(download_text, f"my_{st.session_state.pathway}_reflection.txt", "Download my reflection")
        st.markdown(download_button_str, unsafe_allow_html=True)
    
    if st.button("Complete my learning journey"):
        go_to_page('completion')
    
    # Display progress
    completed, total = check_progress()
    st.progress(completed/total)
    st.text(f"Progress: {completed}/{total} activities completed")

# Completion page
def show_completion():
    st.balloons()
    
    st.title("🎉 Congratulations!")
    
    st.markdown(f"""
    ### You've completed your learning journey about Borneo's {st.session_state.pathway}!
    
    Here's what you accomplished:
    
    * Identified {len(st.session_state.species_done)} different species
    * Completed reading comprehension and vocabulary activities
    * Organized paragraphs to improve your understanding
    * Reflected on your own experiences with {st.session_state.pathway}
    
    Your final score: {st.session_state.correct_answers}/{st.session_state.total_questions} correct answers
    """)
    
    if st.button("Start a new learning journey"):
        # Reset state
        for key in st.session_state.keys():
            del st.session_state[key]
        st.session_state.page = 'welcome'
        st.rerun()

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
    button_id = re.sub('\d+', '', button_uuid)

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

# Main app
def main():
    # Display appropriate page based on state
    if st.session_state.page == 'welcome':
        show_welcome()
    elif st.session_state.page == 'identification':
        show_identification()
    elif st.session_state.page == 'comprehension':
        show_comprehension()
    elif st.session_state.page == 'vocabulary':
        show_vocabulary()
    elif st.session_state.page == 'paragraph':
        show_paragraph()
    elif st.session_state.page == 'reflection':
        show_reflection()
    elif st.session_state.page == 'completion':
        show_completion()

if __name__ == "__main__":
    main()
