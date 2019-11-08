"""
Peter Mastropaolo
Functions that convert files to dictionaries and lists and strings to lists
"""
def filetolist(file):
    dictionaryFile = open(file)
    englishWords = []
    for word in dictionaryFile.read().split('\n'):
        englishWords.append(word)
    dictionaryFile.close()
    return englishWords

def filetodict(file):
    """
    Converts a file into a dictionary
    :param file: file to be converted
    :return: dictionary
    """
    fn = open(file)
    dict = {}
    for line in fn.readlines():
        line1 = line.split()
        dict[line[0]] = line1[1:]
    fn.close()
    return dict


def filetolist1(file):
    """
    Creates a list from a file
    :param file: file to be converted
    :return: list
    """
    fn = open(file)
    lst = []
    new = fn.readlines()
    for line in new:
        lst.append(line.strip('\n'))
    fn.close()
    return lst


def stringtolist(string):
    """
    Converts a string to a list
    :param string: string to be converted
    :return: list
    """
    newstring = string.split()
    return newstring
