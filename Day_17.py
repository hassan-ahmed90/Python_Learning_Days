
#Day 17
name="Hassan Ahmed"
# for i in name:print(i)
# for i in range(1,10,3):print(i)
colors=["White","Green","Red",]
# for c in colors : print(c)

#Day 18
#convinient
#emulate
# i=0
# while(i<=5):
#     print(i)
#     i=i+1
# a=int(input("Enter the no "))
# while(a<=28):
#     a=int(input("No :"))
#     print(a)


#Day 19
#Break and continious

# i=0
# while(i<=5):
#     print(i)
#     if(i==3):
#         break
#     i=i+1



# for i in range(12):
#   if(i == 10):
#     continue
#   print("5 X", i, "=", 5 * i)
#
#   for j in [2, 3, 4, 6, 8, 0]:
#       if (j % 2 != 0):
#           continue
#       print(j)


#Day 20

# def meanG(a,b):
#     c=(a*b)/(a+b)
#     print(c)
# def isGreater(c,d):
#     if(c>d):
#         print("First no is greater")
#     else:
#         print("Second no is greader")
# f=100
# meanG(4,2)
# isGreater(4, 10)

#Day 21
#Arguments in Function

def average(a=9,b=8):
    print(a+b/2)

average(3,4)


def avg(*number):
    sum=0
    for i in number:
        sum=sum+i
    print(sum/len(number))
avg(2,3,4,56,6)

def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")





