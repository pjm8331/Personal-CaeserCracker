import sys
import pyperclip
import storage
import string
#Peter Mastropaolo(pjm8331)
#Decrypts a caeser cipher on your clipboard without the index/shift and puts the result on your clipboard

#Applies the Caeser Cipher decryption to the given word at the given shift index
def change(word, shift):
    ciphertext = []
    for i in range(len(word)):
        if(ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z')):
            ciphertext.append(chr((ord(word[i]) -ord('A') + shift)%26 + ord('A')))

        elif(ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z')):
            ciphertext.append(chr((ord(word[i]) -ord('a') + shift)%26 + ord('a')))

        else:
            ciphertext.append(word[i])
    return ''.join(ciphertext)

def punctcheck(word):
    """
    Checks for extra punctuation and removes it
    :param word: word to have punctuation removed
    :return: word without punctuation
    """
    remove = string.punctuation
    pattern = r"[{}]".format(remove)

    while len(word) > 0 and word[0] in pattern:
        word = word[1:]

    while len(word) > 0 and word[-1] in pattern:
        word = word[:-1]

    return word

#Compares the list of words to a dictionary to acquire its accuracy
def compare(list, listindex, keyindex, americandict):
    if(listindex == len(list)-1):
        wordcheck = change(punctcheck(list[listindex]).lower(), keyindex)
        for word in range(len(americandict)):
            if(wordcheck == americandict[word]):
                return 1
        return 0
    else:
        wordcheck = change(punctcheck(list[listindex]).lower(), keyindex)
        for word in range(len(americandict)):
            if(wordcheck == americandict[word]):
                return (compare(list, listindex+1, keyindex, americandict) + 1)
        return (compare(list, listindex+1, keyindex, americandict))


#Takes in a list of encrypted words and decrypts them
#returns decrypted string
def conversionhandler(text, americandict):
    finalstring = ''
    highestratio = 0 #The highest achieved accuracy
    highestindex = 0 #The index with the above accuracy
    for i in range(1,26):
        comparison = compare(text, 0, i, americandict)/len(text) #Compares the accuracy of the list to the current highest accuracy index
        if(comparison > highestratio): #Replaces the old index if the new one has a high enough accuracy
            highestratio = comparison
            highestindex = i
    for j in range(len(text)):
        string1 = (change(text[j], highestindex) + " ").strip('\n')
        finalstring += string1
    return finalstring
    
def main():
    americandict = storage.filetolist("20k.txt")
    text = []
    
    if len(sys.argv) == 1:
        tinput = pyperclip.paste() #Takes your current clipboard
        text = storage.stringtolist(tinput) #Converts the string to a list of strings(words)
        decrypt = conversionhandler(text, americandict) #Decrypts the Caeser Cipher
        pyperclip.copy(conversionhandler(text, americandict)) #Applies the solved message to your clipboard
        print("===================================================================================================")
    else:
        print("USAGE: py wordchecker.py")

main()