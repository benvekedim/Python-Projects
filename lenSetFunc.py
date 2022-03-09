def findLen(mySet):

    sayac = 0

    for j in list(mySet):
        sayac += 1

    return sayac

print(findLen({1,2,3,"4","merhaba"}))