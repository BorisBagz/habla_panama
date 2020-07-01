import json
import random
import os
import sys

"""
HABLA PANAMA
by: boris a.
"""

# GLOBAL VARIABLES
my_json_words = 'words_test.json'     #json file containing the questions

#read the json file and load it to the variable DATA
def read_json_file(json_file):
    with open(json_file) as words_file:
        data = json.load(words_file)
        return data

# function to add to JSON
def write_json(data, filename=my_json_words):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

#adding entries to the dictionary
def adding_entries(words_file):
    tmp_word = "simi"
    tmp_type = "s"
    tmp_definition = "simi's definition"
    #adding process
    with open(words_file) as json_file:
        data = json.load(json_file)
        # json object to be appended
        new_entry = {   "word": tmp_word,
                        "type": tmp_type,
                        "definition":
                        {
                            "0": tmp_definition
                        }
                    }
        # appending data to file
        data.append(new_entry)
    write_json(data)

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
    adding_entries(my_json_words)
    data = read_json_file(my_json_words)
    print_all_entries(data)

if __name__ == '__main__':
    main()
