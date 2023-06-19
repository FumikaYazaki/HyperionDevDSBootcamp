"""
Instructions
You are helping your younger sister with her English vocabulary homework, which she's finding very tedious. Her class is learning to create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with correct spelling by adding the prefix to the beginning or the suffix to the ending.
There's four activities in the assignment, each with a set of text or words to work with.
"""
#Add a prefix to a word
#One of the most common prefixes in English is un, meaning "not". 
#In this activity, your sister needs to make negative, or "not" words by adding un to them.

def add_prefix_un(word):
    print("un", word, sep="")
add_prefix_un("happy")

#Add prefixes to word groups
#There are four more common prefixes that your sister's class is studying: 
# en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), 
#auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').
#In this exercise, the class is creating groups of vocabulary words using these prefixes, 
#so they can be studied together. Each prefix comes in a list with common words it's used with. 
#The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.
def make_word_group(prefix, word1, word2, word3):
    result = [prefix, (prefix + word1), (prefix + word2), (prefix + word3)]
    return " :: ".join(result)

word_group = make_word_group("en", "close", "joy", "lighten")
print(word_group)

#3. Remove a suffix from a word
#ness is a common suffix that means 'state of being'. 
# In this activity, your sister needs to find the original root word by removing the ness suffix. 
# But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', 
# then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. 
# e.g. happiness --> happi --> happy.
def remove_suffix_ness(word):
    after_removed_ness = word[:-4]
    if after_removed_ness[-1] == "i":
        after_removed_ness = after_removed_ness[:-1] + "y"     
    else:
        pass
    return after_removed_ness

input_word = remove_suffix_ness("happiness")
print(input_word)

#4. Extract and transform a word
#Suffixes are often used to change the part of speech a word has.
#A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an en suffix.
#In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. 
#Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.
def adjective_to_verb(sentence, index):
    split_sentence = sentence.split()
    word_to_verbify = split_sentence[index]
    if word_to_verbify[-1] == ".":
        word_to_verbify = word_to_verbify[:-1] + "en"
    else:
        word_to_verbify = word_to_verbify + "en"   
    return word_to_verbify
input = adjective_to_verb('I need to make that bright.', -1)
print(input)
