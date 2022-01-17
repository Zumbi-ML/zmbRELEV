# -*- coding: UTF-8 -*-

from config import *
import json
import numpy as np
import pandas as pd
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from utils import filehelper as fh
from utils.zmb_stemmer import DISCRIMINATIVE_STEMS, stem_article

vectorizer = CountVectorizer()
vectorizer.fit_transform(DISCRIMINATIVE_STEMS)

def main():

    df = pd.read_csv(TRAINING_SAMPLE_FILE, sep='\t')
    df.columns = ['target', 'article']

    SEP = "=" * 80
    print(SEP)

    msg = \
    """Count of news articles about discrimination.\n\nCAPTION\n1: News articles about racial discrimination\n0: News articles about other topics
    """
    print(msg)
    print("Counts")
    print(SEP)
    counts = df.target.value_counts()
    print(counts)

    print(SEP)
    print("\nPRIOR CLASS PROBABILITIES")

    prior_proba_racial = counts[1] / (counts[1] + counts[0])
    prior_proba_not_racial = 1 - prior_proba_racial

    print(f"prior_proba_racial\t{prior_proba_racial}")
    print(f"prior_proba_not_racial\t{prior_proba_not_racial}")

    #multinomial_nb_clf = MultinomialNB(class_prior=[prior_proba_racial, prior_proba_not_racial])
    nb_clf = BernoulliNB()

    OUTPUT_FILE = BERNOULLI_NB_CLF_FILE

    X = df.article.apply(stem_article)
    y = df.target.values

    print(SEP)
    print("Vectorizer vocabulary")
    print(json.dumps(vectorizer.vocabulary_, indent=4, sort_keys=True))

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    X_train_vec = vectorizer.transform(X_train)
    nb_clf.fit(X_train_vec, y_train)

    X_test_vec = vectorizer.transform(X_test)
    y_test_pred = nb_clf.predict(X_test_vec)

    print(SEP)
    print("Multinomial classification report")
    print(classification_report(y_test, y_test_pred))

    with open(OUTPUT_FILE, 'wb') as f:
        pickle.dump((vectorizer, nb_clf), f)

main()
