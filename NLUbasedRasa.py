from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from MovieAPI import(
    Respond,
    RespondGenres,
    RespondPoster,
    RespondPopular,
)
SorryResponses = "I'm sorry :( I couldn't find anything like that"
responses = '{} is a great movie,actor and actress : {} !'

# Create a trainer that uses this config
trainer = Trainer(config.load("data/config.yml"))
# Load the training data
training_data = load_data('data/cnrasa.json')
# Create an interpreter by training the model
interpreter = trainer.train(training_data)

def extract(message):
    result = interpreter.parse(message)
    print(result)
    entities=result["entities"]
    ent_vals = [e["value"] for e in entities]
    intent=result["intent"]["name"]

    # Fill the dictionary with entities
    return intent,entities,ent_vals

def negated_ents(phrase, ent_vals):
    ents = [e for e in ent_vals if e in phrase]
    print(ents)
    ends = sorted([phrase.index(e) + len(e) for e in ents])
    start = 0
    chunks = []
    for end in ends:
        chunks.append(phrase[start:end])
        start = end
    result = {}
    for chunk in chunks:
        for ent in ents:
            if ent in chunk:
                if "not" in chunk or "n't" in chunk:
                    result[ent] = False
                else:
                    result[ent] = True
    return result
def getresponse(message, params, neg_params):
    intent,entities,ent_vals=extract(message)
    negated = negated_ents(message, ent_vals)
    for ent in entities:
        if ent["value"] in negated and not negated[ent["value"]]:
            neg_params[ent["entity"]] = str(ent["value"])
        else:
            params[ent["entity"]] = str(ent["value"])
    # Find the hotels
    id,name,actor,imageUrl = find_movies(params, neg_params)
    # Return the correct response
    if len(id)>0:
        return responses.format(name,actor), params, neg_params,id,imageUrl
    else:
        return SorryResponses, params, neg_params,id,imageUrl
def find_movies(params, neg_params):
    C = Respond(params["movie_name"])
    if "year" in params:
        for c in C:
            if c["y"]==int(params["year"]):
                return c["id"],c["l"],c["s"],c["i"]["imageUrl"]
    if "year" in neg_params:
        for c in C:
            print(type(c))
            if c["y"]!=int(neg_params["year"]):
                return c["id"],c["l"],c["s"],c["i"]["imageUrl"]
    if "year" not in params and "year" not in neg_params:
        return C[0]["id"],C[0]["l"],C[0]["s"],C[0]["i"]["imageUrl"]

# params={"movie_name":"thegodfather"}
# print(extract("I want to see TheGodfather in the 1990"))
# neg_params={"year":1990}
# find_movies(params, neg_params)






