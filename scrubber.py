# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:42:29 2022

@author: LHoepfinger, MBrown, LPipatanangkura
"""
import spacy
from nltk.corpus import names
from spacy.matcher import Matcher
from datetime import date
from spacy.tokens import Span
import random
import json

male_names = names.words('male.txt')
female_names = names.words('female.txt')

def choose_names(name):
    return random.choice(male_names) if name in male_names else random.choice(female_names)

# input and output files
input_file = "dictatedPHI.txt" #input("Which file do you want to scrub? ")
output_file = 'scrubbed_' + input_file

# Load spaCy module
nlp = spacy.load("en_core_web_sm")

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
    # Create the matched span and assign the match_id as a label
    span = Span(doc, start_char, end_char, label=match_id)

# 2. Return Span objects directly
matches = matcher(doc, as_spans=True)
for span in reversed(matches):
    if (span.label_ == 'PERSON'):
        scrubbed_text = scrubbed_text[:span.start_char] + choose_name(doc[span.start_char:span.end_char]) + scrubbed_text[span.end_char:]
    # replace text with the matched token
    scrubbed_text = scrubbed_text[:span.start_char] + span.label_ + scrubbed_text[span.end_char:]

with open(output_file, 'w') as f:
    f.write(f"This file scrubbed of PHI data on {date.today().month}/{date.today().day}/{date.today().year}\n")
    f.write(scrubbed_text)

print(scrubbed_text)