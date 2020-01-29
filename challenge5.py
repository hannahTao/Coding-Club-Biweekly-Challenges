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

inputString = input("What do you want to convert to Piglatin? (No punctuation, numbers, symbols, etc.)")
inputList = inputString.split()
punctuationBool = True

for word in inputList:
  for letter in word:
    if not letter.isalpha():
      punctuationBool = False
      break

if not punctuationBool:
  print("I said no punctuation, numbers, or symbols!!")
else:
  outputString = ''
  for word in inputList:
    outputString += english_to_piglatin(word)
    outputString += ' '
  print(outputString)
