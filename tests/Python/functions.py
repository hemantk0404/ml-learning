def my_function():
  print("Hello from a function")


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 

#Arbitary arguments 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

#Keyword argument
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

#arbitracy keyword argument
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#Passing a list 
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)




def call_by_value(x):
    x = x * 2
    print("in function value updated to", x)
    return

def call_by_reference(list):
    list.append("D")
    print("in function list updated to", list)
    return

my_list = ["E"]
num = 6
print("number before=", num)
call_by_value(num)
print("after function num value=", num)
print("list before",my_list)
call_by_reference(my_list)
print("after function list is ",my_list)

#Pass by Value and Pass by Reference in Python
#You might want to punch something after reading ahead, so brace yourself. Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 
#Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.
#You can check the difference between pass-by-value and pass-by-reference in the example below:
