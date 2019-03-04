
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

