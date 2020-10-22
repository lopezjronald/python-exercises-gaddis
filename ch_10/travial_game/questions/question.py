class Question:

    def __init__(self):
        question_dictionary = {
            """What is an English translation of this Latin expression?
De mortuis nil nisi bonum""": {
                "About the dead, nothing unless a good thing": [
                    'About the dead, nothing unless a good thing',
                    'Scorn for the world',
                    'It is sweet and honorable to die for the fatherlan',
                    'No penalty without a law'
                ]
            },
            """What kind of animal is missing from this common phrase:
A ____ in the hand is worth two in the bush""": {
                "Bird": [
                    'Bird',
                    'Turkey',
                    'Bee',
                    'Swallow'
                ]
            },
            """Which of these models was produced by this car manufacturer?
Nissan""": {
                "300ZX": [
                    'Acura TL',
                    '300ZX',
                    '308 GTS',
                    'MX-5'
                ]
            },
            """Who is the owner of this fictional dog?
Fang""": {
                "Hagrid (Harry Potter series)": [
                    'Bill Sikes (Oliver Twist)',
                    'Martin Crane (Frasier)',
                    'Hagrid (Harry Potter series)',
                    'Mickey Mouse'
                ]
            },
            """What kind of food is missing from this common phrase?
To hit the ___ (drink alcohol in excess)""": {
                "Sauce": [
                    'Sauce',
                    'Stew',
                    'Salsa',
                    'Salad'
                ]
            },
            """What is an English translation of this Latin expression?
Post scriptum""": {
                "After what has been written": [
                    'After death',
                    'To the stars',
                    'From the former/based upon theory',
                    'After what has been written'
                ]
            },
            """What does this Latin prefix mean?
Ir (e.g. irredeemable, irrational)""": {
                "Not": [
                    'Or',
                    'Not',
                    'And',
                    'More'
                ]
            },
            """Which of these is NOT a room in the standard edition of the board game Cluedo (or Clue)?""": {
                "Waiting Room": [
                    'Dining Room',
                    'Billiard Room',
                    'Ballroom',
                    'Waiting Room'
                ]
            },
            """Which car manufacturer produced this model?
Accord""": {
                "Honda": [
                    'Mitsubishi',
                    'Honda',
                    'Mazda',
                    'Nissan'
                ]
            },
            """What does this Latin prefix mean?
Cand (e.g. candid, candle)""": {
                "Glowing": [
                    'Open',
                    'Soft',
                    'Light',
                    'Glowing'
                ]
            },
            """What does this Latin prefix mean?
Omni (e.g. omnipotent, omniscient)""": {
                "All": [
                    'Lose',
                    'All',
                    'Power',
                    'Strange'
                ]
            },
            """Which famous two persons with the same name are described here?
Leading American ornithologist (1900-1989) AND fictional character created in 1953 by Ian Fleming""": {
                "James Bond": [
                    'Endeavour Morse',
                    'James Bond',
                    'Caractacus Pott',
                    'Hercule Poirot'
                ]
            },
            """This car brand is (or was) originally from which country?
Tesla""": {
                "United States": [
                    'Hungary',
                    'Denmark',
                    'United Kingdom',
                    'United States'
                ]
            },
            """What body part is missing from this common phrase?
To give someone a piece of one's ___ (express opinion strongly)""": {
                "Mind": [
                    'Mind',
                    'Teeth',
                    'Tongue',
                    'Mouth'
                ]
            },
            """What does this Greek prefix mean?
Myo (e.g. myoglobin, myology)""": {
                "Mouse/muscle": [
                    'Medical care',
                    'Dry',
                    'Mouse/muscle',
                    'Red'
                ]
            },
            """What are the names of the members of this famous trio?
The Three Hyenas (Lion King)""": {
                "Shenzi, Banzai, and Ed": [
                    'Moe, Larry, Curly',
                    'Victor, Hugo, and Laverne',
                    'Shenzi, Banzai, and Ed',
                    'Yakko, Wakko, and Dot'
                ]
            },
            """This (historic) occupation can usually be described as what?
Hosier""": {
                "Maker/seller of stockings": [
                    'Writer of letters to court and legal documents',
                    'Responsible for the handling of money on a ship',
                    'Female servant who cares for children in household',
                    'Maker/seller of stockings'
                ]
            },
            """Which car manufacturer produced this model?
Lancer""": {
                "Mitsubishi": [
                    'Buick',
                    'Toyota',
                    'Mitsubishi',
                    'Pontiac'
                ]
            },
            """On bir, on iki, on üç, on dört, on bes are the numbers 11 to 15 in which language?""": {
                "Turkish": [
                    'Turkish',
                    'Arabic',
                    'Finnish',
                    'Polish'
                ]
            },
            """What are the names of the members of this famous trio?
The Kingston Trio""": {
                "Dave Guard, Bob Shane and Nick Reynolds": [
                    'Matt Bellamy, Chris Wolstenholme, Dominic Howard',
                    'Dave Guard, Bob Shane and Nick Reynolds',
                    'Billie Joe Armstrong, Mike Dirnt and Tre Cool',
                    'Gerry Beckley, Dewey Bunnell, and Dan Peek'
                ]
            },
        }

        self.__question_dictionary = question_dictionary

    def get_question_dictionary(self):
        return self.__question_dictionary
