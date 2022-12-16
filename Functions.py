def MaxIntList(list):
    max = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
    return max

def MinIntList(list):
    min = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
    return min