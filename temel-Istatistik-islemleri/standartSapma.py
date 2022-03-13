#Standart sapma
from gettext import install
import math



arr = [6,2,3,1,5,9]
def Ortalama(arr):
    return sum(arr)/len(arr)

def standartSapma(arr):
    for i in arr:
        std = math.sqrt( sum([abs(i-Ortalama(arr))**2 for i in arr]) / len(arr) )

        return std

print(standartSapma(arr))