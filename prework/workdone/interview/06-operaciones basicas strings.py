'''
astring = "Hello world!"
astring2 = 'Hello world!'

astring3 = "Hello world!"
print("single quotes are ' '")
print(len(astring3))

astring4 = "Hello world!"
print(astring4.index("o"))

astring5 = "Hello world!"
print(astring5.count("l"))

astring6 = "Hello world!"
print(astring6[3:7])

astring7 = "Hello world!"
print(astring7[3:7:2])#3 from the end

astring8 = "Hello world!"
print(astring8[3:7])
print(astring8[3:7:1])

astring9 = "Hello world!"
print(astring9[::-1]) #reverse

astring10 = "Hello world!"
print(astring10.upper())
print(astring10.lower())

astring11 = "Hello world!"
print(astring11.startswith("Hello"))
print(astring11.endswith("asdfasdfasdf"))

astring12 = "Hello world!"
afewwords = astring12.split(" ")
print(afewwords)
'''



#s= "Strings are awesome!"
s = "________a___________"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))










