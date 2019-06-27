# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Translator Quick Starts
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

print("""================================
Azure Text Translation to English
=================================
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
    
headers  = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

print("""
Enter a line of text in any language and we'll attempt to translate it to English.

Exit when no text supplied.
""")
      

while True:
    
    print("> ", end="")

    text = input()

    if len(text) == 0: break
    
    smpl = [{'text': text}]

    params   = '&to=en'
    request = requests.post(translate_url + params, headers=headers, json=smpl)
    smpl_en = request.json()

    sys.stdout.write("""
The text was identified as {} with {}% certainty:
    
  {}: {}

""".format(smpl_en[0]['detectedLanguage']['language'],
           round(100*smpl_en[0]['detectedLanguage']['score']),
           smpl_en[0]['translations'][0]['to'],
           smpl_en[0]['translations'][0]['text']))


# sys.stdout.write(fill(hof_fr[0]['translations'][0]['text']))

# sys.stdout.write("""

# *** Translating back to English demonstrates a shallow understanding:

# """)

# if live:
#     params   = '&to=en'
#     request = requests.post(translate_url + params, headers=headers, json=hof_fr[0]['translations'])
#     hof_en = request.json()

# sys.stdout.write(fill(hof_en[0]['translations'][0]['text']))
# print()

# # Google had: 
# #
# #     Dans leur maison, tout vient en paires. Il y a sa voiture et sa
# #     voiture, ses serviettes et ses serviettes, sa bibliothèque et
# #     les siennes.
# #
# #     Then
# #
# #     At home, they have everything in double. There is his own car
# #     and his own car, his own towels and his own towels, his own
# #     library and his own library.
