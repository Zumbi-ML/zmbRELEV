# -*- coding: UTF-8 -*-

def read(file):
    """
    Read the content of the file as a list
    Args:
        file: the name of the file with the path
    """
    with open(file, 'r') as f:
        return f.read().split("\n")

def write(file, text):
	"""
	Save the file into a specific directory
    Args:
        file: the name of the file with the path
        text: the text to be written in the file
	"""
	with open(file, 'w') as f:
		f.write(text)
