# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-3])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet ='abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet.find("h"), alphabet.find("i"), alphabet.find("j"))
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
famous = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(famous.find(" John F. Kennedy " ))
print(famous[83:99])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
given= "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(given.replace("Good is subjective."," "))

# b. Extract every third word.
word = given.split()
splitInfo= word 
thirdWord = splitInfo[::3]
result= " ".join(thirdWord)
print(result)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

jobInfo= splitInfo[::-1]
print(jobInfo)
result = " ".join  (jobInfo)
print(result) 

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
star = "MAY THE FORCE BE WITH YOU"
print(star.upper())
print(star.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
result = " ".join(motto)
print(result)
# b. Now, split the string at every occurrence of the letter 'a'.
noA = result.split('a')
print(noA)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
life= "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(life.replace("busy", "distracted"))
# b. Replace "plans" with "mistakes".
print(life.replace("plans", "mistakes "))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
ite = "Iteration"
print(ite* 7 )

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote.find("moonlight"))
moonlight = False
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
super = "Supercalifragilisticexpialidocious"
print(len(super))
