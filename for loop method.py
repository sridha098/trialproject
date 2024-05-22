#https://pynative.com/python-for-loop/
a = range(10)
print(a)

a = range(10)
c = list(a)
print(c)

a = [1,2,3,4,5,6]
for i  in a:
    print(i)
    
a = [1,2,3,4,5,6]
for i in a:
    print(i,end=" ")


for i in range(5):
    print(i,end="")

## pass break continue

for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)
# continue method 
for a in "ether":
    if a == "e":
        continue
    print(a)
        
# continue method 
for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)
#  1 to 5 loop method 
for t in range(1, 5):
    if t == 1:
        print('One')
    elif t == 2:
        print('Two')
    else:
        print('else block execute')

# split method in for loop

name="python output based questions"
cd = name.split()
for i in cd:
    print(i)

name="python output based questions"
cd = name.split()
for i in cd:
    if i =="python":
        print("yes",i)
    elif i =="output":
        print("yes",i)
    else:
        print("in valid")

# name loop method

for letter in 'mohanraj':
    if letter == 'j' or letter == 'a' or letter == 'n' or letter =='r':
        continue
    for i in letter:
        print(i)
        
# dict method

a = {"guru": "mohan", "user": "client"}

for i, j in a.items():
    print(i, j)

#dict method

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
        'Modi': 'The Changer'}
 
for key, value in king.items():
    print(key)
    
    print(value)

# for lopp and if method
s = ['cat','dog','mouse','horse','bird']

add = []
for animal in s:
    if animal not in add:
        add.append(animal)
print(add)


# overlaping method 

city1 = [10, 20, 30, 40, 50]
city = [60, 70, 80, 90]
for item in city1:
    if item in city:
        print("overlapping")
    else:
        print("not overlapping")


# odd or even method 
numbers = [1,2,3,4,5,6,7,8]
odd_i = []
even_i = []
for i in range (len(numbers)):
    if i % 2:
        even_i.append(numbers[i])
    else :
        odd_i.append(numbers[i])
 
print(odd_i)
print(even_i)



a = [2, 3, 4]
s = [20, 30, 40]
add = []
for i in a:
    for j in s:
        add.append(i+j)
print(add)


df= [1,2,3,4,5,6,7,8,9,10]
cd =[]
for i in df:
    if i >= 3 and i <=10:
        cd.append(i)
    else:
        print(i)
print(cd)



df= ["mohan","guru","chandru","hari","vidya","achu","prasath mba"]
cd =[]
for i in df:
    if i =="vidya" or i =="achu":
        cd.append(i)
    else:
        pass
print(cd)


place = ["covai","1234","tirpur","4521","salem"]
cd = []
dc = []
for rev in place:
    c = rev.isdigit()
    if c == True:
        cd.append(c)
    else:
        dc.append(c)
print(cd)
print(dc)





