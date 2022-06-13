# PHI-Scrubber
### Dependencies ##
Anaconda3 - In the development of this project, we discovered anaconda a useful tool in running spaCy
### Installation ###
1. Install spaCy
```
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
```
2. Download the correct model spacy provides
```
$ python -m spacy download  en_core_web_md
```
Consult spaCy's documentation for further details
### How to run: ###
```
$ python scrubber.py
```
or 
```
$ python3 scrubber.py
```
or just hit run in your IDE or text editor

### Details ###
Once you have it running, the program will prompt you with:
```
Which file do you want to scrub? <Insert File to Scrub Here>
```
The program will then create a scubbed version of the .txt, called:
***
```
scubbed_<original-file-name>.txt
```
### In the text file ###
At the top, you can find that the program will document the date the file was scrubbed for names. With this heading:
```
This file scrubbed of PHI names data on <month>/<day>/<year>
```
This program supports scrubbing:
```
<entity> - <TOKEN>
People Name - PERSON
Dates (month and day) - DATE????
Phone #s/Fax - PHONE
Geographic Data - GPE
SSN - SSN
Emails - EMAIL
Medical record #s Acct #s - MRN 
Health Plan #s HP
Web Addresses(URLs and IP addresses) - WEB 
Vehicle identifiers (serial numbers, license plates) - VIN 
```

Within the text file, each name will be replaced with the token specified token.