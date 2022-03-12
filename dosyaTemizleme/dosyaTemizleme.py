# txt dosyasinda satir sayisini sayalim

from turtle import clear


customerFile = open("dosya.txt","r")
sayac = 0

content = customerFile.read()

customerList = content.split("\n")

for i in customerList:
    if i:
        sayac += 1

#print("Dosyadaki satir sayisi: ",sayac)
#Output: Dosyadaki satir sayisi : 5

#dosya.txt veriler listeye attik.
#print(customerList)

#dosya temizleme

myList = [customerList[i] for i in range(1,len(customerList))]
#print(myList)

customers = []
for i in myList:
    i = i.split(",")
    customers.append(i)

# print(customers)

sutunIsimleri = customerList[0].split(",")
# print(sutunIsimleri)

#txt dosyadaki verileri temizleyip atiyoruz.

yeniArr = []

for j in range(len(customers)):
    for k in range(len(customers[j])):
        if customers[j][k] == "K" or customers[j][k] == "E":
            yeniArr.append(str(customers[j][k]))
        else:
            yeniArr.append(int(customers[j][k]))

# print(yeniArr)

cleared = []

for i in range(0, len(yeniArr), 5):
    cleared.append(yeniArr[i:i+5])

print(cleared)




