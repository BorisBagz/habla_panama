import json
import random
import os
import sys

"""
HABLA PANAMA
by: boris a.
"""

#sys.setdefaultencoding('utf-8')

# GLOBAL VARIABLES
json_words = 'words.json'     #json file containing the questions

#read the json file and load it to the variable DATA
def read_json_file(json_file):
    with open(json_file) as questions_file:
        data = json.load(questions_file)
        return data

def main():
    data = read_json_file(json_words)
    for i in range(len(data)):
        definition = []
        word = data[i]["word"]
        type = data[i]["type"]
        print("{0} [{1}] :".format(word, type))
        nb_def = len(data[i]["definition"])
        for j in range(nb_def):
            def_tmp = data[i]["definition"][str(j)]
            print("{0}. {1}".format(j+1, def_tmp))

if __name__ == '__main__':
    main()
