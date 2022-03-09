#dizinin en büyük elemanını bulma

def largest(arr):

    max = arr[0]

    for i in range(1,len(arr)):

        if arr[i] > max:
            max = arr[i]
    return max

print(largest([1,2,-2,-10]))