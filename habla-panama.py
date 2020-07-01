import json
import random
import os
import sys

"""
HABLA PANAMA
by: boris a.
"""

# GLOBAL VARIABLES
json_words = 'words_test.json'     #json file containing the questions

#read the json file and load it to the variable DATA
def read_json_file(json_file):
    with open(json_file) as questions_file:
        data = json.load(questions_file)
        return data

#print only the word
def print_word(data):
    word = data["word"]
    print("{0}".format(word))

#print the word and its type
def print_word_type(data):
    word = data["word"]
    type = data["type"]
    print("{0} [{1}] :".format(word, type))

#print a single entry: word, type and definition
def print_single_entry(data):
    definition = []
    print_word_type(data)
    nb_def = len(data["definition"])
    for j in range(nb_def):
        def_tmp = data["definition"][str(j)]
        print("{0}. {1}".format(j+1, def_tmp))

#printing all the entries of the dictionary
def print_all_entries(data):
    for i in range(len(data)):
        print_single_entry(data[i])
        print("--------")

def main():
    data = read_json_file(json_words)
    print_all_entries(data)

if __name__ == '__main__':
    main()
