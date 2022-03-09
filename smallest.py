#dizinin en kücük elemanını bulma

def smallest(arr):

    min = arr[0]

    for i in range(1,len(arr)):

        if arr[i] < min :

            min = arr[i]

    return min 

print(smallest([-4,-3,2,1]))