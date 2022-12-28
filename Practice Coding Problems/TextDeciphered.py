#For this question, your goal is to decipher a text message to plain English.
#You can ignore grammar, you're just translating common text slang into
#normal words.
#
#Write a function called text_deciphered. text_deciphered should have two
#parameters: a string representing a text message, and a dictionary representing
#a set of known abbreviations. In this dictionary, the keys are the English words
#and the values are the abbreviated words.
#
#Return a translated version of the string, replacing the abbreviated words with
#the real English words.
#
#For example:
#text_message = "Hey, wat r our plans for tn"
#abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
#text_deciphered(text_message, abbrevs) -> "Hey, what are our plans for tonight"


#Write your code here!
def get_key_by_values(dictionary, search_value):
    for key, value in dictionary.items():
        if search_value in value:
            return key

    return None

def text_deciphered(message, decoder_ring):
    slang_word = ''
    message_list = message.split()
    for word in message_list:
        if word in decoder_ring.values():
            decrypt = get_key_by_values(decoder_ring, word)
            word_location = message_list.index(word)
            message_list.remove(word)
            message_list.insert(word_location, decrypt)

    message = ' '.join(message_list)

    return message
            
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Hey, what are our plans for tonight
text_message = "Hey, wat r our plans for tn"
abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
print(text_deciphered(text_message, abbrevs))

