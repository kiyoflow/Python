n = int(input())
arr = map(int, input().split())

#map() changes string to integer
#.split() splits up a string into seperate words


sorted_numbers = sorted(set(arr), reverse=True) 

if len(sorted_numbers) > 1:
    print(sorted_numbers[1])
else:
    print("No second largest number")
