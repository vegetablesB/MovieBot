# MovieBot
This is a movie search bot based on rasa.

## Table of Contents

- [Background](#background)
- [NLUPart](#NLUPart)
- [MovieAPI](#MovieAPI)
- [Contributing](#contributing)
- [License](#license)

## Background
This is an assignment after the course, a simple project on natural language processing. A telegram chat bot based on Rasa.  
The relevant content is as follows:
> 1) Multiple selective answers to the same question, and a default answer plan;
> 2) Able to answer questions through regular expressions, pattern matching, keyword extraction, syntax conversion, etc.;
> 3) Able to extract user intent through one or more of regular expressions, nearest neighbor classification or support vector machines;
> 4) Perform named entity recognition through pre-built named entity types, role relationships, dependency analysis, etc.;
> 5) Construction of local basic chat robot system based on Rasa NLU;
> 6) API use to get answer;
> 7) Single-round multiple incremental query technology based on incremental filters and technology for screening negative entities
> 8) Realize the technology of multiple rounds and multiple queries of the state machine, and provide explanations and answers based on contextual questions
> 9) Multiple rounds and multiple query technology for handling rejections, waiting state transitions and pending actions

## NLUPart
You could find the code at [NLUbasedRasa.py](https://github.com/vegetablesB/MovieBot/blob/master/NLUbasedRasa.py).  
In this part, I realized extracting user intent and entity. It's easy to extract entity which is common such as year like "2020". But It's hard to   
extract movie name such as The Godfather or Cathch Me If You Can. After thinking, I used regular expressions to improve the ability.   
You can find the code at [data/cnrasa.json](https://github.com/vegetablesB/MovieBot/blob/master/data/cnrasa.json).  
I also found sometimes you cannot extract basic intent or entity because the data used to train is not enough. Maybe other data way too much. So I balanced the training data.

## MovieAPI
Thanks for [rapidapi](https://rapidapi.com/).  
And I used [IMDbapi](https://rapidapi.com/apidojo/api/imdb8?endpoint=apiendpoint_dad99933-4241-43f0-b4f2-529d652dcc96) to realize movie information search including movie name, genre, images and posters.  
You could find the code in [MovieAPI.py](https://github.com/vegetablesB/MovieBot/blob/master/MovieAPI.py).

## Related Efforts
Thanks for Rasa spacy rapidapi and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

## Contributing
[@vegetablesB](https://github.com/vegetablesB)

## License
[MIT © Richard McRichface.](../LICENSE)
