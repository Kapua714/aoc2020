f = open("input.txt")
print(f)
alist = f.readlines()
print(alist)
numbers=[]
for x in alist:
    numbers.append(int(x))
print(numbers)
for x in numbers:
    #x+y=2020 y=2020-x
    y=2020-x
    if y in numbers:
        print(x*y)