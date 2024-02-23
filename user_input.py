def user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))  
    location = input("What is your location? ")
    print(f"Hi {name}, you are {age} years old and live in {location}.")

user_input()