def selectionsort(list):

    for i in range(len(list)):
        min = list[i]
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                min = list[j]
                list[i], list[j] = list[j], list[i]
    print(list)


selectionsort([50, 32, 25, 2, 77])
