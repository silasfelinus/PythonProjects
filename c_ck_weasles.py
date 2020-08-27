"""Cockweasels Dirty Phrase generator
Written by Silas Knight
5/16/2020
version .0001"""

import random

print("Welcome to C*ck Weasels!\n")
print("The dirty phrase generator!")

first_set = ('cock', 'shit', 'fuck', 'turd', 'brain', 'butt', 'suck',
             'wang', 'carpet', 'mung', 'crap', 'fork', 'ass', 'penis',
             'vagina', 'clit', 'semen', 'sperm', 'jizz', 'cheese', 'curd',
             'douche', 'trout', 'fish', 'salmon', 'pussy', 'throat',
             'bone', 'turnip', 'goblin', 'crack', 'lizard', 'cum', 'lust',
             'muff', 'spunk', 'slunt', 'clam', 'slit', 'cunt', 'vomit',
             'lust', 'bone', 'taint', 'grundle', 'nun', 'zombie', 'jesus',
             'mother', 'brother', 'father', 'sister', 'cousin', 'donkey',
             'lip', 'prick', 'bitch', 'tongue', 'whore', 'slut', 'poo',
             'frak', 'fudge', 'tit', 'arse', 'fanny', 'face', 'frog', 'shite',
             'chunk', 'pube', 'cooch', 'zit', 'scab', 'pus', 'sheep', 'coke',
             'skin', 'peach', 'virgin', 'milk', 'schlong', 'wang', 'panty',
             'pig', 'throat', 'beer', 'bum', 'cherry', 'vag', 'puppy', 'pain',
             'slug', 'bruise', 'choad', 'thatch', 'snatch', 'bush', 'shaft',
             'meat', 'willy', 'horse', 'bong', 'midget', 'hog', 'duck',
             'diaper', 'goop', 'gack', 'god', 'weiner', 'pimple', 'booger',
             'whiskey', 'grease', 'condom', 'gnome', 'smegma', 'yogurt',
             'butter', 'corpse', 'sheath', 'foreskin', 'worm', 'knob',
             'flesh', 'custard', 'crab', 'dingle', 'skeeze', 'sweat', 'penguin',
             'kittie', 'kiddie', 'goo')

second_set = ('muncher', 'stroker', 'lover', 'shooter',
              'taster', 'fucker', 'hater', 'clinger',
              'licker', 'spitter', 'swallower', 'rubber', 'eater',
              'hoser', 'guzzler', 'chasm', 'gasm', 'rag',
              'goblin', 'gobbler', 'bag', 'squeezer', 'choker',
              'lapper', 'slave', 'monger', 'screamer', 'porker', 'jizzer',
              'chomper', 'boner', 'spanker', 'toucher', 'stain',
              'porker', 'fister', 'slagger', 'popper', 'slurper',
              'skinner', 'creamer', 'hole', 'ferret', 'wad',
              'sandwich', 'storm', 'donkey', 'bucket', 'dumster',
              'beetle', 'monkey', 'weasel', 'wiper', 'wipe',
              'stick', 'blocker', 'weed', 'receptacle', 'tease',
              'knocker', 'tickler', 'diver', 'bater', 'grabber',
              'slapper', 'bagger', 'plug', 'gutter', 'snorter'
              'sicle', 'lapper', 'absorber', 'commander',
              'sergeant', 'farmer', 'fellator', 'child',
              'warrior', 'cactus', 'casserole', 'pie', 'bagel',
              'caddy', 'butler', 'bishop', 'plumber', 'butcher',
              'wrestler', 'boxer', 'ninja', 'pirate', 'bomber',
              'crusader', 'angel', 'pixie', 'crammer', 'slammer', 'jammer',
              'maiden', 'squid', 'fellatrix', 'strumpet', 'dribbler',
              'nibbler', 'juggler', 'flute', 'fetus', 'victim',
              'o-gram', 'barrier', 'dragon', 'gizzard', 'furber',
              'burger', 'fungus', 'gorger', 'grabber', 'creeper',
              'daisy', 'panther', 'gummer', 'jerker', 'haggler',
              ' hotel', 'pleaser', 'knife', 'nugget', 'ladle',
              'discharge', 'lobster', 'lizard', 'mammoth', 'mullet',
              'oven', 'pot', 'hat', 'bot', 'robot', 'mollusk'
              'mongoose', 'mole', 'pillow', 'vinaigrette',
              'necklace', 'squatter', ' imp', 'berry', 'dingler',
              'slurpee', 'junkie', 'shampoo', 'incubater', 'sphincter',
              'erector', 'bubble', 'rocket', 'drinker', 'fiddler',
              'diddler', 'poker', "chugger", 'bistro', 'buffet', 'drone',
              'jockey', 'cleaner', 'reamer', 'shagger', ' cancer',
              'craver', 'picker', 'pooper', 'squirter', 'thruster')

third_set = ('munching', 'stroking', 'loving', 'shooting',
             'tasting', 'fucking', 'hating', 'clinging',
             'licking', 'spitting', 'swallowing', 'eating',
             'hosing', 'guzzling', 'gasming', 'raging',
             'gobbling', 'bagging', 'squeezing', 'choking',
             'lapping', 'slaving', 'mongering', 'screaming', 'porking', 'jizzing',
             'chomping', 'boning', 'spanking', 'touching', 'staining',
             'porking', 'fisting', 'slagging', 'popping', 'slurping',
             'skinning', 'creaming', 'ferreting', 'wadding', 'thrusting',
             'storming', 'monkeying', 'weaseling', 'wiping'
             'sticking', 'blocking', 'teasing', 'dribbling',
             'knocking', 'tickling', 'diving', 'bating', 'grabbing',
             'slapping', 'bagging', 'plugging', 'gutting', 'snorting',
             'lapping', 'absorbing', 'commanding', 'jamming',
             'farming', 'fellating', 'butchering', 'slamming',
             'wrestling', 'boxing', 'bombing', 'crusading', 'cramming',
             'nibbling', 'juggling', 'gorging', 'grabbing', 'creeping',
             'gumming', 'jerking', 'haggling', 'pleasing', 'ladling',
             'discharging', 'squatting', 'shampooing', 'incubating',
             'erecting', 'bubbling', 'drinking', 'fiddling',
             'diddling', 'poking', "chugging", 'cleaning', 'reaming',
             'shagging', 'craving', 'picking', 'pooping', 'squirting')

while True:
    first = random.choice(first_set)
    second = random.choice(third_set)

    third = random.choice(first_set)
    fourth = random.choice(second_set)

    print("\n")
    print(first + "-" + second + " " + third + fourth)
    print("\n")

    try_again = input("\n\nTry again? Press Enter else n to quit)\n")
    if try_again.lower() == 'n':
        break
    input("\nPress Enter to exit.")
