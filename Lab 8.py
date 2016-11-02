#CSE Lab 8

def buildIndex(text):
    text = text.lower().replace('.'and','and'!'and'?','')
    dictionary = {}
    words = text.split(' ')

    temp_list = words[:]
    #creates copy of the separated words
    for word in words:
        if word in dictionary:
            dictionary[word].append(temp_list.index(word))
                
        else:
            dictionary[word] = [words.index(word)]
            temp_list[words.index(word)] = 'randomwordthatihopeisnttested'
    return dictionary
    
#so far it works for word counts of 1 - 2
def displayIndex(dictionary):
    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        print (key + ':'+ str(dictionary[key]))
    

def main():
    text = input("Enter text here: ")
    dictionary = buildIndex(text)
    print(displayIndex(dictionary)) 

#For some reason it prints None at the end
main()

