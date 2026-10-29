#find the longest word in a sentence

s = "Python is a powerful programming language"

words = s.split()
longest = max(words, key=len)

print("Longest word:", longest)