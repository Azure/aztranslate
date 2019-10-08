# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Translator Quick Starts
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

print("""\
======================
Azure Text Translation
======================

Welcome to a demo of the pre-built models for Text Translation provided
through Azure's Cognitive Services. This service translates text between
multiple languages.
""")

# Import the required libraries.

import sys
import os
import requests
import uuid
import json

from textwrap import fill
from mlhub.pkg import azkey

# Defaults.

SERVICE = "Text Translator"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

live = True

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False, baseurl=True)

# ----------------------------------------------------------------------
# Build the REST API URLs.
# ----------------------------------------------------------------------

path     = '/translate?api-version=3.0'
translate_url = endpoint + path

path = '/languages?api-version=3.0'
languages_url = endpoint + path

# Handle canned demonstration.
    
# if len(subscription_key) == 0:
#     live = False
#     with open(CANNED_PKL, 'rb') as f:
#         languages, sentiments, key_phrases, entities = pickle.load(f)
#     sys.stdout.write("""
# No subscription key was provided so we will continue with a canned
# demonstration. The analyses from the cloud through the API have previously
# been captured and so we will use them.
# """)
    
sys.stdout.write("""
Press Enter to continue: """)
answer = input()

headers  = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

print("""
===================
Supported Languages
===================

These are the languages supported by the Azure Translator for translation.
""")

response = requests.get(languages_url, headers=headers)
response = response.json()
translations = response['translation']

count = 1
for l in translations:
    if count%20 == 0:
        sys.stdout.write("""
Press Enter to continue: """)
        answer = input()
        print()
    t = translations[l]
    print("{:7} {} {:25} {:25}".format(l, t['dir'], t['name'], t['nativeName']))
    count += 1

print("""
That's {} languages in total.""".format(count))

sys.stdout.write("""
Press Enter to continue on to translations from English: """)
answer = input()

print("""
=============================
Text Translation from English
=============================

Below we demonstrate the translation of a variety of common phrases as we might
find when interacting with a voice command system.""")

utterances = [{ 'text': """
    Hi Tom, has my parcel arrived yet?
    Where is a good shop to buy mobile phones?
    Has Frederick replied to my email yet?
    We are running late, please start without us.
    Tell me the most important message this morning?
    When is a good time to meet Susan and Dave?
"""}]

print(utterances[0]['text'])
    
if live:
    params   = '&to=de&to=it&to=id&to=hi'
    request = requests.post(translate_url + params, headers=headers, json=utterances)
    response = request.json()

    lang  = response[0]['detectedLanguage']
    trans = response[0]['translations']

print("The supplied text was detected as '{}' with a score of '{}'.".
      format(lang['language'], lang['score']))

for t in trans:
    sys.stdout.write("""
Press Enter for a translation to {}: """.format(translations[t['to']]['name']))
    answer = input()
    sys.stdout.write(t['text'])

sys.stdout.write("""
Press Enter to continue on to translations back to English: """)
answer = input()

print("""
===========================
Translation back to English
===========================

Below we translate each of the above translations back to English. Again the 
source language is automatically identified.

Here's a reminder of the original English utterances:""")

print(utterances[0]['text'])

if live:
    params   = '&to=en'
    request = requests.post(translate_url + params, headers=headers, json=trans)
    reverse = request.json()

for t in reverse:
    lang  = t['detectedLanguage']
    trans = t['translations']
    sys.stdout.write("""
Press Enter for the translation from {} (language id score={}): """.
                     format(translations[lang['language']]['name'],
                            lang['score']))
    answer = input()
    sys.stdout.write(trans[0]['text'])
