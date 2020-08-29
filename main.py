import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "This word doesn't exist in the english language..."

word = input("Enter Word: ")

print(translate(word))
