#Find the longest substring of unique letters in a given string of n letters


def find_unique(string):
    found = set()
    last = ''
    sub = ''
    longest = ''
    for l in string:
        if l != last and l not in found:
            #Adding an item into the set
            found.add(l)
            last = l
            sub += l
        else:
            #Comparing newest string to the longest one
            if len(longest) < len(sub):
                longest = sub
            #Resetting the set and sub string, putting the last letter as the first one in the sub string
            found = set()
            found.add(l)
            sub = ''
            sub += l
    
    return longest


if __name__ == '__main__':
    string = 'alppkgtcect'
    print(find_unique(string))