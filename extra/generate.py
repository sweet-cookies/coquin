#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import re

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '17A_U8v6_rBv9a2ZGaV3P913XCINzKRm5XE2wx40sRqU'
#SPREADSHEET_ID = '1Y70ljPoJSZnwTvT1Xmb7zGAnk7LXGRTGTtVZcwVgSgo'
PATTERN = r'(// \+\+GENERATED CARDS\+\+).+(// \-\-GENERATED CARDS\-\-)'

CARDS_MAP = {
    "undress": "coquin/src/game/cards/Undress.vue",
    "soft": "coquin/src/game/cards/Soft.vue",
    "coquin": "coquin/src/game/cards/Coquin.vue",
    "hot": "coquin/src/game/cards/Hot.vue",
    "hard": "coquin/src/game/cards/Hard.vue",
    "question": "coquin/src/game/cards/Question.vue",
    "action": "coquin/src/game/cards/Action.vue",
    "soumis": "coquin/src/game/cards/Soumis.vue",
    "end": "coquin/src/game/cards/End.vue",
    "gages": "coquin/src/game/cards/Gages.vue",
}

DECKS_MAP = {
    "soft_soumis": "coquin/src/game/decks/SoftSoumis.vue",
    "hot_soumis": "coquin/src/game/decks/HotSoumis.vue",
    "soft": "coquin/src/game/decks/Soft.vue",
    "coquin": "coquin/src/game/decks/Coquin.vue",
    "hot": "coquin/src/game/decks/Hot.vue",
    "soft_plus": "coquin/src/game/decks/SoftPlus.vue",
    "coquin_plus": "coquin/src/game/decks/CoquinPlus.vue",
    "hot_plus_ech": "coquin/src/game/decks/HotPlusEch.vue",
    "hot_plus_mel": "coquin/src/game/decks/HotPlusMel.vue",
}

class coquin(object):

    def __init__(self):
        self.sheet = self.connect()

        print("# Generate cards")
        self.compute_cards()
        print("# Generate decks")
        self.compute_decks()


    def connect(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        return service.spreadsheets()

    def get_cards(self, name):
        range_name = 'cards_%s!A1:D' % name
        result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=range_name).execute()
        return result.get('values', [])

    def get_deck_cards(self, name):
        range_name = '%s!A1:B' % name
        result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=range_name).execute()
        return result.get('values', [])

    def format_cards(self, cards, cards_type):
        formatted_cards = {}
        _id = 0
        for card in cards:
            _id = _id + 1
            if len(card) <= 1:
                continue
            _text = card[1]
            _for = None
            _timer = None
            cardid = None

            if _text == "":
                continue
            if len(card) > 2:
                _for =  card[2]
            if len(card) > 3:
                _timer = card[3]

            # action
            if cards_type == "action":
                cardid = "a%s" % _id
                formated_card = {
                        "type": "action",
                        "image": "/img/action.svg",
                        "text": _text
                    }
            # soft
            if cards_type == "soft":
                cardid = "s%s" % _id
                formated_card = {
                        "type": "soft",
                        "image": "/img/soft.svg",
                        "text": _text
                    }
            # hot
            if cards_type == "hot":
                cardid = "h%s" % _id
                formated_card = {
                        "type": "hot",
                        "image": "/img/hot.svg",
                        "text": _text
                    }
            # coquin
            if cards_type == "coquin":
                cardid = "c%s" % _id
                formated_card = {
                        "type": "coquin",
                        "image": "/img/coquin.svg",
                        "text": _text
                    }
            #hard
            if cards_type == "hard":
                cardid = "hd%s" % _id
                formated_card = {
                        "type": "hard",
                        "image": "/img/hard.svg",
                        "text": _text
                    }
            # question
            if cards_type == "question":
                cardid = "q%s" % _id
                formated_card = {
                        "type": "question",
                        "image": "/img/question.svg",
                        "text": _text
                    }
            # soumis
            if cards_type == "soumis":
                cardid = "sm%s" % _id
                formated_card = {
                        "type": "soumis",
                        "image": "/img/handcuffs.svg",
                        "text": _text
                    }
            # undress
            if cards_type == "undress":
                cardid = "u%s" % _id
                formated_card = {
                        "type": "undress",
                        "image": "/img/undress.svg",
                        "text": _text
                    }
            # end
            if cards_type == "end":
                cardid = "e%s" % _id
                formated_card = {
                        "type": "end",
                        "image": "/img/end.svg",
                        "text": _text
                    }

            # gage
            if cards_type == "gages":
                cardid = "g%s" % _id
                formated_card = {
                        "type": "gages",
                        "image": "/img/end.svg",
                        "text": _text
                    }

            if _for:
                formated_card['for'] = _for
            if _timer:
                formated_card['timer'] = _timer

            if cardid is None:
                continue

            formatted_cards[cardid] = formated_card

        json_cards = json.dumps(formatted_cards, sort_keys=True).encode('utf-8').decode('unicode-escape')
        return json_cards


    def format_deck_cards(self, cards):
        formatted_cards = {}
        for card in cards:
            if len(card) < 2:
                continue

            cardid = card[0]
            number = card[1]

            if cardid == "" or number == "":
                continue

            formatted_cards[cardid] = int(number)

        json_cards = json.dumps(formatted_cards, sort_keys=True).encode('utf-8').decode('unicode-escape')
        return json_cards

    def write_cards(self, cards, file_path):
        with open(file_path, 'r+') as f:
            file_content = f.read()
            new_file = re.sub(PATTERN, r'\1\ncards:%s\n\2' % cards, file_content, flags=re.DOTALL)
            f.seek(0)
            f.write(new_file)
            f.truncate()

    def write_deck_cards(self, cards, file_path):
        with open(file_path, 'r+') as f:
            file_content = f.read()
            new_file = re.sub(PATTERN, r'\1\ndeckCards:%s\n\2' % cards, file_content, flags=re.DOTALL)
            f.seek(0)
            f.write(new_file)
            f.truncate()

    def compute_cards(self):
        for cards_type in CARDS_MAP.keys():
            print("- %s" % cards_type)
            # Get cards
            cards = self.get_cards(cards_type)
            # format cards
            formatted_cards = self.format_cards(cards=cards, cards_type=cards_type)
            # write cards
            self.write_cards(cards=formatted_cards, file_path=CARDS_MAP[cards_type])


    def compute_decks(self):
        for deck in DECKS_MAP.keys():
            print("- %s" % deck)
            # Get cards
            cards = self.get_deck_cards(deck)
            # format cards
            formatted_cards = self.format_deck_cards(cards=cards)
            # write cards
            self.write_deck_cards(cards=formatted_cards, file_path=DECKS_MAP[deck])

if __name__ == '__main__':
    c = coquin()
