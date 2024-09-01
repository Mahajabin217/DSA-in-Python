# How Binary Search Works:

# Taking input array & target value:

user_input = input('Enter the sorted array: ')
arr = list(map(int,user_input.split()))

target_val = int(input('Enter target value: '))

# Binary Search Logic:

left = 0
right = len(arr)-1
ans = -1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target_val:
        ans = mid
        break

    if arr[mid] < target_val:
        left = mid + 1

    else:
        right = mid -1 

# Results:

if ans != -1:
    print('Found at index:', ans)
else:
    print('Not Found')


""" Output:
            Enter the sorted array: 1 3 5 7 9 11 13 15 17 19
            Enter target value: 15
            Found at index: 7
"""