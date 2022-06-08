# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:42:29 2022

@author: LHoepfinger, MBrown, LPipatanangkura
"""
import spacy

""" Load the Spacy model, use the testing corpus we created"""
nlp = spacy.load("en_core_web_sm")

""" opens the .txt file and saves it as a string"""
with open('PHIScrubber.txt') as f:
    contents = f.read()
    
doc = nlp(contents)

#Prints the POS tag in the terminal
for token in doc:
    print(token.text, token.tag_)
