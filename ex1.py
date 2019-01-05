#R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i and False otherwise.

def multiple(n,m):
    if n%m==0:
        return True
    else:
        return False
    
print(multiple(1,1))

#R-1.2 Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators.
def even(k):

    if k>9:
        k_str=str(k)
        k=int(k_str[len(k_str)-1])
    while k>=2 :
        k=k-2
    if k==0:
        return True
    else:
        return False

print(even(10201))

#R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.

def minmax(data):

    mini=data[0]
    maxi=data[0]
    for i in range(len(data)):
        if data[i]>maxi:
            maxi=data[i]
        if data[i]<mini:
            mini=data[i]
    return maxi, mini
print(minmax([1,4,555,2,11111,0,-1]))

#R-1.4 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.
def sumsquare(n):
    sum=0
    for i in range(n):
        sum=sum+i**2
    return sum

print(sumsquare(100))

#R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
#on Python’s comprehension syntax and the built-in sum function.
def sumsquare_withbuiltin(n): 
    return sum([i**2 for i in range(n) ])

print(sumsquare_withbuiltin(100))

#R-1.6 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the odd positive integers smaller than n.
def sumsquare_odd(n):
    alloddsquares=[]
    for i in range(n):
        if i%2==1:
            alloddsquares.append(i**2)    
    return sum(alloddsquares)

print(sumsquare_odd(100))

#R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
#on Python’s comprehension syntax and the built-in sum function.

def sumsquare_odd_withbuiltin(n): 
    return sum([i**2 for i in range(n) if i%2==1 ])

print(sumsquare_odd_withbuiltin(100))

#R-1.8 Python allows negative integers to be used as indices into a sequence,
#such as a string. If string s has length n, and expression s[k] is used for index
#−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
#the same element?
s="San Francisco"
print(s[-2])
print(s[(len(s)-2)])

#R-1.9 What parameters should be sent to the range constructor, to produce a
#range with values 50, 60, 70, 80?l
def rangecons(start, stop, step): 
    return [i for i in range(start, stop, step)] #[start, stop, step]
print(rangecons(50, 81,10))
#R-1.10 What parameters should be sent to the range constructor, to produce a
#range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
print(rangecons(8,-9,-2))

#R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
#the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

print([2**i for i in range(9)])
   
#R-1.12 Python’s random module includes a function choice(data) that returns a
#random element from a non-empty sequence. The random module includes
#a more basic function randrange, with parameterization similar to
#the built-in range function, that return a random choice from the given
#range. Using only the randrange function, implement your own version
#of the choice function.
import random
def choice(data):
    return data[random.randrange( len(data))]
print(choice([1,2,3,4,5]))

#
#C-1.13 Write a pseudo-code description of a function that reverses a list of n
#integers, so that the numbers are listed in the opposite order than they
#were before, and compare this method to an equivalent Python function
#for doing the same thing.

def reverse(data):
    return [data[len(data)-i-1] for i in range(len(data))]
print(reverse([1,2,3,4,5]))


data=[1,2,3,4,5]
data.reverse()
print(data)
#C-1.14 Write a short Python function that takes a sequence of integer values and
#determines if there is a distinct pair of numbers in the sequence whose
#product is odd.

def product_odd(data):
    if len(data)>1:
        data1=data[0]
        data2=data[1:len(data)]
#        a=[ data2[i] for i in range(len(data2)) if (data1*data2[i])%2 == 1 ]
#        if a!=[]:
#            print([data1, a])
        for i in range(len(data2)):
            if (data1*data2[i])%2 == 1:
                print(data1, data2[i])
    else: 
        return False
    return product_odd(data2)
product_odd([1,2,3,4,5])
#C-1.15 Write a Python function that takes a sequence of numbers and determines
#if all the numbers are different from each other (that is, they are distinct).

def isDistint(data):
    data1=data[0]
    if len(data)>1:
        
        data2=data[1:len(data)]
#        a=[ data2[i] for i in range(len(data2)) if (data1*data2[i])%2 == 1 ]
#        if a!=[]:
#            print([data1, a])
        for i in range(len(data2)):
            if data1==data2[i]:
                print("NOT distinct")
                return False
            else:
                return isDistint(data2)
    else: 
        print("Distinct")
        return True
    
isDistint([1,2,3,4,5])
isDistint([1,2,3,4,5,5])


#C-1.16 In our implementation of the scale function (page 25), the body of the loop
#executes the command data[j] = factor. We have discussed that numeric
#types are immutable, and that use of the = operator in this context causes
#the creation of a new instance (not the mutation of an existing instance).
#How is it still possible, then, that our implementation of scale changes the
#actual parameter sent by the caller?



#C-1.17 Had we implemented the scale function (page 25) as follows, does it work
#properly?
#def scale(data, factor):
#for val in data:
#val = factor
#Explain why or why not.

#C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
#the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
print([(i+1)*i for i in range(10)])
#C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
#the list [ a , b , c , ..., z ], but without having to type all 26 such
#characters literally.
print([chr(i+97) for i in range(26)])
#C-1.20 Python’s random module includes a function shuffle(data) that accepts a
#list of elements and randomly reorders the elements so that each possible
#order occurs with equal probability. The random module includes a
#more basic function randint(a, b) that returns a uniformly random integer
#from a to b (including both endpoints). Using only the randint function,
#implement your own version of the shuffle function.

#C-1.21 Write a Python program that repeatedly reads lines from standard input
#until an EOFError is raised, and then outputs those lines in reverse order
#(a user can indicate end of input by typing ctrl-D)
class student:
    def __init__(self,name,school,idiwka,year):
        self._name=name
        self._school=school
        self._idiwka=idiwka
        self._year=year
    def get_name(self):
        return self._name
    