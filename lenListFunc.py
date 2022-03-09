def findLen(myList):
    sayac = 0

    for j in myList:
        sayac += 1

    return sayac

print(findLen([1,2,3,"1","1",""]))