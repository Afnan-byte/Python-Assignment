a = int(input("enter a value"))
b = int(input("eneter next value"))
c = a + b
print(c)


# To Calculate the simple intrest
p = int(input("enter the principle amount"))
r = int(input("eneter the rate of intrest"))
n = int(input("No.of days"))
i = (p*r*n)/100
print("your simple intrest rate is ",i)


#Pass or Failed
d = int(input("Enter your mark "))
if d < 50:
    print("You failed in exam")
else:
    print('Paased')


#multiplication table
k = int(input("enter a number"))
for x in range(1,11,1):
    d= k*x
    print(k,'*',x,'=',d)


#sum of odd numbers
p = int(input("enter a number"))
sum = 0
for x in range(1,p+1,2):

    sum = sum + x


print("sum of odd number is", sum)

#Number pyramid
row = int(input("enter no.of rows"))

for x in range (1,row+1,1):
    set = []
    for y in range(1,x+1,1):

        set.append(y)
    print(set)


#swapping
size = int(input("enter the size of array1"))
a1 = []
for x in range (1,size+1,1):
    array1 = int(input(f"enter the {x} values in array1"))
    a1.append(array1)
size = int(input("enter the size of array2"))
a2 = []
for y in range (1,size+1,1):
    array2 = int(input(f"enter the {y} values in array2"))
    a2.append(array2)


print("your array 1 is ",a2)
print("your array2 is ",a1)

#even number in array
s = int(input("enter the size of the array"))
array =[]
for x in range(1,s+1,1):
    inp = int(input(f"eneter the {x} number of the array"))

    if inp % 2 == 0:
        array.append(inp)
print(array)

#descending order
z = int(input("enter the size of the array"))
arraynew =[]
for x in range(1,z+1,1):
    inp = int(input(f"eneter the {x} number of the array"))
    arraynew.append(inp)
arraynew.sort(reverse = True)
print(arraynew)

#palidrom
value =  input("enter a word")
if value == value[::-1]:
    print(f"{value} is a palidrom")
else:
    print("its not a palidrom")


#income tax
income = int(input("eneter a amount"))
tax = income/2
print("income tax is",tax)


#pyramid 2
row = int(input("eneter no.of rows"))
n = 1
for x in range(1,row+1):
    for y in range(1,x+1):
        print(n,end="")
        n += 1
    print()





