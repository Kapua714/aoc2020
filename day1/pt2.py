f = open("input.txt")
print(f)
alist = f.readlines()
print(alist)
numbers=[]
for x in alist:
    numbers.append(int(x))
print(numbers)
for i in range(len(numbers)):
    x=numbers[i]
    for y in numbers:
        z=2020-x-y
        if z in numbers:
            print(x*y*z)
    #x+y=2020 y=2020-x