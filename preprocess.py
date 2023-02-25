import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

def pre_process (_sentences) :
    lancaster = LancasterStemmer()

    en_stops = set (stopwords.words ('english')) # Remove Stopwords
    processed_sentences = []

    for sentence in _sentences :
        sentence = re.sub (r'[^\w\s]','', sentence) # Remove special characters
        lower_sen = sentence.lower () # Convert the sentence to Lowercase
        token_sen = word_tokenize (lower_sen) # Tokenize the sentence

        new_sentence = []
        for word in token_sen:
            if word not in en_stops and word.isnumeric() == False : # Remove words that contain only digits
                word = lancaster.stem (word) # Perform Stemming
                new_sentence.append (word)

        if len (new_sentence) > 0 :
            processed_sentences.append (new_sentence)
    return processed_sentences
