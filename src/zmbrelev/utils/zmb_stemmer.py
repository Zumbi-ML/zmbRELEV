# -*- coding: UTF-8 -*-

from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from utils import filehelper as fh
from config import DISCR_TERMS_FILE

stemmer = RSLPStemmer()

def load_discriminative_terms_set():
    term_set = set()
    for term in fh.read(DISCR_TERMS_FILE):
        if (not term):
            continue
        term_set.add(stemmer.stem(term))
    return term_set

DISCRIMINATIVE_STEMS = load_discriminative_terms_set()

def stem_article(text):
    stemmed = ""
    word_tokens = word_tokenize(text.lower())
    for w in word_tokens:
        stemmed += f"{stemmer.stem(w)} "
    return stemmed
