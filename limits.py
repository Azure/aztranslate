# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Translator Quick Starts
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

print("""===========================
Limitations of Translations
===========================

Douglas Hofstadter, a professor of cognitive science and comparative
literature at Indiana University at Bloomington and author of the book
Gödel, Escher, Bach, highlights in a January 2018 article in The
Atlantic the limitations of automated language translation. To
paraphrase, the translators do not have any deep understanding of the
text but have developed a shallower mechanical process to do a decent job
for simple communications.

Below we illustrate the issue with one of Hofstadter's examples. See the
original article for details:

https://www.theatlantic.com/technology/archive/2018/01/the-shallowness-of-google-translate/551570/

The original article demonstrated the issue using Google Translator. We
demonstrate using Azure Translator.
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

headers  = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

sys.stdout.write("""
Press Enter to continue on to the example: """)
answer = input()

print("""
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
