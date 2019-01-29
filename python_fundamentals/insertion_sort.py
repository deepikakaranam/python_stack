
def insertionSort(list):
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else:
                break
    print(list)


insertionSort([50, 32, 25, 2, 77])
