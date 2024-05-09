list_1 = [1, 2, 3, 4, 5, 1, 3]
list_2 = []
print(list_1)
print(list_1)

print(len(list_1))

list_1[3] = 9999
print(list_1)

list_1.append(100)
print(list_1)

list_1 = [1, 2, 3, 9999, 5, 1, 3, 100]
list_2 = []
print(list_1)

list_1.remove(9999)
print(list_1)

list_1.insert(0.777)
print(list_1)

list_2 = list_1.copy()
print(list_2)

list = [1, 2, 3, 5, 1, 3]

for num in list :
    print(num)
