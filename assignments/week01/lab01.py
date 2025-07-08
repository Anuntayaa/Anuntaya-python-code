# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
full_name = input("what is your name? :")
age  = input("How old are you? :")
email = input("What is your email address? :")
phone_number = input("What is your phone number? :")
hobby = input("What is your favorite hobby? :")

print("=== Your Personal Profile  ===")
print(f'Hello, {full_name}')
print(f'Age : {age}')
print(f'Email : {email}')
print(f'Phone number : {phone_number}')
print(f'Your favorite hobby is : {hobby}')