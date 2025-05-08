print("Hello , worlddd!")
print()
print("Hello, Python!")
print(123)
print("In python for integers or literals we do not need quotes to declare a variable")
print("this is a number",12345)
print(2)
print("2")
print("integers without quotes:" + " '3 + 5'")
print(3 + 5)
print("integers with quotes:" + ' "5 + 3"')
print("5" + "3")
print("I like \"Monty Python\"")
print("I\'m Monty Python")
print()


a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print()

john = 3
mary = 4
adam = 7
print(mary, john, adam)
john_mary = john + mary
print(john_mary)
john_adam = john + adam
mary_adam = mary + adam
total_apples = john + mary + adam
print("The total of apples is:", total_apples)
print()

kilometers = 32.25
miles = 17.38

print("Kilometers:", kilometers)
print("Miles:",miles)

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print()

# comments
#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")
#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour
