# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A comman line script to translate text
#
# ml translate aztranslate [<text>]
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

# ----------------------------------------------------------------------
# Import the required libraries.
# ----------------------------------------------------------------------

import sys
import os
import argparse

import requests
import uuid
import json

from mlhub.pkg import azkey

# ----------------------------------------------------------------------
# Parse command line arguments: text to
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'text',
    nargs="*",
    help='text to translate')

option_parser.add_argument(
    '-t', '--to',
    help='target language')

args = option_parser.parse_args()

to = "en" if args.to == None else args.to

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

SERVICE = "Text Translator"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False, baseurl=True)

# ----------------------------------------------------------------------
# Build the REST API URLs.
# ----------------------------------------------------------------------

path     = '/translate?api-version=3.0'
translate_url = endpoint + path

headers  = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

# ------------------------------------------------------------------------
# Helper function.
# ------------------------------------------------------------------------

def translateText(txt, to):
    smpl = [{'text': txt}]

    params   = '&to=' + to
    request = requests.post(translate_url + params, headers=headers, json=smpl)
    smpl_en = request.json()

    sys.stdout.write(f"{smpl_en[0]['detectedLanguage']['language']}," +
                     f"{smpl_en[0]['detectedLanguage']['score']:0.2f}," +
                     f"{smpl_en[0]['translations'][0]['to']}," +
                     f"{smpl_en[0]['translations'][0]['text']}")
    
# ------------------------------------------------------------------------
# Translate text obtained from command line, pipe, or interactively.
# ------------------------------------------------------------------------

txt = " ".join(args.text)

if txt != "":
    translateText(txt, to)
    print()
elif not sys.stdin.isatty():
    for txt in sys.stdin.readlines():
        translateText(txt, to)
else:
    print("Enter text to be analysed. Quit with Empty or Ctrl-d.\n")
    prompt = '> '
    try:
        txt = input(prompt)
    except EOFError:
        print()
        sys.exit(0)
    while txt != '':
        translateText(txt, to)
        try:
            print()
            txt = input(prompt)
        except EOFError:
            print()
            sys.exit(0)

