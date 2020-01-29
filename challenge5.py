def english_to_piglatin(word):
    '''english_to_piglatin(word) -> string
    Translates word into Pig Latin.'''
    # First letter is vowel
    if word[0] in 'aeiou':
        return word + 'way'
   
    # First letter is consonant
    consonants = ''                                  # keep track of consonants at start of word
    originalWord = word                              # store value of word
    while len(word) > 0 and word[0] not in 'aeiou':
        consonants += word[0]                        # add the consonant
        word = word[1:]                              # remove the first letter from word
    rearrangedWord = word + consonants               # Pig Latin word without correct capitalization
    finalWord = ''                                   # empty string to add finalized letters to
    for i in range(len(originalWord)):
        if rearrangedWord[i].isupper() == originalWord[i].isupper(): # capitalization of letter is correct
            finalWord += rearrangedWord[i]
        elif originalWord[i].isupper():              # capitalization of letter is false, needs to be capitalized
            finalWord += rearrangedWord[i].upper()
        else:                                        # capitalization of letter is false, needs to be lowercased
            finalWord += rearrangedWord[i].lower()
    return finalWord + 'ay'

# Test suite
print(english_to_piglatin("John"))
print(english_to_piglatin("JoHn"))
print(english_to_piglatin("JohNnY"))
print(english_to_piglatin("a"))
