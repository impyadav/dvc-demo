import nltk
import numpy as np
from gensim.models import FastText
from gensim.test.utils import get_tmpfile

from data_processing import get_dataframe_from_json


def get_textual_data_for_word2vec_and_fasttext(dataframe, col_name):
    textual_data = list()
    for index, row in dataframe.iterrows():
        text = row[col_name]
        tokens = nltk.word_tokenize(text)
        textual_data.append(tokens)
    return textual_data


def fasttext_fit(list_of_token_lists):
    return FastText(list_of_token_lists, min_count=2, vector_size=64, window=2)



if __name__ == '__main__':
    jsondir = '/home/pk_yadav/prateek/dvc-demo/data'
    df = get_dataframe_from_json(jsondir)


    dataset = get_textual_data_for_word2vec_and_fasttext(df[500:600], 'cleanedContent')
    try:
        model = fasttext_fit(dataset)
        model.save('../models/fastText.model')
    except Exception as e:
        print('Error in training')
        print(e)