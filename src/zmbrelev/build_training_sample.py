# -*- coding: UTF-8 -*-

from config import *
from glob import glob
from newspaper import Article
import os
import re
from utils import filehelper as fh
from utils.hasher import hash_url

def download_n_parse_3k(url):
    """
    Gets the article's metadata
    Args:
        url: The article's URL
    """
    article3k = Article(url)
    try:
        article3k.download()
        article3k.parse()
    except Exception:
        print(f"Download or Parse:\t{url}")
        return
    return article3k.text

def clean_url(url):
    """
    Removes the attributes of the URL
    """
    MAX_URL = 2048
    cleaned_url_lst = re.split(r'[?#]', url)
    if (len(cleaned_url_lst) == 0):
        exc_msg = f"Problem removing the attributes of URL:\t{url}"
        print(exc_msg)

    cleaned_url = cleaned_url_lst[0]
    if len(cleaned_url) > MAX_URL:
        exc_msg = f"URL too long:\t{cleaned_url}"
        print(exc_msg)
    return cleaned_url

def does_file_exist(filename):
    """
    Checks if a file exists in the downloaded dir
    """
    full_filename = DOWNLOAD_DIR + filename
    return os.path.isfile(full_filename))

def download(file_prefix, urls):
    """
    Builds the sample
    """

    cleaned_urls = [clean_url(url) for url in urls]
    for url in cleaned_urls:
        if (not url):
            continue

        hashed_url = hash_url(url)
        download_filename = file_prefix + "_" + str(hashed_url) + ".txt"
        if (does_file_exist(download_filename)):
            print("URL already downloaded")
            continue

        text = download_n_parse_3k(url)
        if (not text):
            content = f"{url}\nFAILED"
            fh.write(DOWNLOAD_DIR + download_filename, content)
            continue
        fh.write(DOWNLOAD_DIR + download_filename, f"{url}\n{text}")

    return glob(DOWNLOAD_DIR + file_prefix + "*")

def load_articles(target, filenames):
    articles = []
    for filename in filenames:
        parts = fh.read(filename)
        if (parts[1] == "FAILED"):
            continue
        content = ""
        for p in parts[1:]:
            if (not p):
                continue
            content += f"{p} "
        articles.append([target, content])
    return articles

def make_training_sample(relev_articles, irrel_articles):
    """
    Builds the training sample
    Args:
        relev_articles: a list of relevant articles
        irrel_articles: a list of irrelevant articles
    """
    all_articles = relev_articles + irrel_articles
    training_sample = ""
    for article in all_articles:
        target, content = article
        training_sample += f"{target}\t{content}\n"
    return training_sample

def main():
    """
    Main
    """
    print("Starting RELEV Files")
    print("="*80)
    relev_urls = fh.read(RELEVANT_URLs_FILE)
    relev_dl_files = download("RELEV", relev_urls)
    relev_articles = load_articles(1, relev_dl_files)

    print("Starting IRREL Files")
    print("="*80)
    irrel_relev_urls = fh.read(NOT_RELEVANT_URLs_FILE)
    irrel_relev_dl_files = download("IRREL", irrel_relev_urls)
    irrel_articles = load_articles(0, irrel_relev_dl_files)

    training_sample = make_training_sample(relev_articles, irrel_articles)
    fh.write(TRAINING_SAMPLE_FILE, training_sample)

# Main
# ==============================================================================
if (__name__ == '__main__'):
    main()
