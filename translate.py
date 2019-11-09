# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A comman line script to translate text.
#
# ml translate aztranslate [<text>]
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
# Parse command line arguments: text --source --to --keep
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'text',
    nargs="*",
    help='text to translate')

option_parser.add_argument(
    '-s', '--source',
    help='source language')

option_parser.add_argument(
    '-t', '--to',
    help='target language')

option_parser.add_argument(
    '-p', '--profanity',
    action="store_true",
    help='remove profanity')

option_parser.add_argument(
    '-k', '--keep',
    action="store_true",
    help='keep original text in output')

args = option_parser.parse_args()

fr = args.source
to = "en" if args.to == None else args.to

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

path = '/translate?api-version=3.0'
url  = endpoint + path

headers  = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}  

# ------------------------------------------------------------------------
# Helper function.
# ------------------------------------------------------------------------

def helper(txt, fr, to):
    smpl = [{'text': txt}]

    params   = '&to=' + to
    if args.profanity:
        params = params + "&ProfanityAction=Marked&ProfanityMarker=Asterisk"
    if fr != None:
        params = params + f"&from={fr}"
    # print(params)
    request = requests.post(url + params, headers=headers, json=smpl)
    result = request.json()

    if fr == None:
        detectedl = result[0]['detectedLanguage']['language']
        detecteds = result[0]['detectedLanguage']['score']
    else:
        detectedl = fr
        detecteds = 1.0
        
    sys.stdout.write(f"{detectedl}," +
                     f"{detecteds:0.2f}," +
                     f"{result[0]['translations'][0]['to']}," )

    if args.keep:
        sys.stdout.write(f"{txt.rstrip()},")
        
    sys.stdout.write(f"{result[0]['translations'][0]['text']}")
    
# ------------------------------------------------------------------------
# Translate text obtained from command line, pipe, or interactively.
# ------------------------------------------------------------------------

txt = " ".join(args.text)

fname = os.path.join(get_cmd_cwd(), txt)

if len(args.text) == 1 and os.path.isfile(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    for l in lines:
        helper(l, fr, to)
        print()
elif txt != "":
    helper(txt, fr, to)
    print()
elif not sys.stdin.isatty():
    for txt in sys.stdin.readlines():
        helper(txt, fr, to)
else:
    print("Enter text to be analysed. Quit with Empty or Ctrl-d.\n")
    prompt = '> '
    try:
        txt = input(prompt)
    except EOFError:
        print()
        sys.exit(0)
    while txt != '':
        helper(txt, fr, to)
        try:
            print()
            txt = input(prompt)
        except EOFError:
            print()
            sys.exit(0)

