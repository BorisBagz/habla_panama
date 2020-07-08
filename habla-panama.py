import json
import random
import os
import sys
import string
from difflib import SequenceMatcher

"""
HABLA PANAMA
by: boris a.
"""
"""
Please, execute using PYTHON3
"""

#print styling
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# GLOBAL VARIABLES
my_json_words = 'words.json'     #json file containing the questions
valid_type_word = ['1', '2', '3', '4', '5'] #list with valid type for adding entries

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

#handle the type of word when adding an entry
def add_type_word():
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
    return tmp_type

#handle adding definitions
def add_definitions():
    #do while for repeating the definition prompt if required
    while True:
        tmp_definition = input("Definicion: ")
        nb_definitions = input("Desea agregar otra deficion para la misma palabra? (Y/N)")
        if nb_definitions == "n" or nb_definitions == "N":
            break
    return tmp_definition

#menu asking for word, type and defitions
def menu_add_entry():
    tmp_word = input('Palabra: ')
    tmp_type = add_type_word()
    tmp_definition = add_definitions()
    adding_entries(tmp_word, tmp_type, tmp_definition)

#print the wod tht starts w a number
def sort_words_w_number(data, length_data):
    valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(color.GREEN + color.BOLD + '0-9:' + color.END)
    for j in range(length_data):
        if data[j]["word"][:1] in valid_numbers:
            print("{0}".format(data[j]["word"]))
    print("-------------------------")

#go thru the alphabet and print the words starting with each letter
def order_alphabet(data):
    length_data = len(data)
    sort_words_w_number(data, length_data)
    #we'll use the string.ascii array to print the letter and look for words
    #starting w that letter
    for i in range(len(string.ascii_uppercase)):
        tmp_letra_mayus = string.ascii_uppercase[i]
        tmp_letra_minus = string.ascii_lowercase[i]
        #print("{0}:".format(tmp_letra_mayus))
        print(color.GREEN + color.BOLD + tmp_letra_mayus + ':' + color.END)
        for j in range(length_data):
            #if the word starts w that letter in upper or lower case
            if data[j]["word"][:1] == tmp_letra_mayus or data[j]["word"][:1] == tmp_letra_minus:
                print("{0}".format(data[j]["word"]))
        print("-------------------------")

#leverages SequenceMatcher to compute the ratio of difference
#btwn the input of the user and words in the dictionary
#if the ratio is over .75 add it to an array matches
def match_difference_words(user_word):
    matches = []
    data = read_json_file(my_json_words)
    for i in range(len(data)):
        entry_word = data[i]["word"].lower()
        ratio = SequenceMatcher(None, user_word, entry_word).ratio()
        if ratio > 0.75:
            matches.append(entry_word)
    return matches

#searching function
#based on the user input and computes a ratio of difference
#creates an array if theres matches, prints the array
def search_words():
    user_word = input("Buscar palabra: ").lower()
    matches = match_difference_words(user_word)
    if matches:
        for i in range(len(matches)):
            print("{0}. {1}".format(i + 1, matches[i]))
        word_to_print = input("Escoge el número de la palabra que deseas ver (0-9): ")
        if word_to_print in valid_numbers:
            


def main():
    search_words()

if __name__ == '__main__':
    main()
