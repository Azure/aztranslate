# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Translator Quick Starts
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import sys
import os
import requests
import uuid
import json
import argparse

from textwrap import fill
from mlhub.pkg import azkey

# Defaults.

SERVICE = "Text Translator"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

# ----------------------------------------------------------------------
# Parse command line arguments: text
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'text',
    nargs="*",
    help='text to translate')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

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

def translateText(txt):
    smpl = [{'text': txt}]

    params   = '&to=en'
    request = requests.post(translate_url + params, headers=headers, json=smpl)
    smpl_en = request.json()

    sys.stdout.write(f"{smpl_en[0]['detectedLanguage']['language']}," +
                     f"{smpl_en[0]['detectedLanguage']['score']:0.2f}," +
                     f"{smpl_en[0]['translations'][0]['to']}," +
                     f"{smpl_en[0]['translations'][0]['text']}")
    
# ------------------------------------------------------------------------
# Obtain text and translate.
# ------------------------------------------------------------------------

txt = " ".join(args.text)

if txt != "":
    translateText(txt)
    print()
elif not sys.stdin.isatty():
    for txt in sys.stdin.readlines():
        translateText(txt)
else:
    print("Enter text to be analysed. Quit with Empty or Ctrl-d.\n")
    prompt = '> '
    try:
        txt = input(prompt)
    except EOFError:
        print()
        sys.exit(0)

    while txt != '':

        translateText(txt)

        try:
            print()
            txt = input(prompt)
        except EOFError:
            print()
            sys.exit(0)

