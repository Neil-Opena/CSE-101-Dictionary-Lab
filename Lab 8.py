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
    #FIX ME
    #doesnt include the first occurance of word
    #repeats the same position ex: 9,9,9

def displayIndex(dictionary):
    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        print (key,':',dictionary[key])
    

def main():
    text = input("Enter text here: ")
    dictionary = buildIndex(text)
    #print (dictionary)
    print(displayIndex(dictionary)) 


main()
 


