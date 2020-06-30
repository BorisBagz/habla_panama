import json
import re

file = open("words_tmp.txt")

for f in file:
    entry = f.replace("\n", " ")

    #regex to parse word, type and definition
    regex_word = ".*:"
    regex_type = r"\[([A-Za-z0-9_.]+)\]"
    regex_definition = "- .*"

    #looking for matches
    word_match = re.search(regex_word, entry)
    type_match = re.search(regex_type, entry)
    definition_match = re.search(regex_definition, entry)

    if word_match:
        print(word_match.group())

    if type_match:
        #removing brackets from type
        tmp_type = type_match.group()[:-1]
        tmp_type = tmp_type[1:]
        print(tmp_type)

    if definition_match:
        #removing - and space from definition
        tmp_definition = definition_match.group()[2:]
        print(tmp_definition)

    print("--------------------------")
