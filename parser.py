import json
import re

words_json_file = "words.json"

# function to add to JSON
def write_json(data, filename=words_json_file):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

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
        tmp_word = word_match.group()

    if type_match:
        #removing brackets from type
        tmp_type = type_match.group()[:-1]
        tmp_type = tmp_type[1:]

    if definition_match:
        #removing - and space from definition
        tmp_definition = definition_match.group()[2:]

    with open(words_json_file) as json_file:
        data = json.load(json_file)
        # python object to be appended
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
