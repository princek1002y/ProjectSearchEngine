print ("Welcome!")
#Asking for input for text
print("Write a text")
#declaring the "text" variable
text = input()
#Asking for input for word
print("Write a word")
#declaring the "word" variable
word = input()
#creating the function search with
#2 variables x and y
#Applying "search" its function
def search(x,y):
    if x in y:
        return "Word Found!"
    else:
        return "Word not found!"
#final output statement
print(search(word,text))