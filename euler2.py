array = [1,2]
while array[-1] <= 4000000: 
    array.append(array[-1]+array[-2])
array.remove(array[-1])

evensum = 0
for i in range(len(array)):
    if array[i]%2 == 0:
        evensum += array[i]

print(array)
print(evensum)

    
