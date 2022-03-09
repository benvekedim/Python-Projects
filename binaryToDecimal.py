#num'ı string alıp işlem yapabiliriz.
#binary sayiyi decimala cevirelim
#binary sayi 0 ve 1'lerden olusur

def binaryToDecimal(num):
    #num'ı int array'e donusturelim
    numArr = list(map(int,[i for i in num]))
    
    #num'da 0 ve 1 harici sayi var mi 
    for n in numArr:
        if(n == 0):
            continue
        elif (n==1):
            continue
        else:
            return "Hatali sayi"

    #2'nin kuvvetlerinden olusan dizi olusturalım
    twoArr = list(reversed([2**n for n in range(len(numArr))]))
    
    #numArr ve twoArr dizilerinin elemanları çarpıp toplayalım dondurelim
    return sum([i*j for i,j in zip(numArr,twoArr)])

print(binaryToDecimal("10000001"))