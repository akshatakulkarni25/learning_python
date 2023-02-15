# Loops in Python
# for loop
# while loop



fruits= ['Apple','Banana','Chikoo','Dragonfruit']
for fruit in fruits:
    print(fruit)

#range function
#prints numbers from 1 to 100 (101 is not included)(for loop in python is similar to for(i=1;i<101;i++) print(i);)
for i in range(1,101):   
    print(i)

#range function case2
#range(start,end,step)
for i in range(2,101,2):
    print(i)

# FizzBuzz Interview Question
# print Fizz if number is divisible by 3. print Buzz if number if divisible by 5 
# and print FizzBuzz if number is divisible by both 3 and 5

for number in range(1,101):
    if(number%3 == 0 and number%5 == 0):
        print("FizzBuzz")
    elif (number%3 == 0):
        print("Fizz")
    elif (number%5 == 0):
        print("Buzz")
    else:
        print(number)