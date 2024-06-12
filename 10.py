def count_occurrences(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count

arr=[1 , 2 , 2 , 2 , 2 , 3 , 4 , 7 , 8 , 8]
n = len(arr)
x=int(input("Enter the number to be occurance"))
print(count_occurrences(arr, n, x))
