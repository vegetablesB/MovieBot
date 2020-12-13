from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import telegram


# Create a trainer that uses this config
trainer = Trainer(config.load("data/config.yml"))

# Load the training data
training_data = load_data('data/cnrasa.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)


message="I want to see DarkKnight"
# print(interpreter.parse("I want the chinese movies called Tenet11 in 1999"))
entities = interpreter.parse(message)["entities"]
print(interpreter.parse(message))
print(entities)
# Initialize an empty params dictionary
params = {}
# Fill the dictionary with entities
for ent in entities:
    params[ent["entity"]] = str(ent["value"])
print(entities)
print(params)

