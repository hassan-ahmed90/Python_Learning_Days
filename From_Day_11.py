#Day 11 String

name="Hassan"
description="""   My Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.name is """
# print(description)

# for char in name : print(char)

#Day 12

#String slicing

print(len(name))
print(name[0:3])

#Day 13

#String Method

stringMethod=" Shani Cool !! "
print(stringMethod.upper())
print(stringMethod.lower())
print(stringMethod.strip())
print(stringMethod.rstrip("!"))
print(stringMethod.replace("C","M"))
print(stringMethod.split(" "))
print(stringMethod.center(50,"!"))
print(stringMethod.title())
print(stringMethod.swapcase())
print(stringMethod.startswith("Cool"))

#Day 14

a=input("Enter the no ")
if(a>18): print("Greater than 18")
elif(a==0):print("No is equal to zero")
elif(a<18):print("Less than 18")
else:print("Error in Input")