"""Creating all my functions"""

import json
import argparse
import sys
from os.path import exists

parser = argparse.ArgumentParser()
parser.add_argument('-filename', default = "input.tex")
args = parser.parse_args()
filename = vars(args)['filename']

def check_if_valid_file():
    """
    Takes argument and run program if file exist and is valid
    """
    last_chars = filename[-3:]
    if exists(filename) is True and last_chars == "tex":
        with open(filename, "r", encoding="utf-8") as read_file:
            read_file.read()
    else:
        sys.exit("Not a valid File")
    return True

def rules_structure(arg1, arg2):
    """
    Basic structure for applying rule newline and space
    """
    with open(arg1, "r", encoding="utf-8") as read_file:
        text = read_file.read()
        json_file = open('rules.json', encoding="utf-8")
        data = json.load(json_file)
        for k in data[arg2]:
            find = k['index0']
            replace = k['index1']
        applyrule = text.replace(find, replace)
        with open("output.tex", "w", encoding="utf-8") as w_tofile:
            w_tofile.write("".join(applyrule))

def get_rule_newline_after_dot():
    """
    Replace dot with dot + newline
    Remove whitespace before dot
    """
    rules_structure(filename, "newline_after_Dot")

def get_rule_space_after_percent():
    """
    Add space after %
    """
    rules_structure("output.tex", "space_after_Percent")

def remove_empty_lines():
    """
    Removing all empty lines in textfile
    """
    with open('output.tex', encoding="utf-8") as filename_output:
        with open('output.tex', 'r+', encoding="utf-8") as writetofile:
            for line in filename_output:
                if line.strip():
                    writetofile.write(line)
                    writetofile.truncate()

def get_rule_intention_tabs():
    """
    Intention tabs for environment blocks
    """
    with open('rules.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        #get all values from the rule
        for k in data["intention_tabs"]:
            begin_marker = k['begin_marker']
            end_marker = k['end_marker']
            excludable_marker = k['excludable_marker']
            find = k['index0']
            replace = k['index1']

    buffer = []
    with open('output.tex', "r", encoding="utf-8") as read_file:
        inside_markers = False
        for text in read_file.readlines():
            if end_marker in text:
                inside_markers = False
            if inside_markers:
                buffer.append(text.replace(find, replace))
            else:
                buffer.append(text)
            if begin_marker in text and excludable_marker not in text:
                inside_markers = True

    with open("output.tex", "w", encoding="utf-8") as w_tofile:
        w_tofile.write(''.join(buffer))
