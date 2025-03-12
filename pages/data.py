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
                    'answer': '
