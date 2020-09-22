#write a python program to print all positive numbers in a range.

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("input List 1:", list1)
print("input List 2:", list2)

for n in list1:
  if n < 0:
    list1.remove(n)

print("output List 1:", list1)

for n in list2:
  if n < 0:
    list2.remove(n)

print("output List 2:", list2)
