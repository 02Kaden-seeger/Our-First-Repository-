
#2.13.3: Greeting
#Kaden Seeger
#2/6/19


name = input("What is your name:")

def greeting():
    print("Hi there " + name + "!")
    print( "nice to meet you ")
greeting()


#4.13.4: Functions and variables '
#Kaden Seeger
#2.14.19


x = 11

def print_somthing():
    x = 13
    print(x)
print_somthing()
print(x)



#4.13.6: Functions & Variables, Part 3
# Kaden Seeger
#2.18.19


def print_num(x):
    print(str(x))
print_num(12)
print_num('\n' + 'Hello World')

#4.14.4: Name & Age
# Kaden Seeger
#2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is ', name, '\n', 'I am ',  str(age), ' year(s) old!')
name_and_age('Kaden Seeger', 8)
name_and_age('Tyson Watson', 4)
name_and_age('Lucas Simpson',2)

#4.13.6: Functions & Variables, Part 3
# Kaden Seeger
#2.18.19


def print_num(x):
    print(str(x))
print_num(12)
print_num('\n' + 'Hello World')


#4.14.4: Name & Age
# Kaden Seeger
#2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is ', name, '\n', 'I am ',  str(age), ' year(s) old!')
name_and_age('Kaden Seeger', 8)
name_and_age('Tyson Watson', 4)
name_and_age('Lucas Simpson',2)


# 4.14.5: Default Parameter values
# Kaden Seeger
#2.19.19

def print_two_num(x, y= 20):
    print('First number: ', x, )
    print('Second number: ', y, '\n')

print_two_num(2, 87)
print_two_num(54)


#4.14.7: Print multiple times
# Kaden Seeger
#2.19.18

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello', 14)

<<<<<<< HEAD
<<<<<<< HEAD




#4.16.4: Name & Age
#Kaden Seeger
#2.20.19

name = input('What is your name: ')
age = -1
try:
    age = int(input('Enter your age: '))
except ValueError:
    print('That was not a good one.')


print('\n''Name:', name)
print('age:', age)
>>>>>>> Enter-Name-And-Age
=======
#4.16.6: Temp converter
#Kaden Seeger
#2.20.19

def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32) / 1.8

try:
    c = float(input('Enter a temp in  C:'))
    print('In F:', round(celcius_to_fahrenheit(c)), 2)

    f = float(input('Enter a temp in  F:'))
    print('In C:', round(fahrenheit_to_celcius(f)), 2)

except ValueError:
    print('wHOoPS you did that wrong')


    
>>>>>>> Temp-converter
