# -*- coding: utf-8 -*-

# Oneshot script to generate cards from a TSV file
# This script don't need to be pretty

import json
import sys
import os

#texts = """
#testt;for;10
#testt;for
#testt
#testt;;10
#"""

try:
    TYPE = sys.argv[1]
except:
    print("Usage: <TYPE>")
    sys.exit(1)

# from /tmp/cards.tsv file
with open("/tmp/cards.tsv", "r") as f:
    texts = f.read()

cards = {}
startid = 0

for line in texts.split('\n'):
    startid = startid + 1
    if line == "":
        continue
    # Extract from csv
    #_line = line.split(";")
    # Extract from tsv
    _line = line.split("\t")
    _text = _line[1]
    _for = None
    _timer = None

    if _text == "":
        continue

    if len(_line) > 2:
        _for =  _line[2]
    if len(_line) > 3:
        _timer = _line[3]

    # action
    if TYPE == "action":
        cardid = "a%s" % startid
        card = {
                "type": "action",
                "image": "/img/action.svg",
                "text": _text
            }
    # soft
    if TYPE == "soft":
        cardid = "s%s" % startid
        card = {
                "type": "soft",
                "image": "/img/soft.svg",
                "text": _text
            }
    # hot
    if TYPE == "hot":
        cardid = "h%s" % startid
        card = {
                "type": "hot",
                "image": "/img/hot.svg",
                "text": _text
            }
    # coquin
    if TYPE == "coquin":
        cardid = "c%s" % startid
        card = {
                "type": "coquin",
                "image": "/img/coquin.svg",
                "text": _text
            }
    #hard
    if TYPE == "hard":
        cardid = "hd%s" % startid
        card = {
                "type": "hard",
                "image": "/img/hard.svg",
                "text": _text
            }
    # question
    if TYPE == "question":
        cardid = "q%s" % startid
        card = {
                "type": "question",
                "image": "/img/question.svg",
                "text": _text
            }
    # soumis
    if TYPE == "soumis":
        cardid = "sm%s" % startid
        card = {
                "type": "soumis",
                "image": "/img/handcuffs.svg",
                "text": _text
            }
    # undress
    if TYPE == "undress":
        cardid = "u%s" % startid
        card = {
                "type": "undress",
                "image": "/img/undress.svg",
                "text": _text
            }
    # end
    if TYPE == "end":
        cardid = "e%s" % startid
        card = {
                "type": "end",
                "image": "/img/end.svg",
                "text": _text
            }

    if _for:
        card['for'] = _for
    if _timer:
        card['timer'] = _timer
    cards[cardid] = card

string = json.dumps(cards, sort_keys=True).encode('utf-8').decode('unicode-escape')
print(string)
#print(json.dumps(cards, encoding="utf-8", sort_keys=True).decode('unicode-escape'))
