## Pig Latin Translator ##


# Get sentence form user
original = input("Please Give The sentence to Translate to pig latin : ").strip().lower()

# Split sentence into words
words = original.split()

# loop through the word and convert them to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick the word back together
output = " ".join(new_words)
# output the final string
print(output)