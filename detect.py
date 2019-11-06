# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A comman line script to detect the language of provided text.
#
# ml detect aztranslate [<text>]
# 
# https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python
#

# ----------------------------------------------------------------------
# Import the required libraries.
# ----------------------------------------------------------------------

import os
import sys

import argparse
import requests
import uuid
import json

from mlhub.pkg import azkey
from mlhub.utils import get_cmd_cwd

# ----------------------------------------------------------------------
# Parse command line arguments: text
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'text',
    nargs="*",
    help='text to translate')

option_parser.add_argument(
    '--header',
    action='store_true')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

SERVICE = "Text Translator"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

# Request.

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False, baseurl=True)

# ----------------------------------------------------------------------
# Build the REST API URLs.
# ----------------------------------------------------------------------

path = '/detect?api-version=3.0'
url  = endpoint + path

headers  = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

# ------------------------------------------------------------------------
# Helper function.
# ------------------------------------------------------------------------

def helper(txt):
    smpl = [{'text': txt}]

    request = requests.post(url, headers=headers, json=smpl)
    result = request.json()

    sys.stdout.write(f"{result[0]['language']}," +
                     f"{result[0]['score']:0.2f}," +
                     f"{result[0]['isTranslationSupported']}," +
                     f"{result[0]['isTransliterationSupported']}" )

# ------------------------------------------------------------------------
# Translate text obtained from command line, pipe, or interactively.
# ------------------------------------------------------------------------

txt = " ".join(args.text)

fname = os.path.join(get_cmd_cwd(), txt)

if args.header: print("language,score,translate,transliterate")

if len(args.text) == 1 and os.path.isfile(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    for l in lines:
        helper(l)
        print()
elif txt != "":
    helper(txt)
    print()
elif not sys.stdin.isatty():
    for txt in sys.stdin.readlines():
        helper(txt)
else:
    print("Enter text to be analysed. Quit with Empty or Ctrl-d.\n")
    prompt = '> '
    try:
        txt = input(prompt)
    except EOFError:
        print()
        sys.exit(0)
    while txt != '':
        helper(txt)
        try:
            print()
            txt = input(prompt)
        except EOFError:
            print()
            sys.exit(0)

