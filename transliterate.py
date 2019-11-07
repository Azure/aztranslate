# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A comman line script to transliterate text
#
# ml transliterate aztranslate [<text>]
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
    '-l', '--lang',
    help='language')

option_parser.add_argument(
    '-f', '--source', '--from',
    help='source script')

option_parser.add_argument(
    '-t', '--to',
    help='target script')

option_parser.add_argument(
    '-k', '--keep',
    action="store_true",
    help='keep original text in output')

args = option_parser.parse_args()

lang = args.lang
fr   = args.source
to   = args.to if args.to != None else 'latn'

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

SERVICE = "Text Translator"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False, baseurl=True)

# ----------------------------------------------------------------------
# Build the REST API URLs.
# ----------------------------------------------------------------------

path     = '/transliterate?api-version=3.0'
url = endpoint + path

headers  = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

# ------------------------------------------------------------------------
# Helper function.
# ------------------------------------------------------------------------

def helper(txt, lang, fr, to):
    smpl = [{'text': txt}]

    # Auto determine LANG and then use first script in the SUPPORTED
    # output as default for FR

    if lang is None:
        durl = endpoint + '/detect?api-version=3.0'
        result = requests.post(durl, headers=headers, json=smpl).json()
        lang = result[0]['language']
        # print(lang)

    if fr is None:
        turl = endpoint + '/languages?api-version=3.0'
        response = requests.get(turl, headers=headers).json()['transliteration']
        fr = response[lang]['scripts'][0]['code']
        # print(fr)

    params = f"&language={lang}&fromScript={fr}&toScript={to}"
    request = requests.post(url + params, headers=headers, json=smpl)
    result = request.json()

    sys.stdout.write(f"{result[0]['text']}")
    
# ------------------------------------------------------------------------
# Translate text obtained from command line, pipe, or interactively.
# ------------------------------------------------------------------------

txt = " ".join(args.text)

if txt != "":
    helper(txt, lang, fr, to)
    print()
elif not sys.stdin.isatty():
    for txt in sys.stdin.readlines():
        helper(txt, lang, fr, to)
else:
    print("Enter text to be analysed. Quit with Empty or Ctrl-d.\n")
    prompt = '> '
    try:
        txt = input(prompt)
    except EOFError:
        print()
        sys.exit(0)
    while txt != '':
        helper(txt, lang, fr, to)
        try:
            print()
            txt = input(prompt)
        except EOFError:
            print()
            sys.exit(0)

