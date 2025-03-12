import streamlit as st
import random
import base64
import re
from PIL import Image
import os

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
        border-radius: L10px;
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
        color: #333333;;
    }
    .word-bank {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
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

# Species data using local images
SPECIES_DATA = {
    'birds': [
        {
            'name': 'Brahminy Kite',
            'image': 'images/Brahminy_kite.jpg',
            'options': ['Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch', 'Collared Kingfisher'],
            'fact': 'The Brahminy Kite is a medium-sized bird of prey found in Borneo. With its distinctive reddish-brown plumage and white head, it\'s often seen soaring over coastal areas and wetlands, searching for fish and small animals.'
        },
        {
            'name': 'Cattle Egret',
            'image': 'images/Cattle_egret.jpg',
            'options': ['Cattle Egret', 'Brahminy Kite', 'Oriental Pied Hornbill', 'Collared Kingfisher'],
            'fact': 'The Cattle Egret is a white heron that often follows cattle and other large animals, feeding on insects disturbed by their movement. During breeding season, they develop orange-buff plumage on their head, back, and chest.'
        },
        {
            'name': 'Chestnut Munia Finch',
            'image': 'images/Chestnut_munia_finch.jpg',
            'options': ['Chestnut Munia Finch', 'Cattle Egret', 'Brahminy Kite', 'Oriental Pied Hornbill'],
            'fact': 'The Chestnut Munia is a small finch with rich chestnut-brown upperparts and a black face and belly. They live in flocks and feed mainly on grass seeds. Their nests are round, woven structures usually built in tall grass or bushes.'
        },
        {
            'name': 'Collared Kingfisher',
            'image': 'images/collared_kingfisher.jpg',
            'options': ['Collared Kingfisher', 'Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch'],
            'fact': 'The Collared Kingfisher has striking blue and white plumage with a distinctive white collar. Unlike many kingfishers, it doesn\'t only eat fish but feeds on a variety of prey including lizards, crabs, and insects.'
        },
        {
            'name': 'Oriental Pied Hornbill',
            'image': 'images/Oriental_Pied_Hornbill.jpg',
            'options': ['Oriental Pied Hornbill', 'Brahminy Kite', 'Cattle Egret', 'Chestnut Munia Finch'],
            'fact': 'The Oriental Pied Hornbill has a distinctive black and white plumage with a large yellow-white bill topped by a casque. During nesting, the female seals herself inside a tree cavity, leaving only a small slit through which the male feeds her.'
        }
    ],
    'monkeys': [
        {
            'name': 'Proboscis Monkey',
            'image': 'images/Proboscis_Monkey_in_Borneo.jpg',
            'options': ['Proboscis Monkey', 'Macaque Monkey', 'Red Leaf Monkey', 'Silvered Leaf Monkey'],
            'fact': 'The Proboscis Monkey is endemic to Borneo and is known for its distinctive long nose. Males have huge noses that can grow up to 7 inches long, which they use to attract females and amplify their warning calls.'
        },
        {
            'name': 'Macaque Monkey',
            'image': 'images/macaque_monkey.jpg',
            'options': ['Macaque Monkey', 'Proboscis Monkey', 'Red Leaf Monkey', 'Silvered Leaf Monkey'],
            'fact': 'Macaques are highly adaptable monkeys found throughout Borneo. They live in large social groups with clear hierarchies and are known for their intelligence. They can use tools and solve complex problems to obtain food.'
        },
        {
            'name': 'Red Leaf Monkey',
            'image': 'images/Red_leaf_monkey.jpg',
            'options': ['Red Leaf Monkey', 'Proboscis Monkey', 'Macaque Monkey', 'Silvered Leaf Monkey'],
            'fact': 'The Red Leaf Monkey, also known as the Maroon Langur, has a distinctive dark maroon coat and a long tail. Babies are born with bright orange fur that gradually darkens as they age.'
        },
        {
            'name': 'Silvered Leaf Monkey',
            'image': 'images/Silvered_Leaf_Monkey.jpg',
            'options': ['Silvered Leaf Monkey', 'Red Leaf Monkey', 'Proboscis Monkey', 'Macaque Monkey'],
            'fact': 'The Silvered Leaf Monkey has striking silver-tipped fur and a distinctive crest of hair on top of its head. They live in groups of 9-40 individuals and primarily eat leaves, making them true folivores.'
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
            'sentence': 'The hornbill\'s ________ casque makes it easy to identify.',
            'answer': 'distinctive',
            'explanation': 'Distinctive means having a quality that makes something recognizably different from others.'
        },
        {
            'sentence': 'Birds help with ________ by carrying seeds to new areas.',
            'answer': 'seed dispersal',
            'explanation': 'Seed dispersal is the movement of seeds away from the parent plant.'
        },
        {
            'sentence': 'The bird\'s ________ shape allows it to fly with minimal resistance.',
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
            'sentence': 'Some monkeys have ________ limbs that can grab onto branches.',
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
                    "The Collared Kingfisher is a special bird.",
                    "It lives in the coastal areas of Borneo.",
                    "It has blue and white feathers.",
                    "It eats insects, fish, and small crabs.",
                    "People can often hear its loud call in the morning."
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
                    "The Kingfisher has a remarkable hunting technique.",
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
                    "The Hornbill faces several threats in Borneo.",
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
                    "Macaques are highly intelligent monkeys found in Borneo.",
                    "First, young macaques learn by watching adults in their group.",
                    "Then, they practice skills like finding food and building shelters.",
                    "Subsequently, they develop their place in the group hierarchy.",
                    "Meanwhile, they form strong bonds with other group members.",
                    "Eventually, they become fully integrated members of their community."
                ]
            },
            {
                'sentences': [
                    "Red Leaf Monkeys have fascinating communication methods.",
                    "Each morning, they call to establish their territory.",
                    "These calls help different groups avoid conflict.",
                    "Furthermore, they use specific sounds to warn about predators.",
                    "Remarkably, they have different calls for different threats.",
                    "Scientists study these calls to understand monkey intelligence."
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

# Home/Welcome page
def show_home():
    st.title("🌴 Borneo Wildlife Explorer 🌴")
    st.markdown("### Welcome to your wildlife learning adventure!")
    
    col1, col2 = st.columns([3, 2])
    
    try:
        with col1:
            st.image("images/Brahminy_kite.jpg", use_container_width=True)
            st.image("images/Proboscis_Monkey_in_Borneo.jpg", use_container_width=True)
    except Exception as e:
        st.warning(f"Could not load images. Please make sure the image files are in the correct location.")
    
    with col2:
        st.markdown("""
        During this activity, you'll learn about the fascinating wildlife of Borneo through:
        1. 🔍 **Wildlife Identification**
        2. 📚 **Reading & Comprehension**
        3. 📝 **Vocabulary Building**
        4. 🧩 **Paragraph Organization**
        5. ✏️ **Creative Reflection**
        """)
        
        st.markdown("Choose an activity on the left. Why not start with identification?")
        
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
    
    # Create a unique key for this question's options
    option_key = f"shuffled_options_{st.session_state.pathway}_{st.session_state.current_species_index}"
    
    # Only create shuffled options if they don't exist yet for this question
    if option_key not in st.session_state:
        shuffled_options = species['options'].copy()
        random.shuffle(shuffled_options)
        st.session_state[option_key] = shuffled_options
    
    # Multiple choice question with stored shuffled options
    answer = st.radio("What species is this?", st.session_state[option_key], key="species_radio")
    
    # Store the correct answer
    correct_answer = species['name']
    
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
# Reading comprehension activity
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
        
        # Display the reading passage
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

# Vocabulary activity
def show_vocabulary():
    st.title(f"📝 Vocabulary Challenge: {st.session_state.pathway.title()}")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_vocab",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_vocab))
    
    with col2:
        data = VOCABULARY_DATA[st.session_state.pathway]
        
        st.markdown("""
        Fill in the blanks with the correct vocabulary word.
        Type the exact word or phrase that fits in each sentence.
        """)
        
        # Create text inputs for each sentence
        for i, item in enumerate(data):
            st.markdown(f"**{i+1}. {item['sentence']}**")
            key = f"vocab_{i}"
            
            # Initialize if not exists
            if key not in st.session_state.vocabulary_answers:
                st.session_state.vocabulary_answers[key] = ""
            
            # Create the text input field
            if not st.session_state.vocab_submitted:
                st.session_state.vocabulary_answers[key] = st.text_input(
                    "", 
                    value=st.session_state.vocabulary_answers.get(key, ""),
                    key=key
                )
            else:
                st.text_input("", value=st.session_state.vocabulary_answers.get(key, ""), key=key, disabled=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            # Check answers button
            if not st.session_state.vocab_submitted:
                if st.button("Check Answers", key="check_vocab_btn"):
                    st.session_state.vocab_submitted = True
                    st.rerun()
        
        with col_b:
            # Reset button
            if st.button("Reset Exercise", key="reset_vocab"):
                st.session_state.vocab_submitted = False
                st.rerun()
        
        # Display results
        if st.session_state.vocab_submitted:
            correct_count = 0
            
            for i, item in enumerate(data):
                user_answer = st.session_state.vocabulary_answers.get(f"vocab_{i}", "").strip().lower()
                correct = user_answer == item['answer'].lower()
                
                if correct:
                    correct_count += 1
                    st.markdown(f"**{i+1}.** ✅ Correct!")
                else:
                    st.markdown(f"**{i+1}.** ❌ The correct answer is: **{item['answer']}**")
                
                st.markdown(f"<div class='fact-box'><p><strong>Explanation:</strong> {item['explanation']}</p></div>", unsafe_allow_html=True)
            
            st.markdown(f"**Your score: {correct_count}/{len(data)}**")

# Paragraph organization activity
def show_paragraph():
    st.title("🧩 Paragraph Organization Challenge")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_para",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_para))
        
        # Choose difficulty level
        st.session_state.paragraph_level = st.radio(
            "Select difficulty:", 
            ["easy", "medium", "hard"],
            index=["easy", "medium", "hard"].index(st.session_state.paragraph_level)
        )
        
        # Button to get a new paragraph
        if st.button("New Paragraph", key="new_para"):
            paragraph_set = PARAGRAPH_DATA[st.session_state.pathway][st.session_state.paragraph_level]
            st.session_state.paragraph_version = (st.session_state.paragraph_version + 1) % len(paragraph_set)
            st.session_state.shuffled_sentences = []
            st.rerun()
    
    with col2:
        # Get paragraph data
        paragraph_set = PARAGRAPH_DATA[st.session_state.pathway][st.session_state.paragraph_level]
        if st.session_state.paragraph_version >= len(paragraph_set):
            st.session_state.paragraph_version = 0
        
        paragraph = paragraph_set[st.session_state.paragraph_version]
        
        st.markdown("""
        Arrange these sentences to form a logical paragraph. Use the "Move Up" and "Move Down" buttons to reorder them.
        """)
        
        # Initialize shuffled sentences if needed
        if not st.session_state.shuffled_sentences:
            st.session_state.shuffled_sentences = paragraph['sentences'].copy()
            random.shuffle(st.session_state.shuffled_sentences)
        
        # Display each sentence with up/down buttons
        for i, sentence in enumerate(st.session_state.shuffled_sentences):
            col_a, col_b, col_c = st.columns([8, 1, 1])
            
            with col_a:
                st.text_input(f"Sentence {i+1}", sentence, key=f"sentence_{i}", disabled=True)
            
            with col_b:
                if i > 0:  # Can't move the first sentence up
                    if st.button("⬆️", key=f"up_{i}"):
                        st.session_state.shuffled_sentences[i], st.session_state.shuffled_sentences[i-1] = \
                            st.session_state.shuffled_sentences[i-1], st.session_state.shuffled_sentences[i]
                        st.rerun()
            
            with col_c:
                if i < len(st.session_state.shuffled_sentences) - 1:  # Can't move the last sentence down
                    if st.button("⬇️", key=f"down_{i}"):
                        st.session_state.shuffled_sentences[i], st.session_state.shuffled_sentences[i+1] = \
                            st.session_state.shuffled_sentences[i+1], st.session_state.shuffled_sentences[i]
                        st.rerun()
        
        # Check answer button
        if st.button("Check My Paragraph", key="check_para"):
            correct = st.session_state.shuffled_sentences == paragraph['sentences']
            
            if correct:
                st.success("✅ Perfect! Your paragraph is in the correct order.")
            else:
                st.error("❌ Not quite right. The sentences aren't in the correct order yet.")
                
                # Give hint
                st.info("Hint: Look for transition words that show sequence or logical connections.")
        
        # Show correct answer button
        if st.button("Show Correct Order", key="show_answer"):
            st.markdown("**Correct paragraph order:**")
            for i, sentence in enumerate(paragraph['sentences']):
                st.markdown(f"{i+1}. {sentence}")

# Reflective writing activity
def show_reflection():
    st.title("✏️ Reflective Writing")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.radio("Select your learning pathway:", 
                 ['birds', 'monkeys'], 
                 key="pathway_refl",
                 index=0 if st.session_state.pathway == 'birds' else 1,
                 on_change=lambda: setattr(st.session_state, 'pathway', st.session_state.pathway_refl))
    
    with col2:
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
        reflection = st.text_area(
            "Your reflection (150 words max):", 
            height=200,
            value=st.session_state.reflection_text,
            key="reflection_textarea"
        )
        
        # Save reflection to session state
        st.session_state.reflection_text = reflection
        
        # Word count
        word_count = len(reflection.split())
        st.text(f"Word count: {word_count}/150")
        
        # Save button
        if st.button("Save My Reflection", key="save_refl"):
            st.success("Your reflection has been saved!")
        
        # Download button
        if reflection:
            download_text = f"""My Reflection on Borneo {st.session_state.pathway.title()}\n\n{reflection}"""
            download_button_str = download_button(download_text, f"my_{st.session_state.pathway}_reflection.txt", "Download My Reflection")
            st.markdown(download_button_str, unsafe_allow_html=True)

# Main app
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    
    # Simple direct navigation buttons
    if st.sidebar.button("🏠 Home"):
        st.session_state.active_section = "home"
    
    if st.sidebar.button("🔍 Identification"):
        st.session_state.active_section = "identification"
    
    if st.sidebar.button("📚 Reading & Comprehension"):
        st.session_state.active_section = "comprehension"
    
    if st.sidebar.button("📝 Vocabulary Challenge"):
        st.session_state.active_section = "vocabulary"
    
    if st.sidebar.button("🧩 Paragraph Organization"):
        st.session_state.active_section = "paragraph"
    
    if st.sidebar.button("✏️ Reflective Writing"):
        st.session_state.active_section = "reflection"
    
    # Score display in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current pathway:** {st.session_state.pathway.title()}")
    st.sidebar.markdown(f"**Identification score:** {st.session_state.correct_answers}/{st.session_state.total_questions}")
    
    # Reset button
    st.sidebar.markdown("---")
    if st.sidebar.button("Reset All Progress"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
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
        st.rerun()
    
    # Display the selected section
    if st.session_state.active_section == "home":
        show_home()
    elif st.session_state.active_section == "identification":
        show_identification()
    elif st.session_state.active_section == "comprehension":
        show_comprehension()
    elif st.session_state.active_section == "vocabulary":
        show_vocabulary()
    elif st.session_state.active_section == "paragraph":
        show_paragraph()
    elif st.session_state.active_section == "reflection":
        show_reflection()

if __name__ == "__main__":
    main()
