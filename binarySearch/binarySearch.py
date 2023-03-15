def binary_search(key, elements):
    middle = 0
    start = 0
    end = len(elements)
    steps = 0
    while (start <= end):
        print("steps", steps, ":", str(elements[start:end + 1]))
        steps += 1
        middle = (start + end) // 2
        if (str(key) == elements[middle]):
            return middle
        if (str(key) < elements[middle]):
            end = middle-1
        else:
            start = middle+1

    return -1


ele = []
while (True):
    elem = input("enter the numbers: ")
    ele.append(elem)
    add = input("enter another number(y,n): ")
    if (add == 'n'):
        break


key = int(input("enter the key: "))
binary_search(key, ele)
