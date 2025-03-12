# Data for all Borneo Wildlife Explorer modules

# Species data
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
            'fact': 'The Chestnut Munia is a small finch with rich chestnut-brown upperparts and a black face and belly. They live in flocks and feed mainly on grass seeds.'
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
            'fact': 'Macaques are highly adaptable monkeys found throughout Borneo. They live in large social groups with clear hierarchies and are known for their intelligence.'
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
            'fact': 'The Silvered Leaf Monkey has striking silver-tipped fur and a distinctive crest of hair on top of its head. They live in groups and primarily eat leaves, making them true folivores.'
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
                    'words': ['The', 'monkeys', 'were', 'eating', 'fruits', 'while', 'the', 'birds', 'were', 'singing', 'in', 'the', 'trees'],
                    'correct': 'The monkeys were eating fruits while the birds were singing in the trees'
                }
            ]
        }
    ]
}

# Comprehension data
COMPREHENSION_DATA = {
    'birds': {
        'easy': {
            'text': """
            Many birds in Borneo have <b>colorful</b> feathers that shine in the sunlight. These pretty colors help birds hide from danger or attract mates.
            
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
            Many birds in Borneo have <b>iridescent</b> feathers that shimmer in the sunlight. These colors aren't from pigments but come from the structure of the feathers that reflect light like tiny prisms. This helps birds with <b>camouflage</b> in the dense rainforest or attracts mates with brilliant displays.
            
            Kingfishers have a <b>streamlined</b> body, perfect for diving into the water at high speed. Their <b>aerodynamic</b> shape reduces water resistance, allowing them to catch fish with precision. Some species can dive from heights of 20 meters, adjusting their dive angle based on the position of their prey.
            
            Hornbills, known for their striking beaks, play an important role in <b>seed dispersal</b> by eating fruits and dropping seeds in different areas. Their <b>distinctive</b> casques (the horn-like structure above their bill) amplify their calls, which can be heard throughout the <b>canopy</b> of the rainforest.
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
                }
            ]
        },
        'hard': {
            'text': """
            The avian species of Borneo exhibit remarkable <b>structural coloration</b> in their plumage, creating <b>iridescent</b> effects as light interacts with nanoscale features of their feathers. Unlike pigment-based colors, these <b>photonic structures</b> manipulate light waves through interference, diffraction, and scattering, producing the vibrant hues that serve dual purposes of <b>crypsis</b> in dense understory vegetation or <b>intersexual selection</b> displays.
            
            Alcedinidae species (kingfishers) possess extraordinarily <b>hydrodynamic</b> morphology optimized for high-velocity aquatic entry. Their <b>fusiform</b> body profile minimizes drag coefficient during the hunting dive, while specialized <b>cranial kinetics</b> allow precise trajectory adjustments in response to light refraction at the air-water interface, compensating for apparent displacement of prey items.
            
            Bucerotidae (hornbills) function as crucial <b>keystone dispersers</b> in forest ecosystems through <b>endozoochory</b> of large-seeded fruits. Their <b>pneumatized</b> casques serve as <b>resonating chambers</b> that amplify vocalizations across long distances in the forest <b>stratification</b>, facilitating both territorial defense and maintenance of pair bonds during nesting periods.
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
            Monkeys in Borneo are <b>highly adaptive</b> creatures that rely on social groups for survival. Living in <b>hierarchical</b> communities, they develop complex social bonds that determine access to food, mates, and safe sleeping sites. Each group has a unique set of vocalizations to communicate danger or food location.
            
            Many species are <b>arboreal</b>, spending most of their lives in the trees, rarely coming down to the ground. Their strong limbs allow them to move with amazing <b>agility</b> through the forest canopy, leaping between branches that might be several meters apart.
            
            Borneo's monkeys have developed <b>specialized</b> diets that prevent competition for the same food sources. While some are <b>omnivorous</b>, eating both plants and small animals, others are strictly <b>herbivorous</b>, feeding only on leaves, fruits, and flowers from specific trees in their territory.
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
                }
            ]
        },
        'hard': {
            'text': """
            Primates of Borneo exhibit remarkable <b>behavioral plasticity</b> and <b>social cognition</b> within their <b>multi-level fission-fusion societies</b>. These <b>conspecific aggregations</b> establish <b>dominance hierarchies</b> governing resource allocation, mate selection, and territorial defense through complex <b>agonistic-affiliative interactions</b>.
            
            The predominantly <b>arboreal locomotion</b> of these species has resulted in specialized <b>brachiation adaptations</b> and <b>anatomical preadaptations</b> for efficient <b>three-dimensional navigation</b> within the forest <b>stratification</b>. Their remarkable <b>proprioceptive acuity</b> enables precise trajectory calculation during <b>suspensory progression</b> and <b>quadrumanous climbing</b>.
            
            <b>Resource partitioning</b> among sympatric primate species in Borneo demonstrates classic <b>niche differentiation</b> strategies. Some exhibit <b>dietary specialization</b> as <b>folivores</b> with complex <b>foregut fermentation</b> systems, while others are <b>frugivore-insectivores</b> with <b>generalist dentition</b>.
            """,
            'questions': [
                {
                    'question': 'What term describes the ability of primates to adapt their behavior to different situations?',
                    'options': ['Social cognition', 'Behavioral plasticity', 'Paralinguistic communication'],
                    'answer': 'Behavioral plasticity'
                },
                {
                    'question': 'What adaptation allows certain monkey species to swing from branch to branch?',
                    'options': ['Brachiation adaptations', 'Proprioceptive acuity', 'Quadrumanous climbing'],
                    'answer': 'Brachiation adaptations'
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

# Reading speed text
# Reading speed text with additional content
READING_SPEED_TEXT = [
    "Brunei's tropical rainforests are home to an astonishing variety of wildlife.",
    "The country's commitment to forest preservation has made it a sanctuary for many species.",
    "In the dense canopy, hornbills can be spotted flying between tall emergent trees.",
    "These magnificent birds are known for their unique nesting habits and loud calls.",
    "The proboscis monkey, with its distinctive long nose, is endemic to Borneo.",
    "These endangered primates live in groups near rivers and mangroves.",
    "They are excellent swimmers and can often be seen crossing rivers in search of food.",
    "Brunei's mangrove forests support a rich ecosystem of birds, reptiles, and mammals.",
    "The collared kingfisher hunts among the mangrove roots for small fish and crabs.",
    "Its bright blue plumage contrasts beautifully with the muddy environment.",
    "Clouded leopards are Brunei's largest wild cats, though they are rarely seen.",
    "These secretive predators hunt at night, climbing trees with extraordinary agility.",
    "The rainforest floor is home to many smaller creatures like the bearded pig.",
    "These wild pigs play an important role in dispersing seeds throughout the forest.",
    "Flying lizards can be spotted gliding between trees using their extended ribs.",
    "These remarkable adaptations allow them to travel up to 30 meters in a single glide.",
    "Brunei's rivers teem with life, including the fearsome saltwater crocodile.",
    "These ancient reptiles can grow to enormous sizes in the undisturbed waterways.",
    "Colorful butterflies add splashes of color to the forest.",
    "Protected species have distinctive patterns with large wingspans.",
    "Orangutans, though rare in Brunei, occasionally appear in the remote forests.",
    "These intelligent great apes build nests each night in different locations.",
    "Conservation efforts in Brunei focus on preserving these diverse habitats.",
    "Nearly 70% of the country remains covered in pristine primary forest.",
    "This commitment to conservation ensures that Brunei's wildlife will continue to thrive.",
    "Ecotourism provides opportunities to observe these animals in their natural settings.",
    "Guided tours along rivers and through forests offer glimpses of this spectacular biodiversity.",
    "Responsible tourism practices help protect these delicate ecosystems for future generations.",
    "Research programs monitor wildlife populations and habitat health in Brunei.",
    "Scientists use camera traps and field surveys to track elusive species.",
    "Climate change poses new challenges for Brunei's wildlife conservation efforts.",
    "Rising temperatures and changing rainfall patterns affect breeding cycles and food availability.",
    "Community involvement is essential for successful wildlife protection.",
    "Local knowledge and traditional practices often complement scientific approaches.",
    "Education programs in schools raise awareness about Brunei's natural heritage.",
    "Children learn about the importance of protecting wildlife and their habitats.",
    "The government has established several protected areas and wildlife sanctuaries.",
    "These protected zones restrict hunting and provide safe havens for many species.",
    "International cooperation helps address cross-border conservation challenges.",
    "Brunei works with Malaysia and Indonesia on initiatives to protect shared wildlife.",
    "Sustainable forestry practices aim to balance economic needs with conservation.",
    "Selective logging allows forests to regenerate while providing timber resources.",
    "Brunei's wetlands are recognized internationally for their ecological importance.",
    "They serve as critical stopover points for migratory birds along the East Asian-Australasian Flyway."
]
