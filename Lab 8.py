#CSE Lab 8

def buildIndex(text):
    #creates an empty dictionary to hold final result
    dictionary = {}
    words = text.split(' ')
    mylist = []
    mylist.append(words)
    print (mylist)
    #uses split() to break into list of words


text = input("Enter text here")
buildIndex(text)

