# PHI-Scrubber #
## Table of Contents ##
1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Installation](#installation)
4. [How to Run](#how-to-run)
5. [Output](#output)
6. [Customization](#customization)

## Overview ##
This scrubber uses spaCy's rule-based-matcher model. The model allows the creation of new tokens and customization of existing tokens. New patterns can be in the form of regular expressions, setting token attributes, etc. In addition to spCy, NLTK is used for name recognition.


Skip to [Customization](#customization) to create modify or create tokens for this scrubber.

## Dependencies ##
1. Anaconda3 - In the development of this project, we discovered anaconda a useful tool in running spaCy and NLTK.
2. spaCy - The rule-rule based recognition is used to identify entities.
3. NLTK - The corpus for names is used for random name generation. 

## Installation ##
1. Install spaCy
```
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
```
Download the correct model spacy provides
```
$ python -m spacy download  en_core_web_sm
```
Consult spaCy's documentation for further details at [spacy.io](https://spacy.io)

2. Install NLTK

Follow the steps to install NLTK according to your operating system here: [https://www.nltk.org/install.html](https://www.nltk.org/install.html)

Then install the NLTK corpus:
```
$ python -m nltk.downloader all
```

## How to run: ##
```
$ python scrubber.py
```
or 
```
$ python3 scrubber.py
```
or just hit run in your IDE or text editor

## Output ##
Once you have it running, the program will prompt you with:
```
Which file do you want to scrub? <Insert File to Scrub Here>
```
The program will then create a scubbed version of the .txt, called:
```
scubbed_<original-file-name>.txt
```
At the top, you can find that the program will document the date the file was scrubbed for names. With this heading:
```
This file scrubbed of PHI data on <month>/<day>/<year>
```
This program supports scrubbing:
Entity | TOKEN 
:---------|:---------
People Name | PERSON
Emails | EMAIL
Phone #s/Fax | PHONE
Web Addresses(URLs and IP addresses) | WEB 
Social Securty Number | SSN
Medical record Numbers & Account Numbers | MRN 
Geographic Data (Locations) | LOC
Number Series (Vehicle Identifiers, health plan numbers, etc) | PHI
Dates | DATE

In the new text file created, each item that is scrubbed will be replaced with the token specified token.

## Customization ##
To customize the tokens or create new tokens, go to `patterns.json`. The id and patterns are the only two attrubutes required for every new token. The id is the label used to scrub that specific element. The pattern defines the token so it is recognized in the file to be scrubbed. This pattern must be inside of an array because there can be multiple patterns to describe one token. For further information about spaCy's rule-based matching, read the [documentation](https://spacy.io/usage/rule-based-matching).

