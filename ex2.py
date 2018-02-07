raw_input = input("What is your name? ")
name = str(raw_input).upper()
print ("Hello, " + name +"!")
print ("Your name has", len(name), "characters in it. AWESOME!")
for char in name:
    print (char)