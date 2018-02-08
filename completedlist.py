# Lists Exercise 1: Sum the Numbers
numbers = [2, 5, 8, 22, 50]
sm = sum(numbers)
print(sm)

# Lists Exercise 2: Largest Number
numbers = [2, 5, 8, 22, 50]
largest = max(numbers)
print(largest)

# Lists Exercise 3: Smallest Number
numbers = [2, 5, 8, 22, 50]
smallest = min(numbers)
print(smallest)

# Lists Exercise 4: Even Numbers
numbers = [2, 5, 8, 13, 22, 50]

even = []

for i in numbers:

     if i%2 == 0:

       even.append(i)
print (even)

# Lists Exercise 5: Positive Numbers
numbers = [-20, -5, 2, 5, 8, 13, 22, 50]
x = [i for i in numbers if i>0]
print(x)

# Lists Exercise 7: Multiply a List
numbers = [5, 15, 25, 45]
new_numbers = [x * 2 for x in numbers]
print(new_numbers)

# Lists Exercise 8: Multiply Vectors
a = [5,10,15]
b = [3,6,9]
newlist = []

listlen = len(a)

for i in range(listlen):
    newlist.append(a[i] * b[i])
print(newlist)

# Lists Exercise 9: Matrix Addition
X = [[1, 3],
    [2, 4]]

Y = [[5, 2],
    [1, 0]]

result = [[0,0],
         [0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Lists Exercise 10: Matrix Addition II
X = [[1, 3, 1],
    [2, 4, 1],
    [1, 1, 1]]

Y = [[5, 2, 2],
    [1, 0, 2],
    [2, 2, 2]]

result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]



# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Lists Exercise 11: De-Up
a = [5,10,15,5,20,11,14,10,100]
newlist=[ii for n,ii in enumerate(a) if ii not in a[:n]]

print(newlist)