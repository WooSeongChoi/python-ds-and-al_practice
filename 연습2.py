array = [1,2,3,4,5,6,7,8,9]
mid = len(array)//2
left = array[:mid]
right = array[mid:]
print(left)
print(right)
print(right or left)
print(left or right)
print([] or right)
print([] or [])

print((left or right) + [11,22,33])