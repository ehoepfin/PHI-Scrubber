# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:42:29 2022

@author: LHoepfinger, MBrown, LPipatanangkura
"""
import spacy

# input and output files
input_file = 'PHIScrubber.txt'
output_file = "Scrubbed_" + input_file

""" Load the Spacy model, use the testing corpus we created"""
nlp = spacy.load("en_core_web_sm")

""" opens the .txt file and saves it as a string"""
with open(input_file, 'r') as f:
    text_to_scrub = f.read()
    
doc = nlp(text_to_scrub)

### Perform NER ###
# replace the NER tagged as 'PERSON'
# with person
scrubbed_text = text_to_scrub
for ent in reversed(doc.ents):
    if ent.label_ == 'PERSON':
        scrubbed_text = scrubbed_text[:ent.start_char] +ent.label_ + scrubbed_text[ent.end_char:]

with open(output_file, 'w') as f:
    f.write(scrubbed_text)

print(scrubbed_text)