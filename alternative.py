#step1
string = "I am learning to code"
new_string = ""

for i in range(len(string)):
   if i % 2 == 0:
       new_string += string[i].upper()
   else:
       new_string += string[i].lower()

print(new_string)

#step 2
string = "I am learning to code"

words = string.split()

for i in range(len(words)):
    if i % 2 == 0:
        words += words[i].upper()
    else:
        words += words[i].lower()

new_string = " ".join(words)

print(new_string)