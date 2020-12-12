#!/usr/bin/env python
# coding: utf-8
string.h header file
1.len function syntax len(string name)
2.slicing stringname[start:stop:step]
slicing is done only upto stop,it doesn't include stop
3.slicing str[:7] 
represents starting from 0 position to 6 position print the string
4.slicing str[2:]
represents start from position 2 and prrint upto the last character
5.slicing str[:]
print whole string
6.str.find('a')
find function: find the character 'a', if it is present in the string or not,if it is present it returns its position in the string else returns -1.
7.str.find('sai') we can use substring too
8.str.upper() ,mean captailising all the small leters in the string..
9.str.lower(),mean converting small letters to captial in the string..
10. str.lstrip() ,mean removing the left space in the string
suppose str='  saisri angajala  '
print(str.lstrip()) prints 'saisri angajala  ',it removes left space in string
11.str.rstrip() ,mean removing the right space in the string
suppose str='  saisri angajala  '
print(str.rstrip()) prints '  saisri angajala',it removes right space in string
12. str.strip()
mean removes both the right and left space in the string..
13. str.replace('saisri' ,'yamuna')
suppose str='saisri angajala' ,replace function replaces the word or character with the given one.. so output would be yamuna angajala
14.indexing concept is same in case of strings in c language..
15.strings are immutable (that mean we cannot change any character in the string)
16.string.title() makes the starting letter of the string Capital..
IMPORTANT NOTE :str() is a empty string like list() {empty list} ,tuple{empty tuple} 
we can reverse the string by slicing [: : -1]
Captailise func 
it is used to captailise the first letter of the string..
title()
is used to captailise the all first letters of word in the string..
# In[16]:


#useful methods for revesing a string..
#1.slicing
string = "saiSri angajala"
print(string[::-1]) #slicing method
print("".join(reversed(string))) #reversed method
for i in range(len(string)-1 , -1, -1) :
    print(string[i],end="") #for loop method.
print('\n')
string1 = list(string)
string1.reverse
rev_string = "".join(string1)
print(rev_string)   #list reverse method...
print(string.title())
print(string.capitalize())


# In[1]:


name=' saisri Angajala '
print(name.upper())
print(name.lower())
print(name.find('a'))
print(name[:])
print(name[::2])
print(name.replace('saisri' , 'Yamuna'))
print(len(name))
print(name.rstrip())
print(name.lstrip())
print(name.strip())
print('saisri' in name)#checking whether the substring is present in the string or not..
print('Angajala' not in name )
print(name[::-1])


# #programm to reverse a string
# suppose string is 'sai sri angajala' upon reversing it would become 'angajala sri sai'
# this can be obtained by performing split,reverse and join operations 
# 1.first step is to follow is ,take the required string and split it using split function
# 2.reverse operation is valid on the lists ,so reverse the list obtained after spliiting
# 3.now join the words in the list using join method 
# IMportant NOTE :
# join method ex : ' '.join('hello' ,'saisri') output would be hello saisri(see that they are joined by whitespace)
#             ex2 : ' k '.join('hello','world') output is hello k world (joined by k)def string_reverse(string) :
#     

# In[3]:


def string_reverse(string) :
    string1 = string.split()
    string1.reverse()#note reverse function doesn't return anyting
    string2 = " ".join(string1)
    print(string1)
    print(string2)

string = input('enter the string : ')
reverse_string = string_reverse(string)


# In[2]:


name='saisri Angajala'
if 'a' in name :
    print('character found!')
else :
    print('character not found!')
    


# lists, tuples,dictonaries are some datastructures in the python
# lists are muttable,that mean the elements of the list can be changed..
# strings are immutable..
# lists can contain various data types like strings,floats,integers..
# slicing and indexing are also possible in the list,there can be lists inside the list..
# functions in the list 
# 1.len(list) find the length of the list..
# 2.sum(list) adds up all the elements of the list..
# 3.list.append(data type) append function adds the new datatype at the end of the list..
# 4.list.sort() sort function sorts the data ,whether it is numerical data or characters based on alphabetical order..
# 5.max(list) find maximum of the list
# 6.min(list) find minimum of the list..
# important : 
#   list() function is nothing but the empty list 
#   mylist=list().. 
#   mean mylist =[]
#   by appending function we can add elements into the list and can perform operations on it ,same as array in the C languagge
# 7.list.remove() remove function is used to remove a particular number from the list.. 
# 8.we can add  any elements of list by using extend function list.extend([1,2,3])
# 
# 
#   

# In[5]:


#list operations :
s=[-1,2,3,1,99,100,32]
a=[10,11,12]
print(s+a)  #adding the lists
print(s[0] ,s[1],s[2])   #Accessing the elements of the list by indexing..
print(s[1:4])  # Accessing the elements by slicing.
s[2]=4 # muting the lists, because lists are mutable unlike the lists and tuples..
s[2]=[2,3,4] #nested lists..
print(s) 
print(s[2][1]) #Accessing the elements from the nested list
s.remove(s[2])  #removing the elements of the list by remove function
print(s)
s.sort() #sorting the list using sort function
print(s)
s.append(89)
print(s) #Adding the single element using append function at the last of the list..
s.extend([12,13,14]) #adding multiple elements at atime using extend function to list at last..
print(s)
print(len(s))
print(sum(s))
print(max(s))
print(min(s))


# In[7]:


#Accessing the elements of list using for loop
s=[1,2,3,4,5]
for i in s :
    print(i)
s=['saisri','angajala' ,'yamuna','sroinivasarao','anuradha']
for  i in s :
    print(i)    
    


# Escape characters :
# suppose if we want the double quotes in the string ,then 'Saisri "Angajala"' woulb be our choice ,if we do not want to use the
# single quotes,then escape characters coe into picture..
# it is represented by '\', suppose 'saisri \"Angajala\" ' output is saisri "Angajala",because escape characters allows the next 
# character to it print ,by without printing itselff

# In[8]:



course="Saisri \"Angajala\" "
print(course)


# Formatted strings :
# first_Name='Saisri'
# last_Name='Angajala'
# suppose for concatinating the both the strings we use Full_Nmae=first_Name+" " +last_Name
# but we can use formatted strings to do the same 
# f"{first_Name} {last_Name}"
# also prints the same,the info in the culy braces can be anything...

# In[2]:


#Formatted strings
first_Name='Saisri'
last_Name='Angajala'
full_Name=first_Name +" " +last_Name
print(full_Name)
fullname=f"{first_Name} {last_Name}"
print(fullname)
fullname=f"{first_Name}{last_Name}"
print(fullname)
fullname=F"{first_Name} {last_Name}"
print(fullname)


# #numbers 
# integers
# floats
# complex numbers 
# usally complex numbers are represented in the form a+ib weresas in he python they are represented as a+bj
# x+=3 argumented arguments
# useful functions in numbers 
# round:rounds the number
# abs : absolute function like modulus operator,which converts negative to +ve

# In[10]:


print(10//3) #Actual division with single slash gives the float value ,whereas if we use // it will give the integer quotient
print(10/3)
print(round(3.8888899999999999999))
print(abs(-2.3455))


# Boolen NOTE: ""(Empty string),0,None returns the False everything else returnS True...
# 

# In[4]:


count = 0
for i in range(1,10) :
    if i%2 == 0 :
        print(i)
        count+=1
print(f"there are {count} even numbers")        


# Comparision operators:
# >
# <
# <=
# >=
# ==
# !=
# 

# In[13]:


print(10>3)
print(2>=3)
print('saisri' < 'Angajala')


# In[3]:


#Ternary operators 
age=22
if age >= 18 :
    print('eligible')
else :
    print('Not eligible')
#we  can whole if else loop in a single line of code 
message='eligible' if age >= 18 else 'in eligible' #this is like simple english languge
print(message)


# #logical operators 
# and, 
# or ,
# not ,are called the logical operators..
# 

# In[9]:


Grade='A'
credits=3
if Grade == 'A' and credits == 3 :
    print('Pass')
else :
    print('fail')
#and operator returns the boolen True if the all the conditions in the conditional statements are true..
age = 17
if age >= 18 or age >= 16 :
    print('Eligible')
else :
    print('Not eligible')
#or operator retrns the boolean True if any one of the condition is true..
name='saisri angajala'
if 'saisri' not in name :
    print('not a substring')
else :
    print('substring')


# chaining comparision operators :
# suppose let us take a example ,that if a man is eligible for the interview if he was b/w age 18 and 65
# 

# In[2]:


#code for chaining operators :
age=22
if age >= 18 and age < 65 :
    print('Eligible')
else :
    print('Ineligible')
#we can write the piece of code in the below way too
if 18 <= age < 65 : #<---- this is chaining operators
    print('Eligible')
else :
    print('Ineligible')
    


# range function 
# syntax is range(starting from,ending,jump)
# note that In range ending value is not counted 
# suppose range(1,10) it will iterates from 1 to 9 
# suppose range(3) ,by default it will set the starting =0,and step=1 if they are not mentioned ,so this will print 0 ,1,2
# 

# In[12]:


for i in range(1,11,2) :
    print(i)


# functions 
# functions are the most significant concept in the any programming language 
# def function name (arguments ) : #syntax for defining the functions
# here def is keyword indicating that we are defining the function,return statement is optional
#     
#     

# In[2]:


#function to check even number is part of the list or not 
def even_check(list2) :
    for number in list2 :
        if number % 2 == 0 :
            return 'found'
        else :
            pass #passs mean 'do nothing'

list1=[1,2,3,4,5]
result = even_check(list1)
print(result)
#Important note :
#function terminates once it encountered the return statement


# In[3]:


def even_check(list2) :
    for number in list2 :
        if number % 2 == 0 :
            return 'found'
        else :
            return 'not found'

list1=[1,2,3,4,5]
result = even_check(list1)
print(result)
# the result is not found,even though there is a even in the list because ,first function execution gets started,as first 
#element of the list is odd,if loop terminates and else will execute,as it encountered the return statement it returs the vallue
#and terminates the function execution,so the remaining elements are not even checked..


# In[4]:


#returning the multiple values from function
def even_numbers_list (list1) :
    even_list = list()
    for number in list1 :
        if number % 2 == 0 :
            even_list.append(number)
        else :
            pass
    return even_list 
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = even_numbers_list(list1)
print(list2)


# In[5]:


#unpacking the tuple :
#finding the employee of the year problem
def employe_of_year(list2) :
    employee = ''
    working_hours = 0
    for employe ,hours in list2 :
        if hours > working_hours :
            working_hours = hours
            employee = employe
    return  (employee,working_hours) #returning tuple  
list1 = [('saisri',400),('yamuna',2000),('anuradha',3000)]
employee = employe_of_year(list1)
print(employee) # or we can seperate employee name and working hours from tuple too
employee,hours = employe_of_year(list1) #assinging employee name to employee variable and working hours to hours variable
print(employee)
print(hours)
print(f"employee of the year is {employee} ,he worked for {hours} hours : ")


# In[6]:


#shuffling game 
from random import shuffle
list1 = [1,3,4,6,7,2,8]
shuffle(list1)
print(list1) #shuffle in the random module shuffles the list,it does not return anything,it modifis the original list itself


# In[17]:


#shuffle game 
from random import shuffle
def shuffling(list1) :
    shuffle(list1)
    return list1
def guess_by_player() :
    guess = input('PLZ enter your choice : ' )
    while int(guess) not in [0,1,2] :
         guess = input('PLZ choose a valid option : ' )
    return int(guess)
def cross_checking_guess(list1,guess) :
    if list1[guess] == 'O' :
        print('YOU WON!.....')
    else :
        print('SORRY YOU LOST,PLZ TRY AGAIN .... ')
        
list1 = ['','O','']
shuffled_list = shuffling(list1)
player_guess = guess_by_player()
cross_checking_guess(shuffled_list,player_guess)
print(shuffled_list)


# *args(shorcut of arguments) ,**kwargs(shortcut of keyword arguments)
# *args returns the tuple,where as the **kwargs returns the dictonary..

# In[3]:


#code describing the *args and **kwargs
def my_function(*args) :
    print(args)
    sum1=sum(args)#summing the all the arguments..
    print(sum1)
my_function(10,20,30,40,50)   #so we can pass any number of arguments,and can do operations on it 


# In[4]:


def my_function(**kwargs) :
    print(kwargs)
my_function(fruit = 23 ,orange = 35, banana = 42)  #so it takes the arguments and makes the dictoonary out of it.. 


# In[6]:


#we can pass arguments to make tuple and dictonary using same function
def my_function(*args, **kwargs) :
    print(args)
    print(kwargs)
my_function(10,20,30,40,saisri = 23, yamuna = 78, anuradha = 'angajala')    


# In[19]:


def two_word_string(string) :
    string1 = string.split()
    if len(string1) is not 2 :
        print('Plz enter a two word string only : ' )
    else :
        if string1[0][0] is string1[1][0] :
            return True
        else :
            return False
string = input('Enter a two word string : ')
result = two_word_string(string)
if result is None :
    pass
else :
    print(result)


# #dictonaries 
# dictonaries are used for locating the value exactly without using the indexing concept..
# syntax is {'key1' : value1, 'key2' :value2, 'key3' :value3}
# note that key value in the dictonaries are must be strings,values may be any datatype...
# NOTE :dictonary is unorderd unlike the list,we cannot access the elements in the same sequence as we entered...
# if we run the for loop over the dict by default we get only key values : 
# we can access either only keys or values by following dictonary.keys() or dictonary.values()
# by using dictonary.items() function we can access both the keys and values
# 

# In[7]:


dicton = {'key1' :2 , 'key2' : 3, 'key3' :4}
print(dicton['key1'])
#elements are accessed by using the key values
for item in dicton :
    print(item)
for item in dicton.keys() :
    print(item)
for item in dicton.values() :
    print(item)
for keys , values in dicton.items():
    print(keys ,values)


# sets is anotehr type data structure in python,it is similar to tuple but it contains only unique elementts 
# synax for sets is set = {1,2,3}
# we caonvert list into set or set into list..
# set() gives the empty set like dict() list() str()
# we can add elements to set by .add() like .append() in list..
# sets are immutable,if we want to perform operations convert it into list perform operstion and convert back to set again

# In[18]:


sets ={1,2,3,4,5}
for i in sets :
    print(i)
lists = [1,2,2,3,3,4,5,5,5,5,66,6,6,7,7,7]
set1 =set(lists)#while converting into set it omitted the duplicarte elements
print(set1)
set2 = set()
for i in range(0,11) :
    set2.add(i)
print(set2)


# #useful functions in pyhton 
# 1.range()
# 2.zip()
# 3.enumerate()
# 4.input()
# ENUMERATE :is used to access the elements with its index value ,they are like tuples,we can access them indivdually by tuple unpacking method..it can apply on anything like list ,string,dctonary.. 

# In[30]:


string = 'saisri'
for character in enumerate(string):
    print(character)
mylist = [i for i in range(11,21)] #list compression
for i in enumerate(mylist) :
    print(i)
# unpacking the tuple 
for index ,value in enumerate(mylist) :
    print(f'index is {index} and its value is {value}')#formatted string way1 
#for dictonary
dicton = {'key1' :2 , 'key2' : 3, 'key3' :4}
for key ,value in enumerate(dicton) :
    print('key is {} and value is {}'.format(key ,value))#formatted sring way2


# zip is used to concatenate the two lists in the form of tuple ..
# we can also do tuple unpacking...

# In[35]:


list1 = ['a' ,'b','c', 'd']
list2 =[1,2,3,4]
list3 = [2,4,5,6]
for item in zip(list1,list2):#syntax is zip(list1,list2)
    print(item)#we can use any number of lists
print('\n')    
for item in zip(list1,list2,list3):
    print(item)
#if the elements are more in any one of the list it takes only the elemnts in shortest list..
print('\n')
list1 = ['a' ,'b','c', 'd']
list2 =[1,2,3,4,5,6,7]
list3 = [2,4,5,6,5]
for item in zip(list1,list2,list3): #as here shortest i.e list1 has 4 elements so output would be also 4 tuples,it omitss rest
    print(item)


# OBJECT ORIENTED PROGRAMMING:
# we have some methods in lists ,dictonaries,tuples etc like append ,sort,in lists..add in tuples etc..
# we can also create our own methods and attributes,that is known as Oject Orieted Programming(OOP) ..it has much scope in the 
# future..
# let us look how can we create our own methods and attributess..
# 
# 

# In[7]:


#syntax for creating
class dog() :
    def __init__(self,breed,name,age) : #init mean instance..
        self.breed = breed  #----->
        self.name = name    #-----> these are all user_defined attributes
        self.age = age      #----->
dog_details = dog('lab','frankie' ,10)
print(dog_details.age)
print(dog_details.breed)
print(dog_details.name)
#when we hit the tab button after the variable(dog_details here) wewould see list of attributes and methods ..
# note there are 2 underscores before and after init
#here attributes are breed name &age ,see self.breed = breed (note what we defined in self.something would become attribute but
# after the = one suppose self.mybreed = breed,here mybreed would be an attributor but  not breed)
#there are2 tyoes of attributes,one is class defined and another is user defined attributes,class defined attributes do not 
#require self keyword for determining,and they are unique to class


# In[9]:


#class attributes and methods..methods aare nothing but functions in class,we use append(),sort() etc 
#tehy are pre defined methods in the list class,nothing but functions that do specific tasks when we apply on list varible..
class dog() :
    owner = 'saisri' #---->this is class attribute..
    def __init__(self,breed,name,age) : #init mean instance..
        self.breed = breed  #----->
        self.name = name    #-----> these are all user_defined attributes
        self.age = age      #----->
    #methods in class
    def bark(self) : #self is must and should inorder to identify it as attribute or method..see we defined method bark as func 
        print('dog barks wooff!!!')
dog_details = dog('lab','frankie' ,10)
print(dog_details.age)
print(dog_details.breed)  #Atributes
print(dog_details.name)
dog_details.bark()  #Method ,note the difference..
#the difference b/w attribute and method is method includes braces like list.sort() ,list.append(),
#whereas attributes did n't..



# In[11]:


# we can also use user_defined & class attributes in methods..
class dog() :
    owner = 'saisri' #---->this is class attribute..
    def __init__(self,breed,name,age) : #init mean instance..
        self.breed = breed  #----->
        self.name = name    #-----> these are all user_defined attributes
        self.age = age      #----->
    #methods in class
    def bark(self) : #self is must and should inorder to identify it as attribute or method..see we defined method bark as func 
        print(f"dog name is {self.name} ,it's breed is {self.breed} it's age is {self.age} ")
        print("it's owner is {}".format(self.owner))
#Note we have used attributes in the method.. 
dog_details = dog('lab','frankie' ,10)
print(dog_details.age)
print(dog_details.breed)  #Atributes
print(dog_details.name)
dog_details.bark() 


# In[18]:


#Inheritence in OOP..It mean calling one class into another class ,and using that class attributes and methods...
class Animal() :
     
        def __init__(self ,gender = 'male',spots = 'no') :
            self.gender = gender
            self.spots = spots
        def  speak(self) :
            print("every animal has it's unique way of expresing" )
class dog() :
      
        def __init__(self,breed='lab',name='farnkie',age = '10') :
               
                self.breed = breed
                self.name = name
                self.age = age
        def bark(self) :
                print('dog barks wofff')
dog_details = dog()
dog_details.spots
#when we try to access spots attribute which  is not in dog it is showing error,we can get 
#that attribute into dog class by inheritence


# In[2]:


class Animal() :
     
        def __init__(self ,gender = 'male',spots = 'no') :
            self.gender = gender
            self.spots = spots
        def  speak(self) :
            print("every animal has it's unique way of expresing" )
        def who_am_i(self) :
            print('I am an animal..')
class dog(Animal) : #-->inherting 1
      
        def __init__(self,breed='lab',name='farnkie',age = '10') :
                Animal.__init__(self)#  inherting the  base class (see syntax [class name.__init__(self)])
                self.breed = breed
                self.name = name
                self.age = age
        def bark(self) :
                print('dog barks wofff')
dog_details = dog()
print(dog_details.gender)
print(dog_details.spots)  #Attributes of base class
print(dog_details.age)
print(dog_details.breed)  #Atributes of sub class 
print(dog_details.name)
dog_details.bark()
dog_details.speak() #if you press tab here you can see attributes & methods which are in both animal & dog class 
#so we can get attributes from another class to without defining here...


# In[3]:


#We can change the methods in one class by inherting...
class Animal() :
     
        def __init__(self ,gender = 'male',spots = 'no') :
            self.gender = gender
            self.spots = spots
        def  speak(self) :
            print("every animal has it's unique way of expresing" )
        def who_am_i(self) :
            print('I am an animal..')
class dog(Animal) : #-->inherting 1
      
        def __init__(self,breed='lab',name='farnkie',age = '10') :
                Animal.__init__(self)#  inherting the  base class (see syntax [class name.__init__(self)])
                self.breed = breed
                self.name = name
                self.age = age
        def bark(self) :
                print('dog barks wofff')
dog_details = dog()
print(dog_details.gender)
print(dog_details.spots)  #Attributes of base class
print(dog_details.age)
print(dog_details.breed)  #Atributes of sub class 
print(dog_details.name)
dog_details.bark()
dog_details.speak() 
dog_details.who_am_i() #see here output is animal


# In[6]:


class Animal() :
     
        def __init__(self ,gender = 'male',spots = 'no') :
            self.gender = gender
            self.spots = spots
        def  speak(self) :
            print("every animal has it's unique way of expresing" )
        def who_am_i(self) :
            print('I am an animal..')
class dog(Animal) : #-->inherting 1
      
        def __init__(self,breed='lab',name='farnkie',age = '10') :
                Animal.__init__(self)#  inherting the  base class (see syntax [class name.__init__(self)])
                self.breed = breed
                self.name = name
                self.age = age
        def bark(self) :
                print('dog barks wofff')
        def who_am_i(self) :
            print("i am a dog")
dog_details = dog()
print(dog_details.gender)
print(dog_details.spots)  #Attributes of base class
print(dog_details.age)
print(dog_details.breed)  #Atributes of sub class 
print(dog_details.name)
dog_details.bark()
dog_details.speak() 
dog_details.who_am_i() #see here output is dog.. ,but it doesn't change in base class
ani =Animal()
ani.who_am_i() # see here in base class ,still output is animal..plz be causious..


# In[7]:


class book() :
    def __init__(self,book = 'python' ,author = 'saisri' ,pages = 200 ) :
        self.book = book
        self.author = author
        self.pages = pages 
b = book()
print(b) #it shows it's location..
#print function checks for string,if it has string type it prints ,else shows location..so we should convert class into str


# In[1]:


class book() :
    def __init__(self,book = 'python' ,author = 'saisri' ,pages = 200 ) :
        self.book = book
        self.author = author
        self.pages = pages 
    def __str__(self) :  #converting to string type..
        return f'book name is {self.book} ,author is {self.author}'
    def __len__(self) :
        return self.pages
b = book()
print(b) #print function .. in this way onlypre defined functions like print(),max(),min(),len() are created.. for diffrent 
#clsses like lists,strings,dictonaries...
len(b)#len function
#in the str function we should


# In[1]:


#lamba functions or Anynonmus functions
#lambda func or functions which does not use def keyword
#they are single line functions
#they return expression but not values.
#they cannot access the global variables..
#syntax is (lambda arguments : expression ) argum can be any number,but expression should be only one...
sum = lambda x,y : x+y
print(sum(2,3))


# In[8]:


#map function 
#map func is used when we want to apply a function on all the elements in iterables(iterables are nothing but which can loop,ex:
#lisst,tuple,string)
#syntax is map(function,iterable)
def add(x,y) :
    return x+y
list1 = [1,2,3,4]
list2 = [4,5,6,7]
l = list(map(add,list1,list2))
print(l)
#square 
def square(x) :
    return x*x
ls = list(map(square,list1))#square is a function ,and list1 is iterable,so using map we cal square of every element
print(ls)
st = 'saisri'
p= list(map(lambda x : x.upper(),st)) #here we used lambada and map function to captailise every char in str...
print(p)
#if we not use list map will return the address of the object..


# In[15]:


#filter func
#syntsx is filter(func,iterable)
#filter func returns value when func applied on elements is true..
list1 = [x for x in range(10)] #list compression
even= tuple(filter(lambda x : x % 2 == 0,list1))
print(even)
s= list(filter(lambda x : x >2 ,list1)) #func is true only fro nums above 2
print(s)
s= list(filter(lambda x : x  ,list1)) #here the func is always true..so it returns all the values..
print(s)


# In[12]:


#overview of decorators in python..
#suppose there is a func ,if we wnat to add something to that func,we should modify it,after if we need no modification,we 
#again overwrite it and get original func back,decoratores is a concept which we would perform odifying functions
#actually not distribuing the original func...

#basics concepts required fro entering into decorators

# 1.assinging function to a variable!!
def hello() :
    return 'Hello'
var = hello #copying the hello func to variable var 
var() #calling func 
del hello #deleting the hello func
var()



# In[10]:


del hello #deleting the hello func
hello() #if we now call the func ,it shows func is not defined..


# In[13]:


var() #if we call the var it works as actual func


# In[14]:


#2.function inside a func
def bank(name= 'canara') :
    print('welcome to the canara bank!! ')
    def customer(name = 'saisri') :
        return f'customer is {name} : '
    
    def balance(amount) :
        return f'balance left is {amount} '
    return 'canara bank welcomes you!!!'
    


# In[15]:


bank() #if we call the bank we can acess the data 


# In[16]:


customer() #if we call customer we would get error that ,func is not defined,because it is inside the bank func


# In[17]:


balance() #same with balance func


# In[21]:


def bank(name= 'canara') :
    print('welcome to the canara bank!! ')
    def customer(name = 'saisri') :
        return f'\t customer is {name} : '
    print(customer()) #calling the customer func
    def balance(amount) :
        return f'\t balance left is {amount} '
    print(balance(4000)) #calling the balance func
    return 'canara bank welcomes you!!!'


# In[24]:


bank() #


# In[29]:


# 3.passing func as argument : 
def myfamily(me) : #calling func me as an argument in fun myfamily 
    print('these are my family info :')
    me()
    def my_father(name= 'srinivas') :
        return f'my father is   {name} '
    print(my_father())
    def my_mother(name= 'anuradha' ) :
        return f'my mother is {name} '
    print(my_mother())
   
    def my_sis(name='yamuna') :
        return f'my sister is {name} '
    print(my_sis())
def me() : # a seprate func 
    print('i am saisri :')
myfamily(me)    #passing only location of me func.but not calling it like myfamily(me())


# In[31]:


def decorater(actual_func) :
    print('additonal code or decorator  before the actual code!!!!')
    actual_func()
    print('additonal code or  decorator after the actual code!!!!')
def actual_func() :
    print('my actual code.. ')
decorater(actual_func)  
#this is description of decorator ,we are not modifing the func actual_func , and wwe added extra info it ..
#this is nothing but decorating the actual_func,this is decorator in py..this can be achieved by simply writing @decorating fun
#over actual func


# In[32]:


def decorater(actual_func) :
    print('additonal code or decorator  before the actual code!!!!')
    actual_func()
    print('additonal code or  decorator after the actual code!!!!')
@decorater  #here we need not to call the decorater func,and pass actual func as argument to it.. if yu don't need to modify
#just make @ line as comment..your actul_func will be same as original one.e.... 

def actual_func() :
    print('my actual code.. ')


# #generators in python..
# #consider range function range() ,it is an gen,because it generates the numbres,it is not consuming memory,it only remembers 
# #what is next and next ,so memory allocation does n't happens..
# #suppose if we want to calclate the squares o 1 milllion numbers,if we take a list and append squares to it it will consume alot of space,instead if we use generator they only remember,them in sequence,if we iterate through them we can get the aquares without using any memory..
# it is done by yield keyword...
# 

# In[1]:


def squares() :
    squ = []
    for num in range(10) :
        squ.append(num**2)
    return squ
square = squares()
print(square) #this consumes the space...


# In[2]:


#same can be done by using gen,which does not consume space
def squares() :
    for num in range(10) :
        yield num**2  #
for num in squares() : #givessame result...
    print(num)  #yields the numbers one by one...


# In[3]:


#next func  in gen
sq= squares()
next(sq)


# In[4]:


next(sq) #it returns the num thast it remembers in sequence


# In[5]:


next(sq)


# In[6]:


#iter func in gen
s = 'saisri'
#we know that str is iterable,if we want to convert into itrerator we should use iter func
next(s) #nexxt func does gives error beccause,string is not a geneartor,so to convert into gen we use iter() func


# In[8]:


a= iter(s)
next(a)


# In[9]:


next(a) #now a is a generator...


# In[11]:


#generator compression :,it is similar to list compresion
mylist = [x for x in range(10)] #here we use brack
gencomp = (item for item in mylist if item > 3) #here we use parenthesis
print(gencomp) #it gives the address ,because it is not the list or something else,it is gen,so we should iterate through 
#to it inorder to grab the content..
for item in gencomp :
    print(item)


# In[1]:


#erors and handling..
#try and except ,else ,finally method..
def add(a,b) :
    return a+b
add(1,2)
#here we don't have any errors because,adding 2 ints is possible..


# In[2]:


def add(a,b) :
    return a+b
add(1,'2')
#it gives an error becauses addition of ints & str are not feasible..we can overcome this by try and except method..


# In[4]:


def square() :
    a = int(input('enter the number\n'))
    return a**2
square() #here is no error
#if we provide any another datatype ,other than int it would give error.


# In[6]:


def square() :
    try :
        a = int(input('enter the number\n'))
        print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
    except :
        print('sorry!! you entered wrong data type.. ')
        #if there is a error in try block ,except will excute..
square() #as here sai is str,which annot be squared,so it gives error


# In[7]:


def square() :
    try :
        a = int(input('enter the number\n'))
        print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
    except :
        print('sorry!! you entered wrong data type.. ')
        #if there is a error in try block ,except will excute..
    else :
        print('successfully executed!!') #else block excutes when there is no error..
square()


# In[8]:


def square() :
    try :
        a = int(input('enter the number\n'))
        print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
    except :
        print('sorry!! you entered wrong data type.. ')
        #if there is a error in try block ,except will excute..
    else :
        print('successfully executed!!') #else block excutes when there is no error..
square()#as here is input is str,so its an error...


# In[9]:


#finally statemnt ,will always excutes ,regrardless of error..
def square() :
    try :
        a = int(input('enter the number\n'))
        print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
    except :
        print('sorry!! you entered wrong data type.. ')
        #if there is a error in try block ,except will excute..
    else :
        print('successfully executed!!') #else block excutes when there is no error..
    finally :
        print('i always run,regardless of error...') #here is error,even though it excuted..
square()


# In[10]:


def square() :
    try :
        a = int(input('enter the number\n'))
        print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
    except :
        print('sorry!! you entered wrong data type.. ')
        #if there is a error in try block ,except will excute..
    else :
        print('successfully executed!!') #else block excutes when there is no error..
    finally :
        print('i always run,regardless of error...') #here is no error,even though it excuted..
square()


# In[13]:


#continously asking..
def square() :
    while True :
        try :
            a = int(input('enter the number\n'))
            print(f'square of num is {a**2}') #if there is no error in try block,it will execute and except block would terminate..
        except :
            print('sorry!! you entered wrong data type.. ')
            #if there is a error in try block ,except will excute..
            continue #if there is error,it will go top and again run try block,and asks for inputt..
        else :
            print('successfully executed!!') #else block excutes when there is no error..
            break  #when there is no error,we will come out of the loop 
square()             


# In[ ]:




