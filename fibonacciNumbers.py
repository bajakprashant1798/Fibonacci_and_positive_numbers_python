#Fibonacci numbers

number = int(input("Enter number.."))
n = 0
m = 0
temp = 1

while(n<number):
  m = n + m
  n = temp
  temp = m
  print(m)
