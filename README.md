Azure Text Translation
======================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the pre-built Text Translation models provided through Azure's
Cognitive Services. This service translates text between multiple
languages, also identifying the source language. Many languages are
supported.

A free Azure subscription allowing up to 2,000,000 character
transactions is available from https://azure.microsoft.com/free/. Once
set up visit https://ms.portal.azure.com and Create a resource under
AI and Machine Learning called Text Translations. Once created you can
access the web API subscription key from the portal. This will be
prompted for in the demo.

Please note that this is *closed source software* which limits your
freedoms and has no guarantee of ongoing availability.

Visit the github repository for more details:
<https://github.com/gjwgit/aztranslate>

The Python code is based on the [Azure Text Translator Quick
Start](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-python-translate)

Usage
-----

- To install mlhub 

        $ pip3 install mlhub

- To install and run the pre-built model:

		$ ml install   aztranslate
		$ ml configure aztranslate
		$ ml demo      aztranslate
		$ ml analyse   aztranslate

