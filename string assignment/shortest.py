#find the shortest word in a sentence

s = "Python is a powerful programming language"

words = s.split()
shortest = min(words, key=len)

print("Shortest word:", shortest)