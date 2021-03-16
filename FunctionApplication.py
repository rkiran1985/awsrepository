a1="awesome"
def myFunction():

        a1 = "fantastic"
        print("Python is : "+a1)

myFunction()
print("Python is : " + a1)

# To change the value of a global variable inside a function, refer to the variable by using the Global Key Word
a1="awesome"
def myFunction():
        global a1
        a1 = "fantastic global"
myFunction()
print("Python is : " + a1)
s="r kiran"
print("*********")
print(s.upper())

x = 5
y = "R Kiran"
print(type(x))
print(type(y))

print("y[0] "+y[0])


# ARRAY
a = "Hello, World!"
print(a[1])
print(a[1].upper())