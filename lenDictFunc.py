def findLen(myDict):

    sayac = 0

    for j in list(myDict):
        sayac += 1

    return sayac

print(findLen({"name":"Mustafa", "soyadı":"eroglu"}))