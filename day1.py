print('Hello World') #print() method helps to print something to the console
print(1+2) #output will be 3 because adding 1+2 = 3
print(87.0+12.3) #float addition 99.3
val=input("What is your name ?") #defaultly input() will take string
number=int('34')#if we provide string in int() then it will automatically convert to integer
n1=int(input("What is your roll number ?"))
var=True
print(var)#output will be True because it is a boolean value
print(0<10) #output: True
print(0>10) #output :False

42==42.0 #Output : True
42=='42' #output: False


var1=11
print(var1<10 or var1>0) #output will be True because it is OR operator  there are and or not operator are there.

#Flow Control
newval=11
if newval>0:
  if newval==11:
    print("Same value)

n=int(input("enter n"))
if n>0:
 if n>=10 and n<40:
     print('c')
 elif n>=40 and n<80:
     print('B')
 elif n>=80 and n<=100:
    print('A')
 else:print('Fail')

n1=122
if n1>0:
    print('Positive')
    if n1%2==0:
        print("EVEN")

 num=11
if num<=10:
    print("Good")
else:
    print("Bad")

# if vs elif

#if
n=95
if n>=20:
  print('D')
if n>=40:
  print('C')
if n>=60:
  print('B')
if n>=80:
  print('A')
if n>=90:
  print('O')
else:
  print('False');

#output:   
D
C
B
A
O

#elif
n=95
if n>=20:
  print('D')
elif n>=40:
  print('C')
elif n>=60:
  print('B')
elif n>=80:
  print('A')
elif n>=90:
  print('O')
else:
  print('False');

#output:
D
