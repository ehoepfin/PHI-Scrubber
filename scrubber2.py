import scrubadub, scrubadub_spacy

input_file = "PHIScrubber.txt"

with open(input_file, 'r') as f:
    text = f.read()

scrubber = scrubadub.Scrubber()
scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector)
print(scrubadub.clean(text))