#### What is Python ?

Python is a general purpose , high level, interpreted and dynamically typed programming language.

General Purpose – A language designed to be used for writing software in various applications domains without begin restricted to a particular domain

High level – A programming language that uses  natural language elements and automate significant areas of computing such as memory allocation

Interpreted – Python script is saved and executed in the same format in which you created the script. 

Dynamically typed – Python parser automatically infers or identifies the type of variable on the basis of what kind of data you have assigned to the variable 


#### Python Syntax compared to other programming languages 

   ##### C: - Procedural Programming
      # include <studio.h>
      int main(int arg, char ** argv)
      {
      Printf(“Hello, world!\n”);
      }

   ##### Java: Object oriented Programming
      Public class Hello
      { 
       public static void main (String argv[])
      {
      System.out.println(“Hello, world!”);
      }
      }

   ##### Python: Functional Programming
      Print(“Hello World!”)


#### Why to choose python ?

Easy to learn and understand - The syntax of the python can be easily understood even by the beginners.
Free and Open source language 
Fewer code lines, less time – Python usually involves less code which in turn results in less time to write the code.
Python is increasing becoming the top preferred language for data science, app developers, devops etc..
Huge Community – which means in case you get stuck there will be many fellow developers (quora, stack overflow)  where you can reach out for help

#### What is IDE?
	An IDE (Integrated Development Environment), a text editor with added features to support programming

   ##### Types of IDE’s:

      Rodeo
      IDLE
      Spyder
      Pycharm
      PyDev

   ##### Features of IDE’s:
      Code Editor
      Syntax Highlighter
      Auto Completion
      Debugger

#### Variables :
Which is one of the most fundamental concepts in programming,   
they are not specific to python, they exist in pretty much every programming language. 
We use variables to temporarily store data in a computer’s memory. 
Variables can be assigned with single or multiple values.
 
https://github.com/AmuDhan4392/Devops_Notes/blob/main/Python/Examples.py
  
#### Keywords:
A python keyword is a reserved word which you can’t use as a name of your variable, class, function etc. 
These keywords have a special meaning and they are used for special purposes in Python programming language.

![image](https://user-images.githubusercontent.com/119385929/206261602-b82d94a3-a55f-4e7f-b548-d0a826100d40.png)


#### Creating Strings and Using them in Print Statement
 
Forming a string in python is by using quotes,  either single quotes or double quotes(‘ ‘ or “ ”). But if the string contains one, we need to use the other

#### Concept of Indentation
	
Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement. 
The statements with the same indentation belong to the same group called a suite.

#### Function in Python:

In Python, a function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

      Syntax of Function
        def function_name(parameters):
           """ statement(s) ""“

Above shown is a function definition that consists of the following components.

   1. Keyword def that marks the start of the function header.
   2. A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in python.
   3. Parameters through which we pass values to a function. 
   4. A colon (:) to mark the end of the function header.
   5. One or more valid python statements that make up the function body. Statements must have the same indentation level.

#### The "input" Statement and Combining Strings

The value of variables was defined or hard coded into the source code. 
To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this.
In Other words, Python has an input function which lets us ask a user for some text input. 
We call this function to tell the program to stop and wait for the user to key in the data.

	Example:
	num = input('Enter a number: ') 
        print(num)

#### Data Types and Data Structures:

  1. Strings
  2. Numbers
  3. Tuples
  4. Lists
  5. Sets
  6. Dictionaries

##### Numbers:

There are three numeric data types:
  1. Integer
  2. Float
  3. Complex

They are defined as  int, float and complex in python. We can use type() function to know which class a variable or a value belongs to.

	Example:
	num = 5678
	rate = 25.25
	comp = 6j+1

##### Strings:

The value of the string data type is string literal. They use to store text.

	Var 1 = “I am okay”
	Var 2 = “python tutorial”

##### Lists

A Sequence of mutable objects.  It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type. 
Items separated by commas are enclosed within brackets [ ]

	Names = [‘john’, ‘rahul’, 100, ’mary’, 5.25]

We can use the slicing operator [ ] to extract an item or a range of items from a list. The index starts from 0 in Python.
Lists are mutable, meaning, the value of elements of a list can be altered.

Adding new items to a list is also easy. (append, extend)

##### Tuples

They are similar to list where we can use them to store a list of items. But unlike list we can  not modify them. 
We say tuples are immutable (cannot mutate or change them). We can only get information about the tuple by indexing.
	
It is defined within parentheses () where items are separated by commas.

	Weeks  = (“Sunday”, “Monday”,”Tuesday”,”Wednesday”,”Thursday”,”Friday”,”Saturday”)

##### Sets

An unordered collection of immutable data which has no duplicate elements. Set is defined by values separated by comma inside braces { }.
We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.

	a = {1,2,3,4,5}
	b = {1,2,3,3,4,4,4,5,5,6}
	n = set([0, 1, 2, 3, 4, 5])


##### Dictionaries

An unordered collection of items. It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. 
We must know the key to retrieve the value.
In Python, dictionaries are defined within braces {} with each item being a pair in the form 

key : value. Key and value can be of any type.

We use key to retrieve the respective value. But not the other way around.

	d = {} creates empty dictionary
	d = {1 : ‘john’, 2:’kom’ , 3:’Alice’, 4:100, 5: 122.36}

##### Conversion of Data Types:

We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
     
    
