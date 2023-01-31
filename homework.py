
#Exercise #1

#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

number_cubed = 0
while True:
    cubed = number_cubed ** 3
    if cubed <= 1000:
        number_cubed += 1
        print(cubed)
    else:
        False  





#Exercise #2

#Get first prime numbers up to 100

for number in range(2,100):
    if number == 2 or number == 3 or number == 5 or number == 7:
        print(number) 
    elif number % 2 != 0:
        if number % 3 != 0:
            if number % 5 != 0:
                if number % 7 != 0:
                    print(number)
    

    
#Exercise 3

#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

user_age = input("What is your age?: ")
user_age = int(user_age)

if user_age <= 17:
    print("kids")
elif user_age >= 18 and user_age <= 65:
    print("adults")
else:
    print("seniors")