import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()] #in case user enters words like USA or NATO
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no.: " %get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query. Pleas try again."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter your word: ")

output =translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

#dir(str) - daje wszyzskite metody do danego zapytania

#import json
#data = json.load(open("plik który chcemy załadować"))


#//https:docs.python.org/3/library/index. - stronka z bibliotekami do pythona
#import.difflib - biblioteka do porównywania stringó
#fron difflib import SequenceMatcher
#SequenceMatcher("none", "y", "x").ratio()
