LaTex linter

Description
-------------
The app is a easy command line interface to linter a tex file,
The app takes an input file, applies rules to it,
then creates an output file with the applied rules.
I have a json file for all my rules
linter.py for calling all my functions
intput.tex is my default text file
getruels.py is where i create all functions

Run program
-------------
You need to have the amazing-linter, rules.json and a tex file inside of 1 folder
Then you need to start the program by parsing a filename,
for example ./amazing-linter -filename input.tex
Then a menu pops up and if you press 1 a output.tex file will be created with all the rules applied.

Code structure
-------------
I used pylint to debug my code

Github
-------------
https://github.com/simonking99/amazing-latex-linter

Imported modules
-------------
from os.path import exists
import sys
import json
import argparse
import re
