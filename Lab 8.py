#CSE Lab 8

def buildIndex(text):
    text = text.lower().replace('.'and','and'!'and'?','')
    dictionary = {}
    words = text.split(' ')
    mylist = []
    
    for word in words:
        if word in dictionary:
            dictionary[word].append(words.index(word))
        else:
            dictionary[word] = list()
    return dictionary

def displayIndex(dictionary):
    keys = sorted(dictionary.keys())
    return keys
    """for key in keys:"""


text = input("Enter text here:")
dictionary = (buildIndex(text))
print (dictionary) 
print(displayIndex(dictionary)) 


