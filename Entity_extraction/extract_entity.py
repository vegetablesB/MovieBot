## Using spaCy's entity recogniser
import spacy
nlp = spacy.load('en_core_web_md')
include_entities = ['DATE', 'NORP', 'PERSON', 'PRODUCT']

def extract_entities1(message):
    doc = nlp(message)
    for entity in doc.ents:
        print(entity, entity.label_, entity.label)
    # Define included entities

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)

    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents
