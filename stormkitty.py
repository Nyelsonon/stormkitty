#imports
import csv
import random
import os

#variables stored in a neat little dictionary
portable_variables = {"max_deck_count":12, "begin_count":0}

#firstly lets generate a random deck using faction as our first param
def generate_random_deck():
    global portable_variables
    main_deck = []
    max_deck_count = portable_variables["max_deck_count"]
    print(max_deck_count)
    begin_count = portable_variables["begin_count"]
    while begin_count != max_deck_count:
        with open(r'C:\Users\nyels\Desktop\development\python\machine learning\deckgen\cards.csv') as f:
            reader = csv.reader(f)
            chosen_row = random.choice(list(reader))
            faction = str(chosen_row[3])
            if faction == "shadowfen" or faction == "neutral":
                print(faction)
                main_deck.append(chosen_row[0])
                begin_count += 1
                print(main_deck)
            else:
                pass

    return main_deck
print(generate_random_deck())
