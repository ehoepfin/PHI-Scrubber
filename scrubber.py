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

# input and output files
input_file = input("Which file do you want to scrub? ")
output_file = 'output\scrubbed_' + input_file

# Load spaCy module
nlp = spacy.load("en_core_web_sm")

# use NLTK to load names
male_names = names.words('male.txt')
male_names_shuffled = random.sample(male_names, len(male_names))
female_names = names.words('female.txt')
female_names_shuffled = random.sample(female_names, len(female_names))
both_names = random.sample(male_names_shuffled + female_names_shuffled, len(male_names) + len(female_names))

#load the drugs/medical terms from the Dictionaries/ 
f = open("Dictionaries/DrugsDictionary.txt")
r = open("Dictionaries/MedicalTermsDictionary.txt")
drug_dict = f.read()
med_dict = r.read()

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

#check the file for the specified drug names that may be tagged as people names, 
# and if so, tag them appropriately
def check_drugs(text):
    if text in drug_dict:
        return True
    if text in med_dict:
        return True
    else:
        return False

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
        #check if a medical entity is being tagged as a person
        if check_drugs(span.text):
            continue
        else:
            print(str(doc[span.start_char:span.end_char]))
            scrubbed_text = scrubbed_text[:span.start_char] + choose_name(span, doc) + scrubbed_text[span.end_char:]
    else:
        # replace text with the matched token
        scrubbed_text = scrubbed_text[:span.start_char] + span.label_ + scrubbed_text[span.end_char:]

with open(output_file, 'w') as f:
    f.write(f"This file scrubbed of PHI data on {date.today().month}/{date.today().day}/{date.today().year}\n")
    f.write(scrubbed_text)

print(scrubbed_text)