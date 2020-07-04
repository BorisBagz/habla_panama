import json
import random
import os
import sys

"""
HABLA PANAMA
by: boris a.
"""
"""
Please, execute using PYTHON3
"""

# GLOBAL VARIABLES
my_json_words = 'words_test.json'     #json file containing the questions
valid_type_word = ['1', '2', '3', '4', '5']

#read the json file and load it to the variable DATA
def read_json_file(json_file):
    with open(json_file) as words_file:
        data = json.load(words_file)
        return data

# function to add to JSON
def write_json(data, filename=my_json_words):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

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

#only the list of words
def print_list_words():
    data = read_json_file(my_json_words)
    for i in range(len(data)):
        print_word(data[i])

#adding entries to the dictionary
def adding_entries(tmp_word, tmp_type, tmp_definition):
    #adding process
    with open(my_json_words) as json_file:
        data = json.load(json_file)
        # json object to be appended
        new_entry = {   "word": tmp_word,
                        "type": tmp_type,
                        "definition":
                        {
                            "0": tmp_definition
                        }
                    }
        # appending entry to data
        data.append(new_entry)
    #writing data to file
    write_json(data)

#menu asking for word, type and defitions
def menu_add_entry():
    tmp_word = input('Palabra: ')
    #do while for the type of word input, it has to be in the valid_type_word array
    while True:
        print("Tipo de palabra:\n 1. VERBO\n 2. SUSTANTIVO\n 3. EXPRESION\n 4. ACRONIMO\n 5. OTRO")
        tmp_type_nb = input()
        #check if answer is valid
        if tmp_type_nb in valid_type_word:
            #set type based on selected number
            if tmp_type_nb == "1":
                tmp_type = "v"
                break
            if tmp_type_nb == "2":
                tmp_type = "s"
                break
            if tmp_type_nb == "3":
                tmp_type = "expr."
                break
            if tmp_type_nb == "4":
                tmp_type = "acr."
                break
            if tmp_type_nb == "5":
                tmp_type = "otro"
                break
        print("Favor introducir un tipo de palabra que esté entro de las opciones. [1-5]")
    #do while for repeating the definition prompt if required
    while True:
        tmp_definition = input("Definicion: ")
        nb_definitions = input("Desea agregar otra deficion para la misma palabra? (Y/N)")
        if nb_definitions == "n" or nb_definitions == "N":
            break;
    adding_entries(tmp_word, tmp_type, tmp_definition)

def main():
    menu_add_entry()
    data = read_json_file(my_json_words)
    print_all_entries(data)
    #print_list_words()

if __name__ == '__main__':
    main()
