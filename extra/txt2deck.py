# -*- coding: utf-8 -*-

import json
import sys
import os

# Oneshot script to generate cards from a TSV file
# This script don't need to be pretty

texts = """
s67 1
s66 1
"""
# from /tmp/decks.tsv file
with open("/tmp/decks.tsv", "r") as f:
    texts = f.read()

decks = {}

for line in texts.split('\n'):
    if line == "":
        continue

    #cardid = text.split()[0]
    #number = int(text.split()[1])

    _line = line.split("\t")
    cardid = _line[0]
    number = _line[1]

    if cardid == "" or number == "":
        continue

    decks[cardid] = int(number)

string = json.dumps(decks, sort_keys=True).encode('utf-8').decode('unicode-escape')
print(string)
#print(json.dumps(decks, encoding="utf-8", sort_keys=True).decode('unicode-escape'))
