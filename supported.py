# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A command line script to list supported languages.
#
# ml supported aztranslate
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
# Parse the command line arguments: language header
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'language',
    nargs="?",
    help='a language code to check')

option_parser.add_argument(
    '--header',
    action='store_true')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

SERVICE  = "Text Translator"
KEY_FILE = os.path.join(os.getcwd(), "private.txt")

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False, baseurl=True)

# ----------------------------------------------------------------------
# Build the REST API.
# ----------------------------------------------------------------------

url = endpoint + '/languages?api-version=3.0'

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

# ------------------------------------------------------------------------
# Obtain and print supported languages.
# ------------------------------------------------------------------------

response = requests.get(url, headers=headers)
response = response.json()
translations = response['translation']

if args.header: print("code,direction,name,native_name")

for l in translations:
    t = translations[l]
    if args.language == None or args.language in l:
        print(f"{l},{t['dir']},{t['name']},{t['nativeName']}")
