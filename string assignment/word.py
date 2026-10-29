#check wheather a word exist in a sentence

s = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in s.split():
    print("Word exists in the sentence")
else:
    print("Word does not exist in the sentence")