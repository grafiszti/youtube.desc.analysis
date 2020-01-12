import re

import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer


class DataCleaner:
    def __init__(self):
        nltk.download('wordnet')

        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

        self.not_alphanumeric_and_whitespace_regex = "[^a-zA-Z\d\s]"

    def clean_description(self, description: str):
        temp = description

        # remove urls
        temp = " ".join(filter(lambda word: not word.startswith("http"), temp.split()))

        # remove not alphanumeric and whitespace
        temp = re.sub(self.not_alphanumeric_and_whitespace_regex, "", temp)

        # lemmatization
        temp = self.lemmatizer.lemmatize(temp)

        # stemming
        temp = self.stemmer.stem(temp)
        return temp
