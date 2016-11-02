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
            #I want it so that the temp_list is modified so that string takes place of word
            temp_list[temp_list.index(word)] = 'randomwordthatihopeisnttested'       
        else:
            dictionary[word] = [words.index(word)]
            #only runs the first time word is recognized
            temp_list[words.index(word)] = 'randomwordthatihopeisnttested'
    return dictionary

def displayIndex(dictionary):
    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        print (key + ':'+ str(dictionary[key]))
    

def main():
    text = input("Enter text here: ")
    dictionary = buildIndex(text)
    print("Index Contents:")
    print(displayIndex(dictionary))
    

#For some reason it prints None at the end
main()

