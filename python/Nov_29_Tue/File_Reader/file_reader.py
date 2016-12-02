# This is an example on how to open a file as a read only text document
def open_file():
    '''
    Input: no input variables
    Usage: open and read a text file
    Output: return a list of words in the text file
    '''
    words = []
    with open('constitution.html','r') as file:
        #text = file.read()
    #return text.split(" ")
        for line in file:
            line = line.rstrip().replace('\\n','\n')
            line_words = line.split()
            for w in line_words:
                words.append(w)
    return words

def create_frenquency_dict(word_list):
    '''
    Input:
    Usage: puts the words into a dictionary so it has a
    Output: returns how many times a word is used
    '''
    frenquency = {}
    # 1) Loop through word_list
        # a) check if word is in the dictionary and add if it isn't
        # and increment count by one if it is

    for word in word_list:
        frenquency[word] = frenquency.get(word , 0) + 1


    return frenquency

def get_max_word_in_file(frenquency_dict):
    '''
    Input: A dictionary of word frenquencies
    Usage: Finds the max word user_word
    Output: None just print the max used word
    '''
    frenquency = {}

    for word in word_list:
        frenquency[word] = frenquency.get(word , 0) + 1


    return max(frenquency)



def main():

    word_list = open_file()

    #print(word_list)
    print(create_frenquency_dict(word_list))
    print(get_max_word_in_file(frenquency_dict))

main()
