# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    a = sorted(A)
    b = sorted(B)
    char_diff = 0
    
    if a == b:
        return char_diff

    curr_i = 0
    curr_j = 0
    print(a)
    print(b)
    while max(curr_i, curr_j) <= max(len(a) - 1, len(b) - 1):
        #These two if statements compare letters to nothing, resulting in a difference of chars.
        if curr_i > (len(a)):
            curr_j += 1
            char_diff += 1
            continue
        if curr_j > (len(b)):
            curr_i += 1
            char_diff += 1
            continue
            
        #If there is a match, each index is moved up and the next letters are compared
        if a[curr_i] == b[curr_j]:
            curr_i += 1
            curr_j += 1
        elif a[curr_i] < b[curr_j]:
            curr_i += 1
            char_diff += 1
        else:
            curr_j += 1 
            char_diff += 1
    
    return char_diff

    
if __name__ == '__main__':
    print(solution('apple', 'pear'))