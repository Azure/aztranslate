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
		$ ml do        aztranslate
		$ ml limits    aztranslate

Demonstration
-------------

```console
$ ml demo aztranslate
======================
Azure Text Translation
======================

Welcome to a demo of the pre-built models for Text Translation provided
through Azure's Cognitive Services. This service translates text between
multiple languages.

The following file has been found and is assumed to contain an Azure Text
Translator subscription key. We will load the file and use this information.

    /home/gjw/.mlhub/aztranslate/private.py

Press Enter to continue: 

===================
Supported Languages
===================

These are the languages supported by the Azure Translator for translation.

af      ltr Afrikaans                 Afrikaans                
ar      rtl Arabic                    العربية                  
bg      ltr Bulgarian                 Български                
bn      ltr Bangla                    বাংলা                    
bs      ltr Bosnian                   bosanski (latinica)      
ca      ltr Catalan                   Català                   
cs      ltr Czech                     Čeština                  
cy      ltr Welsh                     Welsh                    
da      ltr Danish                    Dansk                    
de      ltr German                    Deutsch                  
el      ltr Greek                     Ελληνικά                 
en      ltr English                   English                  
es      ltr Spanish                   Español                  
et      ltr Estonian                  Eesti                    
fa      rtl Persian                   Persian                  
fi      ltr Finnish                   Suomi                    
fil     ltr Filipino                  Filipino                 
fj      ltr Fijian                    Fijian                   
fr      ltr French                    Français                 

Press Enter to continue: 

he      rtl Hebrew                    עברית                    
hi      ltr Hindi                     हिंदी                    
hr      ltr Croatian                  Hrvatski                 
ht      ltr Haitian Creole            Haitian Creole           
hu      ltr Hungarian                 Magyar                   
id      ltr Indonesian                Indonesia                
is      ltr Icelandic                 Íslenska                 
It      ltr Italian                   Italiano                 
ja      ltr Japanese                  日本語                      
ko      ltr Korean                    한국어                      
lt      ltr Lithuanian                Lietuvių                 
lv      ltr Latvian                   Latviešu                 
mg      ltr Malagasy                  Malagasy                 
ms      ltr Malay                     Melayu                   
mt      ltr Maltese                   Il-Malti                 
mww     ltr Hmong Daw                 Hmong Daw                
nb      ltr Norwegian                 Norsk                    
nl      ltr Dutch                     Nederlands               
otq     ltr Querétaro Otomi           Querétaro Otomi          
pl      ltr Polish                    Polski                   

Press Enter to continue: 

pt      ltr Portuguese                Português                
ro      ltr Romanian                  Română                   
ru      ltr Russian                   Русский                  
sk      ltr Slovak                    Slovenčina               
sl      ltr Slovenian                 Slovenščina              
sm      ltr Samoan                    Samoan                   
sr-Cyrl ltr Serbian (Cyrillic)        srpski (ćirilica)        
sr-Latn ltr Serbian (Latin)           srpski (latinica)        
sv      ltr Swedish                   Svenska                  
sw      ltr Kiswahili                 Kiswahili                
ta      ltr Tamil                     தமிழ்                    
te      ltr Telugu                    తెలుగు                   
th      ltr Thai                      ไทย                      
tlh     ltr Klingon                   Klingon                  
to      ltr Tongan                    lea fakatonga            
tr      ltr Turkish                   Türkçe                   
ty      ltr Tahitian                  Tahitian                 
uk      ltr Ukrainian                 Українська               
ur      rtl Urdu                      اردو                     
vi      ltr Vietnamese                Tiếng Việt             

Press Enter to continue: 

yua     ltr Yucatec Maya              Yucatec Maya             
yue     ltr Cantonese (Traditional)   粵語 (繁體中文)                
zh-Hans ltr Chinese Simplified        简体中文                     
zh-Hant ltr Chinese Traditional       繁體中文                     

That's 64 languages in total.

Press Enter to continue on to translations from English: 

=============================
Text Translation from English
=============================

Below we demonstrate the translation of a variety of common phrases as we might
find when interacting with a voice command system.

    Hi Tom, has my parcel arrived yet?
    Where is a good shop to buy mobile phones?
    Has Frederick replied to my email yet?
    We are running late, please start without us.
    Tell me the most important message this morning?
    When is a good time to meet Susan and Dave?

The supplied text was detected as 'en' with a score of '1.0'.

Press Enter for a translation to German: 

    Hallo Tom, ist mein Paket schon angekommen?
    Wo gibt es einen guten Laden, um Handys zu kaufen?
    Hat Frederick meine E-Mail schon beantwortet?
    Wir laufen spät, bitte starten wir ohne uns.
    Sagen Sie mir heute Morgen die wichtigste Botschaft?
    Wann ist ein guter Zeitpunkt, um Susan und Dave zu treffen?

Press Enter for a translation to Italian: 

    Ciao Tom, il mio pacco è arrivato ancora?
    Dove è un buon negozio per comprare telefoni cellulari?
    Frederick ha risposto alla mia email ancora?
    Siamo in ritardo, per favore iniziate senza di noi.
    Dimmi il messaggio più importante di stamattina?
    Quando è il momento giusto per incontrare Susan e Dave?

Press Enter for a translation to Indonesian: 

    Hi Tom, telah paket saya tiba belum?
    Di mana toko yang baik untuk membeli ponsel?
    Apakah Frederick membalas email saya?
    Kami berjalan terlambat, silakan mulai tanpa kami.
    Ceritakan pesan yang paling penting pagi ini?
    Kapan waktu yang baik untuk bertemu Susan dan Dave?

Press Enter for a translation to Hindi: 

    हाय टॉम, मेरे पार्सल अभी तक आ गया है?
    मोबाइल फोन खरीदने के लिए एक अच्छी दुकान कहां है?
    क्या Frederick मेरे ईमेल के लिए अभी तक जवाब दिया?
    हम देर से चल रहे हैं, कृपया हमारे बिना शुरू करो ।
    मुझे सबसे महत्वपूर्ण संदेश आज सुबह बताओ?
    जब एक अच्छा समय Susan और डेव से मिलने के लिए है?

Press Enter to continue on to translations back to English: 

===========================
Translation back to English
===========================

Below we translate each of the above translations back to English. Again the 
source language is automatically identified.

Here's a reminder of the original English utterances:

    Hi Tom, has my parcel arrived yet?
    Where is a good shop to buy mobile phones?
    Has Frederick replied to my email yet?
    We are running late, please start without us.
    Tell me the most important message this morning?
    When is a good time to meet Susan and Dave?


Press Enter for the translation from German (language id score=0.98): 

    HI Tom, has my Package arrived yet?
    Where is a good Store to buy Phones?
    Has Frederick already answered my email?
    We run late, please start without us.
    Tell me the most important Message this Morning?
    When is a good Time to meet Susan and Dave?

Press Enter for the translation from Italian (language id score=0.94): 

    Hello Tom, my parcel has arrived yet?
    Where is a good store to buy cell phones?
    Has Frederick responded to my email yet?
    We'Re late, please start without us.
    Tell me the most important message this morning?
    When is the right time to meet Susan and Dave?

Press Enter for the translation from Indonesian (language id score=0.98): 

    Hi Tom, have my package arrived yet?
    Where is a good store to buy a cell phone?
    Did Frederick replied to my email?
    We are running late, please start without us.
    Tell me the most important message this morning?
    When is a good time to meet Susan and Dave?

Press Enter for the translation from Hindi (language id score=0.97): 

    Hi Tom, has my parcel come yet?
    Where is a good shop to buy mobile phones?
    Has Frederick responded to my email yet?
    We are running late, please start without us.
    Tell me the most important message this morning?
    When is a good time to meet Susan and Dave?

To use the model to translate user provided text:

  $ ml do aztranslate
```

Interactive Use
---------------

We can interact with the model simply. Here we enter a few texts in
different languages and have them translated into English. Note the
variability of the competency of the translation. Translation from the
Indonesian language is not as well developed as other languages!

```console
$ ml do aztranslate
================================
Azure Text Translation to English
=================================

The following file has been found and is assumed to contain an Azure Text
Translator subscription key. We will load the file and use this information.

    /home/gjw/.mlhub/aztranslate/private.py

Enter a line of text in any language and we'll attempt to translate it to English.

Exit when no text supplied.

> सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त है। उन्हें
> बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के भाव से बर्ताव करना चाहिये।

The text was identified as Hindi with 100% certainty:
    
  English: All human beings have inherent freedom and equality in 
  terms of pride and rights. They have the wisdom and the conscience,
  and they must behave in a spirit of brotherhood.

> C’est l’exception qui confirme la règle.

The text was identified as French with 100% certainty:
    
  English: This is the exception that confirms the rule.

> Dimana ada kemauan, di situ ada jalan

The text was identified as Indonesian with 100% certainty:
    
  English: Where there's a will, there is no way

> 

To explore limitations of translations:

  $ ml limits aztranslate
```

Limitations of Translations
---------------------------

Douglas Hofstadter, a professor of cognitive science and comparative
literature at Indiana University at Bloomington and author of the book
Gödel, Escher, Bach, highlights in a January 2018 article in The
Atlantic the limitations of automated language translation. To
paraphrase, the translators do not have any deep understanding of the
text but have developed a shallower mechanical process to do a decent job
for simple communications.

Below we illustrate with one of Hofstadter's examples which you can
replicate with the LIMITS command. See the original article for
details:

https://www.theatlantic.com/technology/archive/2018/01/the-shallowness-of-google-translate/551570/

```console
$ ml limits aztranslate

[...]

*** Consider this sample text:

In their house, everything comes in pairs. There's his car and her
car, his towels and her towels, and his library and hers.

*** The French translation is:

Dans leur maison, tout se passe par paires. Il y a sa voiture, sa
voiture, ses serviettes, ses serviettes, sa bibliothèque et la sienne.

*** Translating back to English demonstrates a shallow understanding:

In their House, everything happens in pairs. There's his car, his car,
his towels, his towels, his library and hers.
```

