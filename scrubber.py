# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:42:29 2022

@author: LHoepfinger, MBrown, LPipatanangkura
"""
from xml.sax.handler import feature_namespace_prefixes
import spacy
from nltk.corpus import names
from spacy.matcher import Matcher
from datetime import date
from spacy.tokens import Span
import random
import json

<<<<<<< HEAD
male_names = names.words('male.txt')
female_names = names.words('female.txt')

def choose_name(name):
    if name in male_names:
        return random.choice(male_names)  
    else:
        return random.choice(female_names)

=======
>>>>>>> main
# input and output files
input_file = "dictatedPHI.txt" #input("Which file do you want to scrub? ")
output_file = 'scrubbed_' + input_file

# Load spaCy module
nlp = spacy.load("en_core_web_sm")

# use NLTK to load names
male_names = names.words('male.txt')
male_names_shuffled = random.sample(male_names, len(male_names))
female_names = names.words('female.txt')
female_names_shuffled = random.sample(female_names, len(female_names))
both_names = random.sample(male_names_shuffled + female_names_shuffled, len(male_names) + len(female_names))

'''
This function chooses a random name for a given person. 
A hash function is used because of how it can return the same 
output. Since the male names and female names are shuffled at 
the beggining of the program, everytime the program is run
a different output is created.

A random name generator without hashing did not work because a 
different name was generated every call of the function rather 
than the same name generated for specific name.
'''
def choose_name(person, doc):
    if str(doc[person.start_char:person.end_char]) in male_names:
        return male_names_shuffled[hash(person.text) % len(male_names)]
    elif str(doc[person.start_char:person.end_char]) in female_names:
        return female_names_shuffled[hash(person.text) % len(female_names)]
    else:
        return both_names[hash(person.text) % len(both_names)]

# add custom paterns (patterns.json holds all the custom patterns)
with open("patterns.json") as j:
    patterns = json.load(j)

# create custom tokens for the patterns
matcher = Matcher(nlp.vocab)
for item in patterns:
    matcher.add(patterns[item]['id'], patterns[item]['pattern'])

# opens the .txt file and saves it as a string
with open(input_file, 'r') as f:
    text_to_scrub = f.read()

# create the object that spaCy can parse
doc = nlp(text_to_scrub)

### Perform NER ###
scrubbed_text = text_to_scrub
# 1. Return (match_id, start, end) tuples
matches = matcher(doc)
for match_id, start_char, end_char in matches:
    span = Span(doc, start_char, end_char, label=match_id)

# 2. Return Span objects directly
matches = matcher(doc, as_spans=True)
for span in reversed(matches):
    if (span.label_ == 'PERSON'):
<<<<<<< HEAD
        scrubbed_text = scrubbed_text[:span.start_char] + choose_name(text_to_scrub[span.start_char:span.end_char]) + scrubbed_text[span.end_char:]
    # replace text with the matched token
    else:
=======
        scrubbed_text = scrubbed_text[:span.start_char] + choose_name(span, doc) + scrubbed_text[span.end_char:]
    else:
        # replace text with the matched token
>>>>>>> main
        scrubbed_text = scrubbed_text[:span.start_char] + span.label_ + scrubbed_text[span.end_char:]

with open(output_file, 'w') as f:
    f.write(f"This file scrubbed of PHI data on {date.today().month}/{date.today().day}/{date.today().year}\n")
    f.write(scrubbed_text)

print(scrubbed_text)