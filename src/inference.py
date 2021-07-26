import nltk
import numpy as np
from gensim.models import FastText

def load_model(fname):
    return FastText.load(fname)


def mean_of_embeddings(list_of_embeddings, embedding_size=128):
    avg = np.zeros((embedding_size, ))
    for embd in list_of_embeddings:
        avg += embd
    return avg / len(list_of_embeddings)


def get_fasttext_embedding(sentence, model):
    tokens = nltk.word_tokenize(sentence)
    embeddings = [model[word] for word in tokens]
    return mean_of_embeddings(embeddings)


if __name__ == '__name__':
    pass
    # sentence = 'DVC is damn'

    # get_fasttext_embedding(sentence, "model_you_want_to_load")