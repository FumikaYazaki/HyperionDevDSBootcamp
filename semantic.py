import spacy
nlp = spacy.load('en_core_web_md')

#example 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#example 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("example 3")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#I found that cat and monkey have the highest similarity, 0.59, and monkey and banana have the second highest similarity, 0.40. Cat and banana don't have much similarity as the similarity score is 0.22.
#My own example
word4 = nlp("iPhone")
word5 = nlp("PC")
word6 = nlp("notebook")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

#sample text
#Because `en_core_web_sm` is a small model that don't ship with word vectors and only use context-sensitive tensors,
# the similarity judgements are not useful enough. Using `en_core_web_sm` gives us more accurate judgment.