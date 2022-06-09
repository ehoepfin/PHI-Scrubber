# PHI-Scrubber
### How to run: ###
***
```
$ python3 scrubber.py
```
or 
***
```
$ python3 scrubber.py
```
or just hit run in your IDE or text editor

### Details ###
Once you have it running, the program will prompt you with:
***
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
***
```
This file scrubbed of PHI names data on <month>/<day>/<year>
```
Within the text file, each name will be replaced with the token "PERSON"