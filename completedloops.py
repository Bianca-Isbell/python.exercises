# Loop Exercise 1: 1 to 10
for number in range(1, 11):
    print(number)

# Loop Exercise 2: n to m
raw_input = input("Start from: ")
start = int(raw_input)
raw_input = input("End on: ")
end = int(raw_input)
for number in range(start, end):
    print(number)

# Loop Exercise 3: Odd Numbers
even_numbers = []
odd_numbers = []

for number in range(1, 11):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
#print(even_numbers) just delete # for even numbers to be printed
print(odd_numbers)

# Loop Exercise 4: Print a Square
size = 5
for i in range(size):
    print ('*' * size)

# Loop Exercise 5: Print a Square II
raw_input = input("How big is the square? ")
big = int(raw_input)
for i in range(big):
    print ('*' * big)

# Loop Exercise 6: Print a Box
raw_input = input("Width? ")
width = int(raw_input)
raw_input = input("Height? ")
height = int(raw_input)
for i in range(height):
    if i in[0]:
        print("* "*(width))
    elif i in[(height-1)]:
        print("* "*(width))
    else:
        print("*"+"  "*(width-2)+" *")

# Loop Exercise 7: Print a Triangle

xr = 4

for x in range(0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print(' ' * spaces + '*' * stars)

# Loop Exercise 8: Print a Triangle II
raw_input = input("How big is the triangle? ")
xr = int(raw_input)


for x in range(0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print(' ' * spaces + '*' * stars)

# Loop Exercise 9: Multiplication Table
n = 10
for i in range(1, 11):
    print(n,'x',i,'=',n*i)