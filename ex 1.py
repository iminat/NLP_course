sentence = "George Bool is an English mathematician, philosopher and logician"

print('George' in sentence) #True

print(sentence.index('is')) #12

words = sentence.split()
print(words.index('philosopher'))

print(words[3]) #an

print(words[1][::-1]) # looB

first_word = words[0]
last_word = words[-1]
concatenated = first_word + last_word
print(concatenated) # Georgelogician

#for i in range (len(words)):
#    if i%2 == 0:
#        print(words[i], end= ',')

print(sentence[-4:])

print(sentence[::-1])

reversed_words = []
for word in words:
    reversed_word = ""
    for letter in reversed(word):
        reversed_word += letter
    reversed_words.append(reversed_word)
print(reversed_words)







