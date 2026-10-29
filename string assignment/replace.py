#Replace a word with another word in a sentence

s = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

result = s.replace(old_word, new_word)

print("Updated sentence:", result)