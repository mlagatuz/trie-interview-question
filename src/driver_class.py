from my_trie import Trie
from collections import deque

def main():
    # Algorithm
    #   add first word from each phrase into a set
    #   insert set into Trie
 
    list_of_phrases = [ "this is a description", 
                        "this is why we speak",
                        "some sort of phrase",
                        "that is what I said",
                        "those are my pictures" ]

    first_words = set()
    print(first_words)

    # Which is more readable: traditional for loop or list comprehension?

    for phrase in list_of_phrases:
        first_words.add(phrase[0:phrase.find(' ')])
    
    #first_words.append([phrase[0:phrase.find(' ')] for phrase in list_of_phrases])
    print(first_words)
    
    trie = Trie()
    for word in first_words:
        trie.insert(word)
    
    input = "tho"

    if trie.search(input):
        print("FOUND")
    else:
        print("NOT FOUND")

if __name__ == '__main__':
    main()