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

if os.path.isfile(KEY_FILE):
    if os.path.getsize(KEY_FILE) != 0:
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
====================
Suppported Languages
====================

These are the languages supported by the Azure Translator for translation.
""")

response = requests.get(languages_url, headers=headers)
response = response.json()
translations = response['translation']

#print(json.dumps(translations, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
#print(json.dumps(translations))

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
Press Enter to continue: """)
answer = input()

print("""
=============================
Text Translation from English
=============================

Below we demonstrate the translation of the text from the lyrics of a famous
song to a collection of languages. Notice for convenience of formatting of the
output each line is terminated with a sentence punctuation.""")

wish_you_were_here = [{ 'text': """
    So, so you think you can tell.
    Heaven from hell.
    Blue skies from pain.
    Can you tell a green field.
    From a cold steel rail?
    A smile from a veil?
    Do you think you can tell?
"""}]

print(wish_you_were_here[0]['text'])
    
if live:

    params   = '&to=de&to=it&to=id&to=tlh&to=hi'
    request = requests.post(translate_url + params, headers=headers, json=wish_you_were_here)
    response = request.json()

lang = response[0]['detectedLanguage']
print("The supplied text was detected as '{}' with a score of '{}'.".
      format(lang['language'], lang['score']))

trans = response[0]['translations']
for t in trans:
    sys.stdout.write("""
Press Enter for a translation to '{}': """.format(t['to']))
    answer = input()

    sys.stdout.write(t['text'])

    
