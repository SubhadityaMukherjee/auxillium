from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

training_data = load_data('rasaintent.md')
trainer = Trainer(config.load("sample_configs/config_spacy.yml"))
trainer.train(training_data)
model_directory = trainer.persist('model/')
interpreter = Interpreter.load(model_directory)
interpreter.parse(u"He tried to molest me")