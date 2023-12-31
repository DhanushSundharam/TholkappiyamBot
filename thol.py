import json
import pandas as pd
from telegram import Update, ForceReply
#from telegram.ext import Filters
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters,CallbackContext 
from typing import Dict

__version__ = '0.0.2'
__author__ = 'i18n Solutions'


tk=[
  {
    "adhikaaram": "எழுத்ததிகாரம்",
    "adhikaaram_eng":"Phonology and Morphophonemics",
    "iyal": [
      {
        "iyal_name": "நூல் மரபு",
        "iyal_eng":"Conventions of Phonology and Orthography",
        "noorpa": [
          {
            "paadal":"எழுத்து எனப்படுப\nஅகரம் முதல் னகர இறுவாய்\nமுப்பஃது என்ப\nசார்ந்து வரல் மரபின் மூன்று அலங்கடையே.",
            "vilakkam":
            { 
              "paadal_category":"Number of Phonemes in Tamil", 
              "paadal_meaning":"The thirty (sounds) from a (அ) to ṉ (ன) except the three secondary ones are termed Eḻuttu (எழுத்து)."
            }
          },
          {
            "paadal": 
            "அவைதாம்,\nகுற்றியலிகரம் குற்றியலுகரம்\nஆய்தம் என்ற\nமுப்பாற்புள்ளியும் எழுத்து ஓரன்ன. ",
            "vilakkam": 
            {
              "paadal_category":"The Secondary Phonemes", 
              "paadal_meaning":"They (secondary sounds) are i (இ), u (உ) and ḵ (ஃ) which are represented by dots (in script)."
            }
          },
          {
            "paadal": 
            "அவற்றுள்,\nஅ இ உ\nஎ ஒ என்னும் அப் பால் ஐந்தும்\nஓர் அளபு இசைக்கும் குற்றெழுத்து என்ப.",
            "vilakkam": 
            {
              "paadal_category":"Short Vowels and the Duration of their Articulation", 
              "paadal_meaning":"Of them the five sounds a (அ), i (இ), u (உ), e (எ) and o (ஒ) are called kuṟṟeḻuttu (குற்றெழுத்து) or short sounds and sound one aḷapu (அளபு) or mātrā (மாத்திரை) each."  
            }
          },
          {
            "paadal": "ஆ ஈ ஊ ஏ ஐ \nஓ ஔ என்னும் அப் பால் ஏழும் \nஈர் அளபு இசைக்கும் நெட்டெழுத்து என்ப. ",
            "vilakkam": 
            {
              "paadal_category":"Long Vowels and the Duration of their Articulation", 
              "paadal_meaning":"The seven ā (ஆ), ī (ஈ), ū (ஊ), ē (ஏ), ai (ஐ), ō (ஓ) and au (ஔ) are called neṭṭeḻuttu (நெட்டெழுத்து) or long sounds and sound two mātras (மாத்திரை) each."
            }
          },
          {
            "paadal": "மூ அளபு இசைத்தல் ஓர் எழுத்து இன்றே.",
            "vilakkam": 
            {
              "paadal_category":"Non-existence of Phoneme requiring Three Māttirai (மாத்திரை)", 
              "paadal_meaning":"One eḻuttu (எழுத்து) never sounds three mātras (மாத்திரை)."
            }
          },
          {
            "paadal": "நீட்டம் வேண்டின் அவ் அளபுடைய \nகூட்டி எழூஉதல் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category":"Extra-lenthening of Vowels and their Māttirai (மாத்திரை)", 
              "paadal_meaning":"Learned men say that, to lengthen the sound, a short vowel or vowels should be produced after the long vowel according to the quantity needed. Ex. āa (ஆ), īi (ஈ) etc."
            }
          },
          {
            "paadal": "கண் இமை நொடி என அவ்வே மாத்திரை \nநுண்ணிதின் உணர்ந்தோர் கண்ட ஆறே.",
            "vilakkam": 
            {
              "paadal_category":"Duration of Māttirai (மாத்திரை)", 
              "paadal_meaning":"One mātrā (மாத்திரை) is the time taken for one wink of-the eyes or one snap of the fingers. This is the view of accurate grammarians."
            }
          },
          {
            "paadal": "ஔகார இறுவாய்ப் \nபன்னீர் எழுத்தும் உயிர் என மொழிப. ",
            "vilakkam": 
            {
              "paadal_category":"Number of Vowels",  
              "paadal_meaning":"The twelve letters (beginning with a (அ) and) ending with au (ஔ) are called uyir (உயிர்) or vowels."
            }
          },
          {
            "paadal": "னகார இறுவாய்ப் \nபதினெண் எழுத்தும் மெய் என மொழிப. ",
            "vilakkam": 
            {
              "paadal_category":"Number of Consonants", 
              "paadal_meaning":"The eighteen letters (beginning with k (க்) and) ending with ṉ (ன்) are called mey or consonants."
            }
          },
          {
            "paadal": "மெய்யொடு இயையினும் உயிர் இயல் திரியா. ",
            "vilakkam": 
            {
              "paadal_category":"Māttirai (மாத்திரை) for Consonantal Articulation",
              "paadal_meaning":"The nature of vowels is not altered even when pronounced after consonants (i.e.) ka (கா), ca (ச), etc. has each only one mātrā (மாத்திரை)."
            }
          },
          {
            "paadal": "மெய்யின் அளபே அரை என மொழிப.",
            "vilakkam": 
            {
              "paadal_category":"Māttirai (மாத்திரை) for Consonantal Articulation",
              "paadal_meaning":"The quantity of a consonant is half a mātrā. (மாத்திரை)"
            }
          },
          {
            "paadal": "அவ் இயல் நிலையும் ஏனை மூன்றே. ",
            "vilakkam": 
            {
              "paadal_category":"Māttirai (மாத்திரை) for the Secondary Phonemes", 
              "paadal_meaning":"The other three too (the secondary vowels) are of the same nature; (i.e.) the quantity of i (இ), u (உ) and ḵ(ஃ) is half a matra each."
            }
          },
          {
            "paadal": "அரை அளபு குறுகல் மகரம் உடைத்தே\n இசையிடன் அருகும் தெரியும் காலை. ",
            "vilakkam": 
            {
              "paadal_category":"/m/ ம் with reduced Māttirai (மாத்திரை)", 
              "paadal_meaning":"The quantity of m (ம்) is shortened to quarter of a mātrā (மாத்திரை) when it follows some consonants. Ex. pōnṁ (போன்)."
            }
          },
          {
            "paadal": "உட் பெறு புள்ளி உரு ஆகும்மே. ",
            "vilakkam": 
            {
              "paadal_category":"The symbol 'ம்' with reduced articulatory measure", 
              "paadal_meaning":"Its symbol is that of m (மஂ) with a dot within."
            }
          },
          {
            "paadal": "மெய்யின் இயற்கை புள்ளியொடு நிலையல். ",
            "vilakkam": 
            {
              "paadal_category":"The Consonant Symbols", 
              "paadal_meaning":"The nature of the consonant symbol is that it is provided with a dot. viz., (iku (க்)), (ichu (ச்)) etc. for k (க), c (ச) etc."
            }
          },
          {
            "paadal": "எகர ஒகரத்து இயற்கையும் அற்றே.",
            "vilakkam": 
            {
              "paadal_category":"The symbols of e(எ) and o(ஒ)",
              "paadal_meaning":"E and o also are of the same nature, (i.e.) the short e(எ) ar the short o(ஒ) should be written as (ea (எ)) and (oo (ஒ))"
            }
          },
          {
            "paadal": "புள்ளி இல்லா எல்லா மெய்யும் \nஉரு உரு ஆகி அகரமொடு உயிர்த்தலும் \nஏனை உயிரொடு உருவு திரிந்து உயிர்த்தலும்\n ஆயீர் இயல உயிர்த்தல் ஆறே. ",
            "vilakkam": 
            {
              "paadal_category":"The Consonant-Vowel Symbols", 
              "paadal_meaning":"All consonant symbols without dots etc. represent consonant sounds followed by a and those for consonants followed by other vowels are different."
            }
          },
          {
            "paadal": "மெய்யின் வழியது உயிர் தோன்று நிலையே. ",
            "vilakkam": 
            {
              "paadal_category":"The Consonant-Vowel Symbols", 
              "paadal_meaning":"Vowel follows a consonant in uyir-mey (உயிர்-மெய்) or consonant-vowels as ka (கா), ki (கி), ku (கு) etc."
            }
          },
          {
            "paadal": "வல்லெழுத்து என்ப க ச ட த ப ற. ",
            "vilakkam": 
            {
              "paadal_category":"Types of consonants - Hard Consonants", 
              "paadal_meaning":"K (க), c (ச), ṭ (ட), t (த), p (ப) and ṟ (ற) are called, valleḻuttu (வல்லெழுத்து) or hard or voiceless consonants."
            }
          },
          {
            "paadal": "மெல்லெழுத்து என்ப ங ஞ ண ந ம ன.",
            "vilakkam": 
            {
              "paadal_category":"Types of consonants - Soft Consonants",
              "paadal_meaning":"ṅ (ங), ñ (ஞ), ṇ (ண), n (ந), m (ம) and ṉ (ன) are called melleḻuttu (மெல்லெழுத்து) or nasals."
            }
          },
          {
            "paadal": "இடையெழுத்து என்ப ய ர ல வ ழ ள.",
            "vilakkam": 
            {
              "paadal_category":"Types of consonants - Medial Consonants",
              "paadal_meaning":"Y (ய), r (ர), l (ல) v (வ), ḻ (ழ)and ḷ (ள) are called iṭaiyeḻuttu (இடையெழுத்து) or semi-vowels."
            }
          },
          {
            "paadal": "அம் மூ ஆறும் வழங்கு இயல் மருங்கின்\n மெய்ம்மயக்கு உடனிலை தெரியும் காலை.",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "The above eighteen (consonants), when carefully examined in their usage, are followed by the same consonants or by different consonants and the former is called uṭaṉilaimayakkam (இயல் மருங்கின்) and the latter meymmayakkam (மெய்ம்மயக்கு). "
            }
          },
          {
            "paadal": "ட ற ல ள என்னும் புள்ளி முன்னர் \nக ச ப என்னும் மூ எழுத்து உரிய. ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "Only k (க), c (ச) and p (ப) can follow ṭ (ட), ṟ (ற), l (ல) and ḷ (ள). "
            }
          },
          {
            "paadal": "அவற்றுள், \nல ளஃகான் முன்னர் ய வவும் தோன்றும். ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "Y (ய) and v (வ) also can follow l (ல) and ḷ (ள)."
            }
          },
          {
            "paadal": "ங ஞ ண ந ம ன எனும் புள்ளி முன்னர் \nதம்தம் இசைகள் ஒத்தன நிலையே. ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "ṅ (ங), ñ (ஞ), ṇ (ண), n (ந), m (ம) and ṉ (ன) are followed by their corresponding voiceless consonants. "
            }
          },
          {
            "paadal": "அவற்றுள், \nண னஃகான் முன்னர் \nக ச ஞ ப ம ய வ ஏழும் உரிய. ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "K (க), c (ச), ṉ (ண), p (ப), m (ம), y (ய)and v (வ) also can follow ṇ (ண) and ṉ (ன). "
            }
          },
          {
            "paadal": "ஞ ந ம வ என்னும் புள்ளி முன்னர் \nயஃகான் நிற்றல் மெய் பெற்றன்றே. ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "Y (ய) also may follow ñ (ஞ), n (ந), m (ம) and v (வ). "
            }
          },
          {
            "paadal": "மஃகான் புள்ளி முன் வவ்வும் தோன்றும்.",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "V (வ) also can follow m (ம)."
            }
          },
          {
            "paadal": "ய ர ழ என்னும் புள்ளி முன்னர் \nமுதல் ஆகு எழுத்து ஙகரமொடு தோன்றும்.",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "Y (ய), r (ர) and ḻ (ழ) can be followed by those consonants which can stand as the initial member of a word (*.£.) k (க), t (த்), n (ந), p (ப), m (ம), c (ச), v (வ), ñ (ஞ), y (ய) and ṅ (ங)."
            }
          },
          {
            "paadal": "மெய்ந் நிலை சுட்டின் எல்லா எழுத்தும்\n தம் முன் தாம் வரூஉம் ர ழ அலங்கடையே. ",
            "vilakkam": 
            {
              "paadal_category":"Consonantal Clustering",
              "paadal_meaning": "All consonants except r (ர) and ḻ (ழ) can be followed by the same consonant."
            }
          },
          {
            "paadal": "அ இ உ அம் மூன்றும் சுட்டு. ",
            "vilakkam": 
            {
              "paadal_category":"Demonstratives",
              "paadal_meaning": "Demonstratives are the three (sounds) a (ழ), i(இ) and u (உ)."
            }
          },
          {
            "paadal": "ஆ ஏ ஓ அம் மூன்றும் வினா.",
            "vilakkam": 
            {
              "paadal_category":"Interrogatives",
              "paadal_meaning": "Interrogates are the three (sounds) ā (ஆ), ē (ஏ), ō (ஓ)."
            }
          },
          {
            "paadal": "அளபு இறந்து உயிர்த்தலும் ஒற்று இசை நீடலும்\n உள என மொழிப இசையொடு சிவணிய\n நரம்பின் மறைய என்மனார் புலவர். ",
            "vilakkam": 
            {
              "paadal_category":"Lengthening of Phonemes",
              "paadal_meaning": "Learned men say that the words and consonants have their quantity increased in music, vocal and instrumental."
            }
          }
        ]
      },
      {
        "iyal_name": "மொழிமரபு",
        "iyal_eng":"Morphophonemics",
        "noorpa": [
          {
            "paadal": "குற்றியலிகரம் நிற்றல் வேண்டும்\n யா என் சினைமிசை உரையசைக் கிளவிக்கு\n ஆவயின் வரூஉம் மகரம் ஊர்ந்தே. ",
            "vilakkam": 
            {
                "paadal_category": "Secondary Phonemes: Shortened i (இ)",
                "paadal_meaning": "i (இ)  stands after m (ம) and before yā (யா) in the iṭaiccol miyā (சினைமிசை) used with a verb when a person is addressed."
            }
          },
          {
            "paadal": "புணரியல் நிலையிடைக் குறுகலும் உரித்தே\n உணரக் கூறின் முன்னர்த் தோன்றும். ",
            "vilakkam": 
            {
                "paadal_category": "Secondary Phonemes: Shortened i (இ)",
                "paadal_meaning": "i (இ) may also stand as the final member of the first of two, words in sandhi; more about it is dealt with later on (i.c.) in Kuṟṟiyalukarappuṇariyal (குறுகலும் உரித்தே புணரியல்)."
            }
          },
          {
            "paadal": "நெட்டெழுத்து இம்பரும் தொடர்மொழி ஈற்றும்\n குற்றியலுகரம் வல் ஆறு ஊர்ந்தே. ",
            "vilakkam":
            {
                "paadal_category": "Secondary phonemes: Shortened u (உ)",
                "paadal_meaning": "u (உ) appears as the final member after a hard consonant in words having a long vowel before it (like nāku (நாகு)) or in toṭarmoḻi (தொடர்மொழி), (like teṅku (தெங்கு), varaku (வரகு), etc )."
            }
          },
          {
            "paadal": "இடைப்படின் குறுகும் இடனுமார் உண்டே\n கடப்பாடு அறிந்த புணரியலான.",
            "vilakkam": 
            {
                "paadal_category": "Secondary phonemes: Shortened u (உ)",
                "paadal_meaning": "U (உ) is further shortened in sandhi and it is dealt with in Kuṟṟiyalukarappunariyal (குறுகலும் உரித்தே புணரியல்))."
            }
          },
          {
            "paadal": "குறியதன் முன்னர் ஆய்தப் புள்ளி\n உயிரொடு புணர்ந்த வல் ஆறன் மிசைத்தே. ",
            "vilakkam": 
            {
                "paadal_category": "Secondary phonemes: Āytam ḵ(ஃ)",
                "paadal_meaning": "ḵ (ஃ) is always preceded by a short vowel and followed by a hard consonant."
            }
          },
          {
            "paadal": "ஈறு இயல் மருங்கினும் இசைமை தோன்றும்.",
            "vilakkam": 
            {
                "paadal_category": "Secondary phonemes: Āytam (ஃ)",
                "paadal_meaning": "ḵ (ஃ) appears in sandhi even when the final member of the preceding word combines with the initial member of the succeeding word."
            }
          },
          {
            "paadal": "உருவினும் இசையினும் அருகித் தோன்றும் \nமொழிக் குறிப்பு எல்லாம் எழுத்தின் இயலா \nஆய்தம் அஃகாக் காலையான. ",
            "vilakkam":
            {
                "paadal_category": "Secondary phonemes: Āytam (ஃ)",
                "paadal_meaning": "ḵ (ஃ) is rarely used in words denoting color, and in onomatopoeic words with more than its usual quantity of half a mātrā (மாத்திரை)."
            }
          },
          {
            "paadal": "குன்று இசை மொழிவயின் நின்று இசை நிறைக்கும்\n நெட்டெழுத்து இம்பர் ஒத்த குற்றெழுத்தே.",
            "vilakkam": 
            {
                "paadal_category": "Euphonic Elongation",
                "paadal_meaning": "Whenever a vowel is so lengthened as to have three mātrās (மாத்திரை) or more, it is represented in script by the symbol for the long vowel followed by one or more symbols for the short vowel of the same class."
            }
          },
          {
            "paadal": "ஐ ஔ என்னும் ஆயீர் எழுத்திற்கு\n இகர உகரம் இசை நிறைவு ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Elongations of ai (ஐ) and au (ஔ)",
                "paadal_meaning": "When ai (ஐ) and au (ஔ) are lengthened in such a way as to have three mātrās (மாத்திரை), they are respectively represented in script by one or more symbols of i (இ) and u (உ) after those of ai (ஐ) and au (ஔ)."
            }
          },
          {
            "paadal": "நெட்டெழுத்து ஏழே ஓர் எழுத்து ஒருமொழி.",
            "vilakkam": 
            {
                "paadal_category": "One-letter Words",
                "paadal_meaning": "The seven long vowels alone can stand as single lettered words."
            }
          },
          {
            "paadal": "குற்றெழுத்து ஐந்தும் மொழி நிறைபு இலவே. ",
            "vilakkam":
            {
                "paadal_category": "One-letter Words",
                "paadal_meaning": "No one of the five short vowels can stand as a word by itself."
            }
          },
          {
            "paadal": "ஓர் எழுத்து ஒருமொழி ஈர் எழுத்து ஒருமொழி \nஇரண்டு இறந்து இசைக்கும் தொடர்மொழி உளப்பட \nமூன்றே மொழி நிலை தோன்றிய நெறியே.",
            "vilakkam": 
            {
                "paadal_category": "Morphosemantic Word-classes",
                "paadal_meaning": "From usage, words may be classified in three ways:—One- lettered word, two-lettered word and word having more than two letters."
            }
          },
          {
            "paadal": "மெய்யின் இயக்கம் அகரமொடு சிவணும்.",
            "vilakkam": 
            {
                "paadal_category": "Articulation of Consonants",
                "paadal_meaning": "The nature of consonants is that they are pronounced with a (to facilitate pronunciation). Refer to sutras 19, 20 and 21."
            }
          },
          {
            "paadal": "தம் இயல் கிளப்பின் எல்லா எழுத்தும் \nமெய்ந் நிலை மயக்கம் மானம் இல்லை.",
            "vilakkam": 
            {
                "paadal_category": "Clustering of Consonants",
                "paadal_meaning": "When a sound denotes itself, it is not a mistake if it does not follow the grammatical rules of assimilation."
            }
          },
          {
            "paadal": "ய ர ழ என்னும் மூன்றும் முன் ஒற்ற \nக ச த ப ங ஞ ந ம ஈர் ஒற்று ஆகும். ",
            "vilakkam": 
            {
                "paadal_category": "Clustering of Consonants",
                "paadal_meaning": "Y (ய), r (ர) and ḻ (ழ) may be followed by k (க), c (ச), t (த), p (ப), ṅ (ங), ñ (ஞ), n (ந) and m (ம)."
            }
          },
          {
            "paadal": "அவற்றுள், \nரகார ழகாரம் குற்றொற்று ஆகா.",
            "vilakkam": 
            {
                "paadal_category": "Clustering of Consonants",
                "paadal_meaning": "Of them r (ர) and ḻ (ழ) cannot be the final member of a word when preceded by a short vowel."
            }
          },
          {
            "paadal": "குறுமையும் நெடுமையும் அளவின் கோடலின் \nதொடர்மொழி எல்லாம் நெட்டெழுத்து இயல.",
            "vilakkam": 
            {
                "paadal_category": "Determination of Māthirai (மாத்திரை) in Words",
                "paadal_meaning": "R (ர) or ḻ (ழ) at the end of toṭarmoli (தொடர்மொழி) is considered in the same way as if it follows a long vowel irrespective of its being followed by short or long vowel."
            }
          },
          {
            "paadal": "செய்யுள் இறுதிப் போலும் மொழிவயின் \nனகார மகாரம் ஈர் ஒற்று ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Pōṉm (போன்ம்) in Compositions",
                "paadal_meaning": "In literary composition the word pōlum (போலும்) is changed to pōṉṁ (போன்ம்)."
            }
          },
          {
            "paadal": "னகாரை முன்னர் மகாரம் குறுகும்.",
            "vilakkam": 
            {
                "paadal_category": "Pōṉm (போன்ம்) in Compositions",
                "paadal_meaning": "M (ம) after ṉ (ன) in the above case is shortened (to quarter of a mātrā (மாத்திரை))."
            }
          },
          {
            "paadal": "மொழிப்படுத்து இசைப்பினும் தெரிந்து வேறு இசைப்பினும் \nஎழுத்து இயல் திரியா என்மனார் புலவர். ",
            "vilakkam": 
            {
                "paadal_category": "Unchanging Nature of Phonetic Quality",
                "paadal_meaning": "Learned men say that the nature or the quantity of a sound is not altered whether it conveys sense in a word, or is used simply for the sake of metre."
            }
          },
          {
            "paadal": "அகர இகரம் ஐகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Character of ai (ஐ)",
                "paadal_meaning": "A (அ) and i (இ) when pronounced together sound like ai (ஐ)."
            }
          },
          {
            "paadal": "அகர உகரம் ஔகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Constitution of au (ஔ)",
                "paadal_meaning": "A (அ) and i (உ) when pronounced together sound like au (ஔ)."
            }
          },
          {
            "paadal": "அகரத்து இம்பர் யகரப் புள்ளியும் \nஐ என் நெடுஞ் சினை மெய் பெறத் தோன்றும்.",
            "vilakkam": 
            {
                "paadal_category": "Phonetic Variant of ai (ஐ)",
                "paadal_meaning": "A (அ) and y (ய) also when pronounced together sound like ai (ஐ)."
            }
          },
          {
            "paadal": "ஓர் அளபு ஆகும் இடனுமார் உண்டே \nதேரும் காலை மொழிவயினான. ",
            "vilakkam": 
            {
                "paadal_category": "Reduced Articulatory Measure of ai (ஐ) and au (ஔ)",
                "paadal_meaning": "In certain positions in words the above-mentioned 'ai (ஐ)' has only one mātrā (மாத்திரை)."
            }
          },
          {
            "paadal": "இகர யகரம் இறுதி விரவும்.",
            "vilakkam": 
            {
                "paadal_category": "Alternation of ai (ஐ) and y (ய்)",
                "paadal_meaning": "The symbol i (இ) is sometimes used for y (ய) at the end of words."
            }
          },
          {
            "paadal": "பன்னீர் உயிரும் மொழி முதல் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "All the twelve vowels can each stand as the initial member of a word."
            }
          },
          {
            "paadal": "உயிர் மெய் அல்லன மொழி முதல் ஆகா.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "Any consonant, unless it is followed by a vowel, cannot stand as the initial member of a word."
            }
          },
          {
            "paadal": "க த ந ப ம எனும் ஆவைந்து எழுத்தும் \nஎல்லா உயிரொடும் செல்லுமார் முதலே.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "K (க), t (த), n (ந), p (ப) and m (ம) can be followed by any vowel when they stand initially."
            }
          },
          {
            "paadal": "சகரக் கிளவியும் அவற்று ஓரற்றே \nஅ ஐ ஔ எனும் மூன்று அலங்கடையே.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "C (ச) can similarly stand initially except when it is followed by a (அ), ai (ஐ) and au (ஔ)."
            }
          },
          {
            "paadal": "உ ஊ ஒ ஓ என்னும் நான்கு உயிர் \nவ என் எழுத்தொடு வருதல் இல்லை.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "V is not followed by u (உ), ū (ஊ), o (ஒ) and ō (ஓ) when it stands initially."
            }
          },
          {
            "paadal": "ஆ எ ஒ எனும் மூ உயிர் ஞகாரத்து உரிய.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "ñ (ஞ) is followed only by ā (ஆ), e (எ) or o (ஒ) when it stands initially."
            }
          },
          {
            "paadal": "ஆவொடு அல்லது யகரம் முதலாது.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "Y (ய) does not stand initially unless it is followed by ā (ஆ)."
            }
          },
          {
            "paadal": "முதலா ஏன தம் பெயர் முதலும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "All consonants can stand initially whatever be the vowels that follow them when the}' denote themselves."

            }
          },
          {
            "paadal": "குற்றியலுகரம் முறைப்பெயர் மருங்கின் \nஒற்றிய நகரமிசை நகரமொடு முதலும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "U (உ) follows the initial n of personal pronouns followed by words denoting relationship."
            }
          },
          {
            "paadal": "முற்றியலுகரமொடு பொருள் வேறுபடாஅது \nஅப் பெயர் மருங்கின் நிலையியலான.",
            "vilakkam": 
            {
                "paadal_category": "Word-initials",
                "paadal_meaning": "U (உ) in words like nuntai serves the same purpose as u without altering the meaning as it does elsewhere."
            }
          },
          {
            "paadal": "உயிர் ஔ எஞ்சிய இறுதி ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "All vowels except au (ஔ) can each stand as the final member of a word."
            }
          },
          {
            "paadal": "க வவொடு இயையின் ஔவும் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "(But) even au can stand finally if it is preceded by k (க) or v (வ)."
            }
          },
          {
            "paadal": "எ என வரும் உயிர் மெய் ஈறாகாது.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "E (எ) cannot stand finally if it is preceded by a consonant."
            }
          },
          {
            "paadal": "ஒவ்வும் அற்றே ந அலங்கடையே.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "O (ஒ) too cannot similarly stand finally if it is preceded by any consonant except n (ந)."
            }
          },
          {
            "paadal": "ஏ ஒ எனும் உயிர் ஞகாரத்து இல்லை.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "ē (ஏ) or ō (ஒ) cannot stand finally if it is preceded by ñ (ஞ)."
            }
          },
          {
            "paadal": "உ ஊகாரம் ந வவொடு நவிலா.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "U (உ) and ū (ஊ) cannot stand finally if each is preceded by n (ந) and v (வ)."
            }
          },
          {
            "paadal": "உச் சகாரம் இரு மொழிக்கு உரித்தே.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "U (உ) preceded by c (ச) stands finally only in two words. Ucu (சு), mucu ()."
            }
          },
          {
            "paadal": "உப் பகாரம் ஒன்று என மொழிப \nஇரு வயின் நிலையும் பொருட்டு ஆகும்மே.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "U (உ) preceded by p occurs only in one word; it gives active sense or causal sense according to the way in which it is pronounced."
            }
          },
          {
            "paadal": "எஞ்சிய எல்லாம் எஞ்சுதல் இலவே.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "There is no objection to use the vowel-consonants that cannot stand as final members of words, as final members if they denote themselves."
            }
          },
          {
            "paadal": "ஞ ண ந ம ன ய ர ல வ ழ ள என்னும் \nஅப் பதினொன்றே புள்ளி இறுதி.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "Only the eleven consonants ñ (ஞ), ṇ (ண), n (ந), m (ம), ṉ (ன), y (ய), r (ர), l (ல), v (வ), ḻ (ழ) and ḷ (ள) can stand finally."
            }
          },
          {
            "paadal": "உச் சகாரமொடு நகாரம் சிவணும்.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "N (ந) can stand finally only in two words as u (உ) preceded by c (ச). "
            }
          },
          {
            "paadal": "உப் பகாரமொடு ஞகாரையும் அற்றே \nஅப் பொருள் இரட்டாது இவணையான.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "ñ (ஞ) can stand finally only in one word as u (உ) preceded by p (ப), but, unlike it, it has only one meaning."
            }
          },
          {
            "paadal": "வகரக் கிளவி நான் மொழி ஈற்றது.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "V (வ) can stand finally only in four words."
            }
          },
          {
            "paadal": "மகரத் தொடர்மொழி மயங்குதல் வரைந்த \nனகரத் தொடர்மொழி ஒன்பஃது என்ப \nபுகர் அறக் கிளந்த அஃறிணை மேன.",
            "vilakkam": 
            {
                "paadal_category": "Word-finals",
                "paadal_meaning": "It is said that there are nine words of neuter gender in which ṉ (ன) stands finally without having the chance of being substituted by m (ம)."
            }
          }
        ]
      },
      {
        "iyal_name": "பிறப்பியல்",
        "iyal_eng":"Production of speech sounds",
        "noorpa": [
          {
            "paadal": "உந்தி முதலா முந்து வளி தோன்றி \nதலையினும் மிடற்றினும் நெஞ்சினும் நிலைஇ \nபல்லும் இதழும் நாவும் மூக்கும் \nஅண்ணமும் உளப்பட எண் முறை நிலையான் \nஉறுப்பு உற்று அமைய நெறிப்பட நாடி \nஎல்லா எழுத்தும் சொல்லும் காலை \nபிறப்பின் ஆக்கம் வேறு வேறு இயல \nதிறப்படத் தெரியும் காட்சியான.",
            "vilakkam":
            {
              "paadal_category":"Air-Stream Mechanism",  
              "paadal_meaning":" It will be evident on careful observation that all the sounds (in Tamil language) are but the results of the modifications which the air undergoes in starting from navel and passing through the eight parts chest, neck, head, tongue, hard palate, teeth, lips and nose."
            }
          },
          {
            "paadal": "அவ் வழி, \nபன்னீர் உயிரும் தம் நிலை திரியா \nமிடற்றுப் பிறந்த வளியின் இசைக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Vowels",  
              "paadal_meaning":" All the twelve vowels are produced by the air starting from navel and passing through the neck without undergoing any modification."
            }
          },
          {
            "paadal": "அவற்றுள், \nஅ ஆ ஆயிரண்டு அங்காந்து இயலும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Vowels",  
              "paadal_meaning":"of them a (அ) and ā (ஆ) are produced by opening the mouth (i.e.) a(அ) and ā(ஆ) are open sounds."
            }
          },
          {
            "paadal": "இ ஈ எ ஏ ஐ என இசைக்கும் \nஅப் பால் ஐந்தும் அவற்று ஓரன்ன \nஅவைதாம், \nஅண்பல் முதல் நா விளிம்பு உறல் உடைய.",
            "vilakkam":
            {
              "paadal_category":"Production of Vowels",  
              "paadal_meaning":" The five sounds i (இ) , ī (ஈ) , e (எ) , ē (ஏ) and ai (ஐ)  are similarly open sounds and are produced by the tip of the tongue approaching the upper gums."
            }
          },
          {
            "paadal": "உ ஊ ஒ ஓ ஔ என இசைக்கும்\n அப் பால் ஐந்தும் இதழ் குவிந்து இயலும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Vowels",  
              "paadal_meaning":"u (உ) ,ū (ஊ) ,o (ஒ) , ō (ஓ) and au (ஔ) (being similarly open) are produced by rounding the lips."
            }
          },
          {
            "paadal": "தம்தம் திரிபே சிறிய என்ப.",
            "vilakkam":
            {
              "paadal_category":"Production of Vowels",  
              "paadal_meaning":"It is said that the difference among themselves [(i.e.) the sounds having the same organ of articulation] is slight."
            }
          },
          {
            "paadal": "ககார ஙகாரம் முதல் நா அண்ணம்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"K (க) and ṅ (ங)  are produced by the contact of the root of the tongue with the root of the hard palate."
            }
          },
          {
            "paadal": "சகார ஞகாரம் இடை நா அண்ணம்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"C (ச) and ñ (ஞ) are produced by the contact of the middle of the tongue with the middle of the hard palate."
            }
          },
          {
            "paadal": "டகார ணகாரம் நுனி நா அண்ணம்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"ṭ (ட)  and ṇ (ண)  are produced by the contact of the tip of the tongue with the front of the hard palate."
            }
          },
          {
            "paadal": "அவ் ஆறு எழுத்தும் மூ வகைப் பிறப்பின.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"Hence the above-mentioned six sounds have three different organs of articulation."
            }
          },
          {
            "paadal": "அண்ணம் நண்ணிய பல் முதல் மருங்கில்\n நா நுனி பரந்து மெய் உற ஒற்ற \nதாம் இனிது பிறக்கும் தகார நகாரம்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"T (தா)  and n (நா)  are produced by the extended tip of the tongue completely touching the upper gums."
            }
          },
          {
            "paadal": "அணரி நுனி நா அண்ணம் ஒற்ற \nறஃகான் னஃகான் ஆயிரண்டும் பிறக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"ṟ (ற) and ṉ (ன) are produced by the tip of the tongue-feeing raised and allowed to gently touch the hard palate."
            }
          },
          {
            "paadal": "நுனி நா அணரி அண்ணம் வருட \nரகார ழகாரம் ஆயிரண்டும் பிறக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":" r (ர) and ḻ (ழ) are produced by the tip of the tongue being raised and allowed to gently rub against the hard palate."
            }
          },
          {
            "paadal": "நா விளிம்பு வீங்கி அண்பல் முதல் உற ஆவயின் அண்ணம் ஒற்றவும் வருடவும் லகார ளகாரம் ஆயிரண்டும் பிறக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"l (ல)  and ḷ (ள) are produced by the extended tip of the tongue respectively touching the upper gums and rubbing against them."
            }
          },
          {
            "paadal": "இதழ் இயைந்து பிறக்கும் பகார மகாரம்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"p (ப) and m (ம) are produced by the contact of the lips."
            }
          },
          {
            "paadal": "பல் இதழ் இயைய வகாரம் பிறக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"v (வ) is produced by the contact of the (upper) row of teeth and the (lower) lip."
            }
          },
          {
            "paadal": "அண்ணம் சேர்ந்த மிடற்று எழு வளி இசை கண்ணுற்று அடைய யகாரம் பிறக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Consonants",  
              "paadal_meaning":"Y (ய) is produced by allowing the air which passes through the neck to pass very close to the hard palate."
            }
          },
          {
            "paadal": "மெல்லெழுத்து ஆறும் பிறப்பின் ஆக்கம் சொல்லிய பள்ளி நிலையின ஆயினும் மூக்கின் வளி இசை யாப்புறத் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"Nasalized Consonants",  
              "paadal_meaning":"The six melleḻuttu noted above (i.e.)  ṅ (ங)  , ñ (ஞ) , ṇ (ண) , n(ந) , m (ம) and ṉ (ன் have the nose as an additional organ of articulation."
            }
          },
          {
            "paadal": "சார்ந்து வரின் அல்லது தமக்கு இயல்பு இல எனத் தேர்ந்து வெளிப்படுத்த ஏனை மூன்றும் தம்தம் சார்பின் பிறப்பொடு சிவணி ஒத்த காட்சியின் தம் இயல்பு இயலும்.",
            "vilakkam":
            {
              "paadal_category":"Production of Secondary Phonemes",  
              "paadal_meaning":"The three secondary sounds (i.e.) ī (ஈ)  , ū (ஊ)  and ḵ (ஃ)  have the same organ of articulation as the consonant which stands as their support (i. e.) the consonant which precedes them in the case of ī (ஈ) and ū (ஊ) and that which succeeds it in the case of ayutha eluthu ḵ (ஃ) ."
            }
          },
          {
            "paadal": "எல்லா எழுத்தும் வெளிப்படக் கிளந்து சொல்லிய பள்ளி எழுதரு வளியின் பிறப்பொடு விடுவழி உறழ்ச்சி வாரத்து அகத்து எழு வளி இசை அரில் தப நாடி அளபின் கோடல் அந்தணர் மறைத்தே.",
            "vilakkam":
            {
              "paadal_category":"Articulatory Phonetics : Sanskrit and Tamil Models",  
              "paadal_meaning":"The nature of the origin of the air which starts from navel and the modifications which it undergoes before it comes out as an articulated sound and of its quantity therein is clearly discussed in the scriptures of Brahmans."
            }
          },
          {
            "paadal": "அஃது இவண் நுவலாது எழுந்து புறத்து இசைக்கும் மெய் தெரி வளி இசை அளபு நுவன்றிசினே.",
            "vilakkam":
            {
              "paadal_category":"Articulatory Phonetics : Sanskrit and Tamil Models",  
              "paadal_meaning":"I have here mentioned only about the quantity of the articulated sounds without mentioning anything about what is mentioned in detail in the scriptures of Brahmans."
            }
          }
        ]
      },
      {
        "iyal_name": "புணரியல்",
        "iyal_eng":"Morphophonemic Coalescence",
        "noorpa": [
          {
            "paadal": "மூன்று தலை இட்ட முப்பதிற்று எழுத்தின்  இரண்டு தலை இட்ட முதல் ஆகு இருபஃது  அறு நான்கு ஈறொடு நெறி நின்று இயலும்  எல்லா மொழிக்கும் இறுதியும் முதலும்  மெய்யே உயிர் என்று ஆயீர் இயல. ",
            "vilakkam":
            {
              "paadal_category":"Word initials and word finals in coalescence",  
              "paadal_meaning":"Of the thirty three sounds consisting of vowels and consonants, twenty-two can stand as the initial member of words and twenty-four as the final member."
            }
          },
          {
            "paadal": "அவற்றுள்,  மெய் ஈறு எல்லாம் புள்ளியொடு-நிலையல்.",
            "vilakkam":
            {
              "paadal_category":"Word initials and word finals in coalescence",  
              "paadal_meaning":"Of them, the final consonants are each provided with a dot"
            }
          },
          {
            "paadal": "குற்றியலுகரமும் அற்று என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"Word initials and word finals in coalescence",  
              "paadal_meaning":"The same is the case with Kuṟṟiyalukaram (குற்றியலுகரம்)."
            }
          },
          {
            "paadal": "உயிர்மெய் ஈறும் உயிர் ஈற்று இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"Word initials and word finals in coalescence",  
              "paadal_meaning":"The final vowel-consonant is of the same nature as the final vowel."
            }
          },
          {
            "paadal": "உயிர் இறு சொல் முன் உயிர் வரு வழியும்  உயிர் இறு சொல் முன் மெய் வரு வழியும்  மெய் இறு சொல் முன் உயிர் வரு வழியும்  மெய் இறு சொல் முன் மெய் வரு வழியும் என்று  இவ் என அறியக் கிளக்கும் காலை  நிறுத்த சொல்லே குறித்து வரு கிளவி என்று  ஆயீர் இயல புணர் நிலைச் சுட்டே. ",
            "vilakkam":
            {
              "paadal_category":"Word initials and word finals in coalescence",  
              "paadal_meaning":"Canti (சந்தி) takes place between the final member of a word and the initial member of the succeeding word and it is classified under four heads :—Vowel following a vowel, consonant following a vowel, vowel following a consonant and consonant following a consonant."
            }
          },
          {
            "paadal": "அவற்றுள்,  நிறுத்த சொல்லின் ஈறு ஆகு எழுத்தொடு  குறித்து வரு கிளவி முதல் எழுத்து இயைய  பெயரொடு பெயரைப் புணர்க்குங் காலும்  பெயரொடு தொழிலைப் புணர்க்குங் காலும்  தொழிலொடு பெயரைப் புணர்க்குங் காலும்  தொழிலொடு தொழிலைப் புணர்க்குங் காலும்  மூன்றே திரிபு இடன் ஒன்றே இயல்பு என  ஆங்கு அந் நான்கே மொழி புணர் இயல்பே.",
            "vilakkam":
            {
              "paadal_category":"Word classes of the preceding and succeeding words",  
              "paadal_meaning":"When Canti (சந்தி)takes place between the final member of the standing word and the initial member of the succeeding word, both the standing word and the succeeding word or either of them may be nouns and verbs ; there are four cases of Canti (சந்தி) in three of which change takes place and there is no change in the fourth."
            }
          },
          {
            "paadal": "அவைதாம்,  மெய் பிறிது ஆதல் மிகுதல் குன்றல் என்று  இவ் என மொழிப திரியும் ஆறே.",
            "vilakkam":
            {
              "paadal_category":"Modes of change in coalescence",  
              "paadal_meaning":"They (i,e Canti (சந்தி)) with change are assimilation, insertion and elision."
            }
          },
          {
            "paadal": "நிறுத்த சொல்லும் குறித்து வரு கிளவியும்  அடையொடு தோன்றினும் புணர் நிலைக்கு உரிய.",
            "vilakkam":
            {
              "paadal_category":"Preceding and following words with modifiers",  
              "paadal_meaning":"Canti (சந்தி) (in Tamil language) admits the insertion of a particle between the final letter of the standing word and the initial letter of the succeeding word."
            }
          },
          {
            "paadal": "மருவின் தொகுதி மயங்கியல் மொழியும்  உரியவை உளவே புணர் நிலைச் சுட்டே.",
            "vilakkam":
            {
              "paadal_category":"Preceding and following words with modifiers",  
              "paadal_meaning":"In Canti (சந்தி) the order of certain maruvu (மருவு) or colloquial words is sometimes inverted. "
            }
          },
          {
            "paadal": "வேற்றுமை குறித்த புணர்மொழி நிலையும்  வேற்றுமை அல்வழிப் புணர்மொழி நிலையும்  எழுத்தே சாரியை ஆயிரு பண்பின்  ஒழுக்கல் வலிய புணரும் காலை. ",
            "vilakkam":
            {
              "paadal_category":"Augmentation and empty morphemes in coalescence",  
              "paadal_meaning":"Canti (சந்தி) may take place both when the standing word and the succeeding word stand in case-relation to each other and when they are not in case-relation to each other. In Canti (சந்தி) either letter or Kāriyai (காரியை) (flexional increment) may be inserted between the two words."
            }
          },
          {
            "paadal": "ஐ ஒடு கு இன் அது கண் என்னும்  அவ் ஆறு என்ப வேற்றுமை உருபே.",
            "vilakkam":
            {
              "paadal_category":"Case morphemes in coalescence",  
              "paadal_meaning":"Case suffixes are six in number viz. ai(ஐ), otu(ஒடு), ku(கு), iṉ(இன்), atu(அது), and kaṇ (கண்)."
            }
          },
          {
            "paadal": "வல்லெழுத்து முதலிய வேற்றுமை உருபிற்கு  ஒல்வழி ஒற்று இடை மிகுதல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"Case morphemes in coalescence",  
              "paadal_meaning":"A voiceless consonant or a nasal must be inserted between the base and the case-suffix that commences with a voiceless consonant (i e.) Ku (கு), of the fourth case and Kan of the seventh case."
            }
          },
          {
            "paadal": "ஆறன் உருபின் அகரக் கிளவி  ஈறு ஆகு அகர முனைக் கெடுதல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"Case morphemes in coalescence",  
              "paadal_meaning":"The a(அ) of atu(அது),, the sixth case suffix, is dropped if the base ends in a(அ). "
            }
          },
          {
            "paadal": "வேற்றுமை வழிய பெயர் புணர் நிலையே.",
            "vilakkam":
            {
              "paadal_category":"Case morphemes in coalescence",  
              "paadal_meaning":"Case-suffix is suffixed to the base."
            }
          },
          {
            "paadal": "உயர்திணைப் பெயரே அஃறிணைப் பெயர் என்று  ஆயிரண்டு என்ப பெயர் நிலைச் சுட்டே.",
            "vilakkam":
            {
              "paadal_category":"Case morphemes in coalescence",  
              "paadal_meaning":"Nouns denoting objects are of two kinds :—Uyartinai(உயர்திணை) and Akkiriṉai (அஃறிணை)."
            }
          },
          {
            "paadal": "அவற்று வழி மருங்கின் சாரியை வருமே.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"Flexional increment or Kāriyai (காரியை)  is suffixed to them [(i.e) the above-mentioned nouns]."
            }
          },
          {
            "paadal": "அவைதாம்,  இன்னே வற்றே அத்தே அம்மே  ஒன்னே ஆனே அக்கே இக்கே  அன் என் கிளவி உளப்பட பிறவும்  அன்ன என்ப சாரியை மொழியே.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"The flexional increments are in, Vaṟṟu(வற்று), attu(அத்து), am(அம்), Oṉ (ஒன்), an(அன்), akku(அக்கு). Ikku(இக்கு). Aṉ(அன்) etc."
            }
          },
          {
            "paadal": "அவற்றுள்,  இன்னின் இகரம் ஆவின் இறுதி  முன்னர்க் கெடுதல் உரித்தும் ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"I (ஐ)of in is optionally dropped after the final ā (ஆ)of the base or standing word."
            }
          },
          {
            "paadal": "அளபு ஆகு மொழி முதல் நிலைஇய உயிர்மிசை  னஃகான் றஃகான் ஆகிய நிலைத்தே.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"N(ன்) of iṉ is changed to r before words denoting measure. "
            }
          },
          {
            "paadal": "வஃகான் மெய் கெட சுட்டு முதல் ஐம் முன்  அஃகான் நிற்றல் ஆகிய பண்பே.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"V (வ) of, Vaṟṟu (வற்று) is dropped after the words beginning with the demonstrative root (a(அ), i(ஐ), u(உ)) and ending in ai(ஐ),"
            }
          },
          {
            "paadal": "னஃகான் றஃகான் நான்கன் உருபிற்கு.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"ṉ(ன்) of iṉ(இன்), on(ஒன்), an(அன்),  and an(அன்),  is changed to ṟ(ற்) before ku(கு),, the fourth case suffix,"
            }
          },
          {
            "paadal": "ஆனின் னகரமும் அதன் ஓரற்றே",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"ṉ(ன்) of aṉ (அன்) is similarly changed to ṟ(ற்) when it comes between a noun denoting a star and a verb beginning with a voiceless consonant"
            }
          },
          {
            "paadal": "அத்தின் அகரம் அகர முனை இல்லை.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"A(அ) of attu (அத்து) is dropped after words ending in a(அ)"
            }
          },
          {
            "paadal": "இக்கின் இகரம் இகர முனை அற்றே.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"I(ஐ) of ikku(இக்கு) is dropped if the base or the standing word ends in i(ஐ)."
            }
          },
          {
            "paadal": "ஐயின் முன்னரும் அவ் இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"I(ஐ) of ikku(இக்கு).  is dropped even if the base or the standing word ends in ai(ஐ)."
            }
          },
          {
            "paadal": "எப் பெயர் முன்னரும் வல்லெழுத்து வரு வழி  அக்கின் இறுதி மெய்ம் மிசையொடும் கெடுமே  குற்றியலுகரம் முற்றத் தோன்றாது.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"Kku(க்கு) of akku(அக்கு).  is dropped when the latter is inserted between any noun and a word beginning with a voiceless consonant."
            }
          },
          {
            "paadal": "அம்மின் இறுதி க ச தக் காலை  தன் மெய் திரிந்து ங ஞ ந ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"M (ம்)of am(அம்) is changed to ṅ(ங), Ñ(ஞ) and n(ந) when it is followed by k(க), c(ச) and t(த) respectively."
            }
          },
          {
            "paadal": "மென்மையும் இடைமையும் வரூஉம் காலை  இன்மை வேண்டும் என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"Learned men say that m(ம்) of am(அம்) is dropped when it is followed by a nasal or a semivowel"
            }
          },
          {
            "paadal": "இன் என வரூஉம் வேற்றுமை உருபிற்கு  இன் என் சாரியை இன்மை வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"Empty morphemes in  coalescence",  
              "paadal_meaning":"The flexional increment in is dropped before the case suffix in."
            }
          },
          {
            "paadal": "பெயரும் தொழிலும் பிரிந்து ஒருங்கு இசைப்ப  வேற்றுமை உருபு நிலைபெறு வழியும்  தோற்றம் வேண்டாத் தொகுதிக்கண்ணும்  ஒட்டுதற்கு ஒழுகிய வழக்கொடு சிவணி  சொற் சிதர் மருங்கின் வழி வந்து விளங்காது  இடை நின்று இயலும் சாரியை இயற்கை  உடைமையும் இன்மையும் ஒடுவயின் ஒக்கும்.",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"When a noun is followed by a verb or a verbal noun, flexional increment is inserted, in Canti (சந்தி), according to usage between the base of the noun and the case suffix or after the base if the case suffix is dropped, though when the two words (noun and verb or noun and verbal noun) are separately read, the flexional increment disappears. Between the base and the case suffix Ōṭu(ஒடு) it (flexional increment) both appears and disappears."
            }
          },
          {
            "paadal": "அத்தே வற்றே ஆயிரு மொழிமேல்  ஒற்று மெய் கெடுதல் தெற்றென்றற்றே  அவற்று முன் வரூஉம் வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"The consonant that precedes the flexional increments attu(அத்து), and Vaṟṟu (வற்று) is dropped, while that which follows them is doubled."
            }
          },
          {
            "paadal": "காரமும் கரமும் கானொடு சிவணி  நேரத் தோன்றும் எழுத்தின் சாரியை. ",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"Kāram(காரம்), karam (கரம்)and Kāṉ (கான்) are the flexional increments used when naming a letter."
            }
          },
          {
            "paadal": "அவற்றுள்,  கரமும் கானும் நெட்டெழுத்து இலவே.",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"Of them karam (கரம் and Kāṉ (கான்) are not used along with long vowels."
            }
          },
          {
            "paadal": "வரன்முறை மூன்றும் குற்றெழுத்து உடைய.",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"All the above three are used along with short vowels."
            }
          },
          {
            "paadal": "ஐகார ஔகாரம் கானொடும் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"Functional characteristics of empty morphemes",  
              "paadal_meaning":"But Kāṉ (கான்)  also is used along with ai (ஐ)and au(ஔ)."
            }
          },
          {
            "paadal": "புள்ளி ஈற்று முன் உயிர் தனித்து இயலாது  மெய்யொடும் சிவணும் அவ் இயல் கெடுத்தே.",
            "vilakkam":
            {
              "paadal_category":"Pairing of consonant vowel in coalescence",  
              "paadal_meaning":"Vowel following a consonant cannot stand by itself, but mingles itself with the preceding consonant."
            }
          },
          {
            "paadal": "மெய் உயிர் நீங்கின் தன் உரு ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"Pairing of consonant vowel in coalescence",  
              "paadal_meaning":"The consonant takes its original form when it is separated from the vowel which follows it."
            }
          },
          {
            "paadal": "எல்லா மொழிக்கும் உயிர் வரு வழியே  உடம்படுமெய்யின் உருபு கொளல் வரையார்.",
            "vilakkam":
            {
              "paadal_category":"Vowels as word finals and word initials",  
              "paadal_meaning":"It is not prohibited to write a suitable consonant between words of which the preceding one ends in a vowel and the succeeding one begins in a vowel."
            }
          },
          {
            "paadal": "எழுத்து ஓரன்ன பொருள் தெரி புணர்ச்சி  இசையின் திரிதல் நிலைஇய பண்பே.",
            "vilakkam":
            {
              "paadal_category":"Vowels as word finals and word initials",  
              "paadal_meaning":"Words though similar in form take different kinds of Canti (சந்தி) according to the way in which they are pronounced. Words though similar in form take different kinds of Canti (சந்தி) according to the way in which they are pronounced."
            }
          },
          {
            "paadal": "அவைதாம்,  முன்னப் பொருள புணர்ச்சிவாயின்  இன்ன என்னும் எழுத்துக் கடன் இலவே.",
            "vilakkam":
            {
              "paadal_category":"Vowels as word finals and word initials",  
              "paadal_meaning":"Since the meaning of such words is determined from the context, they are not bound to a particular rule of Canti (சந்தி)."
            }
          }
        ]
      },
      {
        "iyal_name": "தொகைமரபு",
        "iyal_eng":"Coalescence and Compounding",
        "noorpa": [
          {
            "paadal": "க ச த ப முதலிய மொழிமேல் தோன்றும்  மெல்லெழுத்து இயற்கை சொல்லிய முறையான்  ங ஞ ந ம என்னும் ஒற்று ஆகும்மே  அன்ன மரபின் மொழிவயினான.",
            "vilakkam": 
            {
              "paadal_category":" ṅ(ங), ñ(ஞ), ṇ(ண) and m(ம) before k(க), c(ச), ṭ(ட) and p(ப)",  
              "paadal_meaning":" The nasal sound that can appear before k(க), c(ச), ṭ(ட) and p(ப) is respectively ṅ(ங), ñ(ஞ), ṇ(ண) and m(ம)."
            }
          },
          {
            "paadal": "ஞ ந ம ய வ எனும் முதல் ஆகு மொழியும்  உயிர் முதல் ஆகிய மொழியும் உளப்பட  அன்றி அனைத்தும் எல்லா வழியும்  நின்ற சொல் முன் இயல்பு ஆகும்மே.",
            "vilakkam":
            {
              "paadal_meaning":"When the initial member of the succeeding word is ñ(ஞ), n(ந), m(ம), y(ய), v(வ) or any vowel, no change takes place in sandhi whatever be the final member of the standing word."
            }
          },
          {
            "paadal": "அவற்றுள்,  மெல்லெழுத்து இயற்கை உறழினும் வரையார்  சொல்லிய தொடர்மொழி இறுதியான.",
            "vilakkam":
            {
              "paadal_category":"Optional Changes before ñ(ஞ),n(ந),m(ம)",  
              "paadal_meaning":"None prevents the optional insertion of a nasal after the final member of a toṭar moḻi (தொடர் மொழி) and before the letters mentioned in the previous sūtra."
            }
          },
          {
            "paadal": "ண ன என் புள்ளி முன் யாவும் ஞாவும்  வினை ஓரனைய என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"Interchangeability of y(ய) and ñ(ஞ)",  
              "paadal_meaning":"Learned men say that if y(ய)  is the initial member of a verb and if it stands after a word which ends in ṇ(ண) or ṉ(ன), ñ(ஞ) is optionally substituted for it."
            }
          },
          {
            "paadal": " மொழி முதல் ஆகும் எல்லா எழுத்தும்  வரு வழி நின்ற ஆயிரு புள்ளியும்  வேற்றுமை அல் வழித் திரிபு இடன் இலவே.",
            "vilakkam":
            {
              "paadal_category":"Non-change with ṇ(ண) and ṉ(ன)",  
              "paadal_meaning":"No change takes place if ṇ(ண) or ṉ(ன) is the final member of a word and it is followed by another which does not stand in case relation to it."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் வல்லெழுத்து அல் வழி  மேற் கூறு இயற்கை ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"Non-change with ṇ(ண) and ṉ(ன)",  
              "paadal_meaning":"Similar is the case even when the succeeding word stands in case-relation to the standing word if the former does not begin with a voiceless consonant."
            }
          },
          {
            "paadal": "ல ன என வரூஉம் புள்ளி முன்னர்  த ந என வரின் ற ன ஆகும்மே.",
            "vilakkam":
            {
              "paadal_category":"Change of t(த) and n(ந) into ṟ(ற) and ṉ(ன)",  
              "paadal_meaning":"If t(த) and n(ந) are the initial member of the succeeding word and l(ல) and ṉ(ன) are the final member of the standing word, the former are respectively changed to ṟ (ற) and ṉ (ன)."
            }
          },
          {
            "paadal": "ண ள என் புள்ளி முன் ட ண எனத் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"Change of t(த) and n(ந) into ṭ(ட்) and ṇ(ண) ",  
              "paadal_meaning":" The same t(த) and n(ந)  are changed to ṭ(ட) and ṇ(ங)  if they are preceded by ṇ(ங)  and ḻ(ழ)"
            }
          },
          {
            "paadal": "உயிர் ஈறு ஆகிய முன்னிலைக் கிளவியும்  புள்ளி இறுதி முன்னிலைக் கிளவியும்  இயல்பு ஆகுநவும் உறழ்பு ஆகுநவும் என்று  ஆயீர் இயல வல்லெழுத்து வரினே. ",
            "vilakkam":
            {
              "paadal_category":"Changes with Second Person Verbs",  
              "paadal_meaning":"If the standing word is a verb of the second person ending in a vowel or a consonant and the initial member of the succeeding word is a voiceless consonant, there is either no change in sandhi or the latter voiceless consonant is optionally doubled."
            }
          },
          {
            "paadal": "ஔ என வரூஉம் உயிர் இறு சொல்லும்  ஞ ந ம வ என்னும் புள்ளி இறுதியும்  குற்றியலுகரத்து இறுதியும் உளப்பட  முற்றத் தோன்றா முன்னிலை மொழிக்கே.",
            "vilakkam":
            {
              "paadal_category":"Exception to Second Person Verb Coalescence",  
              "paadal_meaning":"If the final member of the standing word mentioned in the previous sūtra is au(ஔ), ñ(ஞ), n(ந), m(ம), or u(உ), the change mentioned there does not operate completely."
            }
          },
          {
            "paadal": "உயிர் ஈறு ஆகிய உயர்திணைப் பெயரும்  புள்ளி இறுதி உயர்திணைப் பெயரும்  எல்லா வழியும் இயல்பு என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"Coalescence with Human Class Nouns",  
              "paadal_meaning":"No change takes place in sandhi when the standing word is uyartiṇai(உயர்திணை) whether the succeeding word is in case-relation to it or not."
            }
          },
          {
            "paadal": "அவற்றுள்,  இகர ஈற்றுப் பெயர் திரிபு இடன் உடைத்தே.",
            "vilakkam":
            {
              "paadal_category":"Coalescence with Human Class Nouns",  
              "paadal_meaning":"Of them some of the nouns ending in 'i'(இ) undergo change in sandhi."
            }
          },
          {
            "paadal": "அஃறிணை விரவுப்பெயர் இயல்புமார் உளவே.",
            "vilakkam":
            {
              "paadal_category":"Changes with Human-Non-Human Mixed Class Nouns",  
              "paadal_meaning":" Such of those uyartiṇai (உயர்திணை)  nouns which are used as ag(ஃ )ṟiṇai (அஃறிணை) also do not, sometimes, have the change."
            }
          },
          {
            "paadal": "புள்ளி இறுதியும் உயிர் இறு கிளவியும்  வல்லெழுத்து மிகுதி சொல்லிய முறையான்  தம்மின் ஆகிய தொழிற்சொல் முன் வரின்  மெய்ம்மை ஆகலும் உறழத் தோன்றலும்  அம் முறை இரண்டும் உரியவை உளவே  வேற்றுமை மருங்கின் போற்றல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"Changes involving the Third Case",  
              "paadal_meaning":"If a noun (with its third case-suffix dropped) ends in a vowel or consonant and is followed by a verb which denotes its action and which begins with such a letter as admits its doubling (according to the rules mentioned in Uyirmayaṅkiyal(உயிர்மயங்கியல்) and Puḷli mayaṅkiyal(புல்லி மயங்கியல்)), there is no change or the doubling of the initial letter of the succeeding word is optional."
            }
          },
          {
            "paadal": "மெல்லெழுத்து மிகு வழி வலிப்பொடு தோன்றலும்  வல்லெழுத்து மிகு வழி மெலிப்பொடு தோன்றலும்  இயற்கை மருங்கின் மிகற்கை தோன்றலும்  உயிர் மிக வரு வழி உயிர் கெட வருதலும்  சாரியை உள் வழிச் சாரியை கெடுதலும்  சாரியை உள் வழித் தன் உருபு நிலையலும்  சாரியை இயற்கை உறழத் தோன்றலும்  உயர்திணை மருங்கின் ஒழியாது வருதலும்  அஃறிணை விரவுப்பெயர்க்கு அவ் இயல் நிலையலும்   மெய் பிறிது ஆகு இடத்து இயற்கை ஆதலும்  அன்ன பிறவும் தன் இயல் மருங்கின்  மெய் பெறக் கிளந்து பொருள் வரைந்து இசைக்கும்  ஐகார வேற்றுமைத் திரிபு என மொழிப. ",
            "vilakkam":
            {
              "paadal_category":"Changes involving the Second Case",  
              "paadal_meaning":"The different kinds of sandhi which take place between the standing word and the coming word when the former is of the second case with the case-suffix ai (ஐ) or without it are as follows:- (1) Insertion of a voiceless consonant for the nasal or (2) vice versa ; (3) insertion (of a letter or letters) when there should be no change; (4) absence of a vowel which ought to have been inserted; (5) absence of flexional increment where it ought to be ; (6) presence of 'ai' (ஐ) itself along with the flexional increment ; (7) optional insertion of letters instead of flexional increment ; (8) invariable presence of 'ai'(ஐ) at the end of uyartiṇai(உயர்திணை)  words and viravuppeyar(விரவுப்பெயர்); (9) absence of change when there ought to have been assimilation and substitution etc."
            }
          },
          {
            "paadal": "வேற்றுமை அல்வழி இ ஐ என்னும்  ஈற்றுப் பெயர்க் கிளவி மூ வகை நிலைய  அவைதாம்,  இயல்பு ஆகுநவும் வல்லெழுத்து மிகுநவும்  உறழ் ஆகுநவும் என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"Non-case Relations with i (இ) and ai (ஐ) Endings",  
              "paadal_meaning":"If the standing word ends in i (இ)  or ai (ஐ) and if it does not stand in case-relation to the succeeding word, there are 3 possible cases of sandhi:—(1) absence of any change; (2) insertion of a voiceless consonant and; (3) optional insertion of the same."
            }
          },
          {
            "paadal": "சுட்டு முதல் ஆகிய இகர இறுதியும்  எகர முதல் வினாவின் இகர இறுதியும்  சுட்டுச் சினை நீடிய ஐ என் இறுதியும்  யா என் வினாவின் ஐ என் இறுதியும்  வல்லெழுத்து மிகுநவும் உறழ் ஆகுநவும்  சொல்லிய மருங்கின் உள என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"Coalescence with Words Declining for the Seventh Case",  
              "paadal_meaning":"When the standing word begins with a demonstrative root or the interrogative root 'e' (எ)  and ends in i(இ), or when it begins with the lengthened form of the demonstrative root or yā(யா), the initial member of interrogative pronouns, and ends in ai(ஐ), a voiceless consonant is inserted between it and the succeeding word either primarily or optionally."
            }
          },
          {
            "paadal": "நெடியதன் முன்னர் ஒற்று மெய் கெடுதலும்  குறியதன் முன்னர்த் தன் உருபு இரட்டலும்  அறியத் தோன்றிய நெறி இயல் என்ப.",
            "vilakkam":
            {
              "paadal_category":"Long and Short Vowels Followed by Consonants",  
              "paadal_meaning":"It is said that, in usage, the consonant that stands as the final member of the standing word or base of a word is dropped or doubled according as it respectively follows a long or short vowel."
            }
          },
          {
            "paadal": "ஆறன் உருபினும் நான்கன் உருபினும்  கூறிய குற்றொற்று இரட்டல் இல்லை  ஈறு ஆகு புள்ளி அகரமொடு நிலையும்  நெடு முதல் குறுகும் மொழி முன் ஆன.",
            "vilakkam":
            {
              "paadal_category":"Long and Short Vowels Followed by Consonants",  
              "paadal_meaning":"If the base of words which shorten their long vowel in oblique cases are followed by the fourth, or sixth, case-suffix, their final consonants are not doubled, but 'a'(அ)  is inserted after them."
            }
          },
          {
            "paadal": "நும் என் இறுதியும் அந் நிலை திரியாது.",
            "vilakkam":
            {
              "paadal_category":"Long and Short Vowels Followed by Consonants",  
              "paadal_meaning":"The same is the case with num."
            }
          },
          {
            "paadal": "உகரமொடு புணரும் புள்ளி இறுதி  யகரமும் உயிரும் வரு வழி இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"Long and Short Vowels Followed by Consonants",  
              "paadal_meaning":"The words which are capable of having 'u'(உ)  inserted after their final consonant and the succeeding word, do not have it if the succeeding word begins with a vowel or y(ய)."
            }
          },
          {
            "paadal": "உயிரும் புள்ளியும் இறுதி ஆகி  அளவும் நிறையும் எண்ணும் சுட்டி  உள எனப்பட்ட எல்லாச் சொல்லும்  தம்தம் கிளவி தம் அகப்பட்ட  முத்தை வரூஉம் காலம் தோன்றின்  ஒத்தது என்ப ஏ என் சாரியை.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"It is said that ē (ஏ) is the proper cāriyai (சாரியை) or flexional increment after the words that denote measure, weight or number if they are followed by a similar word denoting lesser measure, weight or number."
            }
          },
          {
            "paadal": "அரை என வரூஉம் பால் வரை கிளவிக்கு  புரைவது அன்றால் சாரியை இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"The above ē (ஏ)  is not inserted if the succeeding word is arai (அரை). "
            }
          },
          {
            "paadal": "குறை என் கிளவி முன் வரு காலை  நிறையத் தோன்றும் வேற்றுமை இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"If the word kuṟai (குறை) follows a word denoting measure, weight or number, the sandhi that takes place there, is the same as that when the two words stand in case relation to each other."
            }
          },
          {
            "paadal": "குற்றியலுகரக்கு இன்னே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"If kuṟai(குறை) follows a word denoting measure, weight or number whose final letter is kuṟṟiyalukaram (குற்றியலுகரம்), the flexional increment in is inserted between them."
            }
          },
          {
            "paadal": "அத்து இடை வரூஉம் கலம் என் அளவே.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"Attu(அத்து) is inserted if kuṟai(குறை) follows kalam(கலம்)."
            }
          },
          {
            "paadal": "பனை என் அளவும் கா என் நிறையும்  நினையும் காலை இன்னொடு சிவணும்.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":" On careful consideration it is seen that the cāriyai (சாரியை)  in is inserted if kuṟai (குறை) follows the word 'paṉai' (பனை) denoting measure and kā (கா) denoting weight."
            }
          },
          {
            "paadal": "அளவிற்கும் நிறையிற்கும் மொழி முதல் ஆகி  உள எனப்பட்ட ஒன்பதிற்று எழுத்தே  அவைதாம்,  க ச த ப என்றா ந ம வ என்றா  அகர உகரமொடு அவை என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"There are only nine letters that stand at the beginning of words denoting measure and weight and they are k (க), c (ச), t (த), p (ப), n (ந), m (ம),v (வ), a (அ) and u (உ)."
            }
          },
          {
            "paadal": "ஈறு இயல் மருங்கின் இவை இவற்று இயல்பு எனக்  கூறிய கிளவிப் பல் ஆறு எல்லாம்  மெய்த் தலைப்பட்ட வழக்கொடு சிவணி  ஒத்தவை உரிய புணர்மொழி நிலையே.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving terms of Measure, Weight and Number",  
              "paadal_meaning":"All those changes in sandhi other than those that have been mentioned here must be determined from usage."
            }
          },
          {
            "paadal": "பலர் அறி சொல் முன் யாவர் என்னும்  பெயரிடை வகரம் கெடுதலும் ஏனை  ஒன்று அறி சொல் முன் யாது என் வினா இடை  ஒன்றிய வகரம் வருதலும் இரண்டும்  மருவின் பாத்தியின் திரியுமன் பயின்றே. ",
            "vilakkam":
            {
              "paadal_category":"The Deviant Forms of yāvar (யாவர்) and yātu (யாது)",  
              "paadal_meaning":"In usage the 'va' (வ)  of yāvar (யாவர்)  when it follows a plural noun is dropped and 'va'(வ)  is inserled between yā (யா) and tu (து)  of the interrogative pronoun yātu (யாது) when it follows neuter singular."
            }
          }
        ]
      },
      {
        "iyal_name": "உருபியல்",
        "iyal_eng":"Case Morphemes",
        "noorpa": [
          {
            "paadal": "அ ஆ உ ஊ ஏ ஔ என்னும்  அப் பால் ஆறன் நிலைமொழி முன்னர்  வேற்றுமை உருபிற்கு இன்னே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme 'iṉ'(இன்)",  
              "paadal_meaning":"The inflexional increment 'iṉ'(இன்) is inserted between the noun base ending in a(அ), ā (ஆ), u (உ), ū (ஊ), ē (ஏ) and au(ஔ) and the case-suffixes."
            }
          },
          {
            "paadal": "பல்லவை நுதலிய அகர இறு பெயர்  வற்றொடு சிவணல் எச்சம் இன்றே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme Vaṟṟu (வற்று) ",  
              "paadal_meaning":"The words which denote many and which end in 'a'(அ),  may also take the Kāriyai (காரியை)  Vaṟṟu (வற்று)."
            }
          },
          {
            "paadal": "யா என் வினாவும் ஆயியல் திரியாது.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme Vaṟṟu (வற்று) ",  
              "paadal_meaning":"Yā (யா) also is of the same nature (i e.) it takes Vaṟṟu (வற்று) after it before the case-suffix."
            }
          },
          {
            "paadal": "சுட்டு முதல் உகரம் அன்னொடு சிவணி  ஒட்டிய மெய் ஒழித்து உகரம் கெடுமே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme ann(அன்)",  
              "paadal_meaning":"The words which begin with a demonstrative root and end in u(உ)take ''aṉ''(அன்) before the case-suffix and drop their final u(உ)."
            }
          },
          {
            "paadal": "சுட்டு முதல் ஆகிய ஐ என் இறுதி  வற்றொடு சிவணி நிற்றலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme Vaṟṟu (வற்று) ",  
              "paadal_meaning":"The words which begin with a demonstrative root and end in 'ai'(ஐ) may also take Vaṟṟu (வற்று)  before the case-suffix."
            }
          },
          {
            "paadal": "யா என் வினாவின் ஐ என் இறுதியும்  ஆயியல் திரியாது என்மனார் புலவர்  ஆவயின் வகரம் ஐயொடும் கெடுமே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme Vaṟṟu (வற்று)",  
              "paadal_meaning":"Learned men say that the interrogative yavai(யாவை) is of the same nature (i.e.) it takes Vaṟṟu (வற்று)  after it before case-suffix. Then 'vai(வை)' of yavai(யாவை)  is dropped."
            }
          },
          {
            "paadal": "நீ என் ஒரு பெயர் நெடு முதல் குறுகும்  ஆவயின் னகரம் ஒற்று ஆகும்மே.",
            "vilakkam":
            {
              "paadal_category":"Coalescence involving nii (நீ)",  
              "paadal_meaning":"Ī(ஈ) of ní(நீ) is shortened before case-suffix, when ṉ(ன்) is inserted between them."
            }
          },
          {
            "paadal": "ஓகார இறுதிக்கு ஒன்னே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme  Oṉ(ஒன்)",  
              "paadal_meaning":"Oṉ(ஒன்) is the Kāriyai (காரியை) that is inserted between the base ending in Ō(ஓ) and the case-suffix."
            }
          },
          {
            "paadal": "அ ஆ என்னும் மரப்பெயர்க் கிளவிக்கு  அத்தொடும் சிவணும் ஏழன் உருபே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme attu(அத்து) with tree names",  
              "paadal_meaning":"attu(அத்து),  also is inserted between the base of words ending in a(அ) or ā (ஆ), and denoting trees and the seventh case-suffix."
            }
          },
          {
            "paadal": "ஞ ந என் புள்ளிக்கு இன்னே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"The empty  morpheme in with /ñ (ஞ)/ and /n (ந)/",  
              "paadal_meaning":"'iṉ(இன்) is the Kāriyai (காரியை)   that is inserted after the base ending in Ñ (ஞ) and n(ந)"
            }
          },
          {
            "paadal": "சுட்டு முதல் வகரம் ஐயும் மெய்யும்  கெட்ட இறுதி இயல் திரிபு இன்றே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme Vaṟṟu (வற்று) with demonstratives",  
              "paadal_meaning":"There is no difference in nature between the words beginning with the demonstrative roots and ending in v(வு) j[ie.) av(அவ்வு), iv(அவ்வு) and uv(உவ்வு) and the word yavai(யாவை)  which drops its 'vai(வை) (when it takes the cariyai varru). (i.e av(அவ்வு), iv(அவ்வு) and uv(உவ்வு)take the Kāriyai (காரியை)  Vaṟṟu (வற்று) when their final v(வு) is dropped."
            }
          },
          {
            "paadal": "ஏனை வகரம் இன்னொடு சிவணும். ",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme in with tev",  
              "paadal_meaning":"Word that ends in v(வு) other than those mentioned in the previous sutra takes the Kāriyai (காரியை)  'iṉ(இன்)."
            }
          },
          {
            "paadal": "மஃகான் புள்ளி முன் அத்தே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme attu(அத்து) ",  
              "paadal_meaning":"The base that ends in 'iṉ(இன்) takes attu(அத்து),  before case-suffix."
            }
          },
          {
            "paadal": "இன் இடை வரூஉம் மொழியுமார் உளவே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme inn (இன்)",  
              "paadal_meaning":"Some bases ending in m(ம்) take in instead of attu(அத்து), before case- suffixes."
            }
          },
          {
            "paadal": "நும் என் இறுதி இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"Non-change with num (நும்)",  
              "paadal_meaning":"num(நும்)   takes the case-suffix directly without the insertion of any flexional increment."
            }
          },
          {
            "paadal": "தாம் நாம் என்னும் மகர இறுதியும்  யாம் என் இறுதியும் அதன் ஓரன்ன  ஆ எ ஆகும் யாம் என் இறுதி  ஆவயின் யகர மெய் கெடுதல் வேண்டும்  ஏனை இரண்டும் நெடு முதல் குறுகும்.",
            "vilakkam":
            {
              "paadal_category":"Changes with tām(தாம்), nām (நாம்) and yām (யாம்)",  
              "paadal_meaning":"Of the bases ending in m(ம்),  tām(தாம்) and  nām(நாம்) have their vowels shortened before case-suffix and yām(யாம்) is changed to em(எம்) before the same."
            }
          },
          {
            "paadal": "எல்லாம் என்னும் இறுதி முன்னர்  வற்று என் சாரியை முற்றத் தோன்றும்  உம்மை நிலையும் இறுதியான.",
            "vilakkam":
            {
              "paadal_category":"The empty morphemes varru and um with Ellām (எல்லாம்)",  
              "paadal_meaning":"The base Ellām (எல்லாம்) takes Vaṟṟu (வற்று) before case-suffix and um(உம்) is added after the case-suffix"
            }
          },
          {
            "paadal": "உயர்திணை ஆயின் நம் இடை வருமே.",
            "vilakkam":
            {
              "paadal_category":"The intervention of the empty morpheme Nam(நம்)",  
              "paadal_meaning":"Nam(நம்) is inserted instead of varru Vaṟṟu (வற்று) in the previous case if base Ellām (எல்லாம்) refers to Uyartiṇai (உயர்திணை)."
            }
          },
          {
            "paadal": "எல்லாரும் என்னும் படர்க்கை இறுதியும்  எல்லீரும் என்னும் முன்னிலை இறுதியும்  ஒற்றும் உகரமும் கெடும் என மொழிப  நிற்றல் வேண்டும் ரகரப் புள்ளி  உம்மை நிலையும் இறுதியான  தம் இடை வரூஉம் படர்க்கை மேன  நும் இடை வரூஉம் முன்னிலை மொழிக்கே.",
            "vilakkam":
            {
              "paadal_category":"Changes involving Ellārum (எல்லாரும்) and Ellār(எல்லார்) ",  
              "paadal_meaning":"' Ellārum (எல்லாரும்)' which denotes the third person and Ellārum (எல்லாரும்), which denotes the second person have tam(தம்) (followed by the case- suffix) and num(நும்)  (followed by the case-suffix) inserted between ellār(எல்லார்) and um(உம்), and Ellār(எல்லார்) and um(உம்), respectively."
            }
          },
          {
            "paadal": "தான் யான் என்னும் ஆயீர் இறுதியும்  மேல் முப் பெயரொடும் வேறுபாடு இலவே.",
            "vilakkam":
            {
              "paadal_category":"Chnages involving Ṭāṉ (டான்) and  Yāṉ (யான்)",  
              "paadal_meaning":"Ṭāṉ (டான்) and Yāṉ (யான்) undergo the same change as the above three words tām(தாம்), nām(நாம்)  and yām(யாம்)  (before case-suffixes). (i.e) tan is changed to Ṭāṉ (டான்)  in oblique cases and Yāṉ (யான்) eṉ(ன்)."
            }
          },
          {
            "paadal": "அழனே புழனே ஆயிரு மொழிக்கும்  அத்தும் இன்னும் உறழத் தோன்றல்  ஒத்தது என்ப உணருமோரே.",
            "vilakkam":
            {
              "paadal_category":"The empty morphemes attu(அத்து) and 'iṉ(இன்)",  
              "paadal_meaning":"Learned men say that the Kāriyai (காரியை)  attu(அத்து) and 'iṉ(இன்) are optionally added after the words alaṉ(அழ) and puḻaṉ(புழ) in oblique cases. "
            }
          },
          {
            "paadal": "அன் என் சாரியை ஏழன் இறுதி  முன்னர்த் தோன்றும் இயற்கைத்து என்ப.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme aṉ(அன்) and ēḻ(ஏழ)",  
              "paadal_meaning":"The Kāriyai (காரியை) aṉ(அன்) is added after the number ēḻ(ஏழ)."
            }
          },
          {
            "paadal": "குற்றியலுகரத்து இறுதி முன்னர்  முற்றத் தோன்றும் இன் என் சாரியை.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme in with the shortened /ū(ஊ)/",  
              "paadal_meaning":"The flexional increment 'iṉ(இன்)' is inserted after the base ending in  ū(ஊ)"
            }
          },
          {
            "paadal": " நெட்டெழுத்து இம்பர் ஒற்று மிகத் தோன்றும்  அப் பால் மொழிகள் அல் வழியான.",
            "vilakkam":
            {
              "paadal_category":"Doubling of /ṭ(ட்) and ṟ(ற்)/",  
              "paadal_meaning":"If the consonant that precedes ū(ஊ) is preceded by a long vowel, it is doubled wherever possible (only ṭ(ட்) and ṟ(ற்) are doubled)."
            }
          },
          {
            "paadal": "அவைதாம்,  இயற்கைய ஆகும் செயற்கைய என்ப.",
            "vilakkam":
            {
              "paadal_category":"Doubling of /ṭ(ட்) and ṟ(ற்)/",  
              "paadal_meaning":"It is said that the flexional increment iṉ(இன்) is not added in the above case."
            }
          },
          {
            "paadal": "எண்ணின் இறுதி அன்னொடு சிவணும்.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme aṉ(அன்)",  
              "paadal_meaning":"All numbers ending in ū(ஊ) take the flexional increment aṉ(அன்)"
            }
          },
          {
            "paadal": " ஒன்று முதல் ஆக பத்து ஊர்ந்து வரூஉம்  எல்லா எண்ணும் சொல்லும் காலை  ஆன் இடை வரினும் மானம் இல்லை  அஃது என் கிளவி ஆவயின் கெடுமே  உய்தல் வேண்டும் பஃகான் மெய்யே.",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme āṇ(ஆண்) with numeral terms",  
              "paadal_meaning":"In compound words having the numbers one to eight (i.e., Oṉṟu(ஒன்று),ireṇṭu(ரெண்டு), etc.) as the first member and paஃtu as the second member, there is no harm if the flexional increment 'āṇ(ஆண்)' also is added, and in that case aஃtu of paஃtu is dropped."
            }
          },
          {
            "paadal": "யாது என் இறுதியும் சுட்டு முதல் ஆகிய  ஆய்த இறுதியும் அன்னொடு சிவணும்  ஆய்தம் கெடுதல் ஆவயினான. ",
            "vilakkam":
            {
              "paadal_category":"The empty morpheme ann with yātu (யாது) and akktu",  
              "paadal_meaning":"The word yātu (யாது) and the words (aஃtu, iஃtu and uஃtu) which commence with a demonstrative letter and have āytam(ஆயுதம்) in the middle take the increment ant aṉ(அன்) and the āytam(ஆயுதம்) in the latter case is then dropped."
            }
          },
          {
            "paadal": "ஏழன் உருபிற்குத் திசைப் பெயர் முன்னர்  சாரியைக் கிளவி இயற்கையும் ஆகும்  ஆவயின் இறுதி மெய்யொடும் கெடுமே.",
            "vilakkam":
            {
              "paadal_category":"Nouns denoting directions",  
              "paadal_meaning":"Words denoting direction, when followed by the seventh case-suffix, do not optionally take the increment in (mentioned in sutra 196), in which case, the final  ū(ஊ) with the preceding consonant is dropped."
            }
          },
          {
            "paadal": "புள்ளி இறுதியும் உயிர் இறு கிளவியும்  சொல்லிய அல்ல ஏனைய எல்லாம்  தேரும் காலை உருபொடு சிவணி  சாரியை நிலையும் கடப்பாடு இலவே. ",
            "vilakkam":
            {
              "paadal_category":"Nouns denoting directions",  
              "paadal_meaning":"All words ending in consonants or vowels, not mentioned above, sometimes fake flexional increments and sometimes not."
            }
          }
        ]
      },
      {
        "iyal_name": "உயிர்மயங்கியல்",
        "iyal_eng":"Vowel Coalescence",
        "noorpa": [
          {
            "paadal": "அகர இறுதிப் பெயர் நிலை முன்னர்  வேற்றுமை அல் வழி க ச த ப தோன்றின்  தம்தம் ஒத்த ஒற்று இடை மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If the standing word is a noun ending in 'a'(அ), and if it is followed by k(க), c(ச), t (த)or p(ப), k(க), c(ச), t(த) or p(ப) is respectively inserted in non-case-relation Canti (சந்தி)."
            }
          },
          {
            "paadal": "வினையெஞ்சுகிளவியும் உவமக் கிளவியும்  என என் எச்சமும் சுட்டின் இறுதியும்  ஆங்க என்னும் உரையசைக் கிளவியும்  ஞாங்கர்க் கிளந்த வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If verbal participles and particles denoting comparison that end in 'a'(அ) the particle 'eṉa'(என), the demonstrative root  'a '(அ) and the particle 'āṅka'(ஆங்க) happen to be standing words by k(க), c(ச), t (த)or p(ப), is inserted after them as in the case mentioned in the previous sutra (when they are followed by k(க), c(ச), t (த)or p(ப), respectively)."
            }
          },
          {
            "paadal": "சுட்டின் முன்னர் ஞ ந ம தோன்றின்  ஒட்டிய ஒற்று இடை மிகுதல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If the demonstrative letter 'a'(அ) is followed by n̆(ஞ), n(ந்)or m(ம்) n̆(ஞ), n(ந்)or m(ம்)is respectively inserted after it."
            }
          },
          {
            "paadal": "ய வ முன் வரினே வகரம் ஒற்றும்.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If the demonstrative letter ' a'(அ) is followed by y(ய) or v(வ), v(வ) is inserted after it."
            }
          },
          {
            "paadal": "உயிர் முன் வரினும் ஆயியல் திரியாது.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If the demonstrative letter 'a'(அ) is followed even by a vowel, the same is the case. [(i.e) v (வ)is inserted after it.]"
            }
          },
          {
            "paadal": "நீட வருதல் செய்யுளுள் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The demonstrative letter 'a'(அ) may be lengthened to ā(ஆ) in poetry."
            }
          },
          {
            "paadal": "சாவ என்னும் செய என் எச்சத்து  இறுதி வகரம் கெடுதலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The verbal participle ' cāva'(காவ) optionally loses its final ' va(வ)' (when it happens to be the standing word."
            }
          },
          {
            "paadal": "அன்ன என்னும் உவமக் கிளவியும்  அண்மை சுட்டிய விளிநிலைக் கிளவியும்  செய்ம்மன என்னும் தொழில் இறு சொல்லும்  ஏவல் கண்ணிய வியங்கோட் கிளவியும்  செய்த என்னும் பெயரெஞ்சுகிளவியும்  செய்யிய என்னும் வினையெஞ்சுகிளவியும்  அம்ம என்னும் உரைப்பொருட் கிளவியும்  பலவற்று இறுதிப் பெயர்க்கொடை உளப்பட  அன்றி அனைத்தும் இயல்பு என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"It is said that no change takes place in Canti (சந்தி) if any of the following words that end in 'a'(அ) happen to be the standing words:—(l)'aṇṇā'(அண்ணா), the particle of comparison (2) vocatives addressed to persons near at hand (3) finite verbs of the type 'ceym'maṉa'(செய்ம்மன) (4) verbs of the imperative mood (5) noun participles of the type 'ceyta'(செய்த) (6) verbal participles of the type 'Ceyyiya'(செய்யிய) (7) am'mā(அம்மா), the particle used in addressing a person and (8) palla(பல்ல), pala(பல) etc. that are always plural pronouns."
            }
          },
          {
            "paadal": "வாழிய என்னும் செய என் கிளவி  இறுதி யகரம் கெடுதலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"'Ya(ய)' of the optative vāḻiya(வாழிய) is sometimes dropped when it is the standing word."
            }
          },
          {
            "paadal": "உரைப்பொருட் கிளவி நீட்டமும் வரையார்.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"None prevents the lengthening of the uraipporuṭkiḷavi(உரைப்பொருட்கிளவி) (i.e.) the word 'ammā(அம்மா), mentioned in sutra 211."
            }
          },
          {
            "paadal": "பலவற்று இறுதி நீடு மொழி உளவே  செய்யுள் கண்ணிய தொடர்மொழியான.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The final 'a'(அ)of palla(பல்ல), pala(பல) etc. is sometimes lengthened in compound words in poetry."
            }
          },
          {
            "paadal": "தொடர் அல் இறுதி தம் முன் தாம் வரின்  லகரம் றகர ஒற்று ஆதலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"' La (ல)' of the standing word may sometimes be changed to r if those of the above-mentioned words that are not totarmoli (i, e., pala(பல)  and cila(சில)) are followed by the same words."
            }
          },
          {
            "paadal": "வல்லெழுத்து இயற்கை உறழத் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The insertion of c(சி), or p(ப) after the words pala(பல)  and cila(சில)if they are followed by the same words is only optional."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The same change takes place in case-relation Canti (சந்தி) ( i.e .) if the standing word is a noun ending in is 'a'(அ) and if it is followed by k(க), c(ச), t (த)or p(ப),  k(க), c(ச), t (த)or p(ப), is respectively insetted in case-relation Canti (சந்தி) in the same way as in non-case-relation Canti (சந்தி) mentioned in sutra 204"
            }
          },
          {
            "paadal": "மரப்பெயர்க் கிளவி மெல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If the standing word that ends in  'a'(அ)' denotes a tree, a nasal (i.e,) ṅ(ங்), Ñ (ஞ), n(ந்) or m(ம்)is inserted if it is followed by p(ப),  k(க), c(ச), t (த)or p(ப), respectively."
            }
          },
          {
            "paadal": "மகப்பெயர்க் கிளவிக்கு இன்னே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If is maka(மக) ' is the standing word, it takes the increment 'iṉ(ன்)' after it."
            }
          },
          {
            "paadal": "அத்து அவண் வரினும் வரை நிலை இன்றே.",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"If is not objectionable if the increment  attu(அத்து) ' is added after maka(மக)' instead of iṉ (ன்)."
            }
          },
          {
            "paadal": "பலவற்று இறுதி உருபு இயல் நிலையும். ",
            "vilakkam":
            {
              "paadal_category":"/'a'(அ)/ Ending words",  
              "paadal_meaning":"The words palla(பல்ல), pala(பல)etc. take (the increment 'Vaṟṟu (வற்று) if they are followed by k(க), c(ச), t (த)or p(ப),  k(க), c(ச), t (த)or p(ப), in the same way as when they are followed by case-suffixes."
            }
          },
          {
            "paadal": "ஆகார இறுதி அகர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"The changes (in non-case-relation Canti (சந்தி)) when the standing word is a noun and ends in ā (ஆ) are the same as those when it ends in ''a'(அ)' (if it is followed by k(க), c(ச), t (த)or p(ப),"
            }
          },
          {
            "paadal": "செய்யா என்னும் வினையெஞ்சுகிளவியும்  அவ் இயல் திரியாது என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"Learned men say that the same is the case if the standing word is the verbal participle of the type ceyya(செய்ய), (i.e.) k(க), c(ச), t (த)or p(ப),  k(க), c(ச), t (த)or p(ப), is respectively inserted if it is followed by k(க), c(ச), t (த)or p(ப),  k(க), c(ச), t (த)or p(ப),"
            }
          },
          {
            "paadal": "உம்மை எஞ்சிய இரு பெயர்த் தொகைமொழி  மெய்ம்மையாக அகரம் மிகுமே. ",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"In ummai-t-tokai(உம்மைத்தொகை) or dvandva(இருமை) compounds made up of two words of which the former member ends in ā (ஆ), 'a'(அ) is inserted after it."
            }
          },
          {
            "paadal": "ஆவும் மாவும் விளிப்பெயர்க் கிளவியும்  யா என் வினாவும் பலவற்று இறுதியும்  ஏவல் குறித்த உரையசை மியாவும்  தன் தொழில் உரைக்கும் வினாவின் கிளவியொடு  அன்றி அனைத்தும் இயல்பு என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"It is said that there is no change in Canti (சந்தி) if the standing words are (1) the noun ā (ஆ) or mā (மா) (2) nouns in the vocative case (3) the interrogative pronoun yā(யா) (4) the neuter plural finite verbs ending in ā (ஆ) (5) a verb in the imperative mood with the particle miyā (மியா) suffixed to it and (6) interrogative verbs denoting the action of the speaker."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"The changes in case-relation Canti (சந்தி) (when the standing word is a noun and ends in ā (ஆ) are the same as those when it ends in 'a'(அ) (if it is followed k(க), c(ச), t (த)or p(ப),) (i.e.) k(க), c(ச), t (த)or p(ப),is inserted."
            }
          },
          {
            "paadal": "குறியதன் முன்னரும் ஓரெழுத்து மொழிக்கும் அறியத் தோன்றும் அகரக் கிளவி.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"A (அ) ' is inserted after the standing word if it happens to be either a word ending in ā (ஆ)with a short vowel previous to it or 'a'(அ)single-lettered word ā (ஆ)."
            }
          },
          {
            "paadal": "இரா என் கிளவிக்கு அகரம் இல்லை.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"But ''a'(அ)' is not inserted if the standing word is ' irā(இரா) '."
            }
          },
          {
            "paadal": "நிலா என் கிளவி அத்தொடு சிவணும்.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"If  'nilā (நிலா)' is the standing word, it takes the increment attu(அத்து) ' after it."
            }
          },
          {
            "paadal": "யாமரக் கிளவியும் பிடாவும் தளாவும் ஆமுப்பெயரும் மெல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"If the three nouns yā(யா)  denoting tree Piṭā(பிடா) and Taḷā(தளா) are standing words, the nasal  ṅ(ங்), Ñ(ஞ), n(ந்) or m(ம்)is inserted (after the inserted element a according to the sutra 227)."
            }
          },
          {
            "paadal": "வல்லெழுத்து மிகினும் மானம் இல்லை.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"There is no harm even if a voiceless consonant (k(க), c(ச), t (த)or p(ப)) is inserted (instead of a nasal)."
            }
          },
          {
            "paadal": "மாமரக் கிளவியும் ஆவும் மாவும்  ஆ முப் பெயரும் அவற்று ஓரன்ன  அகரம் வல்லெழுத்து அவை அவண் நிலையா  னகரம் ஒற்றும் ஆவும் மாவும்",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"If the nouns mā (மா)  denoting tree, ā (ஆ).and mā (மா)  are standing words the same is the change in Canti (சந்தி) as is mentioned in the sutra 230 {i.e.) 'a'(அ)nasal is inserted. Besides in the case of ā (ஆ).and mā (மா)  , ṉ(ன்) is inserted in the place of  a followed by a nasal ."
            }
          },
          {
            "paadal": "ஆன் ஒற்று அகரமொடு நிலை இடன் உடைத்தே.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"If the standing word is ā (ஆ), it sometimes takes after it , ṉ(ன்) followed by 'a'(அ)."
            }
          },
          {
            "paadal": "ஆன் முன் வரூஉம் ஈகார பகரம்  தான் மிகத் தோன்றிக் குறுகலும் உரித்தே",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"If the standing word ā (ஆ), is followed by the word 'PĪ'(பீ), p is inserted after ā (ஆ), instead of  ṉ(ன்) and   Ī(ஈ)of pi is shortened to  'I'(இ)."
            }
          },
          {
            "paadal": "குறியதன் இறுதிச் சினை கெட உகரம்  அறிய வருதல் செய்யுளுள் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/aa (ஆ)/ending words",  
              "paadal_meaning":"In poetry, the final ā (ஆ) of the standing word which has a short vowel previous to it is sometimes shortened to a(அ) and u(உ) is inserted after it. "
            }
          },
          {
            "paadal": "இகர இறுதிப் பெயர்நிலை முன்னர்  வேற்றுமை ஆயின் வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"If the standing word is a noun and ends in ' I ' இ) a voiceless consonant (i.e(k(க), c(ச), t (த)or p(ப)) is inserted after it in case-relation Canti (சந்தி) (if the initial of the coming word is k(க), c(ச), t (த)or p(ப)"
            }
          },
          {
            "paadal": "இனி அணி என்னும் காலையும் இடனும்  வினையெஞ்சுகிளவியும் சுட்டும் அன்ன. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"The same is the case (i.e(k(க), c(ச), t (த)or p(ப)) is inserted) after the words ' iṉi(இனி) ' and  'aṇi(அணி)' respectively denoting time and place, verbal participles ending in ' I '(இ) and the demonstrative root ' I '(இ)"
            }
          },
          {
            "paadal": "இன்றி என்னும் வினையெஞ்சு இறுதி  நின்ற இகரம் உகரம் ஆதல்  தொன்று இயல் மருங்கின் செய்யுளுள் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"The final '  I '(இ) of iṉṟi(இன்றி) is changed to 'u'(உ) in old poetry."
            }
          },
          {
            "paadal": "சுட்டின் இயற்கை முன் கிளந்தற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"The nature of Canti (சந்தி)) after the demonstrative root ' I '(இ) is the same as that mentioned after 'a'(அ).(i.e. a nasal is inserted if the coming word commences with a nasal and 'v'(வ்) is inserted if it commences with 'y'(ய்) or 'v'(வ்))"
            }
          },
          {
            "paadal": "பதக்கு முன் வரினே தூணிக் கிளவி  முதல் கிளந்து எடுத்த வேற்றுமை இயற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"If the word 'tūṇi'(தூணி) is followed by the word ' patakku'(படக்கு), the change in Canti (சந்தி) is the same as that in case-relation Canti (சந்தி) (i.e. the voiceless p(பி) is inserted between them)."
            }
          },
          {
            "paadal": "உரி வரு காலை நாழிக் கிளவி  இறுதி இகரம் மெய்யொடும் கெடுமே  டகாரம் ஒற்றும் ஆவயினான. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"If the word 'nāḻi'(நாழி) is followed by the word  'uri'(உரி) , 'ḻi' (ழி) is dropped and  ṭ(ட்) takes its place."
            }
          },
          {
            "paadal": "பனி என வரூஉம் கால வேற்றுமைக்கு  அத்தும் இன்னும் சாரியை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"The word 'paṉi'(பனி) denoting season takes after it the increments 'attu'(அத்து) and 'iṉ'(ன்) in case-relation Canti (சந்தி)."
            }
          },
          {
            "paadal": "வளி என வரூஉம் பூதக் கிளவியும்  அவ் இயல் நிலையல் செவ்விது என்ப.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"It is said that the word 'vaḷi' (வளி) denoting one of the five elements is of the same nature (i.e.) it takes the increments 'attu'(அத்து)  or 'iṉ'(ன்) after it in case-relation Canti (சந்தி) ."
            }
          },
          {
            "paadal": "உதிமரக் கிளவி மெல்லெழுத்து மிகுமே. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"If the word  'uti'(உதி) denoting a kind of tree (is followed by a voiceless consonant), the corresponding nasal is inserted after it."
            }
          },
          {
            "paadal": "புளிமரக் கிளவிக்கு அம்மே சாரியை.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"The word 'puli' denoting tamarind tree takes after it the increment 'am' (அம்) (if it is followed by a voiceless consonant i.c., k (க), c (ச), t (த) or p (ம))."
            }
          },
          {
            "paadal": "ஏனைப் புளிப் பெயர் மெல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"A nasal is inserted after the word 'puḷi'(புளி) denoting anything other than the tamarind tree."
            }
          },
          {
            "paadal": "வல்லெழுத்து மிகினும் மானம் இல்லை  ஒல்வழி அறிதல் வழக்கத்தான.",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"There is no harm if a voiceless consonant is inserted (instead of a nasal in the previous case) if it is so in usage"
            }
          },
          {
            "paadal": "நாள் முன் தோன்றும் தொழில்நிலைக் கிளவிக்கு  ஆன் இடை வருதல் ஐயம் இன்றே. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"Any noun (ending in ' i ' (இ) and) denoting a star takes the increment 'āṉ'(ஆன்) after it, if it is followed by a verb."
            }
          },
          {
            "paadal": "திங்கள் முன் வரின் இக்கே சாரியை. ",
            "vilakkam":
            {
              "paadal_category":"/i (இ)/ ending preceding words",  
              "paadal_meaning":"Any noun (ending in 'i ' (இ)  and) denoting a month takes the increment  'ikku '(இக்கு) after it (if it is followed by a verb)."
            }
          },
          {
            "paadal": "ஈகார இறுதி ஆகார இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"/ī (ஈ)/ ending words",  
              "paadal_meaning":"The change in Canti (சந்தி) when the standing word ends in 'I'(இ) is the same as that when it ends in a (in non-case-relation Canti (சந்தி))."
            }
          },
          {
            "paadal": "நீ என் பெயரும் இடக்கர்ப் பெயரும்  மீ என மரீஇய இடம் வரை கிளவியும்  ஆவயின் வல்லெழுத்து இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"/ī (ஈ)/ ending words",  
              "paadal_meaning":"There is no change in Canti (சந்தி) when the standing word is 'nī'(நீ) 'pī'(பீ) or 'mī'(மீ) denoting place and it is followed by k(க), c(ச), t (த)or p(ப)."
            }
          },
          {
            "paadal": "இடம் வரை கிளவி முன் வல்லெழுத்து மிகூஉம்  உடன் நிலை மொழியும் உள என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"/ī (ஈ)/ ending words",  
              "paadal_meaning":"It is said that there are words before which a voiceless consonant is inserted when the standing word is 'mī'(மீ)."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/ī (ஈ)/ ending words",  
              "paadal_meaning":"The same is the case in case-relation Canti (சந்தி) (i.e.) a voiceless consonant k(க), c(ச), t (த)or p(ப).is inserted after a standing word ending-in ī (ஈ) and before the coming word commencing with a voiceless consonant."
            }
          },
          {
            "paadal": "நீ என் ஒரு பெயர் உருபு இயல் நிலையும்  ஆவயின் வல்லெழுத்து இயற்கை ஆகும். ",
            "vilakkam":
            {
              "paadal_category":"/ī (ஈ)/ ending words",  
              "paadal_meaning":"The single lettered word 'nī'(நீ) (when it stands as the standing word and when it is followed by k(க), c(ச), t (த)or p(ப). is changed to nīṉ(நீன்)) as before case-suffixes. In that case no voiceless consonant is inserted after it."
            }
          },
          {
            "paadal": "உகர இறுதி அகர இயற்றே. ",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"The change in non-case relation Canti (சந்தி) when the standing word ends in u(உ) (and when it is followed by k(க), c(ச), t (த)or p(ப)) is the same as when it ends in a(அ)."
            }
          },
          {
            "paadal": "சுட்டின் முன்னரும் அத் தொழிற்று ஆகும். ",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"The same is the case after the demonstrative root  u(உ)."
            }
          },
          {
            "paadal": "ஏனவை வரினே மேல் நிலை இயல்பே. ",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"If the demonstrative root u(உ) is tollowed by those other than k(க), c(ச), t (த)or p(ப) (i.e., by ṉ(ன்), n(ந்), m(ம்), y(ய) or v(வ்)) the change in Canti (சந்தி) is the same as after the demonstrative root  'a ' (அ) mentioned before."
            }
          },
          {
            "paadal": "சுட்டு முதல் இறுதி இயல்பு ஆகும்மே.",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"There is no change in Canti (சந்தி) if the standing word is one commencing with a (அ) demonstrative root and ending in u (i. e.) atu(அது), itu(இது), & utu(உது)."
            }
          },
          {
            "paadal": "அன்று வரு காலை ஆ ஆகுதலும்  ஐ வரு காலை மெய் வரைந்து கெடுதலும்  செய்யுள் மருங்கின் உரித்து என மொழிப. ",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"It is said that in poetry the final u(உ) of atu(அது), itu(இது), & utu(உது) is changed to 'a'(அ)  if it is followed by the word aṉṟu(அன்று) and it is dropped before the suffix 'ai '(ஐ)."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே.",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"The same is the case in case-relation-Canti (சந்தி) ( i.e .) the change in case-relation Canti (சந்தி) when the standing word ends in u(உ) and is followed k(க), c(ச), t (த)or p(ப), is the same as that when the standing word ends in 'a'(அ)  ."
            }
          },
          {
            "paadal": "எருவும் செருவும் அம்மொடு சிவணி  திரிபு இடன் உடைய தெரியும் காலை  அம்மின் மகரம் செருவயின் கெடுமே  தம் ஒற்று மிகூஉம் வல்லெழுத்து இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"When the standing words are eru(எரு) and ceru(செரு) and they are followed by k(க), c(ச), t (த)or p(ப), the increment ' am '(அம்) is added after the former and 'a'(அ) followed by the same consonant (i.e., k(க), c(ச), t (த)or n(ந்),) after the latter."
            }
          },
          {
            "paadal": "ழகர உகரம் நீடு இடன் உடைத்தே  உகரம் வருதல் ஆவயினான. ",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"If the standing word ends in ḻu(ழு), u(உ) may be lengthened to  ū(ஊ) and another is inserted after it."
            }
          },
          {
            "paadal": "ஒடுமரக் கிளவி உதி மர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"The change in Canti (சந்தி) when the standing word is oṭu(ஒடு) is same when it is the word uti(உதி) denoting a tree."
            }
          },
          {
            "paadal": "சுட்டு முதல் இறுதி உருபு இயல் நிலையும்  ஒற்று இடை மிகா வல்லெழுத்து இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"/u (உ)/ ending words",  
              "paadal_meaning":"If the standing word commences  ends in u(உ), and is followed by k(க), c(ச), t (த),c(ச),  or aṉ(அன்)) as it does before a case-suffix and the succeeding consonant is not doubled."
            }
          },
          {
            "paadal": "ஊகார இறுதி ஆகார இயற்றே. ",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"The change (in non-case-relation Canti (சந்தி)) when the standing word is a noun and ends in ū(ஊ)is the same as that when it ends in ā (ஆ) (when it is followed by k(க), c(ச), t (த)or p(ப))."
            }
          },
          {
            "paadal": "வினையெஞ்சுகிளவிக்கும் முன்னிலை மொழிக்கும்  நினையும் காலை அவ் வகை வரையார்.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"None prevents the same change in Canti (சந்தி) when the standing word is a verbal participle ending in ū(ஊ)or finite verbs of the second person ending in ū(ஊ) (and when they are followed by  k(க), c(ச), t (த)or p(ப))."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"The same is the case in case-relation Canti (சந்தி) (i.c.) the change is the same when the standing word ends in ū(ஊ) as that when it ends in ā (ஆ)."
            }
          },
          {
            "paadal": "குற்றெழுத்து இம்பரும் ஓரெழுத்து மொழிக்கும்  நிற்றல் வேண்டும் உகரக் கிளவி.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"When the standing word is one-lettered word ending in ū(ஊ) or when it has a short vowel previous to its final ū(ஊ), u(உ) is also inserted."
            }
          },
          {
            "paadal": "பூ என் ஒரு பெயர் ஆயியல்பு இன்றே  ஆவயின் வல்லெழுத்து மிகுதலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"The same change does not take place when the standing word is pū (பூ); a voiceless consonant may also be inserted alter it."
            }
          },
          {
            "paadal": "ஊ என் ஒரு பெயர் ஆவொடு சிவணும்",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"The one-lettered word ū(ஊ) (takes ṉ(ன்) after it in case-relation Canti (சந்தி)) in the same way as the word ā (ஆ) (when it is the standing word)."
            }
          },
          {
            "paadal": "அக்கு என் சாரியை பெறுதலும் உரித்தே  தக்க வழி அறிதல் வழக்கத்தான.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"Learn that, in usage ū(ஊ) takes the increment akkū (அக்கூ) after ṉ(ன்)."
            }
          },
          {
            "paadal": "ஆடூஉ மகடூஉ ஆயிரு பெயர்க்கும்  இன் இடை வரினும் மானம் இல்லை.",
            "vilakkam":
            {
              "paadal_category":"The /ū (ஊ)/ ending words",  
              "paadal_meaning":"There is no harm if the increment iṉ(ன்)  is inserted after the standing words āṭūu (ஆடூஉ) and makaṭūu (மகடூஉ)."
            }
          },
          {
            "paadal": "எகர ஒகரம் பெயர்க்கு ஈறு ஆகா  முன்னிலை மொழிய என்மனார் புலவர்  தேற்றமும் சிறப்பும் அல் வழியான.",
            "vilakkam":
            {
              "paadal_category":" /e (எ)/ and /o (ஒ)/ word finals",  
              "paadal_meaning":"E(எ) and o(ஒ) never stand as final members of nouns; they stand so only in the verbs of second person except when they are used as particles to denote certainty and superiority respectively"
            }
          },
          {
            "paadal": "தேற்ற எகரமும் சிறப்பின் ஒவ்வும்  மேற் கூறு இயற்கை வல்லெழுத்து மிகா. ",
            "vilakkam":
            {
              "paadal_category":" /e (எ)/ and /o (ஒ)/ word finals",  
              "paadal_meaning":"A voiceless consonant (k(க), c(ச), t (த)or p(ப)) is not inserted after the particles e denoting certainty and o(ஒ)  denoting superiority."
            }
          },
          {
            "paadal": "ஏகார இறுதி ஊகார இயற்றே",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"The change in non-case-relation Canti (சந்தி) when the standing word (is a noun), ends in ē(ஏ) (and is followed by a voiceless consonant) is the same as that when it ends in ū(ஊ)."
            }
          },
          {
            "paadal": "மாறு கொள் எச்சமும் வினாவும் எண்ணும்  கூறிய வல்லெழுத்து இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"There is no change in Canti (சந்தி) if (k(க), c(ச), t (த)or p(ப)follows the particle ē(ஏ) when the latter denotes negation, question or number."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"The same is the case in case-relation Canti (சந்தி) (i.e.) the change is the same when the standing word ends in ē(ஏ) as that when it ends in ū(ஊ)."
            }
          },
          {
            "paadal": "ஏ என் இறுதிக்கு எகரம் வருமே. ",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"ē(ஏ) will be followed by e((எ)."
            }
          },
          {
            "paadal": "சே என் மரப்பெயர் ஒடுமர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"The Canti (சந்தி) when the standing word is cē (சே) denoting a tree is the same as that when it out denoting a trees."
            }
          },
          {
            "paadal": "பெற்றம் ஆயின் முற்ற இன் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If the standing word cē (சே) denotes perrain (and is followed by (k(க), c(ச), t (த)or p(ப), it takes the increment  iṉ(ன்)after it."
            }
          },
          {
            "paadal": "ஐகார இறுதிப் பெயர்நிலை முன்னர்  வேற்றுமை ஆயின் வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If the standing word ending in 'ai'(ஐ) is a noun (and is followed by (k(க), c(ச), t (த)or p(ப), (k(க), c(ச), t (த)or p(ப)is respectively inserted after it."
            }
          },
          {
            "paadal": "சுட்டு முதல் இறுதி உருபு இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If the standing word ends in ai(ஐ)  and commences with a demonstrative root, the Canti (சந்தி) is the same as that when it is followed by a case-suffix (i.e.) it takes the increment Vaṟṟu(வற்று)  after it."
            }
          },
          {
            "paadal": "விசைமரக் கிளவியும் ஞெமையும் நமையும்  ஆ முப் பெயரும் சேமர இயல.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"if the standing words are vicai(விசை), Ñemai (ஞெமை) and namai(நமை), all denoting trees, the Canti (சந்தி) is the same as that when it is cē (சே) denoting a tree."
            }
          },
          {
            "paadal": "பனையும் அரையும் ஆவிரைக் கிளவியும்  நினையும் காலை அம்மொடு சிவணும்  ஐ என் இறுதி அரை வரைந்து கெடுமே  மெய் அவண் ஒழிய என்மனார் புலவர். ",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"Learned men say that, if the standing word is paṉai(பனை), aria(அரை) or āvirai(ஆவிரை), it takes in Canti (சந்தி) the increment 'am(அம்)' and in the case of paṉai(பனை), and āvirai(ஆவிரை),, their final ai(ஐ) is also dropped."
            }
          },
          {
            "paadal": "பனையின் முன்னர் அட்டு வரு காலை  நிலை இன்று ஆகும் ஐ என் உயிரே  ஆகாரம் வருதல் ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If paṉai(பனை) and attu(அத்து) are respectively the standing word and the coming word, ā(ஆ) is substituted for ai(ஐ)."
            }
          },
          {
            "paadal": "கொடி முன் வரினே ஐ அவண் நிற்ப  கடி நிலை இன்றே வல்லெழுத்து மிகுதி.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If the standing word paṉai(பனை)is followed by the word koṭi(கொடி), ai(ஐ) is not dropped and none prevents the insertion of the voiceless consonant (k(க)) between them."
            }
          },
          {
            "paadal": "திங்களும் நாளும் முந்து கிளந்தன்ன.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"If the standing word ending in ai(ஐ)  is the name of a month or a star, the Canti (சந்தி) is the same as that mentioned before (i.e.) in sutras 248 & 249."
            }
          },
          {
            "paadal": "மழை என் கிளவி வளி இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"The standing word maḻai(மழை) behaves in Canti (சந்தி) in the same way as the word vaḷi (வளி)."
            }
          },
          {
            "paadal": "செய்யுள் மருங்கின் வேட்கை என்னும்  ஐ என் இறுதி அவா முன் வரினே  மெய்யொடும் கெடுதல் என்மனார் புலவர்  டகாரம் ணகாரம் ஆதல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"/e (எ)/ ending words",  
              "paadal_meaning":"Learned men say that, in poetry, if the standing word is vēṭkai(வேட்கை) and the coming word is avā(அவா), ai(ஐ) with the preceding (k(க)) is dropped and ṭ(ட்) is changed to ṇ(ண்)."
            }
          },
          {
            "paadal": "ஓகார இறுதி ஏகார இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"The change in (non-case-relation) Canti (சந்தி) when the standing word ends in Ō (ஓ) is the same as that when it ends in ē(ஏ)."
            }
          },
          {
            "paadal": "மாறு கொள் எச்சமும் வினாவும் ஐயமும்  கூறிய வல்லெழுத்து இயற்கை ஆகும். ",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"There is no change in Canti (சந்தி) if the standing word ends in Ō(ஓ) denoting negation, question or doubt."
            }
          },
          {
            "paadal": "ஒழிந்ததன் நிலையும் மொழிந்தவற்று இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"The same is the case when Ō(ஓ) is Oḻiyicai (i.e.) suggests something that is left out."
            }
          },
          {
            "paadal": "வேற்றுமைக்கண்ணும் அதன் ஓரற்றே  ஒகரம் வருதல் ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"The same is the case in case-relation Canti (சந்தி) when the standing word ends in Ō(ஓ)  as when it ends in ē(ஏ). (i.e.) a voicless consonant is inserted and O(ஒ) follows Ō(ஓ)."
            }
          },
          {
            "paadal": "இல்லொடு கிளப்பின் இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"If the word ending in Ō(ஓ) (kŌ(கோ)) is followed by the word il(இல்), there is no change in Canti (சந்தி), (i.e.) o(ஒ) is not inserted."
            }
          },
          {
            "paadal": "உருபு இயல் நிலையும் மொழியுமார் உளவே  ஆவயின் வல்லெழுத்து இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"The /Ō (ஓ) / ending words",  
              "paadal_meaning":"There are standing words ending in Ō(ஓ) which, when they are followed by other words behave in the same way as when they are followed by case-suffixes (i.e) they take the increment Oṉ (ஒன்) after them). In such cases the following voiceless consonant is not doubled."
            }
          },
          {
            "paadal": "ஔகார இறுதிப் பெயர்நிலை முன்னர்  அல்வழியானும் வேற்றுமைக்கண்ணும்  வல்லெழுத்து மிகுதல் வரை நிலை இன்றே  அவ் இரு ஈற்றும் உகரம் வருதல்  செவ்விது என்ப சிறந்திசினோரே.",
            "vilakkam":
            {
              "paadal_category":"/au (ஔ)/- ending words",  
              "paadal_meaning":"None prevents the insertion of (k(க), c(ச), t (த)or p(ப), between the standing word ending in au(ஔ) and the coming word commencing with (k(க), c(ச), t (த)or p(ப), both in non-case-relation Canti (சந்தி) and in case-relation Canti (சந்தி). Great men opine that it is preferable to insert u(உ) immediately after an(அந்)."
            }
          }
        ]
      },
      {
        "iyal_name": "புள்ளிமயங்கியல்",
        "iyal_eng":"Consonant Coalescence",
        "noorpa": [
          {
            "paadal": "ஞகாரை ஒற்றிய தொழிற்பெயர் முன்னர்  அல்லது கிளப்பினும் வேற்றுமைக்கண்ணும்  வல்லெழுத்து இயையின் அவ் எழுத்து மிகுமே  உகரம் வருதல் ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"ñ (ஞ) ending Words",  
              "paadal_meaning":"If the standing word is a verbal noun ending in ñ (ஞ) and the coming word commences with a voiceless consonant, u (உ) followed by the respective voiceless consonant is inserted between them in case-relation sandhi."
            }
          },
          {
            "paadal": "ஞ ந ம வ இயையினும் உகரம் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ñ (ஞ) ending Words",  
              "paadal_meaning":"u (உ)  alone is inserted when the coming word commences with ñ (ஞ), n (ந), m (ம)  or v (வ)."
            }
          },
          {
            "paadal": "நகர இறுதியும் அதன் ஓரற்றே.",
            "vilakkam":
            {
              "paadal_category":"n (ந) ending Words",  
              "paadal_meaning":"The same is the case when the standing word ends in n (ந) (as when it ends in ñ (ஞ))."
            }
          },
          {
            "paadal": "வேற்றுமைக்கு உக் கெட அகரம் நிலையும். ",
            "vilakkam":
            {
              "paadal_category":"n (ந) ending Words",  
              "paadal_meaning":"In case-relation sandhi a (அ) is inserted instead of u (உ)."
            }
          },
          {
            "paadal": "வெரிந் என் இறுதி முழுதும் கெடுவழி  வரும் இடன் உடைத்தே மெல்லெழுத்து இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"n (ந) ending Words",  
              "paadal_meaning":"If verin (வெரிந்) is the standing word and is followed by a word commencing with k (க), c (ச), t (த) or p (ப), the corresponding nasal is inserted between them in such cases where n (ந) is dropped."
            }
          },
          {
            "paadal": "ஆவயின் வல்லெழுத்து மிகுதலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"n (ந) ending Words",  
              "paadal_meaning":"The corresponding voiceless consonant also is inserted in the above cases."
            }
          },
          {
            "paadal": "ணகார இறுதி வல்லெழுத்து இயையின்  டகாரம் ஆகும் வேற்றுமைப் பொருட்கே.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"If the standing word ends in ṇ (ண்) and the coming word commences with a voiceless consonant ( k (க), c (ச), t (த) or p (ப) ), ṇ (ண) is changed to ṭ (ட) in case-relation sandhi."
            }
          },
          {
            "paadal": "ஆணும் பெண்ணும் அஃறிணை இயற்கை.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"The words āṇ (ஆண்) and peṇ (பெண்) behave in the same way in sandhi as aḵṟiṇai(அஃறிணை) words (i.e.) there is no change."
            }
          },
          {
            "paadal": "ஆண்மரக் கிளவி அரைமர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"The word  āṇ (ஆண்) denoting a tree is of the same nature as the word arai (அரை) denoting a tree."
            }
          },
          {
            "paadal": "விண் என வரூஉம் காயப் பெயர்வயின்  உண்மையும் உரித்தே அத்து என் சாரியை  செய்யுள் மருங்கின் தொழில் வரு காலை.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"If the word viṇ (விண்) that denotes space is the standing word and if it is followed by a verb, the increment attu (அத்து) is also inserted in poetry."
            }
          },
          {
            "paadal": "தொழிற்பெயர் எல்லாம் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"All verbal nouns (ending in ṇ (ண்)) are of the same nature (as those ending in ñ (ஞ்)) (i. e.) if they are followed by words commencing with a voiceless consonant, u (உ) followed by the same voiceless consonant is inserted and if they are followed by words commencing with ñ (ஞ), n (ந), m (ம) or v (வ), u (உ) alone is inserted."
            }
          },
          {
            "paadal": "கிளைப்பெயர் எல்லாம் கொளத் திரிபு இலவே.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"If words ending in ṇ (ண) and denoting groups are standing words, there is, in general, no change in sandhi."
            }
          },
          {
            "paadal": "வேற்றுமை அல்வழி எண் என் உணவுப் பெயர்  வேற்றுமை இயற்கை நிலையலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"The standing word en denoting food is sometimes of the same nature in non-case-relation sandhi as in case-relation sandhi, (i.e.) ṇ (ண) is sometimes changed to ṭ (ட)  if the coming word commences with a voiceless consonant."
            }
          },
          {
            "paadal": "முரண் என் தொழிற்பெயர் முதல் இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ṇ (ண) ending Words",  
              "paadal_meaning":"The change in sandhi when the verbal noun muraṇ (முரண்) is the standing word is the same as is mentioned before (i. e.) in sūtra(சூத்திர) 148 [iyal(இயல்) 5 padal(படல்) 5] and 303 [iyal(இயல்) 8 padal(படல்) 7]."
            }
          },
          {
            "paadal": "மகர இறுதி வேற்றுமை ஆயின்  துவரக் கெட்டு வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If the standing word ends in m (ம) and if the coming word commences with a voiceless, consonant, m (ம) is dropped and the same voiceless consonant is substituted for it."
            }
          },
          {
            "paadal": "அகர ஆகாரம் வரூஉம் காலை  ஈற்றுமிசை அகரம் நீடலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If the coming words commence with a (அ) or ā (ஆ), the a (அ) preceding the final m (ம) of the standing words is optionally lengthened (in case-relation sandhi)."
            }
          },
          {
            "paadal": "மெல்லெழுத்து உறழும் மொழியுமார் உளவே  செல் வழி அறிதல் வழக்கத்தான.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"There are words ending in m (ம) after which corresponding nasal also is inserted instead of voiceless consonant in case-relation sandhi when they arc followed by words beginning with a voiceless consonant. Such words must be found out from usage."
            }
          },
          {
            "paadal": "இல்லம் மரப்பெயர் விசைமர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"The word illam (இல்லம்) denoting a tree is of the same nature as vicai (விசை) denoting a tree."
            }
          },
          {
            "paadal": "அல்வழி எல்லாம் மெல்லெழுத்து ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"M(ம) is changed to the nasal corresponding to the succeeding voiceless consonant in non-case-relation sandhi."
            }
          },
          {
            "paadal": "அகம் என் கிளவிக்குக் கை முன் வரினே  முதல்நிலை ஒழிய முன்னவை கெடுதலும்  வரை நிலை இன்றே ஆசிரியர்க்க  மெல்லெழுத்து மிகுதல் ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":" If akam(அகம்) is the standing word and kai(கை) |the coming word, ham of akam(அகம்) is optionally dropped in the opinion of revered elders, when  ṅ(ங)  is inserted before kai(கை)."
            }
          },
          {
            "paadal": "இலம் என் கிளவிக்குப் படு வரு காலை  நிலையலும் உரித்தே செய்யுளான.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If ilam (இலம்) is followed by paṭu (படு), m (ம) is also retained in poetry. "
            }
          },
          {
            "paadal": "அத்தொடு சிவணும் ஆயிரத்து இறுதி  ஒத்த எண்ணு முன் வரு காலை.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If the word āyiram (ஆயிரம்) is followed by a suitable word denoting number, the increment attā (அட்டா) is inserted between them (after m (ம) is dropped)."
            }
          },
          {
            "paadal": "அடையொடு தோன்றினும் அதன் ஓரற்றே..",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"The same is the case even if the word āyiram (ஆயிரம்) is preceded by a qualifying number."
            }
          },
          {
            "paadal": "அளவும் நிறையும் வேற்றுமை இயல. ",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If āyiram (ஆயிரம்) is followed by a word denoting measure or weight, the change in sandhi as the same is in case-relation sandhi."
            }
          },
          {
            "paadal": "படர்க்கைப் பெயரும் முன்னிலைப் பெயரும்  தொடக்கம் குறுகும் பெயர்நிலைக் கிளவியும்  வேற்றுமை ஆயின் உருபு இயல் நிலையும்  மெல்லெழுத்து மிகுதல் ஆவயினான.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If the third personal pronoun (eliārum)(எலியாரும்), the second personal pronoun (ellīrum)(எல்லாம்), and the pronouns that are shortened (tām (தாம்), nām (நாம்) and yām (யாம்)) are standing words, they undergo the same change in case-relation sandhi as when they are followed by case-suflixes, when m (ம) is dropped and a nasal corresponding to the following consonant is inserted."
            }
            
          },
          {
            "paadal": "அல்லது கிளப்பின் இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"There is no change in non-case-relation sandhi."
            }
          },
          {
            "paadal": "அல்லது கிளப்பினும் வேற்றுமைக்கண்ணும்  எல்லாம் எனும் பெயர் உருபு இயல் நிலையும்  வேற்றுமை அல் வழிச் சாரியை நிலையாது.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If ellām (எல்லாம்) is the standing word, the change in both non-case relation sandhi and case-relation sandhi is the same as when it is followed by case suffixes, except that the increment is not inserted in the case of non-case-relalion sandhi."
            }
          },
          {
            "paadal": "மெல்லெழுத்து மிகினும் மானம் இல்லை.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"There is no harm if a nasal is inserted instead of a voiceless consonant (in the above case)."
            }
          },
          {
            "paadal": "உயர்திணை ஆயின் உருபு இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"If ellām (எல்லாம்) is uyartiṇai (உயர்திணை), the sandhi is the same as when it is followed by a case-suffix."
            }
          },
          {
            "paadal": "நும் என் ஒரு பெயர் மெல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":" If num is the standing word, a nasal is inserted (instead of a voiceless consonant after the dropping of m(ம) in case-relation sandhi)."
            }
          },
          {
            "paadal": "அல்லதன் மருங்கின் சொல்லும் காலை  உக் கெட நின்ற மெய்வயின் ஈ வர  இ இடை நிலைஇ ஈறு கெட ரகரம்  நிற்றல் வேண்டும் புள்ளியொடு புணர்ந்தே  அப் பால் மொழிவயின் இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":" In non-case-relation sandhi , u(உ) of num is replaced by ī(ஈ), i(இ) is inserted after ī(ஈ) and, the final m (ம) is replaced by  r(ர), but no change takes place between the standing word and the coming word."
            }
          },
          {
            "paadal": "தொழிற்பெயர் எல்லாம் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"All verbal nouns (ending in m (ம)) are of the same nature as those (ending in ñ(ஞ))."
            }
          },
          {
            "paadal": "ஈமும் கம்மும் உரும் என் கிளவியும்  ஆ முப் பெயரும் அவற்று ஓரன்ன.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"The three nouns īm (ஈமும்) ,kam (கம்) and urum (உரும்) are of the same nature as the verbal nouns."
            }
          },
          {
            "paadal": "வேற்றுமை ஆயின் ஏனை இரண்டும்  தோற்றம் வேண்டும் அக்கு என் சாரியை.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"The first two take the increment akkū (அக்கு) in case-relation sandhi."
            }
          },
          {
            "paadal": "வகாரம் மிசையும் மகாரம் குறுகும்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"m (ம)followed by v (வ) is shortened (to quarter of a mātrā(மாத்திரை))"
            }
          },
          {
            "paadal": "நாட்பெயர்க் கிளவி மேல் கிளந்தன்ன  அத்தும் ஆன்மிசை வரை நிலை இன்றே  ஒற்று மெய் கெடுதல் என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"m (ம) final Words",  
              "paadal_meaning":"Learned men say that words ending in m (ம) and denoting star take the increment āṉ (ஆன்) as mentioned before (in sūtra 248), drop their final  m(ம) and take the increment attū (அவசரம்) before āṉ (ஆன்), when they are standing words."
            }
          },
          {
            "paadal": "னகார இறுதி வல்லெழுத்து இயையின்  றகாரம் ஆகும் வேற்றுமைப் பொருட்கே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"In case-relation sandhi the final ṉ(ன்) of standing words is changed to ṟ(ற) if the coming words commence with a voiceless consonant."
            }
          },
          {
            "paadal": "மன்னும் சின்னும் ஆனும் ஈனும்  பின்னும் முன்னும் வினையெஞ்சு கிளவியும்  அன்ன இயல என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"Learned men say that the same is the case in sandhi when the words maṉ(மன்), ciṉ(சின்),āṉ(ஆன்),īṉ(ஈன்), piṉ(பின்), muṉ(முன்) and verbal participles are standing words. "
            }
          },
          {
            "paadal": "சுட்டு முதல் வயினும் எகரம் முதல் வயினும்  அப் பண்பு நிலையும் இயற்கைய என்ப.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"It is said that the same is the case in sandhi when the word vayiṉ (வயின்) preceded by a demonstrative root or e(எ) is the standing word. "
            }
          },
          {
            "paadal": "குயின் என் கிளவி இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"There is no change in sandhi if kuyiṉ (குயின்) is the standing word."
            }
          },
          {
            "paadal": "எகின் மரம் ஆயின் ஆண்மர இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"Ekiṉ (எகின்) denoting a tree is of the same nature as āṉ (ஆன்) denoting a tree."
            }
          },
          {
            "paadal": "ஏனை எகினே அகரம் வருமே  வல்லெழுத்து இயற்கை மிகுதல் வேண்டும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"Ekiṉ (எகின்) denoting other than a tree takes 'a' (அ) after it and a voiceless consonant is inserted after 'a' (அ)."
            }
          },
          {
            "paadal": "கிளைப்பெயர் எல்லாம் கிளைப்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":" Words ending in ṉ(ன்) and denoting groups are of the same nalure as those (ending in ṉ(ன்)) and denoting groups."
            }
          },
          {
            "paadal": "மீன் என் கிளவி வல்லெழுத்து உறழ்வே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If mīṉ (மீன்) is the standing word, ṉ(ன்) is optionally changed to ṟ (ற்)."
            }
          },
          {
            "paadal": "தேன் என் கிளவி வல்லெழுத்து இயையின்  மேல் நிலை ஒத்தலும் வல்லெழுத்து மிகுதலும்  ஆ முறை இரண்டும் உரிமையும் உடைத்தே  வல்லெழுத்து மிகு வழி இறுதி இல்லை.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":" If tēṉ (தேன்) is followed by a word commencing with a voiceless consonant, ṉ (ன்) is optionally changed to ṟ (ற்) as before (in the case of mīṉ (மீன்)) or ṉ (ன்) is dropped and the following voiceless consonant is doubled."
            }
          },
          {
            "paadal": "மெல்லெழுத்து மிகினும் மானம் இல்லை.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"There is no harm if a nasal is inserted (instead of a voiceless consonant)."
            }
          },
          {
            "paadal": "மெல்லெழுத்து இயையின் இறுதியொடு உறழும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If tēṉ (தேன்) is followed by a word commencing with a nasal, ṉ (ன்) is optionally dropped."
            }
          },
          {
            "paadal": "இறாஅல் தோற்றம் இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If iṟāl (இறால்) follows tēṉ (தேன்), there is no change in sandhi."
            }
          },
          {
            "paadal": "ஒற்று மிகு தகரமொடு நிற்றலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"It is possible (for the same iṟāl (இறால்)) to be preceded by tt (தத்), (in which case the final ṉ (ன்) of tēṉ (தேன்) is dropped)."
            }
          },

          {
            "paadal": "மின்னும் பின்னும் பன்னும் கன்னும்  அந் நாற் சொல்லும் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"The four words miṉ (மீன்), piṉ (பின்), paṉ (பன்) and kaṉ (கன்) are of the same nature as verbal nouns."
            }
          },
          {
            "paadal": "வேற்றுமை ஆயின் ஏனை எகினொடு  தோற்றம் ஒக்கும் கன் என் கிளவி.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"In case-relation sandhi the word kaṉ (கன்) resembles ekiṉ (எகின்) not denoting tree."
            }
          },
          {
            "paadal": "இயற்பெயர் முன்னர்த் தந்தை முறை வரின்  முதற்கண் மெய் கெட அகரம் நிலையும்  மெய் ஒழித்து அன் கெடும் அவ் இயற்பெயரே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":" If proper names ending in ṉ (ன்) are followed by the word tantai (தந்தை) denoting father, the aṉ (அன்) of the standing word and the initial consonant of the coming word are dropped."
            }
          },
          {
            "paadal": "ஆதனும் பூதனும் கூறிய இயல்பொடு  பெயர் ஒற்று அகரம் துவரக் கெடுமே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If ātaṉ (ஆதன்) and pūtaṉ (பூதம்) are standing words and the coming word is tantai (தந்தை) denoting father, the change in sandhi is the same as before with the addition that the final consonant and the initial vowel of the standing word and the coming word respectively are also dropped; (i.e.) taṉ (தன்) of ātaṉ (ஆதன்) and pūtaṉ (பூதம்) and ta (த) of tantai (தந்தை) are dropped."
            }
          },
          {
            "paadal": "சிறப்பொடு வரு வழி இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If such words are preceded by adjectives there is no change (i.e.) no dropping of letters."
            }
          },
          {
            "paadal": "அப் பெயர் மெய் ஒழித்து அன் கெடு வழியே  நிற்றலும் உரித்தே அம் என் சாரியை  மக்கள் முறை தொகூஉம் மருங்கினான.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"Aṉ (அன்) is dropped in such words (cāttaṉ (சாத்தன்), koṟṟaṉ (கொற்றன்) etc.) and the increment am (அம்) takes its place when the word denoting son is understood between the standing word and the coming word. "
            }
          },
          {
            "paadal": "தானும் பேனும் கோனும் என்னும்  ஆ முறை இயற்பெயர் திரிபு இடன் இலவே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"There is no dropping off if the words tāṉ (தான்), pēṉ (பேன்) and kōē (கோயே) are either followed by the word tantai (தந்தை) or have the word denoting son understood after them."
            }
          },
          {
            "paadal": "தான் யான் எனும் பெயர் உருபு இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If tāṉ (தான்) and yāṉ (யான்) are standing words, the change in sandhi is the same as when they are followed by case-suffixes."
            }
          },
          {
            "paadal": "வேற்றுமை அல் வழிக் குறுகலும் திரிதலும்  தோற்றம் இல்லை என்மனார் புலவர்.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"Learned men say that there is no change in non-case-relaiion sandhi."
            }
          },
          {
            "paadal": "அழன் என் இறுதி கெட வல்லெழுத்து மிகுமே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"If aḻaṉ (அழன்) is the standing word, the final ṉ (ன்) is dropped and the initial voiceless consonant of the coming word is doubled."
            }
          },
          {
            "paadal": "முன் என் கிளவி முன்னர்த் தோன்றும்  இல் என் கிளவிமிசை றகரம் ஒற்றல்  தொல் இயல் மருங்கின் மரீஇய மரபே.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"It is an old usuage that ṟ (ற்) is inserted between mun and il (இல்) in sandhi."
            }
          },
          {
            "paadal": "பொன் என் கிளவி ஈறு கெட முறையின்  முன்னர்த் தோன்றும் லகார மகாரம்  செய்யுள் மருங்கின் தொடர் இயலான.",
            "vilakkam":
            {
              "paadal_category":"ṉ (ன்) ending Words",  
              "paadal_meaning":"The final ṉ (ன்) of poṉ (பொன்) is dropped and lam is inserted after it in poetry whenever it is so needed."
            }
          },
          {
            "paadal": "யகர இறுதி வேற்றுமைப் பொருள்வயின்  வல்லெழுத்து இயையின் அவ் எழுத்து மிகுமே.",
            "vilakkam": 
            {
              "paadal_category":"y (ய) ending Words",  
              "paadal_meaning":"If a word l(ல) ending in y(ய)  is followed by a word commencing with a voiceless consonant, this consonant is doubled in case-relation sandhi."
            }
          },
          {
            "paadal": "தாய் என் கிளவி இயற்கை ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"y (ய) ending Words",  
              "paadal_meaning":"There is no change in sandhi if the standing word is tāy (தாய்)."
            }
          },
          {
            "paadal": "மகன் வினை கிளப்பின் முதல் நிலை இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"y (ய) ending Words",  
              "paadal_meaning":"If the above word tāy (தாய்) is preceded by makaṉ (மகன்) and followed by a word denoting the action of makaṉ (மகன்), the change in sandhi is what has been said at first (i.e.) sūtra 358."
            }
          },
          {
            "paadal": "மெல்லெழுத்து உறழும் மொழியுமார் உளவே.",
            "vilakkam":
            {
              "paadal_category":"y (ய) ending Words",  
              "paadal_meaning":"There are words after which nasals too are optionally inserted in place of voiceless consonants."
            }
          },
          {
            "paadal": "அல்வழி எல்லாம் இயல்பு என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"y (ய) ending Words",  
              "paadal_meaning":"It is said that there is no change in non-case-relation sandhi."
            }
          },
          {
            "paadal": "ரகார இறுதி யகார இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"r (ர) ending Words",  
              "paadal_meaning":" The change in case-relation sandhi when the standing word ends in r(ர) is the same as that when it ends in y(ய)."
            }
          },
          {
            "paadal": "ஆரும் வெதிரும் சாரும் பீரும்  மெல்லெழுத்து மிகுதல் மெய் பெறத் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"r (ர) ending Words",  
              "paadal_meaning":"Nasal is inserted after the standing words ār(ஆர்), vetir(வெதிர்), cār(சார்) and pīr(பீர்) (if the coming word commences with a voiceless consonant)."
            }
          },
          {
            "paadal": "சார் என் கிளவி காழ்வயின் வலிக்கும்.",
            "vilakkam":
            {
              "paadal_category":"r (ர) ending Words",  
              "paadal_meaning":"If cār (சார்)  is followed by kāl (காழ்), the voiceless k (க்) is inserted between them."
            }
          },
          {
            "paadal": "பீர் என் கிளவி அம்மொடும் சிவணும்.",
            "vilakkam":
            {
              "paadal_category":"r (ர) ending Words",  
              "paadal_meaning":"Pīr (பீர்) may take the increment am also after it."
            }
          },
          {
            "paadal": "லகார இறுதி னகார இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"The change in case-relation sandhi when the standing word ends in l (ல) , is the same as that when it ends in ṉ (ன)."
            }
          },
          {
            "paadal": "மெல்லெழுத்து இயையின் னகாரம் ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":" L (ல) is changed to ṉ (ன) if the coming word commences with a nasal"
            }
          },
          {
            "paadal": "அல்வழி எல்லாம் உறழ் என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"L (ல) is optionally changed to ṟ (ற) in non-case-relation sandhi"
            }
          },
          {
            "paadal": "தகரம் வரு வழி ஆய்தம் நிலையலும்  புகர் இன்று என்மனார் புலமையோரே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"Learned men say that there is no harm even if l (ல) is changed to ஃ (ḵ) if the coming word commences with t (த)."
            }
          },
          {
            "paadal": "நெடியதன் இறுதி இயல்புமார் உளவே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"If the vowel preceding l (ல) is long, there are cases when there is no change in sandhi."
            }
          },
          {
            "paadal": "நெல்லும் செல்லும் கொல்லும் சொல்லும்  அல்லது கிளப்பினும் வேற்றுமை இயல.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"If the four words nel (நெல்), cel (செல்), kol (கோல்) and col are standing words, l (ல), even in non-case-relation sandhi is changed to ṟ (ற) as in case-relation sandhi (when they are followed by words commencing with a voiceless consonant)."
            }
          },
          {
            "paadal": "இல் என் கிளவி இன்மை செப்பின்  வல்லெழுத்து மிகுதலும் ஐ இடை வருதலும்  இயற்கை ஆதலும் ஆகாரம் வருதலும்  கொளத் தகு மரபின் ஆகு இடன் உடைத்தே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"If the word il denoting negation is the standing word (and if it is followed by a word commencing with a voiceless consonant), the same consonant is doubled, ai (ஐ) or ā (ஆ) is inserted or there is no change."
            }
          },
          {
            "paadal": "வல் என் கிளவி தொழிற்பெயர் இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"The word val takes the same change in sandhi as verbal nouns (ending in ñ (ஞ))."
            }
          },
          {
            "paadal": "நாயும் பலகையும் வரூஉம் காலை  ஆவயின் உகரம் கெடுதலும் உரித்தே  உகரம் கெடு வழி அகரம் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"If val is followed by nāy (இல்லை) or palakai (பலகை), u (உ) is sometimes dropped when a takes its place."
            }
          },
          {
            "paadal": "பூல் வேல் என்றா ஆல் என் கிளவியொடு  ஆ முப் பெயர்க்கும் அம் இடை வருமே.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":" Pūl (பூல்), vūl (வள்ளல்) and aal (ஆல்) take the increment 'am' after them (in case- relation sandhi)."
            }
          },
          {
            "paadal": "தொழிற்பெயர் எல்லாம் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":"All verbal nouns ending in l (ல) have the same change in sandhi as those ending in n (ந)."
            }
          },
          {
            "paadal": "வெயில் என் கிளவி மழை இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"l (ல) ending Terms",  
              "paadal_meaning":" The change in sandhi when veyil (வெயில்) is the standing word is the same as when it is maḻai (மழை)."
            }
          },
          {
            "paadal": "சுட்டு முதல் ஆகிய வகர இறுதி  முற்படக் கிளந்த உருபு இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"v (வ) ending Terms",  
              "paadal_meaning":"Words ending in v (வ) and commencing with demonstrative roots have the same change in sandhi as when they are followed by case-suffixes."
            }
          },
          {
            "paadal": "வேற்றுமை அல்வழி ஆய்தம் ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"v (வ) ending Terms",  
              "paadal_meaning":" V (வ) is changed to ஃ (ḵ) in non-case-relation sandhi (if it is followed by a voiceless consonant)."
            }
          },
          {
            "paadal": "மெல்லெழுத்து இயையின் அவ் எழுத்து ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"v (வ) ending Terms",  
              "paadal_meaning":" V (வ) is changed to the same nasal as the initial nasal of the coming word if it so happens."
            }
          },
          {
            "paadal": "ஏனவை புணரின் இயல்பு என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"v (வ) ending Terms",  
              "paadal_meaning":" There is no change in sandhi if v (வ) is followed by others."
            }
          },
          {
            "paadal": "ஏனை வகரம் தொழிற்பெயர் இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"v (வ) ending Terms",  
              "paadal_meaning":"The word ending in v (வ) other than those mentioned before [(i.e.) the word tev] takes the same change in sandhi as verbal nouns ending in n (ந)."
            }
          },
          {
            "paadal": "ழகார இறுதி ரகார இயற்றே.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"The change in case-relation sandhi of Words ending in ḻ (ழ) is the same as those ending in r (ர)."
            }
          },
          {
            "paadal": "தாழ் என் கிளவி கோலொடு புணரின்  அக்கு இடை வருதல் உரித்தும் ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":" If tāḻ (தாழ்) is followed by kōl (கோல்), the increment akku (அக்கு) may also be inserted between them."
            }
          },
          {
            "paadal": "தமிழ் என் கிளவியும் அதன் ஓரற்றே.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"The word tamiḻ (தமிழ்) also may similarly take the increment akku (அக்கு) after it."
            }
          },
          {
            "paadal": "குமிழ் என் கிளவி மரப்பெயர் ஆயின்  பீர் என் கிளவியொடு ஓர் இயற்று ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":" Kumiḻ (குமிழ்) denoting a tree takes the same change in sandhi as pīr (பீர்)"
            }
          },
          {
            "paadal": "பாழ் என் கிளவி மெல்லெழுத்து உறழ்வே.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"The word pāḻ (பாழ்) takes after it also a nasal (corresponding to the following voiceless consonant)"
            }
          },
          {
            "paadal": "ஏழ் என் கிளவி உருபு இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":" The change in sandhi when ēḻ (ஏழ்) is the standing word is the same as when it is followed by case-suffixes."
            }
          },
          {
            "paadal": "அளவும் நிறையும் எண்ணும் வரு வழி  நெடு முதல் குறுகலும் உகரம் வருதலும்  கடி நிலை இன்றே ஆசிரியர்க்க.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":" Revered elders opine that when ēḻ (ஏழ்) is followed by words denoting measure, weight and number, ē (ஏ) is shortened to e (எ) and u (உ) is inserted after ḻ (ழ)."
            }
          },
          {
            "paadal": "பத்து என் கிளவி ஒற்று இடை கெடு வழி  நிற்றல் வேண்டும் ஆய்தப் புள்ளி.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"When the word pattu follows ēḻ (ஏழில்), t (த) is dropped and ḵ (ஃ) takes its place."
            }
          },
          {
            "paadal": "ஆயிரம் வரு வழி உகரம் கெடுமே.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":" When āyiram (ஆயிரம்) follows ēḻ (ஏழில்), u (உ) is dropped."
            }
          },
          {
            "paadal": "நூறு ஊர்ந்து வரூஉம் ஆயிரக் கிளவிக்குக்  கூறிய நெடு முதல் குறுக்கம் இன்றே.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"If nurayiram (நூறு - ஆயிரம்) follows ēḻ (ஏழில்), ē (ஏ) is not shortened to e (எ)."
            }
          },
          {
            "paadal": "ஐ அம் பல் என வரூஉம் இறுதி  அல் பெயர் எண்ணும் ஆயியல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"The same is the case when words ending in ai (ஐ), am (அம்) and pal (பல்) and denoting number follow ēḻ (ஏழில்)"
            }
          },
          {
            "paadal": "உயிர் முன் வரினும் ஆயியல் திரியாது.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"The same is the case when el is followed by a word commencing with a vowel."
            }
          },
          {
            "paadal": "கீழ் என் கிளவி உறழத் தோன்றும்.",
            "vilakkam":
            {
              "paadal_category":"ḻ (ழ) ending Terms",  
              "paadal_meaning":"If kiḻ (கீழ்) is followed by a word commencing with a voiceless consonant, the latter is optionally doubled."
            }
          },
          {
            "paadal": "ளகார இறுதி ணகார இயற்றே.",
            "vilakkam": 
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":" The change in sandhi when the standing word ends in ḷ (ள) is the same when it ends in ṇ (ண)."
            }
          },
          {
            "paadal": "மெல்லெழுத்து இயையின் ணகாரம் ஆகும்.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"The final ḷ (ள) is changed to ṇ (ண) if the coming word commences with a nasal."
            }
          },
          {
            "paadal": "அல்வழி எல்லாம் உறழ் என மொழிப.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"It is said that ḷ (ள) optionally changes to ṭ (ட) in non-case relation sandhi."
            }
          },
          {
            "paadal": "ஆய்தம் நிலையலும் வரை நிலை இன்றே  தகரம் வரூஉம் காலையான.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"None prevents the optional change of ḷ (ள) to ḵ (ஃ) if the coming word commences with t (த)."
            }
          },
          {
            "paadal": "நெடியதன் இறுதி இயல்பு ஆகுநவும்  வேற்றுமை அல் வழி வேற்றுமை நிலையலும்  போற்றல் வேண்டும் மொழியுமார் உளவே.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"There are words which have a long vowel preceding ḷ (ள) and have no change ip sandhi and also which have the same change in non-case-relation sandhi as in case-relation sandhi."
            }
          },
          {
            "paadal": "தொழிற்பெயர் எல்லாம் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"All verbal nouns ending in ḷ (ள) have the same change in sandhi as those ending in ñ (ஞ)."
            }
          },
          {
            "paadal": "இருள் என் கிளவி வெயில் இயல் நிலையும்.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"The standing word iruḷ (இருள்) has the same change in sandhi as the word veyil (வெயில்)."
            }
          },
          {
            "paadal": "புள்ளும் வள்ளும் தொழிற்பெயர் இயல.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"The words puḷ (புள்) and vaḷ (வள்) have the same change in sandhi as the verbal nouns ending in n (ந)."
            }
          },
          {
            "paadal": "மக்கள் என்னும் பெயர்ச்சொல் இறுதி  தக்கவழி அறிந்து வலித்தலும் உரித்தே.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"The standing word makkaḷ (மக்கள்) sometimes has ḷ (ள) changed to ṭ (ட) though it generally undergoes no change. "
            }
          },
          {
            "paadal": "உணரக் கூறிய புணர் இயல் மருங்கின்  கண்டு செயற்கு உரியவை கண்ணினர் கொளலே.",
            "vilakkam":
            {
              "paadal_category":"ḷ (ள) Final Words",  
              "paadal_meaning":"All the changes which the final consonant of the standing word undergoes and which are not mentioned in this chapter are to be learnt from usage and ought to be neglected."
            }
          }
        ]
      },
      {
        "iyal_name": "குற்றியலுகரப்புணரியல்",
        "iyal_eng":"Shortened /u/ - Coalescence",
        "noorpa": [
          {
            "paadal": "ஈர் எழுத்து ஒருமொழி உயிர்த்தொடர் இடைத்தொடர்  ஆய்தத் தொடர்மொழி வன்றொடர் மென்றொடர்  ஆயிரு மூன்றே உகரம் குறுகு இடன்.",
            "vilakkam":
          {
            "paadal_category":"Shortened /u/-ending Word-classes",
            "paadal_meaning":"There are only six kinds of words where u (உ) is found. They are īreḻuttorumoḻi(ஈரெழுத்தொருமொழி) or words like nāku(நாகு) or īṟu(ஈறு) made up two vowel-consonants, or of one long vowel and one vowel- consonant, Uyirttoṭarmoḻi(உயிர்த்தொடர்மொழி) or words like varaku(வரகு) or aracu(அரசு) having a vowel-consonant between the first vowel or vowel-consonant and the last vowel-consonant, Iṭaittoṭarmoḻi(இடைத்தொடர்மொழி) or words like teḷku(தெள்கு) or eḷḷu(எள்ளு) having a semi-vowel between the first vowel-consonant or vowel and the last vowel- consonant, āytattoṭarmoḻi(ஆய்தத்தொடர்மொழி) or words like  eஃku(எஃகு) or kaஃcu(கஃசு) having an āytam(ஆய்தம்) between the first vowel or vowel-consonant and last vowel-consonant, vaṉṟoṭarmoḻi(வன்றொடர்மொழி) or words like kokku(கொக்கு) or eṭṭu(எட்டு) having a voiceless consonan between the first vowel-consonant or vowel and the last vowel- consonant and meṉṟoṭarmoḻi(மென்றொடர்மொழி) or words like teṅku(தெங்கு) or eṅku(எங்கு) having a nasal between the first vowel consonant or vowel and the last vowel-consonant. "
          }
          },
          {
            "paadal": "அவற்றுள்,  ஈர் ஒற்றுத் தொடர்மொழி இடைத்தொடர் ஆகா.",
            "vilakkam": 
            {
                "paadal_category":"Shortened /u/-ending Word-classes",
                "paadal_meaning":"The word which has a semi-vowel following the initial vowel or vowel consonant and preceding a consonant other than the first part of the final vowel-consonant, cannot be regarded as Iṭaittoṭar(இடைத்தொடர்). "
            }
          },
          {
            "paadal": "அல்லது கிளப்பினும் வேற்றுமைக்கண்ணும்  எல்லா இறுதியும் உகரம் நிறையும்.",
            "vilakkam": 
            {
                "paadal_category":"Shortened /u/-ending Word-classes",
                "paadal_meaning":"Both in non-case-relation sandhi and in case-relation sandhi u(உ) appears at the end of the above six kinds of words."
            }
          },
          {
            "paadal": "வல்லொற்றுத் தொடர்மொழி வல்லெழுத்து வரு வழி  தொல்லை இயற்கை நிலையலும் உரித்தே.",
            "vilakkam": 
            {
                "paadal_category":"Shortened /u/-ending Word-classes",
                "paadal_meaning":"U(உ) at the end of valloṟṟuttoṭarmoḻi (வல்லொற்றுத்தொடர்மொழி) may remain as such if the coming word commences with a voiceless consonant."
            }
          },
          {
            "paadal": "யகரம் வரு வழி இகரம் குறுகும்  உகரக் கிளவி துவரத் தோன்றாது.",
            "vilakkam": 
            {
                "paadal_category":"Shortened /u/ Modified to Shortened /i/",
                "paadal_meaning":"If the coming word commences with y(ய), the final u(உ) of the standing word is replaced by i(இ). (the shortened i(இ)). "
            }
          },
          {
            "paadal": "ஈர் எழுத்து மொழியும் உயிர்த்தொடர் மொழியும்  வேற்றுமை ஆயின் ஒற்று இடை இனம் மிக  தோற்றம் வேண்டும் வல்லெழுத்து மிகுதி.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"In case-reation sandhi if īreḻuttornmoḻi(ஈரெழுத்தொருமொழி) or uyirttoṭarmoḻi (உயிர்த்தொடர் மொழி) is the standing word and the coming word commences with a voiceless consonant, the voiceless consonant that precedes u(உ) is doubled and another voiceless consonant similar to the initial member of the coming word is inserted after u(உ)."
            }
          },
          {
            "paadal": "ஒற்று இடை இனம் மிகா மொழியுமார் உளவே  அத் திறத்து இல்லை வல்லெழுத்து மிகலே.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"There are, among īreḻuttornmoḻi (ஈரெழுத்தொருமொழி) and uyirttoṭarmoḻi (உயிர்த்தொடர் மொழி), words which do not undergo the change mentioned in the previous sūtra, when they are standing words; nor is the voiceless consonant similar to the initial member of the coming word inserted after u(உ)."
            }
          },
          {
            "paadal": "இடையொற்றுத் தொடரும் ஆய்தத்தொடரும்  நடை ஆயியல என்மனார் புலவர்.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"When iṭaiyoṟṟuttoṭar (இடையொற்றுத்தொடர்) or āytattoṭar (ஆய்தத்தொடர்) is the standing word, the sandhi that takes place is the same as is mentioned in the previous sūtra."
            }
          },
          {
            "paadal": "வன்றொடர் மொழியும் மென்றொடர் மொழியும்  வந்த வல்லெழுத்து ஒற்று இடை மிகுமே  மெல்லொற்றுத் தொடர்மொழி மெல்லொற்று எல்லாம்  வல்லொற்று இறுதி கிளை ஒற்று ஆகும்.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"If u (உ) at the end of vaṉṟoṭarmoḻi (வன்றொடர்மொழி) or meṉṟoṭarmoḻi (மென்றொடர்மொழி) is followed by a word commencing with a voiceless consonant, the latter is doubled; and in the case of meṉṟoṭarmoḻi (மென்றொடர்மொழி) , the nasal within it is also replaced by the corresponding voiceless consonant. "
            }
          },
          {
            "paadal": "மரப்பெயர்க் கிளவிக்கு அம்மே சாரியை.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"(If the above-mentioned vaṉṟoṭarmoḻi (வன்றொடர்மொழி) or meṉṟoṭarmoḻi (மென்றொடர்மொழி)) is the name of a tree, the flexional increment  am (அம்) after is inserted after it. "
            }
          },
          {
            "paadal": "மெல்லொற்று வலியா மரப்பெயரும் உளவே.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning":"There are meṉṟoṭarmoḻi (மென்றொடர்மொழி) denoting trees which do not allow the nasals within them replaced by the corresponding voiceless consonants."
            }
          },
          {
            "paadal": "ஈர் எழுத்து மொழியும் வல்லொற்றுத் தொடரும்  அம் இடை வரற்கும் உரியவை உளவே  அம் மரபு ஒழுகும் மொழிவயினான.",
            "vilakkam": 
            {
                "paadal_category":"Case relation Coalescence",
                "paadal_meaning": "There are some in īreḻuttornmoḻi (ஈரெழுத்தொருமொழி) and valloṟṟuttoṭarmoḻi (வல்லொற்றுத்தொடர்மொழி) which take the flexional increment am (அம்) after them. Such words can be ascertained only from usage."
            }
          },
          {
            "paadal": "ஒற்று நிலை திரியாது அக்கொடு வரூஉம்  அக் கிளைமொழியும் உள என மொழிப.",
            "vilakkam": 
            {
                "paadal_category": "Case relation Coalescence",
                "paadal_meaning": "It is said that there are some (among meṉṟoṭarmoḻi (மென்றொடர்மொழி)) which do not have their nasals replaced by corresponding voiceless consonants, but take the flexional increment akku (அக்கு) after "
            }
          },
          {
            "paadal": "எண்ணுப்பெயர்க் கிளவி உருபு இயல் நிலையும்.",
            "vilakkam": 
            {
                "paadal_category": "Case relation Coalescence",
                "paadal_meaning": "Words (ending in u (உ)) and denoting number undergo the same change in sandhi (when they are followed by words) as when they are followed by case-suffixes (i.e), they take the flexional increment aṉ (அன்) after them."
            }
          },
          {
            "paadal": "வண்டும் பெண்டும் இன்னொடு சிவணும்.",
            "vilakkam": 
            {
                "paadal_category": "Case relation Coalescence",
                "paadal_meaning": "The words vaṇṭu (வண்டு) and peṇṭu (பெண்டு) take the increment iṉ (இன்) after them."
            }
          },
          {
            "paadal": "பெண்டு என் கிளவிக்கு அன்னும் வரையார்.",
            "vilakkam": 
            {
                "paadal_category": "Case relation Coalescence",
                "paadal_meaning": "No one prevents the word peṇṭu (பெண்டு) taking aṉ (அன்) also after it."
            }
          },
          {
            "paadal": "யாது என் இறுதியும் சுட்டு முதல் ஆகிய  ஆய்த இறுதியும் உருபு இயல் நிலையும்.",
            "vilakkam": 
            {
                "paadal_category": "Case relation Coalescence",
                "paadal_meaning": "The words yātu (யாது), aஃtu (ஆஃது), iஃtu (இஃது) and uஃtu (உஃது) undergo the same change in sandhi (when they are followed by words) as when they are followed by case suffixes (i.e.), the increment aṉ (அன்) is inserted after them."
            }
          },
          {
            "paadal": "முன் உயிர் வரும் இடத்து ஆய்தப் புள்ளி  மன்னல் வேண்டும் அல்வழியான.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "ḵ(ஃ) is not dropped in aஃtu (ஆஃது), iஃtu (இஃது) and uஃtu (உஃது) in non-case relation sandhi, if the coming word commences with a vowel. "
            }
          },
          {
            "paadal": "ஏனை முன் வரினே தான் நிலை இன்றே.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": " ḵ(ஃ) is dropped in such words if the coming Wofd does Hot commence with a vowel."
            }
          },
          {
            "paadal": "அல்லது கிளப்பின் எல்லா மொழியும்  சொல்லிய பண்பின் இயற்கை ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "In non-case-relation sandhi the changes in all classes of words ending in u (உ) are the same as those mentioned before."
            }
          },
          {
            "paadal": "வல்லொற்றுத் தொடர்மொழி வல்லெழுத்து மிகுமே.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "If valloṟṟuttoṭarmoḻi (வல்லொற்றுத்தொடர்மொழி) is followed by a voiceless consonant, the latter is doubled."
            }
          },
          {
            "paadal": "சுட்டுச் சினை நீடிய மென்றொடர் மொழியும்  யா வினா முதலிய மென்றொடர் மொழியும்  ஆயியல் திரியா வல்லெழுத்து இயற்கை.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "Such meṉṟoṭarmoḻi (மென்றொடர்மொழி) as commence wiih the lengthened form of demonstrative roots or as are words of interrogation and commence with yā (யா) are of the same nature in sandhi as valloṟṟuttoṭarmoḻi (வல்லொற்றுத்தொடர்மொழி) (if they are followed by a voiceless consonant) (*. e.), the voiceless consonant, is doubled."
            }
          },
          {
            "paadal": "யா வினா மொழியே இயல்பும் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "The interrogative words commencing with, yā (யா) may also remain without having the succeeding voiceless consonant doubled."
            }
          },
          {
            "paadal": "அந் நால் மொழியும் தம் நிலை திரியா",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "The above four (i.e., āṅku (ஆங்கு) , Īṅku (ஈங்கு) , ūṅku (ஊங்கு) and yāṅku (யாங்கு) ) do not have their nasals replaced by voiceless consonants."
            }
          },
          {
            "paadal": "உண்டு என் கிளவி உண்மை செப்பின்  முந்தை இறுதி மெய்யொடும் கெடுதலும்  மேல் நிலை ஒற்றே ளகாரம் ஆதலும்  ஆ முறை இரண்டும் உரிமையும் உடைத்தே  வல்லெழுத்து வரூஉம் காலையான.",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "If the word Uṇṭu (உண்டு) denotes existence and is followed by a Voiceless consonant, ṭu (டு) may be dropped and ḷ (ள) may be substituted for ṇ (ண)."
            }
          },
          {
            "paadal": "",
            "vilakkam": 
            {
                "paadal_category": "Non-case relation Coalescence",
                "paadal_meaning": "If words denoting two different directions are combined, ē (ஏ) is inserted between them."
            }
          },
          {
            "paadal": "திரிபு வேறு கிளப்பின் ஒற்றும் உகரமும்  கெடுதல் வேண்டும் என்மனார் புலவர்  ஒற்று மெய் திரிந்து னகாரம் ஆகும்  தெற்கொடு புணரும் காலையான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Directions",
                "paadal_meaning": "Learned men say that, if the intermediate directions are meant, the final u (உ) and its preceding consonant of the standing word is dropped; and if teṟku (தெற்கு) happens to be the standing word, ṟ (ற) also is changed to ṉ (ன)."
            }
          },
          {
            "paadal": "ஒன்று முதல் ஆக எட்டன் இறுதி  எல்லா எண்ணும் பத்தன் முன் வரின்  குற்றியலுகரம் மெய்யொடும் கெடுமே  முற்ற இன் வரூஉம் இரண்டு அலங்கடையே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If pattu (பத்து) is the standing word and is followed by words denoting number from one to eight except two, the final tu (து) is dropped and iṉ (இன்) is inserted."
            }
          },
          {
            "paadal": "பத்தன் ஒற்றுக் கெட னகாரம் இரட்டல்  ஒத்தது என்ப இரண்டு வரு காலை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If pattu (பத்து) is followed by iraṇṭu (இரண்டு), ttu (த்து) is dropped and ṉṉ  (னன்) is inserted between them."
            }
          },
          {
            "paadal": "ஆயிரம் வரினும் ஆயியல் திரியாது.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If pattu (பத்து) is followed by āyiram (ஆயிரம்), the same change (as mentioned in sūtra 434) takes place."
            }
          },
          {
            "paadal": "நிறையும் அளவும் வரூஉம் காலையும்  குறையாது ஆகும் இன் என் சாரியை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If pattu (பத்து) is followed by words denoting weight and measure, the flexional increment iṉ (இன்) is invariably inserted (and the final tu (து) is dropped)."
            }
          },
          {
            "paadal": "ஒன்று முதல் ஒன்பான் இறுதி முன்னர்  நின்ற பத்தன் ஒற்றுக் கெட ஆய்தம்  வந்து இடை நிலையும் இயற்கைத்து என்ப  கூறிய இயற்கை குற்றியலுகரம்  ஆறன் இறுதி அல் வழியான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "It is said that, if the words denoting from one to nine are standing words and are followed pattu (பத்து), t (த்) following a of pattu (பத்து) is replaced by ஃ , the final u (உ) with its preceding consonants of the standing words is dropped except in the word āṟu (ஆறு) denoting six."
            }
          },
          {
            "paadal": "முதல் ஈர் எண்ணின் ஒற்று ரகரம் ஆகும்  உகரம் வருதல் ஆவயினான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "In the case of the first two numbers (i.e.), Oṉṟu (ஒன்று) and iraṇṭu (இரண்டு), ṉ (ன) and ṇ (ண) are respectively replaced by r (ர) followed by u (உ)."
            }
          },
          {
            "paadal": "இடை நிலை ரகரம் இரண்டு என் எண்ணிற்கு  நடை மருங்கு இன்றே பொருள்வயினான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "Ra (ர) following i (இ) in the word iraṇṭu (இரண்டு) is dropped"
            }
          },
          {
            "paadal": "மூன்றும் ஆறும் நெடு முதல் குறுகும்  மூன்றன் ஒற்றே பகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "The long vowels of mūṉṟu (மூன்று) and āṟu (ஆறு) are shortened, and ṉ (ன) of mūṉṟu (மூன்று) is replaced by p (ப)."
            }
          },
          {
            "paadal": "நான்கன் ஒற்றே றகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of nāṉku (நான்கு) is replaced by ṟ (ற)."
            }
          },
          {
            "paadal": "ஐந்தன் ஒற்றே மகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "n (ந) of aintu (ஐந்து) is changed to m (ம)."
            }
          },
          {
            "paadal": "எட்டன் ஒற்றே ணகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṭ (ட) of eṭṭu (எட்டு) is changed to ṇ (ண)."
            }
          },
          {
            "paadal": "ஒன்பான் ஒகரமிசைத் தகரம் ஒற்றும்  முந்தை ஒற்றே ணகாரம் இரட்டும்  பஃது என் கிளவி ஆய்த பகரம் கெட  நிற்றல் வேண்டும் ஊகாரக் கிளவி  ஒற்றிய தகரம் றகரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When oṉpatu (ஒன்பது) and pattu (பத்து) are combined together, t (த) is inserted before  oṉpatu (ஒன்பது), ṉ (ன்) is replaced by ṇṇ (ணண்) , paஃ (பஃ) of paஃtu (பஃது) (the modified form of pattu (பத்து) according to sūtra 438) is dropped, ū (ஊ) is inserted before the final tu (த்து) of paஃtu (பஃது) and t (த்) of tu (த்து) is changed to ṟ (ற்)."
            }
          },
          {
            "paadal": "அளந்து அறி கிளவியும் நிறையின் கிளவியும்  கிளந்த இயல தோன்றும் காலை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When words denoting measure and weight stand as coming words and words denoting numbers from one to nine are standing words, the change in sandhi will be the same as mentioned above (i.e.), as when the coming word is pattu (பத்து)."
            }
          },
          {
            "paadal": "மூன்றன் ஒற்றே வந்தது ஒக்கும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of mūṉṟu (மூன்று) is replaced by the voiceless consonant that commences the coming word."
            }
          },
          {
            "paadal": "ஐந்தன் ஒற்றே மெல்லெழுத்து ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "n (ந) of aintu (ஐந்து) is replaced by the nasal (corresponding to the voiceless consonant that commences the coming word)."
            }
          },
          {
            "paadal": "க ச த ப முதல் மொழி வரூஉம் காலை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "The changes mentioned above (i. e., in sūtras 447 & 448) take place when the coming word commences with  k (க), c (ச), t (த) or p (ப)."
            }
          },
          {
            "paadal": "ந ம வ என்னும் மூன்றொடு சிவணி  அகரம் வரினும் எட்டன் முன் இயல்பே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṭ (ட) of eṭṭu (எட்டு) is replaced by ṇ (ண) even when the coming word commences with n (ந), m (ம), v (வ) or a (அ)."
            }
          },
          {
            "paadal": "ஐந்தும் மூன்றும் ந ம வரு காலை  வந்தது ஒக்கும் ஒற்று இயல் நிலையே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "n (ந) of aintu (ஐந்து) and ṉ (ன) of mūṉṟu (மூன்று) are changed to n (ந) or m (ம) according as the initial of the coming word is n (ந) or m (ம) ."
            }
          },
          {
            "paadal": "மூன்றன் ஒற்றே வகாரம் வரு வழி  தோன்றிய வகாரத்து உரு ஆகும்மே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of mūṉṟu (மூன்று) is changed to v (வ) if the coming word commences with v (வ)."
            }
          },
          {
            "paadal": "நான்கன் ஒற்றே லகாரம் ஆகும்.",
            "vilakkam":
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of nāṉku (நான்கு) is changed to l (ல்) it the coming word commences with v (வ)."
            }
          },
          {
            "paadal": "ஐந்தன் ஒற்றே முந்தையது கெடுமே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "n (ந) of aintu (ஐந்து) is dropped when the coming word commences with v (வ)."
            }
          },
          {
            "paadal": "முதல் ஈர் எண்ணின் முன் உயிர் வரு காலை  தவல் என மொழிப உகரக் கிளவி  முதல் நிலை நீடல் ஆவயினான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "It is said that, if Oṉṟu (ஒன்று) and iraṇṭu (இரண்டு)  are standing words and coming words commence with a vowel, u (உ) of their modified forms oru (ஒரு) and īṟu(ஈறு) is dropped and their initial vowels are lengthened. "
            }
          },
          {
            "paadal": "மூன்றும் நான்கும் ஐந்து என் கிளவியும்  தோன்றிய வகரத்து இயற்கை ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If mūṉṟu (மூன்று), nāṉku (நான்கு) and aintu (ஐந்து) are standing words and (if the coming words commence with a vowel), the change in sandhi is the same as when the coming words commence with v (வ்)."
            }
          },
          {
            "paadal": "மூன்றன் முதல் நிலை நீடலும் உரித்தே  உழக்கு என் கிளவி வழக்கத்தான.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "Usage allows the lengthening of the first vowel of mūṉṟu (மூன்று) when it is followed by the word uḻakku (உழக்கு)."
            }
          },
          {
            "paadal": "ஆறு என் கிளவி முதல் நீடும்மே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "(When the coming words commence with a vowel), the initial ā (ஆ) of āṟu (ஆறு) which was shortened by the general rule, will resume its original form."
            }
          },
          {
            "paadal": "ஒன்பான் இறுதி உருபு நிலை திரியாது  இன் பெறல் வேண்டும் சாரியை மொழியே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When oṉpatu (ஒன்பது) is the standing word (and w'hen wwds denoting measure and weight are coming words), it does not undergo any modification in its form and the ficxional increment iṉ (இன்) is added after it."
            }
          },
          {
            "paadal": "நூறு முன் வரினும் கூறிய இயல்பே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "The same change as is mentioned above [(i. e.), when the coming word is pattu (பத்து) takes place (when words denoting from one to nine are standing words) and the coming word is nūṟu (நூறு) ."
            }
          },
          {
            "paadal": "மூன்றன் ஒற்றே நகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of mūṉṟu (மூன்று) is replaced by n (ந)."
            }
          },
          {
            "paadal": "நான்கும் ஐந்தும் ஒற்று மெய் திரியா.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of nāṉku (நான்கு) and n (ந) ofaintu (ஐந்து) do not undergo any change. "
            }
          },
          {
            "paadal": "ஒன்பான் முதல் நிலை முந்து கிளந்தற்றே  முந்தை ஒற்றே ளகாரம் இரட்டும்  நூறு என் கிளவி நகாரம் மெய் கெட  ஊ ஆ ஆகும் இயற்கைத்து என்ப  ஆயிடை வருதல் இகார ரகாரம்  ஈறு மெய் கெடுத்து மகாரம் ஒற்றும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When oṉpatu (ஒன்பது) and nūṟu (நூறு) are respectively the standing and the coming words, t (த) is inserted before oṉpatu (ஒன்பது) as is mentioned before (i. e., in sūtra 445), ṉ (ன) is replaced by ḷḷ (ளள்), n (ந) of nūṟu (நூறு) is dropped, ū (ஊ) is chaged to ā (ஆ) and ma (ம) is inserted after ā (ஆ) and ṟu (று) of nūṟu (நூறு) is replaced by m (ம)."
            }
          },
          {
            "paadal": "ஆயிரக் கிளவி வரூஉம் காலை  முதல் ஈர் எண்ணின் உகரம் கெடுமே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When āyiram (ஆயிரம்) is the coming word, the u (உ) of oru (ஒரு) and īṟu(ஈறு), the modified forms of Oṉṟu (ஒன்று) and iraṇṭu (இரண்டு) is dropped."
            }
          },
          {
            "paadal": "முதல் நிலை நீடினும் மானம் இல்லை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "There is no harm if the initial vowel (in both the above cases) is lengthened."
            }
          },
          {
            "paadal": "மூன்றன் ஒற்றே வகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of mūṉṟu (மூன்று) is changed to v (வ)."
            }
          },
          {
            "paadal": "நான்கன் ஒற்றே லகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "ṉ (ன) of nāṉku (நான்கு) is changed to l (ல்."
            }
          },
          {
            "paadal": "ஐந்தன் ஒற்றே யகாரம் ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "n (ந) of aintu (ஐந்து) is changed to y (ய)."
            }
          },
          {
            "paadal": "ஆறன் மருங்கின் குற்றியலுகரம்  ஈறு மெய் ஒழியக் கெடுதல் வேண்டும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "u (உ) of āṟu (ஆறு) is dropped."
            }
          },
          {
            "paadal": "ஒன்பான் இறுதி உருபு நிலை திரியாது  இன் பெறல் வேண்டும் சாரியை மரபே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "oṉpatu (ஒன்பது) without undergoing any change takes the flexional increment iṉ (இன்) after it."
            }
          },
          {
            "paadal": "நூறாயிரம் முன் வரூஉம் காலை  நூறன் இயற்கை முதல் நிலைக் கிளவி.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "The changes which the standing words denoting from one to nine undergo in sandhi when the coming word is nūṟāyiram (நூறாயிரம்) are the same as those when it is nūṟu (நூறு)."
            }
          },
          {
            "paadal": "நூறு என் கிளவி ஒன்று முதல் ஒன்பாற்கு  ஈறு சினை ஒழிய இன ஒற்று மிகுமே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When nūṟu (நூறு) is the standing word and the coming words are from Oṉṟu (ஒன்று) to oṉpatu (ஒன்பது), the consonant ṟ (ற்) preceding u (உ) is doubled."
            }
          },
          {
            "paadal": "அவை ஊர் பத்தினும் அத் தொழிற்று ஆகும்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning":"The same is the case even when the coming words are orupaஃtu (ஒரு-பஃது), irupaஃtu (இரு - பஃது) etc."
            }
          },
          {
            "paadal": "அளவும் நிறையும் ஆயியல் திரியா  குற்றியலுகரமும் வல்லெழுத்து இயற்கையும்  முன் கிளந்தன்ன என்மனார் புலவர்.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "Learned men say that, when nūṟu (நூறு) is the standing word and words denoting measure and weight are coming words, the presence of u (உ) and the doubling of ṟ (ற்) are the same as before."
            }
          },
          {
            "paadal": "ஒன்று முதல் ஆகிய பத்து ஊர் கிளவி  ஒன்று முதல் ஒன்பாற்கு ஒற்று இடை மிகுமே  நின்ற ஆய்தம் கெடுதல் வேண்டும்.",
            "vilakkam":
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "When orupaஃtu (ஒரு-பஃது), irupaஃtu (இரு - பஃது) etc. are standing words and the coming words are from Oṉṟu (ஒன்று) to oṉpatu (ஒன்பது), ஃ () is dropped and t (த்) is doubled."
            }
          },
          {
            "paadal": "ஆயிரம் வரினே இன் ஆம் சாரியை  ஆவயின் ஒற்று இடை மிகுதல் இல்லை.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If āyiram (ஆயிரம்) is the coming word, t (த்) is not doubled, but the flexional increment iṉ (இன்) is inserted."
            }
          },
          {
            "paadal": "அளவும் நிறையும் ஆயியல் திரியா.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "The same is the case when words denoting measure and weight are coming words."
            }
          },
          {
            "paadal": "முதல் நிலை எண்ணின் முன் வல்லெழுத்து வரினும்  ஞ ந மத் தோன்றினும் ய வ வந்து இயையினும்  முதல் நிலை இயற்கை என்மனார் புலவர்.",
            "vilakkam":
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "Learned men say that, if Oṉṟu (ஒன்று) is followed by a voiceless consonant, ñ (ஞ்), n (ந்), m (ம்), y (ய்) or v (வ்), it is changed to oru (ஒரு) as before. Ex. Oṉṟu (ஒன்று) + kal = orukal (ஒருகல்) etc."
            }
          },
          {
            "paadal": "அதன் நிலை உயிர்க்கும் யா வரு காலை  முதல் நிலை ஒகரம் ஓ ஆகும்மே  ரகரத்து உகரம் துவரக் கெடுமே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning": "If a vowel or yā (யா) is the initial of the coming word, the o (ஒ) of oru (ஒரு) mentioned in the previous sūtra is lengthened to ō (ஓ) and u (உ) is dropped."
            }
          },
          {
            "paadal": "இரண்டு முதல் ஒன்பான் இறுதி முன்னர்  வழங்கு இயல் மா என் கிளவி தோன்றின்  மகர அளவொடு நிகரலும் உரித்தே.",
            "vilakkam": 
            {
                "paadal_category": "Nouns Denoting Numerals",
                "paadal_meaning":"If the words from iraṇṭu (இரண்டு) to oṉpatu (ஒன்பது) are standing words and if the coming word is mā (மா) which denotes extent and which is generally in use, the change in sandhi is optionally the same as that when the coming word denotes measure and commences with m (ம்)."
            }
          },
          {
            "paadal": "ல ன என வரூஉம் புள்ளி இறுதி முன்  உம்மும் கெழுவும் உளப்படப் பிறவும்  அன்ன மரபின் மொழியிடைத் தோன்றி  செய்யுள் தொடர்வயின் மெய் பெற நிலையும்  வேற்றுமை குறித்த பொருள்வயினான.",
            "vilakkam": 
            {
                "paadal_category": "Variations",
                "paadal_meaning": "When the standing words end in l (ல) or ṉ (ன), particles like um (உம்), keḻu (கெழு) etc. are, as usage permits, inserted after them in poetry in case-relation sandhi . Ex. vāṉa-vari-villun-tiṅkaḷum (வான-வரி-வில்லுந்-திங்களும்). (Here villun-tiṅkaḷum (வில்லுந்-திங்களும்) means also the moon near the rain-bow.); kal-keḷu-kāṇavar (கல்-கெளு-காணவர்) etc."
            }
          },
          {
            "paadal": "உயிரும் புள்ளியும் இறுதி ஆகி  குறிப்பினும் பண்பினும் இசையினும் தோன்றி  நெறிப் பட வாராக் குறைச்சொற் கிளவியும்  உயர்திணை அஃறிணை ஆயிரு மருங்கின்  ஐம் பால் அறியும் பண்பு தொகு மொழியும்  செய்யும் செய்த என்னும் கிளவியின்  மெய் ஒருங்கு இயலும் தொழில் தொகு மொழியும்  தம் இயல் கிளப்பின் தம் முன் தாம் வரூஉம்  எண்ணின் தொகுதி உளப்படப் பிறவும்  அன்னவை எல்லாம் மருவின் பாத்திய  புணர் இயல் நிலையிடை உணரத் தோன்றா.",
            "vilakkam": 
            {
                "paadal_category": "Variations",
                "paadal_meaning": "The changes that take place in standing words when they are (1; the defective words denoting feeling, paṇpu (பண்பு) (genus, quality or action) and sound and ending in vowel or consonant (i. e., uriccol (உரிச்சொல்)), (2) the words denoting paṇpu (பண்பு) and Pāl (பால்) when they form the first member of Paṇputtokai (பண்புத்தொகை), (3) the participles ceyyum (செய்யும்) and ceyta (செய்த) when they form the first member of Viṉaittokai (வினைத்தொகை), (4) words denoting number preceding the same words etc., have to be determined from usage and are not clearly mentioned here. Ex. (1) veḷḷa (வெள்ள) + viḷarttatu (விளர்த்தது) = velviḷarttatu (வெள்விளர்த்தது); (2) kariyatu (கரியது) + kutirai (குதிரை) = Karuṅkutirai (கருங்குதிரை) ; (3) kollum (கொல்லம்) + yāṉai (யானை) =kol-yanai (கொல்-யானை) , koṉṟa (கொன்ற) f yāṉai (யானை) = kol-yanai (கொல்-யானை) ; (4) pattu (பத்து) + pattu (பத்து) = pappattu (பப்பத்து), Oṉṟu (ஒன்று) + Oṉṟu (ஒன்று) = Ōroṉṟu (ஓரொன்று) etc."
            }
          },
          {
            "paadal": "கிளந்த அல்ல செய்யுளுள் திரிநவும்  வழங்கு இயல் மருங்கின் மருவொடு திரிநவும்  விளம்பிய இயற்கையின் வேறுபடத் தோன்றின்  வழங்கு இயல் மருங்கின் உணர்ந்தனர் ஒழுக்கல்  நன் மதி நாட்டத்து என்மனார் புலவர்.",
            "vilakkam":
            {
                "paadal_category": "Variations",
                "paadal_meaning": "Learned men say that, if changes in the forms of words not mentioned in the previous sections are found in literature and usage, they should be taken into account after they are critically examined by scholars."
            }
          }
        ]
      }
    ]
  },
  {
    "adhikaaram": "சொல்லதிகாரம்",
    "adhikaaram_eng":"Morphology, Syntax and Semantics",
    "iyal": [
      {
        "iyal_name": "கிளவியாக்கம்",
        "iyal_eng":"Morphemes and their Organization",
        "noorpa": [
          {
            "paadal": "உயர்திணை என்மனார் மக்கட் சுட்டே \nஅஃறிணை என்மனார் அவரல பிறவே \nஆயிரு திணையின் இசைக்குமன சொல்லே.",
            "vilakkam": {
              "paadal_category": "Human and non-human classes",
              "paadal_meaning": "Uyartiṇai (உயர்திணை) is that which denotes human beings; and all the rest is aḵṟiṇai(அஃறிணை). Col(சொல்) [word] is used in either Gender"
            }
          },
          {
            "paadal": "ஆடூஉ அறிசொல் மகடூஉ அறிசொல் \nபல்லோர் அறியும் சொல்லொடு சிவணி \nஅம்முப் பாற்சொல் உயர்திணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "Human and non-human classes",
              "paadal_meaning": "Uyartiṇai-col (உயர்திணை-சொல்) is of three kinds āṭūu aṟicol (ஆடூஉ அறிசொல்) or word of the masculine singular; makaṭūu aṟicol (மகடூஉ அறிசொல்) or word of the feminine singular; and pallōr aṟiyum col (பல்லோர் அறியும் சொல்) or word of the epicene plural (masculine-feminine, masculine and feminine, plural)."
            }
          },
          {
            "paadal": "ஒன்றறி சொல்லே பலஅறி சொல்லென்று \nஆயிரு பாற்சொல் அஃறிணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "Human and non-human classes",
              "paadal_meaning": "Aḵṟiṇai-col (அஃறிணை-சொல்) is of two kinds : oṉṟaṟi col (ஒன்றறி சொல்) or word of the neuter singular and pala-aṟi col (பலஅறி சொல்) or word of neuter plural."
            }
          },
          {
            "paadal": "பெண்மை சுட்டிய உயர்திணை மருங்கின் \nஆண்மை திரிந்த பெயர்நிலைக் கிளவியும் \nதெய்வம் சுட்டிய பெயர்நிலைக் கிளவியும் \nஇவ்வென அறியும் அந்தம் தமக்கு இலவே \nஉயர்திணை மருங்கின் பால்பிரிந் திசைக்கும்.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "Word denoting a hermaphrodite with more of feminine traits which belongs to uyartiṇai (உயர்திணை) and words denoting gods do not have a seprate suffix, but the suffix of the pāls (பால்s) of uyartiṇai (உயர்திணை)."
            }
          },
          {
            "paadal": "னஃகான் ஒற்றே ஆடூஉ அறிசொல்.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "āṭūu aṟicol (ஆடூஉ அறிசொல்) has ṉ(ன்) at its end."
            }
          },
          {
            "paadal": "ளஃகான் ஒற்றே மகடூஉ அறிசொல்.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "makaṭūu aṟicol (மகடூஉ அறிசொல்) has ḷ(ள்) in the end."
            }
          },
          {
            "paadal": "ரஃகான் ஒற்றும் பகர இறுதியும் \nமாரைக் கிளவி உளப்பட மூன்றும் \nநேரத் தோன்றும் பலர்அறி சொல்லே.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "Word which are invariably pallōr aṟiyum col (பல்லோர் அறியும் சொல்) are those that end with r(ர்), pa(ப) or mar(மார்)."
            }
          },
          {
            "paadal": "ஒன்றறி கிளவி தறட ஊர்ந்த \nகுன்றியலுகரத்து இறுதி யாகும்.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "oṉṟaṟi col (ஒன்றறி சொல்) has (தூ) tū, (ரூ) rū, or (டூ) ṭū at the end."
            }
          },
          {
            "paadal": "அ ஆ வ என வரூஉம் இறுதி \nஅப்பால் மூன்றே பலர்அறி சொல்லே.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "pala-aṟi col (பலஅறி சொல்) has (அ) a, (ஆ) ā or (வ) va at the end."
            }
          },
          {
            "paadal": "இருதிணை மருங்கின் ஐம்பால் அறிய \nஈற்றில் நின்றிசைக்கும் பதினோர் எழுத்தும் \nதோற்றந் தாமே வினையொடு வருமே.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "The eleven suffixes mentioned above as denoting the five pāls (பால்s) of the two tiṇais (திணைs) invariably appear verbs."
            }
          },
          {
            "paadal": "வினையின் தோன்றும் பால்அறி கிளவியும் \nபெயரின் தோன்றும் பால்அறி கிளவியும் \nமயங்கல் கூடா தம்மர பினவே.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "The gender-number denoting element (pāl(பால்)-element) in the predicted should not disagree  with that in the subject; but they should conform to usage."
            }
          },
          {
            "paadal": "ஆண்மை திரிந்த பெயர்நிலைக் கிளவி \nஆண்மை அறிசொற்கு ஆகிடன் இன்றே.",
            "vilakkam": {
              "paadal_category": "Gender suffixes",
              "paadal_meaning": "The word denoting a hermaphrodite with more of feminine traits cannot be used in the masculine-singular."
            }
          },
          {
            "paadal": "செப்பும் வினாவும் வழாஅல் ஓம்பல்.",
            "vilakkam": {
              "paadal_category": "Texture of Discourse Types",
              "paadal_meaning": "Question and answer should be correct inform and appropriate in sense."
            }
          },
          {
            "paadal": "வினாவும் செப்பே வினாஎதிர் வரினே.",
            "vilakkam": {
              "paadal_category": "Texture of Discourse Types",
              "paadal_meaning": "Even a question may be taken as ceppu (செப்பு) , if it answers a question."
            }
          },
          {
            "paadal": "செப்பே வழீஇயினும் வரைநிலை யின்றே \nஅப்பொருள் புணர்ந்த கிளவி யான.",
            "vilakkam": {
              "paadal_category": "Texture of Discourse Types",
              "paadal_meaning": "It is not the objectionable to use an answer in an irregular form, if it somehow suggests the answer."
            }
          },
          {
            "paadal": "செப்பினும் வினாவினும் சினைமுதல் கிளவிக்கு \nஅப்பொருள் ஆகும் உறழ்துணைப் பொருளே.",
            "vilakkam": {
              "paadal_category": "Texture of Discourse Types",
              "paadal_meaning": "Both in ceppu (செப்பு) and vinā (வினா) only like objects can be compared, or contrasted, part with part and whole with whole."
            }
          },
          {
            "paadal": "தகுதியும் வழக்கும் தழீஇயின ஒழுகும் \nபகுதிக் கிளவி வரைநிலை இலவே.",
            "vilakkam": {
              "paadal_category": "Deviations",
              "paadal_meaning": "Certain expressions (which do not conform to the previous rule) are not prohibited, if propriety demands or usage sanctions them."
            }
          },
          {
            "paadal": "இனச்சுட்டு இல்லாப் பண்புகொள் பெயர்க்கொடை \nவழக்காறு அல்ல செய்யுள் ஆறே.",
            "vilakkam": {
              "paadal_category": "Restrictive and non-restrictive adjectives",
              "paadal_meaning": "The use of adjectives which are not restrictive in character is allowed only in poetry."
            }
          },
          {
            "paadal": "இயற்கைப் பொருளை இற்றெனக் கிளத்தல்.",
            "vilakkam": {
              "paadal_category": "A Convention about designation natural objects",
              "paadal_meaning": "Natural objects should be described by their distinguishing features."
            }
          },
          {
            "paadal": "செயற்கைப் பொருளை ஆக்கமொடு கூறல்.",
            "vilakkam": {
              "paadal_category": "A Convention about designating things",
              "paadal_meaning": "In a sentence describing the change which an object has undergone, the word denoting that object should be followed by the forms of the verb āku (ஆகு) which means 'to become'."
            }
          },
          {
            "paadal": "ஆக்கந் தானே காரணம் முதற்றே.",
            "vilakkam": {
              "paadal_category": "A Convention about designating things",
              "paadal_meaning": "The verb āku (ஆகு) is always preceded by reason, if the reason for the change is given."
            }
          },
          {
            "paadal": "ஆக்கக் கிளவி காரணம் இன்றியும் \nபோக்கின்று என்ப வழக்கி னுள்ளே.",
            "vilakkam": {
              "paadal_category": "A Convention about designating things",
              "paadal_meaning": "Expressions with the forms of the verb āku (ஆகு) without giving the reason for the change are current in speech."
            }
          },
          {
            "paadal": "பால்மயக் குற்ற ஐயக்கிளவி \nதான்அறி பொருள்வயின் பன்மை கூறல்.",
            "vilakkam": {
              "paadal_category": "Uncertainty as to Species and Gender",
              "paadal_meaning": "When a speaker is sure of the tiṇai (திணை) of the object he is talking about, but not of the pāl (பால்), he should use a plural verb of the particular tiṇai (திணை)."
            }
          },
          {
            "paadal": "உருபென மொழியினும் அஃறிணைப் பிரிப்பினும் \nஇருவீற்றும் உரித்தே சுட்டும் காலை.",
            "vilakkam": {
              "paadal_category": "Uncertainty as to Species and Gender",
              "paadal_meaning": "(When the speaker is not sure of the tiṇai (திணை)  of the object at a distance), he may use the word urupu (உருபு) (or its synonyms) or the word atu (அது) when he denotes it."
            }
          },
          {
            "paadal": "தன்மை சுட்டலும் உரித்தென மொழிப \nஅன்மைக் கிளவி வேறிடத் தான.",
            "vilakkam": {
              "paadal_category": "Uncertainty as to Species and Gender",
              "paadal_meaning": "The word aṉmai (அன்மை) denoting negation may take the gender of the ascertained object, through it (aṉmai (அன்மை)) is used along with the word denoting the object other than the ascertained one."
            }
          },
          {
            "paadal": "அடைசினை முதல்என முறைமூன்றும் மயங்காமை \nநடைபெற் றியலும் வண்ணச் சினைச்சொல்.",
            "vilakkam": {
              "paadal_category": "Conventions regarding Attributes",
              "paadal_meaning": "(In a group of words denoting a whole, its limb and the quality of the limb), the word denoting the limb invariably follows the adjective and precedes the word denoting the whole."
            }
          },
          {
            "paadal": "ஒருவரைக் கூறும் பன்மைக் கிளவியும் \nஒன்றனைக் கூறும் பன்மைக் கிளவியும் \nவழக்கி னாகிய உயர்சொல் கிளவி \nஇலக்கண மருங்கின் சொல்லாறு அல்ல.",
            "vilakkam": {
              "paadal_category": "Worldly usage",
              "paadal_meaning": "The use of honorific plural to denotes ones person or one object is allowed only in speech and not in poetry."
            }
          },
          {
            "paadal": "செலவினும் வரவினும் தரவினும் கொடையினும் \nநிலைபெறத் தோன்றும் அந்நாற் சொல்லும் \nதன்மை முன்னிலை படர்க்கை என்னும் \nஅம்மூ விடத்தும் உரிய என்ப.",
            "vilakkam": {
              "paadal_category": "Persons",
              "paadal_meaning": "It is said  that the four words celavu (செலவு), varavu (வரவு), taravu (தரவு), and koṭai (கொடை) are used in the first, second and third persons."
            }
          },
          {
            "paadal": "அவற்றுள், \nதருசொல் வருசொல் ஆயிரு கிளவியும் \nதன்மை முன்னிலை ஆயீர் இடத்த.",
            "vilakkam": {
              "paadal_category": "Persons",
              "paadal_meaning": "Of them the words taravu (தரவு) and varavu (வரவு) are used only along with the pronouns of the first and second persons, ie; the verbs meaning to give and to come are respectively used, only when the recipient of the gift and the person approached are in the first or the second person."
            }
          },
          {
            "paadal": "ஏனை இரண்டும் ஏனை இடத்த.",
            "vilakkam": {
              "paadal_category": "Persons",
              "paadal_meaning": "The remaing two (i.e, celavu (செலவு) and koṭai (கொடை)) are used along with third person."
            }
          },
          {
            "paadal": "யாது எவன் என்னும் ஆயிரு கிளவியும் \nஅறியாப் பொருள்வயின் செறியத் தோன்றும்.",
            "vilakkam": {
              "paadal_category": "Things unidentified",
              "paadal_meaning": "The two (interrogative) pronouns yāṭu (யாடு) and evaṉ (எவன்) are generally used  in questioning about unknown objects."
            }
          },
          {
            "paadal": "அவற்றுள், \nயாதுஎன வரூஉம் வினாவின் கிளவி \nஅறிந்த பொருள்வயின் ஐயம் தீர்தற்குத் \nதெரிந்த கிளவி யாதலும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Things unidentified",
              "paadal_meaning": "Of them, the interrogative pronoun yadave may also be used in sentences where some doubts are to be cleared regarding the particulars of an object whose general features are known."
            }
          },
          {
            "paadal": "இனைத்தென அறிந்த சினைமுதல் கிளவிக்கு \nவினைப்படு தொகுதியின் உம்மை வேண்டும்.",
            "vilakkam": {
              "paadal_category": "The -um (உம்) Particle",
              "paadal_meaning": "The particle um should invariably be used after the group of words which qualify the verb, i.e, immediately preceding the verb or the predicate, where the subject of the verb is a mutal (word denoting a whole) or a ciṉai (சினை) (word denoting a part of a whole) qualified by the word which mentions its exact number"
            }
          },
          {
            "paadal": "மன்னாப் பொருளும் அன்ன இயற்றே.",
            "vilakkam": {
              "paadal_category": "The -um (உம்) Particle",
              "paadal_meaning": "The same is the case even with words denoting transient objects."
            }
          },
          {
            "paadal": "எப்பொருள் ஆயினும் அல்லது இல்லெனின் \nஅப்பொருள் அல்லாப் பிறிதுபொருள் கூறல்.",
            "vilakkam": {
              "paadal_category": "A trade register",
              "paadal_meaning": "If anyone (a merchant) wishes to inform (a purchaser) of the absence of any commodity by using the expression allatil (அல்லதில்), he should associate that expression with a word denoting any commodity (that he has), and not with that denoting the commodity asked for."
            }
          },
          {
            "paadal": "அப்பொருள் கூறின் சுட்டிக் கூறல்.",
            "vilakkam": {
              "paadal_category": "A trade register",
              "paadal_meaning": "If, in the answer given by the merchant, the word denoting the object asked for by the purchaser, is used, it should be preceded by a demonstrative root or adjective."
            }
          },
          {
            "paadal": "பொருளொடு புணராச் சுட்டுப்பெய ராயினும் \nபொருள்வேறு படாஅது ஒன்று ஆகும்மே.",
            "vilakkam": {
              "paadal_category": "A function of the demonstrative pronoun",
              "paadal_meaning": "Even though the demonstrative element is not associated with the word denoting the commodity asked for, the sense conveyed will be the same."
            }
          },
          {
            "paadal": "இயற்பெயர்க் கிளவியும் சுட்டுப்பெயர்க் கிளவியும் \nவினைக்கொருங் கியலும் காலம் தோன்றின் \nசுட்டுப்பெயர்க் கிளவி முற்படக் கிளவார் \nஇயற்பெயர் வழிய என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Personal pronoun as co-referent",
              "paadal_meaning": "If an iyaṟpeyar (இயற்பெயர்) and pronoun referring to it do not stand as logical subject and predicate, but take predicate after them or qualify different predicates, it is said by learned men that the pronoun is never used before the iyaṟpeyar (இயற்பெயர்), but only follows it."
            }
          },
          {
            "paadal": "முற்படக் கிளத்தல் செய்யுளுள் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Personal pronoun as co-referent",
              "paadal_meaning": "(The pronoun referred to in the previous sūtra) may precede the noun which it refers to in poetry."
            }
          },
          {
            "paadal": "சுட்டுமுதல் ஆகிய காரணக் கிளவியும் \nசுட்டுப்பெயர் இயற்கையின் செறியத் தோன்றும்.",
            "vilakkam": {
              "paadal_category": "Personal pronoun as co-referent",
              "paadal_meaning": "The word commencing with a demonstrative root and denoting the reason is similar m (ம்) its usage to the demonstrative pronouns and adjectives."
            }
          },
          {
            "paadal": "சிறப்பின் ஆகிய பெயர்நிலைக் கிளவிக்கும் \nஇயற்பெயர்க் கிளவி முற்படக் கிளவார்.",
            "vilakkam": {
              "paadal_category": "Positioning of Honorific Titles",
              "paadal_meaning": "The original name of a person also should not precede the name of distinction of the same person if both qualify the same verb."
            }
          },
          {
            "paadal": "ஒருபொருள் குறித்த வேறுபெயர்க் கிளவி \nதொழில்வேறு கிளப்பின் ஒன்றிடன் இலவே.",
            "vilakkam": {
              "paadal_category": "Nominal Epithets-Verb Concord",
              "paadal_meaning": "Epithets denoting the same person or subject cannot denote one and the same person or object if each takes a different predicate after it."
            }
          },
          {
            "paadal": "தன்மைச் சொல்லே அஃறிணைக் கிளவியென்று \nஎண்ணுவழி மருங்கின் விரவுதல் வரையார்.",
            "vilakkam": {
              "paadal_category": "A Norm of Usage",
              "paadal_meaning": "It is not even prevented to count an aḵṟiṇai(அஃறிணை) noun along with the first personal pronoun."
            }
          },
          {
            "paadal": "ஒருமை எண்ணின் பொதுப்பிரி பாற்சொல் \nஒருமைக் கல்லது எண்ணுமுறை நில்லாது.",
            "vilakkam": {
              "paadal_category": "A Norm about Common Gender Designation",
              "paadal_meaning": "The words (oruvaṉ (ஒருவன்) or orutti (ஒருத்தி)) which respectively mean one man and one women and have each a suffix denoting the pāl (பால்) or gender-number are not used in counting."
            }
          },
          {
            "paadal": "வியங்கோள் எண்ணுப் பெயர் திணைவிரவு வரையார்.",
            "vilakkam": {
              "paadal_category": "Mixed Human and Non-Human Class",
              "paadal_meaning": "It is not prohibited to connect uyartiṇai (உயர்திணை) nouns and  aḵṟiṇai (அஃறிணை) nouns by and, if both of them have a verb in the potential mood as the common predicate."
            }
          },
          {
            "paadal": "வேறுவினைப் பொதுச்சொல் ஒருவினை கிளவார்.",
            "vilakkam": {
              "paadal_category": "Common Noun and a Specific Verb",
              "paadal_meaning": "A predicate denoting the individuality of an action is not used along with a noun connected with its genus, the predicate denoting the genus of the action itself should be used."
            }
          },
          {
            "paadal": "எண்ணுங் காலும் அதுஅதன் மரபே.",
            "vilakkam": {
              "paadal_category": "Common Noun and a Specific Verb",
              "paadal_meaning": "The same rule (as it mentioned in the previous sūtra) should be observed when eatables of nature are counted,(i.e,) the verb giving the general sense should be used."
            }
          },
          {
            "paadal": "இரட்டைக் கிளவி இரட்டிற்பிரிந் திசையா.",
            "vilakkam": {
              "paadal_category": "Reduplicative term",
              "paadal_meaning": "There are certain words whose roots are always reduplicated."
            }
          },
          {
            "paadal": "ஒரு பெயர்ப் பொதுச்சொல் உள்பொருள் ஒழியத் \nதெரிபுவேறு கிளத்தல் தலைமையும் பன்மையும் \nஉயர்திணை மருங்கினும் அஃறிணை மருங்கினும்.",
            "vilakkam": {
              "paadal_category": "Designation of Dominant Species",
              "paadal_meaning": "If in certain expressions, uyartiṉai(உயர்திணை) and aḵṟiṇai(அஃறிணை) words have to be used to donate a group made up of different kinds of persons or objects, those that denote the pre-eminent or the majority are used. For instance one uses the word pārppaṉa-c-cēri (பார்ப்பனச்சேரி) (the residence of brahmans) to denote a place where Brahmans and members of other communities reside, of whom the Brahmans are considered as superior. Similarly the word kamukan-tōṭṭam (கமுகந்தோட்டம்) to denote a garden containing kamuku (கமுகு) (araca-palm) and other trees. Since kamukan-tōṭṭam (கமுகந்தோட்டம்) is chosen. The word eyiṉar-nāṭu (எயினர்-நாடு) (the land of hunters) is used to denote a where eyiṉar(எயினர்) are majority. Similarly the word oṭu-vaṅ-kāṭu (ஒடுவங்காடு) (forest containing oṭu (ஒடு) trees) is used to denote a forest which abounds in round leveled discous feather foil trees."
            }
          },
          {
            "paadal": "பெயரினும் தொழிலினும் பிரிபவை எல்லாம் \nமயங்கல் கூடா வழக்கு வழிப்பட்டன.",
            "vilakkam": {
              "paadal_category": "Common terms and Sepcific Gender Designation",
              "paadal_meaning": "Nouns and verbs (belonging both to uyartiṉai(உயர்திணை) and aḵṟiṇai(அஃறிணை)) denoting different objects pr actions should be counted together only according to usage."
            }
          },
          {
            "paadal": "பலவயி னானும் எண்ணுத்திணை விரவுப்பெயர் \nஅஃறிணை முடிபின செய்யு ளுள்ளே.",
            "vilakkam": {
              "paadal_category": "Mixed class nouns and enumeration",
              "paadal_meaning": "If uyartiṉai (உயர்திணை) and aḵṟiṇai(அஃறிணை) nouns are connected by and take a common predicate, the akkrinai predicate is generally used in poetry."
            }
          },
          {
            "paadal": "வினைவேறு படூஉம் பலபொருள் ஒருசொல் \nவினைவேறு படாஅப் பலபொருள் ஒருசொல்லென்று \nஆயிரு வகைய பலபொருள் ஒருசொல்.",
            "vilakkam": {
              "paadal_category": "A classification of Homonyms",
              "paadal_meaning": "Pala-poruḷ-oru-col (பல-பொருள்-ஒரு-சொல்) words having different meanings are of two kinds:(1) those which take different verbs after them and (2) those which take the same verb after them."
            }
          },
          {
            "paadal": "அவற்றுள், \nவினைவேறு படூஉம் பலபொருள் ஒருசொல் \nவேறுபடு வினையினும் இனத்தினும் சார்பினும் \nதேறத் தோன்றும் பொருள்தெரி நிலையே.",
            "vilakkam": {
              "paadal_category": "A classification of Homonyms",
              "paadal_meaning": "Of them the meaning of viṉai-vēṟu-paṭūum-pala-poruḷ-oru-col (வினை-வேறு-படூஉம்-பல-பொருள்-ஒரு-சொல்) is clearly determined by vēṟu-paṭu-viṉai (வேறு-படு-வினை) distinguishing verbs, iṉam (இனம்) the words of its class used along with it cārpu (சார்பு) context."
            }
          },
          {
            "paadal": "ஒன்றுவினை மருங்கின் ஒன்றித் தோன்றும் \nவினைவேறு படாஅப் பலபொருள் ஒருசொல் \nநினையும் காலை கிளந்தாங்கு இயலும்.",
            "vilakkam": {
              "paadal_category": "A classification of Homonyms",
              "paadal_meaning": "Words having different meanings should be clearly mentioned with proper adjuncts to enable the reader to understand its exact meaning, if they are followed by non-distinguishing verbs."
            }
          },
          {
            "paadal": "குறித்தோன் கூற்றம் தெரித்துமொழி கிளவி.",
            "vilakkam": {
              "paadal_category": "Nature of Utterance",
              "paadal_meaning": "The idea of the speaker or writer should be definitely expressed."
            }
          },
          {
            "paadal": "குடிமை ஆண்மை இளமை மூப்பே \nஅடிமை வன்மை விருந்தே குழுவே \nபெண்மை அரசே மகவே குழவி \nதன்மை திரிபெயர் உறுப்பின் கிளவி \nகாதல் சிறப்பே செறற்சொல் விறற்சொல் என்று \nஆவறு மூன்றும் உளப்படத் தொகைஇ \nஅன்ன பிறவும் அவற்றொடு சிவணி \nமுன்னத்தின் உணருங் கிளவி எல்லாம் \nஉயர்திணை மருங்கின் நிலையின ஆயினும் \nஅஃறிணை மருங்கின் கிளந்தாங்கு இயலும்.",
            "vilakkam": {
              "paadal_category": "Human class Terms Treated as non-humans",
              "paadal_meaning": "The eighteen words kuṭimai (குடிமை) (status of a family), āṇmai (ஆண்மை) (manliness, man), iḷamai (இளமை ) (youth, young man or women), mūppu (மூப்பு) (old age, old person), aṭimai (அடிமை) (slave, slavery), vaṉmai (வன்மை) (strength, strong ally), viruntu (விருந்து) (feast, guest), kuḻu (குழு) (collection, crowd), peṇmai (பெண்மை) (feminine quality, woman), aracū (அரசூ) (kingship, king), makavu (மகவு) (son-hood, daughter-hood : son,daughter), kuḻavi (குழவி )(childhood, child), taṉmai tiripeyar (தன்மை திரிபெயர்) (noun denoting the change of quality,) uṟuppiṉ kiḷavi (உறுப்பின் கிளவி) (words pertaining to organs like kuruṭu (குருடு) (blindness, blind person)), muṭam (முடம்) (lameness, lame person etc.,) kātaṟ-col (காதற்-சொல்) (terms of endearment,) ciṟappu-c-col (சிறப்பு-ச்-சொல்) (terms of  honour), ceṟaṟ-col (செறற் சொல்) (teṟms of hatred, anger etc.), viṟaṟ-col (விறற் சொல்) (terms of valour) and similar ones take aḵṟiṇai (அஃறிணை) verbs even when they denote uyartiṉai (உயர்திணை) objects."
            }
          },
          {
            "paadal": "காலம் உலகம் உயிரே உடம்பே \nபால்வரை தெய்வம் வினையே பூதம் \nஞாயிறு திங்கள் சொல்என வரூஉம் \nஆயீர் ஐந்தொடு பிறவும் அன்ன \nஆவயின் வரூஉம் கிளவி எல்லாம் \nபால்பிரிந்து இசையா உயர்திணை மேன.",
            "vilakkam": {
              "paadal_category": "Human class Terms Treated as non-humans",
              "paadal_meaning": "The ten words kālam (காலம்) (God of time), (உலகம்) (World), uyir (உயிர்) (soul), uṭampu (உடம்பு) (body), pāl-varai-teyvam (பால்-வரை-தெய்வம்) (supreme god), viṉai (வினை) (fate), pūtam (பூதம் )(elements: earth, water, light, air, space), ñāyiṟu (ஞாயிறு) (sun), tiṅkaḷ (திங்கள்) (moon), col (சொல்) (goddess of sarasvati) and similar one do not take uyartiṉai (உயர்திணை) verbs (ie: āṇpāl (ஆண்பால்), peṇpāl (பெண்பால்), or palarpāl (பலர்பால்) verbs) after them, but take only aḵṟiṇai (அஃறிணை) verbs."
            }
          },
          {
            "paadal": "நின்றாங்கு இசைத்தல் இவணியல் பின்றே.",
            "vilakkam": {
              "paadal_category": "Human class Terms Treated as non-humans",
              "paadal_meaning": "It is not in their nature to take uyartiṉai (உயர்திணை) verbs without modification in their form."
            }
          },
          {
            "paadal": "இசைத்தலும் உரிய வேறிடத் தான.",
            "vilakkam": {
              "paadal_category": "Human class Terms Treated as non-humans",
              "paadal_meaning": "They (the two words kālam (காலம்) etc.) may take āṇpāl (ஆண்பால்), peṇpāl (பெண்பால்) or palarpāl (பலர்பால்) verbs in others places."
            }
          },
          {
            "paadal": "எடுத்த மொழிஇனஞ் செப்பலும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Nature of Certain Assertions",
              "paadal_meaning": "A sentence which is expressed may suggest related ideas."
            }
          },
          {
            "paadal": "கண்ணும் தோளும் முலையும் பிறவும் \nபன்மை சுட்டிய சினைநிலைக் கிளவி \nபன்மை கூறும் கடப்பாடு இலவே \nதம்வினைக்கு இயலும் எழுத்து அலங்கடையே.",
            "vilakkam": {
              "paadal_category": "Concord of Limbs in Pairs",
              "paadal_meaning": "The denoting limbs in plural number like kaṇ (கண்) (eyes), tōḷ (தோள்) (shoulders), mulai (முலை) (breasts) etc., need not denote the plural number unless they are followed by palaviṉpāl (பலவின்பால்) verbs."
            }
          }
        ]
      },
      {
        "iyal_name": "வேற்றுமையியல்",
        "iyal_eng":"The Case System",
        "noorpa": [
          {
            "paadal": "வேற்றுமை தாமே ஏழென மொழிப.",
            "vilakkam": {
              "paadal_category": "Case Types",
              "paadal_meaning": "It is said that cases are 7 in number."
            }
          },
          {
            "paadal": "விளிகொள் வதன்கண் விளியோ டெட்டே.",
            "vilakkam": {
              "paadal_category": "Case Types",
              "paadal_meaning": "The cases are eight when vocative, which is used when one is addressed, is included among them."
            }
          },
          {
            "paadal": "அவைதாம், \nபெயர் ஐ ஒடு கு \nஇன் அது கண் விளி என்னும் ஈற்ற.",
            "vilakkam": {
              "paadal_category": "Case Types",
              "paadal_meaning": "They are peyar-vēṟṟumai (பெயர் வேற்றுமை), ai vēṟṟumai (ஐ-வேற்றுமை), oṭu vēṟṟumai (ஒடு-வேற்றுமை), ku-vēṟṟumai (கு-வேற்றுமை),  iṉ-vēṟṟumai  (இன்-வேற்றுமை) , atu-vēṟṟumai (அது-வேற்றுமை) , kaṇ-vēṟṟumai (கண்-வேற்றுமை) along with viḷi-vēṟṟumai (விளி-வேற்றுமை)"
            }
          },
          {
            "paadal": "அவற்றுள், \nஎழுவாய் வேற்றுமை பெயர்தோன்று நிலையே.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "Of them, the peyar-vēṟṟumai (பெயர் வேற்றுமை) is used to denote the do-er or the subject of the active verb"
            }
          },
          {
            "paadal": "பொருண்மை சுட்டல் வியங்கொள வருதல் \nவினைநிலை உரைத்தல் வினாவிற்கு ஏற்றல் \nபண்பு கொளவருதல் பெயர் கொளவருதல் என்று \nஅன்றி அனைத்தும் பெயர்ப்பய னிலையே.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "The predicate to a subject may denote one of the following: the existence of the subject, the wish or order of another relating to the subject, the kind of action of the subject, question relating to the subject, the quality of the subject, and the number, class, order, etc. of the subject"
            }
          },
          {
            "paadal": "பெயரின் ஆகிய தொகையுமார் உளவே \nஅவ்வும் உரிய அப்பாலான.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "There are also compounds made up of nouns which, when they take predicates after them, are in the same category, that is, they stand in the nominative case."
            }
          },
          {
            "paadal": "எவ்வயின் பெயரும் வெளிப்படத் தோன்றி \nஅவ்வியல் நிலையல் செவ்விது என்ப.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "It is said that it is advisable for every noun to be mentioned explicitely in such places, that is, when they take predicates after them."
            }
          },
          {
            "paadal": "கூறிய முறையின் உருபுநிலை திரியாது \nஈறு பெயர்க்காகும் இயற்கைய என்ப.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "The case-suffixed mentioned above (in eḻuttatikāram (எழுத்ததிகாரம்): padal no.114 [puṇariyal (புணரியல்) padal no.11]) [ai(ஐ), oṭu(ஒடு), ku(கு), iṉ(இன்), atu(அது), kaṇ(கண்)] are suffixed without any modification in form to nouns."
            }
          },
          {
            "paadal": "பெயர்நிலைக் கிளவி காலம் தோன்றா \nதொழில்நிலை ஒட்டும் ஒன்றலங் கடையே.",
            "vilakkam": {
              "paadal_category": "Nominative case",
              "paadal_meaning": "Nouns excent a class of toḻiṟ-peyar (தொழிற்பெயர்) (verbal nouns) do not denote time."
            }
          },
          {
            "paadal": "இரண்டாகுவதே, \nஐஎனப் பெயரிய வேற்றுமைக் கிளவி \nஎவ்வழி வரினும் வினையே வினைக்குறிப்பு \nஅவ்விரு முதலின் தோன்றும் அதுவே.",
            "vilakkam": {
              "paadal_category": "Accusative case",
              "paadal_meaning": "The second one called ai (ஐ) denotes the direct object of a verb or an appellative verb."
            }
          },
          {
            "paadal": "காப்பின் ஒப்பின் ஊர்தியின் இழையின் \nஒப்பின் புகழின் பழியின் என்றா \nபெறலின் இழவின் காதலின் வெகுளியின் \nசெறலின் உவத்தலின் கற்பின் என்றா \nஅறுத்தலின் குறைத்தலின் தொகுத்தலின் பிரித்தலின் \nநிறுத்தலின் அளவின் எண்ணின் என்றா \nஆக்கலின் சார்தலின் செலவின் கன்றலின் \nநோக்கலின் அஞ்சலின் சிதைப்பின் என்றா \nஅன்ன பிறவும் அம்முதற் பொருள \nஎன்ன கிளவியும் அதன்பால என்மனார்.",
            "vilakkam": {
              "paadal_category": "Accusative case",
              "paadal_meaning": "They say that accusative case denotes the direct object which exists as things that are protected, compared, used as vehicle, made, scared away, praised, despised, acquired, lost, loved, scorned, destroyed, appreciated, learned, cut, decreased, gathered, separated, weighed, measured, counted, improved in condition, depended upon, reached, detested, seen, feared, shattered, etc."
            }
          },
          {
            "paadal": "மூன்றாகுவதே, \nஒடுஎனப் பெயரிய வேற்றுமைக் கிளவி \nவினைமுதல் கருவி அனைமுதற் றதுவே.",
            "vilakkam": {
              "paadal_category": "Instrumental case",
              "paadal_meaning": "The third case called oṭu (ஒடு) denotes the agent or instrument of an action."
            }
          },
          {
            "paadal": "அதனின் இயறல் அதன்தகு கிளவி \nஅதன் வினைப்படுதல் அதனின் ஆதல் \nஅதனின் கோடல் அதனொடு மயங்கல் \nஅதனொடு இயைந்த ஒருவினைக் கிளவி \nஅதனொடு இயைந்த வேறுவினைக் கிளவி \nஅதனொடு இயைந்த ஒப்பல் ஒப்புரை \nஇன் ஆன் ஏது ஈங்கு என வரூஉம் \nஅன்ன பிறவும் அதன்பால என்மனார்.",
            "vilakkam": {
              "paadal_category": "Instrumental case",
              "paadal_meaning": "They say that the instrumental case denotes the object that stands as the material cause, the object that serves as an appropriate cause, the agent of an action, the object that is responsible for one's present state, the object of exchange, the object that is mixed with another, the object in company with another doing the same action, the object in company with another incapable of doing the same action, the object of unsuitable comparison, the object of particular description with reference to limbs, senses, etc, and cause, etc."
            }
          },
          {
            "paadal": "நான்காகுவதே, \nகு எனப்பெயரிய வேற்றுமைக் கிளவி \nஎப்பொருள் ஆயினும் கொள்ளும் அதுவே.",
            "vilakkam": {
              "paadal_category": "Dative case",
              "paadal_meaning": "The fourth called ku-vēṟṟumai (கு-வேற்றுமை) denotes recipient, whatever substance it may be."
            }
          },
          {
            "paadal": "அதற்குவினை உடைமையின் அதற்கு உடம்படுதலின் \nஅதற்குப் படு பொருளின் அதுவாகு கிளவியின் \nஅதற்கு யாப்புடைமையின் அதன் பொருட்டாதலின் \nநட்பின் பகையின் காதலின் சிறப்பின் என்று \nஅப்பொருட் கிளவியும் அதன்பால என்மனார்",
            "vilakkam": {
              "paadal_category": "Dative case",
              "paadal_meaning": "They say that the dative case denotes the object for which an action is done, the object to which one subjects himself, the object to which another is apportioned, the object of transformation, the object which is suited to another, the ain of an action, the object of friendship, enmity, love, superiority, etc."
            }
          },
          {
            "paadal": "ஐந்தாகுவதே, \nஇன் எனப்பெயரிய வேற்றுமைக் கிளவி \nஇதனின் இற்று இது என்னும் அதுவே.",
            "vilakkam": {
              "paadal_category": "Ablative case",
              "paadal_meaning": "The fifth case called iṉ-vēṟṟumai  (இன்-வேற்றுமை) denotes the nature of an object in its relation to another. Comparison, contrast, separation, limit, cause, etc. form the meanings of this case."
            }
          },
          {
            "paadal": "வண்ணம் வடிவே அளவே சுவையே \nதண்மை வெம்மை அச்சம் என்றா \nநன்மை தீமை சிறுமை பெருமை \nவன்மை மென்மை கடுமை என்றா \nமுதுமை இளமை சிறத்தல் இழித்தல் \nபுதுமை பழமை ஆக்கம் என்றா \nஇன்மை உடைமை நாற்றம் தீர்தல் \nபன்மை சின்மை பற்றுவிடுதல் என்று \nஅன்ன பிறவும் அதன்பால என்மனார்.",
            "vilakkam": {
              "paadal_category": "Ablative case",
              "paadal_meaning": "They say that the ablative case denotes colour, shape, measure, taste, coolness, hotness, fear, goodness, badness, smallness, largeness, hardness, softness, ferocity, agedness, youth, superiority, inferiority, newness, oldness, source, absence, presence, smell, separation, many-ness, few-ness, absence of attachment, etc."
            }
          },
          {
            "paadal": "ஆறாகுவதே, \nஅது எனப்பெரிய வேற்றுமைக் கிளவி \nதன்னினும் பிறிதினும் இதனது இது எனும் \nஅன்ன கிளவிக் கிழமைத்து அதுவே.",
            "vilakkam": {
              "paadal_category": "Genitive case",
              "paadal_meaning": "The sixth case called atu-vēṟṟumai (அது-வேற்றுமை) denotes the relation between an object and its inseparable elements or between one object and another."
            }
          },
          {
            "paadal": "இயற்கையின் உடைமையின் முறைமையின் கிழமையின் \nசெயற்கையின் முதுமையின் வினையின் என்றா \nகருவியின் துணையின் கலத்தின் முதலின் \nஒருவழி உறுப்பின் குழுவின் என்றா \nதெரிந்துமொழிச் செய்தியின் நிலையின் வாழ்ச்சியின் \nதிரிந்து வேறுபடூஉம் பிறவும் அன்ன \nகூறிய மருங்கின் தோன்றும் கிளவி \nஆறன் பால என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Genitive case",
              "paadal_meaning": "Wise men say that the sixth case denotes the nature, possession, relationship, connection, action, advanced state, effort, instrument, association, document, capital, limb, collection, composition, state, residence and the rest which come under the category of the species of relation."
            }
          },
          {
            "paadal": "ஏழாகுவதே, \nகண்எ னப்பெயரிய வேற்றுமை கிளவி \nவினைசெய் இடத்தின் நிலத்தின் காலத்தின் \nஅனைவகைக் குறிப்பின் தோன்றும் அதுவே.",
            "vilakkam": {
              "paadal_category": "Locative case",
              "paadal_meaning": "The seventh case called the kaṇ-vēṟṟumai (கண்-வேற்றுமை) denotes the place and time of action."
            }
          },
          {
            "paadal": "கண் கால் புறம் அகம் உள் உழை கீழ் மேல் \nபின் சார் அயல் புடை தேவகை எனாஅ \nமுன் இடை கடை தலை வலம் இடம் எனாஅ \nஅன்ன பிறவும் அதன்பால என்மனார்.",
            "vilakkam": {
              "paadal_category": "Locative case",
              "paadal_meaning": "They say that the locative denotes front part near the top or centre, lower portion, outside portion, inside portion, interior part, nearness, botton, top, back side, neighbouring partm exterior part, the different directions, place in front, middle, end, beginning, right, left, etc."
            }
          },
          {
            "paadal": "வேற்றுமைப் பொருளை விரிக்கும் காலை \nஈற்றுநின்று இயலும் தொகைவயின் பிரிந்து \nபல் ஆறாகப் பொருள் புணர்ந்து இசைக்கும் \nஎல்லாச் சொல்லும் உரிய என்ப.",
            "vilakkam": {
              "paadal_category": "Functional Nature of case morphemes",
              "paadal_meaning": "When one wants to expand the meanings of the cases mentioned above, it is said that all which are synonymous with the words found in the collection at the end (sūtrās 11,13,15,17,19,21) have to added to the list of words ound in each of them."
            }
          }
        ]
      },
      {
        "iyal_name": "வேற்றுமைமயங்கியல்",
        "iyal_eng":"Interchange of Case Morphemes",
        "noorpa": [
          {
            "paadal": "கருமம் அல்லாச் சார்புஎன் கிளவிக்கு \nஉரிமையும் உடைத்தே கண்என் வேற்றுமை.",
            "vilakkam": {
              "paadal_category": "Locative and Accusative Case Morphemes",
              "paadal_meaning": "The seventh case also may be used to denote close relationship except direct impact"
            }
          },
          {
            "paadal": "சினை நிலைக்கிளவிக்கு ஐயும் கண்ணும் \nவினை நிலை ஒக்கும் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Locative and Accusative Case Morphemes",
              "paadal_meaning": "Learned men say that the seventh case is used in the same way as the second after words denoting parts, when they qualify verbs other than appellative verbs."
            }
          },
          {
            "paadal": "கன்றலும் செலவும் ஒன்றுமார் வினையே.",
            "vilakkam": {
              "paadal_category": "Locative and Accusative Case Morphemes",
              "paadal_meaning": "Both the seventh and the cases are used with verbs derived from the roots kaṉṟu (கன்று) and cel (செல்)"
            }
          },
          {
            "paadal": "முதற்சினைக் கிளவிக்கு அது என் வேற்றுமை \nமுதற்கண் வரினே சினைக்கு ஐ வருமே.",
            "vilakkam": {
              "paadal_category": "Genitive and Accusative Case Morphemes",
              "paadal_meaning": "If, in a sentance, there is mention denoting whole and part and the sixth case-suffix is used along with the word denoting the whole, the second case-suffix alone is used along with the word denoting the part."
            }
          },
          {
            "paadal": "முதல்முன் ஐவரின் கண் என் வேற்றுமை \nசினைமுன் வருதல் தெள்ளிது என்ப.",
            "vilakkam": {
              "paadal_category": "Locative and Accusative Case Morphemes",
              "paadal_meaning": "If the second case-suffix is used along with the word denoting the whole, the seventh case is used along with the word denoting the part."
            }
          },
          {
            "paadal": "முதலும் சினையும் பொருள்வேறு படாஅ \nநுவலும் காலைச் சொற்குறிப் பினவே.",
            "vilakkam": {
              "paadal_category": "Context as Criterion",
              "paadal_meaning": "An object cannot, by itself, be taken either as a whole or as a part. It should be suggested by the expression of the speaker."
            }
          },
          {
            "paadal": "பிண்டப் பெயரும் ஆயியல் திரியா \nபண்டியல் மருங்கின் மரீஇய மரபே.",
            "vilakkam": {
              "paadal_category": "Mass Nouns",
              "paadal_meaning": "The word denoting collection of the same nature and should be understood as such from the ancient usage."
            }
          },
          {
            "paadal": "ஒருவினை ஒடுச்சொல் உயர்பின் வழித்தே.",
            "vilakkam": {
              "paadal_category": "A function of Instrumental Case Morphemes",
              "paadal_meaning": "The suffix oṭu (ஒடு) (of third case) is used with the word denoting the superior of the two, when both do the same action."
            }
          },
          {
            "paadal": "மூன்றனும் ஐந்தனும் தோன்றக் கூறிய \nஆக்கமொடு புணர்ந்த ஏதுக் கிளவி \nநோக்கோ ரனைய என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Ablative and Instrumental case morphemes",
              "paadal_meaning": "Learned men say that, on careful consideration, the use of the third case-suffix and that of the fifth case-suffix to denote cause are of the same nature when they qualify a verb formed of the root ā (ஆ) - (meaning to become)"
            }
          },
          {
            "paadal": "இரண்டன் மருங்கின் நோக்கல் நோக்கம் அவ் \nஇரண்டன் மருங்கின் ஏதுவும் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Seeing by the Mind's Eye",
              "paadal_meaning": "The verb meaning 'to observe' may be governed not only by a noun in the second case, but also in the third and fifth cases if the observation is not through the physical eye, but through the mind's eye"
            }
          },
          {
            "paadal": "அது என் வேற்றுமை உயர்திணைத் தொகைவயின் \nஅது என் உருபுகெடக் குகரம் வருமே.",
            "vilakkam": {
              "paadal_category": "Genitive and Dative Case Morphemes",
              "paadal_meaning": "The noun (whose case-suffix is dropped) and about the nature of whose action it is difficult to decide is not prevented from being taken either as the second case or as the third form the sense."
            }
          },
          {
            "paadal": "தடுமாறு தொழிற்பெயர்க்கு இரண்டும் மூன்றும் \nகடிநிலை இலவே பொருள்வயி னான.",
            "vilakkam": {
              "paadal_category": "Instrumental and Accusative Case Morphemes",
              "paadal_meaning": "The intelligent will discriminate from what follows after the last words."
            }
          },
          {
            "paadal": "ஈற்றுப்பெயர் முன்னர் மெய்யறி பனுவலின் \nவேற்றுமை தெரிப உணரு மோரே.",
            "vilakkam": {
              "paadal_category": "Instrumental and Accusative Case Morphemes",
              "paadal_meaning": "The noun which qualifies a verb meaning'to protect' may be in the second case or the third case when the case-suffix is dropped."
            }
          },
          {
            "paadal": "ஓம்படைக் கிளவிக்கு ஐயும் ஆனும் \nதாம் பிரிவிலவே தொகைவரு காலை.",
            "vilakkam": {
              "paadal_category": "Instrumental and Accusative Case Morphemes",
              "paadal_meaning": "The word denoting the recipient of a gift which can afford to have the suffix ku (கு) dropped may take the sixth case-suffix also."
            }
          },
          {
            "paadal": "ஆறன் மருங்கின் வாழ்ச்சிக் கிழமைக்கு \nஏழும் ஆகும் உறைநிலத் தான.",
            "vilakkam": {
              "paadal_category": "Locative and Genitive Case Morphemes",
              "paadal_meaning": "A verb denoting fear may be qualified by a noun either in the fifth case or in the second case."
            }
          },
          {
            "paadal": "குத்தொக வரூஉம் கொடைஎதிர் கிளவி \nஅப்பொருள் ஆறற்கு உரித்தும் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Dative and Genitive Case Morphemes",
              "paadal_meaning": "When a word in sixth case is followed by an uyartiṇai (உயர்திணை ) noun, the suffix atu (அது) is replaced by ku (கு)"
            }
          },
          {
            "paadal": "அச்சக் கிளவிக்கு ஐந்தும் இரண்டும் \nஎச்சம் இலவே பொருள்வயி னான.",
            "vilakkam": {
              "paadal_category": "Ablative and Accusative Case Morphemes",
              "paadal_meaning": "The seventh case also maybe used instead of the sixth case with nouns denoting dwelling place when its relation to the noun which it qualifies is that of the land in habitat and the inhabitat."
            }
          },
          {
            "paadal": "அன்ன பிறவும் தொல்நெறி பிழையாது \nஉருபினும் பொருளினும் மெய்தடு மாறி \nஇருவயின் நிலையும் வேற்றுமை எல்லாம் \nதிரிபிடன் இலவே தெரியு மோர்க்கே.",
            "vilakkam": {
              "paadal_category": "Interchange of Case Morphemes in Tune with Usage",
              "paadal_meaning": "There is no confusion in the minds of the learned with regard to the use of one case-suffix for another or of one case-suffix similar to the cases mentioned above, if it is in confirmity with the ancient usage."
            }
          },
          {
            "paadal": "உருபுதொடர்ந்து அடுக்கிய வேற்றுமைக் கிளவி \nஒருசொல் நடைய பொருள்செல் மருங்கே.",
            "vilakkam": {
              "paadal_category": "Succession of Words in Declension",
              "paadal_meaning": "Words having the same case-suffix may be treated as if they are one if the sense allows it, i.e, they may qualify the same word."
            }
          },
          {
            "paadal": "இறுதியும் இடையும் எல்லா உருபும் \nநெறிபடு பொருள்வயின் நிலவுதல் வரையார்.",
            "vilakkam": {
              "paadal_category": "Medial/Final Declension",
              "paadal_meaning": "(Learned men) do not prevent words having different suffixes at the middle and the end of the expression from qualifying the same (qualifying) word."
            }
          },
          {
            "paadal": "பிறிதுபிறிது ஏற்றலும் உருபுதொக வருதலும் \nநெறிபட வழங்கிய வழிமருங்கு என்ப.",
            "vilakkam": {
              "paadal_category": "Dropping of Case Morphemes",
              "paadal_meaning": "It is said that usage sanctions nouns, with the case-suffixes retained or dropped, qualifying different words in the middle and the end of sentances."
            }
          },
          {
            "paadal": "ஐயும் கண்ணும் அல்லாப் பொருள்வயின் \nமெய்யுருபு தொகாஅ இறுதி யான.",
            "vilakkam": {
              "paadal_category": "Dropping of Case Morphemes",
              "paadal_meaning": "No case-suffix will be elided at the end of a sentance except those of the second and the seventh."
            }
          },
          {
            "paadal": "யாதன் உருபின் கூறிற்று ஆயினும் \nபொருள்செல் மருங்கின் வேற்றுமை சாரும்.",
            "vilakkam": {
              "paadal_category": "Contextuality of Case Morphemes",
              "paadal_meaning": "The meaning of case-suffix can be taken in whatever form it is given expression to."
            }
          },
          {
            "paadal": "எதிர்மறுத்து மொழியினும் தத்தம் மரபின் \nபொருள்நிலை திரியா வேற்றுமைச் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Case Morphemes in Negative Utterances",
              "paadal_meaning": "Case suffixes will have the same meaning even when they qualify a negative verb."
            }
          },
          {
            "paadal": "கு ஐ ஆன் என வரூஉம் இறுதி \nஅவ்வொடு சிவணும் செய்யு ளுள்ளே.",
            "vilakkam": {
              "paadal_category": "Case Morphemes in Poetry",
              "paadal_meaning": "The words having suffixes ku (கு) , ai (ஐ) and āṉ (ஆன்) at the end of a line may be appended by the particle a (அ) in verse."
            }
          },
          {
            "paadal": "அ எனப் பிறத்தல் அஃறிணை மருங்கின் \nகுவ்வும் ஐயும் இல்என மொழிப.",
            "vilakkam": {
              "paadal_category": "Case Morphemes in Poetry",
              "paadal_meaning": "ku (கு) and ai (ஐ) cannot append a (அ) if they are suffixed to aḵṟiṇai (அஃறிணை) names."
            }
          },
          {
            "paadal": "இதன் அது இது இற்று என்னும் கிளவியும் \nஅதனைக் கொள்ளும் பொருள் வயினானும் \nஅதனான் செயற்படற்கு ஒத்த கிளவியும் \nமுறைக்கொண்டு எழுந்த பெயர்ச்சொல் கிளவியும் \nபால்வரை கிளவியும் பண்பின் ஆக்கமும் \nகாலத்தின் அறியும் வேற்றுமைக் கிளவியும் \nபற்றுவிடு கிளவியும் தீர்ந்துமொழிக் கிளவியும் \nஅன்ன பிறவும் நான்கன் உருபின் \nதொல்நெறி மரபின தோன்ற லாறே.",
            "vilakkam": {
              "paadal_category": "Sense Designations of Dative Case Morphemes",
              "paadal_meaning": "The fourth case is used form very ancient times in the following meanings -- in place of the sixth case in such sentances as 'this of this is of this sort'; in place of second case in expressions like 'this will hold that'; in the place of the third case sentances like 'this is fit to done by him'; in place of sixth case denoting relationship; in place of the fifth case denoting the exact position of land and comparison; in place of the seventh casedenoting time; and before the roots paṟṟuviṭu (பற்றுவிடு) and tīr (தீர்) which generally take fifth case."
            }
          },
          {
            "paadal": "ஏனை உருபும் அன்ன மரபின \nமானம் இலவே சொல்முறை யான.",
            "vilakkam": {
              "paadal_category": "Sense Designation of Other Case Morphemes",
              "paadal_meaning": "There will be no harm if other case-suffixes also are used in similar manner."
            }
          },
          {
            "paadal": "வினையே செய்வது செயப்படு பொருளே \nநிலனே காலம் கருவி என்றா \nஇன்னதற்கு இது பயனாக என்னும் \nஅன்ன மரபின் இரண்டொடும் தொகைஇ \nஆயெட்டு என்ப தொழில்முதல் நிலையே.",
            "vilakkam": {
              "paadal_category": "Things a Predicator Implies",
              "paadal_meaning": "(Learned men) say that there are eight things that should precede an action - 'kṛti (कृति) (effort within the body of the door), doer, object of a verb, place, time, instrument, the recipitent and the purpose of doing."
            }
          },
          {
            "paadal": "அவைதாம், \nவழங்கியல் மருங்கின் குன்றுவ குன்றும்.",
            "vilakkam": {
              "paadal_category": "Things a Predicator Implies",
              "paadal_meaning": "Some of them may not be used in actual usage."
            }
          },
          {
            "paadal": "முதலிற் கூறும் சினையறி கிளவியும் \nசினையிற் கூறும் முதல்அறி கிளவியும் \nபிறந்தவழிக் கூறலும் பண்புகொள் பெயரும் \nஇயன்றது மொழிதலும் இருபெய ரொட்டும் \nவினைமுதல் உரைக்கும் கிளவியொடு தொகைஇ \nஅனை மரபினவே ஆகுபெயர்க் கிளவி.",
            "vilakkam": {
              "paadal_category": "Ramifications of Metonymy",
              "paadal_meaning": "ākupeyar (ஆகுபெயர்) or metonymy is one of the following kinds - wholee put for the part, part for the whole, the place of production for the product, quality for the object possesing it, cause for the effect, irupeyaroṭṭu (இருபெயரொட்டு) (the compound made up of two words of wich the second denotes a part and the first an object similar to its or its action), the door for the object done etc."
            }
          },
          {
            "paadal": "அவைதாம், \nதத்தம் பொருள்வயின் தம்மொடு சிவணலும் \nஒப்பில் வழியான் பிறிதுபொருள் சுட்டலும் \nஅப்பண் பினவே நுவலும் காலை \nவேற்றுமை மருங்கின் போற்றல் வேண்டும்.",
            "vilakkam": {
              "paadal_category": "Ramifications of Metonymy",
              "paadal_meaning": "They are two kinds; one denoting those that are connected with them and the other denoting those that are not connected with them. If there is any deviation in literature, they should be taken into account."
            }
          },
          {
            "paadal": "அளவும் நிறையும் அவற்றொடு கொள்வழி \nஉளஎன மொழிப உணர்ந்திசி னோரே.",
            "vilakkam": {
              "paadal_category": "Ramifications of Metonymy",
              "paadal_meaning": "Learned men say that words denoting measures and weights are taken with them."
            }
          },
          {
            "paadal": "கிளந்த அல்ல வேறுபிற தோன்றினும் \nகிளந்தவற்று இயலான் உணர்ந்தனர் கொளலே.",
            "vilakkam": {
              "paadal_category": "Ramifications of Metonymy",
              "paadal_meaning": "If anything not mentioned here appears in literature, it should be taken into account on the lines chalked above."
            }
          }
        ]
      },
      {
        "iyal_name": "விளிமரபு",
        "iyal_eng":"The Vocative Case",
        "noorpa": [
          {
            "paadal": "விளி எனப்படுப கொள்ளும் பெயரொடு \nதெளியத் தோன்றும் இயற்கைய என்ப.",
            "vilakkam": {
              "paadal_category": "The Vocative Case",
              "paadal_meaning": "They say that what is called viḷi (விளி) or the vocative case is of the nature of being explicitly seen in words which take a special form in the vocative case."
            }
          },
          {
            "paadal": "அவ்வே, \nஇவ்என அறிதற்கு மெய்பெறக் கிளப்ப.",
            "vilakkam": {
              "paadal_category": "The Vocative Case",
              "paadal_meaning": "In order to understand what the words which take a special form in the vocative case are, they will be explicitly mentioned."
            }
          },
          {
            "paadal": "அவைதாம், \nஇ உ ஐ ஓ என்னும் இறுதி \nஅப்பால் நான்கே உயர்திணை மருங்கின் \nமெய்ப்பொருள் சுட்டிய விளிகொள் பெயரே.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "Among uyartiṇai (உயர்திணை) nouns those which clearly undergo modification in the vocative case are those that end in the vowels i (இ), u (உ) or ai (ஐ) and ō (ஓ)."
            }
          },
          {
            "paadal": "அவற்றுள், \nஇ ஈ ஆகும் ஐ ஆய் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "Of them nouns ending in ai (ஐ) change to i (இ) and those ending in ai (ஐ) change to āy (ஆய்)."
            }
          },
          {
            "paadal": "ஓவும் உவ்வும் ஏயொடு சிவணும்.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "(Of them) nouns ending in ō (ஓ) and u (உ) take ē (ஏ) after them."
            }
          },
          {
            "paadal": "உகரம் தானே குற்றியலுகரம்.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "The u (உ) referred to above is kuṟṟiyalukaram (குற்றியலுகரம்)."
            }
          },
          {
            "paadal": "ஏனை உயிரே உயர்திணை மருங்கின் \nதாம் விளி கொள்ளா என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "Learned men say that uyartiṇai (உயர்திணை) nouns ending in other vowels do not undergo change in from in the vocative case."
            }
          },
          {
            "paadal": "அளபெடை மிகூஉம் இகர இறுபெயர் \nஇயற்கைய ஆகும் செயற்கைய என்ப.",
            "vilakkam": {
              "paadal_category": "Vocative Case Markers",
              "paadal_meaning": "They say that the nouns having i (இ) as aḷapeṭai (அளபெடை) at the end do not change i (இ) to ī (ஈ) but take only i (இ) after them."
            }
          },
          {
            "paadal": "முறைப்பெயர் மருங்கின் ஐ என் இறுதி \nஆவொடு வருதற்கு உரியவும் உளவே.",
            "vilakkam": {
              "paadal_category": "Kinship Terms",
              "paadal_meaning": "There are some in words of relationship ending in ai (ஐ) that even change to āy (ஆ) (in place of āy (ஆய்).)"
            }
          },
          {
            "paadal": "அண்மைச் சொல்லே இயற்கை ஆகும்.",
            "vilakkam": {
              "paadal_category": "Proximate Addressee",
              "paadal_meaning": "Word in the vocative case which is used to call one near at hand undergoes no modification."
            }
          },
          {
            "paadal": "ன ர ல ள என்னும் அந்நான்கு என்ப \nபுள்ளி இறுதி விளிகொள் பெயரே.",
            "vilakkam": {
              "paadal_category": "Consonantal Vocative Markers",
              "paadal_meaning": "Of the words that end in costants ṉ(ன்), r (ர்), l (ல்) and ḷ (ள்), undergo modification in the vocative case."
            }
          },
          {
            "paadal": "ஏனைப் புள்ளி ஈறுவிளி கொள்ளா.",
            "vilakkam": {
              "paadal_category": "Consonantal Vocative Markers",
              "paadal_meaning": "Words ending in other constants do not undergo change in vocative case."
            }
          },
          {
            "paadal": "அன் என் இறுதி ஆ ஆகும்மே.",
            "vilakkam": {
              "paadal_category": "Consonantal Vocative Markers",
              "paadal_meaning": "Of them, those that end in aṉ (அன்) change to ā (ஆ)"
            }
          },
          {
            "paadal": "அண்மைச் சொல்லிற்கு அகரமும் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Consonantal Vocative Markers",
              "paadal_meaning": "aṉ (அன்) in aṉmai-c-col (அன்மைச்சொல்) is changed to a (அ)"
            }
          },
          {
            "paadal": "ஆன் என் இறுதி இயற்கை ஆகும்.",
            "vilakkam": {
              "paadal_category": "Vocative an ending āṉ (ஆன்)",
              "paadal_meaning": "Words ending in āṉ (ஆன்) do not undergo any change."
            }
          },
          {
            "paadal": "தொழிலின் கூறும் ஆன் என் இறுதி \nஆய் ஆகும்மே விளி வயினான.",
            "vilakkam": {
              "paadal_category": "Vocative an ending āṉ (ஆன்)",
              "paadal_meaning": "Verbal and gerundial nouns ending in āṉ (ஆன்) change āṉ (ஆன்) to āy (ஆய்) in the vocative case."
            }
          },
          {
            "paadal": "பண்புகொள் பெயரும் அதன் ஓரற்றே.",
            "vilakkam": {
              "paadal_category": "Vocative an ending āṉ (ஆன்)",
              "paadal_meaning": "Words denoting quality also are of the same nature."
            }
          },
          {
            "paadal": "அளபெடைப் பெயரே அளபெடை இயல.",
            "vilakkam": {
              "paadal_category": "Vocative an ending āṉ (ஆன்)",
              "paadal_meaning": "Words having aḷapeṭai (அளபெடை) before the final ṉ (q) are of the same nature as words ending in aḷapeṭai (அளபெடை)."
            }
          },
          {
            "paadal": "முறைப்பெயர்க் கிளவி ஏயொடு வருமே.",
            "vilakkam": {
              "paadal_category": "ṉ(ன்)-ending Vocatives",
              "paadal_meaning": "Words of relationship ending in ṉ (ன்) take ē (ஏ) after them."
            }
          },
          {
            "paadal": "தான்என் பெயரும் சுட்டுமுதற் பெயரும் \nயான் என் பெயரும் வினாவின் பெயரும் \nஅன்றி அனைத்தும் விளிகோள் இலவே.",
            "vilakkam": {
              "paadal_category": "ṉ(ன்)-ending Vocatives",
              "paadal_meaning": "The pronouns tāṉ (தான்), avaṉ (அவன்), evaṉ (எவன்), uvaṉ (உவன்), yāṉ (யான்), yāvaṉ (யாவன்), etc., do not take the vocative case."
            }
          },
          {
            "paadal": "ஆரும் அருவும் ஈரொடு சிவணும்.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Words ending in ār(ஆர்) and ar(அர்) change to īr(ஈர்)."
            }
          },
          {
            "paadal": "தொழிற்பெயர் ஆயின் ஏகாரம் வருதலும் \nவழுக்கு இன்று என்மனார் வயங்கியோரே.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Those who know the usage say that it is not wrong if verbal and gerundial nouns take ē (ஏ) also in addition to the modification mentioned in the previous 'sutrā'."
            }
          },
          {
            "paadal": "பண்புகொள் பெயரும் அதன் ஓரற்றே.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Words denoting quality also are the same nature."
            }
          },
          {
            "paadal": "அளபெடைப் பெயரே அளபெடை இயல.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Words ending in r(ர்) and preced by aḷapeṭai (அளபெடை) are the same nature as nouns having aḷapeṭai (அளபெடை) mentioned before."
            }
          },
          {
            "paadal": "சுட்டுமுதற் பெயரே முற்கிளந் தன்ன.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Demonstrative pronouns ending in r(ர்) are of the nature of demonstrative pronouns ending in ṉ (ன்) mentioned above (i.e.) they do not take vocative case."
            }
          },
          {
            "paadal": "நும்மின் திரிபெயர் வினாவின் பெயர் என்று \nஅம்முறை இரண்டும் அவற்று இயல்பு இயலும்.",
            "vilakkam": {
              "paadal_category": "r(ர்)-ending Vocatives",
              "paadal_meaning": "Niyir (நியிர்), the modified form of num (நும்) and interogative pronouns ending in r(ர்) of the same nature."
            }
          },
          {
            "paadal": "எஞ்சிய இரண்டின் இறுதிப் பெயரே \nநின்ற ஈற்றயல் நீட்டம் வேண்டும்.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "Nouns ending in othe two (i.e.) l (ல்) and ḻ (ழ்) have their penultimate vowel lengthened."
            }
          },
          {
            "paadal": "அயல் நெடிதாயின் இயற்கை ஆகும்.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "If the penaltimate is long, they undergo no change."
            }
          },
          {
            "paadal": "வினையினும் பண்பினும் \nநினையத் தோன்றும் ஆள்என் இறுதி \nஆய் ஆகும்மே விளி வயினான.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "Verbal and participal nouns denoting quality ending in āḻ (ஆழ்) change āḻ (ஆழ்) to āy (ஆய்) in the vocative case."
            }
          },
          {
            "paadal": "முறைப்பெயர்க் கிளவி முறைப்பெயர் இயல.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "Words denoting relationship ending in l (ல்) are of the same nature as those ending in ṉ (ன்)."
            }
          },
          {
            "paadal": "சுட்டுமுதற் பெயரும் வினாவின் பெயரும் \nமுன்கிளந் தன்ன என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "Learned men say that demonstrative pronouns and interogative pronouns ending in ḻ (ழ்) are of the same nature as those mentioned above; (i.e.) they do not take vocative case."
            }
          },
          {
            "paadal": "அளபெடைப் பெயரே அளபெடை இயல.",
            "vilakkam": {
              "paadal_category": "l (ல்) and ḻ (ழ்) ending Vocatives",
              "paadal_meaning": "Words ending in l (ல்) and ḻ (ழ்) preceded by aḷapeṭai (அளபெடை) are of the same nature as those which end in ṉ (ன்) and r (ர்) preceded by aḷapeṭai (அளபெடை)."
            }
          },
          {
            "paadal": "கிளந்த இறுதி அஃறிணை விரவுப்பெயர் \nவிளம்பிய நெறிய விளிக்குங் காலை.",
            "vilakkam": {
              "paadal_category": "Mixed Generic Class in the Vocative",
              "paadal_meaning": "Nouns common to uyartiṇai (உயர்திணை ) and aḵṟiṇai(அஃறிணை) ending in the four vowels and constants mentioned above undergo the same modification in vocative case when they are used in aḵṟiṇai (அஃறிணை)."
            }
          },
          {
            "paadal": "புள்ளியும் உயிரும் இறுதி ஆகிய \nஅஃறிணை மருங்கின் எல்லாப் பெயரும் \nவிளிநிலை பெறூஉம் காலம் தோன்றின் \nதெளிநிலை உடைய ஏகாரம் வரலே.",
            "vilakkam": {
              "paadal_category": "Non-Human Class in the Vocative",
              "paadal_meaning": "All nouns in aḵṟiṇai (அஃறிணை) ending in constants and vowels take ē (ஏ) after them in the vocative case."
            }
          },
          {
            "paadal": "உள எனப்பட்ட எல்லாப் பெயரும் \nஅளபு இறந்தனவே விளிக்கும் காலை \nசேய்மையின் இசைக்கும் வழக்கத் தான.",
            "vilakkam": {
              "paadal_category": "Vocative for the Non-Proximate Addressee",
              "paadal_meaning": "All the nouns which are said to undergo modification in the vocative case increase the quantity of the vowels when they are used to summon persons or objects at a distance."
            }
          },
          {
            "paadal": "அம்ம என்னும் அசைச்சொல் நீட்டம் \nஅம்முறைப் பெயரொடு சிவணாது ஆயினும் \nவிளியொடு கொள்ப தெளியுமோரே.",
            "vilakkam": {
              "paadal_category": "Vocative Declension for the Expletive amma (அம்ம)",
              "paadal_meaning": "Scholars take that the word amma (அம்ம) used to draw the attention lengthen its final though it is not included among words of relationship."
            }
          },
          {
            "paadal": "த ந நு எ என அவை முதலாகித் \nதன்மை குறித்த ன ர ள என் இறுதியும் \nஅன்ன பிறவும் பெயர்நிலை வரினே \nஇன்மை வேண்டும் விளியொடு கொளலே.",
            "vilakkam": {
              "paadal_category": "Indeclinable Terms",
              "paadal_meaning": "Words commencing with t (த்), n (ந்), nu (நு), and e (எ) are ending in ṉ (ன்), r (ர்), and ḷ (ள்) and denoting relationship and those of the same nature, do not take vocative case."
            }
          }
        ]
      },
      {
        "iyal_name": "பெயரியல்",
        "iyal_eng":"Nouns",
        "noorpa": [
          {
            "paadal": "எல்லாச் சொல்லும் பொருள் குறித்தனவே.",
            "vilakkam": {
              "paadal_category": "Words as sense units",
              "paadal_meaning": "All words denote meaning."
            }
          },
          {
            "paadal": "பொருண்மை தெரிதலும் சொன்மை தெரிதலும் \nசொல்லின் ஆகும் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Form and meaning",
              "paadal_meaning": "Learned men say that both the meaning and the form may be denoted by a word."
            }
          },
          {
            "paadal": "தெரிபுவேறு நிலையலும் குறிப்பின் தோன்றலும் \nஇருபாற்று என்ப பொருண்மை நிலையே.",
            "vilakkam": {
              "paadal_category": "Two fold sense Designation",
              "paadal_meaning": "They say that denoting meaning is of two kinds one by one connation and other by suggestion."
            }
          },
          {
            "paadal": "சொல் எனப்படுப பெயரே வினையென்று \nஆயிரண்டு என்ப அறிந்திசினோரே.",
            "vilakkam": {
              "paadal_category": "Primary word classes",
              "paadal_meaning": "Learned men say that word is of two kinds - noun and verb."
            }
          },
          {
            "paadal": "இடைச்சொல் கிளவியும் உரிச்சொல் கிளவியும் \nஅவற்றுவழி மருங்கின் தோன்றும் என்ப.",
            "vilakkam": {
              "paadal_category": "Secondary word classes",
              "paadal_meaning": "They say that iṭai-c-col (இடைச்சொல்) and uri-c-col (உரிச்சொல்) from part of them are used along with them."
            }
          },
          {
            "paadal": "அவற்றுள், \nபெயர் எனப்படுபவை தெரியுங் காலை \nஉயர்திணைக்கு உரிமையும் அஃறிணைக்கு உரிமையும் \nஆயிரு திணைக்கும் ஓரன்ன உரிமையும் \nஅம்மூ உருபின தோன்றல் ஆறே.",
            "vilakkam": {
              "paadal_category": "Threefold classification of nouns",
              "paadal_meaning": "Of them nouns, on investigation are three kinds in usage those denoting uyartiṇai (உயர்திணை ) those denoting aḵṟiṇai (அஃறிணை) and those denoting either of them."
            }
          },
          {
            "paadal": "இருதிணைப் பிரிந்த ஐம்பால் கிளவிக்கும் \nஉரியவை உரிய பெயர்வயி னான.",
            "vilakkam": {
              "paadal_category": "Gender distinction in nouns",
              "paadal_meaning": "Among nouns particular words have the capacity to denote particular pāl (பால்) among the five pāls (பால்s) of two tiṇais (திணைs)."
            }
          },
          {
            "paadal": "அவ்வழி, \nஅவன் இவன் உவன் என வரூஉம் பெயரும் \nஅவள் இவள் உவள் என வரூஉம் பெயரும் \nஅவர் இவர் உவர் என வரூஉம் பெயரும் \nயான் யாம் நாம் என வரூஉம் பெயரும் \nயாவன் யாவள் யாவர் என்னும் \nஆவயின் மூன்றொடு அப்பதினைந்தும் \nபால்அறி வந்த உயர்திணைப் பெயரே.",
            "vilakkam": {
              "paadal_category": "Gender Distinction in human class nouns",
              "paadal_meaning": "Of them the following fifteen mentioned in three groups are uyarthinai nouns denoting different pāls (பால்s): \n(1) avaṉ (அவன்) ,ivaṉ (இவன்), uvaṉ (உவன்), avaḷ (அவள்), ivaḷ (இவள்), uvaḷ (உவள்), avar (அவர்), ivar (இவர்) and uvar (உவர்)\n(2) yāṉ (யான்) , yām (யாம்) and nām (நாம்) \n(3) yāvaṉ (யாவன்), yāvaḷ (யாவள்) and yāvar (யாவர்) "
            }
          },
          {
            "paadal": "ஆண்மை அடுத்த மகன் என்கிளவியும் \nபெண்மை அடுத்த மகள் என்கிளவியும் \nபெண்மை அடுத்த இகர இறுதியும் \nநம்ஊர்ந்து வரூஉம் இகர ஐகாரமும் \nமுறைமை சுட்டா மகனும் மகளும் \nமாந்தர் மக்கள் என்னும் பெயரும் \nஆடூஉ மகடூஉ ஆயிரு கிளவியும் \nசுட்டு முதலாகிய அன்னும் ஆனும் \nஅவை முதலாகிய பெண்டுஎன் கிளவியும் \nஒப்பொடு வரூஉம் கிளவியொடு தொகைஇ \nஅப்பதினைந்தும் அவற்றோ ரன்ன.",
            "vilakkam": {
              "paadal_category": "Gender Distinction in human class nouns",
              "paadal_meaning": "The following fifteen belong to the same category: āṇmakaṉs (ஆண்மகன்), peṇmakaṉ (பெண்மகன்), peṇtāṭṭi (பெண்தாட்டி), nampi (நம்பி), naṅkai (நங்கை), makaṉ (மகன்), and makaḷ (மகள்) not denoting relationship māntar (மாந்தர்), makkal (மக்கல்), āṭū (ஆடூ), makaṭū (மகடூ) words beginning with demonstrative roots and ending in aṉ (அன்) and āṉ (ஆன்) like attaṉmaiyaṉ (அத்தன்மையன்), aṉaiyāṉ (அனையான்), words beginning with demonstrative roots and ending in feminine suffix like attaṉmaiyaḷ (அத்தன்மையள்), aṉaiyāḷ (அனையாள்), words ending in aṉ (அன்), āṉ (ஆன்), aḷ (அள்), āḷ (ஆள்) preceded by the particle denoting similarly like poṉṉaṉṉaṉ (பொன்னன்னன்), poṉṉaṉṉal (பொன்னன்னல்) etc."
            }
          },
          {
            "paadal": "எல்லாரும் என்னும் பெயர்நிலைக் கிளவியும் \nஎல்லீரும் என்னும் பெயர்நிலைக் கிளவியும் \nபெண்மை அடுத்த மகன்என் கிளவியும் \nஅன்ன இயல என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Gender Distinction in human class nouns",
              "paadal_meaning": "Learned  men say that ellārum (எல்லாரும்), ellīrum (எல்லீரும்) and  peṇmakaṉ (பெண்மகன்) too are of the same nature."
            }
          },
          {
            "paadal": "நிலப்பெயர் குடிப்பெயர் குழுவின் பெயரே \nவினைப்பெயர் உடைப்பெயர் பண்புகொள் பெயரே \nபல்லோர்க் குறித்த முறைநிலைப் பெயரே \nபல்லோர்க் குறித்த சினைநிலைப் பெயரே \nபல்லோர்க் குறித்த திணைநிலைப் பெயரே \nகூடிவரு வழக்கின் ஆடுஇயல் பெயரே \nஇன்றிவர் என்னும் எண்ணியல் பெயரொடு \nஅன்றி அனைத்தும் அவற்று இயல்பினவே.",
            "vilakkam": {
              "paadal_category": "Gender Distinction in human class nouns",
              "paadal_meaning": "Personal names derived from country, family, group, profession and quality, plural nouns denoting relationship, peculiarity of limbs, and caste, catch names used at play by children and personal nouns derived from numerals all are of the same nature."
            }
          },
          {
            "paadal": "அன்ன பிறவும் உயர்திணை மருங்கில் \nபன்மையும் ஒருமையும் பால்அறி வந்த \nஎன்ன பெயரும் அத்திணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "Gender Distinction in human class nouns",
              "paadal_meaning": "Similar nouns denoting uyartiṇai (உயர்திணை) used in singular and plural to denote the pāls (பால்s) are of that tiṇai (திணை)."
            }
          },
          {
            "paadal": "அது இது உது என வரூஉம் பெயரும் \nஅவை முதலாகிய ஆய்தப் பெயரும் \nஅவை இவை உவை என வரூஉம் பெயரும் \nஅவை முதலாகிய வகரப் பெயரும் \nயாது யா யாவை என்னும் பெயரும் \nஆவயின் மூன்றொடு அப்பதினைந்தும் \nபால்அறி வந்த அஃறிணைப் பெயரே.",
            "vilakkam": {
              "paadal_category": "Gender identification in non-human classes",
              "paadal_meaning": "Atu (அது), itu (இது), utu (உது), aḵtū (அஃதூ), iḵtū (இஃதூ), uḵtū (உஃதூ), avai (அவை), ivai (இவை), uvai (உவை), av (அவ்), iv (இவ்), uv (உவ்), yātū (யாதூ), yā (யா), yāvai (யாவை) these fifteen mentioned in three groups are aḵṟiṇai (அஃறிணை) nouns denoting pāl (பால்). utu (உது), uḵtū (உஃதூ), av (அவ்), iv (இவ்), uv (உவ்) and yā (யா) have become obsolete."
            }
          },
          {
            "paadal": "பல்ல பல சில என்னும் பெயரும் \nஉள்ள இல்ல என்னும் பெயரும் \nவினைப்பெயர்க் கிளவியும் பண்புகொள் பெயரும் \nஇனைத்து எனக்கிளக்கும் எண்ணுக்குறிப் பெயரும் \nஒப்பின் ஆகிய பெயர்நிலை உளப்பட \nஅப்பால் ஒன்பதும் அவற்றோ ரன்ன.",
            "vilakkam": {
              "paadal_category": "Gender identification in non-human classes",
              "paadal_meaning": "Palla (பல்ல), pala (பல), cila (சில), uḷḷa (உள்ள), illa (இல்ல) and  numerals and words ending in suffixes preceded by particles of comparison these nine also are of the same value."
            }
          },
          {
            "paadal": "கள்ளொடு சிவணும் அவ்இயற் பெயரே \nகொள்வழி உடைய பலஅறி சொற்கே.",
            "vilakkam": {
              "paadal_category": "Number in  the non-human class nouns",
              "paadal_meaning": "aḵṟiṇai-iyarpeyar (அஃறிணை இயர்பெயர்) may also optionally take the suffix kaḷ (கள்) to denote palviṉpāl (பல்வின்பால்)."
            }
          },
          {
            "paadal": "அன்ன பிறவும் அஃறிணை மருங்கின் \nபன்மையும் ஒருமையும் பால்அறி வந்த \nஎன்ன பெயரும் அத்திணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "Number in  the non-human class nouns",
              "paadal_meaning": "Similar nouns denoting aḵṟiṇai (அஃறிணை) used in similar and plural to denote the pāls (பால்s) are of that tiṇai (திணை)."
            }
          },
          {
            "paadal": "தெரிநிலை உடைய அஃறிணை இயற்பெயர் \nஒருமையும் பன்மையும் வினையொடு வரினே.",
            "vilakkam": {
              "paadal_category": "Number in  the non-human class nouns",
              "paadal_meaning": "The common noun in aḵṟiṇai (அஃறிணை) which is not suffixed with kaḷ (கள்) is determined to be singular or plural according as it is followed by a singular, or plural, verb."
            }
          },
          {
            "paadal": "இருதிணைச் சொற்கும் ஓரன்ன உரிமையின் \nதிரிபு வேறுபடூஉம் எல்லாப் பெயரும் \nநினையும் காலை தத்தம் மரபின் \nவினையொடு அல்லது பால்தெரிபு இலவே.",
            "vilakkam": {
              "paadal_category": "Mixed class nouns",
              "paadal_meaning": "All nouns which may be used both as uyartiṇai (உயர்திணை) and aḵṟiṇai (அஃறிணை) do not clearly show to which tiṇai (திணை) they belong except through the verbs which they take after them."
            }
          },
          {
            "paadal": "நிகழூஉ நின்ற பலர்வரை கிளவியின் \nஉயர்திணை ஒருமை தோன்றலும் உரித்தே \nஅன்ன மரபின் வினைவயி னான.",
            "vilakkam": {
              "paadal_category": "Mixed class nouns",
              "paadal_meaning": "A noun common to uyartiṇai (உயர்திணை) and aḵṟiṇai (அஃறிணை) may also be determined to denote uyartiṇai (உயர்திணை) singular through particular verbs of the form ceyyum (செய்யும்) suited to it."
            }
          },
          {
            "paadal": "இயற்பெயர் சினைப்பெயர் சினைமுதற்பெயரே \nமுறைப்பெயர்க் கிளவி தாமே தானே \nஎல்லாம் நீயிர் நீஎனக் கிளந்து \nசொல்லிய அல்ல பிறவும் ஆஅங்கு \nஅன்னவை தோன்றின் அவற்றொடும் கொளலே.",
            "vilakkam": {
              "paadal_category": "Mixed class nouns",
              "paadal_meaning": "Noun other than a derivative name, noun denoting the peculiarity of limbs, non denoting the peculiarty of limb and whole, noun denoting relationship, tāṉ (தான்), tām (தாம்), ellām (எல்லாம்), nīyir ( நீயிர்), nī (நீ) and others of the same nature should be taken to belong to that class."
            }
          },
          {
            "paadal": "அவற்றுள், \nநான்கே இயற்பெயர் நான்கே சினைப்பெயர் \nநான்கென மொழிமனார் சினைமுதற் பெயரே \nமுறைப்பெயர்க் கிளவி இரண்டு ஆகும்மே \nஏனைப் பெயரே தத்தம் மரபின.",
            "vilakkam": {
              "paadal_category": "Mixed class nouns",
              "paadal_meaning": "Of the iyar-peyar (இயர் பெயர்), ciṉai-p-peyar (சினைப்பெயர்) and ciṉai-mutar-peyar (சினை முதர் பெயர்) are each of four kinds, murai-p-peyar (முரைப்பெயர்) is of two kinds and the rest is of only one kind sanctioned by usage."
            }
          },
          {
            "paadal": "அவைதாம், \nபெண்மை இயற்பெயர் ஆண்மை இயற்பெயர் \nபன்மை இயற்பெயர் ஒருமை இயற்பெயர் என்று \nஅந்நான்கு என்ப இயற்பெயர் நிலையே.",
            "vilakkam": {
              "paadal_category": "Non-derivative proper nouns",
              "paadal_meaning": "The kinds if iyar-peyar (இயர் பெயர்) are those denoting peṇmai (பெண்மை) (female), āṇmai (ஆண்மை) (male), paṉmai (பன்மை) (plural), and orumai (ஒருமை) (singular)."
            }
          },
          {
            "paadal": "பெண்மைச் சினைப்பெயர் ஆண்மைச் சினைப்பெயர் \nபன்மைச் சினைப்பெயர் ஒருமைச் சினைப்பெயர் என்று \nஅந்நான்கு என்ப சினைப்பெயர் நிலையே.",
            "vilakkam": {
              "paadal_category": "Nouns designating limbs",
              "paadal_meaning": "The kinds of ciṉai-p-peyar (சினைப்பெயர்) are those denoting peṇmai (பெண்மை), āṇmai (ஆண்மை), paṉmai (பன்மை), and orumai (ஒருமை)."
            }
          },
          {
            "paadal": "பெண்மை சுட்டிய சினைமுதற் பெயரே \nஆண்மை சுட்டிய சினைமுதற் பெயரே \nபன்மை சுட்டிய சினைமுதற் பெயரே \nஒருமை சுட்டிய சினைமுதற் பெயர் என்று \nஅந்நான்கு என்ப சினைமுதற் பெயரே.",
            "vilakkam": {
              "paadal_category": "Nouns designating limb-whole enitities",
              "paadal_meaning": "The kinds of ciṉai-mutar-peyar (சினை முதர் பெயர்) are those denoting peṇmai (பெண்மை), āṇmai (ஆண்மை), paṉmai (பன்மை) and orumai (ஒருமை)."
            }
          },
          {
            "paadal": "பெண்மை முறைப்பெயர் ஆண்மை முறைப்பெயர் என்று \nஆயிரண்டு என்ப முறைப்பெயர் நிலையே.",
            "vilakkam": {
              "paadal_category": "Kinship nouns",
              "paadal_meaning": "The kinds of murai-p-peyar (முரைப்பெயர்) are those denoting peṇmai (பெண்மை) and āṇmai (ஆண்மை)."
            }
          },
          {
            "paadal": "பெண்மை சுட்டிய எல்லாப் பெயரும் \nஒன்றற்கும் ஒருத்திக்கும் ஒன்றிய நிலையே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "All nouns denoting peṇmai (பெண்மை) can denote an object of aḵṟiṇai (அஃறிணை) or uyartiṇai (உயர்திணை) of the female sex."
            }
          },
          {
            "paadal": "ஆண்மை சுட்டிய எல்லாப் பெயரும் \nஒன்றற்கும் ஒருவற்கும் ஒன்றிய நிலையே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "All nouns denoting āṇmai (ஆண்மை) can denote an object of aḵṟiṇai (அஃறிணை) or uyartiṇai (உயர்திணை) of the male sex."
            }
          },
          {
            "paadal": "பன்மை சுட்டிய எல்லாப் பெயரும் \nஒன்றே பலவே ஒருவர் என்னும் \nஎன்று இப்பாற்கும் ஓரன்னவ்வே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "All nouns denoting paṉmai (பன்மை) can denote one or more objects of aḵṟiṇai (அஃறிணை), one man or one women."
            }
          },
          {
            "paadal": "ஒருமை சுட்டிய எல்லாப் பெயரும் \nஒன்றற்கும் ஒருவர்க்கும் ஒன்றிய நிலையே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "All nouns denoting orumai (ஒருமை) denote an object of aḵṟiṇai (அஃறிணை) or uyartiṇai (உயர்திணை)."
            }
          },
          {
            "paadal": "தாம் என்கிளவி பன்மைக்கு உரித்தே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "The word tām (தாம்) is plural in number."
            }
          },
          {
            "paadal": "தான் என்கிளவி ஒருமைக்கு உரித்தே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "The word tāṉ (தான்) singular in number."
            }
          },
          {
            "paadal": "எல்லாம் என்னும் பெயர்நிலைக் கிளவி \nபல்வழி நுதலிய நிலைத்து ஆகும்மே",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "The word ellām (எல்லாம்) is plural in numbers."
            }
          },
          {
            "paadal": "தன்உள்ளுறுத்த பன்மைக்கு அல்லது \nஉயர்திணை மருங்கின் ஆக்கம் இல்லை.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "Ellām (எல்லாம்) is not used in uyartiṇai (உயர்திணை) except in first person plural."
            }
          },
          {
            "paadal": "நீயிர் நீ என வரூஉம் கிளவி \nபால்தெரிபு இலவே உடன்மொழிப் பொருள.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "The words nīyir (நீயிர்) and nī (நீ) do not express the pāl from their form and they are common to many pāls (பால்s). (i.e) the word nīyir (நீயிர்) is common to palarpāl (பலர்பால்) and palaviṉpāl (பலவின்பால்) and the word nī (நீ) is common to āṇpāl (ஆண்பால்), peṇpāl (பெண்பால்) and oṉraṉpāl (ஒன்ரன்பால்)."
            }
          },
          {
            "paadal": "அவற்றுள், \nநீஎன் கிளவி ஒருமைக்கு உரித்தே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "Of them nī (நீ) is singular in number."
            }
          },
          {
            "paadal": "ஏனைக் கிளவி பன்மைக்கு உரித்தே.",
            "vilakkam": {
              "paadal_category": "Mixed nouns",
              "paadal_meaning": "The other word (nīyir (நீயிர்)) is plural in number."
            }
          },
          {
            "paadal": "ஒருவர் என்னும் பெயர்நிலைக் கிளவி \nஇருபாற்கும் உரித்தே தெரியும் காலை.",
            "vilakkam": {
              "paadal_category": "Gender designation of oruvar ",
              "paadal_meaning": "The noun oruvar (ஒருவர்) is seen to be common to the two pāls (பால்)- āṇpāl (ஆண்பால்) and peṇpāl (பெண்பால்)."
            }
          },
          {
            "paadal": "தன்மை சுட்டின் பன்மைக்கு ஏற்கும்.",
            "vilakkam": {
              "paadal_category": "Gender designation of oruvar ",
              "paadal_meaning": "If one uses it as the subject, it takes a plural predicate after it."
            }
          },
          {
            "paadal": "இன்ன பெயரே இவைஎனல் வேண்டின் \nமுன்னம் சேர்த்தி முறையின் உணர்தல்.",
            "vilakkam": {
              "paadal_category": "Gender designation of oruvar",
              "paadal_meaning": "If one wishes to understand the nature of these words (i.e) nīyir (நீயிர்), nī (நீ) and oruvar (ஒருவர்), he has to determine it form the context combined with the intention of the speaker."
            }
          },
          {
            "paadal": "மகடூஉ மருங்கின் பால்திரி கிளவி \nமகடூஉ இயற்கை தொழில்வயி னான.",
            "vilakkam": {
              "paadal_category": "Aberrant Forms",
              "paadal_meaning": "The word peṇmakaṉ (பெண்மகன்) which takes a masculine ending through denoting a female is of the nature of peṇpāl (பெண்பால்) words when it takes a predicate after it."
            }
          },
          {
            "paadal": "ஆ ஓ ஆகும் பெயருமார் உளவே \nஆயிடன் அறிதல் செய்யுளுள்ளே.",
            "vilakkam": {
              "paadal_category": "Aberrant Forms",
              "paadal_meaning": "There are words where in ā (ஆ) changes to ō (ஓ) and they have to be determined from poetic literature."
            }
          },
          {
            "paadal": "இறைச்சிப் பொருள்வயின் செய்யுளுள் கிளக்கும் \nஇயற்பெயர்க் கிளவி உயர்திணை சுட்டா \nநிலத்துவழி மருங்கின் தோன்ற லான.",
            "vilakkam": {
              "paadal_category": "Aberrant Forms",
              "paadal_meaning": "The nouns which can denote both uyartiṇai (உயர்திணை) and aḵṟiṇai (அஃறிணை) do not denote the former, if they are used in poetry to denote the karu-p-poruḷ (கருப்பொருள்) (animal,bird etc) of a tract of land."
            }
          },
          {
            "paadal": "திணையொடு பழகிய பெயர் அலங்கடையே.",
            "vilakkam": {
              "paadal_category": "Aberrant Forms",
              "paadal_meaning": "Except those which have been used to denote both the tiṇai (திணை) (i.e) some which have been so used may denote uyartiṇai (உயர்திணை)."
            }
          }
        ]
      },
      {
        "iyal_name": "வினையியல்",
        "iyal_eng":"Verbs",
        "noorpa": [
          {
            "paadal": "வினை எனப்படுவது வேற்றுமை கொள்ளாது \nநினையும் காலைக் காலமொடு தோன்றும்.",
            "vilakkam": {
              "paadal_category": "Verbs described",
              "paadal_meaning": "That which is called viṉai (வினை ) (verb) does not take case-suffixes after it and denotes tense on scrutiny."
            }
          },
          {
            "paadal": "காலம் தாமே மூன்று என மொழிப.",
            "vilakkam": {
              "paadal_category": "Tenses",
              "paadal_meaning": "They say that tenses are in three numbers."
            }
          },
          {
            "paadal": "இறப்பின் நிகழ்வின் எதிர்வின் என்றா \nஅம்முக் காலமும் குறிப்பொடும் கொள்ளும் \nமெய்ந்நிலை உடைய தோன்ற லாறே.",
            "vilakkam": {
              "paadal_category": "Tenses",
              "paadal_meaning": "The three tenses past, present and future are denoted even by viṉai–k-kuṟippū (வினைக்குறிப்பூ)."
            }
          },
          {
            "paadal": "குறிப்பினும் வினையினும் நெறிப்படத் தோன்றிக் \nகாலமொடு வரூஉம் வினைச்சொல் எல்லாம் \nஉயர்திணைக்கு உரிமையும் அஃறிணைக்கு உரிமையும் \nஆயிரு திணைக்கும் ஓரன்ன உரிமையும் \nஅம்மூ உருபின தோன்ற லாறே.",
            "vilakkam": {
              "paadal_category": "Verbs classes and their threefold assignment",
              "paadal_meaning": "All verbs denoting tense consisting of appellatative verbs and terinilai viṉai (தெரிநிலை வினை) are, when they used, of three kinds those belonging to uyartiṇai (உயர்திணை), those belonging to aḵṟiṇai (அஃறிணை) and those belonging to both."
            }
          },
          {
            "paadal": "அவைதாம், \nஅம் ஆம் எம் ஏம் என்னும் கிளவியும் \nஉம்மொடு வரூஉம் க ட த ற என்னும் \nஅந்நாற் கிளவியொடு ஆயெண் கிளவியும் \nபன்மை உரைக்கும் தன்மைச் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Termination of first person plural verbs",
              "paadal_meaning": "The first person plural verbs are those that take the eight termination am (அம்), ām (ஆம்), em (எம்), ēm ( ஏம் ), kum (கும்), ṭum (டும்), tum (தும்), and ṟum (றும்)."
            }
          },
          {
            "paadal": "க ட த ற என்னும் \nஅந்நான்கு ஊர்ந்த குன்றியலுகரமொடு \nஏன் அல் என வரூஉம் ஏழும் \nதன்வினை உரைக்கும் தன்மைச் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Termination of first person plural verbs",
              "paadal_meaning": "The first person singular verbs are those that take any one of the seven termination kū (கூ), ṭū (டூ), tū (தூ), rū (ரூ), eṉ (என் ), ēṉ (ஏன்), and al (அல்))."
            }
          },
          {
            "paadal": "அவற்றுள், \nசெய்கு என் கிளவி வினையொடு முடியினும் \nஅவ்வியல் திரியாது என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Termination of first person plural verbs",
              "paadal_meaning": "Learned men say that, of them the form ceykū (செய்கூ) does not lose its finite when it is followed by another finite verb.."
            }
          },
          {
            "paadal": "அன் ஆன் அள் ஆள் என்னும் நான்கும் \nஒருவர் மருங்கின் படர்க்கைச் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Terminations of third person singular verbs",
              "paadal_meaning": "The third person singular verbs of uyartiṇai (உயர்திணை) are those that take the termination aṉ (அன்), āṉ (ஆன்), aḷ (அள்) and āḷ (ஆள்)."
            }
          },
          {
            "paadal": "அர் ஆர் ப என வரூஉம் மூன்றும் \nபல்லோர் மருங்கின் படர்க்கைச் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Termination of third person plural verbs",
              "paadal_meaning": "The third person plural verbs of uyartiṇai (உயர்திணை) are those that takes the terminations aṉ (அன்), āṉ (ஆன்) and pa (ப)."
            }
          },
          {
            "paadal": "மாரைக் கிளவியும் பல்லோர் படர்க்கை \nகாலக் கிளவியொடு முடியும் என்ப.",
            "vilakkam": {
              "paadal_category": "Termination of third person plural verbs",
              "paadal_meaning": "The third person plural verbs of uyartiṇai (உயர்திணை) are those that takes the terminations aṉ (அன்), āṉ (ஆன்) and pa (ப)."
            }
          },
          {
            "paadal": "பன்மையும் ஒருமையும் பால்அறி வந்த \nஅந்நால் ஐந்தும் மூன்று தலையிட்ட \nமுன்னுறக் கிளந்த உயர்திணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "The termination all together",
              "paadal_meaning": "The twenty three verbs mentioned above denoting plural and singular belong to uyartiṇai (உயர்திணை), which has already been mentioned in sūtra 201 (paadal 4)."
            }
          },
          {
            "paadal": "அவற்றுள், \nபன்மை உரைக்கும் தன்மைக் கிளவி \nஎண்ணீயல் மருங்கின் திரிபவை உளவே.",
            "vilakkam": {
              "paadal_category": "Verbs in addictive contexts",
              "paadal_meaning": "Of them the verbs of the first person plural may, when used with objects that are counted, change in its use, (i.e.) may be used along with a subject in aḵṟiṇai (அஃறிணை). "
            }
          },
          {
            "paadal": "யா அர் என்னும் வினாவின் கிளவி \nஅத்திணை மருங்கின் முப்பாற்கும் உரித்தே",
            "vilakkam": {
              "paadal_category": "Interrogative appellative verb",
              "paadal_meaning": "The interrogative predicate yār (யார்) can be used with nouns of three pāls (பால்s) of uyartiṇai (உயர்திணை)."
            }
          },
          {
            "paadal": "பால்அறி மரபின் அம்மூ ஈற்றும் \nஆ ஓ ஆகும் செய்யுளுள்ளே.",
            "vilakkam": {
              "paadal_category": "Change of termination with /aa/- initial",
              "paadal_meaning": "ā (ஆ) in those endings ā (ஆ), āl (ஆ), and ār (ஆ) denoting pāl may change to ō (ஓ) in poetry."
            }
          },
          {
            "paadal": "ஆய் என் கிளவியும் அவற்றொடு கொள்ளும்.",
            "vilakkam": {
              "paadal_category": "Change of termination with /aa/- initial",
              "paadal_meaning": "The termination āy (ஆய்) (to be said in the sūtra 223 (paadal 26)) will also will be similar to them."
            }
          },
          {
            "paadal": "அதுச்சொல் வேற்றுமை உடைமை யானும் \nகண் என் வேற்றுமை நிலத்தி னானும் \nஒப்பினானும் பண்பினானும் என்று \nஅப்பால் காலம் குறிப்பொடு தோன்றும்",
            "vilakkam": {
              "paadal_category": "Nature of Appellative verbs",
              "paadal_meaning": "The appellative verbs will have for their stem words denoting possession which is the meaning of the sixth case, words denoting place which is the meaning of the seventh case and words denoting comparison and quality."
            }
          },
          {
            "paadal": "அன்மையின் இன்மையின் உண்மையின் வன்மையின் \nஅன்ன பிறவும் குறிப்பொடு கொள்ளும் \nஎன்ன கிளவியும் குறிப்பே காலம்.",
            "vilakkam": {
              "paadal_category": "Nature of Appellative verbs",
              "paadal_meaning": "Words denoting anyōnyābhāva (अन्योन्याभाव), atyantābhāva (अत्यन्ताभाव), existence and capacity and other words of"
            }
          },
          {
            "paadal": "பன்மையும் ஒருமையும் பால்அறி வந்த \nஅன்ன மரபின் குறிப்பொடு வரூஉம் \nகாலக் கிளவி உயர்திணை மருங்கின் \nமேலைக் கிளவியொடு வேறுபாடு இலவே",
            "vilakkam": {
              "paadal_category": "Nature of Appellative verbs",
              "paadal_meaning": "Appellative verbs of uyartiṇai (உயர்திணை) do not differ from terinilai (தெரிநிலை) verbs mentioned above in taking the verbal terminations of the different pāls (பால்s) denoting singular or plural. "
            }
          },
          {
            "paadal": "அ ஆ வ என வரூஉம் இறுதி \nஅப்பால் மூன்றே பலவற்றுப் படர்க்கை.",
            "vilakkam": {
              "paadal_category": "Terminations of Non-human class verbs",
              "paadal_meaning": "The third person neutral plural verbs take the terminations a (அ), ā (ஆ) and va (வ)."
            }
          },
          {
            "paadal": "ஒன்றன் படர்க்கை த ற ட ஊர்ந்த \nகுன்றிய லுகரத்து இறுதி ஆகும்.",
            "vilakkam": {
              "paadal_category": "Terminations of Non-human class verbs",
              "paadal_meaning": "The third person neutral singulrar verbs take terminations tū (தூ), ṟū (றூ) and ṭū (டூ)."
            }
          },
          {
            "paadal": "பன்மையும் ஒருமையும் பால்அறி வந்த \nஅம்மூ இரண்டும் அஃறிணை யவ்வே.",
            "vilakkam": {
              "paadal_category": "Terminations of Non-human class verbs",
              "paadal_meaning": "The six verbs mentioned above denoting plural and simiar belong to aḵṟiṇai (அஃறிணை)."
            }
          },
          {
            "paadal": "அத்திணை மருங்கின் இருபாற் கிளவிக்கும் \nஒக்கும் என்ப எவன் என் வினாவே.",
            "vilakkam": {
              "paadal_category": "Terminations of Non-human class verbs",
              "paadal_meaning": "The interrogative predicate evaṉ (எவன்) can be used with nouns of both pāls (பால்s) of aḵṟiṇai (அஃறிணை)."
            }
          },
          {
            "paadal": "இன்று இல உடைய என்னும் கிளவியும் \nஅன்று உடைத்து அல்ல என்னும் கிளவியும் \nபண்பு கொள் கிளவியும் உளஎன் கிளவியும் \nபண்பின் ஆகிய சினைமுதற் கிளவியும் \nஒப்பொடு வரூஉம் கிளவியொடு தொகைஇ \nஅப்பால் பத்தும் குறிப்பொடு கொள்ளும்.",
            "vilakkam": {
              "paadal_category": "Non-human class appellative verbs",
              "paadal_meaning": "Appellative verbs are ten: iṉṟū (இன்றூ), ila (இல), uṭaiya (உடைய), aṉṟū (அன்றூ), uṭaittū (உடைத்தூ ), alla (அல்ல), verbs with stem denoting quality, uḷa (உள), verbs with stem denoting qualified limbs, and verbs with stem denoting comparison."
            }
          },
          {
            "paadal": "பன்மையும் ஒருமையும் பால்அறி வந்த \nஅன்ன மரபின் குறிப்பொடு வரூஉம் \nகாலக் கிளவி அஃறிணை மருங்கின் \nமேலைக் கிளவியொடு வேறுபாடு இலவே.",
            "vilakkam": {
              "paadal_category": "Non-human class appellative verbs",
              "paadal_meaning": "Appellative verbs of aḵṟiṇai (அஃறிணை) do not differ from terinilai (தெரிநிலை) verbs mentioned above in taking the verbal terminations of the pāls (பால்s) denoting plural and singular."
            }
          },
          {
            "paadal": "முன்னிலை வியங்கோள் வினையெஞ்சு கிளவி \nஇன்மை செப்பல் வேறுஎன் கிளவி \nசெய்ம்மன செய்யும் செய்த என்னும் \nஅம்முறை நின்ற ஆயெண் கிளவியும் \nதிரிபு வேறு படூஉம் செய்திய வாகி \nஇருதிணைச் சொற்கும் ஓரன்ன உரிமைய.",
            "vilakkam": {
              "paadal_category": "Verbs common to human and Non-human classes",
              "paadal_meaning": "Verbs of the second person and verbs of the potential mood, infinitives, the words illai (இல்லை) , il (இல்) etc. that denote negation, the word vēṟū (வேறூ) and the verbs of the type ceymmaṉa (செய்ம்மன), ceyyum (செய்யும்) and ceyla (செய்ல) all these eight may be used in both the tiṇais (திணை) differing in their meaning when used in either."
            }
          },
          {
            "paadal": "அவற்றுள், \nமுன்னிலைக் கிளவி \nஇ ஐ ஆய் என வரூஉம் மூன்றும் \nஒப்பத் தோன்றும் ஒருவர்க்கும் ஒன்றற்கும்.",
            "vilakkam": {
              "paadal_category": "Second person singular teriminations",
              "paadal_meaning": "Of them, the verbs which take the second person termimnations i (இ), ai (ஐ) and āy (ஆய்) denote the singular both in uyartiṇai (உயர்திணை) and in aḵṟiṇai (அஃறிணை)."
            }
          },
          {
            "paadal": "இர் ஈர் மின் என வரூஉம் மூன்றும் \nபல்லோர் மருங்கினும் பலவற்று மருங்கினும் \nசொல்லோர் அனைய என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Second person plural terminations",
              "paadal_meaning": "Learned men say that the verbs which take the terminations ir (இர்), īr (ஈர்) and miṉ (மின்) are of the same from in the plural number of the second person both in uyartiṇai (உயர்திணை) and in aḵṟiṇai (அஃறிணை)."
            }
          },
          {
            "paadal": "எஞ்சிய கிளவி இடத்தொடு சிவணி \nஐம்பாற்கும் உரிய தோன்றல் ஆறே.",
            "vilakkam": {
              "paadal_category": "Terminations of all persons",
              "paadal_meaning": "The rest may be used in the three persons of the five pāls (பால்s)."
            }
          },
          {
            "paadal": "அவற்றுள், \nமுன்னிலை தன்மை ஆயீர் இடத்தொடு \nமன்னாது ஆகும் வியங்கோட் கிளவி.",
            "vilakkam": {
              "paadal_category": "Verbs in the optative mood",
              "paadal_meaning": "Of them, the verb in the potential mood is not used either in the second person or the first person."
            }
          },
          {
            "paadal": "பல்லோர் படர்க்கை முன்னிலை தன்மை \nஅவ்வயின் மூன்றும் நிகழும் காலத்துச் \nசெய்யும் என்னும் கிளவியொடு கொள்ளா.",
            "vilakkam": {
              "paadal_category": "Finite verbs of ceyyum (செய்யும்) pattern ",
              "paadal_meaning": "The finite verb of the form ceyyum (செய்யும்) which is used only in the present tense is not used in palarpāl (பலர்பால்) and in the second and first persons."
            }
          },
          {
            "paadal": "செய்து செய்யூ செய்பு செய்தென \nசெய்யியர் செய்யிய செயின் செய செயற்கு என \nஅவ்வகை ஒன்பதும் வினையெஞ்சு கிளவி.",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "Infinitives are of nine types ceytū (செய்தூ), ceyyū (செய்யூ ), ceypū (செய்பூ), ceyleṉa (செய்லென), ceyyiyar (செய்யியர்), ceyyiya (செய்யிய), ceyiṉ (செயின்), ceya (செய) and ceyarkū (செயர்கூ)."
            }
          },
          {
            "paadal": "பின் முன் கால் கடை வழி இடத்து என்னும் \nஅன்ன மரபின் காலம் கண்ணிய \nஎன்ன கிளவியும் அவற்று இயல்பினவே",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "Words ending in piṉ (பின்), muṉ (முன்), kāl (கால்), kaṭai (கடை), vaḻi (வழி), iṭam (இடம்) and those ending in words denoting time are of the same nature."
            }
          },
          {
            "paadal": "அவற்றுள், \nமுதல்நிலை மூன்றும் வினைமுதல் முடி",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "Of them, the first three (ceytū (செய்தூ), ceyyū (செய்யூ ), ceypū (செய்பூ) modify a verb which has for its subject its own."
            }
          },
          {
            "paadal": "அம்முக் கிளவியும் சினைவினை தோன்றின் \nசினையொடு முடியா முதலொடு முடியினும் \nவினை ஓரனைய என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "Through those three take for their subject a limb, yet they may modify a verb whose subject is the whole."
            }
          },
          {
            "paadal": "ஏனை எச்சம் வினைமுத லானும் \nஆன்வந்து இயையும் வினைநிலை யானும் \nதாம்இயல் மருங்கின் முடியும் என்ப.",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "The other infinitives may modify verbs which have for their subjects their own or other verbs that may suit."
            }
          },
          {
            "paadal": "பன்முறை யானும் வினையெஞ்சு கிளவி \nசொன்முறை முடியாது அடுக்குந வரினும் \nமுன்னது முடிய முடியுமன் பொருளே.",
            "vilakkam": {
              "paadal_category": "Participles of Formulaic patterns",
              "paadal_meaning": "Infinitives of different kind used in one sentence, though that which precedes does not modify that which follows, may be used if they modify the last."
            }
          },
          {
            "paadal": "நிலனும் பொருளும் காலமும் கருவியும் \nவினைமுதற் கிளவியும் வினையும் உளப்பட \nஅவ்ஆறு பொருட்கும் ஓரன்ன உரிமைய \nசெய்யும் செய்த என்னும் சொல்லே.",
            "vilakkam": {
              "paadal_category": "Participial premodifiers of nouns",
              "paadal_meaning": "The peyar-eccams (பெயர் எச்சம்) ceyyum (செய்யும்) and ceyta (செய்த) qualify the following six words denoting land, object, time, instrument, agent and action."
            }
          },
          {
            "paadal": "அவற்றொடு வருவழிச் செய்யும் என்கிளவி \nமுதற்கண் வரைந்த மூவீற்றும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Participial premodifiers of nouns",
              "paadal_meaning": "When ceyyum (செய்யும்) qualifies the above six it may be used even in such pāls (பால்s) as were not sanctioned before (for the finite verb ceyyum)."
            }
          },
          {
            "paadal": "பெயரெஞ்சு கிளவியும் வினையெஞ்சு கிளவியும் \nஎதிர்மறுத்து மொழியினும் பொருள்நிலை திரியா.",
            "vilakkam": {
              "paadal_category": "Participial premodifiers of nouns",
              "paadal_meaning": "peyar-eccam (பெயர் எச்சம்) and viṉai-y-eccam (வினையெச்சம்), though used in the negative form, are treated  in the same way."
            }
          },
          {
            "paadal": "தத்தம் எச்சமொடு சிவணும் குறிப்பின் \nஎச்சொல் ஆயினும் இடைநிலை வரையார்.",
            "vilakkam": {
              "paadal_category": "Participial premodifiers of nouns",
              "paadal_meaning": "They do not discredit the use of a suitable word between peyar-eccam (பெயர் எச்சம்) and viṉai-y-eccam (வினையெச்சம்) and the words which they qualify or modify."
            }
          },
          {
            "paadal": "அவற்றுள், \nசெய்யும் என்னும் பெயரெஞ்சு கிளவிக்கு \nமெய்யொடும் கெடுமே ஈற்றுமிசை உகரம் \nஅவ்விடன் அறிதல் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Participial premodifiers of nouns",
              "paadal_meaning": "Learned men say that yu in the peyar-eccam (பெயர் எச்சம்) ceyyum (செய்யும்) is dropped sometimes and it should be found out (by scholars)."
            }
          },
          {
            "paadal": "செய்துஎன் எச்சத்து இறந்த காலம் \nஎய்துஇடன் உடைத்தே வாராக் காலம்.",
            "vilakkam": {
              "paadal_category": "Extented time references",
              "paadal_meaning": "The infinitive ceytū (செய்தூ) which denotes past tense may also denote future tense."
            }
          },
          {
            "paadal": "முந்நிலைக் காலமும் தோன்றும் இயற்கை \nஎம்முறைச் சொல்லும் நிகழும் காலத்து \nமெய்ந்நிலைப் பொதுச்சொல் கிளத்தல் வேண்டும்.",
            "vilakkam": {
              "paadal_category": "Extented time references",
              "paadal_meaning": "The form of the finite verb ceyyum (செய்யும்) should be used to denote things which prove true for all times-past, present and future."
            }
          },
          {
            "paadal": "வாராக் காலத்தும் நிகழும் காலத்தும் \nஓராங்கு வரூஉம் வினைச்சொற் கிளவி \nஇறந்த காலத்துக் குறிப்பொடு கிளத்தல் \nவிரைந்த பொருள என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Extented time references",
              "paadal_meaning": "Learned men say that a verb is used in the past tense instead of in the present and future tenses to denote haste."
            }
          },
          {
            "paadal": "மிக்கதன் மருங்கின் வினைச்சொல் சுட்டி \nஅப்பண்பு குறித்த வினைமுதற் கிளவி \nசெய்வது இல்வழி நிகழும் காலத்து \nமெய்பெறத் தோன்றும் பொருட்டு ஆகும்மே.",
            "vilakkam": {
              "paadal_category": "A function of ceyyum (செய்யும்) verb",
              "paadal_meaning": "The verb that is used in a general statement to denote the fruit of an extraordinary acion (whether noble or heinous) is used in the present tense, even though a particular man has not done it."
            }
          },
          {
            "paadal": "இதுசெயல் வேண்டும் என்னும் கிளவி \nஇருவயின் நிலையும் பொருட்டு ஆகும்மே \nதன் பாலானும் பிறன் பாலானும்.",
            "vilakkam": {
              "paadal_category": "Imperative verbs",
              "paadal_meaning": "The verb ceyal-vēṇṭum (செயல் வேண்டும்) may be both taṉ-viṉai (தன் வினை) or simple verb and piṟa-viṉai (பிற வினை) or casual verb."
            }
          },
          {
            "paadal": "வன்புற வரூஉம் வினாவுடை வினைச்சொல் \nஎதிர்மறுத்து உணர்த்துதற்கு உரிமையும் உடைத்தே.",
            "vilakkam": {
              "paadal_category": "Verbs with interrogative marker",
              "paadal_meaning": "Interrogative verb used to denote certainly may also denote negation"
            }
          },
          {
            "paadal": "வாராக் காலத்து வினைச்சொற் கிளவி \nஇறப்பினும் நிகழ்வினும் சிறப்பத் தோன்றும் \nஇயற்கையும் தெளிவும் கிளக்கும் காலை.",
            "vilakkam": {
              "paadal_category": "Extended time references",
              "paadal_meaning": "Verbs are used in the past and present tenses to denote future in general statements and statements of assertion."
            }
          },
          {
            "paadal": "செயப்படு பொருளைச் செய்தது போலத் \nதொழிற்படக் கிளத்தலும் வழக்கியல் மரபே.",
            "vilakkam": {
              "paadal_category": "Ascribed agentive function",
              "paadal_meaning": "There is usage where object is also used as subject."
            }
          },
          {
            "paadal": "இறப்பே எதிர்வே ஆயிரு காலமும் \nசிறப்பத் தோன்றும் மயங்குமொழிக் கிளவி.",
            "vilakkam": {
              "paadal_category": "content of blending of time references",
              "paadal meaning": "They do not forbit"
            }
          },
            {
              "paadal": "ஏனைக் காலமும் மயங்குதல் வரையார்.",
              "vilakkam": {
                "paadal_category": "Context of blending of time references",
                "paadal_meaning": "They do not forbid the use of the one tense for the another in the case of other tenses also."
              }
            }
          ]
      },
      {
          "iyal_name": "இடையியல்",
          "iyal_eng":"Structural Morphemes",
          "noorpa": [
            {
              "paadal": "இடைஎனப் படுப பெயரொடும் வினையொடும் \nநடைபெற்று இயலும் தமக்கு இயல்பு இலவே.",
              "vilakkam": {
                "paadal_category": "A Functional Definition of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "iṭaiccol (இடைச்சொல்) is used only with nouns and verbs and not separately."
              }
            },
            {
              "paadal": "அவைதாம், \nபுணரியல் நிலையிடைப் பொருள்நிலைக்கு உதநவும் \nவினைசெயல் மருங்கின் காலமொடு வருநவும் \nவேற்றுமைப் பொருள்வயின் உருபு ஆகுநவும் \nஅசைநிலைக் கிளவி ஆகி வருநவும் \nஇசைநிறைக் கிளவி ஆகி வருநவும் \nதத்தம் குறிப்பின் பொருள் செய்குநவும் \nஒப்புஇல் வழியான் பொருள் செய்குநவும் என்று \nஅப்பண் பினவே நுவலும் காலை.",
              "vilakkam": {
                "paadal_category": "Classes of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "They (iṭaiccol (இடைச்சொல்) are cāriyais (சாரியைs) which are used in sandhi, verbal, terminations, case-suffixes, expletive particles, euphonic particles, suggestive particles and particles of comparison not derived from the roots which mean similarity."
              }
            },
            {
              "paadal": "அவைதாம், \nமுன்னும் பின்னும் மொழியடுத்து வருதலும் \nதம்ஈறு திரிதலும் பிறிதவண் நிலையலும் \nஅன்னவை எல்லாம் உரிய என்ப.",
              "vilakkam": {
                "paadal_category": "An Extended Function of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "They say that they come after or before words, that they may be modified at the irends and that one maybe followed by another and soon."
              }
            },
            {
              "paadal": "கழிவே ஆக்கம் ஒழியிசைக் கிளவி என்று \nஅம்மூன்று என்ப மன்னைச் சொல்லே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle maṉ (மன்) denotes what is past, what is to come and what is left understood."
              }
            },
            {
              "paadal": "விழைவே காலம் ஒழியிசைக் கிளவியென்று \nஅம்மூன்று என்ப தில்லைச் சொல்லே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle thil (த்இல்) denotes desire, time and something which is understood."
              }
            },
            {
              "paadal": "அச்சம் பயமிலி காலம் பெருமை என்று \nஅப்பால் நான்கே கொன்னைச் சொல்லே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle koṉ (கொன்) denotes fear, uselessness, time and greatness."
              }
            },
            {
              "paadal": "எச்சம் சிறப்பே ஐயம் எதிர்மறை \nமுற்றே எண்ணே தெரிநிலை ஆக்கமென்று \nஅப்பால் எட்டே உம்மைச் சொல்லே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle um (உம்) denotes the following eight :- incompletion, superiority, doubt, negation, completion, number, definiteness, and that which is to come."
              }
            },
            {
              "paadal": "பிரிநிலை வினாவே எதிர்மறை ஒழியிசை \nதெரிநிலைக் கிளவி சிறப்பொடு தொகைஇ \nஇருமூன்று என்ப ஓகா ரம்மே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle ō (ஓ) denotes the following six :- exclusion, question, negation, that which is left understood, definiteness and superiority."
              }
            },
            {
              "paadal": "தேற்றம் வினாவே பிரிநிலை எண்ணே \nஈற்றசை இவ்வைந்து ஏகா ரம்மே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle ē (ஏ) denotes the following five :- Certainty, question exclusion, number and final expletive syllable."
              }
            },
            {
              "paadal": "வினையே குறிப்பே இசையே பண்பே \nஎண்ணே பெயரொடு அவ்வறு கிளவியும் \nகண்ணிய நிலைத்தே எனவென் கிளவி.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle eṉa (என) denotes the following six :- verb, suggestion, sound, quality, number and noun."
              }
            },
            {
              "paadal": "என்றுஎன் கிளவியும் அதனோ ரற்றே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle eṉṟu (என்று) also is of the same nature."
              }
            },
            {
              "paadal": "விழைவின் தில்லை தன்னிடத்து இயலும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle til (தில்) when it denotes desire is used along with the verb of the first person."
              }
            },
            {
              "paadal": "தெளிவின் ஏயும் சிறப்பின் ஓவும் \nஅளபின் எடுத்த இசைய என்ப.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle ē (ஏ) denoting certainty and the particle ō (ஓ) denoting superiority may lenghten their maatras."
              }
            },
            {
              "paadal": "மற்றுஎன் கிளவி வினைமாற்று அசைநிலை \nஅப்பால் இரண்டென மொழிமனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Learned men say that the particle maṟṟū (மற்றூ) denotes change of viṉai (வினை) and expletion."
              }
            },
            {
              "paadal": "எற்றுஎன் கிளவி இறந்த பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle eṟṟū (எற்றூ) denotes what is past."
              }
            },
            {
              "paadal": "மற்றையது என்னும் கிளவி தானே \nசுட்டுநிலை ஒழிய இனம் குறித்தன்றே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle maṟṟaiyatū (மற்றையதூ) denotes objects of the same class as of those which have been excluded."
              }
            },
            {
              "paadal": "மன்றஎன் கிளவி தேற்றம் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle maṉṟa (மன்ற) denotes certainty."
              }
            },
            {
              "paadal": "தஞ்சக் கிளவி எண்மைப் பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle tañcam (தஞ்சம்) denotes the state of being easy."
              }
            },
            {
              "paadal": "அந்தில் ஆங்க அசைநிலைக் கிளவிஎன்று \nஆயிரண்டு ஆகும் இயற்கைத்து என்ப.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "They say that the particle antil (அந்தில்) denotes 'that place' and is used as an expletive."
              }
            },
            {
              "paadal": "கொல்லே ஐயம்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle kol (கொல்) denotes doubt."
              }
            },
            {
              "paadal": "எல்லே இலக்கம்",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle el (எல்) denotes brightness."
              }
            },
            {
              "paadal": "இயற்பெயர் முன்னர் ஆரைக் கிளவி \nபலர்க்குரி எழுத்தின் வினையொடு முடிமே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The termination ār (ஆர்) which is used in the verbs of palarpāl (பலர்பால்) is used with iyaṟ-peyar (இயற்பெயர்))."
              }
            },
            {
              "paadal": "அசைநிலைக் கிளவி ஆகுவழி அறிதல்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "One should understand where it becomes an expletive."
              }
            },
            {
              "paadal": "ஏயும் குரையும் இசைநிறை அசைநிலை \nஆயிரண்டு ஆகும் இயற்கைய என்ப.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particles ē (ஏ) and kurai are used both as euphonic particles and expletives."
              }
            },
            {
              "paadal": "மாஎன் கிளவி வியங்கோள் அசைச்சொல்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "the particle mā is used as an expletive with a viyañkōḷ (வியஞ்கோள்) verb."
              }
            },
            {
              "paadal": "மியா இக மோ மதி இகும் சின் என்னும் \nஆவயின் ஆறும் முன்னிலை அசைச்சொல்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The following six miyā (மியா), ika (இக), mō (மோ), mati (மதி), ikum (இகும்), ciṉ (சின்) are used as expletives with verbs of second person."
              }
            },
            {
              "paadal": "அவற்றுள், \nஇகுமும் சின்னும் ஏனை இடத்தொடும் \nதகுநிலை உடைய என்மனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Learned men say that, of them, ikum (இகும்) and ciṉ (சின்) are used with verbs of other persons also."
              }
            },
            {
              "paadal": "அம்ம கேட்பிக்கும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle amma (அம்ம) is used to invite the attention of the hearer."
              }
            },
            {
              "paadal": "ஆங்க உரையசை.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle āñka (ஆஞ்க) is used as an expletive."
              }
            },
            {
              "paadal": "ஒப்பில் போலியும் அப்பொருட்டு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle pōli (போலி) not meaning resemblance is also used as an expletive."
              }
            },
            {
              "paadal": "யா கா \nபிற பிறக்கு அரோ போ மாது என வரூஉம் \nஆயேழ் சொல்லும் அசைநிலைக் கிளவி.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The following seven yā (யா), kā (கா), piṟa (பிற), piṟakku (பிறக்கு ), arō (அரோ), pō (போ), mātu (மாது) are used as expletives."
              }
            },
            {
              "paadal": "ஆக ஆகல் என்பது என்னும் \nஆவயின் மூன்றும் பிரிவில் அசைநிலை.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "āka (ஆக), ākal (ஆகல்) and eṉpatū (என்பதூ) are doubled when they are expletives."
              }
            },
            {
              "paadal": "ஈர்ளபு இசைக்கும் இறுதியில் உயிரே \nஆயியல் நிலையும் காலத்தானும் \nஅளபெடை நிலையும் காலத்தானும் \nஅளபெடை இன்றித் தான்வரும் காலையும் \nஉளஎன மொழிப பொருள் வேறுபடுதல் \nகுறிப்பின் இசையால் நெறிப்படத் தோன்றும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "They say that the vowel au (ஔ) which has two mātras and which has been said that it cannot be final has difference in meaning when it is doubled as said in the previous sūtra or lengthens its mātra and is used alone. Its meaning has to be determined by the difference in the tone of the speaker."
              }
            },
            {
              "paadal": "நன்று ஈற்று ஏயும் அன்று ஈற்று ஏயும் \nஅந்து ஈற்று ஓவும் அன் ஈற்று ஓவும் \nஅன்ன பிறவும் குறிப்பொடு கொள்ளும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particles naṉṟē (நன்றே), aṉṟē (அன்றே), antō (அந்தோ) and aṉṉō (அன்னோ) and those of the same nature denote different meanings through the difference in tone."
              }
            },
            {
              "paadal": "எச்ச உம்மையும் எதிர்மறை உம்மையும் \nதத்தமுள் மயங்கும் உடனிலை இலவே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle um (உம்) denoting eccam and that denoting etir-maṟai (எதிர் மறை) are not used together in a sentence."
              }
            },
            {
              "paadal": "எஞ்சுபொருட் கிளவி செஞ்சொல் ஆயின் \nபிற்படக் கிளவார் முற்படக் கிளத்தல்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "If one of the words connected by and (அந்) and is devoid of the particle um (உம்), it may be used as the former member and not as the latter member."
              }
            },
            {
              "paadal": "முற்றிய உம்மைத் தொகைச்சொல் மருங்கின் \nஎச்சக் கிளவி உரித்தும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle um (உம்) denoting completion used a word denoting number may also denote eccam (எச்சம்)."
              }
            },
            {
              "paadal": "ஈற்று நின்று இசைக்கும் ஏஎன் இறுதி \nகூற்றுவயின் ஒரளபு ஆகலும் உரித்தே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "ī (ஈ) used at the end of a stanza may have also one mātrā."
              }
            },
            {
              "paadal": "உம்மை எண்ணும் எனஎன் எண்ணும் \nதம்வயின் தொகுதி கடப்பாடு இலவே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particles um (உம்) and eṉa denoting number may also be followed by a word denoting number."
              }
            },
            {
              "paadal": "எண் ஏகாரம் இடையிட்டுக் கொளினும் \nஎண்ணுக் குறித்து இயலும் என்மனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Learned men say that ē (ஏ) denoting number, though not used incessantly but used at intervals, may be taken to denote number."
              }
            },
            {
              "paadal": "உம்மை தொக்க எனாஎன் கிளவியும் \nஆ ஈறு ஆகிய என்றுஎன் கிளவியும் \nஆயிரு கிளவியும் எண்ணுவழிப் பட்டன.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particles eṉavum (எனவும்) and eṉṟum (என்றும்) are used without um (உம்) to denote number."
              }
            },
            {
              "paadal": "அவற்றின் வரூஉம் எண்ணின் இறுதியும் \nபெயர்க்குரி மரபின் செவ்வெண் இறுதியும் \nஏயின் ஆகிய எண்ணின் இறுதியும் \nயாவயின் வரினும் தொகையின்று இயலா.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Eṉā (எனா), eṉṟā (என்றா), cevveṇ (செவ்வெண்) and ē (ஏ) denoting number are not used without being followed by a word denoting number."
              }
            },
            {
              "paadal": "உம்மை எண்ணின் உருபு தொகல் வரையார்.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "They do not prevent the elision of um (உம்)."
              }
            },
            {
              "paadal": "உம் உந்து ஆகும் இடனுமார் உண்டே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particle um (உம்) in ceyyum (செய்யும்) is also changed to uṇṭū (உண்டூ) in certain places."
              }
            },
            {
              "paadal": "வினையொடு நிலையினும் எண்ணுநிலை திரியா \nநினையல் வேண்டும் அவற்றவற்று இயல்பே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "It should be remembered that the particles used in the sense of and (அந்) do not change their nature even when they are used with verbs."
              }
            },
            {
              "paadal": "என்றும் எனவும் ஒடுவும் தோன்றி \nஒன்றுவழி உடைய எண்ணினுள் பிரிந்தே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "The particles eṉṟū (என்றூ), eṉa (என) and oṭu (ஒடு) though used once may be taken along with others when hey are used in the sense of and (அந்)."
              }
            },
            {
              "paadal": "அவ்வச் சொல்லிற்கு அவையவை பொருளென \nமெய்பெறக் கிளந்த இயல ஆயினும் \nவினையொடும் பெயரொடும் நினையத் தோன்றித் \nnதிரிந்து வேறுபடினும் தெரிந்தனர் கொளலே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Learned men should take such meanings not specified here but suggested in particular combinations with nouns and verbs, even though it has been clearly shown that each particle denotes particular meanings."
              }
            },
            {
              "paadal": "கிளந்த அல்ல வேறுபிற தோன்றினும் \nகிளந்தவற்று இயலான் உணர்ந்தனர் கொளலே.",
              "vilakkam": {
                "paadal_category": "Multivalent Significations of iṭaiccol (இடைச்சொல்)",
                "paadal_meaning": "Learned men will have to take, in the light of what has been mentioned, other particles not mentioned here which come to their notice."
              }
            }
          ]
      },
      {
          "iyal_name": "உரியியல்",
          "iyal_eng":"Indeclinables",
          "noorpa": [
            {
              "paadal": "உரிச்சொற் கிளவி விரிக்குங் காலை \nஇசையினும் குறிப்பினும் பண்பினும் தோன்றி \nபெயரினும் வினையினும் மெய்தடுமாறி \nஒருசொல் பலபொருட்கு உரிமை தோன்றினும் \nபலசொல் ஒருபொருட்கு உரிமை தோன்றினும் \nபயிலாத வற்றைப் பயின்றவை சார்த்தி \nதத்தம் மரபின் சென்றுநிலை மருங்கின் \nஎச்சொல் ஆயினும் பொருள்வேறு கிளத்தல்.",
              "vilakkam": {
                "paadal_category": "Uriccol (உரிச்சொல்) - A Description",
                "paadal_meaning": "Uriccol (உரிச்சொல்) when classified in detail, denotes sound, suggestion or quality and has its form modified both in nouns and verbs; one of them, may have many meanings or many of them may have one meaning; one should give, from usage, the meaning of that which is not frequently used through another which is frequently used."
              }
            },
            {
              "paadal": "வெளிப்படு சொல்லே கிளத்தல் வேண்டா \nவெளிப்பட வாரா உரிச்சொல் மேன",
              "vilakkam": {
                "paadal_category": "Classes of uriccol (உரிச்சொல்)",
                "paadal_meaning": "It is not necessary to give the meaning of roots easily known and it is necessary to give below the meaning of roots not easily known."
              }
            },
            {
              "paadal": "அவைதாம், \nஉறு தவ நனி என வரூஉம் மூன்றும் \nமிகுதி செய்யும் பொருள என்ப.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "There are three roots : uṟu (உறு), tava (தவ) and naṉi (நனி), which mean much or many."
              }
            },
            {
              "paadal": "உரு உட்கு ஆகும் புரை உயர்பு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "uṟu (உறு) means dread and purai means greatness"
              }
            },
            {
              "paadal": "குருவும் கெழுவும் நிறன் ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kuru (குரு) and keḻu (கெழு) denotes colous"
              }
            },
            {
              "paadal": "சல்லல் இன்னல் இன்னாமையே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "cellai (செல்லை) and iṉṉal (இன்னல்) marks distress"
              }
            },
            {
              "paadal": "மல்லல் வளனே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "mallal (மல்லல்) means fertility"
              }
            },
            {
              "paadal": "ஏ பெற்று ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ē (ஏ) means abundance"
              }
            },
            {
              "paadal": "உகப்பே உயர்தல் உவப்பே உவகை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ukappu (உகப்பு) means height and uvappu (உவப்பு) means delight"
              }
            },
            {
              "paadal": "பயப்பே பயனாம்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "payappu (பயப்பு) means fruit or profit"
              }
            },
            {
              "paadal": "பசப்பு நிறனாகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "pacappu (பசப்பு) denotes sallow complextion"
              }
            },
            {
              "paadal": "இயைபே புணர்ச்சி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "iyaipu (இயைபு) means unity"
              }
            },
            {
              "paadal": "இசைப்பு இசையாகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "icaipu (இசைபு) denotes sound"
              }
            },
            {
              "paadal": "அலமரல் தெருமரல் ஆயிரண்டும் சுழற்சி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "alamaral (அலமரல்) and terumaral (தெருமரல்) mean reeling"
              }
            },
            {
              "paadal": "மழவும் குழவும் இளமைப் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "maḻa (மழ) and kuḻa (குழ) mean infancy"
              }
            },
            {
              "paadal": "சீர்த்தி மிகுபுகழ்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "cīrtti (சீர்த்தி) means great fame"
              }
            },
            {
              "paadal": "மாலை இயல்பே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "mālai (மாலை) means nature/characteristics"
              }
            },
            {
              "paadal": "கூர்ப்பும் கழிவும் உள்ளது சிறக்கும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kūrppu (கூர்ப்பு) and kaḻivu (கழிவு) mean superiority"
              }
            },
            {
              "paadal": "கதழ்வும் துனைவும் விரைவின் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kalaḻvu (கலழ்வு) and tuṉaivu (துனைவு) mean hastiness or quickness"
              }
            },
            {
              "paadal": "அதிர்வும் விதிர்ப்பும் நடுக்கம் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "atirvu (அதிர்வு) and vitirppu (விதிர்ப்பு) mean shaking or trembling."
              }
            },
            {
              "paadal": "வார்தல் போகல் ஒழுகல் மூன்றும் \nநேர்பும் நெடுமையும் செய்யும் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vārtal (வார்தல்), pōkal (போகல்) and oḻukal (ஒழுகல்) mean the state of being straight and long."
              }
            },
            {
              "paadal": "தீர்தலும் தீர்த்தலும் விடற்பொருட்டு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "tīrtal (தீர்தல்) and tīrttal (தீர்த்தல்) mean separation."
              }
            },
            {
              "paadal": "கெடவரல் பண்ணை ஆயிரண்டும் விளையாட்டு.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "keṭavaral (கெடவரல்) and paṇṇai (பண்ணை) both mean play."
              }
            },
            {
              "paadal": "தடவும் கயவும் நளியும் பெருமை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "taṭa (தட), kaya (கய) and naḷi (நளி) mean greatness or bigness."
              }
            },
            {
              "paadal": "அவற்றுள், \nதடஎன் கிளவி கோட்டமும் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Of them the word taṭa (தட) may also mean curvedness."
              }
            },
            {
              "paadal": "கயஎன் கிளவி மென்மையும் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word kaya (கய) may also mean tenderness."
              }
            },
            {
              "paadal": "நளிஎன் கிளவி செறிவும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word naḷi (நளி) may also mean denseness."
              }
            },
            {
              "paadal": "பழுது பயம் இன்றே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "paḻutu (பழுது) means uselessness."
              }
            },
            {
              "paadal": "சாயல் மென்மை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "cāyaṉ (சாயன்) means weakness or tenderness."
              }
            },
            {
              "paadal": "முழுது என்கிளவி எஞ்சாப் பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word muḻutu (முழுது) means completeness."
              }
            },
            {
              "paadal": "வம்பு நிலை இன்மை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vampu (வம்பு) means transitoriness or insecurity"
              }
            },
            {
              "paadal": "மாதர் காதல்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "mātar (மாதர்) means desire or love."
              }
            },
            {
              "paadal": "நம்பும் மேவும் நசை ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "nampu (நம்பு) and mēvu (மேவு) mean desire."
              }
            },
            {
              "paadal": "ஓய்தல் ஆய்தல் நிழத்தல் சாஅய் \nஆவயின் நான்கும் உள்ளதன் நுணுக்கம்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ōytal (ஓய்தல்), āytal (ஆய்தல்), niḷattal (நிளத்தல்) and cāy (சாய்), all the four, mean decreasem emaciation or fatigue."
              }
            },
            {
              "paadal": "புலம்பே தனிமை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "pulanpu (புலந்பு) means loneliness."
              }
            },
            {
              "paadal": "துவன்று நிறைவாகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "tuvaṉṟu (துவன்று) means fulness."
              }
            },
            {
              "paadal": "முரஞ்சல் முதிர்வே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "murañcal (முரஞ்சல்) means maturity"
              }
            },
            {
              "paadal": "வெம்மை வேண்டல்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vemmai (வெம்மை) means desire"
              }
            },
            {
              "paadal": "பொற்பே பொலிவு.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "poṟpu (பொற்பு) means magnificence."
              }
            },
            {
              "paadal": "வறிது சிறிது ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vaṟitu (வறிது) means smallness."
              }
            },
            {
              "paadal": "எற்றம் நினைவும் துணிவும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ēṟṟam (ஏற்றம்) means remembrance and determination."
              }
            },
            {
              "paadal": "பிணையும் பேணும் பெட்பின் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "piṇai (பிணை) and pēṇ (பேண்) means love, desire or regard."
              }
            },
            {
              "paadal": "பணையே பிழைத்தல் பெருப்பும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "paṇai (பணை) means escaping or becoming stout."
              }
            },
            {
              "paadal": "படரே உள்ளல் செலவும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "paṭar (படர்) means thinking and going."
              }
            },
            {
              "paadal": "பையுளும் சிறுமையும் நோயின் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "paiyuḷ (பையுள்) and cirumai (சிருமை) mean sickness."
              }
            },
            {
              "paadal": "எய்யாமையே அறியாமையே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "eyyāmai (எய்யாமை) means avidyā (अविद्या) or incorrect knowledge."
              }
            },
            {
              "paadal": "நன்று பெரிது ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "naṉṟu (நன்று) means greatness."
              }
            },
            {
              "paadal": "தாவே வலியும் வருத்தமும் ஆகும்",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "tāvu (தாவு) means strength and pain or distress."
              }
            },
            {
              "paadal": "தெவுக் கொளல் பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Tevu (தெவு) means taking."
              }
            },
            {
              "paadal": "தெவ்வுப் பகை ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Tevvu (தெவ்வு) denotes enmity."
              }
            },
            {
              "paadal": "விறப்பும் உறப்பும் வெறுப்பும் செறிவே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "viṟappu (விறப்பு), uṟappu (உறப்பு) and veṟuppu (வெறுப்பு) mean denseness."
              }
            },
            {
              "paadal": "அவற்றுள், \nவிறப்பே வெரூஉப் பொருட்டும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Of them viṟappu (விறப்பு) also means the state of being terrified."
              }
            },
            {
              "paadal": "கம்பலை சும்மை கலியே அழுங்கல் \nஎன்றிவை நான்கும் அரவப் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Kampalai (கம்பலை), cummai (சும்மை), kali (கலி) and aḻuṅkal (அழுங்கல்) - all these four mean noise."
              }
            },
            {
              "paadal": "அவற்றுள், \nஅழுங்கல் இரக்கமும் கேடும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Of them aḻuṅkal (அழுங்கல்) also means piteousness and disaster."
              }
            },
            {
              "paadal": "கழும் என்கிளவி மயக்கம் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word kaḻum (கழும்) means bewilderment."
              }
            },
            {
              "paadal": "செழுமை வளனும் கொழுப்பும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ceḻumai (செழுமை) means fertility and stoutness."
              }
            },
            {
              "paadal": "விழுமம் சீர்மையும் சிறப்பும் இடும்பையும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "viḻumai (விழுமை) means regularity, magnificence and trouble."
              }
            },
            {
              "paadal": "கருவி தொகுதி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "karuvi (கருவி) means collection."
              }
            },
            {
              "paadal": "கமம் நிறைந்து இயலும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kama (கம) means fulness. "
              }
            },
            {
              "paadal": "அரியே ஐம்மை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ari (அரி) means slendernes or nicety."
              }
            },
            {
              "paadal": "கவவு அகத்திடுமே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kavavu (கவவு) means wearing or embracing."
              }
            },
            {
              "paadal": "துவைத்தலும் சிலைத்தலும் இயம்பலும் இரங்கலும் \nஇசைப்பொருட் கிளவி என்மனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Learned men say that tuvaittal (துவைத்தல்), cilaittal (சிலைத்தல்), iyampal (இயம்பல்) and iraṅkal (இரங்கல்) are words denoting sound."
              }
            },
            {
              "paadal": "அவற்றுள், \nஇரங்கல் கழிந்த பொருட்டும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Of them iraṅkal (இரங்கல்) also means repentence."
              }
            },
            {
              "paadal": "இலம்பாடு ஒற்கம் ஆயிரண்டும் வறுமை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Ilampāṭu (இலம்பாடு) and oṟkam (ஒற்கம்) both mean poverty."
              }
            },
            {
              "paadal": "ஞெமிர்தலும் பாய்தலும் பரத்தல் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ñemirtal (ஞெமிர்தல்) and pāytal (பாய்தல்) means spreading."
              }
            },
            {
              "paadal": "கவர்வு விருப்பு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kavarvu (கவர்வு) means desire."
              }
            },
            {
              "paadal": "சேரே திரட்சி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "cēr (சேர்) means collection."
              }
            },
            {
              "paadal": "வியல்என் கிளவி அகலப் பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": ""
              }
            },
            {
              "paadal": "பேம் நாம் உரும் என வரூஉம் கிளவி \nஆமுறை மூன்றும் அச்சப் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word viyal (வியல்) means breadth or extensiveness."
              }
            },
            {
              "paadal": "வய வலி ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The three words pē (பே), nām (நாம்), urum (உரும்) mean dread"
              }
            },
            {
              "paadal": "வாள் ஒளி ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vaya (வய) means strength"
              }
            },
            {
              "paadal": "துயவு என்கிளவி அறிவின் திரிபே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vāḷ (வாள்) means brilliance or lustre."
              }
            },
            {
              "paadal": "உயாவே உயங்கல்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vāḷ (வாள்) means brilliance or lustre."
              }
            },
            {
              "paadal": "உசாவே சூழ்ச்சி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "uyā (உயா) means suffering or disease."
              }
            },
            {
              "paadal": "வயா என்கிளவி வேட்கைப் பெருக்கம்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ucā (உசா) means wisdom or deliberation."
              }
            },
            {
              "paadal": "கறுப்பும் சிவப்பும் வெகுளிப் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word vayā (வயா) means great desire."
              }
            },
            {
              "paadal": "நிறத்துரு உணர்த்தற்கும் உரிய என்ப.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "karuppu (கருப்பு) and civappu (சிவப்பு) mean anger."
              }
            },
            {
              "paadal": "நொசிவும் நுழைவும் நுணங்கும் நுண்மை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "They say that they can denote colour also."
              }
            },
            {
              "paadal": "புனிறு என்கிளவி ஈன்று அணிமைப் பொருட்டே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Nocivu (நொசிவு), nuḻaivu (நுழைவு) and nuṇaṅku (நுணங்கு) mean minuteness."
              }
            },
            {
              "paadal": "நனவே களனும் அகலமும் செய்யும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word puṉiṟu (புனிறு) dentotes recent calving."
              }
            },
            {
              "paadal": "மதவே மடனும் வலியும் ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "naṉa (நன) means battlefield and extensiveness."
              }
            },
            {
              "paadal": "மிகுதியும் வனப்பும் ஆகலும் உரித்தே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "mata (மத) means artlessness and strength."
              }
            },
            {
              "paadal": "புதிது படற்பொருட்டே யாணர்க் கிளவி.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "mata (மத) also means larger quantity and beauty."
              }
            },
            {
              "paadal": "அமர்தல் மேவல்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word yāṇar (யாணர்) means newness."
              }
            },
            {
              "paadal": "யாணுக் கவினாம்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "amarthal (அமர்த்அல்) means desire."
              }
            },
            {
              "paadal": "பரவும் பழிச்சும் வழுத்தின் பொருள.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "yāṇu (யாணு) means beauty."
              }
            },
            {
              "paadal": "கடி என் கிளவி \nவரைவே கூர்மை காப்பே புதுமை \nவிரைவே விளக்கம் மிகுதி சிறப்பே \nஅச்சம் முன்தேற்று ஆயீர் ஐந்தும் \nமெய்ப்படத் தோன்றும் பொருட்டு ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "paravu (பரவு) and paḻiccu (பழிச்சு) mean extolling."
              }
            },
            {
              "paadal": "ஐயமும் கரிப்பும் ஆகலும் உரித்தே.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The word kaṭi (கடி) has the following ten meanings: forbidding, sharpness, protection, newness, quickness, brilliance, largeness in quantity, superiority, fear and direct promise."
              }
            },
            {
              "paadal": "ஐ வியப்பு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "kaṭi (கடி) may also mean doubt and pungency."
              }
            },
            {
              "paadal": "முனைவு முனிவு ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "ai (ஐ) means wonder or astonishment."
              }
            },
            {
              "paadal": "வையே கூர்மை.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "muṉaivu (முனைவு) means disgust."
              }
            },
            {
              "paadal": "எறுழ் வலி ஆகும்.",
              "vilakkam": {
                "paadal_category": "Semantic Complextions of uriccol (உரிச்சொல்)",
                "paadal_meaning": "vai (வை) means sharpness."
              }
            },
            {
              "paadal": "மெய்பெறக் கிளந்த உரிச்சொல் எல்லாம் \nமுன்னும் பின்னும் வருபவை நாடி \nஒத்த மொழியான் புணர்த்தனர் உணர்த்தல் \nதத்தம் மரபின் தோன்றுமன் பொருளே.",
              "vilakkam": {
                "paadal_category": "uriccol (உரிச்சொல்) as a Context-specific",
                "paadal_meaning": "eruḻ (எருழ்) means strength."
              }
            },
            {
              "paadal": "கூறிய கிளவிப் பொருள்நிலை அல்ல \nவேறுபிற தோன்றினும் அவற்றொடு கொளலே.",
              "vilakkam": {
                "paadal_category": "Extended significance of uriccol (உரிச்சொல்)",
                "paadal_meaning": "The meanings of all uriccols (உரிச்சொல்s) which have been mentioned can be determined through the context."
              }
            },
            {
              "paadal": "பொருட்குப் பொருள் தெரியின் அதுவரம்பின்றே",
              "vilakkam": {
                "paadal_category": "Extended significance of uriccol (உரிச்சொல்)",
                "paadal_meaning": "One should take in meanings other than those mentioned above if such are determined from context."
              }
            },
            {
              "paadal": "பொருட்குத் திரிபு இல்லை உணர்த்த வல்லின்.",
              "vilakkam": {
                "paadal_category": "Extended significance of uriccol (உரிச்சொல்)",
                "paadal_meaning": "There will be no limit if one attempts to give the meaning of the meanings given to the uriccol (உரிச்சொல்) mentioned above."
              }
            },
            {
              "paadal": "உணர்ச்சி வாயில் உணர்வோர் வலித்தே.",
              "vilakkam": {
                "paadal_category": "Extended significance of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Meanings does not change oven if it can be expressed in other ways."
              }
            },
            {
              "paadal": "மொழிப்பொருள் காரணம் விழிப்பத் தோன்றா.",
              "vilakkam": {
                "paadal_category": "Extended significance of uriccol (உரிச்சொல்)",
                "paadal_meaning": "Methods of expressing meanings depend upon the capacity of those who know them."
              }
            },
            {
              "paadal": "எழுத்துப் பிரிந்து இசைத்தல் இவண் இயல்பின்றே",
              "vilakkam": {
                "paadal_category": "uriccol (உரிச்சொல்) as Unsplittable Forms",
                "paadal_meaning": "It is not possible to understand clearly the reason why a particular uriccol (உரிச்சொல்) has a particular meaning."
              }
            },
            {
              "paadal": "அன்ன பிறவும் கிளந்த அல்ல \nபல்முறை யானும் பரந்தன வரூஉம் \nஉரிச்சொல் எல்லாம் பொருட்குறை கூட்ட \nஇயன்ற மருங்கின் இனைத்தென அறியும் \nவரம்பு தமக்கு இன்மையின் வழிநனி கடைப்பிடித்து \nஓம்படை ஆணையின் கிளந்தவற்று இயலான் \nபாங்குற உணர்தல் என்மனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "uriccol (உரிச்சொல்) as Open-ended terms",
                "paadal_meaning": "Learned men say that, since it is not possible to exhaust the meanings of uriccol (உரிச்சொல்) other than mentioned above, one should understand them in the way in which it was done by the ancients with the view that they should be will understood and preserved."
              }
            }
          ]
      },
      {
          "iyal_name": "எச்சவியல்",
          "iyal_eng":"Residual Compounds",
          "noorpa": [
            {
              "paadal": "இயற்சொல் திரிசொல் திசைச்சொல் வடசொல் என்று \nஅனைத்தே செய்யுள் ஈட்டச் சொல்லே.",
              "vilakkam": {
                "paadal_category": "The Four Classes of Words",
                "paadal_meaning": "Words used in verses are of four kinds : iyaṟcol (இயற்சொல்), tiricol (திரிசொல்), ticaicol (திசைசொல்) and vaṭacol (வடசொல்)Words used in verses are of four kinds : iyaṟcol (இயற்சொல்), tiricol (திரிசொல்), ticaicol (திசைசொல்) and vaṭacol (வடசொல்)"
              }
            },
            {
              "paadal": "அவற்றுள், \nஇயற்சொல் தாமே \nசெந்தமிழ் நிலத்து வழக்கொடு சிவணி \nதம்பொருள் வழாமை இசைக்கும் சொல்லே.",
              "vilakkam": {
                "paadal_category": "Standard Idiom",
                "paadal_meaning": "Of them, iyaṟcol (இயற்சொல்) is that which is used in Centamiḻ-nilam (செந்தமிழ்நிலம்) and elsewhere without change in meaning; in other words iyaṟcol (இயற்சொல்)  is indigenous Tamil word."
              }
            },
            {
              "paadal": "ஒருபொருள் குறித்த வேறுசொல் ஆகியும் \nவேறுபொருள் குறித்த ஒருசொல் ஆகியும் \nஇருபாற்று என்ப திரிசொல் கிளவி.",
              "vilakkam": {
                "paadal_category": "Tirichol (திரிசொல்)",
                "paadal_meaning": "Tirichol (திரிசொல்) is of two kinds : one having synonyms and other having different meanings."
              }
            },
            {
              "paadal": "செந்தமிழ் சேர்ந்த பன்னிரு நிலத்தும் \nதம்குறிப் பினவே திசைச்சொல் கிளவி.",
              "vilakkam": {
                "paadal_category": "Dialectal Words",
                "paadal_meaning": "ticaicol (திசைசொல்) is the word borrowed in Tamil from the languages current in the twelve countries bordering the Tamil land."
              }
            },
            {
              "paadal": "வடசொல் கிளவி வடஎழுத்து ஒரீஇ \nஎழுத்தொடு புணர்ந்த சொல் ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "(Sanskrit) Loan Words",
                "paadal_meaning": "vaṭacol (வடசொல்) is the word which is made up of sounds other than those which are peculiar to Sanskrit."
              }
            },
            {
              "paadal": "சிதைந்தன வரினும் இயைந்தன வரையார்.",
              "vilakkam": {
                "paadal_category": "(Sanskrit) Loan Words",
                "paadal_meaning": "They do not ward off words made up of sounds which are different from those found in Sanskrit."
              }
            },
            {
              "paadal": "அந்நாற் சொல்லும் தொடுக்கும் காலை \nவலிக்கும்வழி வலித்தலும் மெலிக்கும்வழி மெலித்தலும் \nவிரிக்கும்வழி விரித்தலும் தொகுக்கும்வழித் தொகுத்தலும் \nநீட்டும்வழி நீட்டலும் குறுக்கும்வழிக் குறுக்கலும் \nநாட்டல் வலிய என்மனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "The Four Classes of Words and Their Usage (Admissible Deviations)",
                "paadal_meaning": "Learned men say that, when those four kinds of words are used in verse, a voice sound may be made a voiceless one and vice-versa, a sound or sounds may be added or elided, a vowel or vowels may be lengthened or shortened as used be."
              }
            },
            {
              "paadal": "நிரல்நிறை சுண்ணம் அடிமறி மொழிமாற்று \nஅவை நான்கு என்ப மொழிபுணர் இயல்பே.",
              "vilakkam": {
                "paadal_category": "Mode of Construing Verse Meaning",
                "paadal_meaning": "Syntax in verse is of four kinds : niraṉiṟai (நிரனிறை), cuṇṇam (சுண்ணம்), aṭimaṟi (அடிமறி) and moḻimāṟṟu (மொழிமாற்று)"
              }
            },
            {
              "paadal": "அவற்றுள், \n நிரல்நிறை தானே \nவினையினும் பெயரினும் நினையத் தோன்றி \nசொல்வேறு நிலைஇ பொருள்வேறு நிலையல்.",
              "vilakkam": {
                "paadal_category": "Niraṉiṟai (நிரனிறை)",
                "paadal_meaning": "Of them niraṉiṟai (நிரனிறை) is that mode wherein verbs, nouns or both and clauses found in one group in one order are grammatically connected with the same found in another group in the same order."
              }
            },
            {
              "paadal": "சுண்ணம்தானே \nபட்டாங்கு அமைந்த ஈர்அடி எண்சீர் \nஒட்டுவழி அறிந்து துணித்தனர் இயற்றல்.",
              "vilakkam": {
                "paadal_category": "Cuṇṇam (சுண்ணம்)",
                "paadal_meaning": "Of them, cuṇṇam (சுண்ணம்) is that mode wherein words in two feet of a stanza with four cīr (சீர்) each are so promisuously arranged that it is necessary to find the proper order in which they are grammatically connected."
              }
            },
            {
              "paadal": "அடிமறிச் செய்தி அடிநிலை திரிந்து \nசீர்நிலை திரியாது தடுமா றும்மே.",
              "vilakkam": {
                "paadal_category": "aṭimaṟi (அடிமறி)",
                "paadal_meaning": "Of them, aṭimaṟi (அடிமறி) is the mode wherein the meaning is not changed though the order of the lines is changed without changing the order of the cīr (சீர்) in each line."
              }
            },
            {
              "paadal": "பொருள்தெரி மருங்கின் \nஈற்றடி இறுசீர் எருத்துவயின் திரியும் \nதோற்றமும் வரையார் அடிமறி யான.",
              "vilakkam": {
                "paadal_category": "aṭimaṟi (அடிமறி)",
                "paadal_meaning": "In aṭimaṟi (அடிமறி) the final cīr (சீர்) of the last line may be grammatically connected with a cīr (சீர்) in the penultimate line when the meaning of a stanza is constructed."
              }
            },
            {
              "paadal": "மொழிமாற்று இயற்கை \nசொல்நிலை மாற்றி பொருள்எதிர் இயைய \nமுன்னும் பின்னும் கொள்வழிக் கொளாஅல்.",
              "vilakkam": {
                "paadal_category": "moḻimāṟṟu (மொழிமாற்று)",
                "paadal_meaning": "Of them, moḻimāṟṟu (மொழிமாற்று) is that mode wherein words which are grammatically connected are so promiscuosly set in that when one makes its meaning, he will have to rearrange it."
              }
            },
            {
              "paadal": "த ந நு எ எனும் அவை முதலாகிய \nகிளைநுதல் பெயரும் பிரிப்பப் பிரியா.",
              "vilakkam": {
                "paadal_category": "Compounding of Words",
                "paadal_meaning": "Words of relationship beginning with ta (த), na (ந), nu (நு),e (எ) cannot be split into component parts."
              }
            },
            {
              "paadal": "இசைநிறை அசைநிலை பொருளொடு புணர்தல் என்று \nஅவைமூன்று என்ப ஒருசொல் அடுக்கே.",
              "vilakkam": {
                "paadal_category": "Reduplication",
                "paadal_meaning": "They say that the reduplication of words is of three kinds : icai-niṟai (இசைநிறை) or that used for euphony, acai-nilai (அசைநிலை) or that used to make up the sylabbles and poruḷoṭu puṇartal (பொருளொடு புணர்தல்) or that used with some meaning."
              }
            },
            {
              "paadal": "வேற்றுமைத் தொகையே உவமத் தொகையே \nவினையின் தொகையே பண்பின் தொகையே \nஉம்மைத் தொகையே அன்மொழித் தொகைஎன்று \nஅவ்ஆறு என்ப தொகைமொழி நிலையே.",
              "vilakkam": {
                "paadal_category": "Classes of Compound Words",
                "paadal_meaning": "They say that compounds are of six kinds : vēṟṟumai-tokai (வேற்றுமைத் தொகை), uvama-tokai ( உவமத் தொகை), viṉaiyiṉ-tokai (வினையின் தொகை), paṇpiṉ-tokai ( பண்பின் தொகை), ummai-tokai (உம்மைத் தொகை) and aṉ-moḻi-tokai (அன்மொழித் தொகை)"
              }
            },
            {
              "paadal": "அவற்றுள், \nவேற்றுமைத் தொகையே வேற்றுமை இயல.",
              "vilakkam": {
                "paadal_category": "Case-Relations Compound",
                "paadal_meaning": "Of them, vēṟṟumai-tokai (வேற்றுமைத் தொகை) is that wherein the former member is in case-relation to the following member."
              }
            },
            {
              "paadal": "உவமத் தொகையே உவம இயல.",
              "vilakkam": {
                "paadal_category": "Compounds of Comparison",
                "paadal_meaning": "uvama-tokai ( உவமத் தொகை) is that wherein the former member is upamaanam and the following member is upameyam."
              }
            },
            {
              "paadal": "வினையின் தொகுதி காலத்து இயலும்.",
              "vilakkam": {
                "paadal_category": "Compounds of Verbs",
                "paadal_meaning": "viṉaiyiṉ-tokai (வினையின் தொகை) is that wherein the former member is a participle denoting time."
              }
            },
            {
              "paadal": "வண்ணத்தின் வடிவின் அளவின் சுவையின் என்று \nஅன்ன பிறவும் அதன்குணம் நுதலி \nஇன்னது இதுஎன வரூஉம் இயற்கை \nஎன்ன கிளவியும் பண்பின் தொகையே.",
              "vilakkam": {
                "paadal_category": "Adjectival Compounds",
                "paadal_meaning": "Paṇpu-tokai ( பண்பு தொகை) is that wherein the former member denotes the quality like color, shape, extent, taste, etc, thus saying something about an object and the following member is the word denoting the object."
              }
            },
            {
              "paadal": "இருபெயர் பலபெயர் அளவின் பெயரே \nஎண்ணியற் பெயரே நிறைப்பெயர்க் கிளவி \nஎண்ணின் பெயரொடு அவ்அறு கிளவியும் \nகண்ணிய நிலைத்தே உம்மைத் தொகையே.",
              "vilakkam": {
                "paadal_category": "Conjunctive relations Compounds",
                "paadal_meaning": "Ummai-tokai (உம்மைத் தொகை) is that, where two words denoting a single object, two words denoting many objects, words denoting measurement, words denoting objects that are counted, words denoting weight and words denoting number - all these six - are combine together."
              }
            },
            {
              "paadal": "பண்புதொக வரூஉம் கிளவி யானும் \nஉம்மை தொக்க பெயர்வயி னானும் /nவேற்றுமை தொக்க பெயர்வயி னானும் \nஈற்று நின்று இயலும் அன்மொழித் தொகையே.",
              "vilakkam": {
                "paadal_category": "Compounds of Elliptical Head",
                "paadal_meaning": "Aṉmoḻi-tokai (அன்மொழித் தொகை) is that wherein the element denoting quality, the particle um or the case-suffix, in the former member is dropped and the element denoting the person at the end is also dropped."
              }
            },
            {
              "paadal": "அவைதாம், \nமுன்மொழி நிலையலும் பின்மொழி நிலையலும் \nஇருமொழி மேலும் ஒருங்குடன் நிலையலும் \nஅம்மொழி நிலையாது அல்மொழி நிலையலும் \nஅந்நான்கு என்ப பொருள்நிலை மரபே.",
              "vilakkam": {
                "paadal_category": "Compounds of Elliptical Head",
                "paadal_meaning": "They say that, in the above compounds, the most important part of the meaning rests in four different ways - on the following member, on the former member, on both the members and on neither the former nor the following member but on something else."
              }
            },
            {
              "paadal": "எல்லாத் தொகையும் ஒருசொல் நடைய.",
              "vilakkam": {
                "paadal_category": "Compounds as Single Words",
                "paadal_meaning": "All the compounds are of the same nature as simple words, (i.e.), are unitary in nature."
              }
            },
            {
              "paadal": "உயர்திணை மருங்கின் உம்மைத் தொகையே \nபலர்சொல் நடைத்தென மொழிமனார் புலவர்.",
              "vilakkam": {
                "paadal_category": "Compounds as Single Words",
                "paadal_meaning": "Learned men say that ummai-tokai (உம்மைத் தொகை) of uyartiṇai (உயர்திணை) nouns are of the nature of plural nouns."
              }
            },
            {
              "paadal": "வாரா மரபின வரக் கூறுதலும் \nஎன்னா மரபின எனக் கூறுதலும் \nஅன்னவை எல்லாம் அவற்றவற்று இயல்பான் \nஇன்ன என்னும் குறிப்புரை ஆகும்.",
              "vilakkam": {
                "paadal_category": "'Pathetic Fallacy'",
                "paadal_meaning": "Expressions where objects which do not have the capacity to come are described as coming and objects which do not have the capacity to think or speak are described as thinking and speaking and such others are said to be kuṟippu-c-col (குறிப்புச்சொல்) or suggestive words."
              }
            },
            {
              "paadal": "இசைப்படு பொருளே நான்கு வரம்பாகும்",
              "vilakkam": {
                "paadal_category": "Reduplication of Euphonic Terms",
                "paadal_meaning": "The maximum limit for the repetition of a word for euphonic harmony is four."
              }
            },
            {
              "paadal": "விரைசொல் அடுக்கே மூன்று வரம்பாகும்.",
              "vilakkam": {
                "paadal_category": "Reduplication of 'Swift' Words",
                "paadal_meaning": "The maximum limit for the repetition of a word to denote haste is three."
              }
            },
            {
              "paadal": "கண்டீர் என்றா கொண்டீர் என்றா \nசென்றது என்றா போயிற்று என்றா \nஅன்றி அனைத்தும் வினாவொடு சிவணி \nநின்றவழி அசைக்கும் கிளவி என்ப.",
              "vilakkam": {
                "paadal_category": "Empty Morphemes in Reduplication",
                "paadal_meaning": "The words kaṇṭīr (கண்டீர்), koṇṭīr (கொண்டீர்), ceṉṟatu (சென்றது), pōyiṟṟu (போயிற்று) when followed by the interrogative letters are said to be acai-c-col (அசைச்சொல்)."
              }
            },
            {
              "paadal": "கேட்டை என்றா நின்றை என்றா \nகாத்தை என்றா கண்டை என்றா \nஅன்றி அனைத்தும் முன்னிலை அல்வழி \nமுன்னுறக் கிளந்த இயல்பு ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "Empty Morphemes in Reduplication",
                "paadal_meaning": "The words kēṭṭai (கேட்டை), niṉṟai (நின்றை), kāttai (காத்தை) and kaṇṭai (கண்டை) when they do not denote the second person singular are acai-c-col (அசைச்சொல்)."
              }
            },
            {
              "paadal": "இறப்பின் நிகழ்வின் எதிர்வின் என்ற \nசிறப்புடை மரபின் அம்முக் காலமும் \nதன்மை முன்னிலை படர்க்கை என்னும் \nஅம்மூ இடத்தான் வினையினும் குறிப்பினும் \nமெய்ம்மை யானும் இவ்விரண்டு ஆகும் \nஅவ்ஆறு என்ப முற்றியல் மொழியே.",
              "vilakkam": {
                "paadal_category": "The Finite Verb",
                "paadal_meaning": "They say that the finite verbs are of 24 kinds : verbs that explicitly denote one of the three tenses (present, past and future) and used in the first, the second and the third person in wither of the numbers singular and plural and appellative verbs that are used in the first, the second and the third person in either of the numbers."
              }
            },
            {
              "paadal": "எவ்வயின் வினையும் அவ்வியல் நிலையும்.",
              "vilakkam": {
                "paadal_category": "The Finite Verb",
                "paadal_meaning": "Verbs which are used in all persons without change of form are also of the same nature."
              }
            },
            {
              "paadal": "அவைதாம், \nதத்தம் கிளவி அடுக்குந வரினும் \nஎத்திறத் தானும் பெயர் முடிபினவே.",
              "vilakkam": {
                "paadal_category": "The Finite Verb",
                "paadal_meaning": "They, even though are used in succession, qualify only the noun (which is their subject)"
              }
            },
            {
              "paadal": "பிரிநிலை வினையே பெயரே ஒழியிசை \nஎதிர்மறை உம்மை எனவே சொல்லே \nகுறிப்பே இசையே ஆயீர் ஐந்தும் \nநெறிப்படத் தோன்றும் எஞ்சுபொருட் கிளவி.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Eñcu-poruṭ-kiḷavi (எஞ்சுபொருட்கிளவி), or word/words which suggest something else are of tem kinds : pirinilai (பிரிநிலை), viṉai (வினை), peyar (பெயர்), oḻiyicai (ஒழியிசை), etirmaṟai (எதிர்மறை), ummai (உம்மை), eṉa (என), col (சொல்), kuṟippu (குறிப்பு), icai (இசை)."
              }
            },
            {
              "paadal": "அவற்றுள், \nபிரிநிலை எச்சம் பிரிநிலை முடிபின.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "pirinilai-y-eccam (பிரிநிலையெச்சம்) completes its idea with delimiting expression."
              }
            },
            {
              "paadal": "வினையெஞ்சு கிளவிக்கு வினையும் குறிப்பும் \nநினையத் தோன்றிய முடிபு ஆகும்மே \nஆவயின் குறிப்பே ஆக்கமொடு வருமே.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "viṉai-eccam (வினைஎச்சம்) completes its idea with a teri-nilai-viṉai (தெரிநிலைவினை) or kurippu-viṉai (குரிப்புவினை). If it is the latter, it is the verb derived from the root ā (ஆ) to āku (ஆகு)."
              }
            },
            {
              "paadal": "பெயரெஞ்சு கிளவி பெயரொடு முடிமே.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Peyar-eñcu-kiḷavi (பெயர்எஞ்சுகிளவி) completes its idea with a noun."
              }
            },
            {
              "paadal": "ஒழியிசை எச்சம் ஒழியிசை முடிபின.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Oḻi-y-icai-y-eccam (ஒழியிசையெச்சம்) completes its idea with what has been left out."
              }
            },
            {
              "paadal": "எதிர்மறை எச்சம் எதிர்மறை முடிபின",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Etir-maṟai-y-eccam (எதிர்மறையெச்சம்) completes its idea with an expression that is antithetic to it."
              }
            },
            {
              "paadal": "உம்மை எச்சம் இருஈற் றானும் \nதன்வினை ஒன்றிய முடிபு ஆகும்மே.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Ummai-eccham (உம்மையெச்சம்) completes its idea, in both the cases, with the verb similar to the verb mentioned."
              }
            },
            {
              "paadal": "தன்மேல் செஞ்சொல் வரூஉம் காலை \nநிகழும் காலமொடு வாராக் காலமும் \nஇறந்த காலமொடு வாராக் காலமும் \nமயங்குதல் வரையார் முறைநிலை யான.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "If a word not being followed by um (உம்) is used in a suggestive sentence with a verb to be in the future in the sentence suggested."
              }
            },
            {
              "paadal": "எனவென் எச்சம் வினையொடு முடிமே",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "The sentence where the particle eṉa (என) is dropped completes its idea even with a verb."
              }
            },
            {
              "paadal": "எஞ்சிய மூன்றும் மேல்வந்து முடிக்கும் \nஎஞ்சு பொருட்கிளவி இலவென மொழிப.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "They say that the remaining three do not suggest anything to complete their idea, that is, There is nothing in themselves to suggest anything. It is the context that makes the sentence suggest other meanings."
              }
            },
            {
              "paadal": "அவைதாம், \nதத்தம் குறிப்பின் எச்சம் செப்பும்",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "They will suggest through the speaker's method of expression."
              }
            },
            {
              "paadal": "சொல்என் எச்சம் முன்னும் பின்னும் \nசொல்அளவு அல்லது எஞ்சுதல் இன்றே.",
              "vilakkam": {
                "paadal_category": "Forms of Incomplete Signification",
                "paadal_meaning": "Col-l-eccham (சொல்ல்எச்ச்அம்) is that word which does not depent upon any word to be filled up to complete the idea wither before it or after it."
              }
            },
              {
                "paadal": "அவையல் கிளவி மறைத்தனர் கிளத்தல்.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "One should not use obscene words and hence should use such words which can suggest them."
                }
              },
              {
                "paadal": "மறைக்கும் காலை மரீஇயது ஒராஅல்.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "One does not avoid while using alternative expressions such expressions that have come to use."
                }
              },
              {
                "paadal": "ஈ தா கொடு எனக் கிளக்கும் மூன்றும் \nஇரவின் கிளவி ஆகிடன் உடைய.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "The three verbs, ī (ஈ), tā (தா) and koḷu (கொளு) are used when one begs of another."
                }
              },
              {
                "paadal": "அவற்றுள்,\nஈ என் கிளவி இழிந்தோன் கூற்றே.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "Of them the root ī (ஈ) is used when the recipient is inferior in status to the giver."
                }
              },
              {
                "paadal": "தா என்கிளவி ஒப்போன் கூற்றே.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "Of them the root tā (தா) is used when both the recipient and the giver are of the same status."
                }
              },
              {
                "paadal": "கொடு என்கிளவி உயர்ந்தோன் கூற்றே.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "Of them the root koḷu (கொளு) is used when the recipient is of superior status."
                }
              },
              {
                "paadal": "கொடு என்கிளவி படர்க்கை ஆயினும்\nதன்னைப் பிறன்போல் கூறும் குறிப்பின்\nதன்னிடத்து இயலும் என்மனார் புலவர்.",
                "vilakkam": {
                  "paadal_category": "Conventions of Use of Certain Classes of Words",
                  "paadal_meaning": "Learned men say that, though the root koḷu (கொளு) is used when the recipient is the third person, it may be used even when the recipient is the speaker if he speaks of himself in the third person."
                }
              },
              {
                "paadal": "பெயர்நிலைக் கிளவியின் ஆஅகுநவும்\nதிசைநிலை கிளவியின் ஆஅகுநவும்\nதொல்நெறி மொழிவயின் ஆஅகுநவும்\nமெய்ந்நிலை மயக்கின் ஆஅகுநவும்\nமந்திரப் பொருள்வயின் ஆஅகுநவும்\nஅன்றி அனைத்தும் கடப்பாடு இலவே.",
                "vilakkam": {
                  "paadal_category": "Classes of Words Outside the Conventions",
                  "paadal_meaning": "There is no rule governing the use of the following : a noun of one tiṉai (தினை) denoting another : an indigenous word used in other countries in different meanings : certain expression having a long usage from early times : riddles, etc : mantrās and similar things, that is, They do not convet the literal meaning. Hence they must be taken as icai-y-eccam (இசையெச்சம்) since they suggest a meaning connected with their literal meaning."
                }
              },
              {
                "paadal": "செய்யாய் என்னும் முன்னிலை வினைச்சொல்\nசெய்என் கிளவி ஆகிடன் உடைத்தே.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "The second person singular verb of the paradigm ceyyāy (செய்யாய்) is used as cey (செய்) also."
                }
              },
              {
                "paadal": "முன்னிலை முன்னர் ஈயும் ஏயும்\nஅந்நிலை மரபின் மெய்ஊர்ந்து வருமே.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "ī (ஈ) and ē (ஏ) may be suffixed to second person singular preceeded by a suitable consonant."
                }
              },
              {
                "paadal": "கடிசொல் இல்லை காலத்துப் படினே.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "One cannot avoid words which become current."
                }
              },
              {
                "paadal": "குறைச்சொற் கிளவி குறைக்கும் வழிஅறிதல்.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "One should understand how certain sounds are elided in words."
                }
              },
              {
                "paadal": "குறைத்தன ஆயினும் நிறைப்பெயர் இயல.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "Though they have certain sounds elided, they convey the meaning of full words."
                }
              },
              {
                "paadal": "இடைச்சொல் எல்லாம் வேற்றுமைச் சொல்லே.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "All iṭai-c-col (இடைச்சொல்) are different words."
                }
              },
              {
                "paadal": "உரிச்சொல் மருங்கினும் உரியவை உரிய.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "Even among uriccol (உரிச்சொல்), there may be some which serve as differentiating words."
                }
              },
              {
                "paadal": "வினையெஞ் சுகிளவியும் வேறுபல் குறிய.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "Viṉai-yeñcu-kiḷavi (வினையெஞுகிளவி) too are of different nature not mentioned before."
                }
              },
              {
                "paadal": "உரையிடத்து இயலும் உடனிலை அறிதல்",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "One should understand the nature of viṉai-yeñu-kiḷavi (வினையெஞுகிளவி) from the context."
                }
              },
              {
                "paadal": "முன்னத்தின் உணரும் கிளவியும் உளவே\nஇன்ன என்னும் சொல்முறை யான.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "In the order of words which describe a thing, there are certain words which suggest some meaning."
                }
              },
              {
                "paadal": "ஒருபொருள் இருசொல் பிரிவில வரையார்.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "They do not object to the use of redundant expressions made of synonymous words."
                }
              },
              {
                "paadal": "ஒருமை சுட்டிய பெயர் நிலைக் கிளவி\nபன்மைக்கு ஆகும் இடனுமார் உண்டே.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "A noun in the singular number may denote more than one object."
                }
              },
              {
                "paadal": "முன்னிலை சுட்டிய ஒருமைக் கிளவி\nபன்மையொடு முடியினும் வரைநிலை இன்றே\nஆற்றுப்படை மருங்கின் போற்றல் வேண்டும்.",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "In āṟṟuppaṭai (ஆற்றுப்படை), a singular noun may take a verb in the plural. It should be passed over."
                }
              },
              {
                "paadal": "செய்யுள் மருங்கினும் வழக்கியல் மருங்கினும்\nமெய்பெறக் கிளந்த கிளவி எல்லாம்\nபல்வேறு செய்தியின் நூல்நெறி பிழையாது\nசொல்வரைந்து அறியப் பிரித்தனர் காட்டல்",
                "vilakkam": {
                  "paadal_category": "Residual Norms of Usage",
                  "paadal_meaning": "One should clearly show the peculiar use of all words in different meanings at different places from the literature and ordinart usage."
                }
              }
            ]
      }
      ]
  },
  {
    "adhikaaram": "பொருளதிகாரம்",
    "adhikaaram_eng":"Semantics and Poetics",
    "iyal": [
      {
        "iyal_name": "அகத்திணையியல்",
        "iyal_eng":"Akam (அகம்) Love",
        "noorpa": [
          {
            "paadal": "கைக்கிளை முதலாப் பெருந்திணை இறுவாய் \nமுற்படக் கிளந்த எழு திணை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "The Modes of Akam (அகம்) Love Behaviour",
              "paadal_meaning": "They say that the groups commencing with kaikkiḷai (கைக்கிளை) and ending with peruntiṇai (பெருந்திணை) mentioned before are the seven tiṇais (திணை)"
            }
          },
          {
            "paadal": "அவற்றுள், \nநடுவண் ஐந்திணை நடுவணது ஒழிய \nபடு திரை வையம் பாத்திய பண்பே.",
            "vilakkam": 
            {
              "paadal_category": "Geographical Identities to the Modes of Akam (அகம்) Love",
              "paadal_meaning": "Of them the middle five except the middle one are of the nature of owning land surrounded by seas apportioned to them."
            }
          },
          {
            "paadal": "முதல் கரு உரிப்பொருள் என்ற மூன்றே \nநுவலும் காலை முறை சிறந்தனவே \nபாடலுள் பயின்றவை நாடும் காலை.",
            "vilakkam": 
            {
              "paadal_category": "The Structural Constituents of Akam (அகம்) Poetry",
              "paadal_meaning": "On examining the padārthas (பதார்த்தஸ்) (the meaning or referent of words) used in poetry, those of them which are important in their order are mutaṟ-poruḷ (முதற்-பொருள்), karu-p-poruḷ (கரு-ப்-பொருள்) and uri-p-poruḷ (உரி-ப்-பொருள்)."
            }
          },
          {
            "paadal": "முதல் எனப்படுவது நிலம் பொழுது இரண்டின் \nஇயல்பு என மொழிப இயல்பு உணர்ந்தோரே.",
            "vilakkam": 
            {
              "paadal_category": "Mutaṟ-poruḷ (முதற்-பொருள்)",
              "paadal_meaning": "Men of the world say that mutaṟ-poruḷ (முதற்-பொருள்) consists of place and time."
            }
          },
          {
            "paadal": "மாயோன் மேய காடு உறை உலகமும் \nசேயோன் மேய மை வரை உலகமும் \nவேந்தன் மேய தீம் புனல் உலகமும் \nவருணன் மேய பெரு மணல் உலகமும் \nமுல்லை குறிஞ்சி மருதம் நெய்தல் எனச் \nசொல்லிய முறையான் சொல்லவும் படுமே.",
            "vilakkam": 
            {
              "paadal_category": "The Landscape Division",
              "paadal_meaning": "#The forest region presided by Viṣṇu (விஷ்ணு), the mountain region presided by Murukaṉ (முருகன்), the region of sweet waters presided by Indiraṉ (இந்திரன்), and the region of extensive sand presided by Varunā (வருணா) are said to be in the order mentioned, mullai (முல்லை), kurinci (குறிஞ்சி), marutam (மருதம்) and neytal (நெய்தல்)."
            }
          },
          {
            "paadal": "காரும் மாலையும் முல்லை.",
            "vilakkam": 
            {
              "paadal_category": "Season and Time",
              "paadal_meaning": "(It is appropriate that) mullai(முல்லை) is applied to winter season and the first third part of the night."
            }
          },
          {
            "paadal": "குறிஞ்சி, \nகூதிர் யாமம் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "The Hilly Tract",
              "paadal_meaning": "Learned men say that Kuṟiñci(குறிஞ்சி) is applied to śarad-tu (Autumn Season)or autumn and second third part of the night."
            }
          },
          {
            "paadal": "பனி எதிர் பருவமும் உரித்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Hilly Tract",
              "paadal_meaning": "#They say that the hēmanta-rtu (winter season)  or the first half of the dewy season also deserves to be taken under Kuṟiñci(குறிஞ்சி) ."
            }
          },
          {
            "paadal": "வைகறை விடியல் மருதம்.",
            "vilakkam": 
            {
              "paadal_category": "The Cultivable Tract",
              "paadal_meaning": "Marutam (மருதம்) is applied to the last third part of the night and daybreak."
            }
          },
          {
            "paadal": "எற்பாடு, \nநெய்தல் ஆதல் மெய் பெறத் தோன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "The Littoral Tract",
              "paadal_meaning": "Neytal (நெய்தல்) is applied to afternoon."
            }
          },
          {
            "paadal": "நடுவுநிலைத் திணையே நண்பகல் வேனிலொடு \nமுடிவு நிலை மருங்கின் முன்னிய நெறித்தே.",
            "vilakkam": 
            {
              "paadal_category": "The Arid Tract",
              "paadal_meaning": "The Tiṉai (திணை) in the middle has for its region that which is suited to the middle part of the day associated with spring and summer."
            }
          },
          {
            "paadal": "பின்பனிதானும் உரித்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Arid Tract",
              "paadal_meaning": "They say that Śiśira-Ṛtu (குளிர்காலம்) also is suited to it."
            }
          },
          {
            "paadal": "இரு வகைப் பிரிவும் நிலை பெறத் தோன்றலும் \nஉரியது ஆகும் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Two Modes of Separation",
              "paadal_meaning": "Learned men say that separation may be classified in two ways."
            }
          },
          {
            "paadal": "திணை மயக்குறுதலும் கடி நிலை இலவே \nநிலன் ஒருங்கு மயங்குதல் இல என மொழிப \nபுலன் நன்கு உணர்ந்த புலமையோரே.",
            "vilakkam": 
            {
              "paadal_category": "Acceptable Deviation",
              "paadal_meaning": "That Aspects of land and time Assigned to given tract Do get mixed with those of another tract is no deviation unacceptable Yet, no commingling is permitted among the tracts themseveles; So goes the norm by men of discerment"
            }
          },
          {
            "paadal": "உரிப்பொருள் அல்லன மயங்கவும் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Acceptable Deviation",
              "paadal_meaning": "Those (aspects of land and time, and distinctive features of the tracts) other than the Akam (அகம்) love behaviour do mark intermingling."
            }
          },
          {
            "paadal": "புணர்தல் பிரிதல் இருத்தல் இரங்கல் \nஊடல் அவற்றின் நிமித்தம் என்றிவை \nதேரும் காலை திணைக்கு உரிப்பொருளே.",
            "vilakkam": 
            {
              "paadal_category": "The Fivefold Akam (அகம்) Love Behaviour",
              "paadal_meaning": "Union, separation, endurance pining and sulking, and the motives therein are perceived to be the strands of Akam (அகம்)  love behaviour (proper to the five tracts of kuṟiñci (குறிஞ்சி), pālai (பாலை), mullai (முல்லை), neytal (நெய்தல்) and marutam (மருதம்) respectively)."
            }
          },
          {
            "paadal": "கொண்டு தலைக்கழிதலும் பிரிந்து அவண் இரங்கலும் \nஉண்டு என மொழிப ஓர் இடத்தான.",
            "vilakkam": 
            {
              "paadal_category": "The Fivefold Akam (அகம்) Love Behaviour",
              "paadal_meaning": "They say that taking away (the lady love) with him and both pining after the separation of the object of love come under one class." 
            }
          },
          {
            "paadal": "கலந்த பொழுதும் காட்சியும் அன்ன.",
            "vilakkam": {
              "paadal_category": "The Fivefold Akam (அகம்) Love Behaviour",
              "paadal_meaning": "The mental attitude of the lover both on seeing the lady and meeting her is of the same clase, i.e., pālai-t-tiṇai (பாலை - திணை)  ."  
            }
          },
          {
            "paadal": "முதல் எனப்படுவது ஆயிரு வகைத்தே.",
            "vilakkam": {
              "paadal_category": "The Fivefold Akam (அகம்) Love Behaviour",
              "#paadal_meaning": "The deity, food, beast, tree, bird, drum, profession, pan or the melody-type of yāḻ (யாழ்) , etc., found in the two kinds of mutaṟ- poruḷ (முத்தர் பொருள்) are said to be karu-p-poruḷ (கருப் பொருள்)."
            }
          },
          {
            "paadal": "தெய்வம் உணாவே மா மரம் புள் பறை \nசெய்தி யாழின் பகுதியொடு தொகைஇ \nஅவ் வகை பிறவும் கரு என மொழிப.",
            "vilakkam": {
              "paadal_category": "The Physical Features of Land",
              "paadal_meaning": "God ,food ,animal ,tree ,bird ,drum ,occupation and lute and such of these constitude the distinctive physical features of the given tract of land."
            }
          },
          {
            "paadal": "எந் நில மருங்கின் பூவும் புள்ளும் \nஅந் நிலம் பொழுதொடு வாரா ஆயினும் \nவந்த நிலத்தின் பயத்த ஆகும்.",
            "vilakkam": {
              "paadal_category": "The Physical Features of Land",
              "#paadal_meaning": "Flowers and birds belonging to their respective tract and season, when described with reference to a different tract or season, have to be considered for the time being to belong to that tract and season."
            }
          },
          {
            "paadal": "பெயரும் வினையும் என்று ஆயிரு வகைய \nதிணைதொறும் மரீஇய திணை நிலைப் பெயரே.",
            "vilakkam": {
              "paadal_category": "The Naming of Characters",
              "paadal_meaning": "The names of the permanent residents with reference to each tiṇai (திணை) are of two kinds: one taken from their family and the other from their profession."
            }
          },
          {
            "paadal": "ஆயர் வேட்டுவர் ஆடூஉத் திணைப் பெயர் \nஆவயின் வரூஉம் கிழவரும் உளரே.",
            "vilakkam": {
              "paadal_category": "The Naming of Characters",
              "paadal_meaning": "The names of men are āyar (ஆயர்) and vēṭṭuvar (வேட்டுவர்) . Among them there may be chieftains."
            }
          },
          {
            "paadal": "ஏனோர் மருங்கினும் எண்ணும் காலை \nஆனா வகைய திணை நிலைப் பெயரே.",
            "vilakkam": {
              "paadal_category": "The Naming of Characters",
              "paadal_meaning": "On examination, the names of the permanent residents of other tiṇai (திணை) are of the same sort as in mullai(முல்லை)."
            }
          },
          {
            "paadal": "அடியோர் பாங்கினும் வினைவலர் பாங்கினும் \nகடிவரை இல புறத்து என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Lowly men as Akam (அகம்) Personae",
              "paadal_meaning": "Learned men say that puṇartal(புணர்தல்), pirital(பிரித்தல்) etc., are not avoided among slaves and servants, but they are outside the range of the five tiṇais (திணை) mentioned, i.t. they belong to kaikkiḷai(கைக்கிளை) and peruntiṇai (பெருந்திணை)."
            }
          },
          {
            "paadal": "ஏவல் மரபின் ஏனோரும் உரியர் \nஆகிய நிலைமை அவரும் அன்னர்.",
            "vilakkam": {
              "paadal_category": "Lowly men as Akam (அகம்) Personae",
              "paadal_meaning": "Others also may be servants, when they may be the heroes and heroines of kaikkiḷai (கைக்கிளை)  and peruntiṇai (பெருந்திணை)."
            }
          },
          {
            "paadal": "ஓதல் பகையே தூது இவை பிரிவே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "The causes of pirivu (பிரிவு) are study, enmity and embassy."
            }
          },
          {
            "paadal": "அவற்றுள், \nஓதலும் தூதும் உயர்ந்தோர் மேன.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "Of them, pirivu (பிரிவு) for study and embassy is found among higher classes of men."
            }
          },
          {
            "paadal": "தானே சேறலும் தன்னொடு சிவணிய \nஏனோர் சேறலும் வேந்தன் மேற்றே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "Going against (the enemy) in person or others accompanying him are found among kings."
            }
          },
          {
            "paadal": "மேவிய சிறப்பின் ஏனோர் படிமைய \nமுல்லை முதலாச் சொல்லிய முறையான் \nபிழைத்தது பிழையாது ஆகல் வேண்டியும் \nஇழைத்த ஒண் பொருள் முடியவும் பிரிவே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "Separation may ensue on account of setting right the irregularities in temples having the idols of gods and among men of all tracts commencing with mullai (முல்லை) mentioned before and on account of making immense wealth of finest type."
            }
          },
          {
            "paadal": "மேலோர் முறைமை நால்வர்க்கும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "The right of those mentioned first in the previous sutrā vests with all the four (i.e.) Brāhmans(பிராமணர்), Kṣatriyas(க்ஷத்திரியர்கள்), Vaiśyos(வைசியோஸ்) and Velālas(வேளாளர்கள்)."
            }
          },
          {
            "paadal": "மன்னர் பாங்கின் பின்னோர் ஆகுப.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "Piṉṉōr(பின்னோர்) (those mentioned next (i.e.) those to set right the irregularities of people) come under the class of kings (i.e.) Kṣatriyas (க்ஷத்திரியர்கள்)."
            }
          },
          {
            "paadal": "உயர்ந்தோர்க்கு உரிய ஓத்தினான.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "Separation on account of making choice wealth is allow able to the uyarṉtōr (உயர்ந்தோர்) in the way in which it is sanctioned in the Vedas(வேதங்கள்)."
            }
          },
          {
            "paadal": "வேந்து வினை இயற்கை வேந்தன் ஒரீஇய \nஏனோர் மருங்கினும் எய்து இடன் உடைத்தே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "The nature of looking after the duties of kings is found even in men other than kings."
            }
          },
          {
            "paadal": "பொருள்வயின் பிரிதலும் அவர்வயின் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "They are also entitled for pirivu (பிரிவு) on account of poruḷ(பொருள்)."
            }
          },
          {
            "paadal": "உயர்ந்தோர் பொருள்வயின் ஒழுக்கத்தான.",
            "vilakkam": {
              "paadal_category": "Modes of Separation",
              "paadal_meaning": "If uyarntōr (உயர்ந்தோர்) take, to pirivu (பிரிவு) on account of poruḷ(பொருள்) they should stick to their ācāra(ஆச்சாரா) or rules of conduct enjoined in smṛtis(ஸ்ம்ருதி)."
            }
          },
          {
            "paadal": "முந்நீர் வழக்கம் மகடூஉவொடு இல்லை.",
            "vilakkam": {
              "paadal_category": "Voyage on the sea",
              "paadal_meaning": "The hero does not take the heroine with him while he undertakes a voyage on the seas."
            }
          },
          {
            "paadal": "எத்திணை மருங்கினும் மகடூஉ மடல்மேல் \nபொற்புடை நெறிமை இன்மையான.",
            "vilakkam": {
              "paadal_category": "A Convention on Palmyra-horse (பனைமரக் குதிரை) riding",
              "paadal_meaning": "Women of any class are prohibited from mounting themselves on a horse of palmyra stems (பனை தண்டுகள்) to proclaim their love publicly, since it is devoid of refinement."
            }
          },
          {
            "paadal": "தன்னும் அவனும் அவளும் சுட்டி \nமன்னும் நிமித்தம் மொழிப் பொருள் தெய்வம் \nநன்மை தீமை அச்சம் சார்தல் என்று \nஅன்ன பிறவும் அவற்றொடு தொகைஇ \nமுன்னிய காலம் மூன்றுடன் விளக்க \nதோழி தேஎத்தும் கண்டோ ர் பாங்கினும் \nபோகிய திறத்து நற்றாய் புலம்பலும் \nஆகிய கிளவியும் அவ் வழி உரிய.",
            "vilakkam": {
              "paadal_category": "Utterance by the Heroine's Mother",
              "paadal_meaning": "When the lover has taken the lady-love with him without the knowledge of her parents, her mother is made to bewail and express her thoughts with reference to herself, the lover and the lady-love .(1) from the omens, (2) from omen-serving- words, and (3) from the prophetic expression of men possessed of spirits-what good, bad or danger, etc., befell them in the past, befall them in the present and will befall in the future to herself, her friends and those that were sent in search of her."
            }
          },
          {
            "paadal": "ஏமப் பேரூர்ச் சேரியும் சுரத்தும் \nதாமே செல்லும் தாயரும் உளரே.",
            "vilakkam": {
              "paadal_category": "Foster-mother in Search of the Eloped Heroine",
              "paadal_meaning": "Mothers may go in search of them through the streets of well-governed big cities or through jungles."
            }
          },
          {
            "paadal": "அயலோர் ஆயினும் அகற்சி மேற்றே.",
            "vilakkam": {
              "paadal_category": "A Convention of Elopement as Separation",
              "paadal_meaning": "Even when the elopement takes the lovers to another house close by within the town, It is to be regarded as separation mode [Of the Akam (அகம்) love conduct]."
            }
          },
          {
            "paadal": "தலைவரும் விழும நிலை எடுத்து உரைப்பினும் \nபோக்கற்கண்ணும் விடுத்தற்கண்ணும் \nநீக்கலின் வந்த தம் உறு விழுமமும் \nவாய்மையும் பொய்ம்மையும் கண்டோ ற் சுட்டித் \nதாய் நிலை நோக்கித் தலைப்பெயர்த்துக் கொளினும் \nநோய் மிகப் பெருகித் தன் நெஞ்சு கலுழ்ந்தோளை \nஅழிந்தது களை என மொழிந்தது கூறி \nவன்புறை நெருங்கி வந்ததன் திறத்தொடு \nஎன்று இவை எல்லாம் இயல்புற நாடின் \nஒன்றித் தோன்றும் தோழி மேன.",
            "vilakkam": {
              "paadal_category": "Utterance by the Confidante",
              "paadal_meaning": "#It is left to the intimate companion of the lady-love to describle the impending dangers, to persuade the lover to go (to foreign countries), to send the lady-love with him, to make the fostermother going in search of the lady return by telling her the views of smṛti (ஸ்ம்ருதி) writers about dharma (தர்மம்) and adharma (அதர்மம்) and to approach the lady's mother to console her with the words said by the lover to her daughter when she was in excessive love-sickness, etc."
            }
          },
          {
            "paadal": "பொழுதும் ஆறும் உட்கு வரத் தோன்றி \nவழுவின் ஆகிய குற்றம் காட்டலும் \nஊரது சார்பும் செல்லும் தேயமும்  \nஆர்வ நெஞ்சமொடு செப்பிய வழியினும் \nபுணர்ந்தோர் பாங்கின் புணர்ந்த நெஞ்சமொடு \nஅழிந்து எதிர் கூறி விடுப்பினும் ஆங்கத்  \nதாய் நிலை கண்டு தடுப்பினும் விடுப்பினும் \nசேய் நிலைக்கு அகன்றோர் செலவினும் வரவினும் \nகண்டோ ர் மொழிதல் கண்டது என்ப.",
            "vilakkam": {
              "paadal_category": "Utterance by the Passers-by",
              "paadal_meaning": "They say that the sayings of those that met them on their way are found with reference to the following points: enumeration of the dangers that may befall them on account of the frightening part of the day and the route; mention of the proximity of the village and the long distance of their destination with sincerity of heart; allowing them to proceed after dissuading them with the warmth of heart; dissuading the foster mother from proceeding further and then permitting her; their departure to distant lands and their return."
            }
          },
          {
            "paadal": "ஒன்றாத் தமரினும் பருவத்தும் சுரத்தும் \nஒன்றிய மொழியொடு வலிப்பினும் விடுப்பினும் \nஇடைச் சுர மருங்கின் அவள் தமர் எய்திக் \nகடைக் கொண்டு பெயர்தலின் கலங்கு அஞர் எய்திக்  \nகற்பொடு புணர்ந்த கௌவை உளப்பட \nஅப் பால் பட்ட ஒரு திறத்தானும் \nநாளது சின்மையும் இளமையது அருமையும் \nதாளாண் பக்கமும் தகுதியது அமைதியும் \nஇன்மையது இளிவும் உடைமையது உயர்ச்சியும் \nஅன்பினது அகலமும் அகற்சியது அருமையும் \nஒன்றாப் பொருள்வயின் ஊக்கிய பாலினும்  \nவாயினும் கையினும் வகுத்த பக்கமொடு   \nஊதியம் கருதிய ஒரு திறத்தானும்  \nபுகழும் மானமும் எடுத்து வற்புறுத்தலும்  \nதூது இடையிட்ட வகையினானும்  \nஆகித் தோன்றும் பாங்கோர் பாங்கினும்  \nமூன்றன் பகுதியும் மண்டிலத்து அருமையும்  \nதோன்றல் சான்ற மாற்றோர் மேன்மையும்  \nபாசறைப் புலம்பலும் முடிந்த காலத்த  \nபாகனொடு விரும்பிய வினைத்திற வகையினும் \nகாவற் பாங்கின் ஆங்கோர் பக்கமும்  \nபரத்தையின் அகற்சியின் பரிந்தோட் குறுகி  \nஇரத்தலும் தெளித்தலும் என இரு வகையொடு  \nஉரைத் திற நாட்டம் கிழவோன் மேன.",
            "vilakkam": {
              "paadal_category": "Utterance by the Hero",
              "paadal_meaning": "It is the privilege of the lover or the husband to speak (1) when he takes the lady-love with her consent through desert tract in inconvenient season from her relatives who did not agree to it, (2) when he leaves her for the reason that her relatives did not agree, that the season is inconvenient and the desert tract is impassable (3) when her relatives ( father and elder brother) overtake them in the desert and she, fearing that they will take her back, openly tells them her resolve to go with him, (4) when he is determined to make money in foreign countries without being dissuaded by the shortness of life, transitoriness of youth, the dangers to be encountered, the prosperity of the attempt, the precariousness of being in want, the dignity of riches, the depth of love and the difficulty of separation, (5) when he is bent upon profitting himself with the study of scriptures and fine arts, (6) when he impresses upon his wife the fame and name he should get, (7) when he goes on embassy, (8) when he speaks of the strength of himself, his allies and his foes, the difficulty of capturing the enemy's fort and the high dignity and superio rity of his foes, (10) when he soliloquizes about his wife's separation in the tent, (11) when he after the war is over asks his charioteer to drive at greater speed, (12) when he is posted as sentinel and (13) when he, after his company with courtezan, beseeches his wife for pardon and comes to terms with her."
            }
          },
          {
            "paadal": "எஞ்சியோர்க்கும் எஞ்சுதல் இலவே.",
            "vilakkam": {
              "paadal_category": "Utterance by Others",
              "paadal_meaning": "Others also are not prohibited to have their say."
            }
          },
          {
            "paadal": "நிகழ்ந்தது நினைத்தற்கு ஏதுவும் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Other contexts of Utterance",
              "paadal_meaning": "Pirivu (பிரிவு) may be the case of the lover and the lady-love to think of past event."
            }
          },
          {
            "paadal": "நிகழ்ந்தது கூறி நிலையலும் திணையே.",
            "vilakkam": {
              "paadal_category": "Other contexts of Utterance",
              "paadal_meaning": "Staying away describing what had happened is included in palai-t-tiṇai (பாலைத் திணை).Is it possible for the porul̥ (பொருள்) of one tiṇai (திணை) to get mixed with another tiṇai (திணை) ?."
            }
          },
          {
            "paadal": "மரபுநிலை திரியா மாட்சிய ஆகி \nவிரவும் பொருளும் விரவும் என்ப.",
            "vilakkam": {
              "paadal_category": "Blending of Land-time Features",
              "paadal_meaning": "They say that porul̥ (பொருள்) belonging to one tiṉai (திணை) may get mixed with another tiṉai (திணை) without going against the tradititional usage.Is there any way to determine the tiṇai (திணை) other than through the mutaṟporuḷ (முத்தர் பொருள்), karupporuḷ (கருப்பொருள்) and uripporuḷ (ஊர்ப்பொருள்) ?."
            }
          },
          {
            "paadal": "உள்ளுறை உவமம் ஏனை உவமம் எனத் \nதள்ளாது ஆகும் திணை உணர் வகையே.",
            "vilakkam": {
              "paadal_category": "A Function of Similes",
              "paadal_meaning": "A simile by suggestion and an ordinary simile are also means to determine the tiṇai (திணை).Where is uḷḷuṟai-y-uvamam (உள்ளுறை உவமம்) used?."
            }
          },
          {
            "paadal": "உள்ளுறை தெய்வம் ஒழிந்ததை நிலம் எனக் \nகொள்ளும் என்ப குறி அறிந்தோரே.",
            "vilakkam": {
              "paadal_category": "Nature and Function of the Suggestive Simile",
              "paadal_meaning": "Grammarians say that uḷḷuṟai (உள்ளுறை) is resorted to with reference to karupporuḷ (கருப்பொருள்) excluding the deities."
            }
          },
          {
            "paadal": "உள்ளுறுத்து இதனொடு ஒத்துப் பொருள் முடிக என \nஉள்ளுறுத்து இறுவதை உள்ளுறை உவமம்.",
            "vilakkam": {
              "paadal_category": "Nature and Function of the Suggestive Simile",
              "paadal_meaning": "Uḷḷuṟai-uvamam (உள்ளுறை உவமம்) is that wherein the prakṛtārtha (பிரக்ருதார்த்த) or the topic on hand is suggested from the description of aprakṛtārtha (அப்ரக்ருதார்த்த)."
            }
          },
          {
            "paadal": "ஏனை உவமம் தான் உணர் வகைத்தே.",
            "vilakkam": {
              "paadal_category": "Nature of Non-suggestive Similes",
              "paadal_meaning": "The other uvamam (உவமம்) is that wherein prakṛtārtha (பிரக்ருதார்த்த)  is explicitly compared to the aprakṛtartha (அப்ரக்ருதார்த்த) .What is kaikkiḷai (கைக்கிளை)?."
            }
          },
          {
            "paadal": "காமம் சாலா இளமையோள்வயின் \nஏமம் சாலா இடும்பை எய்தி \nநன்மையும் தீமையும் என்று இரு திறத்தான் \nதன்னொடும் அவளொடும் தருக்கிய புணர்த்து  \nசொல் எதிர் பெறாஅன் சொல்லி இன்புறல் \nபுல்லித் தோன்றும் கைக்கிளைக் குறிப்பே.",
            "vilakkam": {
              "paadal_category": "The Defining Features of Kaikkiḷai (கைக்கிளை)",
              "paadal_meaning": "Kaikkiḷai (கைக்கிளை) is suggested when a lover carried away by uncontrollable passion at the sight of an immature girl satisfies himself with the expressions that he suffers for no wrong of his and she wrongs to him on his receiving no reply from her."
            }
          },
          {
            "paadal": "ஏறிய மடல் திறம் இளமை தீர் திறம் \nதேறுதல் ஒழிந்த காமத்து மிகு திறம் \nமிக்க காமத்து மிடலொடு தொகைஇ \nசெப்பிய நான்கும் பெருந்திணைக் குறிப்பே.",
            "vilakkam": {
              "paadal_category": "The Defining Features of Peruntiṇai (பெருந்திணை)",
              "paadal_meaning": "Peruntiṇai (பெருந்திணை) is suggested from four things: maṭal-ēṟutal (மாதல் ஏருத்தல்) mounting up a horse made of palm (பனை) stems, the state of either the lover or the lady-love having passed the stage of youth, the state of completely forgetting oneself through extreme passion and their union in that state."
           }
          },
          {
            "paadal": "முன்னைய நான்கும் முன்னதற்கு என்ப.",
            "vilakkam": {
              "paadal_category": "Otheer Features of Kaikkiḷai (கைக்கிளை)",
              "paadal_meaning": "The stages preceding the four mentioned above belong to kaikkiḷai (கைக்கிளை) ."
            }
          },
          {
            "paadal": "நாடக வழக்கினும் உலகியல் வழக்கினும் \nபாடல் சான்ற புலனெறி வழக்கம் \nகலியே பரிபாட்டு ஆயிரு பாவினும் \nஉரியது ஆகும் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Metrical Forms Proper to Akam (அகம்) Poetry",
              "paadal_meaning": "Learned men say that Poetry in literature (relating to aka-t-tiṇai (அகத்திணை)) will be composed in the verses kali (கலி) or paripāṭṭu(பரிபாட்டு ) in consonance with the tradition followed in literature and the world."
            }
          },
          {
            "paadal": "மக்கள் நுதலிய அகன் ஐந்திணையும் \nசுட்டி ஒருவர்ப் பெயர் கொளப் பெறாஅர்.",
            "vilakkam": {
              "paadal_category": "Non-naming Convention",
              "paadal_meaning": "In the five tiṇais (திணை) which are in the middle where mention is made of human beings, their individual names should not be mentioned."
            }
          },
          {
            "paadal": "புறத்திணை மருங்கின் பொருந்தின் அல்லது \nஅகத்திணை மருங்கின் அளவுதல் இலவே.",
            "vilakkam": {
              "paadal_category": "Non-naming Convention",
              "paadal_meaning": "Individual names may be mentioned in pura-t-tiṉai(பொருந்திணை) and not in akattiṇai (அகத்திணை) ."
            }
          }
        ]
      },
      {
        "iyal_name": "புறத்திணையியல்",
        "iyal_eng":"Puṟam (புறம்) Life",
        "noorpa": [
          {
            "paadal": "அகத்திணை மருங்கின் அரில் தப உணர்ந்தோர் \nபுறத்திணை இலக்கணம் திறப்படக் கிளப்பின் \nவெட்சிதானே குறிஞ்சியது புறனே \nஉட்கு வரத் தோன்றும் ஈர் ஏழ் துறைத்தே.",
            "vilakkam": {
              "paadal_category": "Veṭci (வெட்சி) Theme",
              "paadal_meaning": "When those who have correctly understood the classification of akattiṇai (அகத்திணை)  begin to describe clearly the nature of puṟattiṇai (புறத்திணை), (they say) veṭci (வெட்சி) is the puṟattiṇai (புறத்திணை) corresponding to the akattiṇai (அகத்திணை)  kuṟiñci (குறிஞ்சி) and is clearly of fourteen tuṟai (துறை) or minor themes."          }
          },
          {
            "paadal": "வேந்து விடு முனைஞர் வேற்றுப் புலக் களவின் \nஆ தந்து ஓம்பல் மேவற்று ஆகும்.",
            "vilakkam": {
              "paadal_category": "Veṭci (வெட்சி) Theme",
              "paadal_meaning": "Veṭci(வெட்சி) has for its nature the commander of an army, at the instance of the king, taking away the cows of the enemies without their knowledge and keeping them safe."
            }
          },
          {
            "paadal": "படை இயங்கு அரவம் பாக்கத்து விரிச்சி \nபுடை கெடப் போகிய செலவே புடை கெட \nஒற்றின் ஆகிய வேயே வேய்ப்புறம் \nமுற்றின் ஆகிய புறத்து இறை முற்றிய \nஊர் கொலை ஆ கோள் பூசல் மாற்றே \nநோய் இன்று உய்த்தல் நுவல்வழித் தோற்றம் \nதந்து நிறை பாதீடு உண்டாட்டு கொடை என \nவந்த ஈர் ஏழ் வகையிற்று ஆகும்.",
            "vilakkam": {
              "paadal_category": "Substrands of the Veṭci (வெட்சி) Theme",
              "paadal_meaning": "Veṭci (வெட்சி) is of the following fourteen kinds: (1) the noise of trumpet, (2) words of unseen men in neighbouring villages serving as omen, (3) expedition without being seen by the enemy, (4) report of the spies without being seen by the enemy, (5) staying around the place suggested by the spies. (6) massacring the residents of the place, (7) taking away the cows, (8) successfully emerging from the conflict with the enemies, (9) not exposing the cows to misery, (10) appearing at the place suggested (by their own people), (11) stationing the cows taken, (12) classifying the cows, (13) pleasure-party with food, drink and dance, and (14) giving away the cows (to the needy)."
             }
          },
          {
            "paadal": "மறம் கடைக்கூட்டிய குடிநிலை சிறந்த \nகொற்றவை நிலையும் அத் திணைப் புறனே.",
            "vilakkam": {
              "paadal_category": "Substrands of the Veṭci (வெட்சி) Theme",
              "paadal_meaning": "Mustering the courage of the warriors by beating the tuṭi( துய்) drum and offering sacrifice and worship to Durgā(துர்கா) are taken to be the puṟam (புறம்) of that tiṇai (திணை)."
            }
          },
          {
            "paadal": "வெறி அறி சிறப்பின் வெவ் வாய் வேலன் \nவெறியாட்டு அயர்ந்த காந்தளும் உறு பகை \nவேந்திடை தெரிதல் வேண்டி ஏந்து புகழ் \nபோந்தை வேம்பே ஆர் என வரூஉம் \nமா பெருந்தானையர் மலைந்த பூவும் \nவாடா வள்ளி வயவர் ஏத்திய \nஓடாக் கழல் நிலை உளப்பட ஓடா \nஉடல் வேந்து அடுக்கிய உன்ன நிலையும் \nமாயோன் மேய மன் பெருஞ் சிறப்பின் \nதாவா விழுப் புகழ்ப் பூவை நிலையும் \nஆர் அமர் ஓட்டலும் ஆ பெயர்த்துத் தருதலும் \nசீர் சால் வேந்தன் சிறப்பு எடுத்து உரைத்தலும் \nதலைத் தாள் நெடுமொழி தன்னொடு புணர்த்தலும் \nஅனைக்கு உரி மரபினது கரந்தை அன்றியும் \nவரு தார் தாங்கல் வாள் வாய்த்துக் கவிழ்தல் என்று \nஇரு வகைப் பட்ட பிள்ளை நிலையும் \nவாள் மலைந்து எழுந்தோனை மகிழ்ந்து பறை தூங்க \nநாடு அவற்கு அருளிய பிள்ளையாட்டும் \nகாட்சி கால்கோள் நீர்ப்படை நடுதல் \nசீர்த்த மரபின் பெரும்படை வாழ்த்தல் என்று \nஇரு மூன்று மரபின் கல்லொடு புணரச் \nசொல்லப்பட்ட எழு மூன்று துறைத்தே.",
            "vilakkam": {
              "paadal_category": "The Ramifications of the Veṭci (வெட்சி) Theme",
              "paadal_meaning": "Veṭci (வெட்சி) is, in addition, of the following twenty-one tuṟais (துறை) : (1) dance under the possession of Skanda(ஸ்கந்தா) by a priest who is an adept in it and who expresses the ideas in seriousness, (2-4) wearing of the flowers of palmyra (பனைமரம்), margosa (வேம்பு) and common mountain ebony by the renowned warriors of vast and great armies to distinguish themselves from the kings of great enmity 1 , (5) a kind of dance called vāṭā-vaḷḷi (வாடா வள்ளி), (6) the state of anklet not slipping and being extolled by warriors (7) invoking an uṉṉam (உன்னம்) tree for omens before battle by warriors fierce and not receding from the place of action, (8) praising the bilberry flower that it resembles Viṣṇu (விஷ்ணு) in colour and hence it is noted for unfailing fame or comparing great men with Lord Viṣṇu () and other gods of unfailing fame, (9) making a terrible fight against those (who took away the cows) (10) taking back the cows, (11) extolling the superjoriity of the famous king, (12) warriors taking terrible vows within themselves with reference to the fulfilment of their pledge-six to ten belonging to karantai (கரந்தை)  ( 13 & 14), the two piḷḷai-nilai (பிள்ளை நிலை) of resisting the onslaughts of the enemy and falling a prey to the sword in battle, (15) the piḷḷai-y-āṭṭu (பிள்ளையாட்டு) of sending the fallen warriors to svarga (சொர்க்கம்) with the beating of drums * * * 8 , (16) finding the memorial stone, (17) taking away the memorial stone, (18) washing it with water, (19) fixing the same, (20) making the necessary inscription with due honour, and (21) extolling the same."
           }
          },
          {
            "paadal": "வஞ்சிதானே முல்லையது புறனே \nஎஞ்சா மண் நசை வேந்தனை வேந்தன் \nஅஞ்சு தகத் தலைச் சென்று அடல் குறித்தன்றே.",
            "vilakkam": {
              "paadal_category": "Vañci (வஞ்சி) Theme",
              "paadal_meaning": "Vañci (வஞ்சி) is the puṟaṉ (புறன்) of mullai (முல்லை) ; it consists of one king ferociously advancing towards another to kill him when the 1 itter wants to take possession of a land which the former wants for himself."
          }
          },
          {
            "paadal": "இயங்கு படை அரவம் எரி பரந்து எடுத்தல் \nவயங்கல் எய்திய பெருமையானும் \nகொடுத்தல் எய்திய கொடைமையானும் \nஅடுத்து ஊர்ந்து அட்ட கொற்றத்தானும் \nமாராயம் பெற்ற நெடுமொழியானும் \nபொருளின்று உய்த்த பேராண் பக்கமும் \nவரு விசைப் புனலைக் கற் சிறை போல \nஒருவன் தாங்கிய பெருமையானும் \nபிண்டம் மேய பெருஞ்சோற்று நிலையும் \nவென்றோர் விளக்கமும் தோற்றோர் தேய்வும் \nகுன்றாச் சிறப்பின் கொற்ற வள்ளையும் \nஅழி படை தட்டோ ர் தழிஞ்சியொடு தொகைஇ \nகழி பெருஞ் சிறப்பின் துறை பதின்மூன்றே.",
            "vilakkam": {
              "paadal_category": "Substrands of the Vañci (வஞ்சி) Theme",
              "paadal_meaning": "There are thirteen highly meritorious tuṟais (துறை) to vañci (வஞ்சி) :— (1) The din arising from the two armies, (2) setting fire on a large scale, (3) the greatness well exhibited, (4) giving away (weapons of warfare to soldiers) and presents, (5) heroism shown in killing (the enemies) by slowly approaching them, (6 ) words of congratulation on the military honour conferred upon by kings, (7) the highly valorous part of the army rushing against the enemy considering them to be insignificant, (8) the greatness of one resisting the attacks of the enemy like a stone, a huge flood, (9 ) the state of having large provisions of food, (10) the lustre of the victorious, (11) the dimness of the defeated, (12) the tribute (received from the enemy) on account of unmitigated valour or regretting the destruction of the enemy's country on account of unmitigated valour, and (13) the honour and presents offered to those who were maimed in battle."
          }
          },
          {
            "paadal": "உழிஞைதானே மருதத்துப் புறனே \nமுழு முதல் அரணம் முற்றலும் கோடலும் \nஅனை நெறி மரபிற்று ஆகும் என்ப.",
            "vilakkam": {
              "paadal_category": "Uḻiñai (உழிஞை) Theme",
              "paadal_meaning": "Uḻiñai (உழிஞை) is the puṟaṉ (புறன்) of marutam (மருதம்) and it is said that it is of the nature of besieging the external fort (of the enemy) and taking hold of it."        
          }
          },
          {
            "paadal": "அதுவேதானும் இரு நால் வகைத்தே.",
            "vilakkam": {
              "paadal_category": "Uḻiñai (உழிஞை) Theme",
              "paadal_meaning": "It is of eight kinds."
            }
          },
          {
            "paadal": "கொள்ளார் தேஎம் குறித்த கொற்றமும் \nஉள்ளியது முடிக்கும் வேந்தனது சிறப்பும் \nதொல் எயிற்கு இவர்தலும் தோலது பெருக்கமும் \nஅகத்தோன் செல்வமும் அன்றியும் முரணிய \nபுறத்தோன் அணங்கிய பக்கமும் திறல் பட \nஒரு தான் மண்டிய குறுமையும் உடன்றோர் \nவரு பகை பேணார் ஆர் எயில் உளப்பட \nசொல்லப்பட்ட நால் இரு வகைத்தே.",
            "vilakkam": {
              "paadal_category": "Substrands of the Uḻiñai (உழிஞை) Theme",
              "paadal_meaning": "It is of the following eight kinds:—(1) the act of a king directed towards capturing the country of his enemy 1 * 3 (who does not accept his suzerainty or obey his com mud), (2) the greatnessof the king in carryingout his wishes (3) proceeding towards the ancient fort (of the enemy) (4) the vastness of elephantry 4 (5) the riches of the besieged king, (6) the difficulties experienced by the besieger 5 (7) the pitiable situation of the besieged in resisting alone, and (8) the piteous fort of the beseiged who cannot resist the onslaughts of the besieger."    
          }
          },
          {
            "paadal": "குடையும் வாளும் நாள்கோள் அன்றி \nமடை அமை ஏணிமிசை மயக்கமும் கடைஇச் \nசுற்று அமர் ஒழிய வென்று கைக்கொண்டு \nமுற்றிய முதிர்வும் அன்றி முற்றிய \nஅகத்தோன் வீழ்ந்த நொச்சியும் மற்று அதன் \nபுறத்தோன் வீழ்ந்த புதுமையானும் \nநீர்ச் செரு வீழ்ந்த பாசியும் அதாஅன்று \nஊர்ச் செரு வீழ்ந்த மற்றதன் மறனும் \nமதில்மிசைக்கு இவர்ந்த மேலோர் பக்கமும் \nஇகல் மதில் குடுமி கொண்ட மண்ணுமங்கலமும் \nவென்ற வாளின் மண்ணொடு ஒன்ற \nதொகைநிலை என்னும் துறையொடு தொகைஇ \nவகை நால் மூன்றே துறை என மொழிப.",
            "vilakkam": {
              "paadal_category": "The Ramifications of the Uḻiñai (உழிஞை) Theme",
              "paadal_meaning":"On the other hand, they say that there are twelve tuṟais(துறை) (to it) :(1) Kuṭai-nāṭ-kōḷ (குடைநாள்கோள்) or sending the royal umbrella in an auspicious hour, (2) vāl-nal-kol(வாள்நாள்கோள்) or sending the sword in an auspicious hour, (3) the clash between the two armies when the army of the besieger is getting up through ladders, (4) the besieger besieging the inner fort after capturing the outer one by killing in battle the army of the enemy, (5) the defence desired by the besieged, (6) the miraculous attack desired by the besieger, (7) the army defeated at the battle in the moat, (8) the complete disaster of the army fallen in the battle within the fort, (9) the attack of those who spread themselves on the fort and consequently are on a higher level, (10) the purificatory bath of the besieger after gaining victory in the fort and taking hold of the crown of the beseiged or assuming the crown, name and title of his vanquished enemy, (11) the purificatory bath to the sword of the victor and (12) collecting the armies of the victor so as to be honoured."   }
          },
          {
            "paadal": "தும்பைதானே நெய்தலது புறனே \nமைந்து பொருளாக வந்த வேந்தனைச் \nசென்று தலை அழிக்கும் சிறப்பிற்று என்ப.",
            "vilakkam": {
              "paadal_category": "Tumpai (தும்பை) Theme",
              "paadal_meaning": "Tumpai (தும்பை) is the puṟaṉ (புறன்) of neytal (நெய்தல்) and possesses the high feature of one king eager of fame attacking another and the latter too eager of the same fame meeting him in open fight and destroying them."     
          }
          },
          {
            "paadal": "கணையும் வேலும் துணையுற மொய்த்தலின் \nசென்ற உயிரின் நின்ற யாக்கை \nஇரு நிலம் தீண்டா அரு நிலை வகையொடு \nஇரு பாற் பட்ட ஒரு சிறப்பின்றே.",
            "vilakkam": {
              "paadal_category": "Tumpai (தும்பை) Theme",
              "paadal_meaning": "The body lying on the earth after life has departed on account of the shower of arrows and incessant throw of spears, with that which dances not being in contact with the wide earth is of superior excellence both ways."    
          }
          },
          {
            "paadal": "தானை யானை குதிரை என்ற \nநோனார் உட்கும் மூ வகை நிலையும் \nவேல் மிகு வேந்தனை மொய்த்தவழி ஒருவன் \nதான் மீண்டு எறிந்த தார் நிலை அன்றியும் \nஇருவர் தலைவர் தபுதிப் பக்கமும் \nஒருவன் ஒருவனை உடை படை புக்கு \nகூழை தாங்கிய எருமையும் படை அறுத்து \nபாழி கொள்ளும் ஏமத்தானும் \nகளிறு எறிந்து எதிர்ந்தோர் பாடும் களிற்றொடு \nபட்ட வேந்தனை அட்ட வேந்தன் \nவாளோர் ஆடும் அமலையும் வாள் வாய்த்து \nஇரு பெரு வேந்தர்தாமும் சுற்றமும் \nஒருவரும் ஒழியாத் தொகைநிலைக்கண்ணும் \nசெருவகத்து இறைவன் வீழ்ந்தென சினைஇ \nஒருவன் மண்டிய நல் இசை நிலையும் \nபல் படை ஒருவற்கு உடைதலின் மற்றவன் \nஒள் வாள் வீசிய நூழிலும் உளப்படப் \nபுல்லித் தோன்றும் பன்னிரு துறைத்தே",
            "vilakkam": {
              "paadal_category": "Substrands of the Tumpai (தும்பை) Theme",
              "paadal_meaning": "Tumpai (தும்பை) is of twelve tuṟais (துறை) : (1-3) the three stages of the infantry, elephantry, and cavalry creating awe in the friends of foes, (4) the state of the army when one, seeing that the king fighting with his spear is surrounded with foes, leaves his scene of action and comes to his rescue, (5) the piteous scene where the commanders of both sides have fallen dead, (6) unyielding resistence of a warrior entering into the thick of the fight and protecting the rear of the rmy when the army is on the point of being broken by the enemy (7) success in hand-to-hand fight without weapons, (8) the greatness of attacking elephants with those who are on them (9) eulogy 1 of the king who has fallen with his elephant by the warriors of the victorious king, (10) state when both kings with their armies fight with their swords and stand balanced in the battle- filed 2 (11) the scene when a warrior wins undying fame by dashing against the enemy in rage when he finds that their king was killed by them, and (12) one slaughtering by brandishing his sword the different sections of the enemv's army broken on his advance."         
          }
          },
          {
            "paadal": "வாகைதானே பாலையது புறனே \nதா இல் கொள்கைத் தம்தம் கூற்றைப் \nபாகுபட மிகுதிப் படுத்தல் என்ப.",
            "vilakkam": {
              "paadal_category": "Vākai vakai (வாகை) Theme",
              "paadal_meaning": "Vākai (வாகை) is the puṟaṉ (புறன்) of pālai (பாலை) and it is of the nature of eulogising spotless objects coming within one's experience."
          }
          },
          {
            "paadal": "அறு வகைப் பட்ட பார்ப்பனப் பக்கமும் \nஐ வகை மரபின் அரசர் பக்கமும் \nஇரு மூன்று மரபின் ஏனோர் பக்கமும் \nமறு இல் செய்தி மூ வகைக் காலமும் \nநெறியின் ஆற்றிய அறிவன் தேயமும் \nநால் இரு வழக்கின் தாபதப் பக்கமும் \nபால் அறி மரபின் பொருநர்கண்ணும் \nஅனை நிலை வகையொடு ஆங்கு எழு வகையான் \nதொகை நிலைபெற்றது என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Modes of Vocations",
              "paadal_meaning": "Learned men say that vakai-t-tiṉai(வாகைத்திணை) is classified in seven ways :— (1) that which relates to the six duties of brahmans (பிராமணர்கள்), (2) that which relates to the five duties of kings, (3 & 4) that which relates to the six duties of each of vanikar(வணிகர்) , & velalar(வேளாளர்) (5) that which relates to the great who are spotless in their conduct in all the three times-past, present and future (6) that which relates to the eight duties of recluses and (7) that which relates to the warriors who are conversant with their duties."
            }
          },
          {
            "paadal": "கூதிர் வேனில் என்று இரு பாசறைக் \nகாதலின் ஒன்றிக் கண்ணிய வகையினும் \nஏரோர் களவழி அன்றி களவழித் \nதேரோர் தோற்றிய வென்றியும் தேரோர் \nவென்ற கோமான் முன்தேர்க் குரவையும் \nஒன்றிய மரபின் பின்தேர்க் குரவையும் \nபெரும் பகை தாங்கும் வேலினானும் \nஅரும் பகை தாங்கும் ஆற்றலானும் \nபுல்லா வாழ்க்கை வல்லாண் பக்கமும் \nஒல்லார் நாண பெரியவர்க் கண்ணிச் \nசொல்லிய வகையின் ஒன்றொடு புணர்ந்து \nதொல் உயிர் வழங்கிய அவிப்பலியானும் \nஒல்லார் இடவயின் புல்லிய பாங்கினும் \nபகட்டினானும் ஆவினானும் \nதுகள் தபு சிறப்பின் சான்றோர் பக்கமும் \nகடி மனை நீத்த பாலின்கண்ணும் \nஎட்டு வகை நுதலிய அவையகத்தானும் \nகட்டு அமை ஒழுக்கத்துக் கண்ணுமையானும் \nஇடை இல் வண் புகழ்க் கொடைமையானும் \nபிழைத்தோர்த் தாங்கும் காவலானும் \nபொருளொடு புணர்ந்த பக்கத்தானும் \nஅருளொடு புணர்ந்த அகற்சியானும் \nகாமம் நீத்த பாலினானும் என்று \nஇரு பாற் பட்ட ஒன்பதின் துறைத்தே",
            "vilakkam": {
              "paadal_category": "Substrands of the Vākai (வாகை) Theme",
              "paadal_meaning": "Vākai (வாகை) is of twice nine kinds of tuṟai (துறை) , (the first nine with reference to maṟam (மறம்) (valour) and the second nine with reference to (aṟam (அறம்) or dharma (தர்மம்)) : (1) The undivided attention to war in the camps both in winter and in summer, (2) the success gained by the warriors in the battlefield similar to that achieved by the agriculturists in the threshing floor, (3) the dance before the king's chariot at the success of the warriors (4) the traditional dance behind his chariot, (5) the spear which was able to withstand the attacks of the foes, (6) the capacity of the warriors to withstand the strong attacks of the foes. (7) able-bodied warriors fighting with the conviction that the physical body is transitory (8) throwing oneself in fire according to the tenets of the great which makes the foes feel ashamed, (9) taking hold of the enemy's country, (10) those winning fame through oxen and cows 1 (11) avoiding amorous look towards other's wives, 2 (12) the assembly of the great possessing eight qualities 3 (13) conduct according to śāstras() (14) incessant liberality bringing rich fame, (15) protecting the evil doers forgetting their wrongs, (16) identifying oneself with his duties as householder, warrior, or recluse, (17) leaving off the ties of the family on account of the feeling that all are alike and (18) the stage when desire vanishes."       
          }
          },
          {
            "paadal": "காஞ்சிதானே பெருந்திணைப் புறனே \nபாங்கு அருஞ் சிறப்பின் பல் ஆற்றானும் \nநில்லா உலகம் புல்லிய நெறித்தே. ",
            "vilakkam": {
              "paadal_category": "Kāñci (காஞ்சி)  Theme",
              "paadal_meaning": "Kāñci (காஞ்சி) is the puṟaṉ (புறன்) of perun-tiṇai (பெருந்திணை) and deals with the unparallelled transitioriness of the worldly objects in all ways."   
          }
          },
          {
            "paadal": "மாற்ற அருங் கூற்றம் சாற்றிய பெருமையும் \nகழிந்தோர் ஒழிந்தோர்க்குக் காட்டிய முதுமையும் \nபண்பு உற வரூஉம் பகுதி நோக்கிப் \nபுண் கிழித்து முடியும் மறத்தினானும் \nஏமச் சுற்றம் இன்றிப் புண்ணோற் \nபேஎய் ஓம்பிய பேஎய்ப் பக்கமும் \nஇன்னன் என்று இரங்கிய மன்னையானும் \nஇன்னது பிழைப்பின் இது ஆகியர் எனத் \nதுன்ன அருஞ் சிறப்பின் வஞ்சினத்தானும் \nஇன் நகை மனைவி பேஎய் புண்ணோன \nதுன்னுதல் கடிந்த தொடாஅக் காஞ்சியும் \nநீத்த கணவன் தீர்த்த வேலின் \nபேஎத்த மனைவி ஆஞ்சியானும் \nநிகர்த்து மேல் வந்த வேந்தனொடு முதுகுடி \nமகட்பாடு அஞ்சிய மகட்பாலானும் \nமுலையும் முகனும் சேர்த்திக் கொண்டோன் \nதலையொடு முடிந்த நிலையொடு தொகைஇ \nஈர் ஐந்து ஆகும் என்ப பேர் இசை \nமாய்ந்த மகனைச் சுற்றிய சுற்றம் \nமாய்ந்த பூசல் மயக்கத்தானும் \nதாமே எய்திய தாங்க அரும் பையுளும் \nகணவனொடு முடிந்த படர்ச்சி நோக்கிச் \nசெல்வோர் செப்பிய மூதானந்தமும் \nநனி மிகு சுரத்திடைக் கணவனை இழந்து \nதனி மகள் புலம்பிய முதுபாலையும் \nகழிந்தோர் தேஎத்துக் கழி படர் உறீஇ \nஒழிந்தோர் புலம்பிய கையறு நிலையும் \nகாதலி இழந்த தபுதார நிலையும் \nகாதலன் இழந்த தாபத நிலையும் \nநல்லோள் கணவனொடு நளி அழல் புகீஇச் \nசொல் இடையிட்ட பாலை நிலையும் \nமாய் பெருஞ் சிறப்பின் புதல்வற் பயந்த \nதாய் தப வரூஉம் தலைப்பெயல் நிலையும் \nமலர் தலை உலகத்து மரபு நன்கு அறியப் \nபலர் செலச் செல்லாக் காடு வாழ்த்தொடு \nநிறை அருஞ் சிறப்பின் துறை இரண்டு உடைத்தே.",
            "vilakkam": {
              "paadal_category": "Substrands of the Kāñci (காஞ்சி)  Theme",
              "paadal_meaning": "Kāñci(காஞ்சி) has two sets of ten tuṟais (துறை)  each the first set consisting of (1) the greatness of the inevitability of death (i.e. the ransitioness of the physical body), (2) the inevitability of he old age mentioned to the young by the old (i.e. the transitonness of youth) (3) the bravery to die wounded in battle considering the nature of the wordly life, (4) the state of the wounded being attended to by devils in the absence of lovin-i relatives. (5) the state of being pitied at the fallen state by oters mentioning his previous prosperous condition, (A) the taking of terrible oath by one that he would do this if he fails to do the task undertaken (7) the wife who previously met him with sweet srhile not touching him in the wounded state fearing the devils that surround him, (8) the magnanimity of the wife, killing herself with the spear left by the dying husband 2 (9) the state of people not willing to give their daughters in marriage to enemies who offered their hand in consideration of the dignity of their family and (10) the state of wife dying bringing the head of the deceased husband close to her breasts and face; the second set consisting of the (1) the confusion with lamentations of mothers surrounding the dead bodies of their famous sons or the confusion with lamentations of people at the death of mothers round the dead bodies of their famous sons 3 (2) the grievous pain experienced by themselves (i.e. by wives either in prison or in the absence of relatives). (3) the extreme delight experienced by the goers- by on seeing the wife's death along with her husband, (4) the wife's bewailing the loss of the husband in the middle of the forest, (5) the helpless state of the dependents and others at the death of their masters, (6) the pitiable state of the husband at the loss of the wife, (7) the pitiable widowed life of the wife at the loss of the husband, ( 8 ) the words expressed by the wife to those who stood in the way of her entering the funeral pyre of her husband (9) the state of the mother readv to die at the glorious death of her son in the battlefield or the state of the mother ready to die on behalf of honour at the behaviour of her son, and (10) the eulogy of the cremation ground which stands firm though witnessing many disappearing from this wide world."   
          }
          },
          {
            "paadal": "பாடாண் பகுதி கைக்கிளைப் புறனே \nநாடும் காலை நால் இரண்டு உடைத்தே.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்) Theme",
              "paadal_meaning": "Pāṭāṇṭiṇai (பாடாண்திணை) is the puṟaṇ (புறன்) of kaikkiḷai (கைக்கிளை) and is, on examination, of eight kinds."         
          }
          },
          {
            "paadal": "அமரர்கண் முடியும் அறு வகையானும் \nபுரை தீர் காமம் புல்லிய வகையினும் \nஒன்றன் பகுதி ஒன்றும் என்ப.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "In the six kinds of verses with reference to devas and verses with reference to righteous pleasures, one will overlap with another."  
          }
          },    
          {
            "paadal": "வழக்கு இயல் மருங்கின் வகைபட நிலைஇ \nபரவலும் புகழ்ச்சியும் கருதிய பாங்கினும் \nமுன்னோர் கூறிய குறிப்பினும் செந்துறை \nவண்ணப் பகுதி வரைவு இன்று ஆங்கே.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "TThe rhythm of the melody type centuṟai (செந்துறை) is not to be avoided in the paraval (பரவல்) (eulogy in person paḻiccū (பல்லாங்குழி) (eulogy in absence)) and the places suggested by the predecessors wherever they are found in usage."      
          }
          },
          {
            "paadal": "காமப் பகுதி கடவுளும் வரையார் \nஏனோர் பாங்கினும் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "Learned men say that, in erotic verses and in verses which should be concerned with human beings, gods are not prohibited."       
          }
          },
          {
            "paadal": "குழவி மருங்கினும் கிழவது ஆகும்.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "Erotic verses may be with reference to children."
            }
          },
          {
            "paadal": "ஊரொடு தோற்றமும் உரித்து என மொழிப \nவழக்கொடு சிவணிய வகைமையான.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "Erotic verse in pāṭāṇ (பாடாண்) may be with reference to the inhabitants of villages if it is in conformity with usage."          }
          },
          {
            "paadal": "மெய்ப் பெயர் மருங்கின் வைத்தனர் வழியே.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "Predecessors have said that the true names of heroes may be mentioned in erotic verses with reference to pāṭān (பாடாண்)." }
          },
          {
            "paadal": "கொடிநிலை கந்தழி வள்ளி என்ற \nவடு நீங்கு சிறப்பின் முதலன மூன்றும் \nகடவுள் வாழ்த்தொடு கண்ணிய வருமே.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "The three which are considered spotless-sun, Brahma (பிரம்மா) and Moon may be invoked."
            }
          },
          {
            "paadal": "கொற்றவள்ளை ஓர் இடத்தான.",
            "vilakkam": {
              "paadal_category": "Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "Koṟṟavaḷḷai (கொற்றவள்) too may be taken under pāṭāṇ (பாடாண்) is some places."
            }
          },
          {
            "paadal": "கொடுப்போர் ஏத்திக் கொடாஅர்ப் பழித்தலும் \nஅடுத்து ஊர்ந்து ஏத்திய இயன்மொழி வாழ்த்தும் \nசேய் வரல் வருத்தம் வீட வாயில் \nகாவலர்க்கு உரைத்த கடைநிலையானும் \nகண்படை கண்ணிய கண்படை நிலையும் \nகபிலை கண்ணிய வேள்வி நிலையும் \nவேலை நோக்கிய விளக்கு நிலையும் \nவாயுறை வாழ்த்தும் செவியறிவுறூஉவும் \nஆவயின் வரூஉம் புறநிலை வாழ்த்தும் \nகைக்கிளை வகையொடு உளப்படத் தொகைஇ \nதொக்க நான்கும் உள என மொழிப.",
           
            "vilakkam": {
              "paadal_category": "Substrands of the Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "They say that the tuṟais (துறை) of pāṭāṇ (பாடாண்) are (1) eulogising the giver and reviling the non-giver (2) eulogising a king in his close proximity with reference to the nature of his ancestors and himself (3) the scene where words are sent to the king through the gatekeeper enumerating the miseries undergone in the long journey from home (4) suggesting to the king that it is time to go to sleep, (5) the sacrifice where brown cows are freely given away (6) lighting the lamp to commemmorate the victory of the spear or the height of the flame of the lamp like fhat of the spear (7) salutary advice to a king by wise men nolen volens (?) (8) instructing the king in the path of virtue (9) benediction upon a king, invoking his deity to bless him and his descendants and ( 10) interceding etc., during kaikkilai(கைக்கிளை)."      }
          },
          {
            "paadal": "தாவின் நல் இசை கருதிய கிடந்தோர்க்குச் \nசூதர் ஏத்திய துயிலெடை நிலையும் \nகூத்தரும் பாணரும் பொருநரும் விறலியும் \nஆற்றிடைக் காட்சி உறழத் தோன்றி \nபெற்ற பெரு வளம் பெறாஅர்க்கு அறிவுறீஇ \nசென்று பயன் எதிரச் சொன்ன பக்கமும் \nசிறந்த நாளினில் செற்றம் நீக்கி \nபிறந்த நாள்வயின் பெருமங்கலமும் \nசிறந்த சீர்த்தி மண்ணுமங்கலமும் \nநடை மிகுத்து ஏத்திய குடை நிழல் மரபும் \nமாணார்ச் சுட்டிய வாள்மங்கலமும் \nமன் எயில் அழித்த மண்ணுமங்கலமும் \nபரிசில் கடைஇய கடைக்கூட்டு நிலையும் \nபெற்ற பின்னரும் பெரு வளன் ஏத்தி \nநடைவயின் தோன்றிய இரு வகை விடையும் \nஅச்சமும் உவகையும் எச்சம் இன்றி \nநாளும் புள்ளும் பிறவற்றின் நிமித்தமும் \nகாலம் கண்ணிய ஓம்படை உளப்பட \nஞாலத்து வரூஉம் நடக்கையது குறிப்பின் \nகாலம் மூன்றொடு கண்ணிய வருமே.",
            "vilakkam": {
              "paadal_category": "The Ramifications of the Pāṭāṇ (பாடாண்)  Theme",
              "paadal_meaning": "The following connected with the past, present and the future in this earth are also taken as the tuṟais(துறை) of pāṭāṇ (பாடாண்) :— (1) bards singing about the king's spotless good fame to wake him, while asleep, up ; (2) kuttar (கூத்தர்) , pānar (பாணர்),  porunar (பொருநர்) and viṟaliyar(விறலியர்) who have received presents directing those who have not received them and telling them what they have received (3) celebrations on birth days by nullifying the punishments (4) purificatory bath bringing fame; (5) bringing out the excellence of royal umbrella giving shade to many; (6) giving adorations to the spear which brought the foes under control; (7) purifactory bath of the king after capturing the enemy's fort; (8 ) the poets etc mentioning their wants and getting the rewards 3 (9) eulogising the prosperous condition of the king after receiving the reward and taken leave of the taking either on his own initiative or on the initiative of the king; and (10) wishing that the king may be free from the source of fear, delight and want which is foreboded by the stars, birds and other omens."      }
          }
        ]
      },
      {
        "iyal_name": "களவியல்",
        "iyal_eng":"Clandestine Love Career",
        "noorpa": [
          {
            "paadal": "இன்பமும் பொருளும் அறனும் என்றாங்கு \nஅன்பொடு புணர்ந்த ஐந்திணை மருங்கின் \nகாமக் கூட்டம் காணும் காலை \nமறையோர் தேஎத்து மன்றல் எட்டனுள் \nதுறை அமை நல் யாழ்த் துணைமையோர் இயல்பே.",
            "vilakkam": 
            {
            "paadal_category": "The Dynamics of the Clandestine Love Career",
            "paadal_meaning": "Kaḷavu (களவு) or kāmakkūṭṭam (காமக்கூட்டம்) which falls within the range of the five tiṇais (திணை) connected with reciprocal love and which is the source of pleasure, worldly objects and dharma (தர்மம்) is, on examination, of the type of the gāndharva (கந்தர்வ) marriage among the eight kinds of marriage mentioned in the Vēdas(வேதம்)."
          }
          },
          {
            "paadal": "ஒன்றே வேறே என்று இரு பால்வயின் \nஒன்றி உயர்ந்த பாலது ஆணையின் \nஒத்த கிழவனும் கிழத்தியும் காண்ப \nமிக்கோன் ஆயினும் கடி வரை இன்றே.",
            "vilakkam": 
            {
            "paadal_category": "Coming together in Love of a Man and Woman",
            "paadal_meaning": "Suitable lover and lady-love belonging to the same region or of different regions come within the view of each other through the direction of the Fate which gradually raises them by making them husband and wife in every birth. It does not matter much even if the lover is of superior order to the lady-love."
           }
          },
          {
            "paadal": "சிறந்துழி ஐயம் சிறந்தது என்ப \nஇழிந்துழி இழிபே சுட்டலான.",
            "vilakkam": 
            {
              "paadal_category": "Coming together in Love of a Man and Woman",
              "paadal_meaning": "Doubt about their respective nature is praiseworthy only when both are of superior birth, since the low nature is evident if they are of low pedigree."
            }
          },
          {
            "paadal": "வண்டே இழையே வள்ளி பூவே \nகண்ணே அலமரல் இமைப்பே அச்சம் என்று \nஅன்னவை பிறவும் ஆங்கண் நிகழ \nநின்றவை களையும் கருவி என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Coming together in Love of a Man and Woman",
              "paadal_meaning": "Bee (on the flowers on head), ornaments (worn on the body), creeper-like lines (drawn on breast and shoulders), flowers, physical eyes, bewilderment, winking of the eyes, sense of fear, etc., found on and near her, serve as the instruments to clear the doubt (in the mind of the lover)."
            }
          },
          {
            "paadal": "நாட்டம் இரண்டும் அறிவு உடம்படுத்தற்குக் \nகூட்டி உரைக்கும் குறிப்புரை ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "The Role of Eyes",
              "paadal_meaning": "The meeting of the eyes of the two is the evidence to determine that they are mutually attached."
            }
          },
          {
            "paadal": "குறிப்பே குறித்தது கொள்ளும் ஆயின் \nஆங்கு அவை நிகழும் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "The Role of Eyes",
              "paadal_meaning": "Learned men say that eyes will meet there only when her mind is prepared to agree to his wish."
            }
          },
          {
            "paadal": "பெருமையும் உரனும் ஆடூஉ மேன.",
            "vilakkam": 
            {
              "paadal_category": "The Male Traits",
              "paadal_meaning": "Consideration of one's own dignity and mental strength are found in man."
            }
          },
          {
            "paadal": "அச்சமும் நாணும் மடனும் முந்துறுதல் \nநிச்சமும் பெண்பாற்கு உரிய என்ப.",
            "vilakkam": 
            {
              "paadal_category": "The Female Traits",
              "paadal_meaning": "They say that fear, modesty and credulity are the permanent traits of woman which exhibit themselves."
            }
          },
          {
            "paadal": "வேட்கை ஒருதலை உள்ளுதல் மெலிதல் \nஆக்கம் செப்பல் நாணு வரை இறத்தல் \nநோக்குவ எல்லாம் அவையே போறல் \nமறத்தல் மயக்கம் சாக்காடு என்று இச் \nசிறப்புடை மரபினவை களவு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Mindscape of the Man and Woman in Love",
              "paadal_meaning": "They say that the following nine important avasthās () (To remain) happen at the time of kaḷavu (களவு): (1) Amorousness, (2) uninter-rupted thinking of the object of love, ( 3 ) emaciation, ( 4 ) enumeration of what is experienced like sleeplessness, etc., ( 5 ) transgressing the bonds of modesty, ( 6 ) looking at all objects of nature with reference to the limbs of the object of love, ( 7 ) forgetfulness, ( 8 ) stupor and ( 9 ) the dying state."
            }
          },
          {
            "paadal": "முன்னிலை ஆக்கல் சொல்வழிப்படுத்தல் \nநல் நயம் உரைத்தல் நகை நனி உறாஅ \nஅந் நிலை அறிதல் மெலிவு விளக்குறுத்தல் \nதன் நிலை உரைத்தல் தெளிவு அகப்படுத்தல் என்று \nஇன்னவை நிகழும் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Contexts of Hero's Utterance in the Course of the Destined Union",
             "paadal_meaning": "Learned men say that these will then happen :( 1 ) lover addressing the lady-love, ( 2 ) making her listen to him, (3) describing her attractive features, (4) understanding her mind through her smile, (5) making her understand clearly his suffering, ( 6 ) telling her plainly his own condition and (7) convincing himself of her determination."
            }
          },
          {
            "paadal": "மெய் தொட்டுப் பயிறல் பொய் பாராட்டல் \nஇடம் பெற்றுத் தழாஅல் இடையூறு கிளத்தல் \nநீடு நினைந்து இரங்கல் கூடுதல் உறுதல் \nசொல்லிய நுகர்ச்சி வல்லே பெற்றுழித் \nதீராத் தேற்றம் உளப்படத் தொகைஇ \nபேராச் சிறப்பின் இரு நான்கு கிளவியும் \nபெற்றவழி மகிழ்ச்சியும் பிரிந்தவழிக் கலங்கலும் \nநிற்பவை நினைஇ நிகழ்பவை உரைப்பினும் \nகுற்றம் காட்டிய வாயில் பெட்பினும் \nபெட்ட வாயில் பெற்று இரவு வலியுறுப்பினும் \nஊரும் பேரும் கெடுதியும் பிறவும் \nநீரின் குறிப்பின் நிரம்பக் கூறித் \nதோழியைக் குறையுறும் பகுதியும் தோழி \nகுறை அவட் சார்த்தி மெய்யுறக் கூறலும் \nதண்டாது இரப்பினும் மற்றைய வழியும் \nசொல் அவட் சார்த்தலின் புல்லிய வகையினும் \nஅறிந்தோள் அயர்ப்பின் அவ் வழி மருங்கின் \nகேடும் பீடும் கூறலும் தோழி \nநீக்கலின் ஆகிய நிலைமையும் நோக்கி \nமடல் மா கூறும் இடனுமார் உண்டே. ",
            "vilakkam": 
            {
              "paadal_category": "The Context of the Hero's Utterance in the Clandestine Career",
              "paadal_meaning": "Along with the following eight of great importance—the lover's trying to touch any limb of the lady love, pleading false excuses for the same, getting near her, enumerating the obstacles he had to encounter, feeling sorry for the long delay, meeting her in conjugal union, experiencing the pleasure all on a sudden and expressing the insatiety of his lust-expressing pleasure at the meeting, expressing sorrow at separation, thinking of what is past and what is to come in her company, making his friend who found fault with his love-adventure agree to help him, the friend entreating the lady-love or her friend to agree to the lover's wishes, entreating the lady-love's friend to intercede suggesting to her the name of his native place, his name, and the perils which may follow, telling her his determination to mount himself on a horse of palmyra stems when the lady's friend, in spite of his repeated entreaties, refuses to bring about the union by telling him the exact troubles in which the lady was under, the way in which he met her for the first time without anybody's knowledge, the lady's heaving sighs, the difficulties which she would have to encounter, and (the chance for losing) his personal dignity."
            }
          },
          {
            "paadal": "பண்பின் பெயர்ப்பினும் பரிவுற்று மெலியினும் \nஅன்புற்று நகினும் அவட் பெற்று மலியினும் \nஆற்றிடை உறுதலும் அவ் வினைக்கு இயல்பே.",
            "vilakkam": 
            {
              "paadal_category": "The Context of the Hero's Utterance in the Clandestine Career",
              "paadal_meaning": "The following also come within the range of the lover's sayings:—When he is sent away smoothly, when the lady's friend is at the point of yielding to him on account of compassion, when she or the lady smiles out of affection, when he is pleased in having got the lady's company and when he is beset with obstacles either on his return-journey or on his taking the lady-love with him (without the knowledge of her parents)."
            }   
          },
          {
            "paadal": "பாங்கன் நிமித்தம் பன்னிரண்டு என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Union through the Hero's Confidant",
              "paadal_meaning": "There are twelve occasions in which the lover's friend intercedes."
            }
          },
          {
            "paadal": "முன்னைய மூன்றும் கைக்கிளைக் குறிப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Union through the Hero's Confidant",
              "paadal_meaning": "The occasions during the last three (among the eight kinds of marriages) come under kai-k-kiḷai(கைக்கிளை)."
            }
          },
          {
            "paadal": "பின்னர் நான்கும் பெருந்திணை பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Union through the Hero's Confidant",
              "paadal_meaning": "The occasions during the first four (among them) fall under peruntiṇai (பெருந்திணை)."
            }
          },
          {
            "paadal": "முதலொடு புணர்ந்த யாழோர் மேன \nதவல் அருஞ் சிறப்பின் ஐந் நிலம் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Union through the Hero's Confidant",
              "paadal_meaning": "The occasions during kaḷavu (களவு) which is the type of gāndharva (கந்தர்வ) which is said to be of the best type arise in the five regions of spotless importance."
            }
          },
          {
            "paadal": "இரு வகைக் குறி பிழைப்பு ஆகிய இடத்தும் \nகாணா வகையின் பொழுது நனி இகப்பினும் \nதான் அகம் புகாஅன் பெயர்தல் இன்மையின் \nகாட்சி ஆசையின் களம் புக்குக் கலங்கி \nவேட்கையின் மயங்கிக் கையறு பொழுதினும் \nபுகாக் காலைப் புக்கு எதிர்ப்பட்டுழி \nபகாஅ விருந்தின் பகுதிக்கண்ணும் \nவேளாண் எதிரும் விருப்பின்கண்ணும் \nதாளாண் எதிரும் பிரிவினானும் \nநாணு நெஞ்சு அலைப்ப விடுத்தற்கண்ணும் \nவரைதல் வேண்டித் தோழி செப்பிய \nபுரை தீர் கிளவி புல்லிய எதிரும் \nவரைவு உடன்படுதலும் ஆங்கு அதன் புறத்துப் \nபுரை பட வந்த மறுத்தலொடு தொகைஇ \nகிழவோள் மேன என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Contexts of Hero's Utterance",
              "paadal_meaning": "Learned men say that the following are the occasions when the lover speaks: When he fails to meet the be loved at the assigned place both day and night, when he feels the time heavy in her absence, when he stands helpless befooled by his disappointment on going to the assigned place eager of seeing her and not prepared to return home without going there, when he is treated as a guest when he is met though in an inopportune moment, when the lady expects presents from him, when he perseveres to meet her during separation, when he leaves her on seeing her worried through her modesty, when he is addressed by the lady's friend with surest words to prepare for the marriage, when he agrees to propose for the marriage and when his proposal for the marriage is not agreed to."
            }
          },
          {
            "paadal": "காமத் திணையின் கண் நின்று வரூஉம் \nநாணும் மடனும் பெண்மைய ஆகலின் \nகுறிப்பினும் இடத்தினும் அல்லது வேட்கை \nநெறிப்பட வாரா அவள்வயினான.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Heroine's Utterance",
              "paadal_meaning": "Since shyness and credulity are in the nature of women, the amorous desire in women under kaḷavu (களவு) is not clearly expressed, but is to be understood from suggestion and position."
            }
          },
          {
            "paadal": "காமம் சொல்லா நாட்டம் இன்மையின் \nஏமுற இரண்டும் உள என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Heroine's Utterance",
              "paadal_meaning": "Since eyes do not but suggest her amorous desire, both of them, they say, do exist to delight (the lover)."
            }
          },
          {
            "paadal": "சொல் எதிர் மொழிதல் அருமைத்து ஆகலின் \nஅல்ல கூற்றுமொழி அவள்வயினான.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Heroine's Utterance",
              "paadal_meaning": "Since it is rare that lady-love expresses her amorous desire, we see only her apparent refusal."
            }
          },
          {
            "paadal": "மறைந்து அவற் காண்டல் தற் காட்டுறுதல் \nநிறைந்த காதலின் சொல் எதிர் மழுங்கல் \nவழிபாடு மறுத்தல் மறுத்து எதிர்கோடல் \nபழி தீர் முறுவல் சிறிதே தோற்றல் \nகைப்பட்டுக் கலங்கினும் நாணு மிக வரினும் \nஇட்டுப் பிரிவு இரங்கினும் அருமை செய்து அயர்ப்பினும் \nவந்தவழி எள்ளினும் விட்டு உயிர்த்து அழுங்கினும் \nநொந்து தெளிவு ஒழிப்பினும் அச்சம் நீடினும் \nபிரிந்தவழிக் கலங்கினும் பெற்றவழி மலியினும் \nவரும் தொழிற்கு அருமை வாயில் கூறினும் \nகூறிய வா`யில் கொள்ளாக் காலையும் \nமனைப் பட்டுக் கலங்கிச் சிதைந்தவழித் தோழிக்கு \nநினைத்தல் சான்ற அரு மறை உயிர்த்தலும் \nஉயிராக் காலத்து உயிர்த்தலும் உயிர் செல \nவேற்று வரைவு வரின் அது மாற்றுதற்கண்ணும் \nநெறி படு நாட்டத்து நிகழ்ந்தவை மறைப்பினும் \nபொறியின் யாத்த புணர்ச்சி நோக்கி \nஒருமைக் கேண்மையின் உறு குறை தெளிந்தோள் \nஅருமை சான்ற நால் இரண்டு வகையின் \nபெருமை சான்ற இயல்பின்கண்ணும் \nபொய் தலை அடுத்த மடலின்கண்ணும் \nகையறு தோழி கண்ணீர் துடைப்பினும் \nவெறியாட்டு இடத்து வெருவின்கண்ணும் \nகுறியின் ஒப்புமை மருடற்கண்ணும் \nவரைவு தலைவரினும் களவு அறிவுறினும் \nதமர் தற் காத்த காரண மருங்கினும் \nதன் குறி தள்ளிய தெருளாக் காலை \nவந்தவன் பெயர்ந்த வறுங் களம் நோக்கித் \nதன் பிழைப்பாகத் தழீஇத் தேறலும் \nவழு இன்று நிலைஇய இயற்படு பொருளினும் \nபொழுதும் ஆறும் புரைவது அன்மையின் \nஅழிவு தலைவந்த சிந்தைக்கண்ணும் \nகாமம் சிறப்பினும் அவன் அளி சிறப்பினும் \nஏமம் சான்ற உவகைக்கண்ணும் \nதன்வயின் உரிமையும் அவன்வயின் பரத்தையும் \nஅன்னவும் உளவே ஓர் இடத்தான.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Utterance",
             "paadal_meaning": "The lady-love has her sayings on the following occasions totally or partially. When she sees liitn without his seeing her 1 when she stands in such a position as to be seen by him, when she stands still before the lover through excessive love without telling him anything, 2 when she (apparently) refuses to yield to him, when she yields to him after refusal, when she lightly exhibits harmless smile, when she is in bewilderment though in the company of her lover, when she is unnerved through extreme shyness, when she fears separation though at a short distance, when she feds sorry on being prevented fre m going out or on his failing to meet her on account of strict watch, when she derides him on his standing before her, when she explicitly tells him her sufferings bemoaning, when she docs not listen to his promise on account of her suffering, when the obstacles bringing her fear prolonged when she is in bewilder - merit on his separation from her, when she is in ecstasy on meeting him, when her friend tells her of the improbability of his coming on account of obstacles, when she does not take it into her head, when she reveals her situation to her friend on being chained to her house and consequently being put to much worry, when she says that she will die if he does not come to her rescue: when she consoles herself that she was responsible for his non-comingon her non-trying to make her parents change their minds if they arranged for the marriage with another, on her concealing her mind from others, on her being in eight amorous states with magnanimity consoling herself about the separation from her lover through her love for him for which fate is responsible, on hearing the rumour of his n ounting himself on palmyra stalks, on her friend removing her tears, on the priest expressing his views of her being possessed of Skanda, on her bewilderment about her mistaking the assigned place, on approach of the lover's request for marriage on kalavu being on the point of becoming public property, on her relatives keeping her under check, on his going back with disappointment without knowing that she is under check and consequently is unable to meet him at the assigned place; and when she tries to misinterpret his true words, the inconvenient time and place of his arrival, his extreme attachment towards her, his attempt to please her and his exhibiting his extreme delight due io his attachment towards her, by referring to her unsullied state towards him and to his connection with a harlot (which is imaginary)."
            }
          },
          {
            "paadal": "வரைவு இடை வைத்த காலத்து வருந்தினும் \nவரையா நாளிடை வந்தோன் முட்டினும் \nஉரை எனத் தோழிக்கு உரைத்தற்கண்ணும் \nதானே கூறும் காலமும் உளவே.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Utterance",
              "paadal_meaning": "There may be opportunities for the lady-love to volunteer her saying when she suffers before the lover goes to her to marry, when he meets (her friend etc.,) before her marriage and when she requests her friend to relate the real situation (to her parents, lover etc.)."
            }
          },
          {
            "paadal": "உயிரினும் சிறந்தன்று நாணே நாணினும் \nசெயிர் தீர் காட்சிக் கற்புச் சிறந்தன்று எனத் \nதொல்லோர் கிளவி புல்லிய நெஞ்சமொடு \nகாமக் கிழவன் உள்வழிப் படினும் \nதா இல் நல் மொழி கிழவி கிளப்பினும் \nஆ வகை பிறவும் தோன்றுமன் பொருளே.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Utterance",
              "paadal_meaning": "Even if the lady-love goes (of her own accord) to the residence of her lover or says such words free from guilt on the strength of the saying of the ancients that shyness is superior even to life and chastity is superior even to shyness, such things come under aka-p-poruḷ (ஆக்கப்பொருள்)."
            }
          },
          {
            "paadal": "நாற்றமும் தோற்றமும் ஒழுக்கமும் உண்டியும் \nசெய் வினை மறைப்பினும் செலவினும் பயில்வினும் \nபுணர்ச்சி எதிர்ப்பாடு உள்ளுறுத்து வரூஉம் \nஉணர்ச்சி ஏழினும் உணர்ந்த பின்றை \nமெய்யினும் பொய்யினும் வழிநிலை பிழையாது \nபல் வேறு கவர் பொருள் நாட்டத்தானும் \nகுறையுறற்கு எதிரிய கிழவனை மறையுறப் \nபெருமையின் பெயர்ப்பினும் உலகு உரைத்து ஒழிப்பினும் \nஅருமையின் அகற்சியும் அவள் அறிவுறுத்துப் \nபின் வா என்றலும் பேதைமை ஊட்டலும் \nமுன் உறு புணர்ச்சி முறை நிறுத்து உரைத்தலும் \nஅஞ்சி அச்சுறுத்தலும் உரைத்துழிக் கூட்டமொடு \nஎஞ்சாது கிளந்த இரு நான்கு கிளவியும் \nவந்த கிழவனை மாயம் செப்பிப் \nபொறுத்த காரணம் குறித்த காலையும் \nபுணர்ந்த பின் அவன்வயின் வணங்கற்கண்ணும் \nகுறைந்து அவட் படரினும் மறைந்தவள் அருக\nதன்னொடும் அவளொடும் முதல் மூன்று அளைஇ \nபின்னிலை நிகழும் பல் வேறு மருங்கினும் \nநல் நயம் பெற்றுழி நயம் புரி இடத்தினும் \nஎண்ண அரும் பல் நகை கண்ணிய வகையினும் \nபுணர்ச்சி வேண்டினும் வேண்டாப் பிரிவினும் \nவேளாண் பெரு நெறி வேண்டிய இடத்தினும் \nபுணர்ந்துழி உணர்ந்த அறி மடச் சிறப்பினும் \nஓம்படைக் கிளவிப் பாங்கின்கண்ணும் \nசெங் கடு மொழியான் சிதைவுடைத்து ஆயினும் \nஎன்பு நெகப் பிரிந்தோள் வழிச் சென்று கடைஇ \nஅன்பு தலையடுத்த வன்புறைக்கண்ணும் \nஆற்றது தீமை அறிவுறு கலக்கமும் \nகாப்பின் கடுமை கையற வரினும் \nகளனும் பொழுதும் வரை நிலை விலக்கி \nகாதல் மிகுதி உளப்படப் பிறவும் \nநாடும் ஊரும் இல்லும் குடியும் \nபிறப்பும் சிறப்பும் இறப்ப நோக்கி \nஅவன்வயின் தோன்றிய கிளவியொடு தொகைஇ \nஅனை நிலை வகையான் வரைதல் வேண்டினும் \nஐயச் செய்கை தாய்க்கு எதிர் மறுத்து \nபொய் என மாற்றி மெய்வழிக் கொடுப்பினும் \nஅவன் விலங்குறினும் களம் பெறக் காட்டினும் \nபிறன் வரைவு ஆயினும் அவன் வரைவு மறுப்பினும் \nமுன்னிலை அறன் எனப்படுதல் என்று இரு வகைப் \nபுரை தீர் கிளவி தாயிடைப் புகுப்பினும் \nவரைவு உடன்பட்டோ ற் கடாவல் வேண்டினும் \nஆங்கு அதன் தன்மையின் வன்புறை உளப்பட \nபாங்குற வந்த நால் எட்டு வகையும் \nதாங்க அருஞ் சிறப்பின் தோழி மேன. ",
            "vilakkam": 
            {
              "paadal_category": "Contexts of Confidante's Utterance",
              "paadal_meaning": "The lady-love's friend has her fine sayings on the following thirty-two occasions after she decides that the lady-love had conjugal union with the lover through the seven things scent, appearance, behaviour, food, forgetting what she should do, walk and action:—(1) When she, without exceeding the limits of her position, probes into the lady's heart through ambiguous expressions both true and false, (2) when she, pretending ignorance, evades the lover through her expressions of the lady's greatness on his approaching her to state his grievances, (3) when she dismisses him advising him to abide by the ways of the world ( i.e . to request the lady's father for her hand), (4) when she makes him return on saying that it is not easy to see the lady, (5) when she asks him go to her after informing the lady of his arrival, (6) when she convinces him of the lady's credulousness, when she asks him to arrange for meeting her in the same away as he arranged for the previous meeting, (7) when she informs him of her fear (that she would be taken to task by her relatives), (8) when they meet on her information (.about the time, place, manner etc., of their meeting), (9) when she, pretending ignorance of the lover's arrival, makes him understand how the lady bore patiently his absence or when she noted the patience of the lady, on his coming with false excuses, (10) when she makes obeisance to him after their meeting, (11) when she approaches the lady with her misgivings, (12) when she addresses the lady in diverse ways when she stands hidden from the view of the lover making the intention of both the lady and herself understood through suggestion 1 (13) when she informs the lover of the lady's gratifying words (14) when she informs the lover of his becoming the laughing stock in diverse ways (15) when the lover wants union with the lady, (16) when he wants to go away, (17) when she expects help from the lover, (18)' when she gracefully loses her discrimination when they are together and tells the lover to look after the lady, (19) when she affirms the love of the lover by approaching the lady who is skin and bone on being disheartened by the displeasing words of the lover 2 (20-25) when she requests the lover to propose for the marriage, considering their anxiety due to the unsafety of the way, the strict watch, the failure to meet at the proper place and time, growth of the love etc., and with reference to the greatness of his country, village, habitation, family, heredity, nobility and influence, (26) when she removes the doubt from ihe mind of the lady's mother and make her confide in her words, (27-30) when she addresses the foster mother that the meeting of the lover and the ladylove is in accordance with Dharma(தர்மம்) while the lady is kept under restraint 3 4 , while the mother seeks the help of the diviner and the priest in possession of Skanda, while the parents propose to give the lady in marriage to another and while they do not accede to the proposal of the lover, (31) when she informs the lover of the consent of the lady's parents (for the marriage) and (32) when she asserts the same to the lady."
            }
          },
          {
            "paadal": "களவு அலர் ஆயினும் காமம் மெய்ப்படுப்பினும் \nஅளவு மிகத் தோன்றினும் தலைப்பெய்து காணினும் \nகட்டினும் கழங்கினும் வெறி என இருவரும் \nஒட்டிய திறத்தான் செய்திக்கண்ணும் \nஆடிய சென்றுழி அழிவு தலைவரினும் \nகாதல் கைம்மிகக் கனவின் அரற்றலும் \nதோழியை வினவலும் தெய்வம் வாழ்த்தலும் \nபோக்கு உடன் அறிந்த பின் தோழியொடு கெழீஇக் \nகற்பின் ஆக்கத்து நிற்றற்கண்ணும் \nபிரிவின் எச்சத்தும் மகள் நெஞ்சு வலிப்பினும் \nஇரு பால் குடிப் பொருள் இயல்பின்கண்ணும் \nஇன்ன வகையின் பதின்மூன்று கிளவியொடு \nஅன்னவை பிறவும் செவிலி மேன.",
            "vilakkam": 
            {
              "paadal_category": "Contexts of Utterance by Foster-mother",
              "paadal_meaning": "The foster-mother has her say on the following thirteen occasions and more; when she questions the lady's friend (1) on the kalavu(களவு) becoming the object of common talk, (2) on the lady's love exceeding the bounds 2 (3) on the lady's limbs (like breasts) having a greater growth, (4) on seeing the lover and the lady together, (5-7) on seeing the attitude of the lady when both the mother and foster-mother take recourse to divination with kaṭṭū (கட்டு), kaḻanci (கலங்கி) and veṟi-yāṭū (வெறியாட்டு) (8) on the lady becoming unnerved when there is veṟi-yāṭū (வெறியாட்டு) (9) on the lady prattling in dream on account of the mind being steeped in love, (10) when she prays to God (11) when she, on learning that the lady has gone with the lover, appreciates the sense of chastity of the lady along with her friend (12) when she sees the strength of mind of the lady when she was left alone by the lover* (13) when she compares the heredity of both the lover and the love."
            }
          },
          {
            "paadal": "தாய்க்கும் வரையார் உணர்வு உடம்படினே.",
            "vilakkam": 
            {
              "paadal_category": "Utterance by Heroine's Mother",
              "paadal_meaning": "They permit the sayings noted in the previous sūtra (சூத்திரம்) to the lady's mother also, if she feels in the same way as the foster- mother."
            }
          },
          {
            "paadal": "கிழவோன் அறியா அறிவினள் இவள் என \nமை அறு சிறப்பின் உயர்ந்தோர் பாங்கின் \nஐயக் கிளவியின் அறிதலும் உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Mother and Foster-mother Understanding Heroine's Love",
              "paadal_meaning": "The mother and the foster-mother deserve to understand (the real nature) from the ambiguous saying of the great men with unsullied magnanimity 'kiḻavōṉ aṟiyā aṟiviṉāl ivaḷ' (கிழவோன் அறியா அறிவினள் இவள்) which means this lady completely knows the nature of the lover and this lady does not know the nature of the lover."
            }
          },
          {
            "paadal": "தன் உறு வேட்கை கிழவன் முன் கிளத்தல் \nஎண்ணும் காலை கிழத்திக்கு இல்லை \nபிற நீர் மாக்களின் அறிய ஆயிடைப் \nபெய்ந் நீர் போலும் உணர்விற்று என்ப.",
            "vilakkam": 
            {
              "paadal_category": "The Nature of Heroine's Expression of Love",
              "paadal_meaning": "They say that, on examination, the lady-love does not express openly her love in the presence of the lover like low- class women and it is understood like the water that oozes out of the unburnt pot of mud."
            }
          },
          {
            "paadal": "காமக் கூட்டம் தனிமையின் பொலிதலின \nதாமே தூதுவர் ஆகலும் உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Hero and Heroine as Messengers of Their Love",
              "paadal_meaning": "Since union out of reciprocal love is par excellence, it is possible for both the lover and the love to serve as the carriers of message between themselves."
            }
          },
          {
            "paadal": "அவன் வரம்பு இறத்தல் அறம் தனக்கு இன்மையின் \nகளம் சுட்டுக் கிளவி கிழவியது ஆகும் \nதான் செலற்கு உரிய வழி ஆகலான.",
            "vilakkam": 
            {
              "paadal_category": "Heroine Suggesting the Trysting Spot",
              "paadal_meaning": "Since it is not dharma (தர்மம்) for the lady to go against the wishes of the lover, it is her duty to suggest the place of their meeting since she alone knows where it is possible for her to go."
            }
          },
          {
            "paadal": "தோழியின் முடியும் இடனுமார் உண்டே. ",
            "vilakkam": 
            {
              "paadal_category": "Confidante Prearranging Rendezvous",
              "paadal_meaning": "There are cases where the lady's friend also suggests the place of meeting."
            }
          },
          {
            "paadal": "முந் நாள் அல்லது துணை இன்று கழியாது \nஅந் நாள் அகத்தும் அது வரைவு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Occasions That Do not Need the Confidante's Aid",
              "paadal_meaning": "The meeting does not take place without the friend on any day other than the three days (when the lady is in her periods.) It is not prohibited even on the day following the three days (i.e.), on the fourth day."
            }
          },
          {
            "paadal": "பல் நூறு வகையினும் தன் வயின் வரூஉம் \nநல் நய மருங்கின் நாட்டம் வேண்டலின் \nதுணைச் சுட்டுக் கிளவி கிழவியது ஆகும் \nதுணையோர் கருமம் ஆகலான.",
            "vilakkam": 
            {
              "paadal_category": "Confidante as Facilitator of Heroine's Love",
              "paadal_meaning": "Since it is the duty of the lady to investigate into all the benefits that may accrue to her in diverse ways, she has to address her tuṇai (துணை), since it is their duty to look after her."
            }
          },
          {
            "paadal": "ஆய் பெருஞ் சிறப்பின் அரு மறை கிளத்தலின் \nதாய் எனப்படுவோள் செவிலி ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "The Uniqueness of Foster-mother",
              "paadal_meaning": "Tāy (தாய்),here refers to the foster-mother since she atone is confided with secrets, so that she may investigate into them."
            }
          },
          {
            "paadal": "தோழிதானே செவிலி மகளே.",
            "vilakkam": 
            {
              "paadal_category": "The Confidante vis-à-vis Heroine's Love",
              "paadal_meaning": "The lady's friend is the daughter of the foster-mother."
            }
          },
          {
            "paadal": "சூழ்தலும் உசாத்துணை நிலைமையின் பொலிமே.",
            "vilakkam": 
            {
              "paadal_category": "The Confidante vis-à-vis Heroine's Love",
              "paadal_meaning": "She shines most when she critically views the situation on her being consulted."
            }
          },
          {
            "paadal": "குறையுற உணர்தல் முன் உற உணர்தல் \nஇருவரும் உள்வழி அவன் வரவு உணர்தல் என \nமதியுடம்படுத்தல் ஒரு மூ வகைத்தே. ",
            "vilakkam": 
            {
              "paadal_category": "The Confidante vis-à-vis Heroine's Love",
              "paadal_meaning": "There are three ways in which the lady's friend decides the reciprocal love of the lover and the lady:—they happen when the lover expresses his grievances to her, when she infers from the attitude of the lady and when the lover comes while the lady and herself are in each other's company."
            }
          },
          {
            "paadal": "அன்ன வகையான் உணர்ந்த பின் அல்லது \nபின்னிலை முயற்சி பெறாள் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Confidante vis-à-vis Heroine's Love",
              "paadal_meaning": "They say that she does not try for what should follow, unless she has determined their love in the above ways."
            }
          },
          {
            "paadal": "முயற்சிக் காலத்து அதற்பட நாடி \nபுணர்த்தல் ஆற்றலும் அவள்வயினான.",
            "vilakkam": 
            {
              "paadal_category": "The Confidante vis-à-vis Heroine's Love",
              "paadal_meaning": "It is her responsibility to determine towards the opportunities of theiir union when the lover tries for it and to bring it about ?"
            }
          },
          {
            "paadal": "குறி எனப்படுவது இரவினும் பகலினும் \nஅறியக் கிளந்த ஆற்றது என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Trysting",
              "paadal_meaning": "The tryst or the time and place of the lovers meeting may happen both at night and at day."
            }
          },
          {
            "paadal": "இரவுக் குறியே இல்லகத்துள்ளும் \nமனையோர் கிளவி கேட்கும் வழியதுவே \nமனையகம் புகாஅக் காலையான.",
            "vilakkam": 
            {
              "paadal_category": "Trysting Spot by Night",
              "paadal_meaning": "If, at night, it is not possible for the lovers to meet within the house of lady, the place of their meeting is in a place which is so close to her house as to be at hearing distance."
            }
          },
          {
            "paadal": "பகல் புணர் களனே புறன் என மொழிப \nஅவள் அறிவு உணர வரு வழியான.",
            "vilakkam": 
            {
              "paadal_category": "Trysting Spot by Day",
              "paadal_meaning": "They say that the place of meeting of the lovers at day is outside the fort which is within the knowledge of the lady."
            }
          },
          {
            "paadal": "அல்லகுறிப்படுதலும் அவள்வயின் உரித்தே \nஅவன் குறி மயங்கிய அமைவொடு வரினே.",
            "vilakkam": 
            {
              "paadal_category": "Missed Tryst",
              "paadal_meaning": "She may go to a wrong place if the place suggested by the lover is capable of being understood in two ways."
            }
          },
          {
            "paadal": "ஆங்கு ஆங்கு ஒழுகும் ஒழுக்கமும் உண்டே \nஓங்கிய சிறப்பின் ஒரு சிறையான. ",
            "vilakkam": 
            {
              "paadal_category": "Other Spots of Rendezvous",
              "paadal_meaning": "She, even then, may have the superior type of meeting the lover through her mind, though it is physically one-sided."
            }
          },
          {
            "paadal": "மறைந்த ஒழுக்கத்து ஓரையும் நாளும் \nதுறந்த ஒழுக்கம் கிழவோற்கு இல்லை.",
            "vilakkam": 
            {
              "paadal_category": "The Hero During Trysting",
              "paadal_meaning": "The rules prohibiting particular hours and days to meet the lady do not apply to the lover during kaḷavu (களவு)."
            }
          },
          {
            "paadal": "ஆற்றினது அருமையும் அழிவும் அச்சமும் \nஊறும் உளப்பட அதன் ஓரன்ன.",
            "vilakkam": 
            {
              "paadal_category": "The Hero During Trysting",
              "paadal_meaning": "The difficulty of the path, loss of presence of mind, sense of fear and obstacles are of the same nature, (i.e.) do not stand in the way of the lover."
            }
          },
          {
            "paadal": "தந்தையும் தன்னையும் முன்னத்தின் உணர்ப.",
            "vilakkam": 
            {
              "paadal_category": "Knowledge of Heroine's Love by her Kin",
              "paadal_meaning": "The father and the elder brother of the lady infer (the kaḷavu)(களவு) from her features."
            }
          },
          {
            "paadal": "தாய் அறிவுறுதல் செவிலியொடு ஒக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Knowledge of Heroine's Love by her Kin",
              "paadal_meaning": "The mother of the lady understands it in the same way as the foster-mother."
            }
          },
          {
            "paadal": "அம்பலும் அலரும் களவு வெளிப்படுத்தலின் \nஅங்கு அதன் முதல்வன் கிழவன் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Love Coming into the Public",
              "paadal_meaning": "The lover is chiefly responsible for the kaḷavu (களவு) to become known to others through ampal(அம்பல்) and alar(அலர்)."
            }
          },
          {
            "paadal": "வெளிப்பட வரைதல் படாமை வரைதல் என்று \nஆயிரண்டு என்ப வரைதல் ஆறே.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Wedded Union",
              "paadal_meaning": "There ase two ways of expressing the lover's 'wish to the lady's father, one after their kaḷavu (களவு) became the public property and another before it."
            }
          },
          {
            "paadal": "வெளிப்படைதானே கற்பினொடு ஒப்பினும் \nஞாங்கர்க் கிளந்த மூன்று பொருளாக \nவரையாது பிரிதல் கிழவோற்கு இல்லை.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Wedded Union",
              "paadal_meaning": "The lover is not permitted separation from the lady on account of three causes—study, war and embassy—after kaḷavu (களவு) and before varaivu (வரைவு), even though kaḷavu (களவு) that is publicly known is similar to kaṟpū (கற்பு)."
            }
          }
        ]
      },
      {
        "iyal_name": "கற்பியல்",
        "iyal_eng":"Wedded Course of Love Career",
        "noorpa": [
          {
            "paadal": "கற்பு எனப்படுவது கரணமொடு புணர \nகொளற்கு உரி மரபின் கிழவன் கிழத்தியை \nகொடைக்கு உரி மரபினோர் கொடுப்ப கொள்வதுவே.",
            "vilakkam": {
              "paadal_category": "The Wedded Union",
              "paadal_meaning": "Kaṟpu (கற்பு) is that wherein the deserving bridegroom is made to get the hand of the worthy bride by those who are qualified to give her away with the necessary ceremonies like hōma (ஹோமம்) etc."}
          },
          {
            "paadal": "கொடுப்போர் இன்றியும் கரணம் உண்டே \nபுணர்ந்து உடன் போகிய காலையான.",
            "vilakkam": {
              "paadal_category": "The Wedded Union",
              "paadal_meaning": "There is karaṇam (கரணம்) even when there are no relatives to give the bride away, when she goes away with the lover."
          }
          },
          {
            "paadal": "மேலோர் மூவர்க்கும் புணர்த்த கரணம் \nகீழோர்க்கு ஆகிய காலமும் உண்டே.",
            "vilakkam": {
              "paadal_category": "The Wedded Union",
              "paadal_meaning": "There was a time when the karaṇam (கரணம்) enjoined to the first three castes began to be adopted for the fourth."}
          },
          {
            "paadal": "பொய்யும் வழுவும் தோன்றிய பின்னர் \nஐயர் யாத்தனர் கரணம் என்ப. ",
            "vilakkam": {
              "paadal_category": "The Wedded Union",
              "paadal_meaning": "They say, that karaṇam (கரணம்) was introduced by āryas (ஆரியர்கள்) after the lovers began to prove false and the ladies were considered unworthy."}
          },
          {
            "paadal": "கரணத்தின் அமைந்து முடிந்த காலை \nநெஞ்சு தளை அவிழ்ந்த புணர்ச்சிக்கண்ணும் \nஎஞ்சா மகிழ்ச்சி இறந்து வரு பருவத்தும் \nஅஞ்ச வந்த உரிமைக்கண்ணும் \nநல் நெறிப் படரும் தொல் நலப் பொருளினும் \nபெற்ற தேஎத்துப் பெருமையின் நிலைஇ \nகுற்றம் சான்ற பொருள் எடுத்து உரைப்பினும் \nநாமக் காலத்து உண்டு எனத் தோழி \nஏமுறு கடவுள் ஏத்திய மருங்கினும் \nஅல்லல் தீர ஆர்வமொடு அளைஇ \nசொல்லுறு பொருளின்கண்ணும் சொல் என \nஏனது சுவைப்பினும் நீ கை தொட்டது \nவானோர் அமிழ்தம் புரையுமால் எமக்கு என \nஅடிசிலும் பூவும் தொடுதற்கண்ணும் \nஅந்தணர் திறத்தும் சான்றோர் தேஎத்தும் \nஅந்தம் இல் சிறப்பின் பிறர் பிறர் திறத்தினும் \nஒழுக்கம் காட்டிய குறிப்பினும் ஒழுக்கத்துக் \nகளவினுள் நிகழ்ந்த அருமையைப் புலம்பி \nஅலமரல் உள்ளமொடு அளவிய இடத்தும் \nஅந்தரத்து எழுதிய எழுத்தின் மான \nவந்த குற்றம் வழி கெட ஒழுகலும் \nஅழியல் அஞ்சல் என்று ஆயிரு பொருளினும் \nதான் அவட் பிழைத்த பருவத்தானும் \nநோன்மையும் பெருமையும் மெய் கொள அருளி \nபன்னல் சான்ற வாயிலொடு பொருந்தி \nதன்னின் ஆகிய தகுதிக்கண்ணும் \nபுதல்வற் பயந்த புனிறு தீர் பொழுதின் \nநெய் அணி மயக்கம் புரிந்தோள் நோக்கி \nஐயர் பாங்கினும் அமரர்ச் சுட்டியும் \nசெய் பெருஞ் சிறப்பொடு சேர்தற்கண்ணும் \nபயம் கெழு துணை அணை புல்லி புல்லாது \nஉயங்குவனள் கிடந்த கிழத்தியைக் குறுகி \nஅல்கல் முன்னிய நிறை அழி பொழுதின் \nமெல்லென் சீறடி புல்லிய இரவினும் \nஉறல் அருங்குரைமையின் ஊடல் மிகுத்தோளைப் \nபிற பிற பெண்டிரின் பெயர்த்தற்கண்ணும் \nபிரிவின் எச்சத்துப் புலம்பிய இருவரைப் \nபரிவின் நீக்கிய பகுதிக்கண்ணும் \nநின்று நனி பிரிவின் அஞ்சிய பையுளும் \nசென்று கையிகந்து பெயர்த்து உள்ளிய வழியும் \nகாமத்தின் வலியும் கைவிடின் அச்சமும் \nதான் அவட் பிழைத்த நிலையின்கண்ணும் \nஉடன் சேறல் செய்கையொடு அன்னவை பிறவும் \nமடம் பட வந்த தோழிக்கண்ணும் \nவேற்று நாட்டு அகல்வயின் விழுமத்தானும் \nமீட்டு வரவு ஆய்ந்த வகையின்கண்ணும் \nஅவ் வழிப் பெருகிய சிறப்பின்கண்ணும் \nபேர் இசை ஊர்திப் பாகர் பாங்கினும் \nகாமக் கிழத்தி மனையோள் என்று இவர் \nஏமுறு கிளவி சொல்லிய எதிரும் \nசென்ற தேஎத்து உழப்பு நனி விளக்கி \nஇன்றிச் சென்ற தன்னிலை கிளப்பினும் \nஅருந் தொழில் முடித்த செம்மல் காலை \nவிருந்தொடு நல்லவை வேண்டற்கண்ணும் \nமாலை ஏந்திய பெண்டிரும் மக்களும் \nகேளிர் ஒழுக்கத்துப் புகற்சிக்கண்ணும் \nஏனைய வாயிலோர் எதிரொடு தொகைஇ \nபண் அமை பகுதி முப்பதினொருமூன்றும் \nஎண்ண அருஞ் சிறப்பின் கிழவோன் மேன.",
            "vilakkam": {
              "paadal_category": "Contexts of Hero's Utterance",
              "paadal_meaning": "There are thirtythree important occasions when the husband has opportunities to have his say: (1) when he meets in conjugal union his wife with a free mind after the marriage ceremonies are over, (2) whenever he is in ecstasy over the married life while she creates awe in his mind through her keen sense of duty, (3) when she treads the traditional paths of virtue,. (4) when he reconciles her objectionable deeds during kaḷavu (களவு) with reference to her greatness shown in married life, (5) when the lady's friend pays homage to the Gracious God who helped them when they were in danger, (6) when the lady lets her mind out with enthusiasm since her period of trial is over, (7) when he takes the food and makes the garland saying that, whatever she touches is as sweet to him as nectar and asking her the reason for the same (8) when he suggests his appreciation of her exemplary conduct towards brahmans, the great and other saints, 1 (9) when both of them recount towards each other the anxiety and turmoils to which they were put during 'kaḷavu' (களவு) (10) when they are leading their life in such a way that the faults committed by them during kaḷavu (களவு) may disappear like letters written on air, (11) when he has to give her words of encouragement not to dishearten herself, nor to fear for her wrongs in kaḷavu (களவு) , (12) when he does not keep his promise to her, (13) when he tells her that he was responsible for everything and hence she has to put up with what is past and think of her greatness after discussing the same with her friend, 2 (14) when he celebrates the birth of his son on looking at his wife after the  child is given the ceremonial oilbath with presents to brahmans () and prayers to Gods, (15) when he falls at her tender feet praying for mercy while she lies down embracing the soft pillow without allowing herself to be embraced by him on his approaching her after the degeneration of his character through his contact with another woman 1 (16) when he ends the love-quarrel through the intercession of many ladies while she persisted in not allowing him to approach her, (17) when he ends the grief of his wife and faithful concubine caused by his separation from them 2 (18) when he is in distress standing away from the wife, (19) when he approaches her, feels disappointed and thinks of repeating his request, 3 (20) when they are overpowered with kāma (காம), (21) wl:en he fears the effect of his separation from her if it happens (22) when he fails to keep his promise to her, (23) when she tells him that she will follow him, (24) when the lady's friend addresses him through her credulity, (25) when he feels disheartened on starting to a foreign land, (26) when he thinks of returning home on the way, (27) when he meets with victory, honour etc., in that foreign country, (28) when he describes the same to the charioteer having very fine chariot, (29) when he is addressed by his wife and the faithful concubine at home with reference to the difficulties undergone by them, (30) when he describes his situation in the foreign land mixed with grief on their separation, (31) when he enjoys the company of the guests in the feast in commemoration of his victorious feat, (32) when he is given warm reception in the evening by women, children and friends, and (33) when he is addressed with warm words by others"}
          },
          {
            "paadal": "அவன் அறிவு ஆற்ற அறியும் ஆகலின் \nஏற்றற் கண்ணும் நிறுத்தற்கண்ணும் \nஉரிமை கொடுத்த கிழவோன் பாங்கில் \nபெருமையின் திரியா அன்பின்கண்ணும் \nகிழவனை மகடூஉப் புலம்பு பெரிது ஆகலின் \nஅலமரல் பெருகிய காமத்து மிகுதியும் \nஇன்பமும் இடும்பையும் ஆகிய இடத்தும் \nகயந்தலை தோன்றிய காமர் நெய்யணி \nநயந்த கிழவனை நெஞ்சு புண்ணுறீஇ \nநளியின் நீக்கிய இளி வரு நிலையும் \nபுகன்ற உள்ளமொடு புதுவோர் சாயற்கு \nஅகன்ற கிழவனைப் புலம்பு நனி காட்டி \nஇயன்ற நெஞ்சம் தலைப் பெயர்த்து அருக்கி \nஎதிர் பெய்து மறுத்த ஈரத்து மருங்கினும் \nதங்கிய ஒழுக்கத்துக் கிழவனை வணங்கி \nஎங்கையர்க்கு உரை என இரத்தற்கண்ணும் \nசெல்லாக் காலை செல்க என விடுத்தலும் \nகாமக் கிழத்தி தன் மகத் தழீஇ \nஏமுறு விளையாட்டு இறுதிக்கண்ணும் \nசிறந்த செய்கை அவ் வழித் தோன்றி \nஅறம் புரி உள்ளமொடு தன் வரவு அறியாமை \nபுறம் செய்து பெயர்த்தல் வேண்டு இடத்தானும் \nதந்தையர் ஒப்பர் மக்கள் என்பதனால் \nஅந்தம் இல் சிறப்பின் மகப் பழித்து நெருங்கலும் \nகொடியோர் கொடுமை சுடும் என ஒடியாது \nநல் இசை நயந்தோர் சொல்லொடு தொகைஇ \nபகுதியின் நீங்கிய தகுதிக்கண்ணும் \nகொடுமை ஒழுக்கம் கோடல் வேண்டி \nஅடிமேல் வீழ்ந்த கிழவனை நெருங்கி \nகாதல் எங்கையர் காணின் நன்று என \nமாதர் சான்ற வகையின்கண்ணும் \nதாயர் கண்ணிய நல் அணிப் புதல்வனை \nமாயப் பரத்தை உள்ளிய வழியும் \nதன்வயின் சிறைப்பினும் அவன் வயின் பிரிப்பினும் \nஇன்னாத் தொல் சூள் எடுத்தற்கண்ணும் \nகாமக்கிழத்தியர் நலம் பாராட்டிய \nதீமையின் முடிக்கும் பொருளின்கண்ணும் \nகொடுமை ஒழுக்கத்துத் தோழிக்கு உரியவை \nவடு அறு சிறப்பின் கற்பின் திரியாமை \nகாய்தலும் உவத்தலும் பிரித்தலும் பெட்டலும் \nஆவயின் வரூஉம் பல் வேறு நிலையினும் \nவாயிலின் வரூஉம் வகையொடு தொகைஇ \nகிழவோள் செப்பல் கிழவது என்ப.",
            "vilakkam": {
              "paadal_category": "Contexts of Heroine's Utterance",
              "paadal_meaning": "The wife is entitled to have her say on the following occasions;—(1) when she speaks highly of her husband on account of her intimate knowledge of his scholarship, 1 (2) when she supports (the statement of her friend referring to his qualities), (3) when she is attached to him keeping up her dignity on his giving her certain rights, (4) when she is overpowered with passion during his long separation from her, (5) when she is in mirth and misery, (6) when she insults her husband with wounding words asking him not to approach her when he eagerly offers himself to give the ceremonial bath to the child at birth, (7) when she suggests her willingness, though outwardly refuses to allow him to approach her by exhibiting her keen resentment at his separation while he was in loving company with concubines at the time of her weakness after delivery, (8) when she prostrates before her husband who was in company with concubines and sarcastically requests him to express the words addressed to her in the presence of her younger sisters (concubines), (9) when she asks him to go away on his standing before her, (10) when the faithful concubine embraces her child and feels delighted on completing her play with him; (11) when the husband stands behind his wife without being known to her while she is playing with her child, and wants to rid her of the anger towards him so that he may act up to dharma (தர்மம்) (12) when she goes near the child accusing him that he is like his father as is said in the Vēdas (வேதங்கள்) ; (13) when she gives up the love-quarrel and yields to him at the words of the great men effecting reconciliation without dismissing him saying that she was afflicted at his harsh treatment, 2 (14) when she tells him sarcastically that his prostration would be welcomed if done before her younger sisters (i.e.) concubines after feeling that she had to excuse him for his company with other women (15) when she pretends to revile her child on seeing that he is provided with ornaments by his father's concubines,(16) when she confines her child when her, (17) when she alienates herself from the child when he goes with the father, (18) when she takes a cruel vow, (19) when she reviles the faithful concubine at his showing kindness towards her, (20) when she, telling her friend about her husband's company with concubines such things as fit in with her dignity, feels angry with him, reconciles herself to him, spurns him and meets him in conjugal union and behaves with him in diverse similar ways and (21) when pāṇaṉ (பாணம்) and others intercede."}
          },
          {
            "paadal": "புணர்ந்து உடன் போகிய கிழவோள் மனை இருந்து \nஇடைச் சுரத்து இறைச்சியும் வினையும் சுட்டி \nஅன்புறு தக்க கிளத்தல் தானே \nகிழவோன் செய் வினைக்கு அச்சம் ஆகும்.",
            "vilakkam": {
              "paadal_category": "Contexts of Heroine's Utterance",
              "paadal_meaning": "Reference with sweet words to the suggestive words and actions of the husband in the forest when she accompanied him before their marriage, by the wife at home is a source of check to the husband in giving her promise of anything to her."         }
          },
          {
            "paadal": "தோழி உள்ளுறுத்த வாயில் புகுப்பினும் \nஆவயின் நிகழும் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Contexts of Heroine's Utterance",
              "paadal_meaning": "Learned men say that such sayings may be found before pāṇaṉ (பாணம்) and others who are allowed to go before the wife by her friend."}
          },
          {
            "paadal": "பெறற்கு அரும் பெரும் பொருள் முடிந்த பின் வந்த \nதெறற்கு அரு மரபின் சிறப்பின்கண்ணும் \nஅற்றம் அழிவு உரைப்பினும் அற்றம் இல்லாக் \nகிழவோட் சுட்டிய தெய்வக் கடத்தினும் \nசீருடைப் பெரும் பொருள் வைத்தவழி மறப்பினும் \nஅடங்கா ஒழுக்கத்து அவன்வயின் அழிந்தோளை \nஅடங்கக் காட்டுதற் பொருளின் கண்ணும் \nபிழைத்து வந்து இருந்த கிழவனை நெருங்கி \nஇழைத்து ஆங்கு ஆக்கிக் கொடுத்தற்கண்ணும் \nவணங்கு இயல் மொழியான் வணங்கற்கண்ணும் \nபுறம்படு விளையாட்டுப் புல்லிய புகற்சியும் \nசிறந்த புதல்வனைத் தேராது புலம்பினும் \nமாண் நலம் தா என வகுத்தற்கண்ணும் \nபேணா ஒழுக்கம் நாணிய பொருளினும் \nசூள்வயின் திறத்தால் சோர்வு கண்டு அழியினும் \nபெரியோர் ஒழுக்கம் பெரிது எனக் கிளந்து \nபெறு தகை இல்லாப் பிழைப்பினும் அவ் வழி \nஉறு தகை இல்லாப் புலவியுள் மூழ்கிய \nகிழவோள்பால் நின்று கெடுத்தற்கண்ணும் \nஉணர்ப்புவயின் வாரா ஊடல் உற்றோள்வயின் \nஉணர்த்தல் வேண்டிய கிழவோன்பால் நின்று \nதான் வெகுண்டு ஆக்கிய தகுதிக்கண்ணும் \nஅருமைக் காலத்துப் பெருமை காட்டிய \nஎளிமைக் காலத்து இரக்கத்தானும் \nபாணர் கூத்தர் விறலியர் என்று இவர் \nபேணிச் சொல்லிய குறைவினை எதிரும் \nநீத்த கிழவனை நிகழுமாறு படீஇயர் \nகாத்த தன்மையின் கண் இன்று பெயர்ப்பினும் \nபிரியும் காலை எதிர் நின்று சாற்றிய \nமரபு உடை எதிரும் உளப்பட பிறவும் \nவகை பட வந்த கிளவி எல்லாம் \nதோழிக்கு உரிய என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Contexts of Confidante's Utterance",
              "paadal_meaning": "The wife's friend has her say on the following occasions: (1) When (the husband) speaks appreciative words on careful consideration after their great object (marriage) of rare achievement has been accomplished, (2) when she tells him that jtheir sufferings are over, (3) when she tells him that offerings should be given to gods with reference to the wife who escaped from the slander of the public, (4) when the husband forgets the important duty to his wife (in the midst of festivities), (5) when she convinces the wife who is unnerved at the thought that her husband is of suspicious character, that he is not really so, (6) when she makes the husband and the wife meet ftftcr approaching the former with her request while he stands away from his wife having been in company of concubines, (7) when she bends before him with words of supplication, (8) when the husbard is wrongfully engaged in outside sportive activities, (9) when the husband stands separated from his wife forgetting even his son 1 , (10) when the husband is asked to bring back the beauty, health etc. of his wife for the loss of which he is responsible, (11) when the wife feels ashamed of her husband's company with concubines, (12) when the wife is disheartened at the husband not keeping up his word, (13) when he fails in an undignified manner to meet his wife, though he has said that it is wise to follow the great, 2 '(14) when she ends the love-quarrel by going near the wife who is immersed in grief at the undignified behaviour of the husband, (15) when she shows her temper towards the husband with the idea of ending the love-quarrel when the lady does not agree with his wishes, 3 (16) when he is the object of mercy during kaṟpū (கற்பு), though he was an object of veneration during kaḷavu (களவு), (17) when she opposes pāṇar (பாணர்), kūttar (கூத்தர்) and viṟaliyar (விறலியர்) while they intercede, (18) when she mercilessly prevents the husband from seeking the company of concubines in order that he may lead a happy life whhis wife at least in future though he neglected her company before, (19) when she addresses him in the traditional way on his separation from his beloved (on account of war etc.)"}
          },
          {
            "paadal": "புல்லுதல் மயக்கும் புலவிக்கண்ணும் \nஇல்லோர் செய்வினை இகழ்ச்சிக்கண்ணும் \nபல் வேறு புதல்வர்க் கண்டு நனி உவப்பினும் \nமறையின் வந்த மனையோள் செய்வினை \nபொறை இன்று பெருகிய பருவரற்கண்ணும் \nகாதல் சோர்வின் கடப்பாட்டு ஆண்மையின் \nதாய் போல் தழீஇக் கழறி அம் மனைவியைக் \nகாய்வு இன்று அவன்வயின் பொருத்தற்கண்ணும் \nஇன் நகைப் புதல்வனைத் தழீஇ இழை அணிந்து \nபின்னர் வந்த வாயிற்கண்ணும் \nமனையோள் ஒத்தலின் தன்னோர் அன்னோர் \nமிகை எனக் குறித்த கொள்கைக்கண்ணும் \nஎண்ணிய பண்ணை என்று இவற்றொடு பிறவும் \nகண்ணிய காமக்கிழத்தியர் மேன.",
            "vilakkam": {
              "paadal_category": "Utterance by Concubines",
              "paadal_meaning": "The faithful concubines have the following occasions to have their say: (1) when the lover is away from them when he is in the company of his wife, (2) when they slander the action of their lover and his wife, (3) when they delight in the company of different children holding the relationship of sons, (4) when they are in distress not capable of putting up with his actions with another lady in kaḷavu (களவு), (5) when they arrange for his union with his wife acting the part of the foster-mothers and without bearing any ill-will towards her on account oi the laxity of their passion and good-will towards his wife, (6) when they embrace their son with sweet smile and provide him with ornaments and do not then yield to the wishes of other intercedes, (7) when they consider that, since they are equal to the lover's wives, other ladies are unnecessary, (8) when they sport with the lover etc."}
          },
          {
            "paadal": "கற்பும் காமமும் நற்பால் ஒழுக்கமும் \nமெல் இயல் பொறையும் நிறையும் வல்லிதின் \nவிருந்து புறந்தருதலும் சுற்றம் ஓம்பலும் \nபிறவும் அன்ன கிழவோள் மாண்புகள் \nமுகம் புகல் முறைமையின் கிழவோற்கு உரைத்தல் \nஅகம் புகல் மரபின் வாயில்கட்கு உரிய.",
            "vilakkam": {
              "paadal_category": "Utterance by Interceders",
              "paadal_meaning": "The interceders who can go into the residence of the husband are used to tell him about his wife's chastity, love, good conduct, forbearance, sublimity, giving warm welcome to guests, carefully attending to the wants of his relatives and attendants and other good qualities."}
          },
          {
            "paadal": "கழிவினும் நிகழ்வினும் எதிர்வினும் வழி கொள \nநல்லவை உரைத்தலும் அல்லவை கடிதலும் \nசெவிலிக்கு உரிய ஆகும் என்ப.",
            "vilakkam": {
              "paadal_category": "Utterance by Foster-mother",
              "paadal_meaning": "They say that the foster-mother has the right to advise her what she, in the past, present and future, should do and what she should avoid."
            }
          },
          {
            "paadal": "சொல்லிய கிளவி அறிவர்க்கும் உரிய.",
            "vilakkam": {
              "paadal_category": "Utterance by the Wise",
              "paadal_meaning": "The learned are entitled to advise her the same."
            }
          },
          {
            "paadal": "இடித்து வரை நிறுத்தலும் அவரது ஆகும் \nகிழவனும் கிழத்தியும் அவர் வரை நிற்றலின்.",
            "vilakkam": {
              "paadal_category": "Utterance by the Wise",
              "paadal_meaning": "Since the husband and the wife obey their words, they are entitled to set them right forcibly if they go wrong."
            }
          },
          {
            "paadal": "உணர்ப்பு வரை இறப்பினும் செய் குறி பிழைப்பினும் \nபுலத்தலும் ஊடலும் கிழவோற்கு உரிய.",
            "vilakkam": {
              "paadal_category": "Contexts of Hero's Variance",
              "paadal_meaning": "Husband is entitled to be in love-quarrel short or long when the wife is too obstinate to yield to his sweet persuasion and when he mistakes the time and place of meeting suggested by the lady-love."
            }
          },
          {
            "paadal": "புலத்தலும் ஊடலும் ஆகிய இடத்தும் \nசொலத் தகு கிளவி தோழிக்கு உரிய.",
            "vilakkam": {
              "paadal_category": "Confidante's Intercession",
              "paadal_meaning": "The wife's friend is entitled to have her say when they are in love-quarrel short or long."
            }
          },
          {
            "paadal": "பரத்தைமை மறுத்தல் வேண்டியும் கிழத்தி \nமடத் தகு கிழமை உடைமையானும் \nஅன்பிலை கொடியை என்றலும் உரியள்.",
            "vilakkam": {
              "paadal_category": "Confidante's Intercession",
              "paadal_meaning": "The wife's friend is entitled to tell the husband, you are not attached to your wife, touare hard to her', since she wants to prevent him from having companies with concubines and since the wife is too credulous not to suspect him."
            }
          },
          {
            "paadal": "அவன் குறிப்பு அறிதல் வேண்டியும் கிழவி \nஅகம் மலி ஊடல் அகற்சிக்கண்ணும் \nவேற்றுமைக் கிளவி தோற்றவும் பெறுமே. ",
            "vilakkam": {
              "paadal_category": "Heroine's Sulking",
              "paadal_meaning": "The wife is entitled to use even harsh words when she wants to know the mind of the husband at the words of her friend and when she, being pleased, is to end the love-quarrel."
            }
          },
          {
            "paadal": "காமக் கடப்பினுள் பணிந்த கிளவி \nகாணும் காலை கிழவோற்கு உரித்தே \nவழிபடு கிழமை அவட்கு இயலான. ",
            "vilakkam": {
              "paadal_category": "Solicitude by Hero",
              "paadal_meaning": "The husband then is entitled to use soft words if he is in urgent need of union, since the wife is always devoted to him."
            }
          },
          {
            "paadal": "அருள் முந்துறுத்த அன்பு பொதி கிளவி \nபொருள் பட மொழிதல் கிழவோட்கும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Heroine's Loving Response",
              "paadal_meaning": "The wife has to speak in such a way as to suggest her reconciliation and deep love towards him."
            }
          },
          {
            "paadal": "களவும் கற்பும் அலர் வரைவு இன்றே.",
            "vilakkam": {
              "paadal_category": "Gossip about the Love Career",
              "paadal_meaning": "It is not possible to avoid the public talk about the love- quarrel both during kaḷavu (களவு) and kaṟpū (கற்பு)."
            }
          },
          {
            "paadal": "அலரின் தோன்றும் காமத்து மிகுதி.",
            "vilakkam": {
              "paadal_category": "Gossip about the Love Career",
              "paadal_meaning": "Love towards each other is sharpened through public talk."
            }
          },
          {
            "paadal": "கிழவோன் விளையாட்டு ஆங்கும் அற்றே.",
            "vilakkam": {
              "paadal_category": "Acts of Spot",
              "paadal_meaning": "The same happens when the husband is engaged in sports in river, garden etc."
            }
          },
          {
            "paadal": "மனைவி தலைத்தாள் கிழவோன் கொடுமை \nதம் உள ஆதல் வாயில்கட்கு இல்லை.",
            "vilakkam": {
              "paadal_category": "Role of Interceders",
              "paadal_meaning": "The interceders are not entitled to speak about the objectionable conduct of the husband before his wife."
            }
          },
          {
            "paadal": "மனைவி முன்னர்க் கையறு கிளவி \nமனைவிக்கு உறுதி உள்வழி உண்டே. ",
            "vilakkam": {
              "paadal_category": "Role of Interceders",
              "paadal_meaning": "Such words as will unnerve the wife may be used when she is at the point of being reconciled."
            }
          },
          {
            "paadal": "முன்னிலைப் புறமொழி எல்லா வாயிற்கும் \nபின்னிலைத் தோன்றும் என்மனார் புலவர். ",
            "vilakkam": {
              "paadal_category": "Role of Interceders",
              "paadal_meaning": "Learned men say that all interceders are used to address persons in third person at the latter half of their mediation."
            }
          },
          {
            "paadal": "தொல்லவை உரைத்தலும் நுகர்ச்சி ஏத்தலும் \nபல் ஆற்றானும் ஊடலின் தகைத்தலும் \nஉறுதி காட்டலும் அறிவு மெய்ந் நிறுத்தலும் \nஏதுவின் உரைத்தலும் துணிவு காட்டலும் \nஅணி நிலை உரைத்தலும் கூத்தர் மேன.",
            "vilakkam": {
              "paadal_category": "Utterance by Minstrel Messengers",
              "paadal_meaning": "Kūttar (கூத்தர்) are used to quote previous instances, to speak highly of their union, to end their love-quarrel in diverse ways to convince them of the aim of life, to correct their thoughts, to tell them what their action wiil lead to, to tell them why they should consent for the union and to tell her that the present mode of wearing her ornament will serve no useful purpose."}
          },
          {
            "paadal": "நிலம் பெயர்ந்து உரைத்தல் அவள் நிலை உரைத்தல் \nகூத்தர்க்கும் பாணர்க்கும் யாத்தவை உரிய. ",
            "vilakkam": {
              "paadal_category": "Utterance by Minstrel Messengers",
              "paadal_meaning": "Both kūttar (கூத்தர்) and pāṇar (பாணர்) are entitled to go where the husband resides and tell him his wife's condition."}
          },
          {
            "paadal": "ஆற்றது பண்பும் கருமத்து விளைவும் \nஏவல் முடிவும் வினாவும் செப்பும் \nஆற்றிடைக் கண்ட பொருளும் இறைச்சியும் \nதோற்றம் சான்ற அன்னவை பிறவும் \nஇளையோர்க்கு உரிய கிளவி என்ப. ",
            "vilakkam": {
              "paadal_category": "Utterance by Attendant Class Youth",
              "paadal_meaning": "They say that youngsters are entitled to describe the nature of the route, the result of their action and the end of their order, to ask him what they have to do and to tell him the necessary things unasked, what they found on the way, the karupporuḷ (கருப்பொருள்) and other things that came within their view."}
          },
          {
            "paadal": "உழைக் குறுந் தொழிலும் காப்பும் உயர்ந்தோர் \nநடக்கை எல்லாம் அவர்கண் படுமே.",
            "vilakkam": {
              "paadal_category": "Utterance by Attendant Class Youth",
              "paadal_meaning": "They are entitled to do personal service and to watch, and do other acts which may be done to the great."
            }
          },
          {
            "paadal": "பின் முறை ஆக்கிய பெரும் பொருள் வதுவைத் \nதொல் முறை மனைவி எதிர்ப்பாடு ஆயினும் \nஇன் இழைப் புதல்வனை வாயில் கொண்டு புகினும் \nஇறந்தது நினைஇக் கிழவோன் ஆங்கண் \nகலங்கலும் உரியன் என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "Hero's Remorse",
              "paadal_meaning": "Learned men say that the husband noting his wife receiving the other wives married after her with lamps etc. and getting into their houses with her son provided with ornaments may think of the past and feel troubled in his mind."
            }
          },
          {
            "paadal": "தாய் போல் கழறித் தழீஇக் கோடல் \nஆய் மனைக் கிழத்திக்கும் உரித்து என மொழிப \nகவவொடு மயங்கிய காலையான. ",
            "vilakkam": {
              "paadal_category": "And the Heroine's Response",
              "paadal_meaning": "When the husband is in a troubled condition, the wife may admonish him like his mother and embrace him."
            }
          },
          {
            "paadal": "அவன் சோர்பு காத்தல் கடன் எனப்படுதலின் \nமகன் தாய் உயர்பும் தன் உயர்பு ஆகும் \nசெல்வன் பணி மொழி இயல்பு ஆகலான.",
            "vilakkam": {
              "paadal_category": "And the Heroine's Response",
              "paadal_meaning": "Since it is the duty of the wife not to disclose her husband's objectionable ways, she may consider, in obedience to the husband's advice, the honour of kāmakkiḻatti (காமக்கிழட்டி) to be her own honour."}
          },
          {
            "paadal": "எண் அரும் பாசறை பெண்ணொடு புணரார்.",
            "vilakkam": {
              "paadal_category": "Hero in War-camp",
              "paadal_meaning": "Husbands do not meet their wives in the tents of war"
            }
          },
          {
            "paadal": "புறத்தோர் ஆங்கண் புணர்வது ஆகும்.",
            "vilakkam": {
              "paadal_category": "Hero in War-camp",
              "paadal_meaning": "They say that union with women other than iṟkiḻatti (இற்கிழத்தி) and kāmakkiḻatti (காமக்கிழத்தி) is allowable."}
          },
          {
            "paadal": "காம நிலை உரைத்தலும் தேர் நிலை உரைத்தலும் \nகிழவோன் குறிப்பினை எடுத்துக் கூறலும் \nஆவொடு பட்ட நிமித்தம் கூறலும் \nசெலவு உறு கிளவியும் செலவு அழுங்கு கிளவியும் \nஅன்னவை பிறவும் பார்ப்பார்க்கு உரிய.",
            "vilakkam": {
              "paadal_category": "Utterance by Brahminfolk",
              "paadal_meaning": "Brahmans (பிராமணர்கள்) are used to tell the husband of his amorous condition and of what is worthy of him, to openly express in words his mind and to encourage him to proceed or discourage him from proceeding on account of good or bad omens etc."}
          },
          {
            "paadal": "எல்லா வாயிலும் இருவர் தேஎத்தும் \nபுல்லிய மகிழ்ச்சிப் பொருள என்ப.",
            "vilakkam": {
              "paadal_category": "The Intent of Interceders",
              "paadal_meaning": "All intercedes, they say, have the duty of creating amicability between the two—husband and wife through pleasing words."
            }
          },
          {
            "paadal": "அன்பு தலைப்பிரிந்த கிளவி தோன்றின் \nசிறைப்புறம் குறித்தன்று என்மனார் புலவர்.",
            "vilakkam": {
              "paadal_category": "The Intent of Interceders",
              "paadal_meaning": "Learned men say that, if they have to use harsh words, they iare to use them in their hearing distance out of their sight."
            }
          },
          {
            "paadal": "தற் புகழ் கிளவி கிழவன் முன் கிளத்தல் \nஎத் திறத்தானும் கிழத்திக்கு இல்லை \nமுற்பட வகுத்த இரண்டு அலங்கடையே.",
            "vilakkam": {
              "paadal_category": "Heroine's Self-praise",
              "paadal_meaning": "The wife does, under no circumstances, speak highly of herself before tlie* husband except on two occasions mentioned above."
            }
          },
          {
            "paadal": "கிழவி முன்னர்த் தற் புகழ் கிளவி \nகிழவோன் வினைவயின் உரிய என்ப.",
            "vilakkam": {
              "paadal_category": "Hero's Self-adulation",
              "paadal_meaning": "They say that the husband speaks highly of himself before his wife when he starts for war."
            }
          },
          {
            "paadal": "மொழி எதிர் மொழிதல் பாங்கற்கு உரித்தே.",
            "vilakkam": {
              "paadal_category": "Confidant as critic",
              "paadal_meaning": "The husband's friend has the right to refute his statement."
            }
          },
          {
            "paadal": "குறித்து எதிர் மொழிதல் அஃகித் தோன்றும்.",
            "vilakkam": {
              "paadal_category": "Confidant as critic",
              "paadal_meaning": "Rarely does he refute him, understanding his mind through suggestion."
            }
          },
          {
            "paadal": "துன்புறு பொழுதினும் எல்லாம் கிழவன் \nவன்புறுத்தல்லது சேறல் இல்லை. ",
            "vilakkam": {
              "paadal_category": "Hero's Reassurance",
              "paadal_meaning": "The husband has to force his wife, on all occasions of separation, to give her consent."
            }
          },
          {
            "paadal": "செலவிடை அழுங்கல் செல்லாமை அன்றே \nவன்புறை குறித்த தவிர்ச்சி ஆகும்.",
            "vilakkam": {
              "paadal_category": "Hero's Desisting from parting",
              "paadal_meaning": "The pain at the time of separation for war is not dispensed with by not going, but by pressing the wife to give her consent."
            }
          },
          {
            "paadal": "கிழவி நிலையே வினையிடத்து உரையார் \nவென்றிக் காலத்து விளங்கித் தோன்றும்.",
            "vilakkam": {
              "paadal_category": "Hero on his Mission",
              "paadal_meaning": "They do not describe the condition of the wife during war, but it will be clearly seen after victory is won."
            }
          },
          {
            "paadal": "பூப்பின் புறப்பாடு ஈர் ஆறு நாளும் \nநீத்து அகன்று உறையார் என்மனார் புலவர் \nபரத்தையின் பிரிந்த காலையான.",
            "vilakkam": {
              "paadal_category": "Hero's Pursuit of Harlots",
              "paadal_meaning": "Even when the husband is prone to enjoy the company of concubines, he does not avoid the company of his wife for 12 days after she takes her bath after monthly periods."
            }
          },
          {
            "paadal": "வேண்டிய கல்வி யாண்டு மூன்று இறவாது.",
            "vilakkam": {
              "paadal_category": "Hero's Quest of Learning",
              "paadal_meaning": "The period of separation on account of study does not exceed three years."
            }
          },
          {
            "paadal": "வேந்து உறு தொழிலே யாண்டினது அகமே.",
            "vilakkam": {
              "paadal_category": "Parting at King's Calling",
              "paadal_meaning": "The period of separation on account of kingly errand does not exceed one year."
            }
          },
          {
            "paadal": "ஏனைப் பிரிவும் அவ் இயல் நிலையும்.",
            "vilakkam": {
              "paadal_category": "Other Missions",
              "paadal_meaning": "Other kinds of separation also are of the same nature.",
              "example": "Their period is one year."
            }
          },
          {
            "paadal": "யாறும் குளனும் காவும் ஆடி \nபதி இகந்து நுகர்தலும் உரிய என்ப.",
            "vilakkam": {
              "paadal_category": "Acts of Sport",
              "paadal_meaning": "They say that the husband and the wife may leave their home to spend their time sportively in rivers, tanks and gardens."
            }
          },
          {
            "paadal": "காமம் சான்ற கடைக்கோட் காலை \nஏமம் சான்ற மக்களொடு துவன்றி \nஅறம் புரி சுற்றமொடு கிழவனும் கிழத்தியும் \nசிறந்தது பயிற்றல் இறந்ததன் பயனே. ",
            "vilakkam": {
              "paadal_category": "Fruits of Wedded Love",
              "paadal_meaning": "The fruit of what is said before is that the husband and the wife having spent after their youth their time with their children in prosperous condition and with their righteous relatives, have to think of mōkṣa (மோட்சம்)."
            }
          },
          {
            "paadal": "தோழி தாயே பார்ப்பான் பாங்கன் \nபாணன் பாட்டி இளையர் விருந்தினர் \nகூத்தர் விறலியர் அறிவர் கண்டோர் \nயாத்த சிறப்பின் வாயில்கள் என்ப.",
            "vilakkam": {
              "paadal_category": "Interceders",
              "paadal_meaning": "The prominent interceders are the wife's friend, her foster-mother, brahmans (பிராமணர்கள்), husband's friend, he-bard, she-bard, young servants, guests, dancers, female dancers, learned men and passers-by."
            }
          },
          {
            "paadal": "வினை வயின் பிரிந்தோன் மீண்டு வரு காலை \nஇடைச்சுர மருங்கின் தவிர்தல் இல்லை \nஉள்ளம் போல உற்றுழி உதவும் \nபுள் இயல் கலி மா உடைமையான.",
            "vilakkam": {
              "paadal_category": "Hero Returning Home",
              "paadal_meaning": "When the husband returns after war, he does not tarry on the way, since he has strong horses flying like birds at the same speed as that of the mind."
            }
          }
        ]
      },
      {
        "iyal_name": "பொருளியல்",
        "iyal_eng":"Residual Aspects",
        "noorpa": [
          {
            "paadal": "இசை திரிந்து இசைப்பினும் இயையுமன் பொருளே \nஅசை திரிந்து இசையா என்மனார் புலவர். ",
            "vilakkam":
             {
              "paadal_category": "Nature of Signification",
              "paadal_meaning": "Learned men say that, if expressions pronounced in the usual way without any change in the metrical syllable, convey meaning other than their own, such meanings also come under poruḷ (பொருள்)."
            }
          },
          {
            "paadal": "நோயும் இன்பமும் இரு வகை நிலையின் \nகாமம் கண்ணிய மரபிடை தெரிய \nஎட்டன் பகுதியும் விளங்க ஒட்டிய \nஉறுப்புடையது போல் உணர்வுடையது போல் \nமறுத்து உரைப்பது போல் நெஞ்சொடு புணர்த்தும் \nசொல்லா மரபின் அவற்றொடு கெழீஇ \nசெய்யா மரபின் தொழிற்படுத்து அடக்கியும் \nஅவர் அவர் உறு பிணி தம போல் சேர்த்தியும் \nஅறிவும் புலனும் வேறுபட நிறீஇ \nஇரு பெயர் மூன்றும் உரிய ஆக \nஉவமவாயில் படுத்தலும் உவமம் \nஒன்று இடத்து இருவர்க்கும் உரிய பாற் கிளவி.",
            "vilakkam": 
            {
              "paadal_category": "The Monologic Utterances of Hero and Heroine",
              "paadal_meaning": "Such peculiar expressions are within the province of both (the lover and the lady-love) as those addressed to their minds as if they have organs, the sense of feeling and the capacity to refute, in literature wherein the eight rasas are suggested with reference to love-affair where there is pleasure and pain, ns those wherein objects which have no capacity to speak are made to discharge functions which they cannot do, as those wherein they identify other's suffering as if it is their own and as those wherein, whenever there is an opportunity to compare, two objects are compared with reference to three points of comparison by viewing knowledge and the object of knowledge as separate entities."
            }
          },
          {
            "paadal": "கனவும் உரித்தால் அவ் இடத்தான.",
            "vilakkam": 
            {
              "paadal_category": "Occassioning of Dreams",
              "paadal_meaning": "Dream also is within their province."
            }
          },
          {
            "paadal": "தாய்க்கும் உரித்தால் போக்கு உடன் கிளப்பின்.",
            "vilakkam": 
            {
              "paadal_category": "Occassioning of Dreams",
              "paadal_meaning": "Dream is within the province of the mother when elopement is described."
            }
          },
          {
            "paadal": "பால் கெழு கிளவி நால்வர்க்கும் உரித்தே \nநட்பின் நடக்கை ஆங்கு அலங்கடையே. ",
            "vilakkam": 
            {
              "paadal_category": "Characters Given to Monologic Utterances ",
              "paadal_meaning": "#The peculiar expressions (mentioned in sūtra (சூத்திர) 2) are within the province of four except with reference to the conversation between friends."
            }
          },
          {
            "paadal": "உயிரும் நாணும் மடனும் என்று இவை \nசெயிர் தீர் சிறப்பின் நால்வர்க்கும் உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Traits of Principal Women Characters",
              "paadal_meaning": "Life, shyness and credulity of superior type free from flaws are within the province of the lour."
            }
          },
          {
            "paadal": "வண்ணம் பசந்து புலம்புறு காலை \nஉணர்ந்த போல உறுப்பினைக் கிழவி \nபுணர்ந்த வகையான் புணர்க்கவும் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "The Unique Delineation of the Heroine",
              "paadal_meaning": "When the lady is alone with change of complexion on account of her separation from the lover, she may describe her limbs as if they too are aware of it."
            }
          },
          {
            "paadal": "உடம்பும் உயிரும் வாடியக்கண்ணும் \nஎன் உற்றனகொல் இவை எனின் அல்லதை \nகிழவோற் சேர்தல் கிழத்திக்கு இல்லை.",
            "vilakkam": 
            {
              "paadal_category": "The Unique Delineation of the Heroine",
              "paadal_meaning": "Even when the lady has her limbs in an emaciated condition and her mind devoid of spirit, she can say only what a situation have these arrived at ? and can never go where the lover is."
            }
          },
          {
            "paadal": "ஒரு சிறை நெஞ்சமொடு உசாவும் காலை \nஉரியதாகலும் உண்டு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Unique Delineation of the Heroine",
              "paadal_meaning": "They say that she may be considered to be within her province if she is in her mind in the company of het: lover when she sometimes argues with her mind."
            }
          },
          {
            "paadal": "தன்வயின் கரத்தலும் அவன்வயின் வேட்டலும் \nஅன்ன இடங்கள் அல் வழி எல்லாம் \nமடனொடு நிற்றல் கடன் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "The Unique Delineation of the Heroine",
              "paadal_meaning": "They say that it is the duty of the lady to preserve her modesty on all occasions, except when the lover conceals from her his illicit company with a courtezan and when her yearning towards him gets mastery over her."
            }
          },
          {
            "paadal": "அறத்தொடு நிற்கும் காலத்து அன்றி \nஅறத்து இயல் மரபு இலள் தோழி என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Revelation of Candestine's Love",
              "paadal_meaning": "They say that the lady's friend is not entitled to inform the lady's mother or foster-mother of her love towards her lover, unless the lady wants her to do so."
            }
          },
          {
            "paadal": "எளித்தல் ஏத்தல் வேட்கை உரைத்தல் \nகூறுதல் உசாஅதல் ஏதீடு தலைப்பாடு \nஉண்மை செப்பும் கிளவியொடு தொகைஇ \nஅவ் எழு வகைய என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Revelation of Candestine's Love",
              "paadal_meaning": "Learned men say that aṟattoṭu-niṟṟal (அறத்தொடு-நிற்றல்) is of seven kinds:— Speaking low of the lover, speaking high of the lover, mention of his intense love, mingling in the coversation of others, presentation of causes, their meeting (without her knowledge) and the statement of the actual fact."
            }
          },
          {
            "paadal": "உற்றுழி அல்லது சொல்லல் இன்மையின் \nஅப் பொருள் வேட்கை கிழவியின் உணர்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Revelation of Candestine's Love",
              "paadal_meaning": "Since it is not expressed except at the critical situation, the lady's love towards the lover is inferred by others through her features etc."
            }
          },
          {
            "paadal": "செறிவும் நிறைவும் செம்மையும் செப்பும் \nஅறிவும் அருமையும் பெண்பாலான. ",
            "vilakkam": 
            {
              "paadal_category": "Traits of Women Characters",
              "paadal_meaning": "Fullness, modesty, straightforwardness, skill in speech, keen knowledge and depth of mind are the qualities of women."
            }
          },
          {
            "paadal": "பொழுதும் ஆறும் காப்பும் என்று இவற்றின் \nவழுவின் ஆகிய குற்றம் காட்டலும் \nதன்னை அழிதலும் அவண் ஊறு அஞ்சலும் \nஇரவினும் பகலினும் நீ வா என்றலும் \nகிழவோன் தன்னை வாரல் என்றலும் \nநன்மையும் தீமையும் பிறிதினைக் கூறலும் \nபுரை பட வந்த அன்னவை பிறவும் \nவரைதல் வேட்கைப் பொருள என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Urging the Hero to Marry the Heroine",
              "paadal_meaning": "They say that the mention of the dangers due to inopportune time, inconvenient path and watch, mention of her diffidence, mention of the difficulties she (lady-love) will be put to, telling him to come at night and at day, asking the lover not to come and mention of the merits and the defects, etc., at the kaḷavu (களவு) stage are intended only to make him approach the bride's father to give her in marriage to him."
            }
          },
          {
            "paadal": "வேட்கை மறுத்துக் கிளந்தாங்கு உரைத்தல் \nமரீஇய மருங்கின் உரித்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Urging the Hero to Marry the Heroine",
              "paadal_meaning": "They say that it is also proper to avoid the suggestion of varaital (வரைதல்)  vēṭkai (வேட்கை)  and to express it clearly when kaḷavu (களவு)  exceeds the time limit."

            }
          },
          {
            "paadal": "தேரும் யானையும் குதிரையும் பிறவும் \nஊர்ந்தனர் இயங்கலும் உரியர் என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Modes of Conveyance",
            "paadal_meaning": "They say that the lovers may come riding on chariots, elephants, horses, etc., (during kaḷavu (களவு))."
            }
          },
          {
            "paadal": "உண்டற்கு உரிய அல்லாப் பொருளை \nஉண்டன போலக் கூறலும் மரபே.",
            "vilakkam": 
            {
              "paadal_category": "An Imaginative Device",
              "paadal_meaning": "There is tradition to describe an object which is not capable of eating, to have eaten."
            }
          },
          {
            "paadal": "பொருள் என மொழிதலும் வரை நிலை இன்றே \nகாப்புக் கைம்மிகுதல் உண்மையான \nஅன்பே அறனே இன்பம் நாணொடு \nதுறந்த ஒழுக்கம் பழித்து அன்று ஆகலின் \nஒன்றும் வேண்டா காப்பினுள்ளே.",
            "vilakkam": 
            {
              "paadal_category": "Heroine Subjected to Rigours of Watch",
              "paadal_meaning": "When the watch is severe, it is not forbidden to mention about wealth to the lover.Behaviour beyond the limits of aṉpū (அன்பு) (love), aṟaṉ(அறன்) (dharma), iṇpam (இன்பம்) (pleasure) and nāṇ (நான்) (modesty) is not objectionable (in kaḷavu(களவு)) and is hence admissible. Hence consideration of them is not necessary when there is strict watch."
            }
          },
          {
            "paadal": "சுரம் என மொழிதலும் வரை நிலை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Heroine Forbidden to Accompany the Hero",
              "paadal_meaning": "It is not prohibited to say that it is the desert (to pass through)."
            }
          },
          {
            "paadal": "உயர்ந்தோர் கிளவி வழக்கொடு புணர்தலின் \nவழக்கு வழிப்படுதல் செய்யுட்குக் கடனே.",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "It is incumbent in Poetry to take recourse to the ways of the high class people when the ways of the world are described."
            }
          },
          {
            "paadal": "அறக் கழிவு உடையன பொருட் பயம் பட வரின் \nவழக்கு என வழங்கலும் பழித்து அன்று என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "It is not to be despised to take under vaḻakku (வழக்கு) that which is against dharma (தர்மம்) if it comes under akam (அகம்)."
            }
          },
          {
            "paadal": "மிக்க பொருளினுள் பொருள் வகை புணர்க்க \nநாணுத் தலைப்பிரியா நல்வழிப் படுத்தே.",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "When akam (அகம்) is described, attention is to be paid not to dispense with modesty (of women)."
            }
          },
          {
            "paadal": "முறைப்பெயர் மருங்கின் கெழுதகைப் பொதுச் சொல் \nநிலைக்கு உரி மரபின் இரு வீற்றும் உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "When word of relationship is to be used, an appropriate common word may be used both by men and women."
            }
          },
          {
            "paadal": "தாயத்தின் அடையா ஈயச் செல்லா \nவினைவயின் தங்கா வீற்றுக் கொளப்படா \nஎம் என வரூஉம் கிழமைத் தோற்றம் \nஅல்லாவாயினும் புல்லுவ உளவே. ",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "Objects which one cannot claim to be his, since it is not inherited from parents, it is not given to him by others, it is not earned by him through his own work and it is not got by him by other ways, may be described to be his or her own if it suits the context."
            }
          },
          {
            "paadal": "ஒரு பால் கிளவி எனைப் பாற்கண்ணும் \nவரு வகைதானே வழக்கு என மொழிப. ",
            "vilakkam": 
            {
              "paadal_category": "Usage in Poetry",
              "paadal_meaning": "Valakku(வழக்கு) (usage) is that which is universal."
            }
          },
          {
            "paadal": "எல்லா உயிர்க்கும் இன்பம் என்பது \nதான் அமர்ந்து வரூஉம் மேவற்று ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Pursuit of Pleasure",
              "paadal_meaning": "Pleasure for all beings is in the region of mind."
            }
          },
          {
            "paadal": "பரத்தை வாயில் நால்வர்க்கும் உரித்தே \nநிலத் திரிபு இன்று அஃது என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Pursuit of Prostitutes",
              "paadal_meaning": "ūṭal (ஊடல்) due to the lover's connection with courtezan is found among the women of all the four castes. They say that it happens in the same region."
            }
          },
          {
            "paadal": "ஒருதலை உரிமை வேண்டினும் மகடூஉப் \nபிரிதல் அச்சம் உண்மையானும் \nஅம்பலும் அலரும் களவு வெளிப்படுக்கும் என்று \nஅஞ்ச வந்த ஆங்கு இரு வகையினும் \nநோக்கொடு வந்த இடையூறு பொருளினும் \nபோக்கும் வரைவும் மனைவிகண் தோன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Mindscape",
              "paadal_meaning": "It may happen that the wife volunteers to go along with the husband or to ask him approach her father for marriage when she wants to decide her right of becoming the wife, when she fears his separation and when she fears that their intimacy may become known to all through ampal (ஆம்பல்) and alar (அலர்) and when there are obstacles for their meeting in the form of other's observation."
            }
          },
          {
            "paadal": "வருத்த மிகுதி சுட்டும் காலை \nஉரித்து என மொழிப வாழ்க்கையுள் இரக்கம்.",
            "vilakkam": 
            {
              "paadal_category": "Hero's Debauchery and the Interceders",
              "paadal_meaning": "They say that the married life deserves to be pitied when the misunderstanding between the husband and the wife is very great."
            }
          },
          {
            "paadal": "மனைவி உயர்வும் கிழவோன் பணிவும் \nநினையும் காலை புலவியுள் உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Moments of Sulking and Passion",
              "paadal_meaning": "Wife's getting the upper band and husband's submission are found, on examination, during love-quarrel."
            }
          },
          {
            "paadal": "நிகழ் தகை மருங்கின் வேட்கை மிகுதியின் \nபுகழ் தகை வரையார் கற்பினுள்ளே. ",
            "vilakkam": 
            {
              "paadal_category": "Moments of Sulking and Passion",
              "paadal_meaning": "They do not prohibit the husband and the wife alter marriage to speak in eulogistic terms at the height of passion."
            }
          },
          {	
            "paadal": "இறைச்சிதானே உரிப் புறத்ததுவே.",
            "vilakkam": 
            {
              "paadal_category": "Iraicci, The Suggestive Import",
              "paadal_meaning": "Iṟaicci (இறைச்சி) is that which is not related to uripporul̥(உரிபொருள்) ."
            }
          },
          {
            "paadal": "இறைச்சியின் பிறக்கும் பொருளுமார் உளவே \nதிறத்து இயல் மருங்கின் தெரியுமோர்க்கே.",
            "vilakkam": 
            {
              "paadal_category": "Iraicci, The Suggestive Import",
              "paadal_meaning": "There are meanings suggested by iṟaicci (இறைச்சி) and they are understood only by the learned at the proper context."
            }
          },
          {
            "paadal": "அன்புறு தகுவன இறைச்சியுள் சுட்டலும் \nவன்புறை ஆகும் வருந்திய பொழுதே.",
            "vilakkam": 
            {
              "paadal_category": "Iraicci, The Suggestive Import",
              "paadal_meaning": "When (the lady) is in distress, it is a source of comfort to her to point out in iṟaicci(இறைச்சி) the love of the husband towards her."
            }
          },
          {
            "paadal": "செய் பொருள் அச்சமும் வினைவயின் பிரிவும் \nமெய்பெற உணர்த்தும் கிழவி பாராட்டே.",
            "vilakkam": 
            {
              "paadal_category": "The Import of Hero's Praise",
              "paadal_meaning": "Fear to do a thing (lest she should meet with an obstacle) and separation to gather wealth clearly tell us his love for the lady."
            }
          },
          {
            "paadal": "கற்புவழிப் பட்டவள் பரத்தைமை ஏத்தினும் \nஉள்ளத்து ஊடல் உண்டு என மொழிப. ",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Attitude towards the Concubine",
              "paadal_meaning": "They say that a wife after marriage, though she extols a courtezan, has in her mind the feeling of jealousy and the consequent love-quarrel with her husband."
            }
          },
          {
            "paadal": "கிழவோள் பிறள் குணம் இவை எனக் கூறி \nகிழவோன் குறிப்பினை உணர்தற்கும் உரியள். ",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Attitude towards the Concubine",
              "paadal_meaning": "She deserves to gauge the mind of the husband by extolling another woman."
            }
          },
          {
            "paadal": "தம் உறு விழுமம் பரத்தையர் கூறினும் \nமெய்ம்மையாக அவர்வயின் உணர்ந்தும் \nதலைத்தாட் கழறல் தம் எதிர்ப்பொழுது இன்றே \nமலிதலும் ஊடலும் அவை அலங்கடையே.",
            "vilakkam": 
            {
              "paadal_category": "Heroine's Attitude towards the Concubine",
              "paadal_meaning": "Though the wife considers the complaint effected by the courtezan against her husband to be true, she does not openly accuse him when he goes before her. She does so only when she is not in a happy mood and in love-quarrel."
            }
          },
          {
            "paadal": "பொழுது தலைவைத்த கையறு காலை \nஇறந்த போலக் கிளக்கும் கிளவி \nமடனே வருத்தம் மருட்கை மிகுதியொடு \nஅவை நாற் பொருட்கண் நிகழும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Mindscape of Lonesome Heroine",
              "paadal_meaning": "They say that, when the lady is in distress at the approach of a season, her expression that the season has passed is due to ignorance, wonder or bewilderment and uncontrollable state."
            }
          },
          {
            "paadal": "இரந்து குறையுற்ற கிழவனைத் தோழி \nநிரம்ப நீக்கி நிறுத்தல் அன்றியும் \nவாய்மை கூறலும் பொய் தலைப்பெய்தலும் \nநல் வகையுடைய நயத்தின் கூறியும் \nபல் வகையானும் படைக்கவும் பெறுமே. ",
            "vilakkam": 
            {
              "paadal_category": "Confidante's Response to Hero's Solicitations",
              "paadal_meaning": "The lady's friend may, when the lover informs her of his hardship, try to avoid his company, speak truth, or utter lies, may mock at him in a pleasant manner and adopt different ways."
            }
          },
          {
            "paadal": "உயர் மொழிக் கிளவி உறழும் கிளவி \nஐயக் கிளவி ஆடூஉவிற்கு உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Utterances by the Hero",
              "paadal_meaning": "Both the lover and the lady-love may use extolling expression ; expression of doubt is the sole property of the lover alope."
            }
          },
          {
            "paadal": "உறுகண் ஓம்பல் தன் இயல்பு ஆகலின் \nஉரியதாகும் தோழிகண் உரனே.",
            "vilakkam": 
            {
              "paadal_category": "Confidante's Ruling Trait",
              "paadal_meaning": "Sound mind is necessary to the lady's friend, since she has the duty of dispelling the lady's distress."
            }
          },
          {
            "paadal": "உயர் மொழிக் கிளவியும் உரியவால் அவட்கே.",
            "vilakkam": 
            {
              "paadal_category": "Confidante's Ruling Trait",
              "paadal_meaning": "She has the right even to extol (the lover and the lady)."
            }
          },
          {
            "paadal": "வாயிற் கிளவி வெளிப்படக் கிளத்தல் \nதா இன்று உரிய தம்தம் கூற்றே. ",
            "vilakkam": 
            {
              "paadal_category": "Nature of Interceder's Utterances",
              "paadal_meaning": "It is not prohibited, but it is allowed for the intercedes to speak plainly their views."
            }
          },
          {
            "paadal": "உடனுறை உவமம் சுட்டு நகை சிறப்பு எனக் \nகெடல் அரு மரபின் உள்ளுறை ஐந்தே.",
            "vilakkam": 
            {
              "paadal_category": "Uḷḷuṟai (உள்ளுறை)",
              "paadal_meaning": "Uḷḷuṟai (உள்ளுறை) or suggested meaning is, from superior tradition, of five kinds— uṭaṉ-uṟai (உடனுறை), uvamam (உவமம்), cuṭṭu (சுட்டு), nakai (நகை) and ciṟappū (சிறப்பு)."
            }
          },
          {
            "paadal": "அந்தம் இல் சிறப்பின் ஆகிய இன்பம் \nதன்வயின் வருதலும் வகுத்த பண்பே.",
            "vilakkam": 
            {
              "paadal_category": "Uḷḷuṟai (உள்ளுறை)",
              "paadal_meaning": "The delectation coming from a series of superior experiences is also included under Uḷḷuṟai (உள்ளுறை)."
            }
          },
          {
            "paadal": "மங்கல மொழியும் வைஇய மொழியும் \nமாறு இல் ஆண்மையின் சொல்லிய மொழியும் \nகூறிய மருங்கின் கொள்ளும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Uḷḷuṟai (உள்ளுறை)",
              "paadal_meaning": "They say that euphemistic expressions like the use of auspicious words for inauspicious ones, words of decency for obscene words and figurative expressions to show bravery, etc., come within Uḷḷuṟai(உள்ளுறை)."
            }
          },
          {
            "paadal": "சினனே பேதைமை நிம்பிரி நல்குரவு \nஅனை நால் வகையும் சிறப்பொடு வருமே.",
            "vilakkam": 
            {
              "paadal_category": "Negative Traits Implying Positive Worth",
              "paadal_meaning": "From the suggested ciṟappū (சிறப்பு), anger, ignorance, jealousy and poverty—these four—may further be suggested."
            }
          },
          {
            "paadal": "அன்னை என்னை என்றலும் உளவே \nதொல் நெறி முறைமை சொல்லினும் எழுத்தினும் \nதோன்றா மரபின என்மனார் புலவர். ",
            "vilakkam": 
            {
              "paadal_category": "A Poetic Convention",
              "paadal_meaning": "Learned men say that traditionally the words aaṉṉai (அன்னை) (by the lady to the friend—vice versa) and eṉṉai(என்னை) (by both to the lover) were in use though they are not so mentioried in the Eḻuttatikāram (எழுத்ததிகாரம்) and the Collatikāram (சொல்லதிகாரம்)."
            }
          },
          {
            "paadal": "ஒப்பும் உருவும் வெறுப்பும் என்றா \nகற்பும் ஏரும் எழிலும் என்றா \nசாயலும் நாணும் மடனும் என்றா \nநோயும் வேட்கையும் நுகர்வும் என்று ஆங்கு \nஆவயின் வரூஉம் கிளவி எல்லாம் \nநாட்டு இயல் மரபின் நெஞ்சு கொளின் அல்லது \nகாட்டலாகாப் பொருள என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Abstractions in Poetry",
              "paadal_meaning": "#The meanings of the words oppū (ஒப்பு), uru (உரு), veṟuppū (வெறுப்பு), kaṟpū(கற்பு) ,ēr(ஏர்), eḻil (எழில்), cāyal(சாயல்), nān(நான்), maṭan (மடன்), nōy(நோய்), vēṭkai (வேட்கை), nukarvu (நுகர்வு), etc., can be only understood by the mind."
            }
          },
          {
            "paadal": "இமையோர் தேஎத்தும் எறி கடல் வரைப்பினும் \nஅவை இல் காலம் இன்மையான. ",
            "vilakkam": 
            {
              "paadal_category": "Abstractions in Poetry",
              "paadal_meaning": "Since there is no time when they are not found in Heaven and Earth and not explained in words."
            }
          }
        ]
      },
      {
        "iyal_name": "மெய்ப்பாட்டியல்",
        "iyal_eng":"Manifest Emotions",
        "noorpa": [
          {
            "paadal": "பண்ணைத் தோன்றிய எண் நான்கு பொருளும் \nகண்ணிய புறனே நால் நான்கு என்ப.",
            "vilakkam": {
              "paadal_category": "Poetic Sentiments",
              "paadal_meaning": "They say that the thirty-two things that are manifest in places of sport like garden, river-side etc., may be considered to come within sixteen."}
          },
          {
            "paadal": "நால் இரண்டு ஆகும் பாலுமார் உண்டே.",
            "vilakkam": {
              "paadal_category": "Poetic Sentiments",
              "paadal_meaning": "The above sixteen are also compressed into eight."}
          },
          {
            "paadal": "நகையே அழுகை இளிவரல் மருட்கை \nஅச்சம் பெருமிதம் வெகுளி உவகை என்று \nஅப் பால் எட்டே மெய்ப்பாடு என்ப. ",
            "vilakkam": {
              "paadal_category": "Principal Emotions as Treated in Poetry",
              "paadal_meaning": "They say that meyppāṭū (மெய்ப்பாடு) are the following eight: nakai(நகை) [hāsya(Joy)] ; aḻukai(அழுகை) [karuṇa(Sadness)] ; iḷivaral (இளிவரல்) [bībhatsa(Disgust)] ; maruṭkai (மருட்கை) [adbhuta (sentiment (rasa) of wonder)] ; accam (அச்சம்) [bhayānaka (fear)] ; perumitam (பெருமிதம்) [vīra (கணவன்)] ; vekuḷi (வெகுளி) [raudra (Anger)] ; and uvakai (உவகை) (śṟṅgāra (love))."}
          },
          {
            "paadal": "எள்ளல் இளமை பேதைமை மடன் என்று \nஉள்ளப்பட்ட நகை நான்கு என்ப. ",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "Nakoi (நகோய்) the outcome of four:—mockery, childishness, ignorance and credulity"}
          },
          {
            "paadal": "இளிவே இழவே அசைவே வறுமை என \nவிளிவு இல் கொள்கை அழுகை நான்கே.",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of genuine aḻukai(அழுகை) is four:— contemptible treatment, loss, change for the worse and poverty."}
          },
          {
            "paadal": "மூப்பே பிணியே வருத்தம் மென்மையொடு யாப்புற வந்த இளிவரல் \nநான்கே.",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of iSvaral () is four:-old age, disease, pain and low status."}
          },
          {
            "paadal": "புதுமை பெருமை சிறுமை ஆக்கமொடு \nமதிமை சாலா மருட்கை நான்கே. ",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of maruṭkai (மருக்கை) outside the province of intelligentzia is four:—newness, greatness, littleness and transformation."}
          },
          {
            "paadal": "அணங்கே விலங்கே கள்வர் தம் இறை எனப் \nபிணங்கல் சாலா அச்சம் நான்கே. ",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of unsullied accam (அக்காம்) is four:—evil spirits, wild animals, thieves and one's own king."}
          },
          {
            "paadal": "கல்வி தறுகண் புகழ்மை கொடை எனச் \nசொல்லப்பட்ட பெருமிதம் நான்கே.",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of perumitam (பெருமிதம்) mentioned above is four:— scholarship, bravery, fame and liberality."}
          },
          {
            "paadal": "உறுப்பறை குடிகோள் அலை கொலை என்ற \nவெறுப்பின் வந்த வெகுளி நான்கே.",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of vekuḷi (கோபம்) is the extremely painful cutting of limbs, destruction of family, plunder and murder."}
          },
          {
            "paadal": "செல்வம் புலனே புணர்வு விளையாட்டு என்று \nஅல்லல் நீத்த உவகை நான்கே.",
            "vilakkam": {
              "paadal_category": "Sources of the Principal Emotions",
              "paadal_meaning": "The source of high class uvakai (உவகை) is four:—love, experience of pleasures (like beauty etc.), sexual union and sport (in gardens etc.)."}
          },
          {
            "paadal": "ஆங்கவை ஒரு பால் ஆக ஒரு பால் \nஉடைமை இன்புறல் நடுவுநிலை அருளல் \nதன்மை அடக்கம் வரைதல் அன்பு எனாஅ \nகைம்மிகல் நலிதல் சூழ்ச்சி வாழ்த்தல் \nநாணுதல் துஞ்சல் அரற்று கனவு எனாஅ \nமுனிதல் நினைதல் வெரூஉதல் மடிமை \nகருதல் ஆராய்ச்சி விரைவு உயிர்ப்பு எனாஅ \nகையாறு இடுக்கண் பொச்சாப்பு பொறாமை \nவியர்த்தல் ஐயம் மிகை நடுக்கு எனாஅ \nஇவையும் உளவே அவை அலங்கடையே.",
            "vilakkam": {
              "paadal_category": "Emotions Other than the principal Eight",
              "paadal_meaning": "Those mentioned above being on one side, the following being on the other side, are included under mey-p-pāṭū (மெய்ப்பாடூ) in a way, different from them: (1) the feeling of ownership, (2) the feeling of satisfaction, (3) the state of equipoise, (4) showing grace, (5) remaining in ones own nature,(6) control or modesty, (7) right conduct, (8) affection, (9) exceeding the bounds, (10) tormenting others, (11) pondering, (12) wishing health, (13) feeling shy, (14) sleep, (15) blabbering, (16) dream, (17) feeling disgusted, (18) remembering the past, (19) slight anger, (20) sluggishness, (21) thinking mood, (22) deliberation, (23) haste^ (24) sighing, (25) sense of disappointment, (26) suffering, (27) forgetting or disconcerting mood, (28) jealousy, (29) perspiration, (30) indecisive nature, (31) audacity and (32) tremor."}
          },
          {
            "paadal": "புகு முகம் புரிதல் பொறி நுதல் வியர்த்தல் \nநகு நயம் மறைத்தல் சிதைவு பிறர்க்கு இன்மையொடு \nதகு முறை நான்கே ஒன்று என மொழிப. ",
            "vilakkam": {
              "paadal_category": "Emotions Proper to the Fivefold Akam Love: First Phase",
              "paadal_meaning": "The first (avasthā (அவஸ்தா)) consists of four in order:—meeting the look (of the lover), having the perspired forehead, controlling the laugh and not exposing her #weakness to others."}
          },
          {
            "paadal": "கூழை விரித்தல் காது ஒன்று களைதல் \nஊழ் அணி தைவரல் உடை பெயர்த்து உடுத்தலொடு \nஊழி நான்கே இரண்டு என மொழிப.",
            "vilakkam": {
              "paadal_category": "Second Phase",
              "paadal_meaning": "The second consists of four in order:—loosening the hair, setting aright the ear-ornament, moving the ornaments here and there and loosening the dress and tightening it."}
          },
          {
            "paadal": "அல்குல் தைவரல் அணிந்தவை திருத்தல் \nஇல் வலியுறுத்தல் இரு கையும் எடுத்தலொடு \nசொல்லிய நான்கே மூன்று என மொழிப.",
            "vilakkam": {
              "paadal_category": "Third",
              "paadal_meaning": "They say that the third consists of four:—placing the hand on the pudendum muliebre, bringing the ornaments to their original position, pretending to be strong and raising both the hands."}
          },
          {
            "paadal": "பாராட்டு எடுத்தல் மடம் தப உரைத்தல் \nஈரம் இல் கூற்றம் ஏற்று அலர் நாணல் \nகொடுப்பவை கோடல் உளப்படத் தொகைஇ \nஎடுத்த நான்கே நான்கு என மொழிப.",
            "vilakkam": {
              "paadal_category": "Fourth Phase",
              "paadal_meaning": "The fourth consists of four:—speaking in appreciative terms, speaking beyond the region of credulity, feeling shy for the public unsympathetic talk of their love and receiving whatever is given."}
          },
          {
            "paadal": "தெரிந்து உடம்படுதல் திளைப்பு வினை மறுத்தல் \nகரந்திடத்து ஒழிதல் கண்டவழி உவத்தலொடு \nபொருந்திய நான்கே ஐந்து என மொழிப. ",
            "vilakkam": {
              "paadal_category": "Fifth Phase",
              "paadal_meaning": "The fifth consists of four:—giving her consent after deliberation, avoiding sport with friends etc., choosing solitude and feeling happy on seeing the lover."}
          },
          {
            "paadal": "புறம் செயச் சிதைதல் புலம்பித் தோன்றல் \nகலங்கி மொழிதல் கையறவு உரைத்தலொடு \nவிளம்பிய நான்கே ஆறு என மொழிப.",
            "vilakkam": {
              "paadal_category": "Sixth Phase",
              "paadal_meaning": "They say that the sixth consists of four:—not relishing the ornamentations done to the body, appearing dejected, speaking with a disturbed mind and speaking in utter disappointment."}
          },
          {
            "paadal": "அன்ன பிறவும் அவற்றொடு சிவணி \nமன்னிய வினைய நிமித்தம் என்ப.",
            "vilakkam": {
              "paadal_category": "Manifestation and Absence of Emotions",
              "paadal_meaning": "They say that others also similar to them may serve as causes for the marriage in the form of kaṟpū (கற்பு)."}
          },
          {
            "paadal": "வினை உயிர் மெலிவு இடத்து இன்மையும் உரித்தே.",
            "vilakkam": {
              "paadal_category": "Manifestation and Absence of Emotions",
              "paadal_meaning": "When she is in the chance of losing her life, it is allowed not to have the viṉai (வினை)."}
          },
          {
            "paadal": "அவையும் உளவே அவை அலங்கடையே.",
            "vilakkam": {
              "paadal_category": "Manifestation and Absence of Emotions",
              "paadal_meaning": "They also may exist in places other than they."}
          },
          {
            "paadal": "இன்பத்தை வெறுத்தல் துன்பத்துப் புலம்பல் \nஎதிர் பெய்து பரிதல் ஏதம் ஆய்தல் \nபசி அட நிற்றல் பசலை பாய்தல் \nஉண்டியின் குறைதல் உடம்பு நனி சுருங்கல் \nகண் துயில் மறுத்தல் கனவொடு மயங்கல் \nபொய்யாக் கோடல் மெய்யே என்றல் \nஐயம் செய்தல் அவன் தமர் உவத்தல் \nஅறன் அளித்து உரைத்தல் ஆங்கு நெஞ்சு அழிதல் \nஎம் மெய் ஆயினும் ஒப்புமை கோடல் \nஒப்புவழி உவத்தல் உறு பெயர் கேட்டல் \nநலத் தக நாடின் கலக்கமும் அதுவே.",
            "vilakkam": {
              "paadal_category": "Other Emotions Proper to the passion of love",
              "paadal_meaning": "On careful examination the following twenty also form the nimitta (நிமித்த) for the marriage: (1) averseness towards pleasures, (2) soliloquy in suffering, (3) expressing one's grief making the object of love stand before the mind's eye (4) consideration of the impediments, (5) lasting, (6) spreading of beauty-spots on the skin, (7) reduction in the consumption of food, (8) emaciation of the body, (9) sleeplessness, (10) perplexity in dream, (11) doubting the veracity of the words of the object of love, (12) coming to the conclusion that the words are true, (13) doubting his meeting, (14) feeling happy at the sight of his relatives, (15) finding fault with the God of Dharma (), 1 (16) piteous expression of one's feelings, (17) finding the point of comparison between any object and the object of love, (18) feeling happy that there is a point of comparison, (19) feeling happy on hearing the name or fame of the lover and (20) confusion of mind."}
          },
          {
            "paadal": "முட்டுவயின் கழறல் முனிவு மெய்ந் நிறுத்தல் \nஅச்சத்தின் அகறல் அவன் புணர்வு மறுத்தல் \nதூது முனிவு இன்மை துஞ்சிச் சேர்தல் \nகாதல் கைம்மிகல் கட்டுரை இன்மை என்று \nஆயிரு நான்கே அழிவு இல் கூட்டம்.",
            "vilakkam": {
              "paadal_category": "Emotions Preparatory to the Wedded Course",
              "paadal_meaning": "The following eight form the nimitta (நிமித்தா) to the meeting of the lover and the lady-love without their minds experiencing any suffering:—admonition when there is an obstacle, controling anger, evading on account of fear, avoiding union, not feeling angry with the messengers—birds etc., pretending to sleep, being overpowered by passion and keeping silent."}
          },
          {
            "paadal": "தெய்வம் அஞ்சல் புரை அறம் தெளிதல் \nஇல்லது காய்தல் உள்ளது உவர்த்தல் \nபுணர்ந்துழி உண்மை பொழுது மறுப்பு ஆக்கம் \nஅருள் மிக உடைமை அன்பு தொக நிற்றல் \nபிரிவு ஆற்றாமை மறைந்தவை உரைத்தல் \nபுறஞ்சொல் மாணாக் கிளவியொடு தொகைஇ \nசிறந்த பத்தும் செப்பிய பொருளே.",
            "vilakkam": {
              "paadal_category": "Emotions Proper to the Wedded Course",
              "paadal_meaning": "The following ten too are included among the above mentioned (i.e.) from the nimitta (நிமித்தா) for aḻivil-kūṭṭam (aḻivil-kūṭṭam): —fearing God, discerning the correct Dharma (தர்மம்), feeling angry towards the lover for some imaginary wrong in him, not being disposed to-accept the real favour shewn by the lover, telling the truth at the time of union, rejecting at the unsuitable time, being in ecstactf on account of ease of mind, openly exhibiting the height of her love, not being able to put up with separation and relating to the lover the alar(அலார்)."}
          },
          {
            "paadal": "பிறப்பே குடிமை ஆண்மை ஆண்டொடு \nஉருவு நிறுத்த காம வாயில் \nநிறையே அருளே உணர்வொடு திரு என \nமுறையுறக் கிளந்த ஒப்பினது வகையே.",
            "vilakkam": {
              "paadal_category": "Traits of Compatibility",
              "paadal_meaning": "The likeness of the lover and the lady-love is necessary in the following tenheredity, character, manliness, age, appearance, love, gentlemanliness, grace, intelligence and wealth."}
          },
          {
            "paadal": "நிம்பிரி கொடுமை வியப்பொடு புறமொழி \nவன்சொல் பொச்சாப்பு மடிமையொடு குடிமை \nஇன்புறல் ஏழைமை மறப்பொடு ஒப்புமை \nஎன்று இவை இன்மை என்மனார் புலவர். ",
            "vilakkam": {
              "paadal_category": "Negatives that Mar Conjugal Harmony",
              "paadal_meaning": "Learned men say that the following should be avoided:— jealousy, cruelty, pride, back-biting, hard words, irresoluteness, sluggishness, haughtiness on account of heredity, lowering one's dignity, forgetfulness, and misplaced love on account of likeness."}
          },
          {
            "paadal": "கண்ணினும் செவியினும் திண்ணிதின் உணரும் \nஉணர்வுடை மாந்தர்க்கு அல்லது தெரியின் \nநல் நயப் பொருள்கோள் எண்ண அருங்குரைத்தே.",
            "vilakkam": {
              "paadal_category": "Subtleties of Emotional Manifestations",
              "paadal_meaning": "The meyppāṭū (மெய்ப்பாட்டியல்) of fine quality cannot be understood by those other than they who have correct perspective of things through correct observation and hearing."}
          }
        ]
      },
      {
        "iyal_name": "உவமயியல்",
        "iyal_eng":"Modes of Comparison",
        "noorpa": [
          {
            "paadal": "வினை பயன் மெய் உரு என்ற நான்கே \nவகை பெற வந்த உவமத் தோற்றம். ",
            "vilakkam": 
            {
              "paadal_category": "Grounds of Comparision",
              "paadal_meaning": "Simile is based on four kinds of resemblance:— action, effect, quality and colour."
            }
          },
          {
            "paadal": "விரவியும் வரூஉம் மரபின என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Grounds of Comparision",
              "paadal_meaning": "They say that traditionally the points of comparison may mingle with one another."
            }
          },
          {
            "paadal": "உயர்ந்ததன் மேற்றே உள்ளும் காலை.",
            "vilakkam": 
            {
              "paadal_category": "Grounds of Comparision",
              "paadal_meaning": "Upamāna(உவமம்) should be, on examination, of superior nature. "
            }
          },
          {
            "paadal": "சிறப்பே நலனே காதல் வலியொடு \nஅந் நால் பண்பும் நிலைக்களம் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Sources of Similitude",
              "paadal_meaning": "They say that simile is used to denote four: superiority, beauty, affection and heroism in or towards the upamēya(உவமேயம்)."
            }
          },
          {
            "paadal": "கிழக்கிடு பொருளொடு ஐந்தும் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Sources of Similitude",
              "paadal_meaning": "It may be of fire kinds including inferiority "
            }
          },
          {
            "paadal": "முதலும் சினையும் என்று ஆயிரு பொருட்கும் \nநுதலிய மரபின் உரியவை உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Sources of Similitude",
              "paadal_meaning": "Whole and part may be compared to what is suitable according to tradition."
            }
          },
          {
            "paadal": "சுட்டிக் கூறா உவமம் ஆயின் \nபொருள் எதிர் புணர்த்துப் புணர்த்தன கொளலே.",
            "vilakkam": 
            {
              "paadal_category": "Inexplicit Vehicle",
              "paadal_meaning": "If the point of comparison is not expressly stated, that which is suitable should be taken into account."
            }
          },
          {
            "paadal": "உவமமும் பொருளும் ஒத்தல் வேண்டும்.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Similitude",
              "paadal_meaning": "Upamāna (உவமம்) and upamēya (உவமேயம்) should suit each other."
            }
          },
          {
            "paadal": "பொருளே உவமம் செய்தனர் மொழியினும் \nமருள் அறு சிறப்பின் அஃது உவமம் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "",
              "paadal_meaning": "If the upamēya (உவமேயம்)  is made the upamāna (உவமம்) (and consequently the upamāna (உவமம்) is made the upamēya (உவமேயம்)  ), it also comes under upamd, if such an expression is considered to possess doubtless beauty."
            }
          },
          {
            "paadal": "பெருமையும் சிறுமையும் சிறப்பின் தீராக் \nகுறிப்பின் வரூஉம் நெறிப்பாடு உடைய.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Similitude",
              "paadal_meaning": "upamēya (உவமேயம்) and Upamāna (உவமம்) are found in Literature in beautiful passages full of suggestion even when superiority or inferiority is expressed or suggested."
            }
          },
          {
            "paadal": "அவைதாம், \nஅன்ன ஏய்ப்ப உறழ ஒப்ப \nஎன்ன மான என்றவை எனாஅ \nஒன்ற ஒடுங்க ஒட்ட ஆங்க \nஎன்ற வியப்ப என்றவை எனாஅ \nஎள்ள விழைய விறப்ப நிகர்ப்ப \nகள்ள கடுப்ப ஆங்கவை எனாஅ \nகாய்ப்ப மதிப்ப தகைய மருள \nமாற்ற மறுப்ப ஆங்கவை எனாஅ \nபுல்ல பொருவ பொற்ப போல \nவெல்ல வீழ ஆங்கவை எனாஅ \nநாட நளிய நடுங்க நந்த \nஓட புரைய என்றவை எனாஅ \nஆறு ஆறு அவையும் அன்ன பிறவும் \nகூறும் காலைப் பல் குறிப்பினவே.",
            "vilakkam": 
            {
              "paadal_category": "Comparision Makers",
              "paadal_meaning": "The particles which suggest comparison in diverse ways are:—to mention thirtytwo and more. (1) aṉṉa (அன்ன ) (2)  ēyppa (ஏய்ப்ப) (3) uṟaḻa (உறழ) (4) oppa (ஒப்ப) (5) eṉṉa (என்ன) (6) māṉa (மான) (7) oṉṟa (ஒன்ற) (8) oṭuṅka (ஒடுங்க) (9) oṭṭa (ஒட்ட) (10)  āṅka (ஆங்க) (11) eṉṟa (என்ற ) (12)  viyappa (வியப்ப) (13)  eḷḷa (எள்ள) (14) viḻaiya (விழைய) (15) viṟappa (விறப்ப) (16) nikarppa (நிகர்ப்ப) (17) kaḷḷa (கள்ள ) (18) kaṭuppa(கடுப்ப) (19) kayppa (காய்ப்ப) (20) matippa (மதிப்ப) (21) takaiya (தகைய) (22) maruḷa (மருள) (23) māṟṟa (மாற்ற) (24) maṟuppa (மறுப்ப ) (25) pulla (புல்ல) (26) poruva (பொருவ) (27) poṟpa (பொற்ப) (28) pōla (போல) (29) vella (வெல்ல) (30) Vīḻa (வீழ) (31) nāṭa (நாட) and (32) naḷiya (நளிய) etc."
            }
          },
          {
            "paadal": "அன்ன ஆங்க மான விறப்ப \nஎன்ன உறழ தகைய நோக்கொடு \nகண்ணிய எட்டும் வினைப்பால் உவமம்.",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The following eight particles aṉṉa (அன்ன), āṅka (ஆங்க), māṉa (மான), viṟappa (விறப்ப), eṉṉa (என்ன), uṟaḷa (உறழ), takaiya (தகைய) and nōkka(நோக்க) are used when the point of comparison is an action."
            }
          },
          {
            "paadal": "அன்ன என் கிளவி பிறவொடும் சிவணும்.",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The particle aṉṉa (அன்ன) is used when others also are points of comparison."
            }
          },
          {
            "paadal": "எள்ள விழைய புல்ல பொருவ \nகள்ள மதிப்ப வெல்ல வீழ \nஎன்று ஆங்கு எட்டே பயனிலை உவமம்.",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The following eight eḷḷa (எள்ள), viḻaiya (விழைய), pulla (புல்ல), poruva (பொருவ), kaḷḷa (கள்ள), matippa (மதிப்ப), vella (வெல்ல) and Vīḻa (வீழ) are used when the point of comparison is effect."
            }
          },
          {
            "paadal": "கடுப்ப ஏய்ப்ப மருள புரைய \nஒட்ட ஒடுங்க ஓட நிகர்ப்ப என்று \nஅப் பால் எட்டே மெய்ப்பால் உவமம். ",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The following eight kaṭuppa (கடுப்ப), ēyppa (ஏய்ப்ப), maruḷa (மருள), puraiya (புரைய), oṭṭa (ஒட்ட), oṭunka (ஒடுங்க), ōṭa (ஓட) and nikarppa (நிகர்ப்ப) are used when the point of comparison is quality."
            }
          },
          {
            "paadal": "போல மறுப்ப ஒப்ப காய்த்த \nநேர வியப்ப நளிய நந்த என்று \nஒத்து வரு கிளவி உருவின் உவமம்.",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The following eight pōla (போல), maṟuppa (மறுப்ப), oppa (ஒப்ப), kāytta (காய்த்த), nēra (நேர), viyappa (வியப்ப), naḷiya (நளிய) and nanta (நந்த) are used when the point of comparison is colour."
            }
          },
          {
            "paadal": "தம்தம் மரபின் தோன்றுமன் பொருளே. ",
            "vilakkam": 
            {
              "paadal_category": "Funtional Delimitation of Comaprision Markers",
              "paadal_meaning": "The meanings of the particles mentioned are those found in Literature."
            }
          },
          {
            "paadal": "நால் இரண்டு ஆகும் பாலுமார் உண்டே",
            "vilakkam": 
            {
              "paadal_category": "Ramification of Grounds for Comparision",
              "paadal_meaning": "The four (kinds of upamā (உவமம்) mentioned above) maybe doubled."
            }
          },
          {
            "paadal": "பெருமையும் சிறுமையும் மெய்ப்பாடு எட்டன் \nவழி மருங்கு அறியத் தோன்றும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Similitude and the Eightfold Emotions",
              "paadal_meaning": "Greatness and smallness, they say, appear as points of comparisons in passages beaming with meyppāṭū (மெய்ப்பாடு)."
            }
          },
          {
            "paadal": "உவமப் பொருளின் உற்றது உணரும் \nதெளி மருங்கு உளவே திறத்து இயலான. ",
            "vilakkam": 
            {
              "paadal_category": "Tenor and Vehicle",
              "paadal_meaning": "The heart of the poet in using a particular upamāna( உவமம்) is clearly understood through ripe experience in Literature."
            }
          },
          {
            "paadal": "உவமப் பொருளை உணரும் காலை மரீஇய மரபின் வழக்கொடு வருமே.",
            "vilakkam": 
            {
              "paadal_category": "Tenor and Vehicle",
              "paadal_meaning": "The significance of the use of a particular upamāna (உவமம்) is to be understood through the knowledge of tradition."
            }
          },
          {
            "paadal": "இரட்டைக்கிளவி இரட்டை வழித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Tenor and Vehicle",
              "paadal_meaning": "The upamēya (உவமேயம்) consisting of a noun and an adjunct has an upamāna (உவமம்) which also consists of a noun and an adjunct."
            }
          },
          {
            "paadal": "பிறிதொடு படாது பிறப்பொடு நோக்கி \nமுன்னை மரபின் கூறும் காலை \nதுணிவொடு வரூஉம் துணிவினோர் கொளினே. ",
            "vilakkam": 
            {
              "paadal_category": "Ullurai Uvamam",
              "paadal_meaning": "When a thing is described with reference to its origin following the rules of tradition without being compared to any other thing, the object to which it is compared can be seen by scholars through their ripe knowledge in Literature."
            }
          },
          {
            "paadal": "உவமப் போலி ஐந்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Ullurai Uvamam",
              "paadal_meaning": "They say that pseudo-simile is of five kinds."
            }
          },
          {
            "paadal": "தவல் அருஞ் சிறப்பின் அத் தன்மை நாடின் \nவினையினும் பயத்தினும் உறுப்பினும் உருவினும் \nபிறப்பினும் வரூஉம் திறத்த என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Ullurai Uvamam",
              "paadal_meaning": "If it is well described without any flaw, they may have reference to superiority in action, effect, parts, colour and origin."
            }
          },
          {
            "paadal": "கிழவி சொல்லின் அவள் அறி கிளவி.",
            "vilakkam": 
            {
              "paadal_category": "Vehicles in the Similitude of Characters",
              "paadal_meaning": "If the lady-love makes use of uvama-p-pōli (உவமப்போலி), the object described should be within the province of her knowledge."
            }
          },
          {
            "paadal": "தோழிக்கு ஆயின் நிலம் பெயர்ந்து உரையாது.",
            "vilakkam": 
            {
              "paadal_category": "Vehicles in the Similitude of Characters",
              "paadal_meaning": "If the uvama-p-pōli (உவமப்போலி) is used by the lady's friend, the objects described should not belong to the region other than that of her own."
            }
          },
          {
            "paadal": "கிழவோற்கு ஆயின் உரனொடு கிளக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Vehicles in the Similitude of Characters",
              "paadal_meaning": "If the uvama-p-pōli(உவமப்போலி) is made use of by the lover, it should be within the province of his knowledge."
            }
          },
          {
            "paadal": "ஏனோர்க்கு எல்லாம் இடம் வரைவு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vehicles in the Similitude of Characters",
              "paadal_meaning": "If the uvama-p-pōli(உவமப்போலி) is made use of by others, there is no restriction about the region."
            }
          },
          {
            "paadal": "இனிது உறு கிளவியும் துனி உறு கிளவியும் \nஉவம மருங்கின் தோன்றும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Thematic Import in Similitude",
              "paadal_meaning": "They say that the meyppāṭū (மெய்ப்பாடு) - pleasure and love-quarrcl- will be suggested through the suggested simile."
            }
          },
          {
            "paadal": "கிழவோட்கு உவமம் ஈர் இடத்து உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Thematic Import in Similitude",
              "paadal_meaning": "The suggested simile in the expression of the lady-love deserves to suggest the above two."
            }
          },
          {
            "paadal": "கிழவோற்கு ஆயின் இடம் வரைவு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Thematic Import in Similitude",
              "paadal_meaning": "There is no restriction with respect to iṭam (இடம்) so far as the lover is concerned."
            }
          },
          {
            "paadal": "தோழியும் செவிலியும் பொருந்துவழி நோக்கிக் \nகூறுதற்கு உரியர் கொள் வழியான. ",
            "vilakkam": 
            {
              "paadal_category": "Thematic Import in Similitude",
              "paadal_meaning": "Lady's friend and fostermothcr will have to make use of it as suits the context."
            }
          },
          {
            "paadal": "வேறுபட வந்த உவமத் தோற்றம் \nகூறிய மருங்கின் கொள் வழிக் கொளாஅல். ",
            "vilakkam": 
            {
              "paadal_category": "Other Classes of Simile",
              "paadal_meaning": "Upamā (உவமம்) of a type not mentioned before but found m Literature should be taken into account."
            }
          },
          {
            "paadal": "ஒரீஇக் கூறலும் மரீஇய பண்பே.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes of Simile",
              "paadal_meaning": "It is tradition to describe that an object differs from another."
            }
          },
          {
            "paadal": "உவமத் தன்மையும் உரித்து என மொழிப \nபயனிலை புரிந்த வழக்கத்தான.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes of Simile",
              "paadal_meaning": "They say that such expressions where effect a point of comparison is mentioned with reference to two objects do come under upamā (உவமம்) ."
            }
          },
          {
            "paadal": "தடுமாறு உவமம் கடி வரை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes of Simile",
              "paadal_meaning": "It is not excluded to use expressions suggesting simile in a way different from those mentioned."
            }
          },
          {
            "paadal": "அடுக்கிய தோற்றம் விடுத்தல் பண்பே \nநிரல் நிறுத்து அமைத்தல் நிரல் நிறை சுண்ணம் \nவரன் முறை வந்த மூன்று அலங்கடையே.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes of Simile",
              "paadal_meaning": "Uvama-v-aṭukkū (உவமஅடுக்கு) other than niraṉiṟuttamaittaḻ (நிரல் நிறுத்து அமைத்தல்), niraṉiṟai (நிரல் நிறை) and cuṇṇam (சுண்ணம்) is to be avoided."
            }
          }
        ]
      },
      {
        "iyal_name": "செய்யுளியல்",
        "iyal_eng":"Prosody",
        "noorpa": [
          {
            "paadal": "மாத்திரை எழுத்து இயல் அசை வகை எனாஅ \nயாத்த சீரே அடி யாப்பு எனாஅ \nமரபே தூக்கே தொடை வகை எனாஅ \nநோக்கே பாவே அளவு இயல் எனாஅ \nதிணையே கைகோள் கூற்று வகை எனாஅ \nகேட்போர் களனே கால வகை எனாஅ \nபயனே மெய்ப்பாடு எச்ச வகை எனாஅ \nமுன்னம் பொருளே துறை வகை எனாஅ \nமாட்டே வண்ணமொடு யாப்பு இயல் வகையின் \nஆறு தலை இட்ட அந் நால் ஐந்தும் \nஅம்மை அழகு தொன்மை தோலே \nவிருந்தே இயைபே புலனே இழைபு எனாஅப் \nபொருந்தக் கூறிய எட்டொடும் தொகைஇ \nநல் இசைப் புலவர் செய்யுள் உறுப்பு என \nவல்லிதின் கூறி வகுத்து உரைத்தனரே.",
            "vilakkam": 
            {
              "paadal_category": "Limbs of Metrical Verses",
              "paadal_meaning": "Scholars of fame have classified in clear terms that the following twenty-six along with the eight that follow are the, limbs of Poetry:— Māttirai (மாத்திரை ) , eḻuttū (எழுத்து) , acai (அசை), cīr (சீர்) , aṭi (அடி) , yāppiu (யாப்பு) , marapū (மரபு) , tūkkū (தூக்கு) , toṭai(தொடை) , nōkkū(நோக்கு) , pā(பா) , aḷavū (அளவு) , tiṇai (திணை) , kaikōḷ (கைகோள்) , kūrrū (கூற்று) , kēṭpōr (கேட்போர்) , kaḷaṉ (களன்) , kālam (காலம்) , payaṉ (பயன்) ,  meyppāṭū (மெய்ப்பாடு) , eccam (எச்சம்) , muṉṉam (முன்னம்) , poruḷ (பொருள்) , tuṟai (துறை) , māṭṭū (மாட்டே) , vaṇṇam(வண்ணம்) , and ammai (அம்மை) , aḻakū (அழகு) , toṉmai (தொன்மை) , tōl (தோல்) , viruntū (விருந்து) , iyaipū (இயைபு) , pulaṉ (புலன்) and iḻaipū(இழைபு)."}
          },
          {
            "paadal": "அவற்றுள், \nமாத்திரை வகையும் எழுத்து இயல் வகையும் \nமேல் கிளந்தனவே என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Phonemes and Phonic Measure",
              "paadal_meaning": "Learned men say that, of them, the nature of māttirai (மாத்திரை)  ( mātrā (மாத்ரா)) and eḻuttū (எழுத்து) has been mentioned before, (i.e.) in Nūṉmarapū (நுண்மரபு) of Eḻuttatikāram (எழுத்ததிகாரம்)."}
          },
          {
            "paadal": "குறிலே நெடிலே குறில் இணை குறில் நெடில் \nஒற்றொடு வருதலொடு மெய்ப் பட நாடி \nநேரும் நிரையும் என்றிசின் பெயரே. ",
            "vilakkam": 
            {
              "paadal_category": "Nēracai (நேர்அசை)  and Niraiyacai (நிறைஅசை)",
              "paadal_meaning": "(Of them), one short syllable, or one long syllable with or without a consonant after it is called nēracai (நேர்அசை) and two short syllables or one short syllable followed by a long syllable with or without a consonant after it is called niraiacai (நிறைஅசை)."}
          },
          {
            "paadal": "இரு வகை உகரமொடு இயைந்தவை வரினே \nநேர்பும் நிரைபும் ஆகும் என்ப \nகுறில் இணை உகரம் அல் வழியான.",
            "vilakkam": 
            {
              "paadal_category": "Nērpū (நேர்பு) and niraipū (நிரைபு)",
              "paadal_meaning": "They say that, if they (nēr (நேர்) and nirai (நிரை)) are followed by the two kinds of ukaram (உகரம்) (murrukaram (முருகரம்) and kurriyal ukaram (குற்றியல் உகரம்)), they are called nērpū (நேர்பு) and niraipū (நிரைபு) except when one short syllable is followed by ukaram (உகரம்)."}
          },
          {
            "paadal": "இயலசை முதல் இரண்டு ஏனவை உரியசை.",
            "vilakkam": 
            {
              "paadal_category": "Iyalacai (இயலசை) and Uriyacai (உரியசை).",
              "paadal_meaning": "The first two (nēr-acai (நேரசை) and nirai-y-acai (நிரையசை)) are called iyal- acai (இயலசை) and rest (nērpacai (நேர்பசை) and niraipacai (நிறைபசை)) are called uri-y-acai (உரியசை)."}
          },
          {
            "paadal": "தனிக் குறில் முதலசை மொழி சிதைந்து ஆகாது.",
            "vilakkam": 
            {
              "paadal_category": "That Which is not nēr-acai (நேரசை)",
              "paadal_meaning": "A single short syllable cannot be taken as nēr-acai (நேரசை), if it necessitates a word to be unnaturally split."}
          },
          {
            "paadal": "ஒற்று எழுத்து இயற்றே குற்றியலிகரம்.",
            "vilakkam": 
            {
              "paadal_category": "Kuṟṟiyal-ikaram (குற்றியலிகரம்)",
              "paadal_meaning": "Kuṟṟiyal-ikaram (குற்றியலிகரம்) is of the nature of consonants."}
          },
          {
            "paadal": "முற்றியலுகரமும் மொழி சிதைத்துக் கொளாஅ \nநிற்றல் இன்றே ஈற்று அடி மருங்கினும்.",
            "vilakkam": 
            {
              "paadal_category": "Muṟṟiyal-ukaram (முற்றியலுகரம்) ",
              "paadal_meaning": "Muṟṟiyal-ukaram (முற்றியலுகரம்) is not taken as a part of nērpū (நேர்பு) or niraipū (நிரைபு), if it necessitates a word to be unnaturally split and it does not stand as an acai (அசை) at the end of a foot."}
          },
          {
            "paadal": "குற்றியலுகரமும் முற்றியலுகரமும் \nஒற்றொடு தோன்றி நிற்கவும் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Muṟṟiyal-ukaram (முற்றியலுகரம்)",
              "paadal_meaning": "Both kuṟṟiyal-ukaram(குற்றியலுகரம்) and muṟṟiyal-ukaram (முற்றியலுகரம்)  followed by a consonant may stand as acai (அசை)."}
          },
          {
            "paadal": "அசையும் சீரும் இசையொடு சேர்த்தி \nவகுத்தனர் உணர்த்தல் வல்லோர் ஆறே. ",
            "vilakkam": {"paadal_category": "Metrical Rhythm",
            "paadal_meaning": "The practice of the great is to split a line with reference to cīr (சீர்) and acai (அசை) as befits icai (இசை) (harmonious sound)."}
          },
          {
            "paadal": "ஈர் அசை கொண்டும் மூ அசை புணர்த்தும் \nசீர் இயைந்து இற்றது சீர் எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Metrical Foot",
              "paadal_meaning": "Cīr (சீர்) is made up of two acais (அசை)  or three in harmony with sound and sense."}
          },
          {
            "paadal": "இயலசை மயக்கம் இயற்சீர் ஏனை \nஉரியசை மயக்கம் ஆசிரிய உரிச்சீர்.",
            "vilakkam": 
            {
              "paadal_category": "Disyllabic Feet and Trisyllabic Feet",
              "paadal_meaning": "Combination of iyal-acai (இயலசை) forms iyaṟ-cīr (இயற்சீர்) and that of uri-y-acai (உரியசை) forms āciriya-v-uriccīr (ஆசிரிய உரிச்சீர்)."}
          },
          {
            "paadal": "முன் நிரை உறினும் அன்ன ஆகும். ",
            "vilakkam": 
            {
              "paadal_category": "Disyllabic Feet and Trisyllabic Feet",
              "paadal_meaning": "If nērpū (நேர்பு) or niraipū (நிரைபு) is followed by nirai (நிரை) at the end, it is also included under āciriya-v-uriccīr (ஆசிரிய உரிச்சீர்)."}
          },
          {
            "paadal": "நேர் அவண் நிற்பின் இயற்சீர்ப் பால.",
            "vilakkam": 
            {
              "paadal_category": "Disyllabic Feet and Trisyllabic Feet",
              "paadal_meaning": "If nērpū (நேர்பு) or niraipū (நிரைபு) is followed by nēr (நேர்) at the end, it comes under iyaṟcir (இயற்சீர்)."}
          },
          {
            "paadal": "இயலசை ஈற்று முன் உரியசை வரினே \nநிரையசை இயல ஆகும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Disyllabic Feet and Trisyllabic Feet",
              "paadal_meaning": "They say that, if iyal-acai (இயலசை) is followed by uri-y-acai (உரியசை) , it is considered to be similar to iyal-acai (இயலசை) being followed by nirai-y-acai (நிரையசை) "}
          },
          {
            "paadal": "அளபெடை அசைநிலை ஆகலும் உரித்தே",
            "vilakkam": 
            {
              "paadal_category": "Elongations",
              "paadal_meaning": "Aḷapeṭai (அளபெடை) may stand as an acai (அசை)."
            }
          },
          {
            "paadal": "ஒற்று அளபெடுப்பினும் அற்று என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Elongations",
              "paadal_meaning": "They say that consonantal Aḷapeṭai (அளபெடை) too is of the same nature (i.e.) it may stand as an acai (அசை)."}
          },
          {
            "paadal": "இயற்சீர் இறுதி முன் நேர் அவண் நிற்பின் \nஉரிச்சீர் வெண்பா ஆகும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uriccīr (வெண்பா உரிச்சீர்)",
              "paadal_meaning": "If nēr-acai (நேரசை) follows iyaē-cīr (இயற்சீர்), it is called veṇpā-v-uriccīr (வெண்பா உரிச்சீர்)."}
          },
          {
            "paadal": "வஞ்சிச் சீர் என வகை பெற்றனவே \nவெண் சீர் அல்லா மூ அசை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-c-cīr (வஞ்சிச் சீர்)",
              "paadal_meaning": "All the mūvacai-c-cir (மூ-அசைசீர்) other than veṇpā-v-uricīr (வெண்பா உரிச்சீர்) are called vañci-c-cīr(வஞ்சிச் சீர்)."}
          },
          {
            "paadal": "தன் பா அல் வழி தான் அடைவு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-c-cīr (வஞ்சிச் சீர்)",
              "paadal_meaning": "Vañci-y-uriccīr (வஞ்சி உரிச்சீர்) is not found in any other than vañci-p-pā (வஞ்சிப்பா)."}
          },
          {
            "paadal": "வஞ்சி மருங்கின் எஞ்சிய உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-c-cīr (வஞ்சிச் சீர்)",
              "paadal_meaning": "The other cīrs (சீர்) (i.e.) āriya-v-uricīr (ஆசிரிய உரிச்சீர்) and veṇpā-v-uricīr (வெண்பா உரிச்சீர்) may be found in vañci-p-pā (வஞ்சிப்பா) ."}
          },
          {
            "paadal": "வெண்பா உரிச்சீர் ஆசிரிய உரிச்சீர் \nஇன் பா நேரடிக்கு ஒருங்கு நிலை இலவே.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uricīr (வெண்பா உரிச்சீர்) and āciriya-v-uricīr (ஆசிரிய உரிச்சீர்)",
              "paadal_meaning": "Veṇpā-v-uricīr (வெண்பா உரிச்சீர்) and āciriya-v-uricīr (ஆசிரிய உரிச்சீர்) are not found in the foot of veṇpā (வெண்பா) which has four cīrs (சீர் )."}
          },
          {
            "paadal": "கலித்தளை மருங்கின் கடியவும் பெறாஅ.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uricīr (வெண்பா உரிச்சீர்) and āciriya-v-uricīr (ஆசிரிய உரிச்சீர்)",
              "paadal_meaning": "They (Veṇpā-v-uricīr (வெண்பா உரிச்சீர்) and āciriya-v-uricīr (ஆசிரிய உரிச்சீர்)) are not prohibited in kalittaḷai-maruṅkū (கலித்தளை மருங்கு) or kalippā (கலிப்பா) ."}
          },
          {
            "paadal": "கலித்தளை அடிவயின் நேர் ஈற்று இயற்சீர் \nநிலைக்கு உரித்து அன்றே தெரியுமோர்க்கே.",
            "vilakkam": 
            {
              "paadal_category": "Kalippā (கலிப்பா) and Nēr-īṟṟiyaṟ cīr (நேர் ஈற்று இயற்சீர்)",
              "paadal_meaning": "Iyaṟcīr (இயற்சீர்) which has nēr-acai (நேரசை) at the end does not, in the opinion of scholars, appear in the kaṭṭaḷai-y-aṭi (கலித்தளை அடி) of kalippā (கலிப்பா)."}
          },
          {
            "paadal": "வஞ்சி மருங்கினும் இறுதி நில்லா.",
            "vilakkam": 
            {
              "paadal_category": "Kalippā (கலிப்பா) and Nēr-īṟṟiyaṟ cīr (நேர் ஈற்று இயற்சீர்)",
              "paadal_meaning": "Nēr-īṟṟiyaṟ cīr (நேர் ஈற்று இயற்சீர்) does not stand at the end of a foot in vañci-p-pā (வஞ்சிப்பா)."}
          },
          {
            "paadal": "இசைநிலை நிறைய நிற்குவது ஆயின் \nஅசைநிலை வரையார் சீர் நிலை பெறவே.",
            "vilakkam": 
            {
              "paadal_category": "Single-syllabled Foot",
              "paadal_meaning": "They do not prohibit acai (அசை) to be considered a cīr (சீர்) if it satisfies the harmony of the sound."}
          },
          {
            "paadal": "இயற்சீர்ப் பாற்படுத்து இயற்றினர் கொளலே \nதளை வகை சிதையாத் தன்மையான.",
            "vilakkam": 
            {
              "paadal_category": "Single-syllabled Foot",
              "paadal_meaning": "ōr-acai-c-cīr (ஓரசைசீர்) may be taken to be similar to iyaṟcīr (இயற்சீர்) if no harm is done to taḷai (தளை)."}
          },
          {
            "paadal": "வெண்சீர் ஈற்றசை நிரையசை இயற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uriccīr (வெண்பா உரிச்சீர்)",
              "paadal_meaning": "The final acai (அசை) in veṇpā-v-uriccīr (வெண்பா உரிச்சீர்) is to function like nirai (நிரை) in iyoṟcīr-acai(இயற்சீர் அசை)."}
          },
          {
            "paadal": "இன் சீர் இயைய வருகுவது ஆயின் \nவெண்சீர் வரையார் ஆசிரிய அடிக்கே.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uriccīr (வெண்பா உரிச்சீர்)",
              "paadal_meaning": "They do not prohibit veṇpā-v-uriccīr (வெண்பா உரிச்சீர்) in āciriya-v-aṭi (ஆசிரிய அடி) , if it appears to be sweet to the ear."}
          },
          {
            "paadal": "அந் நிலை மருங்கின் வஞ்சி உரிச்சீர் \nஒன்றுதல் உடைய ஓர் ஒரு வழியே.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā-v-uriccīr (வெண்பா உரிச்சீர்)",
              "paadal_meaning": "Vañci-y-uriccīr (வஞ்சி உரிச்சீர்) may come rarely in āciriya-v-aṭi (ஆசிரிய அடி) for the same reason, i.e., if it is sweet to the ear."}
          },
          {
            "paadal": "நாற் சீர் கொண்டது அடி எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Metrical line",
              "paadal_meaning": "That which contains four cīrs (சீர்) is generally called aṭi (அடி) or foot."
            }
          },
          {
            "paadal": "அடி உள்ளனவே தளையொடு தொடையே.",
            "vilakkam": 
            {
              "paadal_category": "Metrical line",
              "paadal_meaning": "Taḷai (தளை) and toṭai (தொடை) are found only in the foot of-four cīrs (சீர்)."
            }
          },
          {
            "paadal": "அடி இறந்து வருதல் இல் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Metrical line",
              "paadal_meaning": "They say that they are not found in feet other than they."
            }
          },
          {
            "paadal": "அடியின் சிறப்பே பாட்டு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Metrical line",
              "paadal_meaning": "A verse which has feet of four cīrs (சீர்) is called pāṭṭū (பாட்டு)."
            }
          },
          {
            "paadal": "நால் எழுத்து ஆதி ஆக ஆறு எழுத்து \nஏறிய நிலத்தே குறளடி என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Kuṟaḷ-aṭi (குறளடி)",
              "paadal_meaning": "They say that kuṟaḷ-aṭi (குறளடி) contains four to six syllables."
            }
          },
          {
            "paadal": "ஏழ் எழுத்து என்ப சிந்தடிக்கு அளவே \nஈர் எழுத்து ஏற்றம் அவ் வழியான. ",
            "vilakkam": 
            {
              "paadal_category": "Cintaṭi (சிந்தடி)",
              "paadal_meaning": "They say that cintaṭi (சிந்தடி) contains seven to nine syllables."
            }
          },
          {
            "paadal": "பத்து எழுத்து என்ப நேரடிக்கு அளவே \nஒத்த நால் எழுத்து ஏற்றலங்கடையே.",
            "vilakkam": 
            {
              "paadal_category": "Nēraṭi (நேரடி) (Alavati)",
              "paadal_meaning": "Nēraṭi (நேரடி) or aḷavaṭi (அளவடி) , they say, contains ten to fourteen syllables."
            }
          },
          {
            "paadal": "மூ ஐந்து எழுத்தே நெடிலடிக்கு அளவே \nஈர் எழுத்து மிகுதலும் இயல்பு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Netiḷ-aṭi (நெடிலடி)",
              "paadal_meaning": "They say that netiḷ-aṭi (நெடிலடி) contains fifteen to seventeen syllables."
            }
          },
          {
            "paadal": "மூ ஆறு எழுத்தே கழிநெடிற்கு அளவே \nஈர் எழுத்து மிகுதலும் இயல்பு என மொழிப.",
            "vilakkam": 
            {"paadal_category": "Kaḻi-netiḷ-aṭi (கழிநெடிலடி)Kalinetilati",
            "paadal_meaning": "They say that kaḻi-netiḷ-aṭi (கழிநெடிலடி) contains eighteen to twenty syllables."
            }
          },
          {
            "paadal": "சீர் நிலைதானே ஐந்து எழுத்து இறவாது \nநேர் நிலை வஞ்சிக்கு ஆறும் ஆகும். ",
            "vilakkam": 
            {
              "paadal_category": "Structure of a Foot",
              "paadal_meaning": "Any cīr (சீர்) does not exceed five syllables. Nēr-nilai-vañci (நேர் நிலை வஞ்சி) or vañci (வஞ்சி) with two cīrs may have six syllables too."
            }
          },
          {
            "paadal": "எழுத்து அளவு எஞ்சினும் சீர் நிலைதானே \nகுன்றலும் மிகுதலும் இல் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Structure of a Foot",
              "paadal_meaning": "TThe number of cīr (சீர்) does neither increase nor decrease though the number of syllables may vary."
            }
          },
          {
            "paadal": "உயிர் இல் எழுத்தும் எண்ணப்படாஅ \nஉயிர்த் திறம் இயக்கம் இன்மையான.",
            "vilakkam": 
            {
              "paadal_category": "Structure of a Foot",
              "paadal_meaning": "Sound other than a vowel is not taken to account, since it is not an open sound like a vowel."
            }
          },
          {
            "paadal": "வஞ்சி அடியே இரு சீர்த்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-p-pā (வஞ்சிப்பா) line",
              "paadal_meaning": "The foot of vañci-p-pā (வஞ்சிப்பா) has two cīrs (சீர்)."
            }
          },
          {
            "paadal": "தன் சீர் எழுத்தின் சின்மை மூன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-p-pā (வஞ்சிப்பா) line",
              "paadal_meaning": "Three syllables is the minimum In the vañci-y-uri-c-cīr (வஞ்சி உரிச்சீர்)."
            }
          },
          {
            "paadal": "முச் சீரானும் வரும் இடன் உடைத்தே.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-p-pā (வஞ்சிப்பா) line",
              "paadal_meaning": "There are places where the foot of the vañci-y-uri-c-cīr (வஞ்சி உரிச்சீர்)."
            }
          },
          {
            "paadal": "அசை கூன் ஆகும் அவ்வயினான.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-p-pā (வஞ்சிப்பா) line",
              "paadal_meaning": "A syllable may stand as a detached foot in vañici-p-pā (வஞ்சிப்பா)."
            }
          },
          {
            "paadal": "சீர் கூன் ஆதல் நேரடிக்கு உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Vañci-p-pā (வஞ்சிப்பா) line",
              "paadal_meaning": "In aḷavaṭi (அளவடி), a cīr (சீர்) may stand as a detached foot."
            }
          },
          {
            "paadal": "ஐ வகை அடியும் விரிக்கும் காலை \nமெய் வகை அமைந்த பதினேழ் நிலத்தும் \nஎழுபது வகையின் வழு இல ஆகி \nஅறுநூற்று இருபத்தைந்து ஆகும்மே.",
            "vilakkam": 
            {
              "paadal_category": "Ramification of Foot",
              "paadal_meaning": "The five feet, when described in detail, with syllables of seventeen kinds from four-syllabled foot' to twenty-seven- syllabled foot are, first of all, seventy faultless kinds and then of 625 kinds."
            }
          },
          {
            "paadal": "ஆங்கனம் விரிப்பின் அளவு இறந்தனவே \nபாங்குற உணர்ந்தோர் பன்னும் காலை.",
            "vilakkam": 
            {
              "paadal_category": "Ramification of Foot",
              "paadal_meaning": "The classification of others like nāṟ-cīr-aṭi (நாற்சீரடி) in that way is endless in the literature of refined scholars."
            }
          },
          {
            "paadal": "ஐ வகை அடியும் ஆசிரியக்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Structure of a āciriyappā (ஆசிரியப்பா)",
              "paadal_meaning": "āciriyappā (ஆசிரியப்பா) may have all the five kinds of feet having nāṟ-cīr (நாற்சீர்)."
            }
          },
          {
            "paadal": "விராஅய் வரினும் ஒரூஉ நிலை இலவே.",
            "vilakkam": {"paadal_category": "Structure of a āciriyappā (ஆசிரியப்பா)",
            "paadal_meaning": "It may not be prohibited if any foot in āciriyam (ஆசிரியம்) is mixed up with different kinds of cīrs (சீர்)."}
          },
          {
            "paadal": "தன் சீர் வகையினும் தளை நிலை வகையினும் \nஇன் சீர் வகையின் ஐந்து அடிக்கும் உரிய \nதன் சீர் உள்வழித் தளை வகை வேண்டா. ",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "Different kinds of taḷai (தளை) are not necessary in the stanza which has the prescribed cīr (சீர்) and which can have the five kinds of feet, if it sounds well with its cīr (சீர்) and taḷai (தளை)."}
          },
          {
            "paadal": "சீர் இயை மருங்கின் ஓர் அசை ஒப்பின் \nஆசிரியத் தளை என்று அறியல் வேண்டும்.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "When there are two cīrs (சீர்) one following the other, and the final acai (அசை) of the former is identical with the initial acai (அசை) of the latter, it must be said that it is āciriya-t-taḷai (ஆசிரியத்தளை), i.e., if that acai (அசை) is nēr(நேர் ), it is called nēr-oṉṟiya-āciriya-t-taḷai (நேர் ஒன்றிய ஆசிரிய தலை) and if it is nirai (நிரை), it is called nirai-oṉṟiya-āciriya-t-taḷai (நிரை ஒன்றிய ஆசிரிய தலை). The .former cīr (சீர்) is iyaṟcīr (இயர்சீர்) and the latter is generally one other than it."}
          },
          {
            "paadal": "குறளடி முதலா அளவடி காறும் \nஉறழ் நிலை இலவே வஞ்சிக்கு என்ப. ",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "They say that vañci-y-uriccīr (வஞ்சி உரிச்சீர்) does not appear in kuṟaḷ-aṭi (குறளடி), cintaṭi (சிந்தடி) and alavaṭi (அளவடி)."}
          },
          {
            "paadal": "அளவும் சிந்தும் வெள்ளைக்கு உரிய \nதளை வகை ஒன்றாத் தன்மையான. ",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "Veṇpā (வெண்பா) deserve to have aḷavaṭi (அளவடி) and cintaṭi (சிந்தடி) with non-agreeing taḷai (தளை)."}
          },
          {
            "paadal": "அளவடி மிகுதி உளப்படத் தோன்றி \nஇரு நெடிலடியும் கலியிற்கு உரிய.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "Kalippā (கலிப்பா) deserves to have the two kinds of netiḷ-aṭi (நெடிலடி), i.e, netiḷ-aṭi (நெடிலடி) and kaḷi-netiḷ-aṭi (கலிநெடிலடி). "}
          },
          {
            "paadal": "நிரை முதல் வெண்சீர் வந்து நிரை தட்பினும் \nவரை நிலை இன்றே அவ் அடிக்கு என்ப.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "It is not prohibited with reference to that aṭi (அடி)  (kalippā-v-aṭi) (கலிப்பாவடி) to have nirai-mutal-veṇ-cīr (நிரை முதல் வெண்சீர்) (after veṇpā-v-uriccīr)(வெண்பா உரிச்சீர்)."}
          },
          {
            "paadal": "விராஅய தளையும் ஒரூஉ நிலை இன்றே.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "It is not to be prohibited if taḷai (தளை) is of a mixed nature."}
          },
          {
            "paadal": "இயற்சீர் வெள்ளடி ஆசிரிய மருங்கின் \nநிலைக்கு உரி மரபின் நிற்கவும் பெறுமே.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "Veṇpā-v-āti (வெண்பாவடி) with iyaṟcīr-veṇṭaḷai (இயற்சீர் வெண்டளை) may find a place in āciriyappā(ஆசிரியப்பா)."}
          },
          {
            "paadal": "வெண்தளை விரவியும் ஆசிரியம் விரவியும் \nஐஞ் சீர் அடியும் உள என மொழிப.",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "They say that āciriyappā (ஆசிரியப்பா) may have five kinds of feet with veṇṭaḷai (வெண்டளை) and āciriyattaḷai (ஆசிரியத்தளை) mixed together."}
          },
          {
            "paadal": "அறு சீர் அடியே ஆசிரியத் தளையொடு \nநெறி பெற்று வரூஉம் நேரடி முன்னே. ",
            "vilakkam": {"paadal_category": "Metrical Linkage",
            "paadal_meaning": "Foot having six cirs(சீர்) may appear in aciriyappa(ஆசிரியப்பா) with aciriyat-talai(ஆசிரியத்தளை) also after ner-ati (நேர்-அடி) or the foot with four cirs(சீர்)."}
          },
          {
            "paadal": "எழு சீர் அடியே முடுகியல் நடக்கும்.",
            "vilakkam": {"paadal_category": "Muṭukiyal (முடுகியல்)",
            "paadal_meaning": "Foot with seven cīrs (சீர்) may come in muṭukiyal (முடுகியல்) , which is a part of kalippā (கலிப்பா) ."}
          },
          {
            "paadal": "முடுகியல் வரையார் முதல் ஈர் அடிக்கும்.",
            "vilakkam": {"paadal_category": "Muṭukiyal (முடுகியல்)l",
            "paadal_meaning": "Feet with five and six cīrs (சீர்) are not prohibited in muṭukiyal (முடுகியல்) ."}
          },
          {
            "paadal": "ஆசிரிய மருங்கினும் வெண்பா மருங்கினும் \nமூ வகை அடியும் முன்னுதல் இலவே.",
            "vilakkam": {"paadal_category": "Muṭukiyal (முடுகியல்)",
            "paadal_meaning": "The three kinds of feet (of muṭukiyal (முடுகியல்)) do not make their appearance in āciriyappā (ஆசிரியப்பா) and veṇpā (வெண்பா) ."}
          },
          {
            "paadal": "ஈற்று அயல் அடியே ஆசிரிய மருங்கின் \nதோற்றம் முச் சீர்த்து ஆகும் என்ப.",
            "vilakkam": {"paadal_category": "Penultimate line of Aciriyappa",
            "paadal_meaning": "The penultimate foot in the āciriyappā (ஆசிரியப்பா) may, they say, have three cīrs (சீர்)."}
          },
          {
            "paadal": "இடையும் வரையார் தொடை உணர்வோரே.",
            "vilakkam": {"paadal_category": "Three-footed lines in Aciriyappa",
            "paadal_meaning": "Scholars in Prosody do not prohibit the last two feet but one from having three cīrs (சீர்)."}
          },
          {
            "paadal": "முச் சீர் முரற்கையுள் நிறையவும் நிற்கும்.",
            "vilakkam": {"paadal_category": "Three-footed lines in Kalippa",
            "paadal_meaning": "In kalippā (கலிப்பா) the penultimate foot may have four cīrs (சீர்) instead of three."}
          },
          {
            "paadal": "வஞ்சித் தூக்கே செந்தூக்கு இயற்றே.",
            "vilakkam": {"paadal_category": "Closing of Vancippa",
            "paadal_meaning": "The feet at the end of vañcippā (வஞ்சிப்பா) is similar to those of āciriya-p-pā (ஆசிரியப்பா), i.e., the penultimate foot may have three cīrs (சீர்) or four."}
          },
          {
            "paadal": "வெண்பாட்டு ஈற்று அடி முச் சீர்த்து ஆகும் \nஅசை சீர்த்து ஆகும் அவ் வழியான.",
            "vilakkam": {"paadal_category": "Veṇpā (வெண்பா) Ending",
            "paadal_meaning": "The last foot of a veṇpā (வெண்பா) has three cīrs (சீர்) the last of which is an acai-c-cīr(அசைச்சீர்)."}
          },
          {
            "paadal": "நேர் ஈற்று இயற்சீர் நிரையும் நிரைபும் \nசீர் ஏற்று இறூஉம் இயற்கைய என்ப.",
            "vilakkam": {"paadal_category": "Veṇpā (வெண்பா) Ending",
            "paadal_meaning": "They say that the acai-c-cīr (அசைச்சீர்) at the end of veṇpā (வெண்பா) may be nirai (நிரை) or niraipū (நிரைபு), if it is preceded by nērīṟṟiyaṟcīr (நேர் ஈற்று இயற்சீர்)."}
          },
          {
            "paadal": "நிரை அவண் நிற்பின் நேரும் நேர்பும் \nவரைவு இன்று என்ப வாய் மொழிப் புலவர்.",
            "vilakkam": {"paadal_category": "Veṇpā (வெண்பா) Ending",
            "paadal_meaning": "Scholars noted for their learning say that nēr (நேர்) and nērpū (நேர்பு) are not prohibited there i.e., at the end of veṇpā (வெண்பா) if it is preceded by nirai-y-īṟṟiyaṟ-cīr (நிரை ஈற்று இயற்சீர்) ."}
          },
          {
            "paadal": "எழு சீர் இறுதி ஆசிரியம் கலியே.",
            "vilakkam": {"paadal_category": "Kalippā (கலிப்பா) Ending",
            "paadal_meaning": "The penultimate foot of kalippā (கலிப்பா) is of the nature-of aciri- yappa(ஆசிரியப்பா) with three cirs(சீர்)."}
          },
          {
            "paadal": "வெண்பா இயலினும் பண்புற முடியும்.",
            "vilakkam": {"paadal_category": "Kalippā (கலிப்பா) Ending",
            "paadal_meaning": "It may be of the nature of veṇpā (வெண்பா)."}
          },
          {
            "paadal": "எழுத்து முதலா ஈண்டிய அடியின் \nகுறித்த பொருளை முடிய நாட்டல் \nயாப்பு என மொழிப யாப்பு அறி புலவர்.",
            "vilakkam": {"paadal_category": "Structure of a Composition",
            "paadal_meaning": "Scholars in Prosody say that yāppū (யாப்பு) is that which is made of the limbs mentioned above from eḻuttū (எழுத்து) to aṭi(அடி)."}
          },
          {
            "paadal": "பாட்டு உரை நூலே வாய்மொழி பிசியே \nஅங்கதம் முதுசொல் அவ் ஏழ் நிலத்தும் \nவண் புகழ் மூவர் தண் பொழில் வரைப்பின் \nநாற் பெயர் எல்லை அகத்தவர் வழங்கும் \nயாப்பின் வழியது என்மனார் புலவர்.",
            "vilakkam": {"paadal_category": "Modes of a Composition",
            "paadal_meaning": "They say that the material described by the residents of the fertile land of the famous three (Tamil kings) having four big boundaries in pāṭṭū (பாட்டு) , urai (உரை) , nūl (நூல்) , vāy-moḻi (வாய்மொழி) , pici (பிசி), aṅkatam (அங்கதம்) and mutu-col (முதுசொல்) is composed in verse form."}
          },
          {
            "paadal": "மரபேதானும், \nநாற் சொல் இயலான் யாப்புவழிப் பட்டன்று.",
            "vilakkam": {"paadal_category": "Usage",
            "paadal_meaning": "Marapū (மரபு) is the form of verse made up of the four kinds of words."}
          },
          {
            "paadal": "அகவல் என்பது ஆசிரியம்மே.",
            "vilakkam": {"paadal_category": "Verse Rhythm",
            "paadal_meaning": "The tūkkū (துக்கு) or ōcai (ஓசை) of āciriyappā (ஆசிரியப்பா) is, they say, akaval (அகவல்)."}
          },
          {
            "paadal": "அதாஅன்று என்ப வெண்பா யாப்பே.",
            "vilakkam": {"paadal_category": "Verse Rhythm",
            "paadal_meaning": "They say that it is not the rhythm found in veṇpā (வெண்பா)."}
          },
          {
            "paadal": "துள்ளல் ஓசை கலி என மொழிப.",
            "vilakkam": {"paadal_category": "Verse Rhythm",
            "paadal_meaning": "They say that the rhythm suited to kalippā (கலிப்பா)  is called tuḷḷal (துள்ளல்).."}
          },
          {
            "paadal": "தூங்கல் ஓசை வஞ்சி ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Verse Rhythm",
              "paadal_meaning": "He rhythm suited to vañci is called tūṅkal(தூங்கல்)."
            }
          },
          {
            "paadal": "மருட்பா ஏனை இரு சார் அல்லது \nதான் இது என்னும் தனிநிலை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Verse Rhythm",
              "paadal_meaning": "There is no rhythm peculiar to maruṭpā except that it has those belonging to veṇpā (வெண்பா) and āciriyappā (ஆசிரியப்பா)."
            }
          },
          {
            "paadal": "அவ் இயல் அல்லது பாட்டு ஆங்குக் கிளவார்.",
            "vilakkam": 
            {"paadal_category": "Verse Rhythm",
             "paadal_meaning": "They do not compose a verse pāṭṭū (பட்டு) except with those traits."
             }
          },
          {
            "paadal": "தூக்கு இயல் வகையே ஆங்கு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Verse Rhythm",
              "paadal_meaning": "They say that the nature of tūkkū (துக்கு) is the same as is mentioned before."
            }
          },
          {
            "paadal": "மோனை எதுகை முரணே இயைபு என \nநால் நெறி மரபின தொடை வகை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Rhyming",
              "paadal_meaning": "They say that Toṭai (தொடை) is traditionally classified into four:— mōṉai (மோனை) , etukāi (எதுகை), muraṇ (முரன்)and iyaipū(இயப்பு) ."
            }
          },
          {
            "paadal": "அளபெடை தலைப்பெய ஐந்தும் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Rhyming",
              "paadal_meaning": "It is of five kinds if aḷapeṭai (அளபெடை) is added to it."
            }
          },
          {
            "paadal": "பொழிப்பும் ஒரூஉவும் செந்தொடை மரபும் \nஅமைத்தனர் தெரியின் அவையுமார் உளவே.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Rhyming",
              "paadal_meaning": "In addition to the above, the three kinds of toṭai-poḻippū (தொடை-பொலிப்பு), orūu (ஒருவு) and centoṭai (சென்தோடை) may also be used."
            }
          },
          {
            "paadal": "நிரல் நிறுத்து அமைத்தலும் இரட்டை யாப்பும் \nமொழிந்தவற்று இயலான் முற்றும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Rhyming",
              "paadal_meaning": "Toṭai (தொடை), they say from literature, may be used at intervals or the same cīr (சீர்) may be repeated in a foot. The former is called niraṉiṟai-t-toṭai (நிரநிரை-டி-தொடை) and the latter iraṭṭai-t-toṭai (இரட்டை-டி-தொடை)."
            }
          },
          {
            "paadal": "அடிதொறும் தலை எழுத்து ஒப்பது மோனை.",
            "vilakkam": 
            {
              "paadal_category": "Mōṉai-t-toṭai (மோனை-த்-தொடை) ",
              "paadal_meaning": "Mōṉai (மோனை) is the alliteration of the initial sounds of the feet of a verse."
            }
          },
          {
            "paadal": "அஃது ஒழித்து ஒன்றின் எதுகை ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Etukai-t-totai (எதுகை-த்-தொடை)",
              "paadal_meaning": "Etukai (எதுகை) is the alliteration of sounds other than initial ones of the feet of a verse."
            }
          },
          {
            "paadal": "ஆயிரு தொடைக்கும் கிளையெழுத்து உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Etukai-t-totai (எதுகை-த்-தொடை)",
              "paadal_meaning": "Sounds of the same class also may be used in the above two kinds of toṭai (தொடை), i-e., in mōṉai-t-toṭai (மோனை-த்-தொடை) and etukoi-t-toṭai (எதுகை-த்-தோடை) ."
            }
          },
          {
            "paadal": "மொழியினும் பொருளினும் முரணுதல் முரணே.",
            "vilakkam": 
            {
              "paadal_category": "Mōṉai-t-toṭai (மோனை-த்-தொடை)",
              "paadal_meaning": "Muraṇ (முரன்) is that wherein words having mōṉai (மோனை) or etukai (எதுகை) have different meanings or words having the same meaning without mōṉai (மோனை) or etukai (எதுகை) stand in the corresponding cīr (சீர்) of each foot."
            }
          },
          {
            "paadal": "இறுவாய் ஒன்றல் இயைபின் யாப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Iyaipū-t-toṭai (இயைபுத் தொடை)",
              "paadal_meaning": "They say that identity, of sounds at the end of each foot in a verse is called iyaipū (இயப்பு)."
            }
          },
          {
            "paadal": "அளபு எழின் அவையே அளபெடைத் தொடையே.",
            "vilakkam": 
            {
              "paadal_category": "Aḷapetai-t-toṭai (அளபெடைத் தொடை)",
              "paadal_meaning": "If there is aḷapeṭai (அழபேதை) at the corresponding cīr (சீர்) of each foot, it is called aḷapetai-t-toṭai (அலபெடை-த்-தொடை)."
            }
          },
          {
            "paadal": "ஒரு சீர் இடையிட்டு எதுகை ஆயின் \nபொழிப்பு என மொழிதல் புலவர் ஆறே.",
            "vilakkam": 
            {
              "paadal_category": "Poḻippū-t-totai (போலிப்புத் தொடை)",
              "paadal_meaning": "It is the practice of scholars to call it poḻippū (போலிப்பு) if there is etukai (எதுகை) in alternate cīr (சீர்) of the same foot."
            }
          },
          {
            "paadal": "இரு சீர் இடையிடின் ஒரூஉ என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Orū-u-toṭai (ஒரூஉ-தொடை)",
              "paadal_meaning": "They say that, if there is etukai (எதுகை) in the cīr (சீர்) of the same interrupted by two cīr (சீர்), it is called orūu (ஒரூஉ)."
            }
          },
          {
            "paadal": "சொல்லிய தொடையொடு வேறுபட்டு இயலின் \nசொல் இயற் புலவர் அது செந்தொடை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Centoṭai (சென்தொடை)",
              "paadal_meaning": "They say that the total which differs from those mentioned above is called centoṭāi (சென்தோடை) composed by scholars with, ordinary words."
            }
          },
          {
            "paadal": "மெய் பெறு மரபின் தொடை வகைதாமே \nஐ ஈர் ஆயிரத்து ஆறு ஐஞ்ஞூற்றொடு \nதொண்டு தலை இட்ட பத்துக் குறை எழுநூற்று \nஒன்பஃது என்ப உணர்ந்திசினோரே.",
            "vilakkam": 
            {
              "paadal_category": "Centoṭai (சென்தொடை)",
              "paadal_meaning": "Experienced scholars say that toṭai (தொடை), as is found in literature, is of 13699 kinds."
            }
          },
          {
            "paadal": "தெரிந்தனர் விரிப்பின் வரம்பு இல ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Centoṭāi (சென்தொடை)",
              "paadal_meaning": "It will become endless if scholars well versed in literature begin to divide it further."
            }
          },
          {
            "paadal": "தொடை வகை நிலையே ஆங்கு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Centoṭāi (சென்தொடை)",
              "paadal_meaning": "They say that the classification of toṭai (தொடை) is of the sort mentioned above."
            }
          },
          {
            "paadal": "மாத்திரை முதலா அடிநிலை காறும் \nநோக்குதல் காரணம் நோக்கு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Nōkkū (நோக்கு)Nokku",
              "paadal_meaning": "The grace from māttirai (மாத்திரை) to foot which arrests the attention of the reader is called nōkkū (நோக்கு)."
            }
          },
          {
            "paadal": "ஆசிரியம் வஞ்சி வெண்பா கலி என \nநால் இயற்று என்ப பா வகை விரியே.",
            "vilakkam": 
            {
              "paadal_category": "Verse Classes",
              "paadal_meaning": "They say that pā (பா) is classified into four kinds; āciriyam (ஆசிரியம்), vañci (வஞ்சி), veṇpā (வெண்பா), and kali (கலி)."
            }
          },
          {
            "paadal": "அந் நிலை மருங்கின் அறம் முதல் ஆகிய மும் முதல் பொருட்கும் உரிய என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Subjects Treated in Verse Compositions",
              "paadal_meaning": "They say that all the four kinds of verses are used, when the three objects of human pursuit aṟam (அறம்), poruḷ (பொருள்), and iṉpam (இன்பம்) are described."
            }
          },
          {
            "paadal": "பா விரி மருங்கினைப் பண்புறத் தொகுப்பின் \nஆசிரியப்பா வெண்பா என்று ஆங்கு \nஆயிரு பாவினுள் அடங்கும் என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "The Inclusiveness of āciriyappā (ஆசிரியப்பா) and Veṇpā (வெண்பா)",
              "paadal_meaning": "If the four kinds of pā (பா) are properly compressed, they may come under the two- āciriyappā (ஆசிரியப்பா) and veṇpā (வெண்பா)."
            }
          },
          {
            "paadal": "ஆசிரிய நடைத்தே வஞ்சி ஏனை \nவெண்பா நடைத்தே கலி என மொழிப. ",
            "vilakkam": 
            {
              "paadal_category": "The Inclusiveness of āciriyappā (ஆசிரியப்பா) and Veṇpā (வெண்பா)",
              "paadal_meaning": "They say that vañci (வஞ்சி) falls under āciriyap-pā (ஆசிரியப்-பா) and kali (காளி) under the other kind, veṇpā (வெண்பா)."
            }
          },
          {
            "paadal": "வாழ்த்தியல் வகையே நாற்பாக்கும் உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Composition of Benediction",
              "paadal_meaning": "Stanzas paying homage to Gods and the Great may be composed in all the four kinds of verses."
            }
          },
          {
            "paadal": "வழிபடு தெய்வம் நின் புறங்காப்ப \nபழி தீர் செல்வமொடு வழி வழி சிறந்து \nபொலிமின் என்னும் புறநிலை வாழ்த்தே \nகலி நிலை வகையும் வஞ்சியும் பெறாஅ.",
            "vilakkam": 
            {
              "paadal_category": "Puṟanilai vāḻttū (புறநிலை வளத்து)",
              "paadal_meaning": "The puṟanilai vāḻttū (புறநிலை வளத்து) of the type 'May you prosper for generations to come with spotless fortune, you being protected by your family deity is not composed either in kali (காளி) or vañci (வஞ்சி)."
            }
          },
          {
            "paadal": "வாயுறை வாழ்த்தே அவையடக்கியலே \nசெவியறிவுறூஉ என அவையும் அன்ன.",
            "vilakkam": 
            {
              "paadal_category": "Vāyuṟai-vāḻttḻ (வாயுரை-வால்ட்டு), Avai-y-aṭakkū (அவை-ஒய்-அடக்கு) and Cevi-y-aṟi-v-uṟūu (செவி-ய்-உரை)",
              "paadal_meaning": "Vāyuṟai-vāḻttḻ (வாயுரை-வால்ட்டு), avai-y-aṭakkū (அவை-ஒய்-அடக்கு) and cevi-y-aṟi-v-uṟūu (செவி-ய்-உரை) are of the same nature, i.e., they are not composed in kalippā (கலிப்பா) or vañcippā (வனிசிப்பா)."
            }
          },
          {
            "paadal": "அவையடக்கியலே அரில் தபத் தெரியின் \nவல்லா கூறினும் வகுத்தனர் கொண்மின் என்று \nஎல்லா மாந்தர்க்கும் வழி மொழிந்தன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vāyuṟai-vāḻttḻ (வாயுரை-வால்ட்டு), Avai-y-aṭakkū (அவை-ஒய்-அடக்கு) and Cevi-y-aṟi-v-uṟūu (செவி-ய்-உரை)",
              "paadal_meaning": "Avai-y-aṭakku (அவை-ய்-அடக்கு) is, if well examined, one's modest expression to all to discriminate what is good in his unworthy sayings and take it."
            }
          },
          {
            "paadal": "செவியுறைதானே, \nபொங்குதல் இன்றி புரையோர் நாப்பண் \nஅவிதல் கடன் எனச் செவியுறுத்தன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vāyuṟai-vāḻttḻ (வாயுரை-வால்ட்டு), Avai-y-aṭakkū (அவை-ஒய்-அடக்கு) and Cevi-y-aṟi-v-uṟūu (செவி-ய்-உரை)",
              "paadal_meaning": "Cevi-y-uṟai (செவி-ய்-உரை) is that which is brought to the ear of one whd stands in submission without assuming superior airs in the midst of learned men,"
            }
          },
          {
            "paadal": "ஒத்தாழிசையும் மண்டில யாப்பும் \nகுட்டமும் நேரடிக்கு ஒட்டின என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Nēraṭi (நேரடி)",
              "paadal_meaning": "They say that ottāḻicai (ஒட்டலிசை), a limb of kalippā (கலிப்பா), maṇṭila-yāppu (மந்திலா-யாப்பு) of āciriyappā (ஆசிரியப்பா) and kuṭṭam (குட்டம்), another limb of kalippā (கலிப்பா). have their feet consisting of four cīrs (சீர்)."
            }
          },
          {
            "paadal": "குட்டம் எருத்தடி உடைத்தும் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Taravu (தரவு)",
              "paadal_meaning": "Kuṭṭam (குட்டம்) may have its penultimate (இறுதியான) foot (having three cīrs (சீர்))."
            }
          },
          {
            "paadal": "மண்டிலம் குட்டம் என்று இவை இரண்டும் \nசெந்தூக்கு இயல என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Maṇṭilam (மந்திலம்) and Kuṭṭam (குட்டம்)",
              "paadal_meaning": "Learned men say that the above mentioned two maṇṭilam (மந்திலம்) and kuṭṭam (குட்டம்) are of the nature of certūkkū (செர்டக்கு) i.e. they have akaval-ōcai (அகவல்-ஓகை)."
            }
          },
          {
            "paadal": "நெடுவெண்பாட்டே குறுவெண்பாட்டே \nகைக்கிளை பரிபாட்டு அங்கதச் செய்யுளொடு \nஒத்தவை எல்லாம் வெண்பா யாப்பின.",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā (வெண்பா) Metre",
              "paadal_meaning": "Neṭu-veṇpāṭṭū (நெடுவெண்பாட்டு), kuṟu-veṇpāṭṭu (குறுவெண்பட்டி), kaikkiḷai (கைக்கிளை), paripāṭṭū (பரிபாட்டு), and aṅkatam (அங்கதம்) have the yāppū (வெண்பா) of Veṇpā (யாப்பு)."
            }
          },
          {
            "paadal": "கைக்கிளைதானே வெண்பா ஆகி \nஆசிரிய இயலான் முடியவும் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Kaikkiḷai (கைக்கிளை)",
              "paadal_meaning": "Kaikkiḷai (கைக்கிளை) may have the first two feet like veṇpā (வெண்பா) and the last two feet like āciriyappā (ஆசிரியப்பா)."
            }
          },
          {
            "paadal": "பரிபாடல்லே தொகை நிலை வகையின் \nஇது பா என்னும் இயல் நெறி இன்றி \nபொதுவாய் நிற்றற்கும் உரித்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Paripāṭal (பரிபாடல்)",
              "paadal_meaning": "They say that paripāṭal (பரிபாடல்) has no metre of its own, but may be composed in all metres."
            }
          },
          {
            "paadal": "கொச்சகம் அராகம் சுரிதகம் எருத்தொடு \nசெப்பிய நான்கும் தனக்கு உறுப்பு ஆக \nகாமம் கண்ணிய நிலைமைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Paripāṭal (பரிபாடல்)",
              "paadal_meaning": "Paripāṭal (பரிபாடல்) has the following four limbs: Koccakam (கொச்சகம்), arākam (அர்ட்கம்), curitakam (குறிதகம்), and eruttū (எருட்டு)."
            }
          },
          {
            "paadal": "சொற்சீர் அடியும் முடுகியல் அடியும் \nஅப் பா நிலைமைக்கு உரிய ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Paripāṭal (பரிபாடல்)",
              "paadal_meaning": "Paripāṭal (பரிபாடல்) may have coṟ-cīr-aṭi (சொற்-சீர்-அடி) and muṭukiyal-aṭi (முடுகியல்-அடி)."
            }
          },
          {
            "paadal": "கட்டுரை வகையான் எண்ணொடு புணர்ந்தும் \nமுட்டடி இன்றிக் குறைவு சீர்த்து ஆகியும் \nமொழி அசை ஆகியும் வழி அசை புணர்ந்தும் \nசொற்சீர்த்து இறுதல் சொற்சீர்க்கு இயல்பே.",
            "vilakkam": 
            {
              "paadal_category": "Coṟ-cīr-aṭi (சொற்-சீர்-அடி)",
              "paadal_meaning": "The nature of coṟ-cīr-aṭi (சொற்-சீர்-அடி) is that it may be in the form of prose, it may consist of one or two feet, it may have the final cīr (சீர்) defective by one or two acais (அசை) and it may have an acai (அசை) standing in place of a cīr (சீர்) or a word standing in place of a cīr (சீர்)."
            }
          },
          {
            "paadal": "அங்கதம்தானே அரில் தபத் தெரியின் \nசெம்பொருள் கரந்தது என இரு வகைத்தே.",
            "vilakkam": 
            {
              "paadal_category": "Aṅkatam (அங்கதம்)",
              "paadal_meaning": "Aṅkatam (அங்கதம்) (satirical stanza), if carefully examined, is of two kinds: Cemporuḷ (செம்பொருள்) and karantatū (கரந்தது)."
            }
          },
          {
            "paadal": "செம்பொருள் ஆயின வசை எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Aṅkatam (அங்கதம்)",
              "paadal_meaning": "Aṅkatam (அங்கதம்) of the kind of cemporuḷ (செம்பொருள்) is called vacai (வசை)."
            }
          },
          {
            "paadal": "மொழி கரந்து மொழியின் அது பழிகரப்பு ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Aṅkatam (அங்கதம்)",
              "paadal_meaning": "If the idea is not directly expressed in aṅkatam (அங்கதம்) but is suggested, it is called paḻi-karappū (பாலி-கரப்பு)."
            }
          },
          {
            "paadal": "செய்யுள்தாமே இரண்டு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Composition",
              "paadal_meaning": "They say that ceyyuḷ (செய்யுள்) (stanza) is of two kinds."
            }
          },
          {
            "paadal": "புகழொடும் பொருளொடும் புணர்ந்தன்று ஆயின் \nசெவியுறைச் செய்யுள் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Composition",
              "paadal_meaning": "If it deals with the fame or aṟam (அறம்), poruḷ (பொருள்) and iṉpam (இன்பம்), it is called ceviyuḷai-c-ceyyuḷ (செவியுரை-சி-செய்யுள்)."
            }
          },
          {
            "paadal": "வசையொடும் நசையொடும் புணர்ந்தன்று ஆயின் \nஅங்கதச் செய்யுள் என்மனார் புலவர். ",
            "vilakkam": 
            {
              "paadal_category": "Modes of Composition",
              "paadal_meaning": "Learned men say that the stanza of satire and mockery is called aṅkatam (அங்கதம்)."
            }
          },
          {
            "paadal": "ஒத்தாழிசைக்கலி கலிவெண்பாட்டே \nகொச்சகம் உறழொடு கலி நால் வகைத்தே. ",
            "vilakkam": 
            {
              "paadal_category": "Kinds of Kalippā (கலிப்பா)",
              "paadal_meaning": "Kali (காளி) is of four kinds: ottāḻicai-k-kali (ஒட்டலிசை-க்-களி), kali-veṇ-pāttū (கலி-வெண்-பாட்டு),koccakam (கொச்சகம்) and uṟaḻ-kali (உரல்-களி)."
            }
          },
          {
            "paadal": "அவற்றுள், \nஒத்தாழிசைக்கலி இரு வகைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "Of them ottāḻicaikkali (ஒட்டலிசைக்கலி) is of two kinds."
            }
          },
          {
            "paadal": "இடைநிலைப்பாட்டே தரவு போக்கு அடை என \nநடை நவின்று ஒழுகும் ஒன்று என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "One of them has the following four limbs: iṭai-nilai-p-pāṭṭu (இடை-நிலை-ப்-பட்டு), taravu (தரவு), pōkkū (போக்கு) and aṭai (அடை)."
            }
          },
          {
            "paadal": "தரவேதானும் நால் அடி இழிபு ஆய் \nஆறு இரண்டு உயர்வும் பிறவும் பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "Taravu (தாராவு) has four feet for the minimum and twelve feei for the maximum."
            }
          },
          {
            "paadal": "இடைநிலைப்பாட்டே, \nதரவு அகப்பட்ட மரபினது என்ப.",
            "vilakkam": 
            {
              "paadal_category": "ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "They say that tāḻici (தாலிசி) has its feet less than taravu (தாராவு)."
            }
          },
          {
            "paadal": "அடை நிலைக் கிளவி தாழிசைப் பின்னர் \nநடை நவின்று ஒழுகும் ஆங்கு என் கிளவி.",
            "vilakkam": 
            {
              "paadal_category": "ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "They say that aṭai-nilai-k-kiḷavi (அடை-நிலை-க்-கிளவி) appears after tāḻicai (தாலிசி)."
            }
          },
          {
            "paadal": "போக்கு இயல் வகையே வைப்பு எனப்படுமே \nதரவு இயல் ஒத்தும் அதன் அகப்படுமே \nபுரை தீர் இறுதி நிலை உரைத்தன்றே. ",
            "vilakkam": 
            {
              "paadal_category": "ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "Pōkkū (போக்கு) is otherwise called vaippū (வைப்பு) and its feet are the same as in taravu (தரவு) or less and it forms the spotless concluding portion of the stanza."
            }
          },
          {
            "paadal": "ஏனை ஒன்றே, \nதேவர்ப் பராஅய முன்னிலைக்கண்ணே. ",
            "vilakkam": 
            {
              "paadal_category": "ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "The other kind of ottāḻicai-k-kali (ஒட்டலிசை-க்-காளி) is used to extol gods in person."
            }
          },
          {
            "paadal": "அதுவே, \nவண்ணகம் ஒருபோகு என இரு வகைத்தே.",
            "vilakkam": 
            {
              "paadal_category": "ottāḻicaikkali (ஒட்டலிசைக்கலி)",
              "paadal_meaning": "It is'of two kinds: Vaṇṇakam (வண்ணகம்) and orupōkū (ஒருபோகு) ."
            }
          },
          {
            "paadal": "வண்ணகம்தானே, \nதரவே தாழிசை எண்ணே வாரம் என்று \nஅந் நால் வகையின் தோன்றும் என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Vannaka Ottalicaikkali",
              "paadal_meaning": "They say that Vaṇṇakam (வண்ணகம்) has the following four limbs— taravu (தரவு), tāḻicai (தளிசை), eṇ (எண்) and vāram (வரம்)."
            }
          },
          {
            "paadal": "தரவேதானும், \nநான்கும் ஆறும் எட்டும் என்ற \nநேரடி பற்றிய நிலைமைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vannaka Ottalicaikkali",
              "paadal_meaning": "The taravu (தரவு) of vaṇṇaka-v-ottāḻicai (வண்ணக-வி-ஒட்டாலிசை) has four, six or eight feet, each having four cīrs (சீர்)."
            }
          },
          {
            "paadal": "ஒத்து மூன்று ஆகும் ஒத்தாழிசையே \nதரவின் சுருங்கித் தோன்றும் என்ப. ",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇaka Ottāḻicaikkali (வண்ணக-வி-ஒட்டாலிசை)",
              "paadal_meaning": "They say that ottāḻicai (ஒட்டலிசை) will be of lesser length than taravu (தரவு) and may consist of three feet of equal length."
            }
          },
          {
            "paadal": "அடக்கு இயல் வாரம் தரவொடு ஒக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇaka Ottāḻicaikkali (வண்ணக-வி-ஒட்டாலிசை)",
              "paadal_meaning": "The vāram (வரம்) otherwise known as aṭakkiyal (அடக்கியல்) is similar to taravu (தரவு )."
            }
          },
          {
            "paadal": "முதல் தொடை பெருகிச் சுருங்குமன் எண்ணே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇaka Ottāḻicaikkali (வண்ணக-வி-ஒட்டாலிசை)",
              "paadal_meaning": "Eṇ (எண்) is that where the ṭoṭai (தொடை) will gradually diminish in length."
            }
          },
          {
            "paadal": "எண் இடை ஒழிதல் ஏதம் இன்றே \nசின்னம் அல்லாக் காலையான.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇaka Ottāḻicaikkali (வண்ணக-வி-ஒட்டாலிசை)",
              "paadal_meaning": "There is no harm if the limb eṇ (எண்) is not found in the absence of taṉi-c-col (தனி-சி-கோல்)."
            }
          },
          {
            "paadal": "ஒருபோகு இயற்கையும் இரு வகைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Orupōkū (ஒருபோகு)",
              "paadal_meaning": "Orupōkū (ஒருபோகு) also is of two kinds."
            }
          },
          {
            "paadal": "கொச்சக ஒருபோகு அம்போதரங்கம் என்று \nஒப்ப நாடி உணர்தல் வேண்டும்.",
            "vilakkam": 
            {
              "paadal_category": "Orupōkū (ஒருபோகு)",
              "paadal_meaning": "One should understand that they are koccaka-v-orupōkū (கொச்சக-வி-ஒருபோகு) and ampōtaraṅkam (அம்போதரங்கம்) ."
            }
          },
          {
            "paadal": "தரவு இன்று ஆகித் தாழிசை பெற்றும் \nதாழிசை இன்றித் தரவு உடைத்து ஆகியும் \nஎண் இடை இட்டுச் சின்னம் குன்றியும் \nஅடக்கியல் இன்றி அடி நிமிர்ந்து ஒழுகியும் \nயாப்பினும் பொருளினும் வேற்றுமை உடையது \nகொச்சக ஒருபோகு ஆகும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Koccaka-v-orupōkū (கொச்சக-வி-ஒருபோகு)",
              "paadal_meaning": "koccaka-v-orupōkū (கொச்சக-வி-ஒருபோகு) may have all the limbs deficient in taravu (தரவு), tāḻicai (தளிசை), taṉiccol (தனிச்சொல்) or curitakam (குறிதகம்) and may vary in yāppū (யாப்பும்) and pōruḷ (பொருள்))."
            }
          },
          {
            "paadal": "ஒருபான் சிறுமை இரட்டி அதன் உயர்பே.",
            "vilakkam": 
            {
              "paadal_category": "Koccaka-v-orupōkū (கொச்சக-வி-ஒருபோகுKoccaka Orupoku",
              "paadal_meaning": "Its feet vary from ten to twenty."
            }
          },
          {
            "paadal": "அம்போதரங்கம் அறுபதிற்று அடித்தே \nசெம்பால் வாரம் சிறுமைக்கு எல்லை. ",
            "vilakkam": 
            {
              "paadal_category": "Ampōtaraṅkam (அம்போதரங்கம்)",
              "paadal_meaning": "Ampōtaraṅkam (அம்போதரங்கம்) varies its feet from sixty to thirty."
            }
          },
          {
            "paadal": "எருத்தே கொச்சகம் அராகம் சிற்றெண் \nஅடக்கியல் வாரமொடு அந் நிலைக்கு உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Ampōtaraṅkam (அம்போதரங்கம்)",
              "paadal_meaning": "Taravu (தாராவு), koccakam (கொச்சகம்), arākam (அர்ட்கம்), ciṟṟen (சிர்ரென்) and aṭakkiyal-vāram (அடக்கியல்-வரம்) are its limbs."
            }
          },
          {
            "paadal": "ஒரு பொருள் நுதலிய வெள்ளடி இயலான் \nதிரிபு இன்றி வருவது கலிவெண்பாட்டே.",
            "vilakkam": 
            {
              "paadal_category": "Kali-veṇ-pāttu (கலி-வெண்-பட்டு)",
              "paadal_meaning": "Kali-veṇ-pāttu (கலி-வெண்-பட்டு) deals with one topic and has all the feet veḷḷati (வெள்ளட்டி) (those pertaining to veṉpā (வெண்பா))"
            }
          },
          {
            "paadal": "தரவும் போக்கும் பாட்டு இடை மிடைந்தும் \nஐஞ் சீர் அடுக்கியும் ஆறு மெய் பெற்றும் \nவெண்பா இயலான் வெளிப்படத் தோன்றும் \nபாநிலை வகையே கொச்சகக் கலி என \nநூல் நவில் புலவர் நுவன்று அறைந்தனரே.",
            "vilakkam": 
            {
              "paadal_category": "Koccaka-k-kali (கொச்சக-க்-காளி)",
              "paadal_meaning": "Scholars of literature have said that koccaka-k-kali (கொச்சக-க்-காளி)  may have taravu (தாராவு) and pōkku (போக்கு) in the middle, may have its feet consisting of five cīrs (சீர்), may have six limbs and may have the nature of veṇpā (வெண்பா)."
            }
          },
          {
            "paadal": "கூற்றும் மாற்றமும் இடை இடை மிடைந்தும் \nபோக்கு இன்றாகல் உறழ்கலிக்கு இயல்பே.",
            "vilakkam": 
            {
              "paadal_category": "Uṟaḻ-kali (உரல்-களி)",
              "paadal_meaning": "There is no harm if uṟaḻ-kali (உரல்-களி) has within it one's speech and another's reply."
            }
          },
          {
            "paadal": "ஆசிரியப் பாட்டின் அளவிற்கு எல்லை \nஆயிரம் ஆகும் இழிபு மூன்று அடியே.",
            "vilakkam": 
            {
              "paadal_category": "āciriyappā (ஆசிரியப்பா)",
              "paadal_meaning": "The limit of the extent of āciriyappā (ஆசிரியப்பா) ranges from thousand to three feet."
            }
          },
          {
            "paadal": "நெடுவெண்பாட்டே முந் நால் அடித்தே \nகுறுவெண்பாட்டின் அளவு எழு சீரே. ",
            "vilakkam": 
            {
              "paadal_category": "Veṇpā (வெண்பா)",
              "paadal_meaning": "Netu-veṇpā (நெடு-வெண்பா) may have twelve feet and kuṟu-veṇpā (குறுவெண்பா) has seven cīrs(சீர்)."
            }
          },
          {
            "paadal": "அங்கதப் பாட்டு அளவு அவற்றொடு ஒக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Aṅkatam (அங்கதம்)",
              "paadal_meaning": "The range of aṅkatappāttū (அங்கதப்பட்டு) is similar to them, i.e., the outer range is twelve feet and the inner range is two feet."
            }
          },
          {
            "paadal": "கலிவெண்பாட்டே கைக்கிளைச் செய்யுள் \nசெவியறி வாயுறை புறநிலை என்று இவை \nதொகு நிலை மரபின் அடி இல என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes",
              "paadal_meaning": "Kali-veṇ-pāṭṭū (கலி -வெண்-பிடியு) and stanzas dealing with kaikkiḷai (கைக்கிளை), cevi-y- aṟi (செவி-அறி), vāyuṟai (வாயுரை), and puṟanilai (புறநிலை) have no limit in their range, i.e., they may have any number of feet."
            }
          },
          {
            "paadal": "புறநிலை வாயுறை செவியறிவுறூஉ எனத் \nதிறநிலை மூன்றும் திண்ணிதின் தெரியின் \nவெண்பா இயலினும் ஆசிரிய இயலினும் \nபண்புற முடியும் பாவின என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Other Classes",
              "paadal_meaning": "Puṟanilai (புடநிலை), vāyuṟai (வாயுரை) and cevi-y-aṟivuṟūu (செவி-அறிவுறு), all these three, are, on  examination, composed in maruṭpā (மருட்பா) (āciriyappā (ஆசிரியப்பா) followed by veṇpā (வெண்பா)).  "
            }
          },
          {
            "paadal": "பரிபாடல்லே, \nநால் ஈர் ஐம்பது உயர்பு அடி ஆக \nஐ ஐந்து ஆகும் இழிபு அடிக்கு எல்லை.",
            "vilakkam": 
            {
              "paadal_category": "Paripāṭal (பரிபாடல்)",
              "paadal_meaning": "The range of Paripāṭal (பரிபாடல்) is from twenty-five to four hundred feet."
            }
          },
          {
            "paadal": "அளவியல் வகையே அனை வகைப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Paripāṭal (பரிபாடல்)",
              "paadal_meaning": "The classification of aḷaviyal (அலவியல்) is of the sort mentioned above."
            }
          },
          {
            "paadal": "எழு நிலத்து எழுந்த செய்யுள் தெரியின் \nஅடி வரை இல்லன ஆறு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Compositions of Unrestricted Line Limits",
              "paadal_meaning": "Of the stanzas in the seven kinds of poetry, six are not limited in extent, i,e. t there is no restriction of feet."
            }
          },
          {
            "paadal": "அவைதாம், \nநூலினான உரையினான \nநொடியொடு புணர்ந்த பிசியினான \nஏது நுதலிய முதுமொழியான \nமறை மொழி கிளந்த மந்திரத்தான \nகூற்று இடை வைத்த குறிப்பினான.",
            "vilakkam": 
            {
              "paadal_category": "Compositions of Unrestricted Line Limits",
              "paadal_meaning": "They are in nūḷ (நூல்), urai (உறை), pici (பிசி)(riddle couched in words), mutumoḻi (முதுமொழி) (proverbs supported by reasons), mantras (மந்திரங்கள்) and in suggestive poems."
            }
          },
          {
            "paadal": "அவற்றுள், \nநூல் எனப்படுவது நுவலும் காலை \nமுதலும் முடிவும் மாறுகோள் இன்றி \nதொகையினும் வகையினும் பொருண்மை காட்டி \nஉள் நின்று அகன்ற உரையொடு புணர்ந்து \nநுண்ணிதின் விளக்கல் அது அதன் பண்பே.",
            "vilakkam": 
            {
              "paadal_category": "Nūḷ (நூல்)",
              "paadal_meaning": "Of them, nūḷ (நூல்) is that wherein a topic is dealt with from beginning to end without impropriety, sometimes concisely and sometimes in detail, full of suggestions clearly seen."
            }
          },
          {
            "paadal": "அதுவேதானும் ஒரு நால் வகைத்தே.",
            "vilakkam": 
            {
              "paadal_category": "Nūḷ (நூல்)",
              "paadal_meaning": "It consists of four parts."
            }
          },
          {
            "paadal": "ஒரு பொருள் நுதலிய சூத்திரத்தானும் \nஇன மொழி கிளந்த ஓத்தினானும் \nபொது மொழி கிளந்த படலத்தானும் \nமூன்று உறுப்பு அடக்கிய பிண்டத்தானும் என்று \nஆங்கு அனை மரபின் இயலும் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Nūḷ (நூல்)",
              "paadal_meaning": "They say that nūḷ (நூள்)  consists of sūtras dealing with one idea, ōttū (ஓத்தூ) (chapter) dealing with one minor topic, paṭalam (படலம்) (section) dealing with one major topic and Piṇṭam (பிண்டம்) consisting of all or any of the three mentioned above."
            }
          },
          {
            "paadal": "அவற்றுள், \nசூத்திரம்தானே \nஆடி நிழலின் அறியத் தோன்றி \nநாடுதல் இன்றிப் பொருள் நனி விளங்க \nயாப்பினுள் தோன்ற யாத்து அமைப்பதுவே.",
            "vilakkam": 
            {
              "paadal_category": "Cūttiram (சூத்திரம்)",
              "paadal_meaning": "Of them sūtras is a verse whose meaning is so clear as the image in a metallic mirror that it can be understood without serious thinking."
            }
          },
          {
            "paadal": "நேர் இன மணியை நிரல்பட வைத்தாங்கு \nஓர் இனப் பொருளை ஒரு வழி வைப்பது \nஓத்து என மொழிப உயர் மொழிப் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "ōttū (ஓட்டு)",
              "paadal_meaning": "Scholars of refined tongue say that, of them, ōttū (ஓட்டு) is the collection of sūtras () dealing with the same topic in a beautiful order like gems of the same kind in a garland."
            }
          },
          {
            "paadal": "ஒரு நெறி இன்றி விரவிய பொருளான் \nபொது மொழி தொடரின் அது படலம் ஆகும். ",
            "vilakkam": 
            {
              "paadal_category": "Paṭalam (படலம்)",
              "paadal_meaning": "Of them, paṭalam (படலம்) is a section of a major topic which consists of chapters dealing with diverse topics under the same."
            }
          },
          {
            "paadal": "மூன்று உறுப்பு அடக்கிய தன்மைத்து ஆயின் \nதோன்று மொழிப் புலவர் அது பிண்டம் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Piṇṭam (பிண்டம்)",
              "paadal_meaning": "Scholars of current literature say that piṇṭam (பிண்டம்) may have all the three— sūtra, ōttu (ஓத்து) and paṭalam (படலம்), or sūtra alone or sūtra and ōttū (ஓத்து) alone."
            }
          },
          {
            "paadal": "பாட்டு இடை வைத்த குறிப்பினானும் \nபா இன்று எழுந்த கிளவியானும் \nபொருள் மரபு இல்லாப் பொய்ம்மொழியானும் \nபொருளொடு புணர்ந்த நகைமொழியானும் என்று \nஉரை வகை நடையே நான்கு என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Urai (உறை)",
              "paadal_meaning": "The course of urai (உறை), they say, is of four kinds;—the connecting link in the middle of a verse, the commentary in the form of prose, fabulous sayings and sayings creating laughter."
            }
          },
          {
            "paadal": "அதுவேதானும் இரு வகைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Urai (உறை)",
              "paadal_meaning": "It is of two kinds."
            }
          },
          {
            "paadal": "ஒன்றே மற்றும் செவிலிக்கு உரித்தே \nஒன்றே யார்க்கும் வரை நிலை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Urai (உறை)",
              "paadal_meaning": "One is within the province of cevili (செவிலி) and the other, all are not forbidden, to make use of."
            }
          },
          {
            "paadal": "ஒப்பொடு புணர்ந்த உவமத்தானும் \nதோன்றுவது கிளந்த துணிவினானும் \nஎன்று இரு வகைத்தே பிசி நிலை வகையே.",
            "vilakkam": 
            {
              "paadal_category": "Pici (பிசி)",
              "paadal_meaning": "Riddle is of two kinds: one that is suggested through the point of comparison and the other that is suggested through tradition."
            }
          },
          {
            "paadal": "நுண்மையும் சுருக்கமும் ஒளியுடைமையும் \nஎண்மையும் என்று இவை விளங்கத் தோன்றி \nகுறித்த பொருளை முடித்தற்கு வரூஉம் \nஏது நுதலிய முதுமொழி என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Mutu-moḻi (முடு மொழி)",
              "paadal_meaning": "They say that mutu-moḻi (முடு மொழி) (proverb) intended to suggest the reason of the desired object is couched in elegant, short, bristling and tender expressions."
            }
          },
          {
            "paadal": "நிறைமொழி மாந்தர் ஆணையின் கிளக்கும் \nமறைமொழிதானே மந்திரம் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Mantra (மந்திரம்)",
              "paadal_meaning": "They say that mantra (மந்திரம்) whose meaning is not explicit is the production of the mind of seers whose words never fail to have its effect."
            }
          },
          {
            "paadal": "எழுத்தொடும் சொல்லொடும் புணராதாகி \nபொருட்புறத்ததுவே குறிப்பு மொழியே. ",
            "vilakkam": 
            {
              "paadal_category": "Kuṟippu (குறிப்பு)",
              "paadal_meaning": "Kuṟippu-moḻi (குறிப்பு-மொழி) is that which suggests a meaning outside the range of the literal meaning of the words."
            }
          },
          {
            "paadal": "பாட்டிடைக் கலந்த பொருள ஆகி \nபாட்டின் இயல பண்ணத்திய்யே.",
            "vilakkam": 
            {
              "paadal_category": "Paṇṇatti (பண்ணட்டி)",
              "paadal_meaning": "Paṇṇatti (பண்ணட்டி) is that which is in the form of a pāṭṭu (பட்டு) which is  capable of being sung."
            }
          },
          {
            "paadal": "அதுவேதானும் பிசியொடு மானும்.",
            "vilakkam": 
            {
              "paadal_category": "Paṇṇatti (பண்ணட்டி)",
              "paadal_meaning": "It has the same number of feet as pici (பிசி)."
            }
          },
          {
            "paadal": "அடி நிமிர் கிளவி ஈர் ஆறு ஆகும் \nஅடி இகந்து வரினும் கடி வரை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Paṇṇatti (பண்ணட்டி)",
              "paadal_meaning": "The number of feet of paṇṇatti (பண்ணட்டி) is of twelve kinds:— four, five, six etc.It is not prohibited if the number of feet exceeds them."
            }
          },
          {
            "paadal": "கிளர் இயல் வகையின் கிளந்தன தெரியின் \nஅளவியல் வகையே அனை வகைப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Paṇṇatti (பண்ணட்டி)",
              "paadal_meaning": "The classification of aḷaviyal (அலவியல்) is of so many kinds if it is examined on the lines of those mentioned above."
            }
          },
          {
            "paadal": "கைக்கிளை முதலா ஏழ் பெருந் திணையும் \nமுன் கிளந்தனவே முறையினான. ",
            "vilakkam": 
            {
              "paadal_category": "tiṇai (திணை) ",
              "paadal_meaning": "The seven major tiṇais (திணை) commencing with kaikkiḷai (கைக்கிளை) have already been described in their order."
            }
          },
          {
            "paadal": "காமப் புணர்ச்சியும் இடம் தலைப்படலும் \nபாங்கொடு தழாஅலும் தோழியின் புணர்வும் என்று \nஆங்க நால் வகையினும் அடைந்த சார்பொடு \nமறை என மொழிதல் மறையோர் ஆறே.",
            "vilakkam": 
            {
              "paadal_category": "Kaḷavu (கலவு)",
              "paadal_meaning": "The way of sages well-versed in Vedas (வேதங்கள்) is to say that kalavu (களவு) consists of meeting through love, obstacles on the way, winning the help of a friend by the hero and meeting the lady through the help of lady's friend."
            }
          },
          {
            "paadal": "மறை வெளிப்படுதலும் தமரின் பெறுதலும் \nஇவை முதலாகிய இயல் நெறி திரியாது \nமலிவும் புலவியும் ஊடலும் உணர்வும் \nபிரிவொடு புணர்ந்தது கற்பு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Kaṟpū (கற்பு)",
              "paadal_meaning": "Kaḷavu (கலவு) becoming known to all, winning the lady's hand through her relatives, enjoying according to human nature, pleasure, conjugal union, love-quarrel, and its end and separation fall under kaṟpū (கற்பு)."        
            }
          },
          {
            "paadal": "மெய் பெறும் அவையே கைகோள் வகையே.",
            "vilakkam": 
            {
              "paadal_category": "Kaṟpū (கற்பு)",
              "paadal_meaning": "Those two kaḷavu (களவு) and kaṟpū (கற்பு) form kaikōḷ (கைகோல்)."
            }
          },
          {
            "paadal": "பார்ப்பான் பாங்கன் தோழி செவிலி \nசீர்த்தகு சிறப்பின் கிழவன் கிழத்தியொடு \nஅளவு இயல் மரபின் அறு வகையோரும் \nகளவின் கிளவிக்கு உரியர் என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Characters in Kaḷavu (கலவு)",
              "paadal_meaning": "They say that traditionally the following six are qualified to speak during kaḷavu (களவு):—Brahman, lover's friend, lady's friend, foster mother, the lover and the lady-love, of whom the last two are evidently very prominent."
            }
          },
          {
            "paadal": "பாணன் கூத்தன் விறலி பரத்தை \nஆணம் சான்ற அறிவர் கண்டோர் \nபேணுதகு சிறப்பின் பார்ப்பான் முதலா \nமுன்னுறக் கிளந்த அறுவரொடு தொகைஇ \nதொல் நெறி மரபின் கற்பிற்கு உரியர்.",
            "vilakkam": 
            {
              "paadal_category": "Characters in Karpu",
              "paadal_meaning": "The following six along with the six mentioned above beginning with Brahman worthy of company, form, from tradition, the speakers in kaṟpū (கற்பு):— pāṇaṉ (பாணன்), kūttaṉ (கூத்தன்), viṟali (விறலி), courtezan (குற்றாலம்), learned men and passers-by attached to the lover and the lady."
            }
          },
          {
            "paadal": "ஊரும் அயலும் சேரியோரும் \nநோய் மருங்கு அறிநரும் தந்தையும் தன்னையும் \nகொண்டெடுத்து மொழியப்படுதல் அல்லது \nகூற்று அவண் இன்மை யாப்புறத் தோன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "Characters with No Direct Utterances",
              "paadal_meaning": "The villagers, neighbours, the residents of the street, those who are in the know of the different stages of lovesickness and the father and the elder brother of the lady do not have their say directly in literature and it is reported by one other than they."
            }
          },
          {
            "paadal": "கிழவன்தன்னொடும் கிழத்திதன்னொடும் \nநற்றாய் கூறல் முற்றத் தோன்றாது. ",
            "vilakkam": 
            {
              "paadal_category": "Utterance by Mother",
              "paadal_meaning": "The mother of the lady-love never has her say either with the lover or the lady."
            }
          },
          {
            "paadal": "ஒண் தொடி மாதர் கிழவன் கிழத்தியொடு \nகண்டோ ர் மொழிதல் கண்டது என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Utterance by the Passers-by",
              "paadal_meaning": "They say that passers-by have their say with women furnished with fine ornaments, the lover and the lady-love."
            }
          },
          {
            "paadal": "இடைச் சுரமருங்கின் கிழவன் கிழத்தியொடு \nவழக்கியல் ஆணையின் கிளத்தற்கும் உரியன்.",
            "vilakkam": 
            {
              "paadal_category": "Hero's Utterance to Heroine during Elopement",
              "paadal_meaning": "The lover may, according to tradition, have his say towards the lady-love in the middle of the desert."
            }
          },
          {
            "paadal": "ஒழிந்தோர் கிளவி கிழவன் கிழத்தியொடு \nமொழிந்தாங்கு உரியர் முன்னத்தின் எடுத்தே.",
            "vilakkam": 
            {
              "paadal_category": "Hero and Heroine vis-à-vis Other Characters",
              "paadal_meaning": "All other than the lover and the lady-love have their say towards the lover or the lady-love or both according to the etiquette suited to the time and place."
            }
          },
          {
            "paadal": "மனையோள் கிளவியும் கிழவன் கிளவியும் \nநினையும் காலை கேட்குநர் அவரே.",
            "vilakkam": 
            {
              "paadal_category": "Hero and Heroine vis-à-vis Other Characters",
              "paadal_meaning": "The sayings of the lady and the lover are addressed to them i.e., the ten mentioned above."
            }
          },
          {
            "paadal": "பார்ப்பார் அறிவர் என்று இவர் கிளவி \nயார்க்கும் வரையார் யாப்பொடு புணர்ந்தே.",
            "vilakkam": 
            {
              "paadal_category": "Utterance by the Wise and Brahmins",
              "paadal_meaning": "They do not prohibit the saying of brahmans and scholars in the form of verse addressed to anybody."
            }
          },
          {
            "paadal": "பரத்தை வாயில் என இரு வீற்றும் \nகிழத்தியைச் சுட்டாக் கிளப்புப் பயன் இலவே.",
            "vilakkam": 
            {
              "paadal_category": "Utterances by Prostitutes and Interceders",
              "paadal_meaning": "he sayings of the courtezan and the interceders are of no use, if they are made to be heafd by the lady love."
            }
          },
          {
            "paadal": "வாயில் உசாவே தம்முள் உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Utterances by Prostitutes and Interceders",
              "paadal_meaning": "The deliberation of interceders may be among themselves."
            }
          },
          {
            "paadal": "ஞாயிறு திங்கள் அறிவே நாணே \nகடலே கானல் விலங்கே மரனே \nபுலம்புறு பொழுதே புள்ளே நெஞ்சே \nஅவை அல பிறவும் நுதலிய நெறியான் \nசொல்லுந போலவும் கேட்குந போலவும் \nசொல்லியாங்கு அமையும் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "A Poetic Convention about Utterances",
              "paadal_meaning": "Learned men say that the following, are found in literature as if they express their ideas and listen to the speech of others:—sun, moon, intelligence, sh>ness, sea, mirage, beast, tree, time of soliloquy, bird, mind etc."
            }
          },
          {
            "paadal": "ஒரு நெறிப்பட்டு ஆங்கு ஓர் இயல் முடியும் \nகரும நிகழ்ச்சி இடம் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Iṭaṉ (ஈடன்)",
              "paadal_meaning": "They say that iṭam (இத்தம்) is that wherein an incident pertaining to minor topic within a major topic takes place."
            }
          },
          {
            "paadal": "இறப்பே நிகழ்வே எதிரது என்னும் \nதிறத்தியல் மருங்கின் தெரிந்தனர் உணர \nபொருள் நிகழ்வு உரைப்பது காலம் ஆகும். ",
            "vilakkam": 
            {
              "paadal_category": "Kālam (கலாம்)",
              "paadal_meaning": "Time is that when one is said to happen with reference to the past, the present and the future."
            }
          },
          {
            "paadal": "இது நனி பயக்கும் இதன் மாறு என்னும் \nதொகு நிலைக் கிளவி பயன் எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Payan (பயான்)",
              "paadal_meaning": "If the fact that this will surely result from this, is not expressed in words, it is called payan (பயான்)."
            }
          },
          {
            "paadal": "உய்த்துணர்வு இன்றி தலைவரு பொருண்மையின் \nமெய்ப் பட முடிப்பது மெய்ப்பாடு ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Meyppāṭū (மெய்ப்பாடு)",
              "paadal_meaning": "If the description of an object is so vivid that one can enjoy it with hair bristling, eyes shedding tears etc. it is called meyppāṭū (மெய்ப்பாடு)."
            }
          },
          {
            "paadal": "எண் வகை இயல் நெறி பிழையாதாகி \nமுன்னுறக் கிளந்த முடிவினது அதுவே.",
            "vilakkam": 
            {
              "paadal_category": "Meyppāṭū (மெய்ப்பாடு)",
              "paadal_meaning": "It is, unfailingly, of eight kinds and is, of the nature mentioned above."
            }
          },
          {
            "paadal": "சொல்லொடும் குறிப்பொடும் முடிவு கொள் இயற்கை \nபுல்லிய கிளவி எச்சம் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Eccam (எக்காம்)",
              "paadal_meaning": "Eccam (எக்காம்) is a stanza whose meaning is completed through some word or suggestion."
            }
          },
          {
            "paadal": "இவ் இடத்து இம் மொழி இவர் இவர்க்கு உரிய என்று \nஅவ் இடத்து அவர் அவர்க்கு உரைப்பது முன்னம்.",
            "vilakkam": 
            {
              "paadal_category": "Muṉṉam (முன்னம்)",
              "paadal_meaning": "Muṉṉam (முன்னம்) is that which indicates the qualified speaker and the qualified person to be spoken to."
            }
          },
          {
            "paadal": "இன்பமும் இடும்பையும் புணர்வும் பிரிவும் \nஒழுக்கமும் என்று இவை இழுக்கு நெறி இன்றி \nஇது ஆகு இத் திணைக்கு உரிப் பொருள் என்னாது \nபொதுவாய் நிற்றல் பொருள் வகை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Porul̥vakai (பொருள்வகை)",
              "paadal_meaning": "They say that porul (பொருள்) is that which is common to all tiṇais (திணை) other than those which are peculiar to particular tiṇai (திணை) and do not trespass the limits which are the source of pleasure and pain, union and separation and right conduct."
            }
          },
          {
            "paadal": "அவ் அம் மக்களும் விலங்கும் அன்றிப் \nபிற அவண் வரினும் திறவதின் நாடி \nதம்தம் இயலின் மரபொடு முடியின் \nஅத் திறம்தானே துறை எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Tuṟai (துறை)",
              "paadal_meaning": "If human beings, beasts etc. peculiar to particular tracts are described in conformity with usage, it is called tuṟai (துறை)."
            }
          },
          {
            "paadal": "அகன்று பொருள் கிடப்பினும் அணுகிய நிலையினும் \nஇயன்று பொருள் முடிய தந்தனர் உணர்த்தல் \nமாட்டு என மொழிப பாட்டியல் வழக்கின்.",
            "vilakkam": 
            {
              "paadal_category": "Māṭṭū (மட்டு)",
              "paadal_meaning": "They say that the mode of construction in verse where words are brought together to suit the meaning whether they are removed from one another or are close to one another."
            }
          },
          {
            "paadal": "மாட்டும் எச்சமும் நாட்டல் இன்றி \nஉடனிலை மொழியினும் தொடர்நிலை பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Toṭarnilai (தொடர்நிலை)",
              "paadal_meaning": "Verse may be composed in such a way as does not need māṭṭū (மட்டு) and eccam (எச்சம்)."
            }
          },
          {
            "paadal": "வண்ணம்தாமே நால் ஐந்து என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "Rhythm , they say, is of twenty kinds."
            }
          },
          {
            "paadal": "அவைதாம், \nபாஅ வண்ணம் தாஅ வண்ணம் \nவல்லிசை வண்ணம் மெல்லிசை வண்ணம் \nஇயைபு வண்ணம் அளபெடை வண்ணம் \nநெடுஞ்சீர் வண்ணம் குறுஞ்சீர் வண்ணம் \nசித்திர வண்ணம் நலிபு வண்ணம் \nஅகப்பாட்டு வண்ணம் புறப்பாட்டு வண்ணம் \nஒழுகு வண்ணம் ஒரூஉ வண்ணம் \nஎண்ணு வண்ணம் அகைப்பு வண்ணம் \nதூங்கல் வண்ணம் ஏந்தல் வண்ணம் \nஉருட்டு வண்ணம் முடுகு வண்ணம் என்று \nஆங்கு என மொழிப அறிந்திசினோரே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "Learned men say that they are paa-vaṇṇam (பா-வண்ணம்), taa-vaṇṇam (தா-வண்ணம்), vallicai-vaṇṇam (வள்ளிசை-வண்ணம்), mellicai-vannam (மெல்லிகை-வண்ணம்), iyaipu-vaṇṇan (இயற்பு-வண்ணம்), alapetai- vaṇṇam (அழபேட்டை- வண்ணம்), netun-cir-vaṇṇam (நெடுன்-சிர்-வண்ணம்), kurun-cir-vaṇṇam (குறுந்-சிர்-வண்ணம்), cittira-vaṇṇam (சித்திர-வண்ணம்வன்னம்), nalipu-vaṇṇam (நலிப்பு-வண்ணம்), akappattu-vaṇṇam (அகப்பாட்டு-வண்ணம்), purappattu-vaṇṇam (புறப்பட்டு- வண்ணம்), oluku-vaṇṇam (ஒழுகு-வண்ணம்), oruu-vaṇṇam (ஒருவு-வண்ணம்), ennu-vaṇṇam (எண்ணு-வண்ணம்), akaippu-vaṇṇam (அகிப்பு-வண்ணம்), tankal-vaṇṇam (தங்கல்-வண்ணம்), ental-vaṇṇam (எந்தல்-வண்ணம்), uruttu-vaṇṇam (உருட்டு-வண்ணம் ) and mutuku - vaṇṇam (முதுகு - வண்ணம்)."
            }
          },
          {
            "paadal": "அவற்றுள், \nபாஅ வண்ணம் \nசொற்சீர்த்து ஆகி நூற்பால் பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "Of them, pāa-vaṇṉam (பா-வண்ணம்) is that where word stands as cīr (சீர்)."
            }
          },
          {
            "paadal": "தாஅ வண்ணம் \nஇடையிட்டு வந்த எதுகைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), tāa vaṇṇam (தா வண்ணம்) is that where etukai is found in alternate feet."
            }
          },
          {
            "paadal": "வல்லிசை வண்ணம் வல்லெழுத்து மிகுமே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them) ,vallicai-vaṇṇam (வல்லிசை-வண்ணம்) is that where voiceless consonants are found in large numbers."
            }
          },
          {
            "paadal": "மெல்லிசை வண்ணம் மெல்லெழுத்து மிகுமே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), mellicai-vaṇṇam (மெல்லிகை-வண்ணம்) is that where nasal consonants preponderate."
            }
          },
          {
            "paadal": "இயைபு வண்ணம் இடையெழுத்து மிகுமே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), iyaipu-vaṇṇam (இயைபு வண்ணம்) is that where semi-vowels preponderate."
            }
          },
          {
            "paadal": "அளபெடை வண்ணம் அளபெடை பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), alapetai-vaṇṇam (அளபெடை வண்ணம்) is that where aḷapeṭais (அளபெடை) (both vocalic and consonantal) are close together."
            }
          },
          {
            "paadal": "நெடுஞ்சீர் வண்ணம் நெட்டெழுத்துப் பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), neṭuñcīr-vaṇṇam (நெடுஞ்சீர் வண்ணம்) is that where long vowels are close together."
            }
          },
          {
            "paadal": "குறுஞ்சீர் வண்ணம் குற்றெழுத்துப் பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), kuṟuñcīr-vaṇṇam (குறுஞ்சீர் வண்ணம்) is that where short vowels are close together."
            }
          },
          {
            "paadal": "சித்திர வண்ணம் \nநெடியவும் குறியவும் நேர்ந்து உடன் வருமே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), cittira-vaṇṇam (சித்திர வண்ணம்) is that where short and long vowels are so used as to produce harmony."
            }
          },
          {
            "paadal": "நலிபு வண்ணம் ஆய்தம் பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), nalipu-vaṇṇam (லிபு வண்ணம்) is that where ay tarn is used."
            }
          },
          {
            "paadal": "அகப்பாட்டு வண்ணம் \nமுடியாத் தன்மையின் முடிந்ததன் மேற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), akappāṭṭu-vaṇṇam (அகப்பாட்டு வண்ணம்) is that in which the final acai (அசை) is different from that which is generally used when the sense is completed."
            }
          },
          {
            "paadal": "புறப்பாட்டு வண்ணம் \nமுடிந்தது போன்று முடியாதாகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), purappāṭṭu-vaṇṇam (புறப்பாட்டு வண்ணம்) is that wherein the acai (அசை) which is generally used when the sense is completed is found even when the sense is not complete."
            }
          },
          {
            "paadal": "ஒழுகு வண்ணம் ஓசையின் ஒழுகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), oḻuku-vaṇṇam (ஒழுகு வண்ணம்) is the rhythm which flows evenly in a pleasing manner."
            }
          },
          {
            "paadal": "ஒரூஉ வண்ணம் ஒரீஇத் தொடுக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), orūu-vaṇṇam (ஒரூஉ வண்ணம்) is that where words flow like the flow of a river."
            }
          },
          {
            "paadal": "எண்ணு வண்ணம் எண்ணுப் பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), eṇṇu-vaṇṇam (எண்ணு வண்ணம்) is that where words and particles denoting number are used."
            }
          },
          {
            "paadal": "அகைப்பு வண்ணம் அறுத்து அறுத்து ஒழுகும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), akaippu-vaṇṇam (அகைப்பு வண்ணம்) is that wherein different kinds of rhythm follow each other."
            }
          },
          {
            "paadal": "தூங்கல் வண்ணம் வஞ்சி பயிலும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), tūṅkal-vaṇṇam (தூங்கல் வண்ணம்) is that which is found in vanci (வஞ்சி) verse."
            }
          },
          {
            "paadal": "ஏந்தல் வண்ணம் \nசொல்லிய சொல்லின் சொல்லியது சிறக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), ēntal-vaṇṇam (ஏந்தல் வண்ணம்) is that where the same word is repeated for emphasis, clearness etc."
            }
          },
          {
            "paadal": "உருட்டு வண்ணம் அராகம் தொடுக்கும்.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), uruṭṭu-vaṇṇam (உருட்டு வண்ணம்) is that wherein ardkant or lines characterised by rapid movement follow each other."
          }
          },
          {
            "paadal": "முடுகு வண்ணம் \nஅடி இறந்து ஓடி அதன் ஓரற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "(Of them), muṭuku-vaṇṇam (முடுகு வண்ணம்) is the rhythm which is effected by mixing lines of short syllables in rapid succession with those of a different type."
            }
          },
          {
            "paadal": "வண்ணம்தாமே இவை என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Vaṇṇam (வண்ணம்) (Verse Rhythm)",
              "paadal_meaning": "They say that vaṇṇam (வண்ணம்) are of the kinds mentioned above. Then the author begins to define the eight commencing with ammai (அம்மை) and ending with iḻaipū (இழைபூ) mentioned at the end of the first sūtra of this chapter"
            }
          },
          {
            "paadal": "வனப்பு இயல்தானே வகுக்கும் காலை \nசில் மென் மொழியான் தாய பனுவலின் \nஅம்மைதானே அடி நிமிர்வு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Vaṉappu (வனப்பு)",
              "paadal_meaning": "Ammai (அம்மை) is that which has not more than five lines made up of cīr (சீர்) composed of minimum words containing nasal sounds."
            }
          },
          {
            "paadal": "செய்யுள் மொழியான் சீர் புனைந்து யாப்பின் \nஅவ் வகைதானே அழகு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Aḻakū (அழகு)",
              "paadal_meaning": "Aḻakū (அழகு) is that which is made up of cīr (சீர்)  containing poetic expressions."
            }
          },
          {
            "paadal": "தொன்மைதானே \nஉரையொடு புணர்ந்த யாப்பின் மேற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Toṉmai (தொன்மை)",
              "paadal_meaning": "Toṉmai (தொன்மை) is that which deals with the incidents of old with explanations here and there."
            }
          },
          {
            "paadal": "இழுமென் மொழியான் விழுமியது நுவலினும் \nபரந்த மொழியான் அடி நிமிர்ந்து ஒழுகினும் \nதோல் என மொழிப தொல் மொழிப் புலவர். ",
            "vilakkam": 
            {
              "paadal_category": "Tōl (தோல்)",
              "paadal_meaning": "Ancient writers say that tol (தோல்) is that which deals with dharma (தர்மம்) , artha (அர்த்த), kāma (காமம்) and mōkṣa (மோட்சம்) in a mellifluous style or that which has more than five feet dealing with the topic in an elaborate way."
            }
          },
          {
            "paadal": "விருந்தேதானும் \nபுதுவது புனைந்த யாப்பின் மேற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Viruntū (விருந்து)",
              "paadal_meaning": "Viruntū (விருந்து) is a composition in a modern style."
            }
          },
          {
            "paadal": "ஞகாரை முதலா ளகாரை ஈற்றுப் \nபுள்ளி இறுதி இயைபு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Iḷaipū (இயப்பு)",
              "paadal_meaning": "It is said that iḷaipū (இயப்பு) is a poetic composition whose lines end in any consonant commencing with ñ (ஞ) and ending with ṉ (ண)."
            }
          },
          {
            "paadal": "சேரி மொழியான் செவ்விதின் கிளந்து \nதேர்தல் வேண்டாது குறித்தது தோன்றின் \nபுலன் என மொழிப புலன் உணர்ந்தோரே.",
            "vilakkam": 
            {
              "paadal_category": "Pulaṉ (புலன்)",
              "paadal_meaning": "Those who are well versed in literature say that pulaṉ (புலன்) is a poetic composition composed of popular words whose meaning is so clear that there is no need for thinking."
            }
          },
          {
            "paadal": "ஒற்றொடு புணர்ந்த வல்லெழுத்து அடங்காது \nகுறளடி முதலா ஐந்து அடி ஒப்பித்து \nஓங்கிய மொழியான் ஆங்கு அவண் மொழியின் \nஇழைபின் இலக்கணம் இயைந்ததாகும்.",
            "vilakkam": 
            {
              "paadal_category": "Iḷaipū (இயப்பு)",
              "paadal_meaning": "The definition of iḷaipū (இயப்பு) is that it is a poetic composition consisting of the five types of aṭi (அதி) from kuṟal-aṭi (குறள்-ஆதி)  onwards which are made up of cir containing long vowels and voiced consonants and avoiding voiceless consonants not followed by vowels."
            }
          },
          {
            "paadal": "செய்யுள் மருங்கின் மெய் பெற நாடி \nஇழைத்த இலக்கணம் பிழைத்தன போல \nவருவ உள எனினும் வந்தவற்று இயலான் \nதிரிபு இன்றி முடித்தல் தெள்ளியோர் கடனே.",
            "vilakkam": 
            {
              "paadal_category": "Poetic Norms and Worldly Conventions",
              "paadal_meaning": "It is the duty of the clear-visioned scholars that, on careful examination, if they find in literature anything not mentioned in the foregoing sutras (சூத்திரம்) of grammar, they should admit it in the fold of the above."
            }
          }
        ]
      },
      {
        "iyal_name": "மரபியல்",
        "iyal_eng":"Coventions in Literature vis-à-vis the Features of the Physical World",
        "noorpa": [
          {
            "paadal": "மாற்ற அருஞ் சிறப்பின் மரபு இயல் கிளப்பின் \nபார்ப்பும் பறழும் குட்டியும் குருளையும் \nகன்றும் பிள்ளையும் மகவும் மறியும் என்று \nஒன்பதும் குழவியொடு இளமைப் பெயரே.",
            "vilakkam": 
           {
            "paadal_category": "Offspring Designations",
            "paadal_meaning": "Marapiyal (மரபியல்) of great superiority commencing, the following nine names are used to denote the young of objects, pārppu (பார்ப்பு) ,paṟal (பறழ்), kuṭṭi (குட்டி) , kuraḷai (குருளை) , kaṉṟū (கன்று), piḷḷai (பிள்ளை) , makavu (மகவு) , maṟi (மறி) and kuḻavi (குழவி)."
            }
           },
          {
            "paadal": "ஏறும் ஏற்றையும் ஒருத்தலும் களிறும் \nசேவும் சேவலும் இரலையும் கலையும் \nமோத்தையும் தகரும் உதளும் அப்பரும் \nபோத்தும் கண்டியும் கடுவனும் பிறவும் \nயாத்த ஆண்பாற் பெயர் என மொழிப.",
            "vilakkam": 
           {
            "paadal_category": "Nouns Denoting Masculine Gender",
            "paadal_meaning": "They say that the following names are used to denote the male of objects, erutū (ஏறும்) , ēṟṟai (ஏற்றை) , oruttal (ஒருத்தல்) , kaḷiṟū (களிறு) , cē (சே) , cēval (சேவல்) , iralai (இரலை), kalai (கலை), mōttai (மோத்தை) , takar (தகர்), utaḷ  (உதள்) , appar (அப்பர்) , pōttū (போத்து) , kanṭi (கண்டி) , kaṭuvaṉ (கடுவன்) etc."
            }
          },
          {
            "paadal": "பேடையும் பெடையும் பெட்டையும் பெண்ணும் \nமூடும் நாகும் கடமையும் அளகும் \nமந்தியும் பாட்டியும் பிணையும் பிணவும் \nஅந்தம் சான்ற பிடியொடு பெண்ணே.",
            "vilakkam":
            {
            "paadal_category": "Nouns Denoting Feminine Gender",
            "paadal_meaning": "The following names denote the female of objects:  pēṭai (பேடை), peṭai (பெடை) , peṭṭai (பெட்டை) , peṇ (பெண்) , mūtu (மூடு), nākū (நாகு), kaṭamai (கடமை) , aḷaku (அளகு) , manti (மந்தி), pāṭṭi (பாட்டி) , piṇai (பிணை) , piṇavu (பிணவு) , piṭi (பிடி) etc."
            }
          },
          {
            "paadal": "அவற்றுள், \nபார்ப்பும் பிள்ளையும் பறப்பவற்று இளமை.",
            "vilakkam": {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Of them, the words pārppū (பார்ப்பு) and piḷḷai (பிள்ளை) are used to denote the young of birds."
            }
          },
          {
            "paadal": "தவழ்பவைதாமும் அவற்று ஓரன்ன.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "The crawling objects too are of the same nature i.e. the above words are used to denote the young of crawling creatures."
            }
          },
          {
            "paadal": "மூங்கா வெருகு எலி மூவரி அணிலொடு \nஆங்கு அவை நான்கும் குட்டிக்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Mūṅkā (மூங்கா) (a kind of mungoose), verukū (வெருகு) (wild cat), rat, and squirrel having three lines take the word kuṭṭi (குட்டி) to denote their young."
            }
          },
          {
            "paadal": "பறழ் எனப்படினும் உறழ் ஆண்டு இல்லை. ",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "There is no harm if the word paṟaḻ (பறழ்) is used to denote the young of the above four."
            }
          },
          {
            "paadal": "நாயே பன்றி புலி முயல் நான்கும் \nஆயும் காலை குருளை என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "They say that, on examination, kuruḷai (குருளை) is the term to denote the young of dog, pig, tiger, and hare."
            }
          },
          {
            "paadal": "நரியும் அற்றே நாடினர் கொளினே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "On examination, the youg of fox too is called the same i.e-, kuruḷai (குருளை)."
            }
          },
          {
            "paadal": "குட்டியும் பறழும் கூற்று அவண் வரையார்.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "They do not prohibit the use of kuṭṭi (குட்டி) and paṟaḻ (பறழ்) with reference to them."
            }
          },
          {
            "paadal": "பிள்ளைப் பெயரும் பிழைப்பு ஆண்டு இல்லை \nகொள்ளும் காலை நாய் அலங்கடையே. ",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "There is no harm if the term piḷḷai (பிள்ளை) is used with reference to them except the dog."
            }
          },
          {
            "paadal": "யாடும் குதிரையும் நவ்வியும் உழையும் \nஓடும் புல்வாய் உளப்பட மறியே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Maṟi (மறி) is the term used to denote the young of the sheep and goat, horse, spotted deer, deer and antelope."
            }
          },
          {
            "paadal": "கோடு வாழ் குரங்கும் குட்டி கூறுப.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "They use kuṭṭi (குட்டி) even with reference to monkeys living in the branches of trees."
            }
          },
          {
            "paadal": "அவையும் அன்ன அப் பாலான.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "The terms makavu (மகவு) , piḷḷai (பிள்ளை), paṟal (பறழ்) , and pārppū (பார்ப்பு) also are used to denote the young of monkeys."
            }
          },
          {
            "paadal": "nயானையும் குதிரையும் கழுதையும் கடமையும் \nமானொடு ஐந்தும் கன்று எனற்கு உரிய. ",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "The term kaṉṟu (கன்று) belongs to the young of elephant, horse, ass, elk and cow."
            }
          },
          {
            "paadal": "எருமையும் மரையும் வரையார் ஆண்டே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "They do not prohibit the term kaṉṟu (கன்று) to denote the end of buffalo and marai (மரை) (bison) also."
            }
          },
          {
            "paadal": "கவரியும் கராமும் நிகர் அவற்றுள்ளே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Kavari (கவரி) (yak) and karā (கரா) (alligator) take the same term kaṉṟu (கன்று)."
            }
          },
          {
            "paadal": "ஒட்டகம் அவற்றொடு ஒரு வழி நிலையும்.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Camel also agrees with them (in taking kaṉṟu (கன்று) to denote their young)."
            }
          },
          {
            "paadal": "குஞ்சரம் பெறுமே குழவிப் பெயர்க்கொடை.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Elephant receives the term kuḻavi (குழவி) (to denote the young)."
            }
          },
          {
            "paadal": "ஆவும் எருமையும் அது சொலப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "A (cow) and erumai(எருமை) (buffalo) too take that, term (kuḻavi)(குழவி)."
            }
          },
          {
            "paadal": "கடமையும் மரையும் முதல் நிலை ஒன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "Kaṭamai (கடமை) and marai (மரை) agree with those mentioned above."
            }
          },
          {
            "paadal": "குரங்கும் முசுவும் ஊகமும் மூன்றும் \nநிரம்ப நாடின் அப் பெயர்க்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of Animal Species",
              "paadal_meaning": "The three kuraṅkū (குரங்கு) , mucu (முசு), and ūkam (ஊகம்) deserve, on careful examination, the same term kuḻavi (குழவி) (fo denote the young)."
            }
          },
          {
            "paadal": "குழவியும் மகவும் ஆயிரண்டு அல்லவை \nகிழவ அல்ல மக்கட்கண்ணே.",
            "vilakkam": 
            {
              "paadal_category": "Human Offspring",
              "paadal_meaning": "No term other than kuḻavi (குழவி) and makavu (மகவு) can be used to denote the young of human beings."
            }
          },
          {
            "paadal": "பிள்ளை குழவி கன்றே போத்து எனக் \nகொள்ளவும் அமையும் ஓர் அறிவு உயிர்க்கே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of One Sense Faculty",
              "paadal_meaning": "The terms piḷḷai (பிள்ளை), kuḻavi (குழவி), kaṉṟū (கன்று), and pōttū (போத்து) may be used to denote the young of living organisms having the sense of touch alone."
            }
          },
          {
            "paadal": "நெல்லும் புல்லும் நேரார் ஆண்டே. ",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of One Sense Faculty",
              "paadal_meaning": "Neḻ (நெல்) (paddy plant) and grass do not take them."
            }
          },
          {
            "paadal": "சொல்லிய மரபின் இளமைதானே \nசொல்லும் காலை அவை அல இலவே.",
            "vilakkam": 
            {
              "paadal_category": "Offsprings of One Sense Faculty",
              "paadal_meaning": "There is no term other than those mentioned above used to denote the young of objects."
            }
          },
          {
            "paadal": "ஒன்று அறிவதுவே உற்று அறிவதுவே \nஇரண்டு அறிவதுவே அதனொடு நாவே \nமூன்று அறிவதுவே அவற்றொடு மூக்கே \nநான்கு அறிவதுவே அவற்றொடு கண்ணே \nஐந்து அறிவதுவே அவற்றொடு செவியே \nஆறு அறிவதுவே அவற்றொடு மனனே \nநேரிதின் உணர்ந்தோர் நெறிப்படுத்தினரே.",
            "vilakkam": 
            {
              "paadal_category": "Distinctions of Sense Organisms",
              "paadal_meaning": "Scholars have classified living organisms under six heads : ōr-ariv-uyir (ஓர் அறிவு உயிர்) having the sense,of touch alone, īr-ariv-uyir (இரண்டு அறிவு உயிர்) having the senses of touch and taste, mū-v-ariv-uyir (மூன்று அறிவு உயிர்) having the senses of touch, taste and smell, nāl-aṟiv-uyir (நான்கு அறிவு உயிர்) having the senses of touch, taste, smell and sight, ai-y-aṟiv-uyir (ஐந்து அறிவு உயிர்) having the senses of touch, taste, smell, sight and hearing and āṟ-aṟiv- uyir (ஆறு அறிவு உயிர்) having the power of discrimination in addition to the above five senses."
            }
          },
          {
            "paadal": "புல்லும் மரனும் ஓர் அறிவினவே \nபிறவும் உளவே அக் கிளைப் பிறப்பே. ",
            "vilakkam": 
            {
              "paadal_category": "One Sense Organisms",
              "paadal_meaning": "The Grass and Tree are single sense organisms, Other species of the flora there are too that are limited to this faculty."
            }
          },
          {
            "paadal": "நந்தும் முரளும் ஈர் அறிவினவே \nபிறவும் உளவே அக்கிளைப் பிறப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Two Sense Organisms",
              "paadal_meaning": "Snail and shell-fish belong to the class of ir-aṟiv-uyir (இரண்டு அறிவு உயிர்); there are others also belonging to it."
            }
          },
          {
            "paadal": "சிதலும் எறும்பும் மூ அறிவினவே \nபிறவும் உளவே அக் கிளைப் பிறப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Three Sense Organisms",
              "paadal_meaning": "Termite and ant belong to the class of mū-v-aṟiv-uyir (மூன்று அறிவு உயிர்) ; there are others also belonging to it."
            }
          },
          {
            "paadal": "நண்டும் தும்பியும் நான்கு அறிவினவே \nபிறவும் உளவே அக் கிளைப் பிறப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Four Sense Organisms",
              "paadal_meaning": "Crab and bee belong to the class of nāṉk-aṟiv-uyir (நான்கு அறிவு உயிர்) : there are others also belonging to it."
            }
          },
          {
            "paadal": "மாவும் மாக்களும் ஐ அறிவினவே \nபிறவும் உளவே அக் கிளைப் பிறப்பே.",
            "vilakkam":
            {
              "paadal_category": "Five Sense Organisms",
              "paadal_meaning": "Animals and birds belong to the class of ai-y-aṟiv-uyir (ஐந்து அறிவு உயிர்) ; there are others also belonging to it."
            }
          },
          {
            "paadal": "மக்கள்தாமே ஆறு அறிவு உயிரே \nபிறவும் உளவே அக் கிளைப் பிறப்பே.",
            "vilakkam": 
            {
              "paadal_category": "Six Sense Organisms",
              "paadal_meaning": "Human beings belong to the class of āṟaṟivuyir (ஆறு அறிவு உயிர்); there are others also belonging to it."
            }
          },
          {
            "paadal": "ஒரு சார் விலங்கும் உள என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Six Sense Organisms",
              "paadal_meaning": "They say that a class of animals also belong to that type (āṟaṟivuyir)(ஆறு அறிவு உயிர்)."
            }
          },
          {
            "paadal": "வேழக்கு உரித்தே விதந்து களிறு என்றல்.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term kaḷirū (களிறு) is used with reference to the male of elephants."
            }
          },
          {
            "paadal": "கேழற்கண்ணும் கடி வரை இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "It is not strictly prohibited to use it to denote boar."
            }
          },
          {
            "paadal": "புல்வாய் புலி உழை மரையே கவரி \nசொல்லிய கராமொடு ஒருத்தல் ஒன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term oru-t-tal (ஒருத்தல்) is used with reference to the male of antelope, tiger, deer, marai, kavari (கவரி) and alligator."
            }
          },
          {
            "paadal": "வார் கோட்டு யானையும் பன்றியும் அன்ன.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "Elephant having big tusks and boar are of the same kind; i.e., they take the term oru-t-tal (ஒருத்தல்) also."
            }
          },
          {
            "paadal": "ஏற்புடைத்து என்ப எருமைக்கண்ணும்.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term oru-t-tal(ஒருத்தல்) may be used to denote even the male of buffalo."
            }
          },
          {
            "paadal": "பன்றி புல்வாய் உழையே கவரி \nஎன்று இவை நான்கும் ஏறு எனற்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The male of the four, paṉṟi (பன்றி), puḻvāy (புல்வாய்), uḻai (உழை) and kavari (கவரி), may also be called ēṟū (ஏறு)."
            }
          },
          {
            "paadal": "எருமையும் மரையும் பெற்றமும் அன்ன.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "Erumai (எருமை), marai (மரை) and peṟṟam(பெற்றம்) also are of the same nature; i.e., their male may be called ēṟū(ஏறு)."
            }
          },
          {
            "paadal": "கடல் வாழ் சுறவும் ஏறு எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The male of cuṟā living in sea also may be called ēṟū(ஏறு)."
            }
          },
          {
            "paadal": "பெற்றம் எருமை புலி மரை புல்வாய் \nமற்று இவை எல்லாம் போத்து எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The male of peṟṟam (பெற்றம்), erumai (எருமை), puli (புலி), marai (மரை), pulvāy (புல்வாய்) etc. is called pōttū (போத்து)."

            }
          },
          {
            "paadal": "நீர் வாழ் சாதியும் அது பெறற்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "There are some in aquatic animals which take the term pōttū (போத்து) to denote their male."
            }
          },
          {
            "paadal": "மயிலும் எழாலும் பயிலத் தோன்றும். ",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "pōttū (போத்து) appears with reference to the male of mayil(மயில்) and eḻāl (எழால்)."
            }
          },
          {
            "paadal": "இரலையும் கலையும் புல்வாய்க்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The terms iralai (இரலை) and kalai (கலை) may be used to denote the male of pulvāy (புல்வாய்)."
           }
          },
          {
            "paadal": "கலை என் காட்சி உழைக்கும் உரித்தே \nநிலையிற்று அப் பெயர் முசுவின்கண்ணும்.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term kalai (கலை) is used with reference to the male of uḷai (உழை) also.The same term kalai (கலை) is used  with regard to the male of mucu (முசு)."
            }
          },
          {
            "paadal": "மோத்தையும் தகரும் உதளும் அப்பரும் \nயாத்த என்ப யாட்டின்கண்ணே.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The terms mōttai (மோத்தை), takar (தகர்), mutaḷ (உதள்), and appar (அப்பர்) are used to denote the male of goat or sheep."
            }
          },
          {
            "paadal": "சேவல் பெயர்க்கொடை சிறகொடு சிவணும் \nமா இருந் தூவி மயில் அலங்கடையே.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term cēval (சேவல்) is used to denote the male of birds except peacock with a big long tail."
            }
          },
          {
            "paadal": "ஆற்றலொடு புணர்ந்த ஆண்பாற்கு எல்லாம் \nஏற்றைக் கிளவி உரித்து என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The term ēṟṟai (ஏற்றை), they say, may be used to denote the male of all valiant beings."
            }
          },
          {
            "paadal": "ஆண்பால் எல்லாம் ஆண் எனற்கு உரிய \nபெண்பால் எல்லாம் பெண் எனற்கு உரிய \nகாண்ப அவை அவை அப்பாலான.",
            "vilakkam": 
            {
              "paadal_category": "Male Designations",
              "paadal_meaning": "The word an may be used to denote the male of all beings and peṇ(பெண்), the female, since such a usage is found in the world."
            }
          },
          {
            "paadal": "பிடி என் பெண் பெயர் யானை மேற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The female term piṭi (பிடி) is used with reference to elephant."
            }
          },
          {
            "paadal": "ஒட்டகம் குதிரை கழுதை மரை இவை \nபெட்டை என்னும் பெயர்க்கொடைக்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The female term peṭai (பெடை) is used with reference to camel horse, ass and bison."
            }
          },
          {
            "paadal": "புள்ளும் உரிய அப் பெயர்க்கு என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The same term may be used with reference to the female of birds."
            }
          },
          {
            "paadal": "பேடையும் பெடையும் நாடின் ஒன்றும்.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "Pēṭai (பேடை) and peṭai (பெடை) are used, on examination, to denote the female of birds."
            }
          },
          {
            "paadal": "கோழி கூகை ஆயிரண்டு அல்லவை \nசூழும் காலை அளகு எனல் அமையா.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The term aḷaku (அளகு) is not used to denote the female of beings other than fowl and owl."
            }
          },
          {
            "paadal": "அப் பெயர்க் கிழமை மயிற்கும் உரித்தே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The same term holds good to peahen also."
            }
          },
          {
            "paadal": "புல்வாய் நவ்வி உழையே கவரி \nசொல்வாய் நாடின் பிணை எனப்படுமே. ",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "On examining usage, the term piṇai (பிணை) is seen denoting the female of pulvāy (புல்வாய்), navvi (நவ்வி), uḻai (உழை) and kavari (கவரி)."
            }
          },
          {
            "paadal": "பன்றி புல்வாய் நாய் என மூன்றும் \nஒன்றிய என்ப பிணவின் பெயர்க்கொடை.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The term piṇavu (பிணவு) is appropriate to the female of Paṉṟi (பன்றி), pulvāy (புல்வாய்) and nāy (நாய்)."
            }
          },
          {
            "paadal": "பிணவல் எனினும் அவற்றின் மேற்றே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The term piṇaval (பிணவல்) also is used with reference to them."
            }
          },
          {
            "paadal": "பெற்றமும் எருமையும் மரையும் ஆவே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The term ā is used to denote the female of peṟṟam (பெற்றம்), erumai (எருமை) and marai (மரை)."
            }
          },
          {
            "paadal": "பெண்ணும் பிணாவும் மக்கட்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "Peṇ (பெண்) and piṇavu (பிணாவு) are the appropriate terms with reference to human beings."
            }
          },
          {
            "paadal": "எருமையும் மரையும் பெற்றமும் நாகே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The term nākū (நாகு) is used to denote the female of erumai (எருமை), marai (மரை) and peṟṟam(பெற்றம்)."
            }
          },
          {
            "paadal": "நீர் வாழ் சாதியுள் நந்தும் நாகே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "Nākū (நாகு) is used with reference to ṇantu (நந்து) among aquatic animals."
            }
          },
          {
            "paadal": "மூடும் கடமையும் யாடு அல பெறாஅ.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The terms mūtū (மூடு) and kaṭamai (கடமை) are not used with reference to any other than yāṭū(யாடு)."
            }
          },
          {
            "paadal": "பாட்டி என்ப பன்றியும் நாயும்.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "Paṉṟi (பன்றி) and nari (நரி) take the terms pāṭṭi (பாட்டி), they say."
            }
          },
          {
            "paadal": "நரியும் அற்றே நாடினர் கொளினே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "If carefully examined, nari (நரி) also belongs to them, i.e., it takes the term pāṭṭi(பாட்டி)."
            }
          },
          {
            "paadal": "குரங்கும் முசுவும் ஊகமும் மந்தி.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "Manti (மந்தி) is the term used to denote the female of kuraṅkū (குரங்கு), mucu (முசு), and ūkam (ஊகம்)."
            }
          },
          {
            "paadal": "குரங்கின் ஏற்றினைக் கடுவன் என்றலும் \nமரம் பயில் கூகையைக் கோட்டான் என்றலும் \nசெவ் வாய்க் கிளியைத் தத்தை என்றலும் \nவெவ் வாய் வெருகினைப் பூசை என்றலும் \nகுதிரையுள் ஆணினைச் சேவல் என்றலும் \nஇருள் நிறப் பன்றியை ஏனம் என்றலும் \nஎருமையுள் ஆணினைக் கண்டி என்றலும் \nமுடிய வந்த அவ் வழக்கு உண்மையின் \nகடியல் ஆகா கடன் அறிந்தோர்க்கே.",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "It is not proper to those conversant with the history of language and the usage to avoid the following terms: Kaṭuvaṉ (கடுவன்) to denote the male of monkeys, kōṭṭan (கோட்டான்) to denote the owl living in the trees, tattai (தத்தை) to denote fine-mouthed parrot, pūcai(பூசை) to denote ferocious wild cat, cēval (சேவல்) to denote the male of horse, ēnam (ஏனம்) to denote black pig and kaṇṭi (கண்டி) to denote the male of buffalo."
            }
          },
          {
            "paadal": "பெண்ணும் ஆணும் பிள்ளையும் அவையே. ",
            "vilakkam": 
            {
              "paadal_category": "Female Designations",
              "paadal_meaning": "The terms peṇ (பெண்), āṇ (ஆண்) and piḷḷai( பிள்ளை) belong to the above category."
            }
          },
          {
            "paadal": "நூலே கரகம் முக்கோல் மணையே \nஆயும் காலை அந்தணர்க்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Possessions of the Brahmins",
              "paadal_meaning": "Sacred thread, jar, trident staff and seat are to be held by antaṇar (அந்தணர்), (high class brahmans)."
            }
          },
          {
            "paadal": "படையும் கொடியும் குடையும் முரசும் \nநடை நவில் புரவியும் களிறும் தேரும் \nதாரும் முடியும் நேர்வன பிறவும் \nதெரிவு கொள் செங்கோல் அரசர்க்கு உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Symbols of Sovereignity",
              "paadal_meaning": "The following are to be held by benignly ruling kings: army, flag, umbrella, war-drum, swift cavalry, elephantry, chariots, rank and file of an army, crown and others which are necessary."
            }
          },
          {
            "paadal": "அந்தணாளர்க்கு உரியவும் அரசர்க்கு \nஒன்றிய வரூஉம் பொருளுமார் உளவே. ",
            "vilakkam": 
            {
              "paadal_category": "Symbols of Sovereignity",
              "paadal_meaning": "There are things worthy to be held by high class brahmans, which may be held by kings."
            }
          },
          {
            "paadal": "பரிசில் பாடாண் திணைத் துறைக் கிழமைப்பெயர் \nநெடுந்தகை செம்மல் என்று இவை பிறவும் \nபொருந்தச் சொல்லுதல் அவர்க்கு உரித்தன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Symbols of Sovereignity",
              "paadal_meaning": "Antaṇar (அந்தணர்), if there is propriety, may be appealed for gifts, may be praised for their patronage, fame etc. and may be addressed by the terms neṭuntakai (நெடுந்தகை ), cemmal (செம்மல்) etc."
            }
          },
          {
            "paadal": "ஊரும் பெயரும் உடைத்தொழிற் கருவியும் \nயாரும் சார்த்தி அவை அவை பெறுமே.",
            "vilakkam": 
            {
              "paadal_category": "Naming of People",
              "paadal_meaning": "All castes take their residence, name and implements of their trade suited to them."
            }
          },
          {
            "paadal": "தலைமைக் குணச் சொலும் தம்தமக்கு உரிய \nநிலைமைக்கு ஏற்ப நிகழ்த்துப என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Titles of Honour",
              "paadal_meaning": "They say that words denoting the predominant quality suited to their taste are used."
            }
          },
          {
            "paadal": "இடை இரு வகையோர் அல்லது நாடின் \nபடை வகை பெறாஅர் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Claims of Kings and Traders",
              "paadal_meaning": "Learned men say that, on examination, none other than the two middle castes, i.e.  Kṣatriyas (சத்திரியர்) and Vaiśyas (வைசியர்கள்) take to army."
            }
          },
          {
            "paadal": "வைசிகன் பெறுமே வாணிக வாழ்க்கை.",
            "vilakkam": 
            {
              "paadal_category": "Claims of Kings and Traders",
              "paadal_meaning": "Vaiśya (வைசியர்கள்)  takes to trade."
            }
          },
          {
            "paadal": "மெய் தெரி வகையின் எண் வகை உணவின் \nசெய்தியும் வரையார் அப் பாலான.",
            "vilakkam": 
            {
              "paadal_category": "Claims of Kings and Traders",
              "paadal_meaning": "They do not prohibit them from producing the eight kinds of food in a suitable manner."
            }
          },
          {
            "paadal": "கண்ணியும் தாரும் எண்ணினர் ஆண்டே.",
            "vilakkam": 
            {
              "paadal_category": "Claims of Kings and Traders",
              "paadal_meaning": "They have stated that Vaiśyas (வைசியர்கள்) deserve to have flowers and garlands."
            }
          },
          {
            "paadal": "வேளாண் மாந்தர்க்கு உழுதூண் அல்லது \nஇல் என மொழிப பிற வகை நிகழ்ச்சி.",
            "vilakkam": 
            {
              "paadal_category": "Farming Class",
              "paadal_meaning": "Vēḷāḻas (வேளாண்) have no profession, they say, other than agriculture."
            }
          },
          {
            "paadal": "வேந்து விடு தொழிலின் படையும் கண்ணியும் \nவாய்ந்தனர் என்ப அவர் பெறும் பொருளே.",
            "vilakkam": 
            {
              "paadal_category": "Farming Class",
              "paadal_meaning": "They are worthy of having weapons and flowers, if they are sent on Government business."
            }
          },
          {
            "paadal": "அந்தணாளர்க்கு அரசு வரைவு இன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Brahmins",
              "paadal_meaning": "Sovereignty is not prohibited to antaṇar (அந்தணர்)."
            }
          },
          {
            "paadal": "வில்லும் வேலும் கழலும் கண்ணியும் \nதாரும் மாலையும் தேரும் மாவும் \nமன் பெறு மரபின் ஏனோர்க்கும் உரிய.",
            "vilakkam": 
            {
              "paadal_category": "Ruling of Chieftains",
              "paadal_meaning": "Bow, spear, anklet, kaṇṇi (கண்ணி), tār (தார்), āram (ஆரம்) , chariot and cavalry may be had by others of high position."
            }
          },
          {
            "paadal": "அன்னர் ஆயினும் இழிந்தோர்க்கு இல்லை.",
            "vilakkam": 
            {
              "paadal_category": "Ruling of Chieftains",
              "paadal_meaning": "Those who are qualified to have them are not entitled to have them, if they are degraded in position."
            }
          },
          {
            "paadal": "புறக் காழனவே புல் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Exogeneous and Endogeneous Species",
              "paadal_meaning": "Vegetable kingdom whose outer part is of close grain is called pul(புல்)."
            }
          },
          {
            "paadal": "அகக் காழனவே மரம் என மொழிப.",
            "vilakkam": 
            {
              "paadal_category": "Exogeneous and Endogeneous Species",
              "paadal_meaning": "Vegetable kingdom whose inner part is of close grain is called maram (மரம்)."
            }
          },
          {
            "paadal": "தோடே மடலே ஓலை என்றா \nஏடே இதழே பாளை என்றா \nஈர்க்கே குலை என நேர்ந்தன பிறவும் \nபுல்லொடு வரும் எனச் சொல்லினர் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Exogeneous and Endogeneous Species",
              "paadal_meaning": "Learned men say that the following terms are used to denote the different parts of pul (புல்) genus:— tōṭū (தோடூ) (sheath), maṭal (மடல்) (tagged stem), ōlai(ஓலை) (leaf), ēṭu (ஏடு) (stripof leaf), itaḻ (இதழ்) (petal), pāḷai (பாளை) (spathe), īrkku (ஈர்க்கு) (rib of a leaf), kulai (குலை) (bunch), etc."
           }
          },
          {
            "paadal": "இலையே தளிரே முறியே தோடே \nசினையே குழையே பூவே அரும்பே \nநனை உள்ளுறுத்த அனையவை எல்லாம் \nமரனொடு வரூஉம் கிளவி என்ப.",
            "vilakkam": 
            {
              "paadal_category": "Exogeneous and Endogeneous Species",
              "paadal_meaning": "They say that the following terms are used to denote the different parts of maram (மரம்) class:— ilai(இலை) (leaf), muṟi (முறி) (tender leaf), taḷir (தளிர்) (sprout), tōṭu (தோடு) (sheath), ciṉai (சினை) (branch), kuḻai (குழை) (shoot), pū (பூ) (flowers), arumpū (அரும்பு) (bud), naṉai (நனை) (bud), etc."
            }
          },
          {
            "paadal": "காயே பழமே தோலே செதிளே \nவீழொடு என்று ஆங்கு அவையும் அன்ன.",
            "vilakkam": 
            {
              "paadal_category": "Exogeneous and Endogeneous Species",
              "paadal_meaning": "The following belong to both: kāy (காய்) (unripe fruit), paḻam (பழம்) (fruit), tōl (தோல்) (inner layer of both), cetiḷ (செதிள்) (outer layer of both), vīḻ (வீழ்) (aerial root), etc."
            }
          },
          {
            "paadal": "நிலம் தீ நீர் வளி விசும்பொடு ஐந்தும் \nகலந்த மயக்கம் உலகம் ஆதலின் \nஇரு திணை ஐம் பால் இயல் நெறி வழாஅமைத் \nதிரிவு இல் சொல்லொடு தழாஅல் வேண்டும்.",
            "vilakkam": 
            {
              "paadal_category": "A Linguistic Convention",
              "paadal_meaning": "Since the worldly objects are the result of combination of the five elements earth, fire, water, air and space, they should be expressed correctly without error with reference to the two tiṇais (திணை) and five pāls (பால்)."
            }
          },
          {
            "paadal": "மரபுநிலை திரிதல் செய்யுட்கு இல்லை \nமரபு வழிப் பட்ட சொல்லினானே.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Literary Usage",
              "paadal_meaning": "One should not go against tradition in writing verse, with reference to words already in use."
            }
          },
          {
            "paadal": "மரபுநிலை திரியின் பிறிது பிறிது ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Literary Usage",
              "paadal_meaning": "If words are used against traditional usage, they will not convey the correct sense."
          }
          },
          {
            "paadal": "வழக்கு எனப்படுவது உயர்ந்தோர் மேற்றே \nநிகழ்ச்சி அவர் கட்டு ஆகலான.",
            "vilakkam": 
            {
              "paadal_category": "Nature of Literary Usage",
              "paadal_meaning": "Vaḻakku (வழக்கு) (usage) refers to that of the high class men, since they alone compose poems, etc."
            }
          },
          {
            "paadal": "மரபுநிலை திரியா மாட்சிய ஆகி \nஉரை படு நூல்தாம் இரு வகை இயல \nமுதலும் வழியும் என நுதலிய நெறியின.",
            "vilakkam": 
            {
              "paadal_category": "Primary and Secondary Works",
              "paadal_meaning": "The work composed by authors with due attention to traditional usage is of two kinds:— mutal-nūl (முதல் நூல்) and vaḻi-nūl (வழி நூல்)."
            }
          },
          {
            "paadal": "வினையின் நீங்கி விளங்கிய அறிவின் \nமுனைவன் கண்டது முதல் நூல் ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Primary and Secondary Works",
              "paadal_meaning": "The work composed by a sage of spotless knowledge on account of his bein tree from the effect of karma (கர்மா) forms the mutal-nūl(முதல் நூல்) ."
            }
          },
          {
            "paadal": "வழி எனப்படுவது அதன் வழித்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Primary and Secondary Works",
              "paadal_meaning": "Vaḻi-nūl (வழி நூல்) is that which follows mutal-nūl (முதல் நூல்) ."
            }
          },
          {
            "paadal": "வழியின் நெறியே நால் வகைத்து ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Primary and Secondary Works",
              "paadal_meaning": "Vaḻi-nūl (வழி நூல்) is of four kinds:"
            }
          },
          {
            "paadal": "தொகுத்தல் விரித்தல் தொகைவிரி மொழிபெயர்த்து \nஅதர்ப்பட யாத்தலொடு அனை மரபினவே.",
            "vilakkam": 
            {
              "paadal_category": "Modes of Composition of Secondary Works",
              "paadal_meaning": "They are abridgement, elaboration, abridgement with elaboration and translation."
            }
          },
          {
            "paadal": "ஒத்த சூத்திரம் உரைப்பின் காண்டிகை \nமெய்ப்படக் கிளந்த வகையது ஆகி \nஈர் ஐங் குற்றமும் இன்றி நேரிதின் \nமுப்பத்திரு வகை உத்தியொடு புணரின் \nநூல் என மொழிப நுணங்கு மொழிப் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Nūl (நூல்)",
              "paadal_meaning": "Ripe scholars say that nūl (நூல்) is that which is made of sūtras (சூத்திரம்) which can be commented on properly in commentaries of the kaṇṭikai (காண்டிகை), etc., which are free from the ten defects of composition and where all the thirty-two uṭṭis (உத்தி) will have room to operate."
            }
          },
            {
            "paadal": "உரை எடுத்து அதன் முன் யாப்பினும் சூத்திரம் \nபுரை தப உடன்படக் காண்டிகை புணர்ப்பினும் \nவிதித்தலும் விலக்கலும் என இரு வகையொடு \nபுரை தப நாடிப் புணர்க்கவும் படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Urai (உறை)",
              "paadal_meaning": "It is possible to write a commentary independent of kāṇṭikai (காண்டிகை) or elucidating the kāṇṭikai (காண்டிகை) which establishes the infallible nature of the sūtras(சூத்திரம்) by telling what the sūtras (சூத்திரம்) enjoin and what they do not enjoin."
            }
          },
          {
            "paadal": "மேற் கிளந்தெடுத்த யாப்பினுள் பொருளொடு \nசில் வகை எழுத்தின் செய்யுட்கு ஆகி \nசொல்லும் காலை உரை அகத்து அடக்கி \nநுண்மையொடு புணர்ந்த ஒண்மைத்து ஆகி \nதுளக்கல் ஆகாத் துணைமை எய்தி \nஅளக்கல் ஆகா அரும் பொருட்டு ஆகி \nபல வகையானும் பயன் தெரிபு உடையது \nசூத்திரத்து இயல்பு என யாத்தனர் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "Cūttiram (சூத்திரம்)",
              "paadal_meaning": "Scholars says that it is the nature of sūtra (சூத்திரம்) to adopt one of the methods. tokuttal (தொகுத்தல்), virittal (விரித்தல்), tokai-viri (தொகைவிரி), and moḻi-peyart-tal (மொழிபெயர்த்தல்) to contain the minimum number of syllables, to be in the form of a verse, to be capable of being commented upon, to be terse and unambiguous, to be tacked on to others that follow, lo be rich in meaning and to be of use in many ways."
            }
          },
          {
            "paadal": "பழிப்பு இல் சூத்திரம் பட்ட பண்பின் \nகரப்பு இன்றி முடிவது காண்டிகை ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Kāṇṭikai (காண்டிகை)",
              "paadal_meaning": "Kāṇṭikai (காண்டிகை) is the commentary which lucidly explains the sūtra (சூத்திரம்) devoid of spots."
            }
          },
          {
            "paadal": "விட்டு அகல்வு இன்றி விரிவொடு பொருந்தி \nசுட்டிய சூத்திரம் முடித்தற் பொருட்டா \nஏது நடையினும் எடுத்துக்காட்டினும் \nமேவாங்கு அமைந்த மெய்ந் நெறித்து அதுவே. ",
            "vilakkam": 
            {
              "paadal_category": "Kāṇṭikai (காண்டிகை)",
              "paadal_meaning": "It (Kāṇṭikai)(காண்டிகை)  is of the nature of not going beyond the range of the sūtra (சூத்திரம்), of splitting it into words and of explaining its meaning clearly with reasons and illustrations."
            }
          },
          {
            "paadal": "சூத்திரத்துட் பொருள் அன்றியும் யாப்புற \nஇன்றியமையாது இயைபவை எல்லாம் \nஒன்ற உரைப்பது உரை எனப்படுமே.",
            "vilakkam": 
            {
              "paadal_category": "Urai (உரை)",
              "paadal_meaning": "It is said to be urai (உரை) which contains not only the literal meaning of the sūtra (சூத்திரம்), but also other topics without which the meaning cannot be easily understood."
            }
          },
          {
            "paadal": "மறுதலைக் கடாஅ மாற்றமும் உடைத்தாய் \nதன் நூலானும் முடிந்த நூலானும் \nஐயமும் மருட்கையும் செவ்விதின் நீக்கி \nதெற்றென ஒரு பொருள் ஒற்றுமை கொளீஇ \nதுணிவொடு நிற்றல் என்மனார் புலவர்.",
            "vilakkam": 
            {
              "paadal_category": "urai (உரை)",
              "paadal_meaning": "Scholars say that it is the nature of urai (உரை) to raise objections and answer them, to clear doubts and incorrect interpretation on the authority (of the ideas elsewhere) in the book on hand or on that of other works and clearly arrive at the correct meaning."
            }
          },
          {
            "paadal": "சொல்லப்பட்டன எல்லா மாண்பும் \nமறுதலை ஆயினும் மற்று அது சிதைவே.",
            "vilakkam": 
            {
              "paadal_category": "Inadequacy  of a Composition",
              "paadal_meaning": "It is considered a flaw, if a work fails to conform to the characteristics mentioned above."
            }
          },
          {
            "paadal": "சிதைவு இல் என்ப முதல்வன் கண்ணே.",
            "vilakkam": 
            {
              "paadal_category": "Inadequacy  of a Composition",
              "paadal_meaning": "The fault is not observed in mutaṉūl(முதனூல்)."
            }
          },
          {
            "paadal": "முதல் வழி ஆயினும் யாப்பினுள் சிதையும் \nவல்லோன் புணரா வாரம் போன்றே.",
            "vilakkam": 
            {
              "paadal_category": "Inadequacy  of a Composition",
              "paadal_meaning": "The vaḻinūl (வழிநூல்) may go astray in yāppu (யாப்பு), i.e., tokuttal (தொகுத்தல்) , virittal (விரித்தல்) , tokai-viri (தொகைவிரி) and moḻi-peyarppu (மொழிபெயர்ப்பு) like the tune repeated by an unskilled man."
            }
          },
          {
            "paadal": "சிதைவு எனப்படுபவை வசை அற நாடின் \nகூறியது கூறல் மாறு கொளக் கூறல் \nகுன்றக் கூறல் மிகை படக் கூறல் \nபொருள் இல கூறல் மயங்கக் கூறல் \nகேட்போர்க்கு இன்னா யாப்பிற்று ஆதல் \nபழித்த மொழியான் இழுக்கம் கூறல் \nதன்னான் ஒரு பொருள் கருதிக் கூறல் \nஎன்ன வகையினும் மனம் கோள் இன்மை \nஅன்ன பிறவும் அவற்று விரி ஆகும்.",
            "vilakkam": 
            {
              "paadal_category": "Defects in a Composition",
              "paadal_meaning": "If citaivu (சிதைவு) is correctly examined, it falls under the following heads:—(1) Repetition of ideas, (2) statement of contradictory ideas (3) omission of ideas, (4) too much elaboration of ideas, (5) statement of meaningless expressions, (6) mixing up of ideas, (7) composing in a yāppu (யாப்பு) which is unpleasant to the hearer, (8) choosing a form of statement which he has already found fault with, (9) interpolation and (10) uncouth expression in diverse ways."
            }
          },
          {
            "paadal": "எதிர் மறுத்து உணரின் அத் திறத்தவும் அவையே.",
            "vilakkam": 
            {
              "paadal_category": "Defects in a Composition",
              "paadal_meaning": "It is a defect if the vaḻi-nūl (வழிநூல்) has ideas diametrically oppoite to those found in mutaṉūl(முதல் நூல்)."
            }
          },
          {
            "paadal": "ஒத்த காட்சி உத்தி வகை விரிப்பின் \nநுதலியது அறிதல் அதிகார முறையே \nதொகுத்துக் கூறல் வகுத்து மெய்ந் நிறுத்தல் \nமொழிந்த பொருளொடு ஒன்ற வைத்தல் \nமொழியாததனை முட்டு இன்றி முடித்தல் \nவாராததனான் வந்தது முடித்தல் \nவந்தது கொண்டு வாராதது உணர்த்தல் \nமுந்து மொழிந்ததன் தலைதடுமாற்றே \nஒப்பக் கூறல் ஒருதலை மொழிதல் \nதன் கோள் கூறல் முறை பிறழாமை \nபிறன் உடன்பட்டது தான் உடம்படுதல் \nஇறந்தது காத்தல் எதிரது போற்றல் \nமொழிவாம் என்றல் கூறிற்று என்றல் \nதான் குறியிடுதல் ஒருதலை அன்மை \nமுடிந்தது காட்டல் ஆணை கூறல் \nபல் பொருட்கு ஏற்பின் நல்லது கோடல் \nதொகுத்த மொழியான் வகுத்தனர் கோடல் \nமறுதலை சிதைத்துத் தன் துணிபு உரைத்தல் \nபிறன் கோள் கூறல் அறியாது உடம்படல் \nபொருள் இடையிடுதல் எதிர் பொருள் உணர்த்தல் \nசொல்லின் எச்சம் சொல்லியாங்கு உணர்த்தல் \nதந்து புணர்ந்து உரைத்தல் ஞாபகம் கூறல் \nஉய்த்துக்கொண்டு உணர்த்தலொடு மெய்ப்பட நாடிச் \nசொல்லிய அல்ல பிற அவண் வரினும் \nசொல்லிய வகையான் சுருங்க நாடி \nமனத்தின் எண்ணி மாசு அறத் தெரிந்துகொண்டு \nஇனத்தின் சேர்த்தி உணர்த்தல் வேண்டும் \nநுனித்தகு புலவர் கூறிய நூலே.",
            "vilakkam": 
            {
              "paadal_category": "Utti (உத்தி) (Devices in a Composition)",
              "paadal_meaning": "If the classification utti (உத்தி) is elaborately given to be applied in the works of high class authors, they are (1) understanding the purport of a sūtra (சூத்திரம்) (2) deciding the extent where one serves as adhikāra sūtra (அதிகார சூத்திரம்) or a word or words in a sūtra (சூத்திரம்) taken along with the sūtras (சூத்திரம்) that follow (3) brief enumeration of what is to be dilated upon later (4) detailed exposition through classification (5) interpreting a sūtra (சூத்திரம்) in consonance with what has been mentioned (6) suitably supplementing the content of a sūtra (சூத்திரம்) , (7) interpreting a sūtra (சூத்திரம்) on the basis of another which is to follow (8) application of analogy (9) adopting an order contrary to that mentioned before (10) statement that one operates similar to another mentioned before (11) deciding one way when there is ambiguity (12) stating one's doctrine not held by predecessors (13) adopting through jñāpaka (ஞாபகம்) from the use of a word by the author though it is not mentioned in the rules (Iḷampūraṇam)(இளம்புராணம்) ; not going against the order adopted before (Pērāśiriyam) (பேரசைரியம்) (14) agreeing with the opinion of others (15) restricting the application of a sūtra (சூத்திரம்) by one which follows (16) interpretidg a sūtra(சூத்திரம்) in the light of what will follow (17) referring to what will be stated later on (18) referring to what has been stated before (19) coining technical terms (20) explaining that what is stated with reference to one applies to others also  (21) mentioning in strong terms his own view (22) choosing one interpretation among many (23) stating one form to denote many (24) stating one's view after refuting that of others (25) giving out others opinion (26) agreeing to other views about which he has no definite idea (27) interceding one between siitras though it is not concerned with the main topic (28) stating what is to come (29) interpreting the denotation of the word etc. or rest from what has been mentioned before (30) taking something found elsewhere and associating it with the topic on hand (31) suggestion and (32) decision through inference. If others also are capable of being taken, they may be carefully scrutinised and added to the list if they deserve it."
            }
         }
        ]
      }
    ]
  }
]

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Wellcome to Tholkkaappiyam Page if you want briefly type /help it will show all the commands ")
    
def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('''The follwoing commands are avaiable in Tholkaappiyam
        /start
        /help
        /about_tholkaappiyam
        /display_tholkaapiyar
        /display_adhikaaram
        /display_iyal 
        Iyal info:
                  /display_total_no_of_songs
                  /categories_paadal_count_dict 
        Adhikaaram:
                  /display_total_no_of_songs1
                  /iyals_paadal_count_dict
        Paadal
                  /display_paadal_data''')
def display_tholkaapiyar(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    image_url = 'https://tamilandvedas.files.wordpress.com/2012/09/tolkappiyar.jpg'  # Replace with the URL of the image you want to display

    context.bot.send_photo(chat_id=chat_id, photo=image_url)

# Inside your main function or dispatcher setup
                                                      

def about_tholkaappiyam(update: Update, _: CallbackContext) ->None:
                update.message.reply_text("""
            Tolkāpiyam (tholkaappiyam) is an endeavour on the grammar of the Tamil vernacular and the initial extant work of Tamil publications and linguistics.
            It is the most ancient extanct of Tamil Grammar Text and the oldest extant long work of Tamil literature


            It has 3 adhikaaram (volumes) namely:
            1. எழுத்ததிகாரம் 
            2. சொல்லதிகாரம்
            3. பொருளதிகாரம்

            Each adhikaaram has 9 iyals (chapters)
            Under each Iyal have a specific number of songs/paadal (or Sutrās).
            Songs are classified into Categories
            If we analyse the songs as categories, it is easier to understand the core meaning of the Sutrās.


            Pandit S. Subrahmanya Sastri (1890-1978) was the first person to Translate tholkaappiyam into English.
                """)
def display_adhikaaram(update: Update, _: CallbackContext) -> None:
    """
    Displays the 3 adhikaarams present in tholkaappiyam with english meaning
    """
    adhikaaram={tk[i]['adhikaaram']:tk[i]['adhikaaram_eng'] for i in range(len(tk))}
    temp=pd.DataFrame([adhikaaram.keys(),adhikaaram.values()]).T
    temp.columns=['அதிகாரம்','Volume']
    temp.index=temp.index+1
    update.message.reply_text(temp.to_markdown())


def display_iyal(update: Update, _: CallbackContext):
    """
    Displays the 9 iyals present in the given adhikaaram with English meaning.
    """
    
    if len(update.message.text.split()) != 2:
        update.message.reply_text("Please provide a valid adhikaaram number.")
        return

    try:
        adhikaaram_no = int(update.message.text.split()[1])

        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"
        
        
        
        iyal = {
            tk[adhikaaram_no-1]['iyal'][i]['iyal_name']: tk[adhikaaram_no-1]['iyal'][i]['iyal_eng']
            for i in range(len(tk[adhikaaram_no-1]['iyal']))
        }
        
        temp = pd.DataFrame([iyal.keys(), iyal.values()]).T
        temp.columns = ['இயல்', 'Chapters']
        temp.index = temp.index + 1

       
        message = f"{tk[adhikaaram_no-1]['adhikaaram']} : {tk[adhikaaram_no-1]['adhikaaram_eng']}\n\n"
        message += temp.to_markdown()

      
        update.message.reply_text(message)
    except ValueError:
        update.message.reply_text("Invalid adhikaaram number. Please provide a valid number.")
    except AssertionError as e:
        update.message.reply_text(str(e))



class Adhikaaram:
    def __init__(self, adhikaaram_no: int):
        assert 0 < adhikaaram_no < 4, "adhikaaram_no must be 1, 2, or 3"
        self.adhikaaram_no = adhikaaram_no

    def display_total_no_of_songs(self):
        """
        Displays the total number of songs in an Adhikaaram
        """
        all_songs = []
        for i in range(len(tk[self.adhikaaram_no - 1]['iyal'])):
            n = tk[self.adhikaaram_no - 1]['iyal'][i]['noorpa']
            for j in range(len(n)):
                all_songs.append(tk[self.adhikaaram_no - 1]['iyal'][i]['noorpa'][j]['paadal'])
        return f"There are totally {len(all_songs)} noorpa in {tk[self.adhikaaram_no - 1]['adhikaaram']}"

    def iyals_paadal_count_dict(self):
        """
        Returns a dict containing iyals of the adhikaaram and the number of paadal in each iyal
        """
        c = {}
        for i in range(9):
            c.update({tk[self.adhikaaram_no - 1]['iyal'][i]['iyal_name']: len(tk[self.adhikaaram_no - 1]['iyal'][i]['noorpa'])})
        return c


def display_total_no_of_songs1(update: Update, _: CallbackContext):
    if len(update.message.text.split()) != 2:
        update.message.reply_text("Please provide a valid adhikaaram number.")
        return

    try:
        adhikaaram_no = int(update.message.text.split()[1])
        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"

        adhikaaram = Adhikaaram(adhikaaram_no)
        result = adhikaaram.display_total_no_of_songs()
        update.message.reply_text(result)
    except ValueError:
        update.message.reply_text("Invalid adhikaaram number. Please provide a valid number.")
    except AssertionError as e:
        update.message.reply_text(str(e))


def iyals_paadal_count_dict(update: Update, _: CallbackContext):
    if len(update.message.text.split()) != 2:
        update.message.reply_text("Please provide a valid adhikaaram number.")
        return

    try:
        adhikaaram_no = int(update.message.text.split()[1])
        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"

        adhikaaram = Adhikaaram(adhikaaram_no)
        result = adhikaaram.iyals_paadal_count_dict()
        update.message.reply_text(str(result))
    except ValueError:
        update.message.reply_text("Invalid adhikaaram number. Please provide a valid number.")
    except AssertionError as e:
        update.message.reply_text(str(e))

class Iyal:
    def __init__(self, adhikaaram_no: int, iyal_no: int):
        assert 0 < adhikaaram_no < 4, "adhikaaram_no must be 1, 2, or 3"
        self.adhikaaram_no = adhikaaram_no
        self.iyal_no = iyal_no
    
    def display_total_no_of_songs(self) -> str:
        """
        Displays the total number of songs in the given Iyal
        """
        return f"There are totally {len(tk[self.adhikaaram_no-1]['iyal'][self.iyal_no-1]['noorpa'])} noorpa in {tk[self.adhikaaram_no-1]['iyal'][self.iyal_no-1]['iyal_name']}"

    def categories_paadal_count_dict(self) -> Dict[str, int]:
        """
        Returns a dict containing categories of the iyal and the number of paadal in each category
        """
        l = len(tk[self.adhikaaram_no-1]['iyal'][self.iyal_no-1]['noorpa'])
        x = [tk[self.adhikaaram_no-1]['iyal'][self.iyal_no-1]['noorpa'][i]['vilakkam']['paadal_category'] for i in range(l)]
        category_list = list(set(x))
        
        # Counting the number of paadal in each category
        count_list = [x.count(category) for category in category_list]

        return {category: count for category, count in zip(category_list, count_list)}

def display_total_no_of_songs(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        update.message.reply_text("Please provide a valid adhikaaram and iyal number.")
        return

    try:
        adhikaaram_no = int(context.args[0])
        iyal_no = int(context.args[1])
        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"

        iyal = Iyal(adhikaaram_no, iyal_no)
        result = iyal.display_total_no_of_songs()
        update.message.reply_text(result)
    except ValueError:
        update.message.reply_text("Invalid adhikaaram or iyal number. Please provide valid numbers.")
    except AssertionError as e:
        update.message.reply_text(str(e))

def categories_paadal_count_dict_command(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        update.message.reply_text("Please provide a valid adhikaaram and iyal number.")
        return

    try:
        adhikaaram_no = int(context.args[0])
        iyal_no = int(context.args[1])
        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"

        iyal = Iyal(adhikaaram_no, iyal_no)
        result = iyal.categories_paadal_count_dict()
        update.message.reply_text(str(result))
    except ValueError:
        update.message.reply_text("Invalid adhikaaram or iyal number. Please provide valid numbers.")
    except AssertionError as e:
        update.message.reply_text(str(e))


        
class Paadal:

    def __init__(self, adhikaaram_no: int, iyal_no: int, paadal_no: int):
        self.adhikaaram_no = adhikaaram_no
        self.iyal_no = iyal_no
        self.paadal_no = paadal_no
        assert 0 < self.adhikaaram_no < 4, "adhikaaram_no must be 1, 2 or 3"
        assert 0 < self.iyal_no < 10, "iyal_no must be in the range of 1 to 9"
        assert 0 < self.paadal_no < len(tk[adhikaaram_no - 1]['iyal'][iyal_no - 1]['noorpa']) + 1, \
            "paadal_no must be in the range of 1 to {}".format(len(tk[adhikaaram_no - 1]['iyal'][iyal_no - 1]['noorpa']))

    def paadal_data(self):
        """
        Returns the paadal data as a dictionary:
        - paadal
        - meaning of the paadal
        - category of the paadal
        - iyal of the paadal in Tamil
        - iyal of the paadal in English
        - adhikaaram of the paadal in Tamil
        - adhikaaram of the paadal in English
        """

        data = {
            "paadal": tk[self.adhikaaram_no - 1]['iyal'][self.iyal_no - 1]['noorpa'][self.paadal_no - 1]['paadal'],
            "paadal_meaning": tk[self.adhikaaram_no - 1]['iyal'][self.iyal_no - 1]['noorpa'][self.paadal_no - 1]['vilakkam'][
                'paadal_meaning'],
            "paadal_category": tk[self.adhikaaram_no - 1]['iyal'][self.iyal_no - 1]['noorpa'][self.paadal_no - 1]['vilakkam'][
                'paadal_category'],
            "paadal_iyal": tk[self.adhikaaram_no - 1]['iyal'][self.iyal_no - 1]['iyal_name'],
            "paadal_iyal_eng": tk[self.adhikaaram_no - 1]['iyal'][self.iyal_no - 1]['iyal_eng'],
            "paadal_adhikaaram": tk[self.adhikaaram_no - 1]['adhikaaram'],
            "paadal_adhikaaram_eng": tk[self.adhikaaram_no - 1]['adhikaaram_eng']
        }

        return data


def display_paadal_data(update: Update, _: CallbackContext):
    # Check if a valid argument is provided
    if len(update.message.text.split()) != 4:
        update.message.reply_text("Please provide valid adhikaaram, iyal, and paadal numbers.")
        return

    try:
        adhikaaram_no = int(update.message.text.split()[1])
        iyal_no = int(update.message.text.split()[2])
        paadal_no = int(update.message.text.split()[3])
        assert 0 < adhikaaram_no < 4, "adhikaaram number must be 1, 2, or 3"

        # Create Paadal object
        paadal = Paadal(adhikaaram_no, iyal_no, paadal_no)

        # Get the paadal data
        paadal_data = paadal.paadal_data()

        # Format the response message
        response = f"Paadal: {paadal_data['paadal']}\n" \
                   f"Meaning: {paadal_data['paadal_meaning']}\n" \
                   f"Category: {paadal_data['paadal_category']}\n" \
                   f"Iyal: {paadal_data['paadal_iyal']} ({paadal_data['paadal_iyal_eng']})\n" \
                   f"Adhikaaram: {paadal_data['paadal_adhikaaram']} ({paadal_data['paadal_adhikaaram_eng']})"

        # Send the response message
        update.message.reply_text(response)

    except ValueError:
        update.message.reply_text("Invalid adhikaaram, iyal, or paadal number. Please provide valid numbers.")
    except AssertionError as e:
        update.message.reply_text(str(e))




def main() -> None:
    updater = Updater("")
    dispatcher = updater.dispatcher
    #dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about_tholkaappiyam", about_tholkaappiyam))
    dispatcher.add_handler(CommandHandler("display_adhikaaram", display_adhikaaram))
    dispatcher.add_handler(CommandHandler("display_iyal",display_iyal))
    dispatcher.add_handler(CommandHandler("display_total_no_of_songs1", display_total_no_of_songs1))
    dispatcher.add_handler(CommandHandler("iyals_paadal_count_dict", iyals_paadal_count_dict))
    dispatcher.add_handler(CommandHandler("display_total_no_of_songs", display_total_no_of_songs))
    dispatcher.add_handler(CommandHandler("display_tholkaapiyar", display_tholkaapiyar))
    dispatcher.add_handler(CommandHandler("categories_paadal_count_dict", categories_paadal_count_dict_command))
    dispatcher.add_handler(CommandHandler("display_paadal_data", display_paadal_data))



    # Initialize ,bot
    updater.start_polling()

    updater.idle()
if __name__=="__main__":
       main()
