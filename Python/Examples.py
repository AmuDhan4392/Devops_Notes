## Comments  in Python:
# Comments are very important while writing a program. They describe what is going on inside a program, so that a person looking at the source code does not have a hard time figuring it out.
# You might forget the key details of the program you just wrote in a month's time. So taking the time to explain these concepts in the form of comments is always fruitful.
# In Python, we use the hash (#) symbol to start writing a comment.
# Comments are for programmers to better understand a program. Python Interpreter ignores comments.

# variables:

price = 10
salary = 200.50
a=b=c = 20
x,y,z = 40

print(price)
print(salary)
print(a)
print(y)

# Strings

name = "His name is Conan O'Brien"
cat = 'My cat is named "Butters"'
na = 'Amudhan'

print(name)
print(cat)
print(na)

# Concept of Indentation

a = 5
b = 10

if a>b:
    print("a is greater than b")

    
# def function:

def areaoftriangle(b,h):
    formula_area = .5*b*h
    
    print("The area of a triangle of base",b,"and height",h,"is",formula_area,)
   
areaoftriangle(2,20)

# Input Statement:

def name():
 """ Input first and last name, combine to one string and print """
   	 fname = input("Enter your first name: ")
   	 lname = input("Enter your last name: ")
     fullname = fname + " " + lname

     print("Your name is:", fullname)

name()

