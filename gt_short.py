import googletrans
from random import randint

def choose_lang1():  # New Param: my_ads_paragraph
    choice_num = randint(0, 5)
    y = ['zh-cn', 'en', 'de', 'es', 'pt', 'ko']  # list of destination language codes
    language_choice = y[choice_num]
    return language_choice

def choose_lang2():  # New Param: my_ads_paragraph
    choice_num = randint(0, 5)
    y = ['zh-cn', 'en', 'de', 'es', 'pt', 'ko']  # list of destination language codes
    language_2c = y[choice_num]
    return language_2c

# MAIN METHOD
def translate_twice(x):  # Use Random Language Codes to Recycle English To Slightly Alter Syntax/Diction
    lang = choose_lang1()
    lang2 = choose_lang2()
    first = googletrans.Translator().translate(text=x, dest=lang, src='en').text
    second = googletrans.Translator().translate(first, dest='en', src=lang).text
    third = googletrans.Translator().translate(second, dest=lang2, src='en').text
    english_cycled = googletrans.Translator().translate(third, dest='en', src=lang2).text
    return english_cycled

# TEST
# ogp = "I am speaking english right now with a lot of confidence, please do your best if you are a snake!"
# print(translate_twice(ogp))
