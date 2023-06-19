import spacy

#Load the English model
nlp = spacy.load('en_core_web_sm')

#Make a list of garden path sentences
gardenpathSentences = ["British left waffles on Falklands",
                       "The sour drink from the ocean.",
                       "Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."]

#passing strings through model
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    #Tokenise each sentence
    print([token.orth_ for token in doc])
    #Named entity recognition
    print([(i, i.label_, i.label) for i in doc.ents])

 #wo entitiy I looked up were NORP and GPE. NORP makes sense but GPE doesn't really make sense to me.
print(spacy.explain("NORP"))
print(spacy.explain("GPE"))