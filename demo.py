# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Translator Quick Starts
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

print("""======================
Azure Text Translation
======================

Welcome to a demo of the pre-built models for Text Translation provided
through Azure's Cognitive Services. This service translates text between
multiple languages.
""")

# Defaults.

KEY_FILE = "private.py"

subscription_key = None
live = True

# Build the REST API URLs.

base_url = 'https://api.cognitive.microsofttranslator.com'

path     = '/translate?api-version=3.0'
translate_url = base_url + path

path = '/languages?api-version=3.0'
languages_url = base_url + path

# Import the required libraries.

import sys
import os
import requests
import uuid
import json
from textwrap import fill

# Prompt the user for the key and save into private.py for
# future runs of the model. The contents of that file is:
#
# subscription_key = "a14d...ef24"

key_found = os.path.isfile(KEY_FILE)

if os.path.isfile(KEY_FILE) and os.path.getsize(KEY_FILE) != 0:
    print("""The following file has been found and is assumed to contain an Azure Text
Translator subscription key. We will load the file and use this information.

    """ + os.getcwd() + "/" + KEY_FILE)
    exec(open(KEY_FILE).read())
else:
    print("""An Azure resource is required to access this service (and to run this
demo). See the README for details of a free subscription. Then you can
provide the key and the region information here.
""")
#If you don't have a key and want to review the canned examples rather
#than work with the live examples, you can indeed continue simply by 
#pressing the Enter key.
#""")
    sys.stdout.write("Please enter your Text Analytics subscription key []: ")
    subscription_key = input()

    if len(subscription_key) > 0:
        assert subscription_key
        oKEY_FILE = open(KEY_FILE, "w")
        oKEY_FILE.write("""subscription_key = "{}"
assert subscription_key
    """.format(subscription_key))
        oKEY_FILE.close()

        print("""
I've saved that information into the file:

""" + os.getcwd() + "/" + KEY_FILE)

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
    'Ocp-Apim-Subscription-Key': subscription_key,
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

sys.stdout.write("""
Press Enter to continue on to Issues: """)
answer = input()

print("""
===========================
Limitations of Translations
===========================

Douglas Hofstadter, a professor of cognitive science and comparative
literature at Indiana University at Bloomington and author of the book
Gödel, Escher, Bach, highlights in a January 2018 article in The
Atlantic the limitations of automated language translation. To
paraphrase, the translators do not have any deep understanding of the
text but have developed a shallower mechanical process to do a decent job
for simple communications.

Below we illustrate with one of Hofstadter's examples. See the
original article for details:

https://www.theatlantic.com/technology/archive/2018/01/the-shallowness-of-google-translate/551570/

*** The sample text is:
""")

hof_or = [{'text': """In their house, everything comes in pairs. There's his car
and her car, his towels and her towels, and his library and hers."""}]

sys.stdout.write(fill(hof_or[0]['text']))

sys.stdout.write("""

*** The French translation is:

""")

if live:
    params   = '&to=fr'
    request = requests.post(translate_url + params, headers=headers, json=hof_or)
    hof_fr = request.json()

sys.stdout.write(fill(hof_fr[0]['translations'][0]['text']))

sys.stdout.write("""

*** Translating back to English demonstrates a shallow understanding:

""")

if live:
    params   = '&to=en'
    request = requests.post(translate_url + params, headers=headers, json=hof_fr[0]['translations'])
    hof_en = request.json()

sys.stdout.write(fill(hof_en[0]['translations'][0]['text']))
print()

# Google had: 
#
#     Dans leur maison, tout vient en paires. Il y a sa voiture et sa
#     voiture, ses serviettes et ses serviettes, sa bibliothèque et
#     les siennes.
#
#     Then
#
#     At home, they have everything in double. There is his own car
#     and his own car, his own towels and his own towels, his own
#     library and his own library.
