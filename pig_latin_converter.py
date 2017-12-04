# created by jenny trac
# created on nov 29 2017
# program converts sentences to pig latin

import ui

def convert_word_to_pig_latin(english_word):
    # function converts a single word to pig latin
    
    word_length = len(english_word)
    first_letter_of_word = english_word[0]
    pig_latin_word = ''
    for letter in range(1, word_length):
        pig_latin_word = str(pig_latin_word) + str(english_word[letter])
    pig_latin_word = str(pig_latin_word) + str(first_letter_of_word) + "ay"
    return_statement = str(pig_latin_word)
    
    return return_statement

def convert_touch_up_inside(sender):
    # button to convert entire sentence to pig latin
    
    # variables
    pig_latin_sentence = ' '
    
    # input
    english_sentence = str(view['english_sentence_textfield'].text).split(' ')
    
    # process
    for every_word in english_sentence:
        new_pig_latin_word = convert_word_to_pig_latin(every_word)
        pig_latin_sentence = pig_latin_sentence + " " + str(new_pig_latin_word)
    
    view['converted_label'].text = pig_latin_sentence

view = ui.load_view()
view.present('sheet')
