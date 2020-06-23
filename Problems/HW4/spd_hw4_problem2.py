#Given a list of n numbers, determine if it contains any duplicate numbers


def find_duplicate(arr):
    arr.sort()
    last = 0
    for i in arr:
        if last == arr[i]:
            return arr[i]
        last = arr[i]

if __name__ == '__main__':
    arr = [6,1,3,4,6,7,9]
    print(find_duplicate(arr))